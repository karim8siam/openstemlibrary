# Unit 1: Electrical conduction and electronic response

**Guiding research question:** How do microscopic charge carriers, specimen geometry and interfaces determine measured electrical response?

## Physical context and experimental objectives

An electrical material is not an ideal circuit element. A measured voltage drop includes geometry, contact barriers, specimen heating, grain boundaries and possible leakage paths. The fundamental measurement question is which region actually carries the current.

A metallic temperature coefficient is often useful as a thermometer over a limited range, but disorder and phase changes can destroy the linear approximation; thickness dependence likewise exposes surface scattering.

The five lessons in this unit emphasize **mobile charges in finite conductors and heterogeneous films**. A central challenge is separating **bulk resistivity versus measured component resistance**, because both may appear as a single output on an instrument display. Before interpreting response, establish **temperature, specimen geometry, contacts and frequency**. The most important rival explanation is **contact barrier, grain-boundary transport or parallel paths**; an efficient validation strategy incorporates **four-terminal transport and temperature sweep** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

Construct a sample diagram with dimensions and sign conventions. Mark which variables can be manipulated independently and which require calibration or inverse modeling. Predict the response at the low-input and high-input limits; if a formula implies a physical divergence, write down which approximation breaks first. Identify the specimen history needed to reproduce an experiment. Separate a mathematical sensitivity exercise from an engineering acceptance test; all exported data here are explicitly synthetic and contain no experimental noise.

## Unit map

For each lesson, read the physical argument, solve the numerical example, reproduce its value using the model, critique the stated limitations, and attempt three graded problems. The two model cards appear after lessons 1 and 4 and are deliberately restricted to one control each. The integrated investigation asks for independent evidence, not simply comparison of two computed curves. If two mechanisms remain observationally indistinguishable, report the unresolved alternative instead of inventing a microscopic identification.

## Lesson 1.1: Carrier motion, local fields and constitutive laws

### Microscopic picture and applicable constitutive law

Electrical current density J and electric field E are related by J=σE only for a local linear isotropic conductor at a specified state. In a crystal, conductivity is a tensor; rotating a single crystal changes the current response even at identical composition. In granular specimens, a fitted effective σ can conceal the conductive paths and insulating contacts. Resistivity ρ=1/σ is intrinsic only when geometry, temperature and frequency are controlled, while resistance R depends explicitly on current path length and cross-section. Distinguish the microscopic electron scattering mechanism from the observed potential difference.

**Primary relationship.** For a uniform bar R=ρL/A; in the local isotropic limit J=σE. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **carrier motion, local fields and constitutive laws**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A sputtered conductor has a lower resistance after annealing. Sketch two hypotheses: grain growth increased mobility, or a previously discontinuous film became connected. Predict whether Hall mobility and spatial conductive mapping should change in the same way.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Metal resistivity versus temperature** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 291.11111 K**. With the implemented expression `1.7*(1+0.0039*(T-293))`, the output is **1.68747667 microohm cm**. Increase the control to **306.66667 K**. The new output is **1.79061 microohm cm**. Thus the model output increases over this interval, with secant slope **0.00663 (microohm cm)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Computational interpretation.** A finite difference checks the sign and scale of one model derivative. It does not determine which unmeasured parameter controls a real specimen, nor does it provide a physical uncertainty interval. Inspect the expression for possible division by zero, logarithm of nonpositive arguments, negative physical quantities or an exponential so large that the assumptions no longer apply. Predict both end values before moving the slider. Then reproduce one displayed value independently on paper by substituting numbers with coherent units. The graph is a deterministic curve, not experimental data, even when it resembles a real measured response.

**Model boundary.** Linear temperature coefficient α=0.0039 K⁻¹ relative to 293 K; ρ_ref=1.7 μΩ cm; illustrative metallic regime only. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Ohm’s law may fail with heating, strong fields, rectifying contacts or changing oxidation state.

Begin with **temperature-controlled four-point transport**, and record **actual probe spacing, film thickness, thermal equilibrium, reversal of current and contact repeatability**. Cross-check with **Hall measurements and conductivity mapping** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Follow with a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **carrier motion, local fields and constitutive laws**, but **contact barrier, grain-boundary transport or parallel paths** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **four-terminal transport and temperature sweep** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

It is also important to ask whether an apparently large effect is a normalization artifact. Magnetization per specimen mass depends on the nonmagnetic fraction; capacitance depends on true electrode area; sheet resistance depends on continuous film thickness; and energy loss per cycle must not be confused with loss per second. Use a dimensional check and at least one independent geometric calibration. If a claim survives these tests, its correct status is still conditional until the relevant physical regime and sample-to-sample robustness are demonstrated.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **carrier motion, local fields and constitutive laws** affects the distinction between **bulk resistivity versus measured component resistance**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **1.68747667 microohm cm** and **1.79061 microohm cm** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (microohm cm)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **contact barrier, grain-boundary transport or parallel paths** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **four-terminal transport and temperature sweep** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_0 -->

## Lesson 1.2: Temperature coefficients and competing scattering mechanisms

### Microscopic picture and applicable constitutive law

Metals often have increasing resistivity with temperature because lattice vibrations scatter electrons, whereas activated electronic or ionic transport may show a decreasing resistance with increasing temperature. Matthiessen’s rule approximates additive scattering contributions, not necessarily resistivities in complex polycrystals. A linear temperature coefficient describes a finite region rather than a universal law. Disorder, magnetic transitions and contact changes can reverse or obscure a trend. State the reference temperature whenever using a coefficient.

**Primary relationship.** In a limited metallic range ρ(T)=ρref[1+α(T−Tref)]. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **temperature coefficients and competing scattering mechanisms**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A wiring alloy and a ceramic sensor exhibit opposite resistance slopes. Calculate the simple reference model, then design temperature cycles to test reversibility and observe drift, self-heating and thermal lag separately.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Conductive thin-film sheet resistance** as an exercise in numerical reasoning. Its controllable variable is **Film thickness**; all other quantities follow fixed assumptions. Set **Film thickness = 180 nm**. With the implemented expression `1000/t`, the output is **5.55555556 ohm per square**. Increase the control to **233.33333 nm**. The new output is **4.28571429 ohm per square**. Thus the model output decreases over this interval, with secant slope **-0.0238095238 (ohm per square)/(nm)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Uniform film resistivity 100 μΩ cm and t in nm; ignores interface scattering and lateral variation. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Extrapolating a room-temperature linear coefficient to cryogenic or near-melting regimes is unjustified.

Begin with **guarded dielectric impedance spectroscopy**, and record **open–short standards, fixture parasitics, drive amplitude, temperature and frequency**. Cross-check with **electrode-thickness comparison and conductivity measurement** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Follow with a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **temperature coefficients and competing scattering mechanisms**, but **contact barrier, grain-boundary transport or parallel paths** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **four-terminal transport and temperature sweep** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **temperature coefficients and competing scattering mechanisms** affects the distinction between **bulk resistivity versus measured component resistance**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **5.55555556 ohm per square** and **4.28571429 ohm per square** from the explicit expression for the stated two values of **Film thickness**. Report a unit-consistent slope in (ohm per square)/(nm), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 1.3: Two-dimensional conduction and sheet resistance

### Microscopic picture and applicable constitutive law

A thin conductive coating is often specified by sheet resistance in ohms per square. The word square is a geometric reminder: the length-to-width ratio multiplies the sheet resistance, and the numeric resistance of a square does not depend on that square’s absolute edge length when material and thickness are uniform. Surface and interface scattering make bulk resistivity assumptions unreliable for ultrathin films. Parallel conduction in a substrate further contaminates a four-point sheet measurement.

**Primary relationship.** For uniform thickness t, Rs=ρ/t and strip R=Rs L/W. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **two-dimensional conduction and sheet resistance**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Compare two patterned strips of equal film and width but different lengths. Predict how R changes, then make a thickness series to determine whether inferred resistivity stays constant. If it does not, seek evidence of scattering or discontinuity.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Metal resistivity versus temperature** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 322.22222 K**. With the implemented expression `1.7*(1+0.0039*(T-293))`, the output is **1.89374333 microohm cm**. Increase the control to **337.77778 K**. The new output is **1.99687667 microohm cm**. Thus the model output increases over this interval, with secant slope **0.00663 (microohm cm)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Sheet resistance is not the same as contact resistance, and thickness nonuniformity invalidates the simple formula.

Begin with **ferroelectric switching-current analysis**, and record **pulse polarity, leakage compensation, electrode area, voltage waveform and conditioning history**. Cross-check with **PUND pulse sequence and structural domain microscopy** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Follow with a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **two-dimensional conduction and sheet resistance**, but **contact barrier, grain-boundary transport or parallel paths** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **four-terminal transport and temperature sweep** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **two-dimensional conduction and sheet resistance** affects the distinction between **bulk resistivity versus measured component resistance**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **1.89374333 microohm cm** and **1.99687667 microohm cm** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (microohm cm)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 1.4: Interfaces, contacts and nonlinear injection

### Microscopic picture and applicable constitutive law

A nominally excellent conductor can fail to deliver current through an electronic device because electrode interfaces inject carriers imperfectly. Rectification can arise from Schottky barriers, oxides, tunneling gaps or diffusion-limited contacts. Two-terminal I–V curves therefore combine bulk and contact processes. Transmission-line and four-terminal designs help separate them when geometry and fabrication permit. Interface chemistry may also change over the first few sweeps.

**Primary relationship.** A basic series model writes Rtwo-terminal=Rbulk+Rcontact,1+Rcontact,2. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **interfaces, contacts and nonlinear injection**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A contact-metal substitution doubles apparent channel resistance. Use unequal channel lengths and contact test structures to decide whether the contact term rather than film conductivity changed. Repeat in both current directions.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Conductive thin-film sheet resistance** as an exercise in numerical reasoning. Its controllable variable is **Film thickness**; all other quantities follow fixed assumptions. Set **Film thickness = 286.66667 nm**. With the implemented expression `1000/t`, the output is **3.48837209 ohm per square**. Increase the control to **340 nm**. The new output is **2.94117647 ohm per square**. Thus the model output decreases over this interval, with secant slope **-0.0102599179 (ohm per square)/(nm)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Extracted specific contact resistivity can be model dependent in current-crowding geometries.

Begin with **vibrating-sample or SQUID magnetometry**, and record **sample mass, holder background, field calibration, temperature and demagnetizing geometry**. Cross-check with **magneto-optic imaging or neutron/X-ray diffraction as relevant** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Follow with a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **interfaces, contacts and nonlinear injection**, but **contact barrier, grain-boundary transport or parallel paths** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **four-terminal transport and temperature sweep** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **interfaces, contacts and nonlinear injection** affects the distinction between **bulk resistivity versus measured component resistance**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **3.48837209 ohm per square** and **2.94117647 ohm per square** from the explicit expression for the stated two values of **Film thickness**. Report a unit-consistent slope in (ohm per square)/(nm), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_1 -->

## Lesson 1.5: Hopping, ionic and percolative transport

### Microscopic picture and applicable constitutive law

Not every conducting solid transports charges through free-electron-like bands. Disordered oxides may show thermally assisted hopping; polymer composites may conduct through filler networks; solid electrolytes carry ions that redistribute over time. Frequency, electric-field history and time since bias application become essential state variables. A percolation exponent fitted to bulk data cannot establish the microscopic identity of conductive links, and the threshold depends on particle geometry and processing.

**Primary relationship.** Near an idealized percolation threshold, σ ∝ (p−pc)^t for p>pc; t is model-specific. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **hopping, ionic and percolative transport**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A composite suddenly becomes conductive at increasing carbon loading. Prepare independent samples near the apparent threshold and compare direct current, alternating current and microscopy to distinguish percolation from electrode leakage.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Metal resistivity versus temperature** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 353.33333 K**. With the implemented expression `1.7*(1+0.0039*(T-293))`, the output is **2.10001 microohm cm**. Increase the control to **368.88889 K**. The new output is **2.20314333 microohm cm**. Thus the model output increases over this interval, with secant slope **0.00663 (microohm cm)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Steady-state Ohmic models can fail when conducting paths form, break or migrate under an applied field.

Begin with **dynamic core-loss metrology**, and record **B waveform, excitation frequency, winding calibration, sample dimensions and thermal drift**. Cross-check with **calorimetry and static loop analysis** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Follow with a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **hopping, ionic and percolative transport**, but **contact barrier, grain-boundary transport or parallel paths** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **four-terminal transport and temperature sweep** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **hopping, ionic and percolative transport** affects the distinction between **bulk resistivity versus measured component resistance**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **2.10001 microohm cm** and **2.20314333 microohm cm** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (microohm cm)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: Conductive coating qualification

### Diagnose the evidence, not just the material label

A transparent electrode candidate meets its nominal room-temperature sheet-resistance target but fails a patterned interconnect test. The failure could reflect an unstable contact, discontinuous coating or bulk temperature coefficient. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Combine sheet-resistance scaling and temperature measurements, then use independently varied contact geometry and sputtering conditions. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Compare four-terminal and two-terminal data across four widths; include microscopy and independent deposition batches. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **contact barrier, grain-boundary transport or parallel paths** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** Do not accept thin-film conductivity from a bulk formula without thickness characterization.

### Five capstone examination questions

1. Draw the specimen and measurement chain, marking E, D, P, H, M or B with correct units where they are actually relevant.
2. Explain the leading mechanism and a serious alternative. What extra measurement would make their predictions differ?
3. Recalculate the two unit models at their endpoints, and identify a limiting condition where each approximation fails.
4. Design an uncertainty and replication plan that separates same-device sweeps from independent process-batch results.
5. Write a one-page materials selection decision listing demonstrated observations, synthetic model sensitivities, unresolved risks and the tests required before qualification.

