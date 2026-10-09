#!/usr/bin/env python3
"""
build_kinetics_units_7_8_9_10.py
Builds Units 7, 8, 9, and 10 (Sections 1-7, Solved Problems 1-7) for Molecular Motion and Reaction Kinetics.
"""

import json

def get_units_7_8_9_10():
    units = []

    # =========================================================================
    # UNIT 7: Unimolecular Reactions & Advanced Experimental Kinetic Methods
    # =========================================================================
    u7 = {
        "id": "unit-7",
        "unitNumber": 7,
        "title": "Unit 7: Unimolecular Reactions & Advanced Experimental Kinetic Methods",
        "leadSummary": "Microscopic kinetics of unimolecular gas reactions and modern fast-reaction metrology: the Lindemann-Hinshelwood collisional activation mechanism, RRK and RRKM microcanonical statistical rate theories, fall-off behavior, and fast kinetic diagnostic instrumentation (stopped-flow spectrophotometry, flash photolysis, laser-induced fluorescence, resonance fluorescence, shock tubes, and chemical relaxation jumps).",
        "simulations": ["sim_kin_lindemann_pressure_falloff"],
        "sections": [
            {
                "id": "sec-7-1",
                "secNumber": "7.1",
                "title": "The Unimolecular Reaction Paradox & The Lindemann-Hinshelwood Mechanism",
                "content": """A fundamental paradox in early chemical kinetics arose from unimolecular gas-phase decompositions ($A \\longrightarrow P$): if an isolated molecule reacts without colliding with a second species, where does it acquire its activation energy? If it acquires activation energy via collisions, why is the reaction empirically first-order rather than second-order?

### The Lindemann-Hinshelwood Mechanism (1922)
Frederick Lindemann resolved this paradox by separating activation from chemical decomposition into a two-step mechanism:

1. **Collisional Activation and Deactivation**:
   $$A + M \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} A^* + M$$
   A reactant molecule $A$ collides with a bath gas molecule $M$ (which may be another $A$ molecule or an inert buffer gas), acquiring vibrational energy in excess of the critical threshold $E_0$ to form an energized molecule $A^*$. Deactivation occurs by collision with rate constant $k_{-1}$.

2. **Unimolecular Decomposition**:
   $$A^* \\\\xrightarrow{k_2} P$$
   The energized molecule $A^*$ undergoes unimolecular rearrangement or bond cleavage to form product $P$ with rate constant $k_2$.

### Derivation of the Effective Rate Law
Applying the Bodenstein Steady-State Approximation to the energized intermediate $[A^*]$:
$$\\frac{d[A^*]}{dt} = k_1 [A][M] - k_{-1} [A^*][M] - k_2 [A^*] = 0$$
$$[A^*] = \\frac{k_1 [A][M]}{k_{-1} [M] + k_2}$$

The rate of product formation is:
$$r = \\frac{d[P]}{dt} = k_2 [A^*] = \\frac{k_1 k_2 [A][M]}{k_{-1} [M] + k_2} = k_{\\text{uni}} [A]$$

where the **effective unimolecular rate constant** $k_{\\text{uni}}$ is:
$$k_{\\text{uni}} = \\frac{k_1 k_2 [M]}{k_{-1} [M] + k_2}$$

### The Pressure Fall-Off Regimes
1. **High-Pressure Limit ($[M] \\to \\infty$, $k_{-1}[M] \\gg k_2$)**:
   Deactivation is much faster than decomposition. A Boltzmann equilibrium population of $A^*$ is maintained:
   $$k_{\\text{uni}} \\to k_\\infty = \\frac{k_1 k_2}{k_{-1}} = K_1 k_2$$
   The rate is strictly **first-order**: $r = k_\\infty [A]$.
2. **Low-Pressure Limit ($[M] \\to 0$, $k_2 \\gg k_{-1}[M]$)**:
   Every energized molecule $A^*$ decomposes before it can be deactivated:
   $$k_{\\text{uni}} \\to k_0 [M] = k_1 [M]$$
   The rate falls off to **second-order**: $r = k_1 [A][M]$."""
            },
            {
                "id": "sec-7-2",
                "secNumber": "7.2",
                "title": "Hinshelwood Modification: Multi-Mode Vibrational Energy Redistribution",
                "content": """While Lindemann's theory explained the qualitative shift from first-order to second-order kinetics, it dramatically underestimated the experimental high-pressure rate constant $k_\\infty$ for polyatomic molecules by several orders of magnitude.

### Hinshelwood's Insight (1927)
Lindemann treated activation as occurring with simple hard-sphere kinetic energy. Cyril Hinshelwood recognized that polyatomic molecules possess $s$ internal classical vibrational degrees of freedom among which thermal energy can be distributed.

According to classical statistical mechanics, the probability that a molecule with $s$ harmonic vibrational modes possesses total energy exceeding $E_0$ is given by the Euler gamma distribution:
$$P(E \\ge E_0) = \\frac{1}{(s - 1)!} \\left( \\frac{E_0}{k_B T} \\right)^{s - 1} \\exp\\left( -\\frac{E_0}{k_B T} \\right)$$

For $s = 1$, this reduces to the simple Boltzmann factor $e^{-E_0 / k_B T}$.
For polyatomic molecules with many vibrational modes ($s \\gg 1$), the prefactor $\\frac{1}{(s - 1)!} (E_0 / k_B T)^{s - 1}$ is colossal:
For $s = 10$ and $E_0 / k_B T = 30$:
$$\\frac{1}{9!} (30)^9 = \\frac{1.968 \\times 10^{13}}{362880} \\approx 5.4 \\times 10^7$$
This factor of $10^7\\text{--}10^8$ accounts precisely for the observed activation rates in complex hydrocarbons and ethers."""
            },
            {
                "id": "sec-7-3",
                "secNumber": "7.3",
                "title": "RRK & RRKM Microcanonical Transition State Rate Theories",
                "content": """While Hinshelwood allowed energy to be stored across $s$ oscillators, he assumed the decomposition rate $k_2$ was independent of the total energy $E$.

### Rice-Ramsperger-Kassel (RRK) Classical Theory (1927-1928)
Oscar Rice, Herman Ramsperger, and Louis Kassel introduced the concept that for reaction to occur, a critical amount of energy $E_0$ must localize into a **single critical reactive bond** (the reaction coordinate) out of the $s$ available vibrational modes.

By combinatorial statistics of distributing quanta across classical oscillators, the microcanonical rate constant $k_2(E)$ for an energized molecule with total energy $E \\ge E_0$ is:
$$k_2(E) = k_{\\text{intra}} \\left( \\frac{E - E_0}{E} \\right)^{s - 1}$$
where $k_{\\text{intra}} \\sim 10^{13}\\text{ s}^{-1}$ is the fundamental vibrational frequency.
As total energy $E$ increases above threshold $E_0$, $k_2(E)$ increases monotonically.

### RRKM Quantum Transition State Theory (Marcus, 1952)
Rudolph Marcus reformulated RRK theory quantum mechanically within Transition State Theory, earning the 1992 Nobel Prize in Chemistry:
$$k(E) = \\frac{W^\\ddagger(E - E_0)}{h \\, \\rho(E)}$$
where:
- $W^\\ddagger(E - E_0)$ is the total sum of quantum vibrational-rotational states of the transition state complex with energy up to $E - E_0$.
- $\\rho(E)$ is the density of quantum states of the reactant molecule at energy $E$.
- $h$ is Planck's constant.

RRKM theory provides the modern gold standard for microcanonical unimolecular rate calculations in combustion, atmospheric chemistry, and mass spectrometry."""
            },
            {
                "id": "sec-7-4",
                "secNumber": "7.4",
                "title": "Experimental Fast Reaction Methods I: Continuous Flow & Stopped-Flow",
                "content": """Conventional kinetic sampling (manual pipetting, titration) is limited to half-lives longer than several seconds. Reactions occurring on millisecond to microsecond timescales demand rapid hydrodynamic mixing.

### Continuous Flow Method (Hartridge and Roughton, 1923)
Two reactant solutions are driven under high pressure into an efficient jet mixing chamber (dead time $\\tau_{\\text{mix}} < 1\\text{ ms}$). The reaction mixture flows down an observation tube of cross-sectional area $A$ at a constant linear flow velocity $u$:
$$x = u \\cdot t \\iff t = \\frac{x}{u}$$
The distance $x$ downstream from the mixing chamber maps directly to reaction elapsed time $t$. Spectroscopic absorbance measured at various spatial positions $x$ yields concentration $[A](t)$ directly under steady-state flow conditions.
- **Limitation**: Requires massive volumes of reactants (liters) to maintain steady flow.

### Stopped-Flow Spectrophotometry (Chance, 1940)
The stopped-flow apparatus overcomes the reagent consumption limitation by operating in transient batch mode:
1. Two pneumatic or motor-driven syringes rapidly inject small volumes ($\\sim 0.1\\text{ mL}$) of reactants through an impingement mixer into an optical cuvette.
2. The emerging fluid hits a mechanical stopping syringe plunger, halting flow abruptly within $\\sim 1\\text{ ms}$.
3. High-speed spectrophotometric absorption or fluorescence detection records the kinetic decay in the stationary cuvette in real time on a digital oscilloscope.
- **Dead Time**: Typically $0.5\\text{--}2.0\\text{ ms}$. Widely utilized for enzyme-substrate binding, protein folding, and inorganic ligand substitution kinetics."""
            },
            {
                "id": "sec-7-5",
                "secNumber": "7.5",
                "title": "Experimental Fast Reaction Methods II: Flash Photolysis & Pump-Probe Spectroscopy",
                "content": """To study reactions on microsecond, nanosecond, picosecond, and femtosecond timescales, physical perturbations replace mechanical mixing.

### Flash Photolysis (Norrish and Porter, 1949; Nobel Prize 1967)
Ronald Norrish and George Porter developed flash photolysis to generate high concentrations of short-lived reactive free radicals, atoms, and triplet states using an intense flash of light:
1. **Pump Flash**: A high-intensity optical pulse (historically a xenon flash lamp, now a pulsed laser) photolytically dissociates precursor molecules within nanoseconds:
   $$Cl_2 + h\\nu_{\\text{pump}} \\longrightarrow 2 Cl^\\bullet$$
2. **Probe Flash**: A secondary, weaker continuous or delayed light source probes the transient intermediate via ultraviolet-visible absorption spectroscopy as a function of delay time $\\Delta t$.

### Ultrafast Femtosecond Pump-Probe Spectroscopy (Zewail, 1990s)
Ahmed Zewail extended pump-probe spectroscopy to the femtosecond regime ($10^{-15}\\text{ s}$), directly observing the transition state of chemical reactions:
$$\\Delta t = \\frac{\\Delta x}{c}$$
where $\\Delta x$ is optical path delay ($1\\;\\mu\\text{m} \\approx 3.3\\text{ fs}$) and $c$ is the speed of light.
This enabled real-time observation of wavepackets traversing the transition state saddle point in photodissociation ($NaI^* \\to Na + I$)."""
            },
            {
                "id": "sec-7-6",
                "secNumber": "7.6",
                "title": "Laser-Induced Fluorescence (LIF) & Resonance Fluorescence",
                "content": """Spectroscopic detection of trace radical intermediates at ultra-low concentrations requires techniques with exceptional sensitivity and quantum specificity.

### Laser-Induced Fluorescence (LIF)
In LIF, a tunable dye or solid-state laser is tuned to an exact electronic absorption transition of a radical species (e.g., $OH(^2\\Sigma^+ \\leftarrow ^2\\Pi)$, $CH(^2\\Delta \\leftarrow ^2\\Pi)$, $CN(^2\\Sigma^+ \\leftarrow ^2\\Sigma^+)$):
$$R + h\\nu_{\\text{laser}} \\longrightarrow R^* \\longrightarrow R + h\\nu_{\\text{fluorescence}}$$
Fluorescence is collected at $90^\\circ$ to the excitation beam using a photomultiplier tube through bandpass optical filters.
- **Sensitivity**: Detects radical concentrations down to $10^6\\text{ molecules/cm}^3$ ($< 10^{-13}\\text{ M}$).
- **State-to-State Resolution**: Resolves individual vibrational and rotational quantum states ($v, J$) of reacting fragments.

### Resonance Fluorescence (RF)
For atomic radicals ($H, O, N, Cl, Br$), transitions lie in the vacuum ultraviolet (VUV, $\\lambda < 200\\text{ nm}$).
A microwave-powered discharge lamp containing trace gas ($H_2$ in $He$ emits Lyman-$\\alpha$ at $121.6\\text{ nm}$; $O_2$ in $He$ emits $130.2\\text{ nm}$) excites ground-state atoms, and resonance fluorescence is detected under single-photon counting conditions. RF is the gold standard for measuring elementary gas-phase rate constants with hydroxyl radicals in tropospheric chemistry."""
            },
            {
                "id": "sec-7-7",
                "secNumber": "7.7",
                "title": "Shock Tubes & Chemical Relaxation Methods (T-Jump, P-Jump)",
                "content": """Reactions at extreme temperatures or ultra-fast reversible equilibria require shock heating or chemical relaxation.

### Shock Tube Kinetics
A shock tube consists of a long steel pipe divided into a high-pressure driver section ($He$ or $H_2$ at $10\\text{--}100\\text{ bar}$) and a low-pressure driven section containing reactants in argon ($1\\text{--}10\\text{ mbar}$), separated by a metal diaphragm.
1. When the diaphragm ruptures, a planar shock wave propagates into the driven gas at supersonic speeds (Mach $2\\text{--}6$).
2. Shock compression heats the gas instantaneously (within $< 0.1\\;\\mu\\text{s}$) to $1000\\text{--}5000\\text{ K}$ at high pressure, without thermal wall effects.
3. Radical kinetics, combustion ignition delay times, and high-temperature thermal decompositions are monitored via laser absorption or emission behind the reflected shock wave.

### Chemical Relaxation Methods (Manfred Eigen, 1954; Nobel Prize 1967)
For rapid reversible equilibria ($A + B \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} C$) where equilibrium is established in microseconds, hydrodynamic mixing is too slow.
Eigen perturbed the existing equilibrium by applying an abrupt physical jump in temperature or pressure:
$$\\Delta \\ln K = \\frac{\\Delta H^\\circ}{R T^2} \\Delta T \\quad (\\text{Temperature Jump / T-Jump})$$
$$\\Delta \\ln K = -\\frac{\\Delta V^\\circ}{R T} \\Delta P \\quad (\\text{Pressure Jump / P-Jump})$$

A capacitor discharge discharges kilovolt electricity through an electrolyte cell within $1\\;\\mu\\text{s}$, raising temperature by $3\\text{--}10\\text{ K}$.
The relaxation back to the new equilibrium follows a first-order exponential rate:
$$\\Delta [A](t) = \\Delta [A]_0 \\exp(-t / \\tau_{\\text{relax}})$$
where the **relaxation time** $\\tau_{\\text{relax}}$ is:
$$\\frac{1}{\\tau_{\\text{relax}}} = k_1 ([A]_{\\text{eq}} + [B]_{\\text{eq}}) + k_{-1}$$
Plotting $1/\\tau_{\\text{relax}}$ versus $([A]_{\\text{eq}} + [B]_{\\text{eq}})$ gives slope $k_1$ and intercept $k_{-1}$ directly."""
            }
        ],
        "problems": [
            {
                "id": "p7-1",
                "title": "Lindemann Fall-Off Parameters and Limiting Rate Constants for Cyclopropane Isomerization",
                "difficulty": "Easy",
                "statement": """The thermal isomerization of cyclopropane to propene follows the Lindemann-Hinshelwood unimolecular mechanism. At $T = 770.0\\text{ K}$, measured effective first-order rate constants $k_{\\text{uni}}$ vary with pressure as follows:
- At $P_1 = 1.00\\text{ Torr}$ ($133.3\\text{ Pa}$), $k_{\\text{uni}, 1} = 2.98 \\times 10^{-4}\\text{ s}^{-1}$
- At $P_2 = 100.0\\text{ Torr}$ ($13332\\text{ Pa}$), $k_{\\text{uni}, 2} = 1.50 \\times 10^{-3}\\text{ s}^{-1}$

Using the Lineweaver-style linear relation $\\frac{1}{k_{\\text{uni}}} = \\frac{1}{k_\\infty} + \\frac{k_{-1}}{k_1 k_2} \\frac{1}{P}$, calculate: (a) the high-pressure limiting rate constant $k_\\infty$, and (b) the transition pressure $P_{1/2}$ at which $k_{\\text{uni}} = \\frac{1}{2} k_\\infty$.""",
                "solution": """**Step 1: Set up simultaneous linear equations**
Let $y = 1 / k_{\\text{uni}}$ and $x = 1 / P$:
$$y_1 = \\frac{1}{2.98 \\times 10^{-4}\\text{ s}^{-1}} = 3355.70\\text{ s}$$
$$x_1 = \\frac{1}{1.00\\text{ Torr}} = 1.000\\text{ Torr}^{-1}$$

$$y_2 = \\frac{1}{1.50 \\times 10^{-3}\\text{ s}^{-1}} = 666.67\\text{ s}$$
$$x_2 = \\frac{1}{100.0\\text{ Torr}} = 0.0100\\text{ Torr}^{-1}$$

**Step 2: Solve for slope and intercept**
$$\\text{Slope } m = \\frac{y_1 - y_2}{x_1 - x_2} = \\frac{3355.70 - 666.67}{1.000 - 0.0100} = \\frac{2689.03}{0.990} = 2716.19\\text{ s}\\cdot\\text{Torr}$$

Intercept:
$$b = \\frac{1}{k_\\infty} = y_2 - m x_2 = 666.67 - (2716.19 \\times 0.0100) = 666.67 - 27.16 = 639.51\\text{ s}$$

$$k_\\infty = \\frac{1}{639.51\\text{ s}} = 1.5637 \\times 10^{-3}\\text{ s}^{-1} \\approx 1.56 \\times 10^{-3}\\text{ s}^{-1}$$

**Step 3: Calculate transition pressure $P_{1/2}$**
At $k_{\\text{uni}} = \\frac{1}{2} k_\\infty$, $\\frac{1}{k_{\\text{uni}}} = \\frac{2}{k_\\infty}$:
$$\\frac{2}{k_\\infty} = \\frac{1}{k_\\infty} + m \\left( \\frac{1}{P_{1/2}} \\right) \\implies \\frac{1}{k_\\infty} = \\frac{m}{P_{1/2}}$$
$$P_{1/2} = m \\cdot k_\\infty = \\frac{m}{b} = \\frac{2716.19\\text{ s}\\cdot\\text{Torr}}{639.51\\text{ s}} = 4.247\\text{ Torr} = 566.2\\text{ Pa}$$"""
            },
            {
                "id": "p7-2",
                "title": "Hinshelwood Classical Oscillators Calculation for Azomethane Pyrolysis",
                "difficulty": "Medium",
                "statement": "The thermal decomposition of azomethane ($CH_3N=NCH_3 \\longrightarrow C_2H_6 + N_2$) has an activation energy of $E_0 = 215.0\\text{ kJ/mol}$ at $T = 600.0\\text{ K}$. (a) Calculate the simple Boltzmann fraction $\\exp(-E_0 / R T)$. (b) If azomethane has $s = 12$ effective classical vibrational modes participating in energy pooling, calculate the Hinshelwood factor $\\frac{1}{(s - 1)!} (E_0 / R T)^{s - 1} \\exp(-E_0 / R T)$ and the enhancement factor over the simple Boltzmann expression.",
                "solution": """**Step 1: Simple Boltzmann factor**
$$R T = (8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})) \\times (600.0\\text{ K}) = 4988.68\\text{ J/mol} = 4.98868\\text{ kJ/mol}$$
$$x = \\frac{E_0}{R T} = \\frac{215.0}{4.98868} = 43.0976$$
$$\\exp(-x) = \\exp(-43.0976) = 1.9188 \\times 10^{-19}$$

**Step 2: Hinshelwood prefactor for $s = 12$**
Number of modes: $s = 12 \\implies s - 1 = 11$.
Factorial:
$$(s - 1)! = 11! = 39916800 = 3.99168 \\times 10^7$$

Power:
$$x^{s - 1} = (43.0976)^{11} = 1.0505 \\times 10^{18}$$

Hinshelwood multiplier:
$$\\mathcal{M} = \\frac{x^{s - 1}}{(s - 1)!} = \\frac{1.0505 \\times 10^{18}}{3.99168 \\times 10^7} = 2.6318 \\times 10^{10}$$

**Step 3: Total Hinshelwood probability and enhancement factor**
$$P_{\\text{Hinshelwood}} = \\mathcal{M} \\times \\exp(-x) = (2.6318 \\times 10^{10}) \\times (1.9188 \\times 10^{-19}) = 5.050 \\times 10^{-9}$$

Enhancement factor:
$$\\frac{P_{\\text{Hinshelwood}}}{P_{\\text{Boltzmann}}} = \\mathcal{M} = 2.63 \\times 10^{10}$$
The internal vibrational energy redistribution increases the fraction of reactive energized molecules by a factor of **26 billion**, resolving the Lindemann paradox for azomethane."""
            },
            {
                "id": "p7-3",
                "title": "Temperature-Jump Chemical Relaxation Kinetics of Protein Folding",
                "difficulty": "Hard",
                "statement": "The reversible two-state conformational transition of a small globular protein ($Native \\underset{k_u}{\\overset{k_f}{\\rightleftharpoons}} Unfolded$) is studied via laser temperature-jump spectroscopy. At $T = 37.0^\\circ\\text{C}$, the equilibrium constant for unfolding is $K_{\\text{eq}} = [U]_{\\text{eq}} / [N]_{\\text{eq}} = 0.250$. Following a rapid $\\Delta T = 5.0\\text{ K}$ jump, the optical circular dichroism signal relaxes to the new equilibrium with a single exponential relaxation time of $\\tau = 45.0\\;\\mu\\text{s}$. Calculate: (a) the folding rate constant $k_f$, and (b) the unfolding rate constant $k_u$ in $\\text{s}^{-1}$.",
                "solution": """**Step 1: Relate relaxation time to forward and reverse rate constants**
For a first-order reversible isomerization $N \\underset{k_u}{\\overset{k_f}{\\rightleftharpoons}} U$:
$$\\frac{1}{\\tau} = k_f + k_u$$
where:
$$\\tau = 45.0\\;\\mu\\text{s} = 45.0 \\times 10^{-6}\\text{ s}$$
$$\\frac{1}{\\tau} = \\frac{1}{45.0 \\times 10^{-6}\\text{ s}} = 2.2222 \\times 10^4\\text{ s}^{-1}$$

Thus:
$$k_f + k_u = 22222\\text{ s}^{-1}$$

**Step 2: Relate rate constants via thermodynamic equilibrium constant**
$$K_{\\text{eq}} = \\frac{[U]_{\\text{eq}}}{[N]_{\\text{eq}}} = \\frac{k_u}{k_f} = 0.250 \\implies k_u = 0.250 \\, k_f$$

**Step 3: Solve for individual rate constants**
$$k_f + 0.250 \\, k_f = 1.250 \\, k_f = 22222\\text{ s}^{-1}$$
$$k_f = \\frac{22222}{1.250} = 17778\\text{ s}^{-1} = 1.78 \\times 10^4\\text{ s}^{-1}$$

Unfolding rate constant:
$$k_u = 0.250 \\times 17778 = 4444\\text{ s}^{-1} = 4.44 \\times 10^3\\text{ s}^{-1}$$"""
            },
            {
                "id": "p7-4",
                "title": "Continuous Flow Dead-Time and Spatial-to-Temporal Calibration",
                "difficulty": "Easy",
                "statement": "In a continuous-flow tube apparatus, two reactant solutions are pumped into an impingement mixing nozzle at a combined volumetric flow rate of $Q = 120.0\\text{ mL/s}$. The mixing chamber volume is $V_{\\text{mix}} = 0.180\\text{ mL}$, and the observation capillary tube has an internal diameter of $d = 2.00\\text{ mm}$. Calculate: (a) the hydrodynamic mixing dead time $\\tau_{\\text{mix}}$, (b) the linear flow velocity $u$ inside the observation capillary in $\\text{m/s}$, and (c) the elapsed reaction time $t$ corresponding to an optical detector positioned $x = 15.0\\text{ cm}$ downstream.",
                "solution": """**Step 1: Calculate mixing dead time $\\tau_{\\text{mix}}$**
$$\\tau_{\\text{mix}} = \\frac{V_{\\text{mix}}}{Q} = \\frac{0.180\\text{ mL}}{120.0\\text{ mL/s}} = 1.50 \\times 10^{-3}\\text{ s} = 1.50\\text{ ms}$$

**Step 2: Capillary cross-sectional area and linear velocity $u$**
$$r = \\frac{2.00 \\times 10^{-3}\\text{ m}}{2} = 1.00 \\times 10^{-3}\\text{ m}$$
$$A = \\pi r^2 = \\pi (1.00 \\times 10^{-3})^2 = 3.1416 \\times 10^{-6}\\text{ m}^2$$

Volumetric flow rate in SI units:
$$Q = 120.0 \\times 10^{-6}\\text{ m}^3/\\text{s}$$
$$u = \\frac{Q}{A} = \\frac{120.0 \\times 10^{-6}\\text{ m}^3/\\text{s}}{3.1416 \\times 10^{-6}\\text{ m}^2} = 38.197\\text{ m/s}$$

**Step 3: Elapsed reaction time at $x = 15.0\\text{ cm}$**
$$x = 15.0 \\times 10^{-2}\\text{ m} = 0.150\\text{ m}$$
Flow transit time:
$$t_{\\text{flow}} = \\frac{x}{u} = \\frac{0.150\\text{ m}}{38.197\\text{ m/s}} = 3.927 \\times 10^{-3}\\text{ s} = 3.93\\text{ ms}$$

Total elapsed reaction time:
$$t_{\\text{total}} = \\tau_{\\text{mix}} + t_{\\text{flow}} = 1.50\\text{ ms} + 3.93\\text{ ms} = 5.43\\text{ ms}$$"""
            },
            {
                "id": "p7-5",
                "title": "Shock Tube Aerodynamic Mach Number and Post-Shock Gas Temperature",
                "difficulty": "Hard",
                "statement": """A shock tube filled with argon ($M = 39.948\\text{ g/mol}$, $\\gamma = 5/3 = 1.667$) at initial conditions $T_1 = 298.15\\text{ K}$ and $P_1 = 10.0\\text{ Torr}$ is struck by an incident planar shock wave traveling at velocity $u_s = 1450.0\\text{ m/s}$. Using standard 1D ideal gas shock jump relations: (a) calculate the initial speed of sound $a_1$ and the shock Mach number $M_s$, and (b) calculate the post-shock gas temperature $T_2$ behind the incident shock wave using:
$$\\frac{T_2}{T_1} = \\frac{(2 \\gamma M_s^2 - (\\gamma - 1))((\\gamma - 1) M_s^2 + 2)}{(\\gamma + 1)^2 M_s^2}$$$""",
                "solution": """**Step 1: Initial speed of sound $a_1$ and shock Mach number $M_s$**
$$a_1 = \\sqrt{\\frac{\\gamma R T_1}{M}} = \\sqrt{\\frac{1.6667 \\times 8.314462 \\times 298.15}{0.039948}} = \\sqrt{\\frac{4132.06}{0.039948}} = \\sqrt{1.03436 \\times 10^5} = 321.61\\text{ m/s}$$
$$M_s = \\frac{u_s}{a_1} = \\frac{1450.0\\text{ m/s}}{321.61\\text{ m/s}} = 4.5085$$
$$M_s^2 = (4.5085)^2 = 20.327$$

**Step 2: Evaluate terms in the temperature jump relation**
$$\\gamma = 1.6667 \\implies \\gamma - 1 = 0.6667, \\quad \\gamma + 1 = 2.6667$$
$$(\\gamma + 1)^2 = (2.6667)^2 = 7.1111$$

Term 1:
$$2 \\gamma M_s^2 - (\\gamma - 1) = 2(1.6667)(20.327) - 0.6667 = 67.757 - 0.667 = 67.090$$

Term 2:
$$(\\gamma - 1) M_s^2 + 2 = (0.6667)(20.327) + 2 = 13.551 + 2 = 15.551$$

Numerator:
$$67.090 \\times 15.551 = 1043.32$$

Denominator:
$$(\\gamma + 1)^2 M_s^2 = 7.1111 \\times 20.327 = 144.547$$

Temperature ratio:
$$\\frac{T_2}{T_1} = \\frac{1043.32}{144.547} = 7.2179$$

**Step 3: Calculate post-shock temperature $T_2$**
$$T_2 = 298.15\\text{ K} \\times 7.2179 = 2152.0\\text{ K}$$
The supersonic shock wave compresses and heats the ambient argon gas to over **$2150\\text{ K}$** within sub-microsecond timescales."""
            },
            {
                "id": "p7-6",
                "title": "Laser Flash Photolysis Triplet Quenching Bimolecular Rate Constant",
                "difficulty": "Medium",
                "statement": "In a laser flash photolysis experiment ($\lambda_{\text{laser}} = 355\text{ nm}$), triplet anthracene ($^3\text{An}^*$) is generated in deaerated cyclohexane. In the absence of quencher, triplet decay is first-order with lifetime $\tau_0 = 120.0\;\mu\text{s}$ ($k_0 = 1 / \tau_0$). Upon adding molecular oxygen ($O_2$) at concentration $[O_2] = 2.50 \times 10^{-4}\text{ M}$, the observed triplet lifetime decreases to $\tau = 1.85\;\mu\text{s}$. Calculate: (a) the pseudo-first-order quenching rate constant $k_{\text{obs}}$, and (b) the bimolecular quenching rate constant $k_q$ in $\text{M}^{-1}\text{s}^{-1}$.",
                "solution": """**Step 1: Calculate unquenched and quenched decay constants**
Unquenched:
$$k_0 = \\frac{1}{\\tau_0} = \\frac{1}{120.0 \\times 10^{-6}\\text{ s}} = 8.333 \\times 10^3\\text{ s}^{-1}$$

Quenched:
$$k_{\\text{obs}} = \\frac{1}{\\tau} = \\frac{1}{1.85 \\times 10^{-6}\\text{ s}} = 5.4054 \\times 10^5\\text{ s}^{-1}$$

**Step 2: Calculate bimolecular quenching rate constant $k_q$**
According to the Stern-Volmer kinetic relation:
$$k_{\\text{obs}} = k_0 + k_q [O_2]$$
$$k_q [O_2] = k_{\\text{obs}} - k_0 = 5.4054 \\times 10^5 - 8.333 \\times 10^3 = 5.3221 \\times 10^5\\text{ s}^{-1}$$

Solving for $k_q$:
$$k_q = \\frac{5.3221 \\times 10^5\\text{ s}^{-1}}{2.50 \\times 10^{-4}\\text{ M}} = 2.1288 \\times 10^9\\text{ M}^{-1}\\text{s}^{-1} = 2.13 \\times 10^9\\text{ L}/(\\text{mol}\\cdot\\text{s})$$
This value approaches the diffusion-controlled limit in cyclohexane, characteristic of spin-allowed triplet-triplet energy transfer to yield singlet oxygen ($^1O_2$)."""
            },
            {
                "id": "p7-7",
                "title": "Laser-Induced Fluorescence Absolute Hydroxyl Radical Concentration",
                "difficulty": "Hard",
                "statement": "Tropospheric hydroxyl radicals ($OH$) are measured by laser-induced fluorescence at $\\lambda_{\\text{pump}} = 308.0\\text{ nm}$ ($A^2\\Sigma^+ \\leftarrow X^2\\Pi$). The fluorescence emission quantum yield in air at $1.00\\text{ atm}$ is $\\Phi_f = 1.20 \\times 10^{-3}$ due to collisional electronic quenching by $N_2$ and $O_2$. An excitation laser pulse delivers energy $E_{\\text{pulse}} = 15.0\\text{ mJ}$ across a beam cross-section $A_{\\text{beam}} = 0.250\\text{ cm}^2$. Given the absorption cross-section $\\sigma_{OH} = 1.40 \\times 10^{-16}\\text{ cm}^2$ and collection detection efficiency $\\eta_{\\text{det}} = 2.50 \\times 10^{-4}$, an observed single-pulse signal of $S_f = 850\\text{ photon counts}$ was recorded. Calculate the absolute hydroxyl radical concentration $[OH]$ in $\\text{molecules/cm}^3$.",
                "solution": """**Step 1: Calculate laser photon fluence**
Photon energy at $\\lambda = 308\\text{ nm} = 308 \\times 10^{-9}\\text{ m}$:
$$E_{\\text{photon}} = \\frac{h c}{\\lambda} = \\frac{(6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}) \\times (2.99792 \\times 10^8\\text{ m/s})}{308 \\times 10^{-9}\\text{ m}} = 6.4495 \\times 10^{-19}\\text{ J}$$

Number of photons per pulse:
$$N_{\\text{photons}} = \\frac{15.0 \\times 10^{-3}\\text{ J}}{6.4495 \\times 10^{-19}\\text{ J}} = 2.3258 \\times 10^{16}\\text{ photons}$$

Photon fluence per unit area:
$$F = \\frac{N_{\\text{photons}}}{A_{\\text{beam}}} = \\frac{2.3258 \\times 10^{16}}{0.250\\text{ cm}^2} = 9.3032 \\times 10^{16}\\text{ photons/cm}^2$$

**Step 2: Signal equation for LIF**
The recorded fluorescence count is:
$$S_f = [OH] \\cdot \\sigma_{OH} \\cdot F \\cdot \\Phi_f \\cdot \\eta_{\\text{det}} \\cdot V_{\\text{obs}}$$
For normalized volume $V_{\\text{obs}} = 1.00\\text{ cm}^3$:
$$\\text{Combined Factor } \\mathcal{C} = \\sigma_{OH} \\cdot F \\cdot \\Phi_f \\cdot \\eta_{\\text{det}}$$
$$\\mathcal{C} = (1.40 \\times 10^{-16}) \\times (9.3032 \\times 10^{16}) \\times (1.20 \\times 10^{-3}) \\times (2.50 \\times 10^{-4})$$
$$(1.40 \\times 10^{-16}) \\times (9.3032 \\times 10^{16}) = 13.0245$$
$$(1.20 \\times 10^{-3}) \\times (2.50 \\times 10^{-4}) = 3.00 \\times 10^{-7}$$
$$\\mathcal{C} = 13.0245 \\times (3.00 \\times 10^{-7}) = 3.9073 \\times 10^{-6}$$

**Step 3: Solve for $[OH]$**
$$[OH] = \\frac{S_f}{\\mathcal{C}} = \\frac{850}{3.9073 \\times 10^{-6}} = 2.175 \\times 10^8\\text{ molecules/cm}^3$$
In molarity:
$$[OH] = \\frac{2.175 \\times 10^8}{6.02214 \\times 10^{23}} \\times 1000 = 3.61 \\times 10^{-13}\\text{ M}$$
This demonstrates how LIF quantifies sub-picomolar atmospheric radical intermediates."""
            }
        ]
    }
    units.append(u7)

    # =========================================================================
    # UNIT 8: Chain Reactions, Branched Kinetics & Explosions
    # =========================================================================
    u8 = {
        "id": "unit-8",
        "unitNumber": 8,
        "title": "Unit 8: Chain Reactions, Branched Kinetics & Thermal/Branching Explosions",
        "leadSummary": "Kinetics of non-elementary chain reaction mechanisms: initiation, propagation, chain transfer, inhibition, and termination steps, steady-state radical dynamics in halogenation and free-radical polymerizations, Semenov branched-chain branching theory, the hydrogen-oxygen explosion peninsula, and thermal runaway explosion criteria.",
        "simulations": ["sim_kin_branched_chain_explosion_peninsula"],
        "sections": [
            {
                "id": "sec-8-1",
                "secNumber": "8.1",
                "title": "Fundamental Morphology of Chain Reactions: Radicals & Elementary Steps",
                "content": """Chain reactions are complex chemical networks in which a reactive intermediate (chain carrier, typically a free radical or atom) is consumed in a reaction step that regenerates one or more new chain carriers, enabling a single initiation event to trigger hundreds or thousands of product-forming cycles.

### The Four Essential Stages
1. **Initiation**: Generation of active chain carriers from stable closed-shell molecules, driven by thermal activation, photolysis, or chemical initiators:
   $$Cl_2 + h\\nu \\longrightarrow 2 Cl^\\bullet$$
2. **Propagation**: Elementary reactions between chain carriers and stable molecules that yield final products while regenerating active chain carriers:
   $$Cl^\\bullet + H_2 \\longrightarrow HCl + H^\\bullet$$
   $$H^\\bullet + Cl_2 \\longrightarrow HCl + Cl^\\bullet$$
3. **Inhibition / Retardation**: Reversible or irreversible scavenging of chain carriers by products or added inhibitors:
   $$H^\\bullet + HBr \\longrightarrow H_2 + Br^\\bullet$$
4. **Termination**: Destruction of active chain carriers, halting the propagation cycle:
   - *Homogeneous (Gas-Phase)*: Binary or termolecular radical recombination:
     $$Br^\\bullet + Br^\\bullet + M \\longrightarrow Br_2 + M$$
   - *Heterogeneous (Wall)*: Diffusion to the vessel wall followed by adsorption and recombination:
     $$H^\\bullet + \\text{wall} \\longrightarrow \\frac{1}{2} H_2$$

### Chain Length ($\\Lambda_{\\text{chain}}$)
The kinetic chain length $\\Lambda_{\\text{chain}}$ is defined as the average number of propagation cycles executed per initiation event:
$$\\Lambda_{\\text{chain}} = \\frac{r_{\\text{propagation}}}{r_{\\text{initiation}}}$$
For highly exothermic chain systems like $H_2 + Cl_2$, $\\Lambda_{\\text{chain}} \\sim 10^5\\text{--}10^6$, meaning a tiny flash of light can cause explosive transformation."""
            },
            {
                "id": "sec-8-2",
                "secNumber": "8.2",
                "title": "Stationary Chain Kinetics: The Hydrogen-Bromine Comprehensive Rate Law",
                "content": """Max Bodenstein (1906) experimentally discovered that the gas-phase reaction $H_2 + Br_2 \\longrightarrow 2 HBr$ follows an extraordinarily intricate empirical rate law:
$$r = \\frac{k [H_2] [Br_2]^{1/2}}{1 + m \\frac{[HBr]}{[Br_2]}}$$

### The Christiansen-Kramers-Polanyi Mechanism (1919)
1. **Initiation**:
   $$Br_2 + M \\\\xrightarrow{k_1} 2 Br^\\bullet + M$$
2. **Propagation 1**:
   $$Br^\\bullet + H_2 \\\\xrightarrow{k_2} HBr + H^\\bullet$$
3. **Propagation 2**:
   $$H^\\bullet + Br_2 \\\\xrightarrow{k_3} HBr + Br^\\bullet$$
4. **Inhibition (Product Retardation)**:
   $$H^\\bullet + HBr \\\\xrightarrow{k_4} H_2 + Br^\\bullet$$
5. **Termination**:
   $$2 Br^\\bullet + M \\\\xrightarrow{k_5} Br_2 + M$$

### Derivation via Bodenstein SSA
Apply SSA to the two chain carriers, $[Br^\\bullet]$ and $[H^\\bullet]$:
$$\\frac{d[H^\\bullet]}{dt} = k_2 [Br^\\bullet][H_2] - k_3 [H^\\bullet][Br_2] - k_4 [H^\\bullet][HBr] = 0$$
$$\\frac{d[Br^\\bullet]}{dt} = 2 k_1 [Br_2][M] - k_2 [Br^\\bullet][H_2] + k_3 [H^\\bullet][Br_2] + k_4 [H^\\bullet][HBr] - 2 k_5 [Br^\\bullet]^2 [M] = 0$$

Adding both steady-state equations:
$$2 k_1 [Br_2][M] - 2 k_5 [Br^\\bullet]^2 [M] = 0 \\implies [Br^\\bullet] = \\left( \\frac{k_1}{k_5} \\right)^{1/2} [Br_2]^{1/2}$$

From the first equation:
$$[H^\\bullet] = \\frac{k_2 [Br^\\bullet][H_2]}{k_3 [Br_2] + k_4 [HBr]} = \\frac{k_2 (k_1/k_5)^{1/2} [H_2][Br_2]^{1/2}}{k_3 [Br_2] + k_4 [HBr]}$$

The rate of product formation is:
$$\\frac{d[HBr]}{dt} = k_2 [Br^\\bullet][H_2] + k_3 [H^\\bullet][Br_2] - k_4 [H^\\bullet][HBr] = 2 k_3 [H^\\bullet][Br_2]$$
Substituting $[H^\\bullet]$:
$$\\frac{d[HBr]}{dt} = \\frac{2 k_2 k_3 (k_1/k_5)^{1/2} [H_2][Br_2]^{3/2}}{k_3 [Br_2] + k_4 [HBr]} = \\frac{2 k_2 (k_1/k_5)^{1/2} [H_2][Br_2]^{1/2}}{1 + \\left( \\frac{k_4}{k_3} \\right) \\frac{[HBr]}{[Br_2]}}$$
This derivation mathematically reproduces Bodenstein's empirical law, proving that $k = 2 k_2 (k_1/k_5)^{1/2}$ and $m = k_4 / k_3$."""
            },
            {
                "id": "sec-8-3",
                "secNumber": "8.3",
                "title": "Free-Radical Polymerization Kinetics & Steady-State Radical Populations",
                "content": """Chain-growth free-radical polymerization represents an industrial manifestation of stationary chain kinetics.

### Kinetic Steps
1. **Initiation**: Thermal decomposition of initiator $I$ (e.g., AIBN, benzoyl peroxide) followed by addition to monomer $M$:
   $$I \\\\xrightarrow{k_d} 2 R_0^\\bullet \\quad (r_d = k_d [I])$$
   $$R_0^\\bullet + M \\\\xrightarrow{k_i} M_1^\\bullet \\implies r_i = 2 f k_d [I]$$
   where $f$ is initiator efficiency ($0.5 < f < 0.9$).

2. **Propagation**: Sequential addition of monomer units:
   $$M_n^\\bullet + M \\\\xrightarrow{k_p} M_{n+1}^\\bullet \\implies r_p = k_p [M][M^\\bullet]$$
   assuming rate constant $k_p$ is independent of radical chain length $n$.

3. **Termination**: Bimolecular combination or disproportionation:
   $$M_n^\\bullet + M_m^\\bullet \\\\xrightarrow{k_t} \\text{Dead Polymer} \\implies r_t = 2 k_t [M^\\bullet]^2$$

### Steady-State Radical Concentration
Applying the Bodenstein SSA to total active radicals $[M^\\bullet]$:
$$r_i = r_t \\implies 2 f k_d [I] = 2 k_t [M^\\bullet]^2 \\implies [M^\\bullet] = \\sqrt{\\frac{f k_d [I]}{k_t}}$$

### Overall Polymerization Rate ($r_p$)
$$r_p = -\\frac{d[M]}{dt} = k_p [M][M^\\bullet] = k_p \\left( \\frac{f k_d}{k_t} \\right)^{1/2} [M] [I]^{1/2}$$
The rate is strictly **first-order in monomer** and **half-order in initiator**.

### Number-Average Degree of Polymerization ($\\bar{X}_n$)
$$\\bar{X}_n = \\frac{r_p}{r_i / 2} = \\frac{k_p [M] [M^\\bullet]}{k_t [M^\\bullet]^2} = \\frac{k_p [M]}{k_t [M^\\bullet]} = \\frac{k_p [M]}{\\sqrt{f k_d k_t [I]}}$$
Increasing initiator concentration increases polymerization rate but decreases average polymer molecular weight."""
            },
            {
                "id": "sec-8-4",
                "secNumber": "8.4",
                "title": "Non-Stationary & Branched Chain Reactions: Semenov Branching Dynamics",
                "content": """In a **branched chain reaction**, a propagation step generates more chain carriers than it consumes. Nikolai Semenov (1934; Nobel Prize 1956) formulated the mathematical theory of branching explosion kinetics.

### Semenov Differential Equation
Let $n(t)$ be the concentration of active chain carriers.
1. Rate of initiation: $w_0$
2. Rate of chain branching: $f \\, n$ (where $f$ is the branching probability coefficient per second)
3. Rate of chain termination: $g \\, n$ (where $g$ is the termination probability coefficient per second)

The differential equation for radical population growth is:
$$\\frac{dn}{dt} = w_0 + (f - g) n = w_0 + \\phi n$$
where $\\phi = f - g$ is the **net branching factor**.

### Solution and Stability Criteria
Integrating with initial condition $n(0) = 0$:
$$n(t) = \\frac{w_0}{\\phi} \\left( e^{\\phi t} - 1 \\right)$$

Three distinct regimes emerge:
1. **Stationary Sub-Critical Regime ($\\phi < 0$, $g > f$)**:
   Termination exceeds branching. As $t \\to \\infty$, $e^{\\phi t} \\to 0$:
   $$n_{\\text{ss}} = \\frac{w_0}{g - f} = \\frac{w_0}{|\\phi|}$$
   The radical population reaches a finite, stable steady state. The reaction proceeds smoothly and slowly.
2. **Critical Limit ($\\phi = 0$, $f = g$)**:
   Branching exactly balances termination:
   $$n(t) = w_0 t$$
   Linear growth marking the boundary of explosion.
3. **Explosive Super-Critical Regime ($\\phi > 0$, $f > g$)**:
   Branching exceeds termination. The exponential term $e^{\\phi t}$ diverges:
   $$n(t) = \\frac{w_0}{\\phi} e^{\\phi t} \\longrightarrow \\infty$$
   The active radical concentration multiplies exponentially within milliseconds, producing an isothermal **chain-branching explosion**."""
            },
            {
                "id": "sec-8-5",
                "secNumber": "8.5",
                "title": "The Hydrogen-Oxygen Explosion Peninsula: Three Pressure Limits",
                "content": """The reaction $2 H_2 + O_2 \\longrightarrow 2 H_2O$ exhibits an iconic \"explosion peninsula\" in a pressure-temperature ($P-T$) phase diagram, governed by competition between branching and termination.

### Elementary Branching Mechanism
- **Initiation**:
  $$H_2 + O_2 \\longrightarrow HO_2^\\bullet + H^\\bullet$$
- **Branching Step 1**:
  $$H^\\bullet + O_2 \\\\xrightarrow{k_2} \\cdot OH + \\cdot O \\cdot \\quad (\\text{One carrier } H \\to \\text{ two carriers } OH + O)$$
- **Branching Step 2**:
  $$\\cdot O \\cdot + H_2 \\\\xrightarrow{k_3} \\cdot OH + H^\\bullet \\quad (\\text{One carrier } O \\to \\text{ two carriers } OH + H)$$
- **Propagation**:
  $$\\cdot OH + H_2 \\\\xrightarrow{k_1} H_2O + H^\\bullet$$
Net result of the branching cycle:
$$H^\\bullet + O_2 + 2 H_2 \\longrightarrow 2 \\cdot OH + H^\\bullet + H_2O$$
From one $H$ atom, **three active radicals** are produced (net generation of $+2$ radicals).

### The Three Explosion Limits
1. **First (Lower) Limit ($P_1$)**:
   At very low pressures (few Torr), mean free path is long. Radicals diffuse rapidly to the reactor walls where they are destroyed ($g_{\\text{wall}} \\propto D / d^2 \\propto 1 / (P d^2)$).
   Explosion occurs when branching overcomes wall loss:
   $$2 k_2 [O_2] > k_{\\text{wall}} \\implies P_1 \\propto \\frac{1}{d}$$
2. **Second (Upper) Limit ($P_2$)**:
   As pressure rises, termolecular gas-phase termination becomes dominant:
   $$H^\\bullet + O_2 + M \\\\xrightarrow{k_4} HO_2^\\bullet + M$$
   The hydroperoxyl radical $HO_2^\\bullet$ is unreactive at moderate temperatures and diffuses to the wall without branching.
   Condition for explosion:
   $$2 k_2 [O_2] > k_4 [O_2][M] \\implies [M]_2 = \\frac{2 k_2}{k_4}$$
   Because $k_2$ has high activation energy ($E_a \\approx 70\\text{ kJ/mol}$) and $k_4$ has near-zero activation energy, $P_2$ increases exponentially with temperature.
3. **Third Limit ($P_3$)**:
   At high pressures ($P > 1\\text{ bar}$), $HO_2^\\bullet$ begins to react via $HO_2^\\bullet + H_2 \\longrightarrow H_2O_2 + H^\\bullet$, regenerating radicals while massive exothermic heat release triggers thermal runaway."""
            },
            {
                "id": "sec-8-6",
                "secNumber": "8.6",
                "title": "Hydrocarbon Combustion, Cool Flames & Degenerate Branching",
                "content": """The oxidation of hydrocarbons ($RH + O_2$) exhibits complex kinetic behavior including two-stage ignition, cool flames, and negative temperature coefficient (NTC) behavior.

### Degenerate Chain Branching (Semenov)
Unlike $H_2 + O_2$ where branching is instantaneous via unstable atoms, hydrocarbon oxidation forms relatively stable molecular intermediates (hydroperoxides $ROOH$, aldehydes $RCHO$) that slowly decompose to produce radicals:
$$RH + O_2 \\longrightarrow R^\\bullet + HO_2^\\bullet$$
$$R^\\bullet + O_2 \\longrightarrow RO_2^\\bullet$$
$$RO_2^\\bullet + RH \\longrightarrow ROOH + R^\\bullet$$
The hydroperoxide undergoes occasional unimolecular homolysis:
$$ROOH \\\\xrightarrow{k_{\\text{deg}}} RO^\\bullet + ^\\bullet OH$$
Because $ROOH$ has a lifetime of seconds, radical multiplication is delayed: **degenerate branching**.

### Cool Flame Phenomena and NTC Regime
Between $300^\\circ\\text{C}$ and $400^\\circ\\text{C}$, hydrocarbons exhibit a pale bluish luminescence called a **cool flame**, emitted by electronically excited formaldehyde ($HCHO^* \\to HCHO + h\\nu$).
In this temperature window, the reaction rate **slows down** as temperature increases (Negative Temperature Coefficient, NTC).
- **Kinetic Origin**: The peroxy radical equilibrium $R^\\bullet + O_2 \\rightleftharpoons RO_2^\\bullet$ shifts backward at higher temperatures, favoring non-branching alkene formation ($R^\\bullet + O_2 \\to \\text{alkene} + HO_2^\\bullet$). This kinetic competition underpins engine knock in internal combustion engines and defines fuel octane ratings."""
            },
            {
                "id": "sec-8-7",
                "secNumber": "8.7",
                "title": "Thermal Explosion Theory: Semenov & Frank-Kamenetskii Criteria",
                "content": """In contrast to isothermal branched-chain explosions, a **thermal explosion** occurs when the rate of exothermic chemical heat generation exceeds the rate of heat dissipation to the surroundings.

### Semenov Thermal Explosion Model (Uniform Temperature)
Consider a reaction vessel of volume $V$, surface area $S$, and heat transfer coefficient $\\chi$, containing an exothermic reaction ($\Delta H_r < 0$) with rate $r = k_0 e^{-E_a / R T} c^n$:

1. **Rate of Heat Generation ($q_{\\text{gen}}$)**:
   $$q_{\\text{gen}} = V (-\Delta H_r) k_0 c^n \\exp\\left( -\\frac{E_a}{R T} \\right)$$
   Increases exponentially with temperature $T$.

2. **Rate of Heat Removal ($q_{\\text{loss}}$)**:
   $$q_{\\text{loss}} = S \\chi (T - T_0)$$
   Increases linearly with temperature $T$ above ambient wall temperature $T_0$ (Newton's law of cooling).

### Critical Semenov Condition
Steady-state heat balance requires $q_{\\text{gen}} = q_{\\text{loss}}$.
The boundary of stability occurs when the heat generation curve is tangent to the heat loss line:
$$q_{\\text{gen}} = q_{\\text{loss}} \\quad \\text{and} \\quad \\frac{dq_{\\text{gen}}}{dT} = \\frac{dq_{\\text{loss}}}{dT}$$

Evaluating derivatives:
$$\\frac{E_a}{R T_{\\text{crit}}^2} q_{\\text{gen}} = S \\chi$$
Substituting $q_{\\text{gen}} = S \\chi (T_{\\text{crit}} - T_0)$:
$$\\frac{E_a}{R T_{\\text{crit}}^2} (T_{\\text{crit}} - T_0) = 1 \\implies \\Delta T_{\\text{crit}} = T_{\\text{crit}} - T_0 \\approx \\frac{R T_0^2}{E_a}$$
For typical activation energies ($E_a \\approx 100\\text{ kJ/mol}$, $T_0 \\approx 300\\text{ K}$):
$$\\Delta T_{\\text{crit}} \\approx \\frac{8.314 \\times (300)^2}{100000} \\approx 7.5\\text{ K}$$
If the self-heating exceeds this critical temperature rise $\\Delta T_{\\text{crit}}$, heat generation outstrips heat removal, triggering catastrophic thermal runaway."""
            }
        ],
        "problems": [
            {
                "id": "p8-1",
                "title": "Kinetic Chain Length in Photochemical Free-Radical Chlorination",
                "difficulty": "Easy",
                "statement": "In a gas-phase photochemical chlorination of methane ($CH_4 + Cl_2 \\\\xrightarrow{h\\nu} CH_3Cl + HCl$), a light pulse delivers an absorbed photon rate of $I_a = 4.50 \\times 10^{-6}\\text{ Einstein}/(\\text{L}\\cdot\\text{s})$. The quantum yield of initiation is $\\Phi_i = 1.00$ ($r_i = 2 I_a$). The steady-state rate of formation of chloromethane is measured to be $r_p = 0.450\\text{ mol}/(\\text{L}\\cdot\\text{s})$. Calculate: (a) the initiation rate $r_i$, and (b) the kinetic chain length $\\Lambda_{\\text{chain}}$.",
                "solution": """**Step 1: Calculate rate of initiation $r_i$**
Each absorbed photon dissociates one $Cl_2$ into two $Cl^\\bullet$ radicals:
$$r_i = 2 \\Phi_i I_a = 2 \\times 1.00 \\times (4.50 \\times 10^{-6}\\text{ mol}/(\\text{L}\\cdot\\text{s})) = 9.00 \\times 10^{-6}\\text{ mol}/(\\text{L}\\cdot\\text{s})$$

**Step 2: Calculate kinetic chain length $\\Lambda_{\\text{chain}}$**
$$\\Lambda_{\\text{chain}} = \\frac{r_p}{r_i} = \\frac{0.450\\text{ mol}/(\\text{L}\\cdot\\text{s})}{9.00 \\times 10^{-6}\\text{ mol}/(\\text{L}\\cdot\\text{s})} = 5.00 \\times 10^4 = 50000$$

A single absorbed photon initiates a chain reaction that produces **$50,000$ molecules** of chloromethane before radical termination occurs."""
            },
            {
                "id": "p8-2",
                "title": "Bodenstein Hydrogen-Bromine Inhibition Ratio Evaluation",
                "difficulty": "Medium",
                "statement": "The empirical rate law for the hydrogen-bromine reaction is $r = \\frac{k [H_2][Br_2]^{1/2}}{1 + m ([HBr]/[Br_2])}$. In an experiment at $T = 575.0\\text{ K}$, the rate of $HBr$ formation with zero initial $HBr$ was $r_0 = 1.20 \\times 10^{-4}\\text{ M/s}$. When $HBr$ was added such that the ratio $[HBr]/[Br_2] = 2.00$, the measured rate dropped to $r = 6.00 \\times 10^{-5}\\text{ M/s}$. Calculate: (a) the inhibition parameter $m = k_4 / k_3$, and (b) the ratio of rate constants $k_3 / k_4$.",
                "solution": """**Step 1: Formulate rate ratio**
$$r_0 = k [H_2] [Br_2]^{1/2}$$
$$r = \\frac{k [H_2] [Br_2]^{1/2}}{1 + m \\left( \\frac{[HBr]}{[Br_2]} \\right)} = \\frac{r_0}{1 + m (2.00)}$$

**Step 2: Solve for $m$**
$$\\frac{r_0}{r} = 1 + 2.00 \\, m$$
$$\\frac{1.20 \\times 10^{-4}}{6.00 \\times 10^{-5}} = 2.000 = 1 + 2.00 \\, m$$
$$2.00 \\, m = 1.000 \\implies m = 0.500$$

**Step 3: Evaluate ratio $k_3 / k_4$**
From the Christiansen-Kramers-Polanyi mechanism:
$$m = \\frac{k_4}{k_3} = 0.500 \\implies \\frac{k_3}{k_4} = \\frac{1}{0.500} = 2.00$$
The attack of atomic hydrogen on molecular bromine ($H^\\bullet + Br_2 \\\\xrightarrow{k_3} HBr + Br^\\bullet$) is twice as fast as the product-inhibiting back-attack on hydrogen bromide ($H^\\bullet + HBr \\\\xrightarrow{k_4} H_2 + Br^\\bullet$)."""
            },
            {
                "id": "p8-3",
                "title": "Free-Radical Polymerization Rate and Degree of Polymerization",
                "difficulty": "Hard",
                "statement": """Methyl methacrylate is polymerized in benzene at $60.0^\\circ\\text{C}$ with monomer concentration $[M] = 2.00\\text{ M}$ using AIBN initiator at $[I] = 5.00 \\times 10^{-3}\\text{ M}$. Kinetic constants at $60^\\circ\\text{C}$ are:
- $k_d = 8.50 \\times 10^{-6}\\text{ s}^{-1}$ (initiator efficiency $f = 0.60$)
- $k_p = 515\\text{ M}^{-1}\\text{s}^{-1}$
- $k_t = 2.55 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}$ (termination exclusively by combination)

Calculate: (a) the steady-state radical concentration $[M^\\bullet]$, (b) the polymerization rate $r_p$ in $\\text{mol}/(\\text{L}\\cdot\\text{s})$, and (c) the number-average degree of polymerization $\\bar{X}_n$.""",
                "solution": """**Step 1: Calculate steady-state radical concentration $[M^\\bullet]$**
$$[M^\\bullet] = \\sqrt{\\frac{f k_d [I]}{k_t}}$$
$$f k_d [I] = 0.60 \\times (8.50 \\times 10^{-6}\\text{ s}^{-1}) \\times (5.00 \\times 10^{-3}\\text{ M}) = 2.55 \\times 10^{-8}\\text{ M/s}$$
$$\\frac{f k_d [I]}{k_t} = \\frac{2.55 \\times 10^{-8}\\text{ M/s}}{2.55 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}} = 1.000 \\times 10^{-15}\\text{ M}^2$$
$$[M^\\bullet] = \\sqrt{1.000 \\times 10^{-15}} = 3.1623 \\times 10^{-8}\\text{ M}$$

**Step 2: Calculate polymerization rate $r_p$**
$$r_p = k_p [M] [M^\\bullet] = (515\\text{ M}^{-1}\\text{s}^{-1}) \\times (2.00\\text{ M}) \\times (3.1623 \\times 10^{-8}\\text{ M}) = 3.257 \\times 10^{-5}\\text{ mol}/(\\text{L}\\cdot\\text{s})$$

**Step 3: Number-average degree of polymerization $\\bar{X}_n$**
Because termination is exclusively by combination, each dead polymer chain contains two kinetic chains:
$$\\bar{X}_n = \\frac{2 r_p}{r_i} = \\frac{2 r_p}{2 f k_d [I]} = \\frac{r_p}{f k_d [I]} = \\frac{3.257 \\times 10^{-5}\\text{ M/s}}{2.55 \\times 10^{-8}\\text{ M/s}} = 1277$$
The resulting poly(methyl methacrylate) chains have an average length of **1,277 monomer units** ($M_n \\approx 1.28 \\times 10^5\\text{ g/mol}$)."""
            },
            {
                "id": "p8-4",
                "title": "Semenov Branched-Chain Explosion Induction Time Calculation",
                "difficulty": "Hard",
                "statement": "In a gas mixture undergoing branched-chain explosion, the background thermal initiation rate is $w_0 = 1.50 \\times 10^{10}\\text{ radicals}/(\\text{cm}^3\\cdot\\text{s})$. The net branching factor is $\\phi = f - g = +12.0\\text{ s}^{-1}$. (a) Calculate the time required for the active radical population $n(t)$ to multiply from zero to a critical explosion threshold of $n_{\\text{crit}} = 1.00 \\times 10^{16}\\text{ radicals/cm}^3$. (b) What would the steady-state radical population be if termination exceeded branching by $\\phi = -12.0\\text{ s}^{-1}$?",
                "solution": """**Step 1: Calculate explosion induction time for $\\phi = +12.0\\text{ s}^{-1}$**
Using Semenov's equation:
$$n(t) = \\frac{w_0}{\\phi} \\left( e^{\\phi t} - 1 \\right)$$
$$n_{\\text{crit}} = \\frac{w_0}{\\phi} e^{\\phi t_{\\text{ind}}} \\quad (\\text{since } e^{\\phi t} \\gg 1)$$

$$e^{\\phi t_{\\text{ind}}} = \\frac{\\phi \\, n_{\\text{crit}}}{w_0}$$
$$\\frac{\\phi \\, n_{\\text{crit}}}{w_0} = \\frac{12.0\\text{ s}^{-1} \\times (1.00 \\times 10^{16}\\text{ cm}^{-3})}{1.50 \\times 10^{10}\\text{ cm}^{-3}\\text{s}^{-1}} = \\frac{1.20 \\times 10^{17}}{1.50 \\times 10^{10}} = 8.00 \\times 10^6$$

Taking natural logarithms:
$$\\phi t_{\\text{ind}} = \\ln(8.00 \\times 10^6) = 15.895$$
$$t_{\\text{ind}} = \\frac{15.895}{12.0\\text{ s}^{-1}} = 1.325\\text{ s}$$
The system explodes within **$1.33\\text{ seconds}$** of ignition.

**Step 2: Steady-state population for $\\phi = -12.0\\text{ s}^{-1}$**
In the stationary regime:
$$n_{\\text{ss}} = \\frac{w_0}{|\\phi|} = \\frac{1.50 \\times 10^{10}\\text{ cm}^{-3}\\text{s}^{-1}}{12.0\\text{ s}^{-1}} = 1.25 \\times 10^9\\text{ radicals/cm}^3$$
The radical population remains stably clamped at $1.25 \\times 10^9\\text{ cm}^{-3}$, seven orders of magnitude below the explosion threshold."""
            },
            {
                "id": "p8-5",
                "title": "Second Explosion Limit Shift for Hydrogen-Oxygen with Buffer Gas",
                "difficulty": "Medium",
                "statement": "The second explosion limit of a stoichiometric $2 H_2 + O_2$ mixture at $500^\\circ\\text{C}$ is governed by the branching step $H + O_2 \\\\xrightarrow{k_2} OH + O$ and the termolecular termination step $H + O_2 + M \\\\xrightarrow{k_4} HO_2 + M$. For pure $2 H_2 + O_2$, the measured second limit is $P_2 = 42.0\\text{ Torr}$. If argon buffer gas is added such that the gas is $10\\%\\; H_2$, $5\\%\\; O_2$, and $85\\%\\; Ar$, given that argon has a third-body collision efficiency of only $\\alpha_{Ar} = 0.35$ relative to $H_2/O_2$ ($\alpha = 1.00$), calculate the new second explosion limit pressure $P_2'$ in Torr.",
                "solution": """**Step 1: Effective third-body concentration at the second limit**
The condition for the second limit is:
$$2 k_2 [O_2] = k_4 [O_2] [M]_{\\text{eff}} \\implies [M]_{\\text{eff}} = \\frac{2 k_2}{k_4} = \\text{constant at fixed } T$$

For the pure mixture:
$$[M]_{\\text{eff}} = P_2 = 42.0\\text{ Torr}$$

**Step 2: Calculate effective third-body efficiency of the argon mixture**
In the argon mixture:
$$\\chi_{\\text{eff}} = y_{H_2} (1.00) + y_{O_2} (1.00) + y_{Ar} (0.35) = 0.10(1.00) + 0.05(1.00) + 0.85(0.35)$$
$$\\chi_{\\text{eff}} = 0.15 + 0.2975 = 0.4475$$

**Step 3: Calculate new limit pressure $P_2'$**
$$[M]_{\\text{eff}} = \\chi_{\\text{eff}} P_2' = 42.0\\text{ Torr}$$
$$P_2' = \\frac{42.0\\text{ Torr}}{0.4475} = 93.85\\text{ Torr}$$
Because argon is an inefficient third-body collision partner for radical deactivation, the explosion peninsula expands upward, raising the second limit from $42.0\\text{ Torr}$ to **$93.9\\text{ Torr}$**."""
            },
            {
                "id": "p8-6",
                "title": "Semenov Critical Self-Heating Temperature Rise for Exothermic Runaway",
                "difficulty": "Medium",
                "statement": "An exothermic batch reactor operates with an ambient coolant wall temperature of $T_0 = 350.0\\text{ K}$. The reaction has an activation energy of $E_a = 92.5\\text{ kJ/mol}$. (a) Calculate the critical Semenov temperature rise $\\Delta T_{\\text{crit}} = T_{\\text{crit}} - T_0$ beyond which catastrophic thermal explosion occurs. (b) What is the maximum allowable internal temperature $T_{\\text{crit}}$ to avoid runaway?",
                "solution": """**Step 1: Semenov critical temperature rise formula**
$$\\Delta T_{\\text{crit}} = \\frac{R T_0^2}{E_a}$$
$$R = 8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})$$
$$T_0^2 = (350.0)^2 = 1.2250 \\times 10^5\\text{ K}^2$$
$$E_a = 92500\\text{ J/mol}$$

$$\\Delta T_{\\text{crit}} = \\frac{8.314462 \\times (1.2250 \\times 10^5)}{92500} = \\frac{1.01852 \\times 10^6}{92500} = 11.01\\text{ K}$$

**Step 2: Maximum allowable internal temperature**
$$T_{\\text{crit}} = T_0 + \\Delta T_{\\text{crit}} = 350.0 + 11.01 = 361.01\\text{ K} = 87.86^\\circ\\text{C}$$
If the internal reacting fluid temperature exceeds $361.0\\text{ K}$ (a self-heating rise of merely $11^\\circ\\text{C}$ above coolant), the exponential heat generation curve overtakes linear heat transfer, initiating irreversible thermal explosion."""
            },
            {
                "id": "p8-7",
                "title": "Frank-Kamenetskii Dimensionless Critical Parameter for Vessel Geometry",
                "difficulty": "Hard",
                "statement": """In the Frank-Kamenetskii thermal explosion theory, which accounts for internal conductive temperature gradients, the dimensionless explosion parameter is:
$$\\delta = \\frac{Q_r E_a r_0^2 k(T_0) c_0^n}{\\kappa R T_0^2}$$
where $r_0$ is the characteristic radius, $Q_r$ is heat of reaction, $\\kappa$ is thermal conductivity, and $T_0$ is surface wall temperature. For an infinite cylinder, the critical threshold is $\\delta_{\\text{crit}} = 2.00$. A cylindrical storage vessel has radius $r_0 = 0.250\\text{ m}$. Given $Q_r = 1.80 \\times 10^5\\text{ J/mol}$, $E_a = 85.0\\text{ kJ/mol}$, $\\kappa = 0.150\\text{ W}/(\\text{m}\\cdot\\text{K})$, and $T_0 = 320.0\\text{ K}$, calculate the maximum safe zero-order reaction rate $k(T_0) c_0^n$ in $\\text{mol}/(\\text{m}^3\\cdot\\text{s})$ to prevent thermal runaway.""",
                "solution": """**Step 1: Evaluate parameters in the Frank-Kamenetskii equation**
$$r_0 = 0.250\\text{ m} \\implies r_0^2 = 0.0625\\text{ m}^2$$
$$Q_r = 1.80 \\times 10^5\\text{ J/mol}$$
$$E_a = 8.50 \\times 10^4\\text{ J/mol}$$
$$\\kappa = 0.150\\text{ W}/(\\text{m}\\cdot\\text{K}) = 0.150\\text{ J}/(\\text{s}\\cdot\\text{m}\\cdot\\text{K})$$
$$T_0 = 320.0\\text{ K} \\implies T_0^2 = 1.024 \\times 10^5\\text{ K}^2$$
$$R T_0^2 = 8.314462 \\times 1.024 \\times 10^5 = 8.5140 \\times 10^5\\text{ J}\\cdot\\text{K/mol}$$

**Step 2: Solve for reaction rate at critical condition $\\delta_{\\text{crit}} = 2.00$**
$$\\delta = \\frac{Q_r E_a r_0^2}{\\kappa R T_0^2} \\cdot \\text{Rate} = 2.00$$
$$\\text{Rate} = \\frac{2.00 \\kappa R T_0^2}{Q_r E_a r_0^2}$$

Numerator:
$$2.00 \\times 0.150 \\times (8.5140 \\times 10^5) = 2.5542 \\times 10^5\\text{ J}^2/(\\text{s}\\cdot\\text{m}\\cdot\\text{mol})$$

Denominator:
$$(1.80 \\times 10^5) \\times (8.50 \\times 10^4) \\times 0.0625 = 9.5625 \\times 10^8\\text{ J}^2\\cdot\\text{m}^2/\\text{mol}^2$$

Maximum allowable rate:
$$\\text{Rate} = \\frac{2.5542 \\times 10^5}{9.5625 \\times 10^8} = 2.671 \\times 10^{-4}\\text{ mol}/(\\text{m}^3\\cdot\\text{s})$$"""
            }
        ]
    }
    units.append(u8)

    # =========================================================================
    # UNIT 9: Homogeneous, Enzymatic & Oscillating Catalytic Systems
    # =========================================================================
    u9 = {
        "id": "unit-9",
        "unitNumber": 9,
        "title": "Unit 9: Homogeneous, Enzymatic & Oscillating Catalytic Systems",
        "leadSummary": "Comprehensive kinetics of catalytic reaction networks: homogeneous acid-base catalysis, Brønsted catalysis laws, enzyme-substrate binding, Briggs-Haldane steady-state derivation of Michaelis-Menten kinetics, catalytic turnover numbers, graphical linearizations, competitive, uncompetitive, and non-competitive enzyme inhibition, autocatalysis, and non-linear chemical dynamics (Lotka-Volterra, Belousov-Zhabotinsky oscillator, and the Brusselator).",
        "simulations": ["sim_kin_michaelis_menten_inhibition"],
        "sections": [
            {
                "id": "sec-9-1",
                "secNumber": "9.1",
                "title": "Homogeneous Catalysis Principles: Activation Barrier Lowering",
                "content": """A catalyst is a substance that accelerates the rate of a chemical reaction without being consumed in the net stoichiometric process, by providing an alternative reaction pathway with a lower activation free energy ($\Delta G^\ddagger$).

### Fundamental Thermodynamic Invariants
1. **Unchanged Equilibrium Constant**: Because a catalyst alters only kinetic barrier heights without altering the standard chemical potentials of reactants and products:
   $$\Delta G^\circ = -R T \ln K_c = \text{invariant}$$
   A catalyst accelerates both forward ($k_1$) and reverse ($k_{-1}$) reactions by exactly identical factors, leaving $K_c = k_1 / k_{-1}$ strictly unchanged.
2. **Microscopic Reversibility**: The catalyzed pathway for the forward reaction must be the exact microscopic reverse of the catalyzed pathway for the backward reaction.

### Rate Enhancement Factor
According to the Arrhenius equation:
$$\frac{k_{\text{cat}}}{k_{\text{uncat}}} = \exp\left( \frac{E_{a, \text{uncat}} - E_{a, \text{cat}}}{R T} \right) = \exp\left( \frac{\Delta E_a}{R T} \right)$$
At room temperature ($R T \approx 2.48\text{ kJ/mol}$), lowering the activation energy by:
- $10\text{ kJ/mol}$ increases the rate by a factor of $e^{4.03} \approx 56$.
- $30\text{ kJ/mol}$ increases the rate by a factor of $e^{12.1} \approx 1.8 \times 10^5$.
- $60\text{ kJ/mol}$ increases the rate by a factor of $e^{24.2} \approx 3.2 \times 10^{10}$."""
            },
            {
                "id": "sec-9-2",
                "secNumber": "9.2",
                "title": "Homogeneous Acid-Base Catalysis & The Brønsted Catalysis Law",
                "content": """Acid-base catalysis governs a vast domain of organic, biochemical, and industrial reactions (esterification, mutarotation, keto-enol tautomerism).

### Specific vs. General Acid Catalysis
1. **Specific Acid Catalysis**:
   The reaction rate depends strictly on the concentration of solvated protons (hydronium ions, $[H_3O^+]$), independent of the concentration of undissociated buffer acid $[HA]$:
   $$r = k_H [H_3O^+] [S]$$
   - *Mechanism*: Rapid, reversible protonation of substrate $S$ to form conjugate acid $SH^+$, followed by slow, rate-determining conversion:
     $$S + H_3O^+ \\underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} SH^+ + H_2O \quad (\text{fast pre-equilibrium})$$
     $$SH^+ \\\\xrightarrow{k_2} P \quad (\text{slow})$$

2. **General Acid Catalysis**:
   Proton transfer occurs directly in the rate-determining step. Every proton donor in solution contributes to the rate:
   $$r = \left( k_0 + k_H [H_3O^+] + \sum_i k_{HA, i} [HA]_i \right) [S]$$

### The Brønsted Catalysis Law (1924)
Johannes Brønsted discovered a linear free-energy relationship (LFER) connecting the catalytic rate constant $k_A$ of general acid catalysts to their acid dissociation constants $K_a$:
$$\log_{10} k_A = \alpha \log_{10} K_a + \text{constant} \iff k_A = C \cdot K_a^\alpha$$
where:
- $\alpha$ is the Brønsted coefficient ($0 < \alpha < 1$).
- $\alpha \to 1$: Transition state resembles protonated product (late transition state).
- $\alpha \to 0$: Transition state resembles unprotonated reactant (early transition state)."""
            },
            {
                "id": "sec-9-3",
                "secNumber": "9.3",
                "title": "Enzyme Catalysis Foundations: Active Site Architecture & Induced-Fit",
                "content": """Enzymes are macromolecular biological catalysts (primarily globular proteins and catalytic RNAs) exhibiting extraordinary catalytic power and stereochemical specificity.

### Mechanisms of Enzymatic Acceleration
1. **Proximity and Orientation Effects**: Binding substrates in precise relative spatial alignment within the active site increases effective local concentration by up to $10^5\text{ M}$, reducing activation entropy ($\Delta S^\ddagger$).
2. **Transition-State Stabilization (Pauling Principle)**: The active site is complementary not to the ground-state substrate, but to the **transition state** structure ($S^\ddagger$). Strong binding to $S^\ddagger$ drastically lowers $\Delta G^\ddagger$.
3. **Acid-Base and Covalent Catalysis**: Catalytic amino acid side chains (His, Asp, Glu, Lys, Cys) act as synchronized general acids and bases, or form transient covalent intermediates.
4. **Induced Fit (Koshland, 1958)**: Binding of substrate induces conformational rearrangements that clamp the active site around the substrate, excluding bulk water and aligning catalytic residues."""
            },
            {
                "id": "sec-9-4",
                "secNumber": "9.4",
                "title": "The Michaelis-Menten Mechanism: Briggs-Haldane Steady-State Derivation",
                "content": """Leonor Michaelis and Maud Menten (1913) formulated the fundamental kinetic model of enzyme action, rigorously generalized by G.E. Briggs and J.B.S. Haldane (1925) using the steady-state approximation.

### The Reaction Scheme
$$E + S \\underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} ES \\\\xrightarrow{k_{\text{cat}}} E + P$$
where:
- $E$ is free enzyme, $S$ is substrate, $ES$ is the enzyme-substrate complex, and $P$ is product.
- Total enzyme concentration is conserved: $[E]_0 = [E] + [ES]$.

### Steady-State Derivation
Applying the Bodenstein SSA to $[ES]$:
$$\frac{d[ES]}{dt} = k_1 [E][S] - k_{-1} [ES] - k_{\text{cat}} [ES] = 0$$
Substitute $[E] = [E]_0 - [ES]$:
$$k_1 ([E]_0 - [ES]) [S] = (k_{-1} + k_{\text{cat}}) [ES]$$
$$k_1 [E]_0 [S] - k_1 [ES][S] = (k_{-1} + k_{\text{cat}}) [ES]$$
$$[ES] \left[ (k_{-1} + k_{\text{cat}}) + k_1 [S] \right] = k_1 [E]_0 [S]$$

Dividing by $k_1$:
$$[ES] \left( \frac{k_{-1} + k_{\text{cat}}}{k_1} + [S] \right) = [E]_0 [S]$$

Defining the **Michaelis Constant** $K_m$:
$$K_m \equiv \frac{k_{-1} + k_{\text{cat}}}{k_1}$$
$$[ES] = \frac{[E]_0 [S]}{K_m + [S]}$$

### Velocity Equation
The initial reaction velocity is:
$$v = \frac{d[P]}{dt} = k_{\text{cat}} [ES] = \frac{k_{\text{cat}} [E]_0 [S]}{K_m + [S]}$$

Defining the maximum velocity $V_{\max} \equiv k_{\text{cat}} [E]_0$:
$$v = \frac{V_{\max} [S]}{K_m + [S]}$$
This is the celebrated **Michaelis-Menten Equation** (a rectangular hyperbola).

### Physical Significance of Parameters
1. **$V_{\max}$**: Asymptote reached at saturating substrate ($[S] \gg K_m$), where all enzyme is locked in complex ($[ES] \approx [E]_0$).
2. **$K_m$**: Substrate concentration at which initial velocity is half-maximal ($v = V_{\max} / 2$). Represents an apparent dissociation constant; when $k_{-1} \gg k_{\text{cat}}$, $K_m \to K_d = k_{-1} / k_1$.
3. **Turnover Number ($k_{\text{cat}} = V_{\max} / [E]_0$)**: Maximum number of substrate molecules converted to product per enzyme active site per second (units: $\text{s}^{-1}$).
4. **Catalytic Efficiency ($k_{\text{cat}} / K_m$)**: The apparent second-order rate constant at low substrate concentrations ($[S] \ll K_m$):
   $$v \approx \left( \frac{k_{\text{cat}}}{K_m} \right) [E]_0 [S]$$
   Capped by the diffusion-controlled encounter limit ($\sim 10^8\text{--}10^9\text{ M}^{-1}\text{s}^{-1}$), characterizing \"catalytically perfect\" enzymes (e.g., catalase, carbonic anhydrase)."""
            },
            {
                "id": "sec-9-5",
                "secNumber": "9.5",
                "title": "Graphical Linearization Methods: Lineweaver-Burk, Eadie-Hofstee & Hanes-Woolf",
                "content": """Because the Michaelis-Menten curve is hyperbolic, determining $V_{\max}$ and $K_m$ by visual inspection of non-linear plots is prone to error. Three classical algebraic linearizations were developed.

### 1. Lineweaver-Burk (Double-Reciprocal) Plot (1934)
Inverting the Michaelis-Menten equation:
$$\frac{1}{v} = \frac{K_m + [S]}{V_{\max} [S]} = \left( \frac{K_m}{V_{\max}} \right) \frac{1}{[S]} + \frac{1}{V_{\max}}$$
Plotting $1/v$ versus $1/[S]$ yields a straight line:
- Slope $= K_m / V_{\max}$
- $y$-intercept $= 1 / V_{\max}$
- $x$-intercept $= -1 / K_m$
- *Limitation*: Unequal statistical weighting; small errors at low $[S]$ (large $1/[S]$) dominate the fit.

### 2. Eadie-Hofstee Plot
Multiplying the Lineweaver-Burk equation by $v V_{\max}$:
$$v = V_{\max} - K_m \left( \frac{v}{[S]} \right)$$
Plotting $v$ versus $v / [S]$ yields a straight line:
- Slope $= -K_m$
- $y$-intercept $= V_{\max}$
- $x$-intercept $= V_{\max} / K_m$
Provides more uniform weighting across concentration ranges.

### 3. Hanes-Woolf Plot
Multiplying Lineweaver-Burk by $[S]$:
$$\frac{[S]}{v} = \left( \frac{1}{V_{\max}} \right) [S] + \frac{K_m}{V_{\max}}$$
Plotting $[S]/v$ versus $[S]$:
- Slope $= 1 / V_{\max}$
- $y$-intercept $= K_m / V_{\max}$
- $x$-intercept $= -K_m$"""
            },
            {
                "id": "sec-9-6",
                "secNumber": "9.6",
                "title": "Reversible Enzyme Inhibition: Competitive, Uncompetitive & Non-Competitive",
                "content": """Enzyme inhibitors are chemical agents that diminish catalytic activity, serving as vital pharmacophores and metabolic regulators.

### 1. Competitive Inhibition
The inhibitor $I$ is a structural analog of substrate that binds exclusively to free enzyme active site ($E + I \rightleftharpoons EI$, dissociation constant $K_i$):
$$v = \frac{V_{\max} [S]}{\alpha K_m + [S]}$$
where $\alpha = 1 + \frac{[I]}{K_i}$.
- **Apparent Parameters**: $V_{\max}^{\text{app}} = V_{\max}$ (unchanged); $K_m^{\text{app}} = \alpha K_m$ (increased).
- **Lineweaver-Burk**: Lines intersect on the $y$-axis at $1/V_{\max}$.

### 2. Uncompetitive Inhibition
The inhibitor binds exclusively to the enzyme-substrate complex ($ES + I \rightleftharpoons ESI$, dissociation constant $K_i'$):
$$v = \frac{(V_{\max}/\alpha') [S]}{(K_m/\alpha') + [S]} = \frac{V_{\max} [S]}{K_m + \alpha' [S]}$$
where $\alpha' = 1 + \frac{[I]}{K_i'}$.
- **Apparent Parameters**: $V_{\max}^{\text{app}} = V_{\max} / \alpha'$ (decreased); $K_m^{\text{app}} = K_m / \alpha'$ (decreased by identical factor!).
- **Lineweaver-Burk**: Produces a set of strictly **parallel lines** (slope $K_m/V_{\max}$ is invariant).

### 3. Non-Competitive (Mixed) Inhibition
The inhibitor binds with equal affinity to both free enzyme and $ES$ complex ($K_i = K_i'$, so $\alpha = \alpha'$):
$$v = \frac{(V_{\max}/\alpha) [S]}{K_m + [S]}$$
- **Apparent Parameters**: $V_{\max}^{\text{app}} = V_{\max} / \alpha$ (decreased); $K_m^{\text{app}} = K_m$ (unchanged).
- **Lineweaver-Burk**: Lines intersect on the negative $x$-axis at $-1/K_m$."""
            },
            {
                "id": "sec-9-7",
                "secNumber": "9.7",
                "title": "Autocatalysis, Oscillating Reactions & The Belousov-Zhabotinsky (BZ) Engine",
                "content": """When a chemical reaction product acts as a catalyst for its own generation, the kinetics become non-linear, giving rise to bistability, chemical clocks, and spatial Turing patterns.

### Autocatalytic Kinetics ($A + X \\\\xrightarrow{k} 2 X$)
Rate differential equation:
$$\frac{dx}{dt} = k ([A]_0 - x) x$$
where $x = [X]$. This is the classical logistic equation.
Integrating:
$$x(t) = \frac{[A]_0 x_0}{x_0 + ([A]_0 - x_0) e^{-k [A]_0 t}}$$
The rate starts near zero, undergoes exponential acceleration to an inflection point at $x = [A]_0 / 2$, and plateaus as reactant is exhausted (sigmoidal kinetics).

### The Belousov-Zhabotinsky (BZ) Reaction
Discovered by Boris Belousov (1951) and refined by Anatol Zhabotinsky (1964), the BZ reaction oxidizes malonic acid by bromate in acidic solution catalyzed by a cerium ($Ce^{4+}/Ce^{3+}$) or ferroin redox pair:
$$2 HBrO_3 + 3 CH_2(COOH)_2 \\\\xrightarrow{Ce^{4+}/Ce^{3+}} 2 BrCH(COOH)_2 + 3 CO_2 + 4 H_2O$$
The solution spontaneously and periodically alternates between yellow ($Ce^{4+}$) and colorless ($Ce^{3+}$) (or blue and red with ferroin) for hours!

### The Oregonator Model (Field, Körös, Noyes, 1974)
The core non-linear mechanism involves five coupled steps:
1. $Br^- + HBrO_2 + H^+ \longrightarrow 2 HOBr$ (bromide scavenging)
2. $Br^- + BrO_3^- + 2 H^+ \longrightarrow HBrO_2 + HOBr$
3. $BrO_3^- + HBrO_2 + H^+ \longrightarrow 2 HBrO_2 + 2 Ce^{4+}$ (**Autocatalytic step**)
4. $2 HBrO_2 \longrightarrow BrO_3^- + HOBr + H^+$ (termination)
5. $Ce^{4+} + \text{organic substrate} \longrightarrow Ce^{3+} + f Br^-$ (bromide regeneration)

When $[Br^-]$ falls below a critical threshold, autocatalytic production of $HBrO_2$ turns on violently, rapidly oxidizing $Ce^{3+}$ to $Ce^{4+}$. Subsequent slow reaction with malonic acid regenerates $[Br^-]$, which shuts down autocatalysis, repeating the cycle in a limit-cycle relaxation oscillation."""
            }
        ],
        "problems": [
            {
                "id": "p9-1",
                "title": "Determination of Michaelis-Menten Parameters via Lineweaver-Burk Regression",
                "difficulty": "Easy",
                "statement": """An enzymatic reaction was investigated at various substrate concentrations $[S]$, yielding initial rates $v$ as follows:
- At $[S]_1 = 2.00 \\times 10^{-4}\\text{ M}$, $v_1 = 1.39 \\times 10^{-5}\\text{ M/s}$
- At $[S]_2 = 1.00 \\times 10^{-3}\\text{ M}$, $v_2 = 3.33 \\times 10^{-5}\\text{ M/s}$

Using the Lineweaver-Burk relation $\\frac{1}{v} = \\frac{K_m}{V_{\\max}} \\frac{1}{[S]} + \\frac{1}{V_{\\max}}$, calculate: (a) $V_{\\max}$, (b) the Michaelis constant $K_m$, and (c) the turnover number $k_{\\text{cat}}$ if total enzyme concentration is $[E]_0 = 5.00 \\times 10^{-8}\\text{ M}$.""",
                "solution": """**Step 1: Invert concentrations and rates**
$$x_1 = \frac{1}{[S]_1} = \frac{1}{2.00 \times 10^{-4}\text{ M}} = 5000\text{ M}^{-1}$$
$$y_1 = \frac{1}{v_1} = \frac{1}{1.39 \times 10^{-5}\text{ M/s}} = 7.1942 \times 10^4\text{ s/M}$$

$$x_2 = \frac{1}{[S]_2} = \frac{1}{1.00 \times 10^{-3}\text{ M}} = 1000\text{ M}^{-1}$$
$$y_2 = \frac{1}{v_2} = \frac{1}{3.33 \times 10^{-5}\text{ M/s}} = 3.0030 \times 10^4\text{ s/M}$$

**Step 2: Solve for slope and intercept**
$$\text{Slope } m = \frac{y_1 - y_2}{x_1 - x_2} = \frac{71942 - 30030}{5000 - 1000} = \frac{41912}{4000} = 10.478\text{ s}$$

Intercept:
$$b = \frac{1}{V_{\max}} = y_2 - m x_2 = 30030 - (10.478 \times 1000) = 30030 - 10478 = 19552\text{ s/M}$$

$$V_{\max} = \frac{1}{19552\text{ s/M}} = 5.1146 \times 10^{-5}\text{ M/s} \approx 5.11 \times 10^{-5}\text{ M/s}$$

**Step 3: Solve for $K_m$ and $k_{\text{cat}}$**
$$\frac{K_m}{V_{\max}} = m \implies K_m = m \cdot V_{\max} = 10.478\text{ s} \times (5.1146 \times 10^{-5}\text{ M/s}) = 5.359 \times 10^{-4}\text{ M} = 0.536\text{ mM}$$

Turnover number:
$$k_{\text{cat}} = \frac{V_{\max}}{[E]_0} = \frac{5.1146 \times 10^{-5}\text{ M/s}}{5.00 \times 10^{-8}\text{ M}} = 1022.9\text{ s}^{-1} \approx 1023\text{ s}^{-1}$$"""
            },
            {
                "id": "p9-2",
                "title": "Enzyme Inhibition Mode Diagnostic from Kinetic Shifts",
                "difficulty": "Medium",
                "statement": "An enzyme has baseline parameters $V_{\max} = 80.0\;\mu\text{mol}/(\text{L}\cdot\text{min})$ and $K_m = 4.00\text{ mM}$. In the presence of $[I] = 6.00\text{ mM}$ of an inhibitor, the apparent parameters are measured to be $V_{\max}^{\text{app}} = 80.0\;\mu\text{mol}/(\text{L}\cdot\text{min})$ and $K_m^{\text{app}} = 16.00\text{ mM}$. (a) Identify the mode of inhibition. (b) Calculate the inhibition constant $K_i$. (c) Calculate the reaction rate at $[S] = 4.00\text{ mM}$ in the presence of the inhibitor.",
                "solution": """**Step 1: Identify mode of inhibition**
- $V_{\max}^{\text{app}} = 80.0 = V_{\max}$ (completely unchanged).
- $K_m^{\text{app}} = 16.00\text{ mM} > K_m = 4.00\text{ mM}$ (increased by a factor of 4).
Because $V_{\max}$ is unaffected while $K_m$ increases, the mechanism is strictly **Competitive Inhibition**.

**Step 2: Calculate inhibition constant $K_i$**
For competitive inhibition:
$$K_m^{\text{app}} = \alpha K_m = \left( 1 + \frac{[I]}{K_i} \right) K_m$$
$$\alpha = \frac{K_m^{\text{app}}}{K_m} = \frac{16.00\text{ mM}}{4.00\text{ mM}} = 4.000$$
$$1 + \frac{[I]}{K_i} = 4.000 \implies \frac{[I]}{K_i} = 3.000$$
$$K_i = \frac{[I]}{3.000} = \frac{6.00\text{ mM}}{3.000} = 2.00\text{ mM}$$

**Step 3: Calculate reaction rate at $[S] = 4.00\text{ mM}$**
$$v = \frac{V_{\max} [S]}{K_m^{\text{app}} + [S]} = \frac{80.0 \times 4.00}{16.00 + 4.00} = \frac{320.0}{20.00} = 16.00\;\mu\text{mol}/(\text{L}\cdot\text{min})$$
Without inhibitor, the rate would have been $40.0\;\mu\text{mol}/(\text{L}\cdot\text{min})$; competitive inhibition reduces the velocity by $60\%.$"""
            },
            {
                "id": "p9-3",
                "title": "Brønsted Catalysis Law Linear Free-Energy Relationship",
                "difficulty": "Medium",
                "statement": """The general-acid-catalyzed dehydration of an aldehyde hydrate was studied using four carboxylic acids at $25.0^\\circ\\text{C}$:
- Acetic acid: $pK_a = 4.76$, $k_A = 1.25 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$
- Monochloroacetic acid: $pK_a = 2.86$, $k_A = 1.58 \\times 10^{-2}\\text{ M}^{-1}\\text{s}^{-1}$

(a) Calculate the Brønsted exponent $\\alpha$. (b) Predict the catalytic rate constant $k_A$ for formic acid ($pK_a = 3.75$).""",
                "solution": """**Step 1: Calculate the Brønsted exponent $\alpha$**
The Brønsted catalysis law is:
$$\log_{10} k_A = \alpha \log_{10} K_a + C = -\alpha (pK_a) + C$$
Taking differences:
$$\log_{10}(k_{A, 2}) - \log_{10}(k_{A, 1}) = -\alpha (pK_{a, 2} - pK_{a, 1})$$
$$\log_{10}\left( \frac{k_{A, 2}}{k_{A, 1}} \right) = \alpha (pK_{a, 1} - pK_{a, 2})$$

Evaluate ratios:
$$\frac{k_{A, 2}}{k_{A, 1}} = \frac{1.58 \times 10^{-2}}{1.25 \times 10^{-3}} = 12.64$$
$$\log_{10}(12.64) = 1.1017$$
$$pK_{a, 1} - pK_{a, 2} = 4.76 - 2.86 = 1.90$$

Solving for $\alpha$:
$$\alpha = \frac{1.1017}{1.90} = 0.5798 \approx 0.58$$

**Step 2: Predict $k_A$ for formic acid ($pK_a = 3.75$)**
$$\log_{10}\left( \frac{k_{A, \text{formic}}}{k_{A, \text{acetic}}} \right) = \alpha (pK_{a, \text{acetic}} - pK_{a, \text{formic}})$$
$$pK_{a, \text{acetic}} - pK_{a, \text{formic}} = 4.76 - 3.75 = 1.01$$
$$\log_{10}\left( \frac{k_{A, \text{formic}}}{1.25 \times 10^{-3}} \right) = 0.5798 \times 1.01 = 0.5856$$
$$\frac{k_{A, \text{formic}}}{1.25 \times 10^{-3}} = 10^{0.5856} = 3.851$$
$$k_{A, \text{formic}} = (1.25 \times 10^{-3}) \times 3.851 = 4.81 \times 10^{-3}\text{ M}^{-1}\text{s}^{-1}$$"""
            },
            {
                "id": "p9-4",
                "title": "Uncompetitive Enzyme Inhibition Double-Reciprocal Parallel Shifts",
                "difficulty": "Hard",
                "statement": "An enzyme-catalyzed reaction exhibiting uncompetitive inhibition has baseline parameters $V_{\max} = 150.0\;\mu\text{M/s}$ and $K_m = 50.0\;\mu\text{M}$. When inhibitor is added at $[I] = 20.0\;\mu\text{M}$, the apparent maximum velocity drops to $V_{\max}^{\text{app}} = 50.0\;\mu\text{M/s}$. (a) Calculate the uncompetitive inhibition constant $K_i'$. (b) Calculate the apparent Michaelis constant $K_m^{\text{app}}$. (c) Verify that the slope of the Lineweaver-Burk plot is strictly invariant.",
                "solution": """**Step 1: Calculate $K_i'$**
For uncompetitive inhibition:
$$V_{\max}^{\text{app}} = \frac{V_{\max}}{\alpha'} \implies \alpha' = \frac{V_{\max}}{V_{\max}^{\text{app}}} = \frac{150.0\;\mu\text{M/s}}{50.0\;\mu\text{M/s}} = 3.000$$
$$\alpha' = 1 + \frac{[I]}{K_i'} = 3.000 \implies \frac{[I]}{K_i'} = 2.000$$
$$K_i' = \frac{[I]}{2.000} = \frac{20.0\;\mu\text{M}}{2.000} = 10.0\;\mu\text{M}$$

**Step 2: Calculate $K_m^{\text{app}}$**
In uncompetitive inhibition, $K_m$ is divided by the exact same factor $\alpha'$:
$$K_m^{\text{app}} = \frac{K_m}{\alpha'} = \frac{50.0\;\mu\text{M}}{3.000} = 16.67\;\mu\text{M}$$

**Step 3: Verify Lineweaver-Burk slope invariance**
- Baseline slope:
  $$\text{Slope}_0 = \frac{K_m}{V_{\max}} = \frac{50.0\;\mu\text{M}}{150.0\;\mu\text{M/s}} = 0.3333\text{ s}$$
- Inhibited slope:
  $$\text{Slope}_{\text{inh}} = \frac{K_m^{\text{app}}}{V_{\max}^{\text{app}}} = \frac{K_m / \alpha'}{V_{\max} / \alpha'} = \frac{K_m}{V_{\max}} = \frac{16.67\;\mu\text{M}}{50.0\;\mu\text{M/s}} = 0.3333\text{ s}$$
Because $\text{Slope}_0 = \text{Slope}_{\text{inh}}$, the Lineweaver-Burk plots form perfectly parallel lines, the definitive diagnostic fingerprint of uncompetitive inhibition."""
            },
            {
                "id": "p9-5",
                "title": "Catalytic Efficiency and Diffusion-Controlled Limit for Carbonic Anhydrase",
                "difficulty": "Easy",
                "statement": "Human carbonic anhydrase II hydratizes carbon dioxide ($CO_2 + H_2O \rightleftharpoons HCO_3^- + H^+$) with extraordinary speed. At $25.0^\\circ\text{C}$, $k_{\text{cat}} = 1.00 \times 10^6\text{ s}^{-1}$ and $K_m = 1.20 \times 10^{-2}\text{ M}$ ($12.0\text{ mM}$). (a) Calculate the catalytic efficiency $k_{\text{cat}} / K_m$ in $\text{M}^{-1}\text{s}^{-1}$. (b) Compare this value to the physical Smoluchowski diffusion limit ($k_{\text{diff}} \approx 10^9\text{ M}^{-1}\text{s}^{-1}$) and comment on the enzyme's evolutionary perfection.",
                "solution": """**Step 1: Calculate catalytic efficiency**
$$\text{Efficiency} = \frac{k_{\text{cat}}}{K_m} = \frac{1.00 \times 10^6\text{ s}^{-1}}{1.20 \times 10^{-2}\text{ M}} = 8.333 \times 10^7\text{ M}^{-1}\text{s}^{-1} = 8.33 \times 10^7\text{ L}/(\text{mol}\cdot\text{s})$$

**Step 2: Comparison with diffusion limit**
$$\frac{k_{\text{cat}}/K_m}{k_{\text{diff}}} = \frac{8.33 \times 10^7}{1.00 \times 10^9} = 0.0833 \approx 8.3\%$$
Carbonic anhydrase operates within a single order of magnitude of the ultimate physical diffusion limit. Roughly 1 out of every 12 random diffusional collisions between $CO_2$ and the enzyme results in catalytic turnover, classifying it as a **kinetically perfect enzyme** where evolution has optimized active-site chemistry to the boundary set by Brownian diffusion."""
            },
            {
                "id": "p9-6",
                "title": "Logistic Inflection and Maximum Velocity in Autocatalytic Growth",
                "difficulty": "Medium",
                "statement": "An autocatalytic reaction $A + X \\\\xrightarrow{k} 2 X$ has rate constant $k = 0.0400\text{ M}^{-1}\text{s}^{-1}$. Initial concentrations are $[A]_0 = 0.500\text{ M}$ and $[X]_0 = 0.0100\text{ M}$. (a) Calculate the maximum reaction rate $r_{\max}$. (b) Calculate the concentration $[X]$ at which $r_{\max}$ occurs. (c) Calculate the time $t_{\max}$ required to reach this maximum rate.",
                "solution": """**Step 1: Rate expression as a function of $[X]$**
Total mass is conserved: $[A] + [X] = [A]_0 + [X]_0 = 0.500 + 0.0100 = 0.5100\text{ M} = C_{\text{tot}}$.
$$r = k [A][X] = k (C_{\text{tot}} - [X]) [X] = k (C_{\text{tot}} [X] - [X]^2)$$

**Step 2: Maximum rate condition**
Setting $\frac{dr}{d[X]} = k (C_{\text{tot}} - 2 [X]) = 0$:
$$[X]_{r_{\max}} = \frac{C_{\text{tot}}}{2} = \frac{0.5100\text{ M}}{2} = 0.2550\text{ M}$$
$$[A]_{r_{\max}} = C_{\text{tot}} - 0.2550 = 0.2550\text{ M}$$

Maximum rate:
$$r_{\max} = k [A][X] = 0.0400\text{ M}^{-1}\text{s}^{-1} \times (0.2550\text{ M})^2 = 0.0400 \times 0.065025 = 2.601 \times 10^{-3}\text{ M/s}$$

**Step 3: Calculate time $t_{\max}$ to reach maximum rate**
Integrated logistic equation:
$$\ln\left( \frac{[X]}{C_{\text{tot}} - [X]} \right) - \ln\left( \frac{[X]_0}{C_{\text{tot}} - [X]_0} \right) = k C_{\text{tot}} t$$
At $[X] = C_{\text{tot}} / 2$, $\frac{[X]}{C_{\text{tot}} - [X]} = 1 \implies \ln(1) = 0$.
$$0 - \ln\left( \frac{0.0100}{0.5000} \right) = k C_{\text{tot}} t_{\max}$$
$$\ln(50.00) = 3.9120$$
$$k C_{\text{tot}} = 0.0400 \times 0.5100 = 0.02040\text{ s}^{-1}$$
$$t_{\max} = \frac{3.9120}{0.02040\text{ s}^{-1}} = 191.76\text{ s} \approx 3.20\text{ minutes}$$"""
            },
            {
                "id": "p9-7",
                "title": "Limit Cycle Amplitude and Period in Lotka-Volterra Chemical Oscillator",
                "difficulty": "Hard",
                "statement": """The idealized Lotka-Volterra chemical oscillation scheme:
1. $A + X \\\\xrightarrow{k_1} 2 X$ (autocatalytic prey generation)
2. $X + Y \\\\xrightarrow{k_2} 2 Y$ (predator feeding on prey)
3. $Y \\\\xrightarrow{k_3} P$ (predator death)

operates in an open reactor with constant $[A] = 1.00\\text{ M}$. Kinetic constants are $k_1 = 2.00\\text{ M}^{-1}\\text{s}^{-1}$, $k_2 = 10.0\\text{ M}^{-1}\\text{s}^{-1}$, and $k_3 = 4.00\\text{ s}^{-1}$. (a) Calculate the steady-state equilibrium concentrations $[X]^*$ and $[Y]^*$. (b) Linearizing around the fixed point, calculate the angular frequency $\\omega_0$ and the natural period $T_{\\text{osc}}$ of the harmonic oscillations.""",
                "solution": """**Step 1: Find fixed point steady-state concentrations**
$$\frac{d[X]}{dt} = k_1 [A][X] - k_2 [X][Y] = [X] (k_1 [A] - k_2 [Y]) = 0$$
$$\frac{d[Y]}{dt} = k_2 [X][Y] - k_3 [Y] = [Y] (k_2 [X] - k_3) = 0$$

For non-trivial steady state ($[X]^*, [Y]^* > 0$):
$$k_2 [X]^* = k_3 \implies [X]^* = \frac{k_3}{k_2} = \frac{4.00\text{ s}^{-1}}{10.0\text{ M}^{-1}\text{s}^{-1}} = 0.400\text{ M}$$
$$k_2 [Y]^* = k_1 [A] \implies [Y]^* = \frac{k_1 [A]}{k_2} = \frac{2.00 \times 1.00}{10.0} = 0.200\text{ M}$$

**Step 2: Linearization and Jacobian matrix**
Let $x = [X] - [X]^*$ and $y = [Y] - [Y]^*$:
$$\mathcal{J} = \begin{pmatrix} \frac{\partial \dot{X}}{\partial X} & \frac{\partial \dot{X}}{\partial Y} \\ \frac{\partial \dot{Y}}{\partial X} & \frac{\partial \dot{Y}}{\partial Y} \end{pmatrix}_{\text{fixed}} = \begin{pmatrix} k_1 [A] - k_2 [Y]^* & -k_2 [X]^* \\ k_2 [Y]^* & k_2 [X]^* - k_3 \end{pmatrix} = \begin{pmatrix} 0 & -k_2 [X]^* \\ k_2 [Y]^* & 0 \end{pmatrix}$$

Substitute values:
$$\mathcal{J} = \begin{pmatrix} 0 & -10.0(0.400) \\ 10.0(0.200) & 0 \end{pmatrix} = \begin{pmatrix} 0 & -4.00 \\ 2.00 & 0 \end{pmatrix}$$

Eigenvalue equation:
$$\det(\mathcal{J} - \lambda I) = \lambda^2 - (0) \lambda + ( -4.00 \times -2.00 ) = \lambda^2 + 8.00 = 0$$
$$\lambda = \pm i \sqrt{8.00} = \pm i (2.8284)\text{ rad/s}$$

**Step 3: Angular frequency and oscillation period**
$$\omega_0 = \sqrt{8.00} = 2.8284\text{ rad/s}$$
$$T_{\text{osc}} = \frac{2 \pi}{\omega_0} = \frac{2 \pi}{2.8284} = 2.221\text{ s}$$
The concentrations of intermediates $X$ and $Y$ oscillate periodically around the fixed point with a period of **$2.22\text{ seconds}$**."""
            }
        ]
    }
    units.append(u9)

    # =========================================================================
    # UNIT 10: Molecular Reaction Dynamics, PES & Transition State Theory
    # =========================================================================
    u10 = {
        "id": "unit-10",
        "unitNumber": 10,
        "title": "Unit 10: Molecular Reaction Dynamics, Potential Energy Surfaces & Transition State Theory",
        "leadSummary": "Microscopic molecular dynamics of chemical transformations: hard-sphere collision theory, steric orientation factors, the Smoluchowski-Debye diffusion-controlled limits in solution, statistical thermodynamic partition function derivation of the Eyring-Polanyi Transition State Theory (TST), thermodynamic activation parameters, primary and secondary kinetic salt effects, crossed molecular beam reactive scattering, and London-Eyring-Polanyi-Sato (LEPS) potential energy surfaces.",
        "simulations": ["sim_kin_potential_energy_surface_trajectory"],
        "sections": [
            {
                "id": "sec-10-1",
                "secNumber": "10.1",
                "title": "Hard-Sphere Collision Theory of Gas Reactions & Steric Factor P",
                "content": """Simple collision theory (Trautz and Lewis, 1916-1918) provided the earliest microscopic physical model for bimolecular reaction rate constants.

### Fundamental Formulation
For an elementary bimolecular reaction $A + B \\longrightarrow P$:
$$r = Z_{AB} \\cdot f_{\\text{Boltzmann}} \\cdot P$$
where:
1. $Z_{AB}$ is the collision density between species $A$ and $B$:
   $$Z_{AB} = \\sigma_{AB} \\bar{v}_{\\text{rel}} \\mathcal{N}_A \\mathcal{N}_B = \\pi d_{AB}^2 \\sqrt{\\frac{8 k_B T}{\\pi \\mu}} \\mathcal{N}_A \\mathcal{N}_B$$
   where $d_{AB} = \\frac{d_A + d_B}{2}$ is the collision diameter, and $\\mu = \\frac{m_A m_B}{m_A + m_B}$ is the reduced mass.
2. $f_{\\text{Boltzmann}} = \\exp(-E_0 / R T)$ is the fraction of collisions possessing relative kinetic energy along the line of centers exceeding threshold $E_0$.
3. $P$ is the **steric factor** ($0 < P \\le 1$).

### The Bimolecular Rate Constant
Expressing in molar units ($k = r / [A][B]$):
$$k(T) = P \\cdot N_A \\pi d_{AB}^2 \\sqrt{\\frac{8 k_B T}{\\pi \\mu}} \\exp\\left( -\\frac{E_0}{R T} \\right)$$

Comparing with the Arrhenius equation $k = A \\exp(-E_a / R T)$:
$$A = P \\cdot N_A \\sigma_{AB} \\sqrt{\\frac{8 k_B T}{\\pi \\mu}} \\propto P T^{1/2}$$

### Physical Meaning of the Steric Factor $P$
For simple spherical atom-atom reactions (e.g., $K + Br_2$), $P \\approx 1\\text{--}4$ (the \"harpoon mechanism\" gives $P > 1$ due to long-range electron transfer).
For polyatomic molecules with complex geometry (e.g., cyclization of hexatriene), $P$ drops to $10^{-4}\\text{--}10^{-7}$, indicating that less than one in a million energetic collisions occurs with proper mutual orientation."""
            },
            {
                "id": "sec-10-2",
                "secNumber": "10.2",
                "title": "Diffusion-Controlled Reactions in Solution: Smoluchowski & Debye Limits",
                "content": """In liquid solution, molecules are enclosed within solvent \"cages\", undergoing dozens of rapid repeated collisions (an encounter) before diffusing apart.

### The Smoluchowski Equation (1917)
For an activationless reaction between neutral species where every encounter leads immediately to reaction ($E_a \\approx 0$), the rate is strictly limited by the rate at which reactants diffuse toward one another.
Solving Fick's second law for spherical diffusion to an absorbing sphere of radius $R_{AB} = r_A + r_B$:
$$k_{\\text{diff}} = 4 \\pi N_A (D_A + D_B) R_{AB}$$
where $D_A, D_B$ are diffusion coefficients.

Substituting the Stokes-Einstein relation $D_i = \\frac{k_B T}{6 \\pi \\eta r_i}$:
Assuming equal hydrodynamic radii $r_A = r_B = r$:
$$D_A + D_B = \\frac{2 k_B T}{6 \\pi \\eta r} = \\frac{k_B T}{3 \\pi \\eta r}$$
$$R_{AB} = 2 r$$
$$k_{\\text{diff}} = 4 \\pi N_A \\left( \\frac{k_B T}{3 \\pi \\eta r} \\right) (2 r) = \\frac{8 N_A k_B T}{3 \\eta} = \\frac{8 R T}{3 \\eta}$$

**Remarkable Feature**: The diffusion-controlled rate constant is **independent of solute size** and depends solely on temperature and solvent dynamic viscosity $\\eta$!
For water at $298.15\\text{ K}$ ($\\eta = 0.890\\text{ cP}$):
$$k_{\\text{diff}} = \\frac{8 \\times 8.314 \\times 298.15}{3 \\times (0.890 \\times 10^{-3})} \\approx 7.4 \\times 10^9\\text{ M}^{-1}\\text{s}^{-1}$$

### The Debye Modification for Ionic Encounters (1942)
For charged ions ($z_A e$ and $z_B e$), Coulombic attraction or repulsion alters encounter flux:
$$k_{\\text{diff, ions}} = k_{\\text{diff}} \\cdot \\left[ \\frac{\\Phi}{e^\\Phi - 1} \\right], \\quad \\text{where } \\Phi = \\frac{z_A z_B e^2}{4 \\pi \\varepsilon_r \\varepsilon_0 R_{AB} k_B T}$$
Oppositely charged ions ($z_A z_B < 0$) accelerate diffusion ($k > k_{\\text{diff}}$), while like-charged ions repel ($k < k_{\\text{diff}}$)."""
            },
            {
                "id": "sec-10-3",
                "secNumber": "10.3",
                "title": "Transition State Theory (TST): Eyring Equation via Statistical Partition Functions",
                "content": """Henry Eyring, Michael Polanyi, and Eugene Wigner (1935) established Transition State Theory (also known as Activated Complex Theory), which calculates absolute reaction rates from first-principles statistical mechanics without empirical parameters.

### Postulates of Classical TST
1. Reactants are in quasi-thermal equilibrium with the activated complex:
   $$A + B \\rightleftharpoons [AB]^\\ddagger \\\\xrightarrow{k^\\ddagger} P$$
2. The activated complex $[AB]^\\ddagger$ is treated as an ordinary molecule, except that one vibrational mode along the reaction coordinate has transformed into a loose translational motion across the saddle point.
3. Every activated complex crossing the barrier in the forward direction proceeds irreversibly to product (transmission coefficient $\\kappa_{\\text{trans}} \\approx 1$).

### Partition Function Derivation
The pseudo-equilibrium constant is:
$$K^\\ddagger = \\frac{[AB]^\\ddagger}{[A][B]} = \\frac{q^\\ddagger}{q_A q_B} \\exp\\left( -\\frac{\\Delta E_0^\\ddagger}{k_B T} \\right)$$
where $q$ are molecular partition functions per unit volume.

Factoring out the critical reaction-coordinate vibration:
$$q^\\ddagger = q_{\\text{rc}} \\cdot q_{\\text{int}}^\\ddagger$$
In the classical limit ($h \\nu \\ll k_B T$):
$$q_{\\text{rc}} = \\frac{k_B T}{h \\nu^\\ddagger}$$

The rate of barrier crossing is the vibrational frequency $\\nu^\\ddagger$:
$$k^\\ddagger = \\nu^\\ddagger$$

The reaction rate is:
$$r = k^\\ddagger [AB]^\\ddagger = \\nu^\\ddagger \\left( \\frac{k_B T}{h \\nu^\\ddagger} \\right) \\frac{q_{\\text{int}}^\\ddagger}{q_A q_B} \\exp\\left( -\\frac{\\Delta E_0^\\ddagger}{k_B T} \\right) [A][B]$$

The unknown imaginary frequency $\\nu^\\ddagger$ cancels identically, yielding the foundational **Eyring Equation**:
$$k(T) = \\kappa_{\\text{trans}} \\frac{k_B T}{h} \\frac{q^\\ddagger}{q_A q_B} \\exp\\left( -\\frac{\\Delta E_0^\\ddagger}{k_B T} \\right)$$
The universal prefactor $\\frac{k_B T}{h} \\approx 6.21 \\times 10^{12}\\text{ s}^{-1}$ at $298.15\\text{ K}$ represents the fundamental attempt frequency of chemical transformation."""
            },
            {
                "id": "sec-10-4",
                "secNumber": "10.4",
                "title": "Thermodynamic Formulation of TST: Activation Enthalpy, Entropy & Free Energy",
                "content": """Eyring recast Transition State Theory into macroscopic thermodynamic language by expressing the quasi-equilibrium constant in terms of standard activation free energy:
$$K^\\ddagger = \\exp\\left( -\\frac{\\Delta G^{\\ddagger\\circ}}{R T} \\right) = \\exp\\left( \\frac{\\Delta S^{\\ddagger\\circ}}{R} \\right) \\exp\\left( -\\frac{\\Delta H^{\\ddagger\\circ}}{R T} \\right)$$

### The Thermodynamic Eyring Equation
$$k(T) = \\frac{k_B T}{h} (c^\\circ)^{1 - m} \\exp\\left( \\frac{\\Delta S^{\\ddagger\\circ}}{R} \\right) \\exp\\left( -\\frac{\\Delta H^{\\ddagger\\circ}}{R T} \\right)$$
where $m$ is molecularity and $c^\\circ = 1\\text{ M}$ is standard state concentration.

### Relation Between Arrhenius and Eyring Parameters
From the Arrhenius definition $E_a \\equiv R T^2 \\frac{d \\ln k}{dT}$:
$$\\ln k = \\ln\\left( \\frac{k_B}{h} \\right) + \\ln T - \\frac{\\Delta H^{\\ddagger\\circ}}{R T} + \\frac{\\Delta S^{\\ddagger\\circ}}{R}$$
$$\\frac{d \\ln k}{dT} = \\frac{1}{T} + \\frac{\\Delta H^{\\ddagger\\circ}}{R T^2}$$
$$E_a = R T^2 \\left( \\frac{1}{T} + \\frac{\\Delta H^{\\ddagger\\circ}}{R T^2} \\right) = \\Delta H^{\\ddagger\\circ} + R T \\quad (\\text{liquid-phase reactions})$$

For ideal gas reactions of molecularity $m$:
$$E_a = \\Delta H^{\\ddagger\\circ} + m R T$$
- For unimolecular gas reactions ($m = 1$): $E_a = \\Delta H^{\\ddagger\\circ} + R T$.
- For bimolecular gas reactions ($m = 2$): $E_a = \\Delta H^{\\ddagger\\circ} + 2 R T$.

### Physical Meaning of Activation Entropy ($\\Delta S^{\\ddagger\\circ}$)
- $\\Delta S^{\\ddagger\\circ} < 0$ (associative transition state): Two independent molecules combine to form a rigid, highly ordered transition state, losing translational and rotational degrees of freedom (typical bimolecular additions).
- $\\Delta S^{\\ddagger\\circ} > 0$ (dissociative transition state): A molecule loosens bonds, releasing fragments or solvent molecules, increasing disorder."""
            },
            {
                "id": "sec-10-5",
                "secNumber": "10.5",
                "title": "Kinetic Salt Effects in Solution: The Brønsted-Bjerrum Equation",
                "content": """The rate of ionic reactions in solution depends strongly on the ionic strength $I$ of the medium.

### Brønsted-Bjerrum Formulation (1922-1924)
Consider an elementary reaction between ions $A^{z_A}$ and $B^{z_B}$ forming an activated complex $[AB]^{\\ddagger (z_A + z_B)}$:
$$A^{z_A} + B^{z_B} \\rightleftharpoons [AB]^\\ddagger \\\\xrightarrow{k_0} P$$

Thermodynamic equilibrium requires activities:
$$K^\\ddagger = \\frac{a_\\ddagger}{a_A a_B} = \\frac{[AB]^\\ddagger \\gamma_\\ddagger}{[A]\\gamma_A [B]\\gamma_B} \\implies [AB]^\\ddagger = K^\\ddagger [A][B] \\left( \\frac{\\gamma_A \\gamma_B}{\\gamma_\\ddagger} \\right)$$

The observed rate is:
$$r = k_0 [AB]^\\ddagger = k_0 K^\\ddagger [A][B] \\left( \\frac{\\gamma_A \\gamma_B}{\\gamma_\\ddagger} \\right) = k [A][B]$$
Thus, the rate constant $k$ is:
$$k = k_0 \\left( \\frac{\\gamma_A \\gamma_B}{\\gamma_\\ddagger} \\right) \\iff \\log_{10} k = \\log_{10} k_0 + \\log_{10} \\gamma_A + \\log_{10} \\gamma_B - \\log_{10} \\gamma_\\ddagger$$
where $k_0$ is the rate constant at infinite dilution ($I \\to 0$).

### Incorporation of Debye-Hückel Limiting Law
At low ionic strength ($I < 0.05\\text{ M}$), the activity coefficient is given by $\\log_{10} \\gamma_i = -A z_i^2 \\sqrt{I}$:
$$\\log_{10}\\left( \\frac{\\gamma_A \\gamma_B}{\\gamma_\\ddagger} \\right) = -A \\left[ z_A^2 + z_B^2 - (z_A + z_B)^2 \\right] \\sqrt{I} = -A [ -2 z_A z_B ] \\sqrt{I} = 2 A z_A z_B \\sqrt{I}$$

For water at $298.15\\text{ K}$, $A = 0.509\\;(\\text{mol/kg})^{-1/2}$:
$$\\log_{10}\\left( \\frac{k}{k_0} \\right) = 2 (0.509) z_A z_B \\sqrt{I} = 1.018 \\, z_A z_B \\sqrt{I}$$

### Diagnostic Regimes of Primary Salt Effect
1. **Like Charges ($z_A z_B > 0$)**: Slope $> 0$. Adding inert electrolyte shields repulsion, stabilizing the $[AB]^\\ddagger$ complex and accelerating the reaction.
2. **Opposite Charges ($z_A z_B < 0$)**: Slope $< 0$. Adding inert electrolyte stabilizes separated reactants more than the complex, decelerating the reaction.
3. **Neutral Reactant ($z_A z_B = 0$)**: Slope $= 0$. Rate is virtually independent of ionic strength."""
            },
            {
                "id": "sec-10-6",
                "secNumber": "10.6",
                "title": "Molecular Reaction Dynamics: Crossed Beams & State-to-State Scattering",
                "content": """While classical kinetics measures macroscopic ensemble thermal averages $k(T)$, molecular reaction dynamics probes single-collision events with defined quantum states, velocity vectors, and scattering angles.

### Crossed Molecular Beam Experiments (Herschbach and Lee, Nobel Prize 1986)
Two collimated supersonic molecular beams collide at right angles in an ultra-high vacuum chamber ($P < 10^{-10}\\text{ Torr}$):
1. **Velocity Selection**: Choppers select initial relative kinetic energy $E_{\\text{coll}}$.
2. **Rotatable Mass Spectrometer**: Measures angular distribution $d\\sigma / d\\Omega$ and time-of-flight velocity distributions of scattered reaction products.

### Dynamics Classification: Rebound vs. Stripping
1. **Rebound Mechanism ($K + CH_3I \\longrightarrow KI + CH_3$)**:
   - Small impact parameter ($b < d$).
   - Direct backward scattering ($\\theta \\approx 180^\\circ$).
   - Low product vibrational excitation; high translational energy release.
2. **Stripping Mechanism ($K + Br_2 \\longrightarrow KBr + Br$)**:
   - Large impact parameter ($b > d$).
   - Forward scattering ($\\theta \\approx 0^\\circ$).
   - **Harpoon Model**: At long distance ($R_c \\approx 4\\text{--}6\\text{ Å}$), an electron jumps from potassium to bromine ($K + Br_2 \\to K^+ + Br_2^-$), followed by strong Coulombic attraction that strips the halogen atom into high vibrational excitation."""
            },
            {
                "id": "sec-10-7",
                "secNumber": "10.7",
                "title": "Potential Energy Surfaces (PES): LEPS Formulation & Saddle Points",
                "content": """The Potential Energy Surface (PES) is the hyper-dimensional function $V(\\vec{R})$ expressing the electronic energy of a reacting system as a function of nuclear geometry under the Born-Oppenheimer approximation.

### Collinear Triatomic Reactions ($A + B-C \\longrightarrow A-B + C$)
For a collinear arrangement, the potential energy depends on only two internuclear distances: $R_{AB}$ and $R_{BC}$.

### The London-Eyring-Polanyi-Sato (LEPS) Surface
Constructed from semi-empirical valence bond theory by summing Coulombic ($Q$) and exchange ($J$) integrals:
$$V(R_{AB}, R_{BC}, R_{AC}) = Q_1 + Q_2 + Q_3 - \\sqrt{\\frac{1}{2} \\left[ (J_1 - J_2)^2 + (J_2 - J_3)^2 + (J_3 - J_1)^2 \\right]}$$
calibrated using experimental diatomic Morse potentials.

### Topography of the PES
1. **Reactant Valley**: Large $R_{AB}$, equilibrium $R_{BC}$.
2. **Product Valley**: Equilibrium $R_{AB}$, large $R_{BC}$.
3. **Transition State (Saddle Point $\\ddagger$)**: A first-order saddle point where the gradient vanishes ($\\nabla V = 0$), corresponding to a maximum along the reaction coordinate and a minimum along all perpendicular vibrational coordinates.

### Polanyi's Rules for Barrier Location
John Polanyi (Nobel Prize 1986) related barrier location to energy partitioning:
1. **Early Barrier (Attractive Surface, reactant valley)**:
   Translational energy $E_{\\text{trans}}$ is highly effective in promoting reaction; product energy appears primarily as vibration ($E_{\\text{vib}}'$). Exothermic reactions generally possess early barriers.
2. **Late Barrier (Repulsive Surface, product valley)**:
   Vibrational energy $E_{\\text{vib}}$ in the reactant bond is far more effective than translational energy in crossing the barrier. Endothermic reactions generally possess late barriers."""
            }
        ],
        "problems": [
            {
                "id": "p10-1",
                "title": "Bimolecular Collision Theory Pre-Exponential Factor for Gas Reactions",
                "difficulty": "Easy",
                "statement": "For the gas-phase reaction $H + O_2 \\longrightarrow OH + O$ at $T = 1000.0\\text{ K}$, atomic and molecular diameters are $d_H = 0.100\\text{ nm}$ and $d_{O_2} = 0.360\\text{ nm}$. Molar masses are $M_H = 1.008\\text{ g/mol}$ and $M_{O_2} = 31.999\\text{ g/mol}$. Assuming a steric factor of $P = 0.400$: (a) calculate the collision cross-section $\\sigma_{AB}$, (b) calculate the reduced mass $\\mu$, and (c) calculate the theoretical collision-theory pre-exponential factor $A$ in $\\text{M}^{-1}\\text{s}^{-1}$.",
                "solution": """**Step 1: Calculate collision cross-section $\\sigma_{AB}$**
$$d_{AB} = \\frac{d_H + d_{O_2}}{2} = \\frac{0.100 + 0.360}{2} = 0.230\\text{ nm} = 2.30 \\times 10^{-10}\\text{ m}$$
$$\\sigma_{AB} = \\pi d_{AB}^2 = \\pi (2.30 \\times 10^{-10}\\text{ m})^2 = 1.6619 \\times 10^{-19}\\text{ m}^2$$

**Step 2: Calculate reduced mass $\\mu$**
$$\\mu = \\frac{m_H m_{O_2}}{m_H + m_{O_2}} = \\frac{1.008 \\times 31.999}{(1.008 + 31.999) \\times (6.02214 \\times 10^{26}\\text{ kg/mol})} = \\frac{32.255}{33.007 \\times 6.02214 \\times 10^{26}} = 1.6225 \\times 10^{-27}\\text{ kg}$$

**Step 3: Average relative speed $\\bar{v}_{\\text{rel}}$**
$$\\bar{v}_{\\text{rel}} = \\sqrt{\\frac{8 k_B T}{\\pi \\mu}} = \\sqrt{\\frac{8 \\times (1.380649 \\times 10^{-23}) \\times 1000.0}{\\pi \\times (1.6225 \\times 10^{-27})}} = \\sqrt{\\frac{1.10452 \\times 10^{-19}}{5.0973 \\times 10^{-27}}} = \\sqrt{2.16687 \\times 10^7} = 4654.96\\text{ m/s}$$

**Step 4: Compute pre-exponential factor $A$**
$$A = P \\cdot N_A \\sigma_{AB} \\bar{v}_{\\text{rel}}$$
$$A = 0.400 \\times (6.02214 \\times 10^{23}\\text{ mol}^{-1}) \\times (1.6619 \\times 10^{-19}\\text{ m}^2) \\times (4654.96\\text{ m/s})$$
$$A = 0.400 \\times 1.00082 \\times 10^5 \\times 4654.96 = 1.8635 \\times 10^8\\text{ m}^3/(\\text{mol}\\cdot\\text{s})$$

Converting to $\\text{M}^{-1}\\text{s}^{-1}$ ($1\\text{ m}^3 = 1000\\text{ L}$):
$$A = (1.8635 \\times 10^8) \\times 1000 = 1.86 \\times 10^{11}\\text{ M}^{-1}\\text{s}^{-1}$$"""
            },
            {
                "id": "p10-2",
                "title": "Thermodynamic Activation Parameters ($\\Delta H^\\ddagger, \\Delta S^\\ddagger, \\Delta G^\\ddagger$) from Eyring Plot",
                "difficulty": "Medium",
                "statement": "A second-order liquid-phase nucleophilic substitution reaction has measured rate constants of $k_1 = 3.20 \\times 10^{-4}\\text{ M}^{-1}\\text{s}^{-1}$ at $T_1 = 298.15\\text{ K}$ and $k_2 = 2.85 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$ at $T_2 = 318.15\\text{ K}$. Calculate: (a) the activation enthalpy $\\Delta H^{\\ddagger\\circ}$ in $\\text{kJ/mol}$, (b) the activation entropy $\\Delta S^{\\ddagger\\circ}$ in $\\text{J}/(\\text{mol}\\cdot\\text{K})$, and (c) the Gibbs activation free energy $\\Delta G^{\\ddagger\\circ}$ at $298.15\\text{ K}$.",
                "solution": """**Step 1: Eyring two-point equation**
$$\\ln\\left( \\frac{k_2 / T_2}{k_1 / T_1} \\right) = -\\frac{\\Delta H^{\\ddagger\\circ}}{R} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right) = \\frac{\\Delta H^{\\ddagger\\circ}}{R} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right)$$

Evaluate ratios:
$$\\frac{k_2 / T_2}{k_1 / T_1} = \\frac{2.85 \\times 10^{-3} / 318.15}{3.20 \\times 10^{-4} / 298.15} = \\frac{8.95804 \\times 10^{-6}}{1.07329 \\times 10^{-6}} = 8.3463$$
$$\\ln(8.3463) = 2.1218$$

$$\\frac{T_2 - T_1}{T_1 T_2} = \\frac{20.0}{298.15 \\times 318.15} = \\frac{20.0}{9.4856 \\times 10^4} = 2.10846 \\times 10^{-4}\\text{ K}^{-1}$$

$$\\Delta H^{\\ddagger\\circ} = \\frac{R \\ln(8.3463)}{2.10846 \\times 10^{-4}} = \\frac{8.314462 \\times 2.1218}{2.10846 \\times 10^{-4}} = \\frac{17.6416}{2.10846 \\times 10^{-4}} = 8.3670 \\times 10^4\\text{ J/mol} = 83.67\\text{ kJ/mol}$$

**Step 2: Activation entropy $\\Delta S^{\\ddagger\\circ}$**
Using data at $T_1 = 298.15\\text{ K}$:
$$k = \\frac{k_B T}{h} \\exp\\left( \\frac{\\Delta S^{\\ddagger\\circ}}{R} \\right) \\exp\\left( -\\frac{\\Delta H^{\\ddagger\\circ}}{R T} \\right)$$
$$\\frac{k_B T_1}{h} = \\frac{(1.380649 \\times 10^{-23}) \\times (298.15)}{6.62607 \\times 10^{-34}} = 6.2124 \\times 10^{12}\\text{ s}^{-1}$$

$$\\frac{k_1}{k_B T_1 / h} = \\frac{3.20 \\times 10^{-4}}{6.2124 \\times 10^{12}} = 5.1510 \\times 10^{-17}$$
$$\\ln(5.1510 \\times 10^{-17}) = -37.505$$

$$\\frac{\\Delta S^{\\ddagger\\circ}}{R} - \\frac{\\Delta H^{\\ddagger\\circ}}{R T_1} = -37.505$$
$$\\frac{\\Delta H^{\\ddagger\\circ}}{R T_1} = \\frac{83670}{8.314462 \\times 298.15} = \\frac{83670}{2478.96} = 33.752$$
$$\\frac{\\Delta S^{\\ddagger\\circ}}{R} = -37.505 + 33.752 = -3.753$$
$$\\Delta S^{\\ddagger\\circ} = -3.753 \\times 8.314462 = -31.20\\text{ J}/(\\text{mol}\\cdot\\text{K})$$

The negative activation entropy signifies an associative bimolecular transition state.

**Step 3: Activation free energy $\\Delta G^{\\ddagger\\circ}$ at $298.15\\text{ K}$**
$$\\Delta G^{\\ddagger\\circ} = \\Delta H^{\\ddagger\\circ} - T_1 \\Delta S^{\\ddagger\\circ} = 83.67\\text{ kJ/mol} - (298.15\\text{ K}) \\times (-0.03120\\text{ kJ}/(\\text{mol}\\cdot\\text{K})) = 83.67 + 9.30 = 92.97\\text{ kJ/mol}$$"""
            },
            {
                "id": "p10-3",
                "title": "Primary Kinetic Salt Effect on Persulfate-Iodide Redox Reaction",
                "difficulty": "Medium",
                "statement": "The reaction between persulfate ion and iodide ion ($S_2O_8^{2-} + 2 I^- \\longrightarrow 2 SO_4^{2-} + I_2$) involves an initial rate-determining step between $S_2O_8^{2-}$ ($z_A = -2$) and $I^-$ ($z_B = -1$). At $T = 25.0^\\circ\\text{C}$ in water, the rate constant at infinite dilution is $k_0 = 1.05 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$. Using the Brønsted-Bjerrum equation $\\log_{10}(k / k_0) = 1.018 \\, z_A z_B \\sqrt{I}$: (a) calculate the rate constant $k$ in an electrolyte solution of ionic strength $I = 0.0100\\text{ M}$, and (b) at $I = 0.0400\\text{ M}$.",
                "solution": """**Step 1: Calculate charge product**
$$z_A = -2, \\quad z_B = -1 \\implies z_A z_B = (-2) \\times (-1) = +2$$
Because both reactants carry negative charges, the charge product is positive ($+2$), predicting a positive salt effect.

**Step 2: Rate constant at $I = 0.0100\\text{ M}$**
$$\\sqrt{I} = \\sqrt{0.0100} = 0.100\\text{ M}^{1/2}$$
$$\\log_{10}\\left( \\frac{k}{k_0} \\right) = 1.018 \\times (+2) \\times 0.100 = 0.2036$$
$$\\frac{k}{k_0} = 10^{0.2036} = 1.598$$
$$k = 1.598 \\times (1.05 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}) = 1.68 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$$

**Step 3: Rate constant at $I = 0.0400\\text{ M}$**
$$\\sqrt{I} = \\sqrt{0.0400} = 0.200\\text{ M}^{1/2}$$
$$\\log_{10}\\left( \\frac{k}{k_0} \\right) = 1.018 \\times (+2) \\times 0.200 = 0.4072$$
$$\\frac{k}{k_0} = 10^{0.4072} = 2.554$$
$$k = 2.554 \\times (1.05 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}) = 2.68 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$$
Adding inert salt increases ionic strength from $0$ to $0.04\\text{ M}$, accelerating the reaction rate by **$155\\%$**."""
            },
            {
                "id": "p10-4",
                "title": "Debye Diffusion-Controlled Limit for Oppositely Charged Ions",
                "difficulty": "Hard",
                "statement": "The neutralization reaction between hydronium and hydroxide ions ($H_3O^+ + OH^- \\longrightarrow 2 H_2O$) is diffusion-controlled in water at $T = 298.15\\text{ K}$ ($\\varepsilon_r = 78.36$). The encounter distance is $R_{AB} = 0.450\\text{ nm}$, and diffusion coefficients are $D(H_3O^+) = 9.31 \\times 10^{-9}\\text{ m}^2/\\text{s}$ and $D(OH^-) = 5.30 \\times 10^{-9}\\text{ m}^2/\\text{s}$. (a) Calculate the neutral Smoluchowski rate constant $k_{\\text{diff}}$. (b) Calculate the Debye Coulombic electrostatic factor $f_{\\text{Debye}} = \\frac{\\Phi}{e^\\Phi - 1}$ where $\\Phi = \\frac{z_A z_B e^2}{4 \\pi \\varepsilon_r \\varepsilon_0 R_{AB} k_B T}$. (c) Calculate the true ionic diffusion-controlled rate constant $k_{\\text{diff, ions}}$.",
                "solution": """**Step 1: Calculate neutral Smoluchowski rate constant**
$$D_A + D_B = (9.31 + 5.30) \\times 10^{-9} = 1.461 \\times 10^{-8}\\text{ m}^2/\\text{s}$$
$$R_{AB} = 4.50 \\times 10^{-10}\\text{ m}$$
$$k_{\\text{diff}} = 4 \\pi N_A (D_A + D_B) R_{AB}$$
$$k_{\\text{diff}} = 4 \\pi \\times (6.02214 \\times 10^{23}\\text{ mol}^{-1}) \\times (1.461 \\times 10^{-8}\\text{ m}^2/\\text{s}) \\times (4.50 \\times 10^{-10}\\text{ m})$$
$$k_{\\text{diff}} = 4.9669 \\times 10^7\\text{ m}^3/(\\text{mol}\\cdot\\text{s}) = 4.97 \\times 10^{10}\\text{ M}^{-1}\\text{s}^{-1}$$

**Step 2: Calculate Debye factor $\\Phi$**
$$z_A = +1, \\quad z_B = -1 \\implies z_A z_B = -1$$
$$e^2 = (1.6021766 \\times 10^{-19})^2 = 2.56697 \\times 10^{-38}\\text{ C}^2$$
$$4 \\pi \\varepsilon_r \\varepsilon_0 = 4 \\pi \\times 78.36 \\times (8.85419 \\times 10^{-12}) = 8.7188 \\times 10^{-10}\\text{ F/m}$$
$$k_B T = (1.380649 \\times 10^{-23}) \\times (298.15) = 4.1164 \\times 10^{-21}\\text{ J}$$

Denominator:
$$\\text{Denom} = (8.7188 \\times 10^{-10}) \\times (4.50 \\times 10^{-10}) \\times (4.1164 \\times 10^{-21}) = 1.6151 \\times 10^{-39}$$
$$\\Phi = \\frac{-2.56697 \\times 10^{-38}}{1.6151 \\times 10^{-39}} = -1.5893$$

Debye enhancement factor:
$$e^\\Phi = e^{-1.5893} = 0.20407$$
$$f_{\\text{Debye}} = \\frac{\\Phi}{e^\\Phi - 1} = \\frac{-1.5893}{0.20407 - 1} = \\frac{-1.5893}{-0.79593} = 1.9968 \\approx 2.00$$

**Step 3: Calculate true ionic rate constant**
$$k_{\\text{diff, ions}} = k_{\\text{diff}} \\cdot f_{\\text{Debye}} = (4.9669 \\times 10^{10}\\text{ M}^{-1}\\text{s}^{-1}) \\times 1.9968 = 9.92 \\times 10^{10}\\text{ M}^{-1}\\text{s}^{-1} \\approx 1.0 \\times 10^{11}\\text{ M}^{-1}\\text{s}^{-1}$$
Electrostatic Coulombic attraction doubles the rate of diffusional encounter, matching the experimental neutralization rate ($1.3 \\times 10^{11}\\text{ M}^{-1}\\text{s}^{-1}$)."""
            },
            {
                "id": "p10-5",
                "title": "Harpoon Mechanism Electron Jump Radius and Cross-Section",
                "difficulty": "Medium",
                "statement": """In the crossed molecular beam reaction $K + Br_2 \\longrightarrow KBr + Br$, electron transfer occurs via the harpoon mechanism when the covalent and ionic potential energy curves cross at radius $R_c$:
$$I_P(K) - E_A(Br_2) = \\frac{e^2}{4 \\pi \\varepsilon_0 R_c}$$
Given the ionization potential of potassium $I_P(K) = 4.34\\text{ eV}$ and the electron affinity of bromine $E_A(Br_2) = 2.50\\text{ eV}$: (a) calculate the electron jump radius $R_c$ in Ångströms, and (b) calculate the reaction cross-section $\\sigma = \\pi R_c^2$ and compare it with the hard-sphere gas kinetic cross-section ($\\sigma_{\\text{hs}} \\approx 35\\text{ Å}^2$).""",
                "solution": """**Step 1: Calculate energy difference**
$$\\Delta E = I_P(K) - E_A(Br_2) = 4.34\\text{ eV} - 2.50\\text{ eV} = 1.84\\text{ eV}$$
Convert to Joules:
$$\\Delta E = 1.84 \\times (1.6021766 \\times 10^{-19}\\text{ J}) = 2.9480 \\times 10^{-19}\\text{ J}$$

**Step 2: Solve for crossing radius $R_c$**
$$R_c = \\frac{e^2}{4 \\pi \\varepsilon_0 \\Delta E} = \\frac{(8.98755 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2) \\times (1.6021766 \\times 10^{-19}\\text{ C})^2}{2.9480 \\times 10^{-19}\\text{ J}}$$
$$e^2 / (4 \\pi \\varepsilon_0) = 2.30708 \\times 10^{-28}\\text{ J}\\cdot\\text{m}$$
$$R_c = \\frac{2.30708 \\times 10^{-28}\\text{ J}\\cdot\\text{m}}{2.9480 \\times 10^{-19}\\text{ J}} = 7.8259 \\times 10^{-10}\\text{ m} = 7.83\\text{ Å}$$

**Step 3: Calculate reaction cross-section $\\sigma$**
$$\\sigma = \\pi R_c^2 = \\pi (7.8259\\text{ Å})^2 = 192.4\\text{ Å}^2$$

Ratio to hard-sphere cross-section:
$$\\frac{\\sigma}{\\sigma_{\\text{hs}}} = \\frac{192.4\\text{ Å}^2}{35.0\\text{ Å}^2} = 5.50$$
The harpoon electron jump occurs at a distance of almost **$8\\text{ Å}$**, yielding a reaction cross-section over **5.5 times larger** than the physical hard-sphere collision size."""
            },
            {
                "id": "p10-6",
                "title": "Universal Eyring Attempt Frequency Calculation",
                "difficulty": "Easy",
                "statement": "The fundamental prefactor in Transition State Theory is the universal attempt frequency $\\nu_0 = \\frac{k_B T}{h}$. Calculate $\\nu_0$ and the corresponding period $\\tau_0 = 1/\\nu_0$ at: (a) cryogenic temperature $T = 77.0\\text{ K}$ (liquid nitrogen), (b) room temperature $T = 298.15\\text{ K}$, and (c) flame temperature $T = 2000.0\\text{ K}$.",
                "solution": """**Step 1: Formula for attempt frequency**
$$\\nu_0 = \\frac{k_B T}{h} = \\frac{1.380649 \\times 10^{-23}\\text{ J/K}}{6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}} \\times T = (2.08366 \\times 10^{10}\\text{ s}^{-1}\\text{K}^{-1}) \\times T$$

**Step 2: At $T = 77.0\\text{ K}$**
$$\\nu_0(77\\text{ K}) = (2.08366 \\times 10^{10}) \\times 77.0 = 1.6044 \\times 10^{12}\\text{ s}^{-1} = 1.60\\text{ THz}$$
$$\\tau_0(77\\text{ K}) = \\frac{1}{1.6044 \\times 10^{12}\\text{ s}^{-1}} = 6.233 \\times 10^{-13}\\text{ s} = 623.3\\text{ fs}$$

**Step 3: At $T = 298.15\\text{ K}$**
$$\\nu_0(298.15\\text{ K}) = (2.08366 \\times 10^{10}) \\times 298.15 = 6.2124 \\times 10^{12}\\text{ s}^{-1} = 6.21\\text{ THz}$$
$$\\tau_0(298.15\\text{ K}) = \\frac{1}{6.2124 \\times 10^{12}\\text{ s}^{-1}} = 1.610 \\times 10^{-13}\\text{ s} = 161.0\\text{ fs}$$

**Step 4: At $T = 2000.0\\text{ K}$**
$$\\nu_0(2000\\text{ K}) = (2.08366 \\times 10^{10}) \\times 2000.0 = 4.1673 \\times 10^{13}\\text{ s}^{-1} = 41.67\\text{ THz}$$
$$\\tau_0(2000\\text{ K}) = \\frac{1}{4.1673 \\times 10^{13}\\text{ s}^{-1}} = 2.400 \\times 10^{-14}\\text{ s} = 24.0\\text{ fs}$$
Across all temperatures, the transit time across the transition state barrier is on the **femtosecond ($10^{-14}\\text{--}10^{-13}\\text{ s}$)** timescale."""
            },
            {
                "id": "p10-7",
                "title": "Polanyi Parameter Classification of Early vs. Late Barrier Dynamics",
                "difficulty": "Hard",
                "statement": """For the collinear atom-diatom reaction $A + BC \\longrightarrow AB + C$, the barrier location parameter is defined as $\\mathcal{L} = \\frac{R_{AB}^\\ddagger - R_{AB, e}}{R_{BC}^\\ddagger - R_{BC, e}}$. Consider two reactions:
1. Reaction 1 ($F + H_2 \\longrightarrow HF + H$): $\\Delta H_r^\\circ = -134\\text{ kJ/mol}$, $R_{FH}^\\ddagger = 1.54\\text{ Å}$ ($R_{FH, e} = 0.92\\text{ Å}$), $R_{HH}^\\ddagger = 0.76\\text{ Å}$ ($R_{HH, e} = 0.74\\text{ Å}$).
2. Reaction 2 ($H + HF \\longrightarrow H_2 + F$): $\\Delta H_r^\\circ = +134\\text{ kJ/mol}$, $R_{HH}^\\ddagger = 0.76\\text{ Å}$ ($R_{HH, e} = 0.74\\text{ Å}$), $R_{FH}^\\ddagger = 1.54\\text{ Å}$ ($R_{FH, e} = 0.92\\text{ Å}$).

(a) Classify each reaction as having an early or late barrier according to the Hammond-Polanyi postulate. (b) For each reaction, state whether translational kinetic energy or vibrational reactant excitation is more effective at driving the reaction across the barrier.""",
                "solution": """**Step 1: Analyze Reaction 1 ($F + H_2 \\longrightarrow HF + H$)**
- $\\Delta H_r^\\circ = -134\\text{ kJ/mol}$ (strongly exothermic).
- At the transition state:
  $$\\Delta R_{HH} = R_{HH}^\\ddagger - R_{HH, e} = 0.76 - 0.74 = 0.02\\text{ Å} \\quad (\\text{bond barely stretched by } 2.7\\%)$$
  $$\\Delta R_{FH} = R_{FH}^\\ddagger - R_{FH, e} = 1.54 - 0.92 = 0.62\\text{ Å} \\quad (\\text{forming bond is still very distant})$$

Because the reactant $H-H$ bond is virtually unstretched at the saddle point, the transition state resembles the reactants:
This is an **Early Barrier (Attractive PES)**, located in the entrance valley.
- **Dynamic consequence**: According to Polanyi's rules, **relative translational kinetic energy** ($E_{\\text{trans}}$) is far more effective than reactant vibrational energy in crossing an early barrier. Excess energy in products appears as **vibrational excitation** of $HF$ (the basis of the $HF$ chemical laser).

**Step 2: Analyze Reaction 2 ($H + HF \\longrightarrow H_2 + F$)**
- $\\Delta H_r^\\circ = +134\\text{ kJ/mol}$ (strongly endothermic, the microscopic reverse of Reaction 1).
- At the transition state:
  $$\\Delta R_{FH} = R_{FH}^\\ddagger - R_{FH, e} = 1.54 - 0.92 = 0.62\\text{ Å} \\quad (\\text{reactant bond is stretched by } 67\\%!)$$
  $$\\Delta R_{HH} = R_{HH}^\\ddagger - R_{HH, e} = 0.76 - 0.74 = 0.02\\text{ Å} \\quad (\\text{product bond is almost formed})$$

Because the reactant $F-H$ bond must be stretched extensively to reach the saddle point, the transition state resembles the products:
This is a **Late Barrier (Repulsive PES)**, located in the exit valley.
- **Dynamic consequence**: According to Polanyi's rules, **vibrational excitation of the reactant $HF$ bond** ($v \\ge 1$) is overwhelmingly more effective than translational energy in promoting reaction across a late barrier."""
            }
        ]
    }
    units.append(u10)

    return units

if __name__ == "__main__":
    units = get_units_7_8_9_10()
    print(f"Built Units 7, 8, 9, and 10 successfully! Total units: {len(units)}")
    for u in units:
        print(f"  - {u['title']}: {len(u['sections'])} sections, {len(u['problems'])} problems")
