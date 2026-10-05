import json

# Unit 3: Entropy & The Third Law
u3 = {
    "unitNumber": 3,
    "title": "Entropy & The Third Law of Thermodynamics",
    "description": "Macroscopic entropy, Clausius theorem and inequality, entropy of ideal gases and universal entropy growth, T-S diagrams, the Third Law (Nernst-Planck theorem), and Ehrenfest classification of phase transitions.",
    "sections": [
        {
            "id": "u3-sec1",
            "title": "Concept of Entropy & Clausius Theorem",
            "content": """
### 1. Clausius Theorem for Cyclic Reversible Processes

In 1854, Rudolf Clausius discovered that the Second Law implies the existence of a fundamental thermodynamic state function. Consider an arbitrary reversible cyclic process operating on a state plane $(P, V)$. 

Any arbitrary reversible cycle $\\mathcal{C}$ can be decomposed into an infinite grid of infinitesimal Carnot cycles operating between adjacent adiabats. For each infinitesimal Carnot cycle operating between reservoirs at temperatures $T_{1, i}$ and $T_{2, i}$:
$$\\frac{\\delta Q_{1, i}}{T_{1, i}} + \\frac{\\delta Q_{2, i}}{T_{2, i}} = 0$$
Summing over all sub-cycles, the internal adiabatic and isothermal paths cancel pairwise because each internal segment is traversed in opposite directions by adjacent cycles. The only uncompensated heat exchanges are along the outer closed boundary:
$$\\sum_{i} \\frac{\\delta Q_{\\text{rev}, i}}{T_i} = 0$$
Taking the continuum limit as the number of sub-cycles $N \\to \\infty$:
$$\\oint_{\\mathcal{C}} \\frac{\\delta Q_{\\text{rev}}}{T} = 0$$
This is **Clausius's Theorem**.

### 2. Definition of Entropy as a State Function

Because the cyclic integral of $\\frac{\\delta Q_{\\text{rev}}}{T}$ vanishes for every conceivable reversible loop, the line integral between any two equilibrium states $A$ and $B$ is strictly independent of the reversible path:
$$\\int_{\\text{Path 1}}^{A \\to B} \\frac{\\delta Q_{\\text{rev}}}{T} = \\int_{\\text{Path 2}}^{A \\to B} \\frac{\\delta Q_{\\text{rev}}}{T}$$
Consequently, $\\frac{\\delta Q_{\\text{rev}}}{T}$ is an **exact differential** of an extensive state function, which Clausius named **Entropy** ($S$):
$$dS \\equiv \\frac{\\delta Q_{\\text{rev}}}{T}$$
The finite entropy difference between states $A$ and $B$ is:
$$\\Delta S = S(B) - S(A) = \\int_A^B \\frac{\\delta Q_{\\text{rev}}}{T}$$
The absolute value of entropy is defined relative to an arbitrary reference state ($S_0$), until anchored by the Third Law.
            """
        },
        {
            "id": "u3-sec2",
            "title": "Clausius Inequality & Principle of Increase of Entropy",
            "content": """
### 1. The Clausius Inequality

Now consider a real, irreversible cyclic process $\\mathcal{C}$. Let the system absorb heat $\\delta Q$ at temperature $T$ during an irreversible forward path $A \\to B$, and return to initial state $A$ via an idealized reversible path $B \\to A$.
By Carnot's theorem, an irreversible engine is less efficient than a reversible engine:
$$\\eta_{\\text{irrev}} < \\eta_{\\text{rev}} \\implies \\oint \\frac{\\delta Q}{T} < 0$$
Combining reversible ($= 0$) and irreversible ($< 0$) cases yields the universal **Clausius Inequality**:
$$\\oint \\frac{\\delta Q}{T} \\le 0$$
where equality holds if and only if the entire cycle is strictly reversible.

### 2. The Second Law in Differential Form

Splitting the cyclic integral into the irreversible path $I$ ($A \\to B$) and reversible path $R$ ($B \\to A$):
$$\\int_{A, I}^B \\frac{\\delta Q}{T} + \\int_{B, R}^A \\frac{\\delta Q_{\\text{rev}}}{T} \\le 0$$
Since the second path is reversible, $\\int_{B, R}^A \\frac{\\delta Q_{\\text{rev}}}{T} = S_A - S_B = -\\Delta S$:
$$\\int_{A, I}^B \\frac{\\delta Q}{T} - \\Delta S \\le 0 \\implies \\Delta S \\ge \\int_{A, I}^B \\frac{\\delta Q}{T}$$
In differential form:
$$dS \\ge \\frac{\\delta Q}{T}$$
For an **isolated system**, which cannot exchange heat with its surroundings ($\delta Q = 0$):
$$dS_{\\text{isolated}} \\ge 0$$
This is the **Principle of Increase of Entropy**:
$$\\Delta S_{\\text{isolated}} > 0 \\quad (\\text{spontaneous natural processes}), \\quad \\Delta S_{\\text{isolated}} = 0 \\quad (\\text{reversible equilibrium})$$

### 3. Entropy of the Universe

Any system interacting with its environment can be embedded within an overall isolated composite universe:
$$\\Delta S_{\\text{universe}} = \\Delta S_{\\text{system}} + \\Delta S_{\\text{surroundings}} \\ge 0$$
While the entropy of a localized open subsystem can decrease (e.g., crystal freezing, living organism biological growth), it does so only by ejecting an even greater quantity of entropy into its surrounding environment, ensuring that total universal entropy relentlessly increases.
            """
        },
        {
            "id": "u3-sec3",
            "title": "Entropy of Ideal Gases & Irreversible Transformations",
            "content": """
### 1. Analytical Expressions for Ideal Gas Entropy

From the combined First and Second Laws for a reversible process in a simple fluid:
$$T dS = dU + P dV = C_v dT + P dV$$
For an ideal gas, substituting $dU = n C_{v, m} dT$ and $P = n R T / V$:
$$dS = n C_{v, m} \\frac{dT}{T} + n R \\frac{dV}{V}$$
Integrating from state $(T_1, V_1)$ to $(T_2, V_2)$:
$$S(T_2, V_2) - S(T_1, V_1) = n C_{v, m} \\ln\\left(\\frac{T_2}{T_1}\\right) + n R \\ln\\left(\\frac{V_2}{V_1}\\right)$$

Alternatively, using enthalpy $T dS = dH - V dP = n C_{p, m} dT - V dP$:
$$dS = n C_{p, m} \\frac{dT}{T} - n R \\frac{dP}{P}$$
$$S(T_2, P_2) - S(T_1, P_1) = n C_{p, m} \\ln\\left(\\frac{T_2}{T_1}\\right) - n R \\ln\\left(\\frac{P_2}{P_1}\\right)$$

### 2. Free Adiabatic Expansion (Joule Expansion)

Consider $n$ moles of an ideal gas expanding freely into an evacuated volume from $V_1$ to $V_2 = 2 V_1$ inside an adiabatic container:
- $Q = 0, W = 0 \\implies \\Delta U = 0 \\implies T_2 = T_1$.
- Because the expansion is irreversible, we cannot integrate $\\delta Q / T$ along the actual path.
- But because $S$ is a **state function**, $\\Delta S$ depends solely on initial and final states. We construct an imaginary reversible isothermal expansion connecting $(T_1, V_1)$ to $(T_1, V_2)$:
$$\\Delta S_{\\text{system}} = n R \\ln\\left(\\frac{V_2}{V_1}\\right) = n R \\ln 2 > 0$$
- Surroundings experience zero heat transfer: $\\Delta S_{\\text{surroundings}} = 0$.
- Total universal entropy generated:
$$\\Delta S_{\\text{universe}} = n R \\ln 2 > 0$$
This positive entropy change quantifies the intrinsic irreversibility of free expansion.
            """
        },
        {
            "id": "u3-sec4",
            "title": "Temperature-Entropy (T-S) Diagrams",
            "content": """
### 1. Representation of Thermodynamic Cycles on T-S Coordinates

The **Temperature-Entropy ($T$-$S$) diagram** provides deep geometric insight into thermodynamic transformations because the area under a reversible curve directly represents heat exchanged:
$$\\delta Q_{\\text{rev}} = T dS \\implies Q_{\\text{rev}} = \\int_1^2 T dS$$
- An **isothermal process** ($T = \\text{const}$) maps to a horizontal straight line.
- A **reversible adiabatic process** ($dS = 0$) maps to a vertical straight line (an *isentropic* process).

### 2. The Carnot Cycle on a T-S Diagram

On a $T$-$S$ plane, the Carnot cycle maps to an exact **rectangle**:
1. Stage $A \\to B$ (Isothermal expansion at $T_H$): Horizontal line from $S_A$ to $S_B$. Heat absorbed:
$$Q_H = \\text{Area under } AB = T_H (S_B - S_A) = T_H \\Delta S$$
2. Stage $B \\to C$ (Adiabatic expansion): Vertical line downward at constant entropy $S_B$ from $T_H$ to $T_C$ ($Q = 0$).
3. Stage $C \\to D$ (Isothermal compression at $T_C$): Horizontal line from $S_B$ back to $S_A$. Heat rejected:
$$Q_C = \\text{Area under } CD = T_C (S_B - S_A) = T_C \\Delta S$$
4. Stage $D \\to A$ (Adiabatic compression): Vertical line upward at constant entropy $S_A$ from $T_C$ back to $T_H$ ($Q = 0$).

### 3. Net Mechanical Work and Efficiency

The net mechanical work done per cycle is the enclosed area of the rectangle:
$$W_{\\text{net}} = Q_H - Q_C = (T_H - T_C)(S_B - S_A) = (T_H - T_C) \\Delta S$$
The thermal efficiency is the ratio of enclosed area to total area under the upper horizontal curve:
$$\\eta = \\frac{W_{\\text{net}}}{Q_H} = \\frac{(T_H - T_C) \\Delta S}{T_H \\Delta S} = 1 - \\frac{T_C}{T_H}$$
This offers an elegant geometric proof of Carnot efficiency.
            """
        },
        {
            "id": "u3-sec5",
            "title": "The Third Law of Thermodynamics & Unattainability of Absolute Zero",
            "content": """
### 1. Nernst Heat Theorem & Planck Formulation

In 1906, Walther Nernst observed that during chemical reactions between condensed phases, the entropy change $\\Delta S$ approaches zero as temperature approaches absolute zero:
$$\\lim_{T \\to 0} \\Delta S = 0$$
Max Planck (1911) generalized this into the **Third Law of Thermodynamics**:
$$\\text{The entropy of all pure, perfectly crystalline substances approaches a universal constant (which can be chosen as zero) as absolute temperature approaches zero:}$$
$$\\lim_{T \\to 0} S = 0$$

### 2. Physical Consequences of the Third Law

1. **Vanishing Heat Capacities**: The entropy of a substance at temperature $T$ is $S(T) = \\int_0^T \\frac{C_p(T')}{T'} dT'$. For this integral to converge at $T = 0$, $C_p$ and $C_v$ must vanish:
$$\\lim_{T \\to 0} C_p = 0, \\quad \\lim_{T \\to 0} C_v = 0$$
In quantum physics, Debye's law confirms $C_v \\propto T^3$ for non-metallic crystals and $C_v \\propto T$ for conduction electrons as $T \\to 0$.
2. **Vanishing Thermal Expansion**: Using Maxwell's relation $(\\partial V/\\partial T)_P = -(\\partial S/\\partial P)_T$, and since $S \\to 0$ independent of pressure:
$$\\lim_{T \\to 0} \\left(\\frac{\\partial V}{\\partial T}\\right)_P = 0 \\implies \\lim_{T \\to 0} \\alpha = 0$$

### 3. Principle of Unattainability of Absolute Zero

The Third Law is equivalent to the proposition: *It is physically impossible to reduce the temperature of any macroscopic system to absolute zero ($T = 0\\text{ K}$) in a finite number of thermodynamic operations.*

To cool a system, one alternates between isothermal parameter changes (e.g., magnetization $M$) and adiabatic changes (e.g., demagnetization). Because all isentropic curves converge to $S = 0$ at $T = 0\\text{ K}$, the temperature steps $\\Delta T$ achieved per cycle diminish asymptotically to zero as $T \\to 0$, requiring an infinite sequence of operations to reach $0\\text{ K}$.
            """
        },
        {
            "id": "u3-sec6",
            "title": "First and Second Order Phase Transitions",
            "content": """
### 1. Ehrenfest Classification Scheme

Paul Ehrenfest (1933) classified phase transitions according to the lowest order derivative of the Gibbs Free Energy $G(T, P)$ that displays a mathematical discontinuity:

### 2. First-Order Phase Transitions

A transition is **first-order** if the first partial derivatives of $G$ exhibit finite discontinuities across the phase boundary:
- Entropy discontinuity:
$$\\Delta S = S_2 - S_1 = -\\left[\\left(\\frac{\\partial G_2}{\\partial T}\\right)_P - \\left(\\frac{\\partial G_1}{\\partial T}\\right)_P\\right] = \\frac{L}{T} \\neq 0$$
where $L$ is the **latent heat** of transformation.
- Volume discontinuity:
$$\\Delta V = V_2 - V_1 = \\left(\\frac{\\partial G_2}{\\partial P}\\right)_T - \\left(\\frac{\\partial G_1}{\\partial P}\\right)_T \\neq 0$$
Examples include solid-liquid melting, liquid-vapor boiling, and solid-vapor sublimation. Along the coexistence curve, equality of chemical potentials $G_1(T, P) = G_2(T, P)$ leads directly to the **Clausius-Clapeyron equation**:
$$\\frac{dP}{dT} = \\frac{\\Delta S}{\\Delta V} = \\frac{L}{T \\Delta V}$$

### 3. Second-Order Phase Transitions

A transition is **second-order** (continuous) if the first derivatives of $G$ are continuous ($\Delta S = 0, \Delta V = 0, L = 0$), but the second partial derivatives exhibit finite jump discontinuities or power-law divergences:
1. **Specific Heat Discontinuity**:
$$\\Delta C_p = -T \\left[ \\left(\\frac{\\partial^2 G_2}{\\partial T^2}\\right)_P - \\left(\\frac{\\partial^2 G_1}{\\partial T^2}\\right)_P \\right]$$
2. **Thermal Expansion Discontinuity**:
$$\\Delta \\alpha = \\frac{1}{V} \\left[ \\frac{\\partial^2 G_2}{\\partial T \\partial P} - \\frac{\\partial^2 G_1}{\\partial T \\partial P} \\right]$$
3. **Isothermal Compressibility Discontinuity**:
$$\\Delta \\kappa_T = -\\frac{1}{V} \\left[ \\left(\\frac{\\partial^2 G_2}{\\partial P^2}\\right)_T - \\left(\\frac{\\partial^2 G_1}{\\partial P^2}\\right)_T \\right]$$

Examples include:
- Ferromagnetic to paramagnetic transition at the Curie temperature $T_C$.
- Superconducting transition in zero external magnetic field.
- Order-disorder transitions in binary metal alloys (e.g., $\\beta$-brass).
- Liquid Helium-4 normal to superfluid lambda transition at $T_\\lambda = 2.17\\text{ K}$.
            """
        }
    ],
    "problems": [
        {
            "id": "u3-p1",
            "title": "Thermal Equilibration of Two Identical Solid Blocks",
            "statement": "Two identical blocks of copper, each of mass $m = 2.50\\\\text{ kg}$ and constant specific heat capacity $c = 385\\\\text{ J/(kg}\\\\cdot\\\\text{K)}$, are initially at temperatures $T_1 = 373.15\\\\text{ K}$ ($100^\\\\circ\\\\text{C}$) and $T_2 = 273.15\\\\text{ K}$ ($0^\\\\circ\\\\text{C}$). The blocks are brought into thermal contact inside a thermally insulated calorimeter until they reach mutual equilibrium. (a) Calculate the final equilibrium temperature $T_f$. (b) Calculate the entropy change of Block 1, Block 2, and the universe. (c) If a Carnot engine had been operated reversibly between the two blocks to extract the maximum mechanical work while bringing them to equilibrium, calculate the final common temperature $T_f'$ and the maximum work delivered $W_{\\\\max}$.",
            "steps": [
                {
                    "step": "Step 1: Final Temperature under Direct Irreversible Contact",
                    "detail": "By energy conservation in an insulated system ($Q_1 + Q_2 = 0$):\n$$m c (T_f - T_1) + m c (T_f - T_2) = 0 \\implies 2 T_f = T_1 + T_2$$\n$$T_f = \\\\frac{T_1 + T_2}{2} = \\\\frac{373.15 + 273.15}{2} = 323.15\\\\text{ K} = 50.0^\\\\circ\\\\text{C}$$\nThe final temperature is the arithmetic mean."
                },
                {
                    "step": "Step 2: Entropy Changes in Irreversible Thermal Contact",
                    "detail": "For each block, entropy change is integrated via $\\\\Delta S = \\\\int \\\\frac{m c dT}{T} = m c \\\\ln\\\\left(\\\\frac{T_f}{T_i}\\\\right)$:\nTotal heat capacity $C = m c = (2.50)(385) = 962.5\\\\text{ J/K}$.\n$$\\\\Delta S_1 = C \\\\ln\\\\left(\\\\frac{323.15}{373.15}\\\\right) = 962.5 \\\\ln(0.8660) = 962.5(-0.14387) = -138.48\\\\text{ J/K}$$\n$$\\\\Delta S_2 = C \\\\ln\\\\left(\\\\frac{323.15}{273.15}\\\\right) = 962.5 \\\\ln(1.1830) = 962.5(+0.16809) = +161.79\\\\text{ J/K}$$\nNet universal entropy production is:\n$$\\\\Delta S_{\\\\text{univ}} = \\\\Delta S_1 + \\\\Delta S_2 = -138.48 + 161.79 = +23.31\\\\text{ J/K}$$\nSince $\\\\Delta S_{\\\\text{univ}} > 0$, the process is spontaneously irreversible."
                },
                {
                    "step": "Step 3: Reversible Extraction of Maximum Work via Carnot Engine",
                    "detail": "For a reversible process operating between the two finite blocks, the total entropy change of the universe must be zero:\n$$\\\\Delta S_{\\\\text{univ}} = \\\\Delta S_1 + \\\\Delta S_2 = C \\\\ln\\\\left(\\\\frac{T_f'}{T_1}\\\\right) + C \\\\ln\\\\left(\\\\frac{T_f'}{T_2}\\\\right) = 0$$\n$$C \\\\ln\\\\left(\\\\frac{(T_f')^2}{T_1 T_2}\\\\right) = 0 \\implies (T_f')^2 = T_1 T_2 \\implies T_f' = \\\\sqrt{T_1 T_2}$$\nThe reversible final temperature is the geometric mean:\n$$T_f' = \\\\sqrt{(373.15)(273.15)} = \\\\sqrt{101915.9} = 319.24\\\\text{ K} = 46.09^\\\\circ\\\\text{C}$$\nNotice $T_f' < T_f$ because energy has been extracted from the blocks as useful mechanical work."
                },
                {
                    "step": "Step 4: Maximum Work Delivered $W_{\\\\max}$",
                    "detail": "By the First Law, the work delivered is the decrease in total internal energy of both blocks:\n$$W_{\\\\max} = -(\\\\Delta U_1 + \\\\Delta U_2) = C (T_1 - T_f') + C (T_2 - T_f') = C (T_1 + T_2 - 2 T_f')$$\n$$W_{\\\\max} = 962.5 [ 373.15 + 273.15 - 2(319.24) ] = 962.5 [ 646.30 - 638.48 ] = 962.5 (7.82) = 7526.8\\\\text{ J} = 7.53\\\\text{ kJ}$$"
                }
            ],
            "answer": "(a) Direct thermal contact: $T_f = 323.15\\\\text{ K}$ ($50.0^\\\\circ\\\\text{C}$). (b) $\\\\Delta S_1 = -138.5\\\\text{ J/K}$, $\\\\Delta S_2 = +161.8\\\\text{ J/K}$, $\\\\Delta S_{\\\\text{univ}} = +23.3\\\\text{ J/K}$. (c) Reversible work extraction: $T_f' = 319.24\\\\text{ K}$ ($46.1^\\\\circ\\\\text{C}$) and $W_{\\\\max} = 7.53\\\\text{ kJ}$."
        },
        {
            "id": "u3-p2",
            "title": "Entropy of Free Gas Expansion vs Irreversible Heat Transfer",
            "statement": "An insulated rigid tank is divided into two equal compartments, each of volume $V_0 = 0.050\\\\text{ m}^3$, by a partition. One compartment contains $n = 3.00\\\\text{ mol}$ of an ideal gas at $T_0 = 400.0\\\\text{ K}$, and the second compartment is evacuated. The partition ruptures, and the gas expands freely to fill the entire container. Subsequently, the gas is placed in thermal contact with a large heat reservoir at $T_R = 300.0\\\\text{ K}$ until thermal equilibrium is attained. Calculate: (a) the entropy change of the gas during the free expansion stage, (b) the entropy change of the gas during cooling, (c) the entropy change of the reservoir during cooling, and (d) the total entropy generation of the universe across both stages.",
            "steps": [
                {
                    "step": "Step 1: Free Expansion Stage Entropy Change",
                    "detail": "During free expansion into vacuum, $Q = 0$ and $W = 0$, so $\\\\Delta U = 0$ and $T_1 = T_0 = 400.0\\\\text{ K}$.\nThe volume doubles: $V_1 = 2 V_0 = 0.100\\\\text{ m}^3$.\n$$\\\\Delta S_{\\\\text{gas, 1}} = n R \\\\ln\\\\left(\\\\frac{V_1}{V_0}\\\\right) = (3.00\\\\text{ mol})(8.314\\\\text{ J/(mol}\\\\cdot\\\\text{K)}) \\\\ln(2) = (24.942)(0.69315) = +17.29\\\\text{ J/K}$$\nThe isolated surroundings experience zero change: $\\\\Delta S_{\\\\text{surr, 1}} = 0$.\n$$\\\\Delta S_{\\\\text{univ, 1}} = +17.29\\\\text{ J/K}$$"
                },
                {
                    "step": "Step 2: Cooling Stage Entropy Change of the Gas",
                    "detail": "During cooling at constant volume $V_1$ from $T_1 = 400.0\\\\text{ K}$ to $T_2 = 300.0\\\\text{ K}$ for an ideal gas with $C_v = \\\\frac{5}{2} R$ (diatomic gas):\n$$C_v = \\\\frac{5}{2} (8.314) = 20.785\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\n$$\\\\Delta S_{\\\\text{gas, 2}} = n C_v \\\\ln\\\\left(\\\\frac{T_2}{T_1}\\\\right) = (3.00)(20.785) \\\\ln\\\\left(\\\\frac{300.0}{400.0}\\\\right) = (62.355)(-0.28768) = -17.94\\\\text{ J/K}$$"
                },
                {
                    "step": "Step 3: Entropy Change of the Reservoir",
                    "detail": "The heat released by the gas during isochoric cooling is:\n$$Q_{\\\\text{gas}} = n C_v (T_2 - T_1) = (3.00)(20.785)(300 - 400) = -6235.5\\\\text{ J}$$\nThe reservoir absorbs heat $Q_{\\\\text{res}} = -Q_{\\\\text{gas}} = +6235.5\\\\text{ J}$ at constant temperature $T_R = 300.0\\\\text{ K}$:\n$$\\\\Delta S_{\\\\text{res}} = \\\\frac{Q_{\\\\text{res}}}{T_R} = \\\\frac{+6235.5\\\\text{ J}}{300.0\\\\text{ K}} = +20.785\\\\text{ J/K}$$"
                },
                {
                    "step": "Step 4: Total Entropy Generation of the Universe",
                    "detail": "For stage 2 (thermal cooling across finite temperature difference):\n$$\\\\Delta S_{\\\\text{univ, 2}} = \\\\Delta S_{\\\\text{gas, 2}} + \\\\Delta S_{\\\\text{res}} = -17.94 + 20.79 = +2.85\\\\text{ J/K}$$\nSumming both irreversible stages:\n$$\\\\Delta S_{\\\\text{univ, total}} = \\\\Delta S_{\\\\text{univ, 1}} + \\\\Delta S_{\\\\text{univ, 2}} = +17.29 + 2.85 = +20.14\\\\text{ J/K}$$"
                }
            ],
            "answer": "(a) Free expansion gas entropy $\\\\Delta S_{\\\\text{gas, 1}} = +17.29\\\\text{ J/K}$. (b) Cooling gas entropy $\\\\Delta S_{\\\\text{gas, 2}} = -17.94\\\\text{ J/K}$. (c) Reservoir entropy $\\\\Delta S_{\\\\text{res}} = +20.79\\\\text{ J/K}$. (d) Total universal entropy produced $\\\\Delta S_{\\\\text{univ}} = +20.14\\\\text{ J/K}$."
        },
        {
            "id": "u3-p3",
            "title": "Third Law Low-Temperature Debye Entropy Integration",
            "statement": "At low temperatures ($T < 20\\\\text{ K}$), the molar heat capacity of solid silver obeys the Debye cubic power law $C_{v, m}(T) = a T^3$, where $a = 1.70\\\\times 10^{-4}\\\\text{ J/(mol}\\\\cdot\\\\text{K}^4)$. (a) Verify that this relation satisfies the Third Law of Thermodynamics. (b) Calculate the absolute molar entropy of silver at $T = 15.0\\\\text{ K}$. (c) Calculate the heat absorbed per mole when warming from $0\\\\text{ K}$ to $15.0\\\\text{ K}$ and compare the heat absorbed with the product $T S(T)$.",
            "steps": [
                {
                    "step": "Step 1: Verify Third Law Compliance",
                    "detail": "According to the Third Law (Nernst-Planck theorem), $C_v \\\\to 0$ as $T \\\\to 0$.\n$$\\\\lim_{T \\\\to 0} C_{v, m}(T) = \\\\lim_{T \\\\to 0} (a T^3) = 0$$\nFurthermore, the entropy integral at the lower limit is:\n$$S(T) = \\\\int_0^T \\\\frac{C_v(T')}{T'} dT' = \\\\int_0^T a (T')^2 dT' = \\\\frac{a T^3}{3}$$\nSince $\\\\lim_{T \\\\to 0} S(T) = 0$, the expression strictly obeys the Third Law without logarithmic divergences."
                },
                {
                    "step": "Step 2: Calculate Absolute Molar Entropy at $15.0\\\\text{ K}$",
                    "detail": "Evaluating at $T = 15.0\\\\text{ K}$:\n$$S(15.0) = \\\\frac{a (15.0)^3}{3} = \\\\frac{(1.70 \\\\times 10^{-4})(3375)}{3} = \\\\frac{0.57375}{3} = 0.19125\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\nNotice that the molar heat capacity at this temperature is:\n$$C_v(15.0) = a (15.0)^3 = 0.57375\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$$\nRemarkably, $S(T) = \\\\frac{1}{3} C_v(T)$ for any substance obeying Debye's $T^3$ law."
                },
                {
                    "step": "Step 3: Calculate Heat Absorbed and Compare with $T S(T)$",
                    "detail": "The total heat absorbed per mole from $0\\\\text{ K}$ to $T$ is:\n$$Q = \\\\int_0^T C_v(T') dT' = \\\\int_0^T a (T')^3 dT' = \\\\frac{a T^4}{4}$$\nEvaluating at $T = 15.0\\\\text{ K}$ ($15^4 = 50625$):\n$$Q = \\\\frac{(1.70 \\\\times 10^{-4})(50625)}{4} = \\\\frac{8.60625}{4} = 2.1516\\\\text{ J/mol}$$\nComparing with the product $T S(T)$:\n$$T S(T) = T \\\\left(\\\\frac{a T^3}{3}\\\\right) = \\\\frac{a T^4}{3} = \\\\frac{8.60625}{3} = 2.8688\\\\text{ J/mol}$$\n$$Q = \\\\frac{3}{4} T S(T)$$\nThis shows that $25\\\\%$ of the thermal energy $T S$ represents bound unavailable energy locked within the low-frequency phonon modes."
                }
            ],
            "answer": "(a) $C_v \\\\to 0$ and $S \\\\to 0$ as $T \\\\to 0$, rigorously satisfying the Third Law. (b) Absolute molar entropy $S(15.0\\\\text{ K}) = 0.191\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$. (c) Heat absorbed $Q = 2.15\\\\text{ J/mol}$, satisfying the exact scaling $Q = \\\\frac{3}{4} T S$."
        }
    ]
}

# Unit 4: Thermodynamic Potentials
u4 = {
    "unitNumber": 4,
    "title": "Thermodynamic Potentials & Cryogenics",
    "description": "Legendre transformations, Internal Energy, Enthalpy, Helmholtz and Gibbs Free Energies, thermodynamic equilibrium criteria, liquid surface interfaces, magnetic work, and cooling by adiabatic demagnetization.",
    "sections": [
        {
            "id": "u4-sec1",
            "title": "Extensive & Intensive Variables & Euler Relations",
            "content": """
### 1. Mathematical Scaling of Thermodynamic Functions

A state variable $X$ is **extensive** if scaling the system size by a positive parameter $\\lambda$ scales the variable by $\\lambda$: $X(\\lambda N, \\lambda V) = \\lambda X(N, V)$. A state variable $Y$ is **intensive** if it remains invariant: $Y(\\lambda N, \\lambda V) = Y(N, V)$.

Let the fundamental relation for internal energy be $U = U(S, V, N)$. Because $S, V, N$ are all extensive:
$$U(\\lambda S, \\lambda V, \\lambda N) = \\lambda U(S, V, N)$$
Differentiating with respect to $\\lambda$ via the chain rule:
$$\\frac{\\partial U}{\\partial (\\lambda S)} \\frac{d(\\lambda S)}{d\\lambda} + \\frac{\\partial U}{\\partial (\\lambda V)} \\frac{d(\\lambda V)}{d\\lambda} + \\frac{\\partial U}{\\partial (\\lambda N)} \\frac{d(\\lambda N)}{d\\lambda} = U(S, V, N)$$
Setting $\\lambda = 1$:
$$S \\left(\\frac{\\partial U}{\\partial S}\\right)_{V, N} + V \\left(\\frac{\\partial U}{\\partial V}\\right)_{S, N} + N \\left(\\frac{\\partial U}{\\partial N}\\right)_{S, V} = U$$
Recalling definitions of temperature $T = (\\partial U/\\partial S)_{V, N}$, hydrostatic pressure $P = -(\\partial U/\\partial V)_{S, N}$, and chemical potential $\\mu = (\\partial U/\\partial N)_{S, V}$, we obtain the fundamental **Euler Equation**:
$$U = T S - P V + \\mu N$$

### 2. The Gibbs-Duhem Relation

Taking the total differential of the Euler equation:
$$dU = T dS + S dT - P dV - V dP + \\mu dN + N d\\mu$$
Subtracting the fundamental differential relation $dU = T dS - P dV + \\mu dN$:
$$S dT - V dP + N d\\mu = 0$$
This is the **Gibbs-Duhem Relation**. It demonstrates that the intensive parameters $(T, P, \\mu)$ of a single-component system cannot all vary independently; varying any two strictly determines the third.
            """
        },
        {
            "id": "u4-sec2",
            "title": "The Four Fundamental Potentials (U, H, F, G)",
            "content": """
### 1. Legendre Transformations

In experimental physics, controlling extensive entropy $S$ is difficult; controlling intensive temperature $T$ using a thermal bath is straightforward. Legendre transformations systematically replace an extensive variable with its conjugate intensive derivative without losing any fundamental thermodynamic information.

### 2. The Four Potentials and Natural Variables

1. **Internal Energy** $U(S, V)$:
$$dU = T dS - P dV + \\mu dN$$
Natural variables: $(S, V, N)$.
Conjugate relations: $T = \\left(\\frac{\\partial U}{\\partial S}\\right)_{V}$, $P = -\\left(\\frac{\\partial U}{\\partial V}\\right)_{S}$.

2. **Enthalpy** $H(S, P) \\equiv U + P V$:
$$dH = dU + P dV + V dP = (T dS - P dV) + P dV + V dP = T dS + V dP$$
Natural variables: $(S, P, N)$.
Conjugate relations: $T = \\left(\\frac{\\partial H}{\\partial S}\\right)_{P}$, $V = \\left(\\frac{\\partial H}{\\partial P}\\right)_{S}$.
Enthalpy represents heat transferred under constant pressure ($dH = \\delta Q_P$).

3. **Helmholtz Free Energy** $F(T, V) \\equiv U - T S$:
$$dF = dU - T dS - S dT = (T dS - P dV) - T dS - S dT = -S dT - P dV$$
Natural variables: $(T, V, N)$.
Conjugate relations: $S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_{V}$, $P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_{T}$.
Helmholtz free energy represents the **maximum reversible work** extractable from a system during an isothermal process: $W_{\\max} = -\\Delta F$.

4. **Gibbs Free Energy** $G(T, P) \\equiv H - T S = U + P V - T S$:
$$dG = dH - T dS - S dT = (T dS + V dP) - T dS - S dT = -S dT + V dP$$
Natural variables: $(T, P, N)$.
Conjugate relations: $S = -\\left(\\frac{\\partial G}{\\partial T}\\right)_{P}$, $V = \\left(\\frac{\\partial G}{\\partial P}\\right)_{T}$.
From Euler's relation $U = TS - PV + \\mu N$, we obtain $G = \\mu N$, proving that chemical potential $\\mu = G/N$ is simply molar/molecular Gibbs free energy.
            """
        },
        {
            "id": "u4-sec3",
            "title": "Equilibrium Criteria & Extremum Principles",
            "content": """
### 1. Thermodynamic Equilibrium Criteria

From the Clausius inequality for a non-isolated system in contact with surroundings at temperature $T_0$ and pressure $P_0$:
$$dU \\le T_0 dS - P_0 dV$$

Applying this inequality to constrained systems generates specific **extremum principles**:
1. **Isolated System** ($U, V$ constant):
$$dS_{U, V} \\ge 0 \\implies S \\text{ is a maximum at equilibrium.}$$
2. **System at Constant Entropy and Volume** ($S, V$ constant):
$$dU_{S, V} \\le 0 \\implies U \\text{ is a minimum at equilibrium.}$$
3. **System at Constant Temperature and Volume** ($T = T_0, V$ constant):
$$d(U - T S)_{T, V} \\le 0 \\implies dF_{T, V} \\le 0 \\implies F \\text{ is a minimum at equilibrium.}$$
4. **System at Constant Temperature and Pressure** ($T = T_0, P = P_0$):
$$d(U - T S + P V)_{T, P} \\le 0 \\implies dG_{T, P} \\le 0 \\implies G \\text{ is a minimum at equilibrium.}$$

### 2. Practical Importance of Gibbs Energy Minimum

Most real-world chemical reactions, phase transitions, and biological processes occur at constant atmospheric pressure and ambient temperature. Therefore:
$$\\Delta G < 0 \\implies \\text{Process is thermodynamically spontaneous.}$$
$$\\Delta G = 0 \\implies \\text{System is in dynamic phase/chemical equilibrium.}$$
$$\\Delta G > 0 \\implies \\text{Process is non-spontaneous (requires external work input).}$$
            """
        },
        {
            "id": "u4-sec4",
            "title": "Thermodynamics of Liquid Surface Films",
            "content": """
### 1. Interfacial Work and Surface Free Energy

Creating an interface of area $A$ requires pulling molecules from the bulk liquid against attractive intermolecular cohesive forces to the surface. The work performed to expand surface area by $dA$ at surface tension $\\gamma$ is:
$$\\delta W = -\\gamma dA$$
Including interfacial work in the fundamental First Law relation:
$$dU = T dS - P dV + \\gamma dA$$
For the Helmholtz free energy $F = U - TS$:
$$dF = -S dT - P dV + \\gamma dA$$
At constant temperature and volume:
$$\\gamma = \\left(\\frac{\\partial F}{\\partial A}\\right)_{T, V} = \\left(\\frac{\\partial G}{\\partial A}\\right)_{T, P}$$
Thus, **surface tension is the surface Helmholtz/Gibbs free energy per unit area**.

### 2. Temperature Dependence of Surface Tension & Total Surface Energy

Applying Maxwell's cross-derivative reciprocity to $dF$:
$$\\left(\\frac{\\partial S}{\\partial A}\\right)_{T, V} = -\\left(\\frac{\\partial \\gamma}{\\partial T}\\right)_A$$
Since surface tension decreases monotonically with temperature ($d\\gamma/dT < 0$), surface entropy per unit area $s_A = -d\\gamma/dT$ is positive; creating new surface area absorbs heat isothermally ($q_A = T s_A = -T d\\gamma/dT$).

The **Total Surface Internal Energy Density** $u_A = U_A / A$ is:
$$u_A = f_A + T s_A = \\gamma - T \\left(\\frac{d\\gamma}{dT}\\right)$$
Because $d\\gamma/dT < 0$, total surface energy $u_A$ is strictly greater than surface tension $\\gamma$.
            """
        },
        {
            "id": "u4-sec5",
            "title": "Magnetic Thermodynamics & Adiabatic Demagnetization",
            "content": """
### 1. Thermodynamics of Magnetic Systems

For a paramagnetic material placed inside an external magnetic field $\\vec{H}$, work done by the magnetic field generator to alter total sample magnetic dipole moment $\\vec{M}$ is:
$$\\delta W_{\\text{mag}} = -\\mu_0 \\vec{H} \\cdot d\\vec{M}$$
The fundamental thermodynamic relation becomes:
$$dU = T dS - P dV + \\mu_0 H dM$$
Neglecting small magnetostrictive volume changes ($dV \\approx 0$):
$$dU = T dS + \\mu_0 H dM$$
The magnetic Gibbs free energy is defined as $G_{\\text{mag}} = U - TS - \\mu_0 HM$:
$$dG_{\\text{mag}} = -S dT - \\mu_0 M dH$$

### 2. Curie's Law and Spin Entropy

For an ideal paramagnetic salt (e.g., cerium magnesium nitrate, gadolinium sulfate), the magnetic dipoles follow Curie's law:
$$M = \\frac{C H}{T}$$
Applying Maxwell's cross-derivative to $dG_{\\text{mag}}$:
$$\\left(\\frac{\\partial S}{\\partial H}\\right)_T = \\mu_0 \\left(\\frac{\\partial M}{\\partial T}\\right)_H = -\\mu_0 \\frac{C H}{T^2} < 0$$
Applying an external magnetic field forces randomly tumbling atomic spins to align parallel to $\\vec{H}$, drastically reducing spin orientation entropy ($S_{\\text{spin}}$).

### 3. Cooling by Adiabatic Demagnetization

Adiabatic demagnetization (proposed by Debye and Giauque in 1926) achieves sub-millikelvin temperatures through a two-stage thermodynamic sequence:
1. **Isothermal Magnetization ($A \\to B$)**: The paramagnetic salt is immersed in a liquid helium bath at $T_i \\approx 1.0\\text{ K}$. A powerful magnetic field ($H_i \\sim 2\\text{ to } 5\\text{ T}$) is applied. The spins align, releasing heat of magnetization $Q = T_i \\Delta S_{\\text{mag}}$ to the helium bath via helium exchange gas.
2. **Adiabatic Demagnetization ($B \\to C$)**: The exchange gas is pumped out to thermally isolate the salt. The external magnetic field is reduced slowly to zero ($H \\to 0$).
Because the process is isentropic ($\Delta S_{\\text{total}} = 0$):
$$S_{\\text{spin}}(H_i, T_i) + S_{\\text{lattice}}(T_i) = S_{\\text{spin}}(0, T_f) + S_{\\text{lattice}}(T_f)$$
As $H \\to 0$, the magnetic spins disorder thermally, absorbing entropy and heat from the crystal lattice vibrations, causing the lattice temperature to plummet:
$$T_f = T_i \\frac{\\sqrt{h_{\\text{int}}^2}}{H_i} = T_i \\frac{h_{\\text{int}}}{H_i}$$
where $h_{\\text{int}} \\sim 0.01\\text{ T}$ is the small internal local dipole field of the crystal. By this technique, temperatures down to $10^{-3}\\text{ K}$ (electronic demagnetization) and $10^{-6}\\text{ K}$ (nuclear demagnetization of copper nuclei) are routinely achieved.
            """
        }
    ],
    "problems": [
        {
            "id": "u4-p1",
            "title": "Surface Film Cooling During Reversible Adiabatic Expansion",
            "statement": "A soap film stretched across a rectangular wire frame has a surface area of $A = 0.0200\\\\text{ m}^2$ at temperature $T_0 = 293.15\\\\text{ K}$. Its surface tension follows the linear empirical relation $\\\\gamma(T) = \\\\gamma_0 - b(T - T_0)$, where $\\\\gamma_0 = 0.0280\\\\text{ N/m}$ and $b = 1.40\\\\times 10^{-4}\\\\text{ N/(m}\\\\cdot\\\\text{K)}$. The total heat capacity of the liquid film is $C = 8.40\\\\text{ J/K}$. (a) Calculate the total surface energy density $u_A$ at $T_0$. (b) If the film area is stretched reversibly and adiabatically from $A_1 = 0.0200\\\\text{ m}^2$ to $A_2 = 0.0600\\\\text{ m}^2$, derive and calculate the resulting temperature drop $\\\\Delta T$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Total Surface Energy Density $u_A$",
                    "detail": "The surface internal energy density is:\n$$u_A = \\\\gamma - T \\\\left(\\\\frac{d\\\\gamma}{dT}\\\\right)$$\nGiven $\\\\frac{d\\\\gamma}{dT} = -b = -1.40 \\\\times 10^{-4}\\\\text{ N/(m}\\\\cdot\\\\text{K)}$:\n$$u_A = 0.0280 - (293.15)(-1.40 \\\\times 10^{-4}) = 0.0280 + 0.04104 = 0.06904\\\\text{ J/m}^2$$\nNotice that total surface internal energy is nearly $2.5\\\\times$ greater than surface tension $\\\\gamma$, because creating surface absorbs latent heat of orientation."
                },
                {
                    "step": "Step 2: Formulate Differential Equation for Adiabatic Stretching",
                    "detail": "For a reversible adiabatic process ($dS = 0$), the total entropy is a function of temperature and area, $S = S(T, A)$:\n$$dS = \\\\left(\\\\frac{\\\\partial S}{\\partial T}\\\\right)_A dT + \\\\left(\\\\frac{\\\\partial S}{\\\\partial A}\\\\right)_T dA = 0$$\nRecalling that $\\\\left(\\\\frac{\\\\partial S}{\\\\partial T}\\\\right)_A = \\\\frac{C}{T}$ and from Maxwell's relation $\\\\left(\\\\frac{\\\\partial S}{\\\\partial A}\\\\right)_T = -\\\\frac{d\\\\gamma}{dT} = b$:\n$$\\\\frac{C}{T} dT + b dA = 0 \\implies dT = -\\\\frac{b T}{C} dA$$\nSince $\\\\Delta T \\\\ll T_0$, we can approximate $T \\\\approx T_0$:\n$$\\\\Delta T = -\\\\frac{b T_0}{C} \\\\Delta A$$"
                },
                {
                    "step": "Step 3: Numerical Evaluation of Temperature Drop",
                    "detail": "The increase in surface area is $\\\\Delta A = A_2 - A_1 = 0.0600 - 0.0200 = 0.0400\\\\text{ m}^2$.\n$$\\\\Delta T = -\\\\frac{(1.40 \\\\times 10^{-4}\\\\text{ N/(m}\\\\cdot\\\\text{K)})(293.15\\\\text{ K})}{8.40\\\\text{ J/K}} (0.0400\\\\text{ m}^2)$$\n$$\\\\Delta T = -\\\\frac{0.04104}{8.40} \\\\times 0.0400 = - (0.004886)(0.0400) = -1.954 \\\\times 10^{-4}\\\\text{ K}$$\nFor double-sided soap film (two interfaces, area $2\\\\Delta A$):\n$$\\\\Delta T_{\\\\text{film}} = 2 \\\\times (-1.954 \\\\times 10^{-4}\\\\text{ K}) = -3.91 \\\\times 10^{-4}\\\\text{ K} = -0.391\\\\text{ mK}$$"
                }
            ],
            "answer": "(a) Total surface energy density $u_A = 0.0690\\\\text{ J/m}^2$. (b) Adiabatic stretching produces a cooling effect of $\\\\Delta T = -0.391\\\\text{ mK}$ for a double-sided soap film."
        },
        {
            "id": "u4-p2",
            "title": "Cooling of Paramagnetic Salt by Adiabatic Demagnetization",
            "statement": "A crystal of gadolinium sulfate of mass $m = 0.150\\\\text{ kg}$ is magnetized isothermally at initial temperature $T_i = 1.20\\\\text{ K}$ in a magnetic field of $H_i = 2.50\\\\text{ T}$. The effective internal local dipole field of the crystal lattice is $h_{\\\\text{int}} = 0.0350\\\\text{ T}$. (a) Calculate the final temperature $T_f$ when the external field is reduced adiabatically to zero ($H_f = 0$). (b) Calculate the final temperature if the field is reduced to a residual value of $H_f = 0.200\\\\text{ T}$. (c) Determine the heat absorbed from a cryogenic sample when warmed back up to $1.20\\\\text{ K}$ if the total heat capacity is approximated as $C = \\\\alpha T^3$ with $\\\\alpha = 0.0450\\\\text{ J/K}^4$.",
            "steps": [
                {
                    "step": "Step 1: Calculate Final Temperature for Complete Demagnetization ($H_f = 0$)",
                    "detail": "During isentropic demagnetization of an ideal paramagnetic dipole system, total entropy depends on the effective field-to-temperature ratio $\\\\frac{\\\\sqrt{H^2 + h_{\\\\text{int}}^2}}{T} = \\\\text{constant}$.\n$$T_f = T_i \\\\sqrt{\\\\frac{H_f^2 + h_{\\\\text{int}}^2}{H_i^2 + h_{\\\\text{int}}^2}}$$\nFor $H_f = 0$:\n$$T_f = T_i \\\\frac{h_{\\\\text{int}}}{\\\\sqrt{H_i^2 + h_{\\\\text{int}}^2}}$$\nSince $H_i = 2.50\\\\text{ T} \\\\gg h_{\\\\text{int}} = 0.0350\\\\text{ T}$, $\\\\sqrt{2.50^2 + 0.0350^2} \\\\approx 2.5002\\\\text{ T}$:\n$$T_f = (1.20\\\\text{ K}) \\\\left(\\\\frac{0.0350}{2.5002}\\\\right) = (1.20)(0.01400) = 0.0168\\\\text{ K} = 16.8\\\\text{ mK}$$"
                },
                {
                    "step": "Step 2: Calculate Final Temperature for Partial Demagnetization ($H_f = 0.200\\\\text{ T}$)",
                    "detail": "With residual external field $H_f = 0.200\\\\text{ T}$:\n$$\\\\sqrt{H_f^2 + h_{\\\\text{int}}^2} = \\\\sqrt{(0.200)^2 + (0.0350)^2} = \\\\sqrt{0.0400 + 0.001225} = \\\\sqrt{0.041225} = 0.2030\\\\text{ T}$$\n$$T_f = (1.20\\\\text{ K}) \\\\left(\\\\frac{0.2030}{2.5002}\\\\right) = (1.20)(0.08119) = 0.0974\\\\text{ K} = 97.4\\\\text{ mK}$$"
                },
                {
                    "step": "Step 3: Calculate Cryogenic Heat Absorbed During Reheating",
                    "detail": "The heat capacity of the lattice and spin reservoir is $C = \\\\alpha T^3$ with $\\\\alpha = 0.0450\\\\text{ J/K}^4$.\nReheating from $T_f = 0.0168\\\\text{ K}$ to $T_i = 1.20\\\\text{ K}$:\n$$Q = \\\\int_{T_f}^{T_i} \\\\alpha T^3 dT = \\\\frac{\\\\alpha}{4} [T_i^4 - T_f^4]$$\n$$(1.20)^4 = 2.0736, \\quad (0.0168)^4 \\\\approx 7.96 \\\\times 10^{-8} \\\\approx 0$$\n$$Q = \\\\frac{0.0450}{4} (2.0736) = (0.01125)(2.0736) = 0.02333\\\\text{ J} = 23.33\\\\text{ mJ}$$"
                }
            ],
            "answer": "(a) Complete demagnetization yields $T_f = 16.8\\\\text{ mK}$. (b) Partial demagnetization to $0.20\\\\text{ T}$ yields $T_f = 97.4\\\\text{ mK}$. (c) Cryogenic cooling capacity absorbed upon warming to $1.20\\\\text{ K}$ is $Q = 23.3\\\\text{ mJ}$."
        },
        {
            "id": "u4-p3",
            "title": "Derivation of Gibbs-Helmholtz Equation & Chemical Reaction Spontaneity",
            "statement": "Starting from the definition of Gibbs free energy $G = H - TS$ and the fundamental differential $dG = -S dT + V dP$: (a) derive the Gibbs-Helmholtz equation in both the form $\\\\left(\\\\frac{\\\\partial (G/T)}{\\\\partial T}\\\\right)_P = -\\\\frac{H}{T^2}$ and $\\\\left(\\\\frac{\\\\partial (\\\\Delta G/T)}{\\\\partial (1/T)}\\\\right)_P = \\\\Delta H$. (b) A chemical reaction has an enthalpy change of $\\\\Delta H^\\\\circ = -84.2\\\\text{ kJ/mol}$ and an entropy change of $\\\\Delta S^\\\\circ = -165.0\\\\text{ J/(mol}\\\\cdot\\\\text{K)}$. Calculate $\\\\Delta G^\\\\circ$ at $298.15\\\\text{ K}$ and determine the inversion temperature above which the reaction ceases to be spontaneous.",
            "steps": [
                {
                    "step": "Step 1: Derivation of the Gibbs-Helmholtz Relation",
                    "detail": "From $dG = -S dT + V dP$, at constant pressure ($dP = 0$):\n$$\\\\left(\\\\frac{\\\\partial G}{\\\\partial T}\\\\right)_P = -S$$\nSubstituting $-S = \\\\frac{G - H}{T}$ from $G = H - TS$:\n$$\\\\left(\\\\frac{\\\\partial G}{\\\\partial T}\\\\right)_P = \\\\frac{G - H}{T} \\implies G - T \\\\left(\\\\frac{\\\\partial G}{\\\\partial T}\\\\right)_P = H$$\nNow evaluate the derivative of the quotient $G / T$ with respect to $T$:\n$$\\\\left(\\\\frac{\\\\partial (G/T)}{\\\\partial T}\\\\right)_P = \\\\frac{T \\\\left(\\\\frac{\\\\partial G}{\\\\partial T}\\\\right)_P - G}{T^2} = -\\\\frac{G - T \\\\left(\\\\frac{\\\\partial G}{\\\\partial T}\\\\right)_P}{T^2} = -\\\\frac{H}{T^2}$$\nUsing the chain rule with $u = 1/T$, so $du = -dT/T^2$ or $\\\\frac{d}{d(1/T)} = -T^2 \\\\frac{d}{dT}$:\n$$\\\\left(\\\\frac{\\\\partial (G/T)}{\\\\partial (1/T)}\\\\right)_P = -T^2 \\\\left(\\\\frac{\\\\partial (G/T)}{\\\\partial T}\\\\right)_P = -T^2 \\\\left(-\\\\frac{H}{T^2}\\\\right) = H$$\nFor a finite reaction transformation: $\\\\left(\\\\frac{\\\\partial (\\\\Delta G/T)}{\\\\partial (1/T)}\\\\right)_P = \\\\Delta H$."
                },
                {
                    "step": "Step 2: Calculate $\\\\Delta G^\\\\circ$ at $298.15\\\\text{ K}$",
                    "detail": "Using $\\\\Delta G^\\\\circ = \\\\Delta H^\\\\circ - T \\\\Delta S^\\\\circ$:\n$$\\\\Delta H^\\\\circ = -84200\\\\text{ J/mol}$$\n$$T \\\\Delta S^\\\\circ = (298.15\\\\text{ K})(-165.0\\\\text{ J/(mol}\\\\cdot\\\\text{K)}) = -49194.75\\\\text{ J/mol}$$\n$$\\\\Delta G^\\\\circ = -84200 - (-49194.75) = -84200 + 49194.75 = -35005.25\\\\text{ J/mol} = -35.01\\\\text{ kJ/mol}$$\nSince $\\\\Delta G^\\\\circ < 0$, the reaction is thermodynamically spontaneous at $298.15\\\\text{ K}$."
                },
                {
                    "step": "Step 3: Calculate Inversion Temperature for Spontaneity",
                    "detail": "Spontaneity boundary occurs where $\\\\Delta G^\\\\circ = 0$:\n$$\\\\Delta H^\\\\circ - T_{\\\\text{inv}} \\\\Delta S^\\\\circ = 0 \\implies T_{\\\\text{inv}} = \\\\frac{\\\\Delta H^\\\\circ}{\\\\Delta S^\\\\circ}$$\n$$T_{\\\\text{inv}} = \\\\frac{-84200\\\\text{ J/mol}}{-165.0\\\\text{ J/(mol}\\\\cdot\\\\text{K)}} = 510.30\\\\text{ K} = 237.15^\\\\circ\\\\text{C}$$\nFor $T < 510.3\\\\text{ K}$, $\\\\Delta G^\\\\circ < 0$ (spontaneous). For $T > 510.3\\\\text{ K}$, the unfavorable entropy loss ($-T\\\\Delta S > 0$) overcomes the favorable exothermic enthalpy ($\\\\Delta H < 0$), causing $\\\\Delta G^\\\\circ > 0$ and terminating spontaneity."
                }
            ],
            "answer": "(a) Proof yields $\\\\left(\\\\frac{\\\\partial (\\\\Delta G/T)}{\\\\partial (1/T)}\\\\right)_P = \\\\Delta H$. (b) At $298.15\\\\text{ K}$, $\\\\Delta G^\\\\circ = -35.01\\\\text{ kJ/mol}$ (spontaneous); inversion temperature is $T_{\\\\text{inv}} = 510.3\\\\text{ K}$ ($237.2^\\\\circ\\\\text{C}$)."
        }
    ]
}

with open("tp_u3.json", "w") as f:
    json.dump(u3, f, indent=2)
print("tp_u3.json written successfully.")

with open("tp_u4.json", "w") as f:
    json.dump(u4, f, indent=2)
print("tp_u4.json written successfully.")
