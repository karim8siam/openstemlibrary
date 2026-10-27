# Unit 2: Dielectric polarization, relaxation and loss

**Guiding research question:** How do reversible polarization, delayed dipoles, ionic conduction and electrode geometry affect a dielectric?

## Physical context and experimental objectives

Capacitance registers displacement and storage, whereas dielectric loss records irreversible dissipation. Their separation requires a known drive frequency and electrode configuration. A high apparent capacitance alone cannot establish a good insulating material.

A single-relaxation Debye model is a conceptual starting point; space-charge polarization and broad distributions of dipole times produce different dispersion signatures.

The five lessons in this unit emphasize **bound polarization, displacement current and dielectric dissipation**. A central challenge is separating **real permittivity versus loss and conduction**, because both may appear as a single output on an instrument display. Before interpreting response, establish **field amplitude, thickness, sweep rate and electrode area**. The most important rival explanation is **electrode polarization or leakage masquerading as permittivity**; an efficient validation strategy incorporates **guarded broadband impedance and thickness scaling** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 2.1: Electric displacement, polarization and capacitance

### Microscopic picture and applicable constitutive law

The constitutive relation D=ε0E+P separates vacuum response from matter polarization. Under linear isotropic conditions P=ε0χeE, giving D=ε0εrE. The geometry of a capacitor determines its measured capacitance and can distort an inferred permittivity if field lines fringe or the electrode area is wrong. A frequency-dependent dielectric constant is not a single invariant material fingerprint. Real capacitors also have electrodes, interfaces and parasitic inductance.

**Primary relationship.** For parallel plates, C=ε0εrA/d when the field is uniform. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **electric displacement, polarization and capacitance**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Two devices share nominal dielectric chemistry but different layer thicknesses. Predict inverse-thickness capacitance, measure guarded fixture parasitics, and decide whether an interfacial dead layer changes the scaling.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Planar dielectric capacitance** as an exercise in numerical reasoning. Its controllable variable is **Insulator thickness**; all other quantities follow fixed assumptions. Set **Insulator thickness = 9.6666667 micrometers**. With the implemented expression `8.8541878188e-12*20*0.0001/(d*1e-6)*1e9`, the output is **1.83190093 nF**. Increase the control to **14 micrometers**. The new output is **1.26488397 nF**. Thus the model output decreases over this interval, with secant slope **-0.130850066 (nF)/(micrometers)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Ideal parallel plates, A=1 cm², εr=20 independent of field and frequency; no fringing. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

The ideal relation fails for nonlinear materials, nonuniform fields, finite leakage and large fringe fields.

Perform a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Follow with a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **electric displacement, polarization and capacitance**, but **electrode polarization or leakage masquerading as permittivity** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **guarded broadband impedance and thickness scaling** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **electric displacement, polarization and capacitance** affects the distinction between **real permittivity versus loss and conduction**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **1.83190093 nF** and **1.26488397 nF** from the explicit expression for the stated two values of **Insulator thickness**. Report a unit-consistent slope in (nF)/(micrometers), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **electrode polarization or leakage masquerading as permittivity** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **guarded broadband impedance and thickness scaling** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_2 -->

## Lesson 2.2: Dipolar relaxation and complex permittivity

### Microscopic picture and applicable constitutive law

Bound dipoles require time to respond, creating dispersion and loss. With the exp(+iωt) convention, a convenient ε*=ε′−iε″ has positive ε″ for passive relaxation. The Debye law assumes one relaxation time, allowing a characteristic loss feature near ωτ=1, but real ceramics and polymers often contain broad distributions. Plotting the real and imaginary parts together is essential: a single capacitance number cannot determine whether changes are storage or dissipation.

**Primary relationship.** Debye ε′=ε∞+Δε/(1+ω²τ²) and ε″=Δε ωτ/(1+ω²τ²). This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **dipolar relaxation and complex permittivity**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A dielectric exhibits a loss peak that shifts to higher frequencies as it warms. Estimate the characteristic time at each peak, then compare a single-relaxation fit with a stretched or multi-time response.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Debye dielectric loss tangent** as an exercise in numerical reasoning. Its controllable variable is **Drive frequency**; all other quantities follow fixed assumptions. Set **Drive frequency = 33366.667 Hz**. With the implemented expression `(16*(2*Math.PI*f*0.0001)/(1+Math.pow(2*Math.PI*f*0.0001,2)))/(4+16/(1+Math.pow(2*Math.PI*f*0.0001,2)))`, the output is **0.188649089 dimensionless**. Increase the control to **44472.222 Hz**. The new output is **0.14223912 dimensionless**. Thus the model output decreases over this interval, with secant slope **-4.17898671e-06 (dimensionless)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Single relaxation time τ=100 μs, ε∞=4, Δε=16; excludes conduction and distributions of relaxation times. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Conduction loss contributes σ/(ε0ω) to the effective ε″ under common conventions; neglecting it may misidentify dipoles.

Perform a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Follow with a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **dipolar relaxation and complex permittivity**, but **electrode polarization or leakage masquerading as permittivity** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **guarded broadband impedance and thickness scaling** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **dipolar relaxation and complex permittivity** affects the distinction between **real permittivity versus loss and conduction**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.188649089 dimensionless** and **0.14223912 dimensionless** from the explicit expression for the stated two values of **Drive frequency**. Report a unit-consistent slope in (dimensionless)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 2.3: Polarization mechanisms and frequency hierarchy

### Microscopic picture and applicable constitutive law

Electronic polarization involves electron clouds, ionic polarization relative ionic displacements, orientational polarization permanent dipoles and interfacial polarization charge accumulation. Different mechanisms have different response scales and frequency windows. An apparent giant permittivity at low frequency may be caused by a poorly conducting barrier layer rather than large intrinsic ionic displacement. Microstructural context is therefore indispensable.

**Primary relationship.** Complex permittivity ε*(ω) links phase-shifted polarization to alternating electric field. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **polarization mechanisms and frequency hierarchy**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Given low- and high-frequency permittivity from the same pellet, decide which polarizations can plausibly follow the drive. Compare polished and coated electrodes and a thickness series before assigning the enhancement to an intrinsic material response.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Planar dielectric capacitance** as an exercise in numerical reasoning. Its controllable variable is **Insulator thickness**; all other quantities follow fixed assumptions. Set **Insulator thickness = 18.333333 micrometers**. With the implemented expression `8.8541878188e-12*20*0.0001/(d*1e-6)*1e9`, the output is **0.965911398 nF**. Increase the control to **22.666667 micrometers**. The new output is **0.781251866 nF**. Thus the model output decreases over this interval, with secant slope **-0.0426137382 (nF)/(micrometers)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Relaxation spectra depend on temperature, moisture, electrode chemistry and texture; mechanism labels require supporting evidence.

Perform a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Follow with a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **polarization mechanisms and frequency hierarchy**, but **electrode polarization or leakage masquerading as permittivity** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **guarded broadband impedance and thickness scaling** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **polarization mechanisms and frequency hierarchy** affects the distinction between **real permittivity versus loss and conduction**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.965911398 nF** and **0.781251866 nF** from the explicit expression for the stated two values of **Insulator thickness**. Report a unit-consistent slope in (nF)/(micrometers), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 2.4: Dielectric breakdown, defects and leakage

### Microscopic picture and applicable constitutive law

An insulating material can fail through intrinsic field acceleration, defect-mediated conduction, thermal runaway, electrode injection or mechanical damage. Breakdown voltage is a component outcome; electric strength is conventionally field V/d under specified geometry, though local hotspots can exceed this average. Thinner films often exhibit a different failure population because extreme defects scale with tested area and thickness. Averages without sample sizes conceal tails that matter in design.

**Primary relationship.** Average applied field E=V/d; this is not the maximum local field at a defect. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **dielectric breakdown, defects and leakage**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Two production lots show identical median leakage but different weak-end failure tails. Plan area-matched stress testing with censored survivors and a transparent selection criterion rather than claiming one fixed breakdown field.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Debye dielectric loss tangent** as an exercise in numerical reasoning. Its controllable variable is **Drive frequency**; all other quantities follow fixed assumptions. Set **Drive frequency = 55577.778 Hz**. With the implemented expression `(16*(2*Math.PI*f*0.0001)/(1+Math.pow(2*Math.PI*f*0.0001,2)))/(4+16/(1+Math.pow(2*Math.PI*f*0.0001,2)))`, the output is **0.114077995 dimensionless**. Increase the control to **66683.333 Hz**. The new output is **0.0951979525 dimensionless**. Thus the model output decreases over this interval, with secant slope **-1.70005385e-06 (dimensionless)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Do not use teaching breakdown calculations to set safe operating voltages; qualified safety procedures are required.

Perform a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Follow with a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **dielectric breakdown, defects and leakage**, but **electrode polarization or leakage masquerading as permittivity** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **guarded broadband impedance and thickness scaling** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **dielectric breakdown, defects and leakage** affects the distinction between **real permittivity versus loss and conduction**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.114077995 dimensionless** and **0.0951979525 dimensionless** from the explicit expression for the stated two values of **Drive frequency**. Report a unit-consistent slope in (dimensionless)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_3 -->

## Lesson 2.5: Interfacial charge and Maxwell–Wagner response

### Microscopic picture and applicable constitutive law

Heterogeneous regions with different conductivities and permittivities can accumulate charge at internal boundaries. This produces Maxwell–Wagner-type dispersion without requiring molecular dipole rotation. Equivalent RC networks can reproduce the low-frequency signature but are not unique microstructural proofs. An interface layer can also make dielectric loss strongly sensitive to electrode metal or annealing conditions.

**Primary relationship.** A serial dielectric stack has 1/Ctotal=Σi(1/Ci) for ideal planar sublayers. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **interfacial charge and maxwell–wagner response**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A high-κ ceramic pellet develops a massive low-frequency apparent εr only after adding one electrode material. Contrast electrode-controlled space charge with a grain-boundary polarization hypothesis using matched electrodes and thickness scaling.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Planar dielectric capacitance** as an exercise in numerical reasoning. Its controllable variable is **Insulator thickness**; all other quantities follow fixed assumptions. Set **Insulator thickness = 27 micrometers**. With the implemented expression `8.8541878188e-12*20*0.0001/(d*1e-6)*1e9`, the output is **0.655865764 nF**. Increase the control to **31.333333 micrometers**. The new output is **0.565160925 nF**. Thus the model output decreases over this interval, with secant slope **-0.0209318861 (nF)/(micrometers)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

A circuit-element fit is an interpretation framework, not a direct image of the real microstructure.

Begin with **spin-dependent magnetotransport**, and record **contact series resistance, field orientation, bias polarity, junction area and repeated field cycles**. Cross-check with **thickness-series junctions and noise spectroscopy** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Follow with a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **interfacial charge and maxwell–wagner response**, but **electrode polarization or leakage masquerading as permittivity** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **guarded broadband impedance and thickness scaling** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **interfacial charge and maxwell–wagner response** affects the distinction between **real permittivity versus loss and conduction**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.655865764 nF** and **0.565160925 nF** from the explicit expression for the stated two values of **Insulator thickness**. Report a unit-consistent slope in (nF)/(micrometers), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: A high-permittivity but lossy capacitor

### Diagnose the evidence, not just the material label

A pellet shows extraordinary low-frequency capacitance, while dissipation and electrode sensitivity complicate the interpretation. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Use the ideal geometric capacitance to identify an apparent εr and compare the Debye loss model with measured dispersion and thickness scaling. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Measure phase-corrected impedance at multiple frequencies and at two electrode metallizations, reporting confidence limits. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **electrode polarization or leakage masquerading as permittivity** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** A fitted dielectric relaxation time alone cannot establish an atomistic mechanism.

### Five capstone examination questions

