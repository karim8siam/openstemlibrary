import json

# Unit 1: Zeroth and First Law of Thermodynamics
u1 = {
    "unitNumber": 1,
    "title": "Zeroth and First Law of Thermodynamics",
    "description": "Foundations of macroscopic thermodynamics: thermodynamic equilibrium, empirical temperature, state functions, work and heat energy, conservation of energy, Mayer's relation, and atmospheric adiabatic lapse rates.",
    "sections": [
        {
            "id": "u1-sec1",
            "title": "Thermodynamic Equilibrium & State Variables",
            "content": """
### 1. The Nature of Thermodynamic Systems

A **thermodynamic system** is defined as any macroscopic quantity of matter or radiation separated from the rest of the universe (the *surroundings*) by an identifiable real or hypothetical boundary. Thermodynamic systems are classified according to the permeability of their boundaries:
1. **Isolated Systems**: Exchange neither matter nor energy (heat or work) with surroundings (e.g., matter enclosed within an idealized rigid, non-radiating adiabatic vacuum chamber).
2. **Closed Systems**: Exchange energy with surroundings via mechanical work or heat conduction, but have boundaries impermeable to mass ($dN = 0$).
3. **Open Systems**: Exchange both energy and matter with their environment across permeable control surfaces.

### 2. Multi-Criteria Thermodynamic Equilibrium

For a macroscopic system to be in genuine **thermodynamic equilibrium**, three independent physical conditions must be satisfied simultaneously:
- **Thermal Equilibrium**: There exists no net heat exchange between any sub-regions within the system or across its boundary, implying uniform empirical temperature throughout ($T_A = T_B = \dots = T$).
- **Mechanical Equilibrium**: No unbalanced macroscopic forces exist within the system or at the boundary, ensuring uniform hydrostatic pressure ($P_A = P_B = \dots = P$) in the absence of external fields, or hydrostatic balance $\nabla P = \rho \vec{g}$ under gravitational fields.
- **Chemical Equilibrium**: No spontaneous chemical reactions or net diffusive species transport occur between phases, ensuring uniform chemical potentials ($\mu_i^{(A)} = \mu_i^{(B)} = \dots = \mu_i$) for every species $i$.

When all three conditions hold, the system's state remains invariant over time in the absence of external perturbations.

### 3. Intensive vs. Extensive State Coordinates

Thermodynamic state variables are categorized by their scaling behavior under spatial partitioning or scaling of total mass by a dimensionless scalar $\lambda$:
- **Extensive Variables**: Scale linearly with system size such that $X(\lambda N, \lambda V) = \lambda X(N, V)$. Examples include volume $V$, internal energy $U$, enthalpy $H$, entropy $S$, Helmholtz free energy $F$, and Gibbs free energy $G$.
- **Intensive Variables**: Invariant under system scaling such that $Y(\lambda N, \lambda V) = Y(N, V)$. Examples include temperature $T$, hydrostatic pressure $P$, chemical potential $\mu$, density $\rho = M/V$, and molar volumes $V_m = V/n$.

By Euler's theorem for homogeneous functions of degree 1, any fundamental extensive thermodynamic function, say $U(S, V, N_i)$, satisfies the exact relation:
$$U = S \left(\frac{\partial U}{\partial S}\right)_{V, N} + V \left(\frac{\partial U}{\partial V}\right)_{S, N} + \sum_i N_i \left(\frac{\partial U}{\partial N_i}\right)_{S, V} = T S - P V + \sum_i \mu_i N_i$$
            """
        },
        {
            "id": "u1-sec2",
            "title": "Zeroth Law of Thermodynamics & Empirical Temperature",
            "content": """
### 1. The Postulate of Thermal Transitivity

The **Zeroth Law of Thermodynamics** formalizes the operational and mathematical basis for the existence of temperature. Historically recognized after the First and Second Laws, Ralph H. Fowler in 1935 noted its logical priority:

$$\\text{If system } A \\text{ is in thermal equilibrium with system } C, \\text{ and system } B \\text{ is independently in thermal equilibrium with } C, \\text{ then system } A \\text{ is in thermal equilibrium with } B.$$

Mathematically, let the thermodynamic state of system $A$ be specified by coordinates $(P_A, V_A)$, system $B$ by $(P_B, V_B)$, and thermometer system $C$ by $(P_C, V_C)$. Thermal equilibrium between $A$ and $C$ establishes an implicit functional constraint:
$$f_{AC}(P_A, V_A; P_C, V_C) = 0$$
Solving for $P_C$:
$$P_C = \phi_A(P_A, V_A; V_C)$$
Similarly, thermal equilibrium between $B$ and $C$ requires:
$$P_C = \phi_B(P_B, V_B; V_C)$$
Equating both expressions yields:
$$\\phi_A(P_A, V_A; V_C) = \\phi_B(P_B, V_B; V_C)$$

The Zeroth Law asserts that thermal equilibrium between $A$ and $B$ depends strictly on coordinates $(P_A, V_A)$ and $(P_B, V_B)$ without reference to the arbitrary coordinates $V_C$ of the intermediary. Hence, the parameter $V_C$ must factor out algebraically:
$$\\theta_A(P_A, V_A) = \\theta_B(P_B, V_B)$$

### 2. Definition of Empirical Temperature

The scalar function $\\theta(P, V)$ is called the **empirical temperature**. Thermal equilibrium is an equivalence relation possessing:
1. **Reflexivity**: $A \\sim A$.
2. **Symmetry**: $A \\sim B \\implies B \\sim A$.
3. **Transitivity**: $A \\sim C \\land B \\sim C \\implies A \\sim B$.

This partitions all thermodynamic equilibrium states into disjoint equivalence classes (isotherms). A thermometer is any physical system possessing a measurable thermometric property $X$ (e.g., mercury column height, electrical resistance of platinum, thermoelectric EMF, gas pressure at constant volume) that monotonically tracks empirical temperature $\\theta = a X$.
            """
        },
        {
            "id": "u1-sec3",
            "title": "Work, Heat Energy & Exact vs Inexact Differentials",
            "content": """
### 1. Macroscopic Work Interactions

Thermodynamic work represents energy transfer driven by a generalized force operating through a conjugate generalized displacement. Unlike mechanical work on a point mass, thermodynamic work alters the external configuration or boundary of a macroscopic ensemble:
- **Hydrostatic Boundary Work**: When a fluid exerts normal pressure $P$ on a movable piston of area $A$, an infinitesimal displacement $dx$ produces volume change $dV = A dx$. The work performed by the system is:
$$\\delta W = P dV$$
- **Surface Film Work**: For a 2D interface with surface tension $\\gamma$, expanding interfacial area by $dA$ requires work:
$$\\delta W = -\\gamma dA$$
- **Magnetic Work**: In a paramagnetic medium subjected to external magnetic field $\\vec{H}$, altering total magnetization $\\vec{M}$ performs work:
$$\\delta W = -\\mu_0 \\vec{H} \\cdot d\\vec{M}$$

### 2. Inexact Differentials and Path Dependence

Work $\\delta W$ and heat $\\delta Q$ are **path functions**, not state functions. They describe energy in transit across boundaries during a process, rather than properties stored within a state.

Mathematically, let a differential form in two independent state variables $(x, y)$ be written as:
$$\\delta Z = M(x, y) dx + N(x, y) dy$$
By Euler's criterion, $\\delta Z$ is an **exact differential** ($dZ$) if and only if:
$$\\left(\\frac{\\partial M}{\\partial y}\\right)_x = \\left(\\frac{\\partial N}{\\partial x}\\right)_y$$
When exact, the line integral between state 1 and state 2 is independent of path:
$$\\int_{\\text{Path } A}^{(1) \\to (2)} dZ = \\int_{\\text{Path } B}^{(1) \\to (2)} dZ = Z_2 - Z_1, \\quad \\oint dZ = 0$$

For boundary work $\\delta W = P dV + 0 dP$, we have $M(V, P) = P$ and $N(V, P) = 0$. The cross-derivatives give:
$$\\left(\\frac{\\partial M}{\\partial P}\\right)_V = \\frac{\\partial P}{\\partial P} = 1, \\quad \\left(\\frac{\\partial N}{\\partial V}\\right)_P = 0 \\implies 1 \\neq 0$$
Hence $\\delta W$ is an **inexact differential**, denoted by $\\delta W$ or $\\mathrm{d}\\\\!\\bar{\\;\\,}W$. Consequently:
$$W_{1 \\to 2} = \\int_{\\text{Path}} P dV \\neq W_2 - W_1$$
The integral equals the area under the process curve on a $P$-$V$ indicator diagram, which explicitly depends on the transformation trajectory.
            """
        },
        {
            "id": "u1-sec4",
            "title": "First Law of Thermodynamics & Internal Energy",
            "content": """
### 1. Conservation of Energy in Macroscopic Systems

The **First Law of Thermodynamics** is the universal law of conservation of energy extended to incorporate thermal phenomena. In any thermodynamic transformation between equilibrium states (1) and (2), the individual quantities of heat absorbed $Q$ and work performed $W$ depend heavily on the specific path. However, experimental investigations by Joule (1843–1850) established that their algebraic difference $(Q - W)$ is strictly identical for every conceivable path connecting the two states:

$$\\Delta U \\equiv U_2 - U_1 = Q - W$$

In infinitesimal differential form:
$$dU = \\delta Q - \\delta W = \\delta Q - P dV$$

Because $dU$ is an exact differential, the **Internal Energy** $U$ is a true thermodynamic state function.

### 2. Microscopic Nature of Internal Energy

Microscopically, internal energy $U$ represents the total microscopic kinetic and potential energies of all constituent particles within the rest frame of the center of mass:
$$U = \\sum_{i=1}^N \\frac{\\vec{p}_i^2}{2m} + \\sum_{i < j} V(\\vec{r}_i - \\vec{r}_j) + \\sum_{i=1}^N \\left( E_{\\text{rot}, i} + E_{\\text{vib}, i} + E_{\\text{electronic}, i} \\right)$$
For a monoatomic ideal gas, intermolecular potential energies are zero ($V(r) \\equiv 0$), and translational kinetic energy dominates:
$$U = \\frac{3}{2} N k_B T = \\frac{3}{2} n R T$$

### 3. Joule's Free Expansion Experiment

In 1845, James Prescott Joule tested whether internal energy depends on volume at constant temperature. Two copper vessels—one containing gas at high pressure ($P_1$) and the other evacuated—were immersed in a thermally insulated water calorimeter and connected by a stopcock. When the stopcock was opened, gas expanded freely into the vacuum without moving any external boundary:
- $W = 0$ (no external resistance against expansion into vacuum).
- $Q = 0$ (no net heat transfer observed from calorimeter water).
- By the First Law: $\\Delta U = Q - W = 0$.

Joule detected no measurable change in calorimeter water temperature ($\Delta T = 0$). Hence, for an ideal gas:
$$\\left(\\frac{\\partial U}{\\partial V}\\right)_T = 0 \\implies U = U(T)$$
Internal energy of an ideal gas depends solely on absolute temperature, fundamentally independent of volume or pressure.
            """
        },
        {
            "id": "u1-sec5",
            "title": "Thermodynamic Processes & Work Calculations",
            "content": """
### 1. Reversible Isochoric Process ($V = \\text{constant}$)
In a rigid container, volume remains fixed ($dV = 0$):
- Work performed: $W = \\int P dV = 0$.
- Heat added: $Q = \\Delta U = \\int_{T_1}^{T_2} C_v dT$.
- Specific heat at constant volume: $C_v \\equiv \\left(\\frac{\\partial U}{\\partial T}\\right)_V$.

### 2. Reversible Isobaric Process ($P = \\text{constant}$)
In a cylinder with freely moving weighted piston:
- Work performed: $W = \\int_{V_1}^{V_2} P dV = P (V_2 - V_1) = n R (T_2 - T_1)$.
- Heat added: $Q = \\Delta U + W = (U_2 - U_1) + P(V_2 - V_1) = (U_2 + P V_2) - (U_1 + P V_1) = H_2 - H_1 = \\Delta H$.
- The **Enthalpy** $H \\equiv U + P V$ serves as the heat content state function under constant pressure conditions.
- Specific heat at constant pressure: $C_p \\equiv \\left(\\frac{\\partial H}{\\partial T}\\right)_P$.

### 3. Reversible Isothermal Process ($T = \\text{constant}$)
For an ideal gas at constant temperature $T$:
- Internal energy change: $\\Delta U = 0$ (since $U = U(T)$).
- Heat and work equality: $Q = W$.
- Work integration from ideal gas equation $P = nRT / V$:
$$W = \\int_{V_1}^{V_2} \\frac{n R T}{V} dV = n R T \\ln\\left(\\frac{V_2}{V_1}\\right) = n R T \\ln\\left(\\frac{P_1}{P_2}\\right)$$

### 4. Reversible Adiabatic Process ($Q = 0$)
When thermally insulated from surroundings ($\delta Q = 0$):
- First law: $dU = -\\delta W \\implies C_v dT = -P dV$.
- Substituting $P = nRT / V$:
$$C_v dT = -\\frac{n R T}{V} dV \\implies \\frac{dT}{T} + \\frac{R}{C_v} \\frac{dV}{V} = 0$$
Recalling Mayer's relation $R = C_p - C_v$ and the adiabatic index $\\gamma = C_p / C_v$, the ratio $R / C_v = \\gamma - 1$:
$$\\ln T + (\\gamma - 1) \\ln V = \\text{const} \\implies T V^{\\gamma - 1} = \\text{constant}$$
Using $T = P V / nR$:
$$P V^\\gamma = \\text{constant}, \\quad T^\\gamma P^{1 - \\gamma} = \\text{constant}$$
- Adiabatic Work Integration:
$$W = -\\Delta U = -C_v (T_2 - T_1) = \\frac{n R (T_1 - T_2)}{\\gamma - 1} = \\frac{P_1 V_1 - P_2 V_2}{\\gamma - 1}$$
            """
        },
        {
            "id": "u1-sec6",
            "title": "Specific Heats, Compressibility & Thermal Expansion",
            "content": """
### 1. General Thermodynamic Relation Between $C_p$ and $C_v$

Let internal energy be expressed as a function of temperature and volume, $U = U(T, V)$:
$$dU = \\left(\\frac{\\partial U}{\\partial T}\\right)_V dT + \\left(\\frac{\\partial U}{\\partial V}\\right)_T dV = C_v dT + \\left(\\frac{\\partial U}{\\partial V}\\right)_T dV$$
Substituting into the First Law $\\delta Q = dU + P dV$:
$$\\delta Q = C_v dT + \\left[ P + \\left(\\frac{\\partial U}{\\partial V}\\right)_T \\right] dV$$
Dividing by $dT$ at constant pressure $P$:
$$C_p = \\left(\\frac{\\delta Q}{dT}\\right)_P = C_v + \\left[ P + \\left(\\frac{\\partial U}{\\partial V}\\right)_T \\right] \\left(\\frac{\\partial V}{\\partial T}\\right)_P$$
Therefore, the universal relation between heat capacities is:
$$C_p - C_v = \\left[ P + \\left(\\frac{\\partial U}{\\partial V}\\right)_T \\right] \\left(\\frac{\\partial V}{\\partial T}\\right)_P$$

For an ideal gas, Joule's experiment proves $(\\partial U/\\partial V)_T = 0$, and from $P V = n R T$, $(\\partial V/\\partial T)_P = n R / P$:
$$C_p - C_v = P \\cdot \\left(\\frac{n R}{P}\\right) = n R \\quad \\implies \\quad C_{p, m} - C_{v, m} = R$$
This is **Mayer's classical relation**.

### 2. Response Coefficients: Compressibility and Expansion

To express thermodynamic relations in terms of directly measurable material properties, we define three response coefficients:
1. **Isobaric Thermal Expansion Coefficient** $\\alpha$:
$$\\alpha \\equiv \\frac{1}{V} \\left(\\frac{\\partial V}{\\partial T}\\right)_P$$
2. **Isothermal Compressibility** $\\kappa_T$:
$$\\kappa_T \\equiv -\\frac{1}{V} \\left(\\frac{\\partial V}{\\partial P}\\right)_T$$
3. **Isochoric Pressure Coefficient** $\\beta$:
$$\\beta \\equiv \\frac{1}{P} \\left(\\frac{\\partial P}{\\partial T}\\right)_V$$

By the cyclic triple product identity for $(P, V, T)$:
$$\\left(\\frac{\\partial P}{\\partial T}\\right)_V \\left(\\frac{\\partial T}{\\partial V}\\right)_P \\left(\\frac{\\partial V}{\\partial P}\\right)_T = -1 \\implies \\left(\\frac{\\partial P}{\\partial T}\\right)_V = -\\frac{(\\partial V/\\partial T)_P}{(\\partial V/\\partial P)_T} = \\frac{\\alpha V}{\\kappa_T V} = \\frac{\\alpha}{\\kappa_T}$$
Using Maxwell's relation $(\\partial U/\\partial V)_T = T (\\partial P/\\partial T)_V - P$, the bracketed term in $C_p - C_v$ becomes:
$$P + \\left(\\frac{\\partial U}{\\partial V}\\right)_T = T \\left(\\frac{\\partial P}{\\partial T}\\right)_V = T \\frac{\\alpha}{\\kappa_T}$$
Multiplying by $(\\partial V/\\partial T)_P = V \\alpha$:
$$C_p - C_v = T V \\frac{\\alpha^2}{\\kappa_T}$$
This rigorous formula holds for **any substance in any phase** (solids, liquids, and real gases). Because absolute temperature $T > 0$, volume $V > 0$, and mechanical stability requires $\kappa_T > 0$, it follows that $C_p \\ge C_v$ always, with $C_p = C_v$ occurring only at $T = 0\\text{ K}$ or where $\\alpha = 0$ (such as liquid water at $3.98^\\circ\\text{C}$).
            """
        },
        {
            "id": "u1-sec7",
            "title": "Atmospheric Thermodynamics & Adiabatic Lapse Rate",
            "content": """
### 1. Hydrostatic Equation of the Atmosphere

Consider a column of dry atmospheric air under gravity. For a horizontal air parcel of cross-sectional area $A$ and thickness $dz$, mechanical balance between upward pressure force, downward pressure force, and parcel weight gives:
$$P A - (P + dP) A = \\rho A g dz \\implies dP = -\\rho g dz$$
where $\\rho$ is local air density and $g$ is gravitational acceleration. Using the ideal gas equation of state $\\rho = \\frac{P M}{R T}$ where $M$ is the effective molar mass of dry air ($M \\approx 28.97\\text{ g/mol}$):
$$\\frac{dP}{P} = -\\frac{M g}{R T(z)} dz$$

### 2. Derivation of the Dry Adiabatic Lapse Rate

When an air parcel rises rapidly through the troposphere, thermal conduction across its boundary is negligible compared to convective transit times; the parcel expands **adiabatically** ($Q = 0$). For an adiabatic parcel:
$$T^\\gamma P^{1-\\gamma} = \\text{const} \\implies \\gamma \\frac{dT}{T} + (1-\\gamma) \\frac{dP}{P} = 0$$
Solving for $dP/P$:
$$\\frac{dP}{P} = \\frac{\\gamma}{\\gamma - 1} \\frac{dT}{T}$$
Equating this with the hydrostatic relation $\\frac{dP}{P} = -\\frac{M g}{R T} dz$:
$$\\frac{\\gamma}{\\gamma - 1} \\frac{dT}{T} = -\\frac{M g}{R T} dz \\implies \\frac{dT}{dz} = -\\frac{\\gamma - 1}{\\gamma} \\frac{M g}{R}$$
Recalling that $C_{p, m} = \\frac{\\gamma R}{\\gamma - 1}$, the specific heat capacity per unit mass is $c_p = \\frac{C_{p, m}}{M} = \\frac{\\gamma R}{M (\\gamma - 1)}$. Thus:
$$\\Gamma_{\\text{dry}} \\equiv -\\frac{dT}{dz} = \\frac{g}{c_p}$$

For Earth's atmosphere, $g \\approx 9.807\\text{ m/s}^2$ and dry air specific heat $c_p \\approx 1005\\text{ J/(kg}\\cdot\\text{K)}$:
$$\\Gamma_{\\text{dry}} = \\frac{9.807}{1005} \\approx 0.00976\\text{ K/m} \\approx 9.76\\text{ K/km} \\approx 9.8^\\circ\\text{C/km}$$

### 3. Atmospheric Stability Criteria
The environmental lapse rate $\\Gamma_{\\text{env}} = -\\frac{dT_{\\text{env}}}{dz}$ determines atmospheric convective stability:
- **Unstable Atmosphere** ($\\Gamma_{\\text{env}} > \\Gamma_{\\text{dry}}$): A displaced air parcel becomes warmer and less dense than surrounding ambient air, experiencing positive buoyant acceleration, generating strong convective storms and cumulonimbus clouds.
- **Neutral Atmosphere** ($\\Gamma_{\\text{env}} = \\Gamma_{\\text{dry}}$): Displaced parcel remains at ambient density.
- **Stable Atmosphere** ($\\Gamma_{\\text{env}} < \\Gamma_{\\text{dry}}$): Parcel becomes colder and denser than surrounding air, experiencing restoring buoyant forces that suppress vertical air motion (temperature inversions and smog trapping).
            """
        }
    ],
    "problems": [
        {
            "id": "u1-p1",
            "title": "Polytropic Process Gas Work, Internal Energy & Heat Capacity",
            "statement": "Two moles of an ideal diatomic gas ($\\\\gamma = 1.40$) undergo a reversible polytropic expansion according to the relation $P V^{1.25} = \\\\text{constant}$, expanding from an initial pressure of $P_1 = 4.00\\\\times 10^5\\\\text{ Pa}$ and volume $V_1 = 0.020\\\\text{ m}^3$ to a final volume of $V_2 = 0.060\\\\text{ m}^3$. Calculate: (a) the final pressure $P_2$, (b) the total work done $W$, (c) the change in internal energy $\\\\Delta U$, and (d) the molar heat capacity $C$ for this specific polytropic trajectory.",
            "steps": [
                {
                    "step": "Step 1: Determine Final Pressure $P_2$",
                    "detail": "For a polytropic process $P V^n = \\\\text{const}$ with $n = 1.25$:\n$$P_2 = P_1 \\\\left(\\\\frac{V_1}{V_2}\\\\right)^n = (4.00 \\\\times 10^5\\\\text{ Pa}) \\\\left(\\\\frac{0.020}{0.060}\\\\right)^{1.25} = \\\\frac{4.00 \\\\times 10^5}{3^{1.25}} = \\\\frac{4.00 \\\\times 10^5}{3.9482} = 1.0131 \\\\times 10^5\\\\text{ Pa}$$\nThis confirms the gas expands to nearly standard atmospheric pressure."
                },
                {
                    "step": "Step 2: Calculate Boundary Work Done $W$",
                    "detail": "The boundary work performed during a polytropic path is:\n$$W = \\\\int_{V_1}^{V_2} P dV = \\\\frac{P_1 V_1 - P_2 V_2}{n - 1}$$\nEvaluating the pressure-volume products:\n$$P_1 V_1 = (4.00 \\\\times 10^5)(0.020) = 8000\\\\text{ J}$$\n$$P_2 V_2 = (1.0131 \\\\times 10^5)(0.060) = 6078.7\\\\text{ J}$$\n$$W = \\\\frac{8000 - 6078.7}{1.25 - 1} = \\\\frac{1921.3}{0.25} = +7685.2\\\\text{ J}$$"
                },
                {
                    "step": "Step 3: Calculate Change in Internal Energy $\\\\Delta U$",
                    "detail": "Using the ideal gas relation $\\\\Delta U = n C_v \\\\Delta T = \\\\frac{P_2 V_2 - P_1 V_1}{\\\\gamma - 1}$:\n$$\\\\Delta U = \\\\frac{6078.7 - 8000}{1.40 - 1} = \\\\frac{-1921.3}{0.40} = -4803.3\\\\text{ J}$$\nThe gas internal energy decreases by $4.80\\\\text{ kJ}$ due to thermal cooling during expansion."
                },
                {
                    "step": "Step 4: Determine Net Heat Absorbed $Q$ and Polytropic Heat Capacity $C_m$",
                    "detail": "By the First Law of Thermodynamics:\n$$Q = \\\\Delta U + W = -4803.3 + 7685.2 = +2881.9\\\\text{ J}$$\nThe molar polytropic heat capacity is derived via $C_m = C_{v, m} + \\\\frac{R}{1 - n}$:\n$$C_{v, m} = \\\\frac{R}{\\\\gamma - 1} = \\\\frac{8.314}{0.40} = 20.785\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\n$$\\\\frac{R}{1 - n} = \\\\frac{8.314}{1 - 1.25} = \\\\frac{8.314}{-0.25} = -33.256\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\n$$C_m = 20.785 - 33.256 = -12.47\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\nNotice that the polytropic molar heat capacity is negative: as the gas absorbs heat, its temperature decreases because the work done on the surroundings exceeds the heat supplied."
                }
            ],
            "answer": "Final pressure $P_2 = 1.01\\\\times 10^5\\\\text{ Pa}$, work done $W = +7.69\\\\text{ kJ}$, internal energy change $\\\\Delta U = -4.80\\\\text{ kJ}$, heat absorbed $Q = +2.88\\\\text{ kJ}$, and molar heat capacity $C_m = -12.47\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$."
        },
        {
            "id": "u1-p2",
            "title": "Exact Calculation of $C_p - C_v$ for a Van der Waals Gas",
            "statement": "Starting from the fundamental thermodynamic relation $C_p - C_v = \\\\left[ P + \\\\left(\\\\frac{\\\\partial U}{\\\\partial V}\\\\right)_T \\\\right] \\\\left(\\\\frac{\\\\partial V}{\\\\partial T}\\\\right)_P$, derive an explicit formula for $C_p - C_v$ for one mole of a real gas obeying the Van der Waals equation of state $\\\\left(P + \\\\frac{a}{V_m^2}\\\\right)(V_m - b) = R T$, and evaluate the percentage deviation from Mayer's ideal relation ($R$) for carbon dioxide at $T = 300\\\\text{ K}$ and $V_m = 1.00\\\\times 10^{-3}\\\\text{ m}^3\\\\text{/mol}$, given $a = 0.364\\\\text{ J}\\\\cdot\\\\text{m}^3\\\\text{/mol}^2$ and $b = 4.27\\\\times 10^{-5}\\\\text{ m}^3\\\\text{/mol}$.",
            "steps": [
                {
                    "step": "Step 1: Evaluate the Internal Pressure Term $\\\\left(\\\\frac{\\\\partial U}{\\\\partial V}\\\\right)_T$",
                    "detail": "From thermodynamic energy equations (derived from Maxwell's relations):\n$$\\\\left(\\\\frac{\\\\partial U}{\\\\partial V_m}\\\\right)_T = T \\\\left(\\\\frac{\\\\partial P}{\\\\partial T}\\\\right)_{V_m} - P$$\nFor a Van der Waals gas, $P = \\\\frac{R T}{V_m - b} - \\\\frac{a}{V_m^2}$.\nTaking the derivative with respect to $T$ at constant $V_m$:\n$$\\\\left(\\\\frac{\\\\partial P}{\\\\partial T}\\\\right)_{V_m} = \\\\frac{R}{V_m - b}$$\nSubstituting back:\n$$\\\\left(\\\\frac{\\\\partial U}{\\\\partial V_m}\\\\right)_T = T \\\\left(\\\\frac{R}{V_m - b}\\\\right) - \\\\left(\\\\frac{R T}{V_m - b} - \\\\frac{a}{V_m^2}\\\\right) = \\\\frac{a}{V_m^2}$$\nTherefore, the bracketed term simplifies beautifully to:\n$$P + \\\\left(\\\\frac{\\\\partial U}{\\\\partial V_m}\\\\right)_T = \\\\frac{R T}{V_m - b}$$"
                },
                {
                    "step": "Step 2: Evaluate the Thermal Expansion Derivative $\\\\left(\\\\frac{\\\\partial V_m}{\\\\partial T}\\\\right)_P$",
                    "detail": "Differentiating the Van der Waals equation $\\\\left(P + \\\\frac{a}{V_m^2}\\\\right)(V_m - b) = R T$ implicitly with respect to $T$ at constant $P$:\n$$\\\\left(-\\\\frac{2a}{V_m^3} \\\\frac{\\\\partial V_m}{\\\\partial T}\\\\right)(V_m - b) + \\\\left(P + \\\\frac{a}{V_m^2}\\\\right)\\\\frac{\\\\partial V_m}{\\\\partial T} = R$$\nFactoring $\\\\frac{\\\\partial V_m}{\\\\partial T}$:\n$$\\\\frac{\\\\partial V_m}{\\\\partial T} \\\\left[ \\\\frac{R T}{V_m - b} - \\\\frac{2a(V_m - b)}{V_m^3} \\\\right] = R$$\n$$\\\\left(\\\\frac{\\\\partial V_m}{\\\\partial T}\\\\right)_P = \\\\frac{R}{\\\\frac{R T}{V_m - b} - \\\\frac{2a(V_m - b)}{V_m^3}} = \\\\frac{R (V_m - b)}{R T - \\\\frac{2a(V_m - b)^2}{V_m^3}}$$"
                },
                {
                    "step": "Step 3: Combine Expressions for $C_p - C_v$",
                    "detail": "Multiplying the two terms:\n$$C_p - C_v = \\\\left(\\\\frac{R T}{V_m - b}\\\\right) \\\\left[ \\\\frac{R (V_m - b)}{R T - \\\\frac{2a(V_m - b)^2}{V_m^3}} \\\\right] = \\\\frac{R}{1 - \\\\frac{2a(V_m - b)^2}{R T V_m^3}}$$\nNotice that when $a \\\\to 0$, $C_p - C_v \\\\to R$ (ideal gas)."
                },
                {
                    "step": "Step 4: Numerical Evaluation for Carbon Dioxide",
                    "detail": "Given parameters: $T = 300\\\\text{ K}$, $V_m = 1.00 \\\\times 10^{-3}\\\\text{ m}^3\\\\text{/mol}$, $a = 0.364$, $b = 4.27 \\\\times 10^{-5}$.\n$$V_m - b = 1.00 \\\\times 10^{-3} - 0.0427 \\\\times 10^{-3} = 0.9573 \\\\times 10^{-3}\\\\text{ m}^3$$\n$$(V_m - b)^2 = 9.164 \\\\times 10^{-7}\\\\text{ m}^6$$\n$$2a(V_m - b)^2 = 2(0.364)(9.164 \\\\times 10^{-7}) = 6.671 \\\\times 10^{-7}$$\n$$R T V_m^3 = (8.314)(300)(1.00 \\\\times 10^{-3})^3 = 2494.2 \\\\times 10^{-9} = 2.4942 \\\\times 10^{-6}$$\nThe denominator dimensionless correction term is:\n$$\\\\delta = \\\\frac{2a(V_m - b)^2}{R T V_m^3} = \\\\frac{6.671 \\\\times 10^{-7}}{2.4942 \\\\times 10^{-6}} = 0.2675$$\nThus:\n$$C_p - C_v = \\\\frac{R}{1 - 0.2675} = \\\\frac{8.314}{0.7325} = 11.35\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\nPercentage deviation from ideal gas Mayer value:\n$$\\\\Delta\\\\% = \\\\frac{11.35 - 8.314}{8.314} \\\\times 100\\\\% = +36.5\\\\%$$"
                }
            ],
            "answer": "Exact relation is $C_p - C_v = \\\\frac{R}{1 - \\\\frac{2a(V_m - b)^2}{R T V_m^3}}$. For $\\\\text{CO}_2$ at $300\\\\text{ K}$, $C_p - C_v = 11.35\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$, representing a $+36.5\\\\%$ enhancement above the ideal gas constant $R$ due to intermolecular attractive forces."
        },
        {
            "id": "u1-p3",
            "title": "Atmospheric Parcel Ascent & Dry Adiabatic Lapse Rate",
            "statement": "An air parcel with an initial temperature of $T_0 = 25.0^\\\\circ\\\\text{C}$ ($298.15\\\\text{ K}$) at sea level ($z = 0\\\\text{ m}$, $P_0 = 101.3\\\\text{ kPa}$) is forced to rise over a mountain ridge of height $h = 3200\\\\text{ m}$. Assuming dry adiabatic ascent ($c_p = 1005\\\\text{ J/(kg}\\\\cdot\\\\text{K)}$, $g = 9.81\\\\text{ m/s}^2$, $M = 28.97\\\\text{ g/mol}$): (a) calculate the parcel temperature at the mountain summit, (b) calculate the barometric pressure at the summit, and (c) determine the buoyant force per unit mass if the ambient environment exhibits an environmental lapse rate of $\\\\Gamma_{\\\\text{env}} = 6.50^\\\\circ\\\\text{C/km}$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Parcel Temperature at Summit",
                    "detail": "The dry adiabatic lapse rate is:\n$$\\\\Gamma_{\\\\text{dry}} = \\\\frac{g}{c_p} = \\\\frac{9.81\\\\text{ m/s}^2}{1005\\\\text{ J/(kg}\\\\cdot\\\\text{K)}} = 0.009761\\\\text{ K/m} = 9.761\\\\text{ K/km}$$\nAt altitude $h = 3200\\\\text{ m} = 3.20\\\\text{ km}$:\n$$T_{\\\\text{parcel}}(h) = T_0 - \\\\Gamma_{\\\\text{dry}} h = 298.15 - (9.761)(3.20) = 298.15 - 31.24 = 266.91\\\\text{ K} = -6.24^\\\\circ\\\\text{C}$$"
                },
                {
                    "step": "Step 2: Calculate Summit Atmospheric Pressure",
                    "detail": "For an adiabatic ascent, pressure and temperature are related via:\n$$P(h) = P_0 \\\\left(\\\\frac{T_{\\\\text{parcel}}(h)}{T_0}\\\\right)^{\\\\frac{\\\\gamma}{\\\\gamma - 1}}$$\nFor dry air ($\\\\gamma = 1.40$), $\\\\frac{\\\\gamma}{\\\\gamma - 1} = \\\\frac{1.40}{0.40} = 3.50$.\n$$P(h) = (101.3\\\\text{ kPa}) \\\\left(\\\\frac{266.91}{298.15}\\\\right)^{3.50} = (101.3) (0.89522)^{3.50} = (101.3)(0.6781) = 68.69\\\\text{ kPa}$$"
                },
                {
                    "step": "Step 3: Calculate Ambient Temperature and Buoyancy Acceleration",
                    "detail": "The surrounding ambient environmental temperature at $3200\\\\text{ m}$ with $\\\\Gamma_{\\\\text{env}} = 6.50^\\\\circ\\\\text{C/km}$ is:\n$$T_{\\\\text{env}}(h) = 298.15 - (6.50)(3.20) = 298.15 - 20.80 = 277.35\\\\text{ K} = +4.20^\\\\circ\\\\text{C}$$\nNotice that the adiabatic parcel ($-6.24^\\\\circ\\\\text{C}$) is colder than the environment ($+4.20^\\\\circ\\\\text{C}$).\nThe buoyant acceleration (Archimedes force per unit mass) is:\n$$a_b = g \\\\left(\\\\frac{\\\\rho_{\\\\text{env}} - \\\\rho_{\\\\text{parcel}}}{\\\\rho_{\\\\text{parcel}}}\\\\right) = g \\\\left(\\\\frac{T_{\\\\text{parcel}} - T_{\\\\text{env}}}{T_{\\\\text{env}}}\\\\right)$$\n$$a_b = 9.81 \\\\left(\\\\frac{266.91 - 277.35}{277.35}\\\\right) = 9.81 \\\\left(\\\\frac{-10.44}{277.35}\\\\right) = -0.369\\\\text{ m/s}^2$$\nThe negative sign signifies a restoring downward buoyant force, proving that the atmosphere is stable against dry convection."
                }
            ],
            "answer": "At $3200\\\\text{ m}$, parcel temperature $T_{\\\\text{parcel}} = -6.24^\\\\circ\\\\text{C}$ ($266.9\\\\text{ K}$), atmospheric pressure $P = 68.7\\\\text{ kPa}$, and restoring buoyant acceleration $a_b = -0.369\\\\text{ m/s}^2$ indicating a statically stable atmosphere."
        }
    ]
}

# Unit 2: Second Law of Thermodynamics
u2 = {
    "unitNumber": 2,
    "title": "Second Law of Thermodynamics",
    "description": "Directionality of natural processes: reversibility, heat engine cycles, Carnot theorem, refrigeration cycles, Kelvin-Planck and Clausius statements, and the thermodynamic temperature scale.",
    "sections": [
        {
            "id": "u2-sec1",
            "title": "Reversible vs Irreversible Changes & Dissipation",
            "content": """
### 1. Thermodynamic Reversibility

A thermodynamic process is defined as **strictly reversible** if both the system and every portion of its external surroundings can be restored to their exact initial states without producing any residual changes anywhere in the universe. 

For a transformation to be reversible, two conditions must be satisfied:
1. **Mechanical & Thermal Quasi-Static Equilibrium**: The transformation must proceed along a continuous succession of equilibrium states, requiring driving forces (pressure differences $\Delta P \to 0$ and temperature gradients $\Delta T \to 0$) to be infinitesimal.
2. **Total Absence of Dissipative Effects**: There can be zero friction, electrical resistance, inelastic hysteresis, or turbulent hydrodynamic drag.

### 2. Physical Sources of Irreversibility

All macroscopic processes occurring in nature are fundamentally **irreversible**. Natural irreversibility manifests in two distinct classes:
- **Internal Dissipative Irreversibility**: Conversion of organized mechanical kinetic energy or boundary work into disorganized thermal kinetic motion through viscosity, dry Coulomb friction, plastic deformation, or electrical Joule heating.
- **External Unrestrained Irreversibility**: Spontaneous transport driven by finite thermodynamic affinities, such as heat transfer across finite temperature gaps ($\Delta T > 0$), free expansion of gases into a vacuum ($\Delta P > 0$), or spontaneous inter-diffusion of distinct chemical species across concentration gradients ($\Delta \mu > 0$).
            """
        },
        {
            "id": "u2-sec2",
            "title": "Work-to-Heat Asymmetry & Heat Engines",
            "content": """
### 1. Directional Asymmetry of Thermal and Mechanical Energy

The First Law recognizes work $W$ and heat $Q$ as equivalent forms of energy transfer ($1\\text{ J} = 1\\text{ J}$). However, experience reveals a profound **asymmetry in their inter-conversion**:
- Mechanical work can be converted **100% into heat** with complete ease and without requiring any additional cyclic machinery (e.g., stirring viscous fluid, friction braking).
- Heat **cannot be completely converted into mechanical work** in a continuous, cyclic process. Any heat engine operating in a closed thermodynamic cycle *must* inevitably reject a portion of the absorbed thermal energy to a lower-temperature reservoir.

### 2. General Architecture of a Heat Engine

A **heat engine** is a thermodynamic device that operates in a closed thermodynamic cycle ($\Delta U_{\\text{cycle}} = 0$) to continuously produce net mechanical work from heat supplied by an external source. It consists of:
1. A **Hot Reservoir** at uniform absolute temperature $T_H$, providing heat $Q_H > 0$.
2. A **Working Substance** (e.g., steam, ideal gas, air-fuel mixture) undergoing cyclic expansion and compression.
3. A **Cold Reservoir** (thermal sink) at uniform temperature $T_C < T_H$, absorbing rejected heat $Q_C > 0$.

By the First Law over one complete closed cycle:
$$\\Delta U = Q_{\\text{net}} - W_{\\text{net}} = 0 \\implies W_{\\text{net}} = Q_H - Q_C$$

### 3. Thermal Efficiency

The **thermal efficiency** $\\eta$ of any heat engine is the dimensionless ratio of net mechanical work delivered to the total high-grade heat purchased/absorbed from the hot reservoir:
$$\\eta \\equiv \\frac{W_{\\text{net}}}{Q_H} = \\frac{Q_H - Q_C}{Q_H} = 1 - \\frac{Q_C}{Q_H}$$
Since natural conservation requires $Q_C > 0$, thermal efficiency is strictly bounded: $\\eta < 1$ (or $\\eta < 100\\%$).
            """
        },
        {
            "id": "u2-sec3",
            "title": "The Carnot Engine & Reversible Cycle Analysis",
            "content": """
### 1. The Idealized Carnot Cycle

In 1824, French engineer Nicolas Léonard Sadi Carnot established the theoretical upper limit on heat engine efficiency by devising an idealized four-stage reversible cyclic sequence using an ideal gas as the working substance:

- **Stage 1: Reversible Isothermal Expansion ($A \\to B$)**: Cylinder is placed in thermal contact with hot reservoir at $T_H$. Gas expands quasi-statically from $V_A$ to $V_B$ while maintaining constant temperature $T_H$.
  $$W_{AB} = Q_H = n R T_H \\ln\\left(\\frac{V_B}{V_A}\\right)$$
- **Stage 2: Reversible Adiabatic Expansion ($B \\to C$)**: Cylinder is placed on an adiabatic insulated stand. Gas expands without heat exchange ($Q_{BC} = 0$) from $V_B$ to $V_C$, doing work against piston and cooling from $T_H$ down to $T_C$.
  $$W_{BC} = -\\Delta U = n C_v (T_H - T_C), \\quad T_H V_B^{\\gamma - 1} = T_C V_C^{\\gamma - 1}$$
- **Stage 3: Reversible Isothermal Compression ($C \\to D$)**: Cylinder is placed in thermal contact with cold reservoir at $T_C$. Gas is compressed quasi-statically from $V_C$ to $V_D$, rejecting heat $Q_C$ at temperature $T_C$.
  $$W_{CD} = -Q_C = n R T_C \\ln\\left(\\frac{V_D}{V_C}\\right) \\implies Q_C = n R T_C \\ln\\left(\\frac{V_C}{V_D}\\right)$$
- **Stage 4: Reversible Adiabatic Compression ($D \\to A$)**: Cylinder is placed back on adiabatic insulated stand. Gas is compressed from $V_D$ back to initial volume $V_A$, raising temperature from $T_C$ back to $T_H$ to complete the cycle.
  $$W_{DA} = -n C_v (T_H - T_C) = -W_{BC}, \\quad T_C V_D^{\\gamma - 1} = T_H V_A^{\\gamma - 1}$$

### 2. Exact Efficiency Derivation

Dividing the two adiabatic relations:
$$\\frac{T_H V_B^{\\gamma - 1}}{T_H V_A^{\\gamma - 1}} = \\frac{T_C V_C^{\\gamma - 1}}{T_C V_D^{\\gamma - 1}} \\implies \\left(\\frac{V_B}{V_A}\\right)^{\\gamma - 1} = \\left(\\frac{V_C}{V_D}\\right)^{\\gamma - 1} \\implies \\frac{V_B}{V_A} = \\frac{V_C}{V_D}$$
The ratio of rejected heat to absorbed heat becomes:
$$\\frac{Q_C}{Q_H} = \\frac{n R T_C \\ln(V_C / V_D)}{n R T_H \\ln(V_B / V_A)} = \\frac{T_C}{T_H}$$
Substituting this into the efficiency definition yields the celebrated **Carnot Efficiency**:
$$\\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}$$
Carnot efficiency depends *exclusively* on the reservoir temperatures $T_H$ and $T_C$, completely independent of the working substance, whether ideal gas, real gas, or magnetic dipole ensemble.
            """
        },
        {
            "id": "u2-sec4",
            "title": "Refrigerators, Heat Pumps & Coefficients of Performance",
            "content": """
### 1. The Reversed Carnot Cycle

Because all four stages of the Carnot cycle are strictly reversible, the cycle can be operated in reverse ($A \\to D \\to C \\to B \\to A$). In reverse operation, external net mechanical work $W_{\\text{net}} > 0$ is delivered to the working substance to extract heat $Q_C$ from a low-temperature cold space and discharge heat $Q_H = Q_C + W_{\\text{net}}$ into a higher-temperature ambient environment.

### 2. Coefficient of Performance (COP) of a Refrigerator

For a refrigerator, the desired thermodynamic benefit is the heat removed from the cold storage space ($Q_C$), while the required economic input is the compressor work ($W_{\\text{net}}$). The **Coefficient of Performance (COP)**, denoted by $\\beta$ or $\\text{COP}_{\\text{ref}}$, is:
$$\\beta \\equiv \\frac{Q_C}{W_{\\text{net}}} = \\frac{Q_C}{Q_H - Q_C} = \\frac{1}{\\frac{Q_H}{Q_C} - 1}$$
For an ideal reversible Carnot refrigerator:
$$\\beta_{\\text{Carnot}} = \\frac{T_C}{T_H - T_C}$$
Unlike heat engine efficiency (which is strictly $< 1$), $\\beta$ routinely exceeds 1 (typically $\\beta \\approx 3$ to $5$ in domestic refrigeration units).

### 3. Coefficient of Performance of a Heat Pump

For a heat pump used for indoor heating, the desired thermodynamic output is the total heat delivered to the warm living space ($Q_H$), driven by electrical work input ($W_{\\text{net}}$):
$$\\text{COP}_{\\text{hp}} \\equiv \\frac{Q_H}{W_{\\text{net}}} = \\frac{Q_C + W_{\\text{net}}}{W_{\\text{net}}} = \\frac{Q_C}{W_{\\text{net}}} + 1 = \\beta + 1$$
For a Carnot heat pump:
$$\\text{COP}_{\\text{hp, Carnot}} = \\frac{T_H}{T_H - T_C}$$
Because $\\text{COP}_{\\text{hp}} > 1$ always, a heat pump delivers substantially more heating energy to a building than a direct electric resistive heater ($Q_H = W$, corresponding to $\\text{COP} = 1$) for the identical electricity consumption.
            """
        },
        {
            "id": "u2-sec5",
            "title": "Kelvin-Planck & Clausius Statements & Equivalence Proof",
            "content": """
### 1. Classical Statements of the Second Law

The Second Law of Thermodynamics encapsulates the macroscopic impossibility of certain hypothetical processes that satisfy energy conservation (First Law) but violate nature's arrow of time:
- **Kelvin-Planck Statement**: *It is impossible to construct a device operating in a thermodynamic cycle that produces no effect other than the extraction of heat from a single reservoir and the performance of an equivalent amount of mechanical work.* (A 100% efficient heat engine—a *perpetual motion machine of the second kind*—is physically impossible).
- **Clausius Statement**: *It is impossible to construct a device operating in a thermodynamic cycle that produces no effect other than the transfer of heat from a body at a lower temperature to a body at a higher temperature.* (Heat cannot spontaneously flow uphill from cold to hot without external work compensation).

### 2. Formal Proof of Logical Equivalence

To demonstrate that the Kelvin-Planck and Clausius statements are logically identical, we prove that a violation of either statement leads directly to a violation of the other.

#### Part A: Violation of Clausius $\\implies$ Violation of Kelvin-Planck
Suppose a hypothetical refrigerator $R_{\\text{anti-Clausius}}$ exists that violates the Clausius statement: it transfers heat $Q_C$ from a cold reservoir at $T_C$ to a hot reservoir at $T_H$ with zero net work input ($W = 0$).
Now couple this refrigerator to a standard heat engine $E$ operating between the same two reservoirs. Let engine $E$ absorb heat $Q_H$ from $T_H$, perform net work $W = Q_H - Q_C$, and reject heat $Q_C$ to $T_C$.
Consider the combined composite system:
- Heat rejected to cold reservoir: $+Q_C$ (from $E$) $- Q_C$ (into $R$) $= 0$.
- Net heat extracted from hot reservoir: $Q_H - Q_C$.
- Net work produced: $W = Q_H - Q_C$.

The composite machine operates in a complete cycle, extracts heat $(Q_H - Q_C)$ from a single reservoir at $T_H$, and converts 100% of it into work with zero thermal discharge to the cold reservoir. This directly violates the Kelvin-Planck statement.

#### Part B: Violation of Kelvin-Planck $\\implies$ Violation of Clausius
Suppose a hypothetical heat engine $E_{\\text{anti-Kelvin}}$ exists that violates the Kelvin-Planck statement: it absorbs heat $Q$ from a reservoir at $T_H$ and converts it entirely into work $W = Q$, rejecting zero heat to any sink.
Let this work $W$ drive a standard reversible Carnot refrigerator $R$ operating between reservoirs $T_H$ and $T_C$. The refrigerator absorbs heat $Q_C$ from the cold reservoir and delivers heat $Q_H' = Q_C + W = Q_C + Q$ to the hot reservoir.
Consider the combined composite system:
- Net work input/output: $W - W = 0$.
- Net heat extracted from cold reservoir: $Q_C$.
- Net heat delivered to hot reservoir: $Q_H' - Q = (Q_C + Q) - Q = Q_C$.

The composite system operates in a complete cycle and accomplishes nothing other than transferring heat $Q_C$ from a cold reservoir at $T_C$ to a hot reservoir at $T_H$ with zero work input. This directly violates the Clausius statement.

Hence, both statements are **rigorously equivalent**.
            """
        },
        {
            "id": "u2-sec6",
            "title": "Carnot's Theorem & The Thermodynamic Temperature Scale",
            "content": """
### 1. Carnot's Theorems

Sadi Carnot established two fundamental propositions governing all cyclic heat engines:
1. **Theorem 1**: *No heat engine operating between two given thermal reservoirs can be more efficient than a completely reversible Carnot engine operating between the same two reservoirs:*
$$\\eta_{\\text{irreversible}} \\le \\eta_{\\text{reversible}}$$
2. **Theorem 2**: *All completely reversible heat engines operating between the same two thermal reservoirs possess identical thermal efficiencies, regardless of the nature or phase of the working substance:*
$$\\eta_{\\text{rev, 1}} = \\eta_{\\text{rev, 2}} = \\eta(T_H, T_C)$$

### 2. Proof of Carnot's Theorem
Suppose an irreversible engine $I$ exists with efficiency greater than a reversible engine $R$: $\\eta_I > \\eta_R$.
Operate both engines between reservoirs $T_H$ and $T_C$ such that both deliver identical work output $W$:
$$W = \\eta_I Q_{H, I} = \\eta_R Q_{H, R} \\implies Q_{H, I} < Q_{H, R} \\quad (\\text{since } \\eta_I > \\eta_R)$$
Now run reversible engine $R$ in reverse as a refrigerator, driven by the work output $W$ of engine $I$.
The net heat absorbed from the hot reservoir by the combined engine-refrigerator assembly is:
$$Q_{\\text{net, hot}} = Q_{H, I} - Q_{H, R} < 0$$
Thus, net heat is delivered *to* the hot reservoir:
$$|Q_{\\text{net, hot}}| = Q_{H, R} - Q_{H, I} > 0$$
Since net work is zero ($W - W = 0$), the First Law requires that an equal quantity of heat must have been extracted from the cold reservoir:
$$Q_{\\text{net, cold}} = Q_{C, R} - Q_{C, I} = Q_{H, R} - Q_{H, I} > 0$$
The composite device operates in a cycle and transfers heat spontaneously from a cold reservoir to a hot reservoir with zero work input, violating the Clausius statement. Therefore, $\\eta_I > \\eta_R$ is impossible:
$$\\eta_I \\le \\eta_{\\text{Carnot}}$$

### 3. Absolute Thermodynamic Scale of Temperature (Kelvin Scale)

Because the efficiency of any reversible engine is independent of working material, the ratio $Q_H / Q_C$ must be a universal function solely of empirical reservoir temperatures $\\theta_H$ and $\\theta_C$:
$$\\frac{Q_H}{Q_C} = \\psi(\\theta_H, \\theta_C)$$
Consider a third reservoir at $\\theta_0$. Running two intermediate reversible engines gives:
$$\\frac{Q_H}{Q_0} = \\psi(\\theta_H, \\theta_0), \\quad \\frac{Q_C}{Q_0} = \\psi(\\theta_C, \\theta_0)$$
Dividing these equations:
$$\\frac{Q_H}{Q_C} = \\frac{\\psi(\\theta_H, \\theta_0)}{\\psi(\\theta_C, \\theta_0)} = \\frac{\\phi(\\theta_H)}{\\phi(\\theta_C)}$$
Lord Kelvin (William Thomson, 1848) chose the simplest linear assignment $\\phi(\\theta) \\equiv T$:
$$\\frac{Q_H}{Q_C} = \\frac{T_H}{T_C}$$
This defines the **Absolute Thermodynamic Temperature Scale**. Absolute zero ($T = 0\\text{ K}$) is defined as the temperature of a thermal sink that would permit a reversible engine to reject zero heat ($Q_C = 0$), yielding 100% efficiency. Because the ideal gas Carnot cycle yields $Q_H / Q_C = T_{\\text{gas, H}} / T_{\\text{gas, C}}$, the thermodynamic Kelvin scale is identical to the ideal gas temperature scale throughout its range of physical validity.
            """
        }
    ],
    "problems": [
        {
            "id": "u2-p1",
            "title": "Two-Stage Compound Carnot Engine Efficiency Optimization",
            "statement": "A compound heat engine consists of two Carnot engines connected in series. Engine A operates between a high-temperature reservoir at $T_H = 1200\\\\text{ K}$ and an intermediate reservoir at temperature $T_M$. Engine B absorbs the entire heat rejected by Engine A at temperature $T_M$ and exhausts heat to a low-temperature sink at $T_C = 300\\\\text{ K}$. (a) Determine the intermediate temperature $T_M$ if both engines produce identical work output ($W_A = W_B$). (b) Determine $T_M$ if both engines have identical thermal efficiencies ($\\\\eta_A = \\\\eta_B$). (c) Calculate the overall thermal efficiency of the compound system in both cases and compare with a single Carnot engine operating directly between $1200\\\\text{ K}$ and $300\\\\text{ K}$.",
            "steps": [
                {
                    "step": "Step 1: Intermediate Temperature for Equal Work Outputs ($W_A = W_B$)",
                    "detail": "Let Engine A absorb heat $Q_H$ at $T_H$ and reject $Q_M$ at $T_M$.\n$$W_A = Q_H - Q_M = Q_H \\\\left(1 - \\\\frac{T_M}{T_H}\\\\right)$$\nEngine B absorbs $Q_M$ at $T_M$ and rejects $Q_C$ at $T_C$:\n$$W_B = Q_M - Q_C = Q_M \\\\left(1 - \\\\frac{T_C}{T_M}\\\\right)$$\nUsing the Carnot relationship $Q_M / Q_H = T_M / T_H$, we have $Q_M = Q_H (T_M / T_H)$:\n$$W_B = Q_H \\\\left(\\\\frac{T_M}{T_H}\\\\right) \\\\left(1 - \\\\frac{T_C}{T_M}\\\\right) = Q_H \\\\left(\\\\frac{T_M - T_C}{T_H}\\\\right)$$\nSetting $W_A = W_B$:\n$$Q_H \\\\left(1 - \\\\frac{T_M}{T_H}\\\\right) = Q_H \\\\left(\\\\frac{T_M - T_C}{T_H}\\\\right) \\implies T_H - T_M = T_M - T_C$$\n$$2 T_M = T_H + T_C \\implies T_M = \\\\frac{T_H + T_C}{2}$$\nFor $T_H = 1200\\\\text{ K}$ and $T_C = 300\\\\text{ K}$:\n$$T_M = \\\\frac{1200 + 300}{2} = 750\\\\text{ K}$$\nThe intermediate temperature is the arithmetic mean."
                },
                {
                    "step": "Step 2: Intermediate Temperature for Equal Efficiencies ($\\\\eta_A = \\\\eta_B$)",
                    "detail": "Equating the two Carnot efficiencies:\n$$\\\\eta_A = 1 - \\\\frac{T_M}{T_H}, \\quad \\\\eta_B = 1 - \\\\frac{T_C}{T_M}$$\n$$1 - \\\\frac{T_M}{T_H} = 1 - \\\\frac{T_C}{T_M} \\implies \\\\frac{T_M}{T_H} = \\\\frac{T_C}{T_M}$$\n$$T_M^2 = T_H T_C \\implies T_M = \\\\sqrt{T_H T_C}$$\nFor $T_H = 1200\\\\text{ K}$ and $T_C = 300\\\\text{ K}$:\n$$T_M = \\\\sqrt{1200 \\\\times 300} = \\\\sqrt{360000} = 600\\\\text{ K}$$\nThe intermediate temperature is the geometric mean."
                },
                {
                    "step": "Step 3: Calculate Overall Compound Efficiency",
                    "detail": "The total work delivered by the series compound engine is $W_{\\\\text{total}} = W_A + W_B = (Q_H - Q_M) + (Q_M - Q_C) = Q_H - Q_C$.\nThe overall system efficiency is:\n$$\\\\eta_{\\\\text{overall}} = \\\\frac{W_{\\\\text{total}}}{Q_H} = 1 - \\\\frac{Q_C}{Q_H}$$\nSince both engines are reversible:\n$$\\\\frac{Q_C}{Q_H} = \\\\left(\\\\frac{Q_C}{Q_M}\\\\right) \\\\left(\\\\frac{Q_M}{Q_H}\\\\right) = \\\\left(\\\\frac{T_C}{T_M}\\\\right) \\\\left(\\\\frac{T_M}{T_H}\\\\right) = \\\\frac{T_C}{T_H}$$\n$$\\\\eta_{\\\\text{overall}} = 1 - \\\\frac{T_C}{T_H} = 1 - \\\\frac{300}{1200} = 1 - 0.25 = 0.75 \\\\quad (75.0\\\\%)$$\nRemarkably, the overall compound efficiency is strictly identical ($75.0\\\\%$) in both cases and exactly equal to a single Carnot engine operating directly between $1200\\\\text{ K}$ and $300\\\\text{ K}$."
                }
            ],
            "answer": "(a) For equal work: $T_M = 750\\\\text{ K}$ (arithmetic mean). (b) For equal efficiencies: $T_M = 600\\\\text{ K}$ (geometric mean). (c) Overall compound efficiency $\\\\eta = 75.0\\\\%$ in all configurations, matching a direct Carnot engine."
        },
        {
            "id": "u2-p2",
            "title": "Carnot Heat Pump vs Direct Resistance Heating Power Analysis",
            "statement": "A residential building requires a continuous heating rate of $\\\\dot{Q}_H = 24.0\\\\text{ kW}$ to maintain an interior temperature of $T_H = 21.0^\\\\circ\\\\text{C}$ ($294.15\\\\text{ K}$) during a winter day when outside ambient temperature is $T_C = -7.0^\\\\circ\\\\text{C}$ ($266.15\\\\text{ K}$). (a) Calculate the theoretical minimum electrical power input required to drive a Carnot heat pump. (b) If an actual real-world heat pump operates at $55.0\\\\%$ of the Carnot COP, calculate the real electrical power consumption. (c) Compare the daily operational electricity cost with direct electrical resistance heaters, assuming an electricity tariff of $\\\\0.15\\\\text{ per kWh}$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Carnot Heat Pump Coefficient of Performance",
                    "detail": "The ideal Carnot COP for heating is:\n$$\\\\text{COP}_{\\\\text{hp, Carnot}} = \\\\frac{T_H}{T_H - T_C} = \\\\frac{294.15}{294.15 - 266.15} = \\\\frac{294.15}{28.00} = 10.505$$"
                },
                {
                    "step": "Step 2: Minimum Electrical Power for Carnot Heat Pump",
                    "detail": "The electrical power input is:\n$$\\\\dot{W}_{\\\\text{min}} = \\\\frac{\\\\dot{Q}_H}{\\\\text{COP}_{\\\\text{hp, Carnot}}} = \\\\frac{24.0\\\\text{ kW}}{10.505} = 2.285\\\\text{ kW}$$\nThe heat pump extracts $\\\\dot{Q}_C = \\\\dot{Q}_H - \\\\dot{W} = 24.0 - 2.285 = 21.715\\\\text{ kW}$ of free thermal energy from the cold outside air."
                },
                {
                    "step": "Step 3: Actual Heat Pump Power Consumption",
                    "detail": "Given that the actual heat pump achieves $55.0\\\\%$ of Carnot COP:\n$$\\\\text{COP}_{\\\\text{actual}} = 0.55 \\\\times 10.505 = 5.778$$\nActual electrical power consumption is:\n$$\\\\dot{W}_{\\\\text{actual}} = \\\\frac{24.0\\\\text{ kW}}{5.778} = 4.154\\\\text{ kW}$$"
                },
                {
                    "step": "Step 4: Economic Cost Comparison Over 24 Hours",
                    "detail": "1. **Direct Electrical Resistance Heater** ($\\\\text{COP} = 1.00$):\n- Power required: $\\\\dot{W}_{\\\\text{resistive}} = 24.0\\\\text{ kW}$.\n- Daily energy consumed: $E_1 = (24.0\\\\text{ kW})(24\\\\text{ h}) = 576.0\\\\text{ kWh}$.\n- Daily cost: $576.0 \\\\times \\\\$0.15 = \\\\$86.40\\\\text{ per day}$.\n\n2. **Actual Heat Pump** ($\\\\text{COP} = 5.778$):\n- Power required: $4.154\\\\text{ kW}$.\n- Daily energy consumed: $E_2 = (4.154\\\\text{ kW})(24\\\\text{ h}) = 99.70\\\\text{ kWh}$.\n- Daily cost: $99.70 \\\\times \\\\$0.15 = \\\\$14.96\\\\text{ per day}$.\n\nDaily savings using the heat pump: $\\\\86.40 - \\\\$14.96 = \\\\$71.44\\\\text{ per day}$ ($82.7\\\\%$ cost reduction)."
                }
            ],
            "answer": "Minimum theoretical Carnot power $\\\\dot{W}_{\\\\text{min}} = 2.28\\\\text{ kW}$; actual heat pump power $\\\\dot{W}_{\\\\text{actual}} = 4.15\\\\text{ kW}$; daily operational cost is $\\\\14.96$ for the heat pump compared to $\\\\86.40$ for direct resistance heaters (saving $\\\\71.44\\\\text{/day}$)."
        },
        {
            "id": "u2-p3",
            "title": "Thermodynamic Refutation of a Super-Carnot Patent Claim",
            "statement": "An inventor files a patent application claiming to have developed a proprietary heat engine that operates between thermal reservoirs at $T_H = 800\\\\text{ K}$ and $T_C = 300\\\\text{ K}$, absorbing $Q_H = 1000\\\\text{ kJ}$ of heat per cycle and delivering $W = 680\\\\text{ kJ}$ of net mechanical work while exhausting $Q_C = 320\\\\text{ kJ}$ of heat. Prove via the Second Law of Thermodynamics (both Kelvin-Planck and Clausius formulations) that this device is physically impossible.",
            "steps": [
                {
                    "step": "Step 1: Check First Law Conservation",
                    "detail": "Energy balance over one cycle:\n$$\\\\Delta U = Q_H - Q_C - W = 1000\\\\text{ kJ} - 320\\\\text{ kJ} - 680\\\\text{ kJ} = 0\\\\text{ kJ}$$\nThe device satisfies the First Law of Thermodynamics."
                },
                {
                    "step": "Step 2: Compare Claimed Efficiency with Carnot Upper Limit",
                    "detail": "The claimed engine efficiency is:\n$$\\\\eta_{\\\\text{claimed}} = \\\\frac{W}{Q_H} = \\\\frac{680}{1000} = 0.680 \\\\quad (68.0\\\\%$$\nThe theoretical maximum reversible Carnot efficiency operating between these exact temperatures is:\n$$\\\\eta_{\\\\text{Carnot}} = 1 - \\\\frac{T_C}{T_H} = 1 - \\\\frac{300}{800} = 1 - 0.375 = 0.625 \\\\quad (62.5\\\\%$$\nNotice that $\\\\eta_{\\\\text{claimed}} = 68.0\\\\% > \\\\eta_{\\\\text{Carnot}} = 62.5\\\\%$. The engine claims to exceed the Carnot limit by $5.5\\\\%$."
                },
                {
                    "step": "Step 3: Formal Second Law Refutation via Kelvin-Planck Violation",
                    "detail": "Couple the inventor's claimed engine $X$ to a standard reversible Carnot refrigerator $R$ operating between the same reservoirs.\nLet refrigerator $R$ consume the $680\\\\text{ kJ}$ of work produced by engine $X$.\nThe COP of the Carnot refrigerator is:\n$$\\\\beta_{\\\\text{Carnot}} = \\\\frac{T_C}{T_H - T_C} = \\\\frac{300}{800 - 300} = \\\\frac{300}{500} = 0.600$$\nThe heat extracted from the cold reservoir by refrigerator $R$ is:\n$$Q_{C, R} = \\\\beta_{\\\\text{Carnot}} \\\\cdot W = 0.600 \\\\times 680\\\\text{ kJ} = 408\\\\text{ kJ}$$\nThe heat discharged to the hot reservoir by refrigerator $R$ is:\n$$Q_{H, R} = Q_{C, R} + W = 408 + 680 = 1088\\\\text{ kJ}$$\nNow examine the net performance of the combined composite system per cycle:\n- Net work produced: $W_X - W_R = 680 - 680 = 0\\\\text{ kJ}$.\n- Net heat extracted from cold reservoir: $Q_{C, R} - Q_{C, X} = 408 - 320 = +88\\\\text{ kJ}$.\n- Net heat delivered to hot reservoir: $Q_{H, R} - Q_{H, X} = 1088 - 1000 = +88\\\\text{ kJ}$.\n\nThe composite system produces no external work, operates in a complete cycle, and transfers $+88\\\\text{ kJ}$ of heat continuously from a cold reservoir at $300\\\\text{ K}$ to a hot reservoir at $800\\\\text{ K}$ with zero net energy input. This directly violates the Clausius statement of the Second Law of Thermodynamics."
                }
            ],
            "answer": "The claimed engine efficiency ($68.0\\\\%$) exceeds the theoretical Carnot limit ($62.5\\\\%$). Coupling it with a reversible Carnot refrigerator would spontaneously pump $88\\\\text{ kJ}$ of heat from $300\\\\text{ K}$ to $800\\\\text{ K}$ with zero net work, directly violating the Clausius statement of the Second Law."
        }
    ]
}

with open("tp_u1.json", "w") as f:
    json.dump(u1, f, indent=2)
print("tp_u1.json written successfully.")

with open("tp_u2.json", "w") as f:
    json.dump(u2, f, indent=2)
print("tp_u2.json written successfully.")
