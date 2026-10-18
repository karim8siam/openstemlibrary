# -*- coding: utf-8 -*-
"""
expand_nuclear_problem8.py
Injects Problem 8 across all 10 units for Nuclear and Radiochemistry (#47),
bringing total problems from 70 to 80.
Strictly Zero Course Numbers or Marks.
"""

def add_problem_8_to_units(units):
    prob8_data = {
        1: {
            "id": "prob-1-8",
            "problemNumber": "1.8",
            "title": "Alpha Particle Relativistic Mass-Energy and De Broglie Wavelength",
            "difficulty": "Intermediate",
            "statement": r"""A high-energy alpha particle emitted by polonium-212 has a kinetic energy $T_\alpha = 8.785\text{ MeV}$.
Given the alpha particle rest mass $m_\alpha c^2 = 3727.38\text{ MeV}$ and Planck's constant $h c = 1239.84\text{ MeV}\cdot\text{fm}$:
1. Compute the relativistic momentum $p_\alpha c$ of the alpha particle in $\text{MeV}$.
2. Calculate its reduced de Broglie wavelength $\lambdabar = \hbar / p$ in femtometers ($\text{fm}$).
3. Compare $\lambdabar$ with the nuclear radius of a gold nucleus ($R \approx 7.3\text{ fm}$) and explain why wave diffraction effects were negligible in Rutherford's original experiment.""",
            "solution": r"""### Step 1: Relativistic Momentum
Total relativistic energy:
$$E = T_\alpha + m_\alpha c^2 = 8.785 + 3727.38 = 3736.165\text{ MeV}$$
Momentum:
$$p c = \sqrt{E^2 - (m_\alpha c^2)^2} = \sqrt{(3736.165)^2 - (3727.38)^2} = \sqrt{1.39589 \times 10^7 - 1.38934 \times 10^7} \approx \sqrt{65,580} \approx 256.09\text{ MeV}$$

### Step 2: Reduced de Broglie Wavelength
$$\lambdabar = \frac{\hbar c}{p c} = \frac{197.327\text{ MeV}\cdot\text{fm}}{256.09\text{ MeV}} \approx 0.7705\text{ fm}$$

### Step 3: Comparison with Nuclear Radius
The nuclear radius of gold is $R \approx 7.3\text{ fm}$.
Because the reduced de Broglie wavelength ($\lambdabar \approx 0.77\text{ fm}$) is **nearly ten times smaller than the nuclear radius** ($0.77\text{ fm} \ll 7.3\text{ fm}$), the alpha particle behaves as a localized classical point projectile. Quantum wave diffraction effects are minimal, validating Rutherford's classical hyperbolic trajectory derivation.""",
            "hints": ["Use relativistic energy-momentum invariant: (pc)^2 = E^2 - (m_0*c^2)^2.", "Reduced de Broglie wavelength is hbar*c / (p*c) with hbar*c = 197.3 MeV*fm."]
        },
        2: {
            "id": "prob-2-8",
            "problemNumber": "2.8",
            "title": "Schmidt Limits for Single-Particle Nuclear Magnetic Dipole Moments",
            "difficulty": "Advanced",
            "statement": r"""In the single-particle Shell Model, the magnetic dipole moment $\mu$ of an odd-mass nucleus is determined by the unpaired valence nucleon.
The Schmidt limits state that for an odd nucleon with orbital angular momentum $l$ and total angular momentum $j$:
- Case $j = l + 1/2$: $\mu = j g_l + \frac{1}{2}(g_s - g_l)$
- Case $j = l - 1/2$: $\mu = \frac{j}{j + 1} \left[ (j + 1) g_l - \frac{1}{2}(g_s - g_l) \right]$
Given:
- For a proton: $g_l = 1$, $g_s = +5.586$ nuclear magnetons ($\mu_N$).
- For a neutron: $g_l = 0$, $g_s = -3.826$ nuclear magnetons ($\mu_N$).
1. Calculate the theoretical Schmidt magnetic moment in $\mu_N$ for oxygen-17 ($^{17}_{8}\text{O}$, valence neutron in $1d_{5/2}$, $l = 2, j = 5/2$).
2. Calculate the Schmidt magnetic moment for potassium-39 ($^{39}_{19}\text{K}$, proton hole in $1d_{3/2}$, $l = 2, j = 3/2$).
3. Compare with experimental values ($\mu_{\text{exp}}(^{17}\text{O}) = -1.894\,\mu_N$, $\mu_{\text{exp}}(^{39}\text{K}) = +0.391\,\mu_N$).""",
            "solution": r"""### Step 1: Schmidt Moment for Oxygen-17 ($^{17}\text{O}$)
Valence neutron: $g_l = 0, g_s = -3.826\,\mu_N$.
State is $1d_{5/2} \implies l = 2, j = 5/2 = l + 1/2$.
Using the $j = l + 1/2$ Schmidt formula:
$$\mu = j g_l + \frac{1}{2}(g_s - g_l) = \frac{5}{2}(0) + \frac{1}{2}(-3.826 - 0) = -1.913\,\mu_N$$
Comparison: Experimental value is $-1.894\,\mu_N$—in **exceptional agreement** ($<1\%$ difference)!

### Step 2: Schmidt Moment for Potassium-39 ($^{39}\text{K}$)
Unpaired proton: $g_l = 1, g_s = +5.586\,\mu_N$.
State is $1d_{3/2} \implies l = 2, j = 3/2 = l - 1/2$.
Using the $j = l - 1/2$ Schmidt formula:
$$\mu = \frac{j}{j + 1} \left[ (j + 1) g_l - \frac{1}{2}(g_s - g_l) \right]$$
Here $j = 3/2 \implies j + 1 = 5/2$:
$$\mu = \frac{3/2}{5/2} \left[ \frac{5}{2}(1) - \frac{1}{2}(5.586 - 1) \right] = \frac{3}{5} \left[ 2.500 - \frac{1}{2}(4.586) \right] = 0.60 \times [2.500 - 2.293] = 0.60 \times 0.207 = +0.124\,\mu_N$$
Comparison: Experimental value is $+0.391\,\mu_N$. The deviation is due to core polarization of the paired nucleons.""",
            "hints": ["Identify whether the state is j = l + 1/2 or j = l - 1/2.", "Oxygen-17 has an odd neutron (g_l = 0, g_s = -3.826); Potassium-39 has an odd proton (g_l = 1, g_s = +5.586)."]
        },
        3: {
            "id": "prob-3-8",
            "problemNumber": "3.8",
            "title": "Actinium Natural Series Branching Decay Kinetics at Bismuth-211",
            "difficulty": "Intermediate",
            "statement": r"""In the natural actinium ($4n + 3$) radioactive decay series, bismuth-211 ($^{211}_{83}\text{Bi}$, $T_{1/2} = 2.14\text{ min}$) undergoes branched decay:
- Alpha decay ($99.72\%$, $\lambda_\alpha$) to thallium-207 ($^{207}_{81}\text{Tl}$, $T_{1/2} = 4.77\text{ min}$)
- Beta decay ($0.28\%$, $\lambda_\beta$) to polonium-211 ($^{211}_{84}\text{Po}$, $T_{1/2} = 0.516\text{ s}$)
Both branches terminate at stable lead-207 ($^{207}_{82}\text{Pb}$).
1. Calculate the total decay constant $\lambda_{\text{tot}}$ and partial decay constants $\lambda_\alpha$ and $\lambda_\beta$ in $\text{s}^{-1}$.
2. In a sample containing initially $N_0 = 1.00 \times 10^9\text{ atoms}$ of pure $^{211}\text{Bi}$ at $t = 0$, compute the total number of $^{207}\text{Tl}$ atoms and $^{211}\text{Po}$ atoms formed after complete decay ($t \to \infty$).""",
            "solution": r"""### Step 1: Decay Constants
$$T_{1/2} = 2.14\text{ min} = 128.4\text{ s}$$
$$\lambda_{\text{tot}} = \frac{\ln 2}{128.4\text{ s}} \approx 0.0053983\text{ s}^{-1}$$
Partial constants:
$$\lambda_\alpha = BR_\alpha \cdot \lambda_{\text{tot}} = 0.9972 \times 0.0053983\text{ s}^{-1} \approx 0.0053832\text{ s}^{-1}$$
$$\lambda_\beta = BR_\beta \cdot \lambda_{\text{tot}} = 0.0028 \times 0.0053983\text{ s}^{-1} \approx 1.5115 \times 10^{-5}\text{ s}^{-1}$$

### Step 2: Cumulative Atom Yields
As $t \to \infty$, all initial $^{211}\text{Bi}$ atoms disintegrate. The total number of atoms produced through each branch equals the branching fraction multiplied by $N_0$:
$$N(^{207}\text{Tl}) = BR_\alpha \cdot N_0 = 0.9972 \times 1.00 \times 10^9 = 9.972 \times 10^8\text{ atoms}$$
$$N(^{211}\text{Po}) = BR_\beta \cdot N_0 = 0.0028 \times 1.00 \times 10^9 = 2.80 \times 10^6\text{ atoms}$$
Both branches terminate at stable $^{207}\text{Pb}$, so exactly $1.00 \times 10^9$ lead-207 atoms are created.""",
            "hints": ["Partial decay constants: lambda_i = BR_i * lambda_tot.", "Total atoms produced through branch i as t -> infinity is simply BR_i * N_0."]
        },
        4: {
            "id": "prob-4-8",
            "problemNumber": "4.8",
            "title": "Center-of-Mass Transformation of Differential Cross-Section",
            "difficulty": "Advanced",
            "statement": r"""A nuclear reaction $X(a, b)Y$ has a differential cross-section $(d\sigma/d\Omega)_{\text{CM}}$ in the center-of-mass frame that is isotropic:
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} = \frac{\sigma_{\text{total}}}{4\pi} = \text{constant}$$
1. Derive the kinematic transformation relating the laboratory scattering angle $\theta_{\text{lab}}$ to the center-of-mass angle $\theta_{\text{CM}}$:
$$\tan\theta_{\text{lab}} = \frac{\sin\theta_{\text{CM}}}{\cos\theta_{\text{CM}} + \gamma}$$
where $\gamma = V_{\text{CM}} / v_b^{\text{CM}}$.
2. Derive the transformation formula for the laboratory differential cross-section $(d\sigma/d\Omega)_{\text{lab}}$.
3. Show that forward scattering ($\theta_{\text{lab}} \to 0$) is kinematically enhanced in the laboratory frame.""",
            "solution": r"""### Step 1: Angular Transformation Derivation
In the laboratory frame, the velocity components of particle $b$ are:
$$v_{b,\parallel}^{\text{lab}} = v_b^{\text{CM}} \cos\theta_{\text{CM}} + V_{\text{CM}}$$
$$v_{b,\perp}^{\text{lab}} = v_b^{\text{CM}} \sin\theta_{\text{CM}}$$
The laboratory emission angle $\theta_{\text{lab}}$ satisfies:
$$\tan\theta_{\text{lab}} = \frac{v_{b,\perp}^{\text{lab}}}{v_{b,\parallel}^{\text{lab}}} = \frac{v_b^{\text{CM}} \sin\theta_{\text{CM}}}{v_b^{\text{CM}} \cos\theta_{\text{CM}} + V_{\text{CM}}} = \frac{\sin\theta_{\text{CM}}}{\cos\theta_{\text{CM}} + \gamma}$$
where $\gamma = \frac{V_{\text{CM}}}{v_b^{\text{CM}}}$.

### Step 2: Cross-Section Transformation
By definition of total particle conservation into solid angle:
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{lab}} d\Omega_{\text{lab}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} d\Omega_{\text{CM}}$$
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{lab}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} \frac{\sin\theta_{\text{CM}} d\theta_{\text{CM}}}{\sin\theta_{\text{lab}} d\theta_{\text{lab}}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} \left| \frac{d(\cos\theta_{\text{CM}})}{d(\cos\theta_{\text{lab}})} \right|$$
Evaluating the derivative:
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{lab}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} \frac{(1 + 2\gamma\cos\theta_{\text{CM}} + \gamma^2)^{3/2}}{|1 + \gamma\cos\theta_{\text{CM}}|}$$

### Step 3: Forward Kinematic Enhancement
At forward angle $\theta_{\text{CM}} = 0^\circ$ ($\cos 0^\circ = 1$):
$$\left(\frac{d\sigma}{d\Omega}\right)_{\text{lab}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} \frac{(1 + 2\gamma + \gamma^2)^{3/2}}{1 + \gamma} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} \frac{[(1 + \gamma)^2]^{3/2}}{1 + \gamma} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{CM}} (1 + \gamma)^2$$
Because $\gamma > 0$, $(1 + \gamma)^2 > 1$. The laboratory cross-section in the forward direction is enhanced by the factor $(1 + \gamma)^2$ due to center-of-mass forward focusing!""",
            "hints": ["Velocity in LAB frame is vector sum of CM velocity plus center-of-mass frame particle velocity.", "Conserve total events: (d sigma / d Omega)_lab * d Omega_lab = (d sigma / d Omega)_CM * d Omega_CM."]
        },
        5: {
            "id": "prob-5-8",
            "problemNumber": "5.8",
            "title": "Thermal Utilization and Heterogeneous Fuel Rod Lattice Pitch Optimization",
            "difficulty": "Intermediate",
            "statement": r"""In a heterogeneous graphite-moderated reactor core:
Fuel rods of natural uranium metal ($V_{\text{fuel}} = 1.00\text{ L}$) are arranged in a lattice with graphite moderator volume $V_{\text{mod}} = 45.0\text{ L}$.
Thermal absorption parameters:
- Uranium fuel: $\Sigma_a^{\text{fuel}} = 0.367\text{ cm}^{-1}$
- Graphite moderator: $\Sigma_a^{\text{mod}} = 0.000385\text{ cm}^{-1}$
- Average thermal neutron flux ratio in fuel to moderator: $\bar{\Phi}_{\text{fuel}} / \bar{\Phi}_{\text{mod}} = 0.720$ (flux depression factor)
1. Formulate the thermal utilization factor $f$ incorporating heterogeneous flux depression:
$$f = \frac{\Sigma_a^{\text{fuel}} V_{\text{fuel}} \bar{\Phi}_{\text{fuel}}}{\Sigma_a^{\text{fuel}} V_{\text{fuel}} \bar{\Phi}_{\text{fuel}} + \Sigma_a^{\text{mod}} V_{\text{mod}} \bar{\Phi}_{\text{mod}}}$$
2. Calculate the thermal utilization factor $f$.
3. If the lattice spacing is increased such that $V_{\text{mod}} = 65.0\text{ L}$, compute the new thermal utilization factor and describe the physical tradeoff with resonance escape probability $p$.""",
            "solution": r"""### Step 1: Thermal Utilization Formulation
Dividing numerator and denominator by $\Sigma_a^{\text{fuel}} V_{\text{fuel}} \bar{\Phi}_{\text{fuel}}$:
$$f = \frac{1}{1 + \left(\frac{\Sigma_a^{\text{mod}}}{\Sigma_a^{\text{fuel}}}\right) \left(\frac{V_{\text{mod}}}{V_{\text{fuel}}}\right) \left(\frac{\bar{\Phi}_{\text{mod}}}{\bar{\Phi}_{\text{fuel}}}\right)}$$

### Step 2: Numerical Calculation for $V_{\text{mod}} = 45.0\text{ L}$
Given:
- $\Sigma_a^{\text{mod}} / \Sigma_a^{\text{fuel}} = 0.000385 / 0.367 \approx 1.049 \times 10^{-3}$
- $V_{\text{mod}} / V_{\text{fuel}} = 45.0 / 1.00 = 45.0$
- $\bar{\Phi}_{\text{mod}} / \bar{\Phi}_{\text{fuel}} = 1 / 0.720 \approx 1.3889$

Product:
$$\text{Term} = (1.049 \times 10^{-3}) \times (45.0) \times (1.3889) \approx 0.06556$$
$$f = \frac{1}{1 + 0.06556} \approx 0.9385 \quad (93.85\%)$$

### Step 3: Calculation for $V_{\text{mod}} = 65.0\text{ L}$
$$\text{Term} = (1.049 \times 10^{-3}) \times (65.0) \times (1.3889) \approx 0.09470$$
$$f' = \frac{1}{1 + 0.09470} \approx 0.9135 \quad (91.35\%)$$
The thermal utilization drops by $2.5\%$.
**Physical Tradeoff**: Increasing moderator volume decreases $f$ (more parasitic absorption in graphite), but increases the resonance escape probability $p$ (neutrons slow down safely in the moderator without encountering $^{238}\text{U}$ resonance capture peaks). Reactor engineers optimize lattice pitch where the product $p \cdot f$ reaches its global maximum!""",
            "hints": ["Incorporate flux depression ratio Phi_mod / Phi_fuel into the thermal absorption ratio.", "Tradeoff: increasing moderator volume increases p but decreases f."]
        },
        6: {
            "id": "prob-6-8",
            "problemNumber": "6.8",
            "title": "Double Escape Peak Intensity Ratio in HPGe Detector for 6.13 MeV Gamma",
            "difficulty": "Intermediate",
            "statement": r"""High-energy $6.129\text{ MeV}$ gamma rays emitted by excited oxygen-16 ($^{16}\text{O}^*$ in reactor coolant) interact with a small HPGe detector.
1. State the nominal energies of:
   (a) The full-energy photopeak
   (b) The Single Escape Peak (SEP)
   (c) The Double Escape Peak (DEP)
2. In a small detector volume ($V = 30\text{ cm}^3$), explain why the Double Escape Peak often has a higher count rate than the Full-Energy Photopeak.""",
            "solution": r"""### Step 1: Nominal Spectral Peak Energies
1. **Full-Energy Photopeak**:
$$E = 6.129\text{ MeV} = 6,129\text{ keV}$$
2. **Single Escape Peak (SEP)**:
One $511.0\text{ keV}$ annihilation photon escapes:
$$E_{\text{SEP}} = E - m_e c^2 = 6,129 - 511.0 = 5,618\text{ keV} = 5.618\text{ MeV}$$
3. **Double Escape Peak (DEP)**:
Both $511.0\text{ keV}$ annihilation photons escape:
$$E_{\text{DEP}} = E - 2 m_e c^2 = 6,129 - 1,022.0 = 5,107\text{ keV} = 5.107\text{ MeV}$$

### Step 2: Physical Explanation of DEP Dominance
At $6.13\text{ MeV}$, **pair production** dominates all interaction modes in germanium ($\kappa \gg \tau$).
The created positron slows and annihilates, emitting two back-to-back $511\text{ keV}$ photons.
For a small crystal volume ($30\text{ cm}^3$, dimension $\sim 3\text{ cm}$), the mean free path of a $511\text{ keV}$ photon in germanium is $\lambda_{\text{mfp}} = 1/\mu \approx 2.5\text{ cm}$.
Consequently, the probability that both $511\text{ keV}$ photons escape without interacting is extraordinarily high ($>70\%$).
Therefore, the **Double Escape Peak** at $5.107\text{ MeV}$ appears as the dominant peak in the high-energy spectrum, dwarfing the full-energy photopeak!""",
            "hints": ["Single escape peak is E - 511 keV; Double escape peak is E - 1022 keV.", "At high energies (>5 MeV), pair production dominates over photoelectric absorption."]
        },
        7: {
            "id": "prob-7-7-ext",
            "problemNumber": "7.8",
            "title": "Digital Pulse Processor Ballistic Deficit Elimination and Trapezoidal Peaking",
            "difficulty": "Intermediate",
            "statement": r"""In a coaxial High-Purity Germanium detector, charge collection times vary from $t_{\text{coll}} = 150\text{ ns}$ to $400\text{ ns}$ depending on whether ionizing events occur near the central core contact or the outer circumference.
An analog RC-(CR) filter with shaping time $\tau = 1.0\,\mu\text{s}$ experiences a peak amplitude loss of $8.5\%$ for the slowest pulses (ballistic deficit).
1. Explain how a digital trapezoidal filter with flat-top duration $L_{\text{flat}}$ completely eliminates ballistic deficit.
2. Determine the minimum flat-top duration $L_{\text{flat}}$ required in microseconds.""",
            "solution": r"""### Step 1: Mechanism of Ballistic Deficit Elimination
In analog semi-Gaussian shaping, the pulse peak occurs at a single point in time ($t_{\text{peak}} \approx 2\tau$). If charge collection is prolonged, some charge has not yet arrived when the shaping network peaks, causing a deficit in pulse height that broadens the spectral line.

A **Digital Trapezoidal Filter** convolves the digitized step pulse with a finite impulse response (FIR) filter having a flat plateau (flat top) of duration $L_{\text{flat}}$.
The height of the flat top represents the true total integrated charge collected at the electrode, independent of when individual charge carriers arrived.

### Step 2: Minimum Flat-Top Duration
To ensure complete, invariant charge collection:
$$L_{\text{flat}} \ge t_{\text{coll,\max}} - t_{\text{coll,\min}} = 400\text{ ns} - 150\text{ ns} = 250\text{ ns}$$
Adding an electronic safety margin of $100\text{ ns}$:
$$L_{\text{flat}} \ge 0.35 - 0.50\,\mu\text{s} \quad (350 - 500\text{ ns})$$
Setting the flat top to $0.50\,\mu\text{s}$ eliminates ballistic deficit completely, restoring intrinsic HPGe energy resolution even in large $150\%$ relative efficiency crystals!""",
            "hints": ["Ballistic deficit occurs when charge collection time is comparable to shaping time.", "The flat top must be longer than the maximum variation in charge collection time."]
        },
        8: {
            "id": "prob-8-8",
            "problemNumber": "8.8",
            "title": "Reverse Isotope Dilution for High-Level Liquid Waste Strontium-90 Assay",
            "difficulty": "Easy",
            "statement": r"""A $10.0\text{ mL}$ aliquot of high-level liquid radioactive reprocessing waste containing an unknown mass $m_x$ of $^{90}\text{Sr}$ ($T_{1/2} = 28.9\text{ yr}$, pure $\beta^-$) has an activity $A_x = 4.50 \times 10^7\text{ Bq}$ ($1.216\text{ mCi}$).
Because the waste contains overwhelming levels of other beta emitters, reverse isotope dilution is performed:
1. Pure non-radioactive stable strontium carrier of mass $m_1 = 50.0\text{ mg}$ is added.
2. Strontium is precipitated selectively as strontium carbonate ($\text{SrCO}_3$) with chemical recovery yield of only $38.0\%$.
3. A $5.00\text{ mg}$ sample of the purified $\text{SrCO}_3$ ($M = 147.63\text{ g/mol}$, containing $2.967\text{ mg}$ of pure elemental $\text{Sr}$) is counted, yielding an activity $A_2 = 2.67 \times 10^5\text{ Bq}$.
Calculate:
1. The specific activity $S_2$ of the isolated strontium in $\text{Bq/mg}$.
2. The initial mass $m_x$ of $^{90}\text{Sr}$ in the $10.0\text{ mL}$ waste sample in micrograms ($\mu\text{g}$).""",
            "solution": r"""### Step 1: Specific Activity $S_2$
Elemental strontium mass in counted sample: $m_{\text{Sr}} = 2.967\text{ mg}$.
$$S_2 = \frac{A_2}{m_{\text{Sr}}} = \frac{2.67 \times 10^5\text{ Bq}}{2.967\text{ mg}} \approx 90,000\text{ Bq/mg} = 9.00 \times 10^4\text{ Bq/mg}$$

### Step 2: Calculate Initial $^{90}\text{Sr}$ Mass $m_x$
By conservation of total radioactivity:
The total initial activity $A_x$ is now distributed uniformly across total strontium mass $(m_1 + m_x) \approx m_1$ (since $m_x \ll m_1$):
$$S_2 = \frac{A_x}{m_1 + m_x} \approx \frac{A_x}{m_1}$$
Theoretical specific activity of carrier-free $^{90}\text{Sr}$:
$$\lambda = \frac{\ln 2}{28.9 \times 3.15576 \times 10^7\text{ s}} \approx 7.600 \times 10^{-10}\text{ s}^{-1}$$
$$SA(^{90}\text{Sr}) = \frac{\lambda N_A}{M} = \frac{(7.600 \times 10^{-10})(6.022 \times 10^{23})}{89.91\text{ g}} \approx 5.09 \times 10^{12}\text{ Bq/g} = 5.09 \times 10^9\text{ Bq/mg}$$
Unknown mass $m_x$:
$$m_x = \frac{A_x}{SA(^{90}\text{Sr})} = \frac{4.50 \times 10^7\text{ Bq}}{5.09 \times 10^9\text{ Bq/mg}} \approx 0.00884\text{ mg} = 8.84\,\mu\text{g}$$
Notice that the chemical recovery yield ($38\%$) did not enter into the calculation—reverse IDA is completely independent of extraction recovery!""",
                    "hints": ["Specific activity S_2 = A_2 / m_isolated.", "Mass of radioisotope m_x = A_x / SA_theoretical."]
                },
        9: {
            "id": "prob-9-8",
                    "problemNumber": "9.8",
                    "title": "Carrier-Free Iodine-131 Distillation Yield from Irradiated Tellurium Target",
                    "difficulty": "Intermediate",
                    "statement": r"""Carrier-free iodine-131 is produced by neutron irradiation of natural tellurium dioxide ($\text{TeO}_2$, containing $34.08\%$ $^{130}\text{Te}$):
$$^{130}\text{Te}(n, \gamma)^{131}\text{Te} \xrightarrow[\beta^-]{25.0\text{ min}} \, ^{131}\text{I} \quad (T_{1/2} = 8.025\text{ days})$$
The thermal capture cross-section of $^{130}\text{Te}$ is $\sigma = 0.220\text{ barns}$.
A target of $m_{\text{target}} = 100.0\text{ g}$ of $\text{TeO}_2$ is irradiated in a thermal neutron flux $\Phi = 5.00 \times 10^{13}\text{ n/cm}^2\cdot\text{s}$ for $t_{\text{irr}} = 14.0\text{ days}$.
1. Calculate the number of $^{130}\text{Te}$ target atoms present.
2. Because $^{131}\text{Te}$ decays rapidly into $^{131}\text{I}$, calculate the activity of $^{131}\text{I}$ produced at the end of irradiation in $\text{GBq}$.
3. After thermal dry distillation at $750^\circ\text{C}$ with $85\%$ recovery, compute the harvested activity in Curies.""",
                    "solution": r"""### Step 1: Target $^{130}\text{Te}$ Atoms
Molar mass of $\text{TeO}_2 \approx 127.60 + 32.00 = 159.60\text{ g/mol}$.
Total tellurium atoms:
$$N_{\text{Te}} = \frac{100.0\text{ g}}{159.60\text{ g/mol}} \times 6.022 \times 10^{23} \approx 3.773 \times 10^{23}\text{ atoms}$$
Number of $^{130}\text{Te}$ atoms ($34.08\%$):
$$N_{130} = 3.773 \times 10^{23} \times 0.3408 \approx 1.286 \times 10^{23}\text{ atoms}$$

### Step 2: Iodine-131 Activity at EOI
Because $^{131}\text{Te}$ has a very short half-life ($25\text{ min}$), it rapidly reaches secular equilibrium with production; every $(n, \gamma)$ capture directly yields $^{131}\text{I}$.
Production rate:
$$R = N_{130} \sigma \Phi = (1.286 \times 10^{23})(0.220 \times 10^{-24}\text{ cm}^2)(5.00 \times 10^{13}\text{ cm}^{-2}\cdot\text{s}^{-1}) \approx 1.4146 \times 10^{12}\text{ atoms/second}$$
Decay constant of $^{131}\text{I}$:
$$\lambda = \frac{\ln 2}{8.025 \times 86400\text{ s}} \approx 9.997 \times 10^{-7}\text{ s}^{-1}$$
Irradiation time $t_{\text{irr}} = 14.0\text{ days} = 1,209,600\text{ s}$.
Saturation factor:
$$\lambda t_{\text{irr}} = (9.997 \times 10^{-7}\text{ s}^{-1})(1,209,600\text{ s}) \approx 1.2092$$
$$1 - e^{-\lambda t_{\text{irr}}} = 1 - e^{-1.2092} = 1 - 0.29844 = 0.70156$$
Activity at EOI:
$$A_{\text{EOI}} = R (1 - e^{-\lambda t_{\text{irr}}}) = (1.4146 \times 10^{12}\text{ s}^{-1})(0.70156) \approx 9.924 \times 10^{11}\text{ Bq} \approx 992.4\text{ GBq}$$

### Step 3: Harvested Distillation Activity
With $85\%$ recovery:
$$A_{\text{harvest}} = 992.4\text{ GBq} \times 0.85 \approx 843.5\text{ GBq}$$
In Curies:
$$A_{\text{harvest}} = \frac{843.5\text{ GBq}}{37\text{ GBq/Ci}} \approx 22.8\text{ Curies}$$
The distillation batch yields **$22.8\text{ Curies}$** ($844\text{ GBq}$) of carrier-free iodine-131.""",
                    "hints": ["Calculate target atoms N_130 = (m / M) * N_A * abundance.", "Activity A = R * (1 - exp(-lambda * t_irr))."]
                },
        10: {
            "id": "prob-10-8",
                    "problemNumber": "10.8",
                    "title": "Air Kerma Rate Constant and Shielding Calculation for Technetium-99m Syringe",
                    "difficulty": "Easy",
                    "statement": r"""A nuclear medicine technologist prepares a patient injection syringe containing $A = 30.0\text{ mCi}$ ($1,110\text{ MBq}$) of $^{99m}\text{Tc}$ ($E_\gamma = 140.5\text{ keV}$).
The air kerma rate constant is $\Gamma_\delta = 17.0\,\mu\text{Gy}\cdot\text{m}^2 / (\text{GBq}\cdot\text{h}) = 0.076\text{ R}\cdot\text{m}^2 / (\text{Ci}\cdot\text{h})$.
1. Calculate the unshielded dose rate at distance $d = 1.00\text{ meter}$ and at distance $d = 10.0\text{ cm}$ in $\mu\text{Sv/h}$ ($w_R = 1$).
2. The technologist holds the syringe inside a tungsten syringe shield of thickness $x = 2.0\text{ mm}$ ($\text{HVL}_{\text{tungsten}} = 0.40\text{ mm}$ for $140\text{ keV}$). Determine the transmission factor and the attenuated dose rate at $10.0\text{ cm}$.
3. Calculate the hand dose received during a $30\text{-second}$ injection.""",
                    "solution": r"""### Step 1: Unshielded Dose Rates
At $d = 1.00\text{ meter}$:
$$\dot{H}(1\text{ m}) = \frac{\Gamma \cdot A}{d^2} = \frac{(17.0\,\mu\text{Sv}\cdot\text{m}^2/\text{GBq}\cdot\text{h})(1.110\text{ GBq})}{(1.00\text{ m})^2} = 18.87\,\mu\text{Sv/h}$$
At $d = 10.0\text{ cm} = 0.100\text{ m}$:
$$\dot{H}(0.10\text{ m}) = 18.87\,\mu\text{Sv/h} \times \left(\frac{1.00}{0.100}\right)^2 = 18.87 \times 100 = 1,887\,\mu\text{Sv/h} \approx 1.89\text{ mSv/h}$$

### Step 2: Tungsten Shield Attenuation
Shield thickness: $x = 2.0\text{ mm}$.
Number of half-value layers:
$$n = \frac{x}{\text{HVL}} = \frac{2.0\text{ mm}}{0.40\text{ mm}} = 5.0\text{ HVLs}$$
Transmission factor:
$$T = \left(\frac{1}{2}\right)^n = \left(\frac{1}{2}\right)^5 = \frac{1}{32} \approx 0.03125 \quad (3.125\%)$$
Attenuated dose rate at $10\text{ cm}$:
$$\dot{H}_{\text{shielded}} = 1,887\,\mu\text{Sv/h} \times 0.03125 \approx 59.0\,\mu\text{Sv/h}$$

### Step 3: Injection Dose
Injection duration: $t = 30\text{ seconds} = 30 / 3600\text{ h} = 0.008333\text{ h}$.
$$\text{Hand Dose} = (59.0\,\mu\text{Sv/h}) \times (0.008333\text{ h}) \approx 0.492\,\mu\text{Sv}$$
The tungsten shield reduces the hand dose to barely **$0.49\,\mu\text{Sv}$** (compared to $15.7\,\mu\text{Sv}$ unshielded), ensuring total ALARA protection across hundreds of injections!""",
                    "hints": ["Inverse square law scales dose rate by (d_1 / d_2)^2.", "Transmission factor is (1/2)^n where n = thickness / HVL."]
                }
    }

    for unit in units:
        un = unit["unitNumber"]
        if un in prob8_data:
            p8 = prob8_data[un]
            if not any(p["id"] == p8["id"] for p in unit["problems"]):
                unit["problems"].append(p8)
    return units
