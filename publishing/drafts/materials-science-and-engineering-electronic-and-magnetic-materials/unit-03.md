# Unit 3: Ferroelectricity, piezoelectricity and domain physics

**Guiding research question:** What evidence distinguishes switchable spontaneous polarization from ordinary dielectric response and electromechanical motion?

## Physical context and experimental objectives

Ferroelectric order is a thermodynamic symmetry-breaking phenomenon with switchable spontaneous polarization under suitable conditions; a large dielectric constant alone is not proof. Piezoelectricity need not imply ferroelectric switching.

Processing-induced texture, dead layers, electrode work function and elastic clamping alter observed loops and strains. True polarization must be separated from leakage and parasitic capacitance.

The five lessons in this unit emphasize **switchable polar order and electromechanical coupling**. A central challenge is separating **reversible dielectric response versus remanent switching**, because both may appear as a single output on an instrument display. Before interpreting response, establish **thermal history, stress boundary, drive waveform and domain texture**. The most important rival explanation is **leakage charge or electrostatic actuation rather than switching**; an efficient validation strategy incorporates **PUND pulses, in-situ structural probes and frequency tests** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 3.1: Symmetry breaking and spontaneous polarization

### Microscopic picture and applicable constitutive law

Ferroelectricity requires a phase with a spontaneous electric polarization that can be switched by an accessible field under suitable conditions. A polar crystal can be pyroelectric without exhibiting demonstrable switching; every ferroelectric is polar but not every polar material is a practical ferroelectric. Structural symmetry and free-energy minima constrain whether the order is possible. Polarization loops alone are insufficient if mobile charge can mimic current integration.

**Primary relationship.** The Landau free-energy expansion F(P)=aP²/2+bP⁴/4−EP is illustrative near a transition. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **symmetry breaking and spontaneous polarization**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A thin oxide film displays a rectangular polarization–voltage trace. Require a structurally plausible polar phase and switching-current measurements that subtract non-switching leakage before naming the phase ferroelectric.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie–Weiss paraelectric permittivity** as an exercise in numerical reasoning. Its controllable variable is **Temperature above assumed Curie point**; all other quantities follow fixed assumptions. Set **Temperature above assumed Curie point = 486.11111 K**. With the implemented expression `5+80000/(T-400)`, the output is **934.032258 relative permittivity**. Increase the control to **516.66667 K**. The new output is **690.714286 relative permittivity**. Thus the model output decreases over this interval, with secant slope **-7.96313364 (relative permittivity)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Paraelectric branch, T > 400 K, phenomenological C=80,000 K and background 5; not valid through transition. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Mechanical clamping, electrode screening and nanoscale depolarizing fields can radically alter bulk behavior.

Perform a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Follow with a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **symmetry breaking and spontaneous polarization**, but **leakage charge or electrostatic actuation rather than switching** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **PUND pulses, in-situ structural probes and frequency tests** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **symmetry breaking and spontaneous polarization** affects the distinction between **reversible dielectric response versus remanent switching**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **934.032258 relative permittivity** and **690.714286 relative permittivity** from the explicit expression for the stated two values of **Temperature above assumed Curie point**. Report a unit-consistent slope in (relative permittivity)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **leakage charge or electrostatic actuation rather than switching** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **PUND pulses, in-situ structural probes and frequency tests** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_4 -->

## Lesson 3.2: Curie transitions and susceptibility

### Microscopic picture and applicable constitutive law

In a simple displacive ferroelectric, a temperature-dependent Landau coefficient can change sign and produce a spontaneous order parameter. Above a transition, a Curie–Weiss-like susceptibility is frequently used as a local phenomenological approximation. Real transitions can be first order, diffuse, relaxor-like or influenced by defects. The dielectric maximum is not automatically identical to a microscopic ordering temperature under all measurement conditions.

**Primary relationship.** A common phenomenological relation is χe≈C/(T−T0) above the specified transition region. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **curie transitions and susceptibility**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Measure ε′ and ε″ through a proposed transition at several frequencies. Compare the temperature of the peak, hysteresis on heating/cooling and an independent structural symmetry measurement.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Linear converse piezoelectric displacement** as an exercise in numerical reasoning. Its controllable variable is **Applied voltage**; all other quantities follow fixed assumptions. Set **Applied voltage = 16.666667 V**. With the implemented expression `0.2*V`, the output is **3.33333333 nm**. Increase the control to **22.222222 V**. The new output is **4.44444444 nm**. Thus the model output increases over this interval, with secant slope **0.2 (nm)/(V)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Unclamped longitudinal d33=200 pm/V, uniform field, quasistatic small-signal linear response; no domain switching or resonance. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Our Curie–Weiss slider represents only a T>Tc branch and diverges artificially when extrapolated to Tc.

Perform a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Follow with a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **curie transitions and susceptibility**, but **leakage charge or electrostatic actuation rather than switching** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **PUND pulses, in-situ structural probes and frequency tests** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **curie transitions and susceptibility** affects the distinction between **reversible dielectric response versus remanent switching**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **3.33333333 nm** and **4.44444444 nm** from the explicit expression for the stated two values of **Applied voltage**. Report a unit-consistent slope in (nm)/(V), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 3.3: Switching currents, domains and hysteresis loops

### Microscopic picture and applicable constitutive law

Polarization switching changes domain populations and generates transient charge. Integrating a total measured current also integrates leakage, injection and capacitive charging, so pulse protocols with nonswitching references are valuable. Coercive electric field depends on pulse width, defects, stress and thickness; it is not a geometry-independent universal constant. Domain imaging, structural changes and reproducible reversal establish a stronger evidence chain than loop shape alone.

**Primary relationship.** Measured electrode charge Q=∫I dt contains switched P·A plus nonswitching contributions. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **switching currents, domains and hysteresis loops**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A loop grows with slower measurement sweep. Predict whether leakage charge or slow domain nucleation is more likely, and test using positive-up-negative-down pulse sequences with independent voltage control.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie–Weiss paraelectric permittivity** as an exercise in numerical reasoning. Its controllable variable is **Temperature above assumed Curie point**; all other quantities follow fixed assumptions. Set **Temperature above assumed Curie point = 547.22222 K**. With the implemented expression `5+80000/(T-400)`, the output is **548.396226 relative permittivity**. Increase the control to **577.77778 K**. The new output is **455 relative permittivity**. Thus the model output decreases over this interval, with secant slope **-3.05660377 (relative permittivity)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Loops measured under breakdown or electrochemical drift are not evidence of stable ferroelectric memory operation.

Perform a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Follow with a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **switching currents, domains and hysteresis loops**, but **leakage charge or electrostatic actuation rather than switching** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **PUND pulses, in-situ structural probes and frequency tests** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **switching currents, domains and hysteresis loops** affects the distinction between **reversible dielectric response versus remanent switching**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **548.396226 relative permittivity** and **455 relative permittivity** from the explicit expression for the stated two values of **Temperature above assumed Curie point**. Report a unit-consistent slope in (relative permittivity)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 3.4: Direct and converse piezoelectric coefficients

### Microscopic picture and applicable constitutive law

Piezoelectrics couple stress and electrical displacement, or electric field and strain, under specific mechanical and electrical boundary conditions. The effective d33 of a bonded thin film need not equal the free crystal coefficient because a substrate constrains transverse strain. Resonance magnifies motion and changes phase, invalidating simple quasi-static displacement estimates. A linear piezo response does not establish remanent ferroelectric order.

**Primary relationship.** A free small-signal slab obeys ΔL≈d33V for uniform field along its poling direction. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **direct and converse piezoelectric coefficients**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A cantilever actuator produces more displacement after thinning the substrate. Distinguish a change in intrinsic d33 from altered bending stiffness and neutral-axis geometry before interpreting the signal as improved material coupling.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Linear converse piezoelectric displacement** as an exercise in numerical reasoning. Its controllable variable is **Applied voltage**; all other quantities follow fixed assumptions. Set **Applied voltage = 27.777778 V**. With the implemented expression `0.2*V`, the output is **5.55555556 nm**. Increase the control to **33.333333 V**. The new output is **6.66666667 nm**. Thus the model output increases over this interval, with secant slope **0.2 (nm)/(V)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Report drive waveform, clamping, field amplitude and frequency with every measured coefficient.

Perform a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Follow with a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **direct and converse piezoelectric coefficients**, but **leakage charge or electrostatic actuation rather than switching** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **PUND pulses, in-situ structural probes and frequency tests** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **direct and converse piezoelectric coefficients** affects the distinction between **reversible dielectric response versus remanent switching**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **5.55555556 nm** and **6.66666667 nm** from the explicit expression for the stated two values of **Applied voltage**. Report a unit-consistent slope in (nm)/(V), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_5 -->

## Lesson 3.5: Domain-wall motion, fatigue and retention

### Microscopic picture and applicable constitutive law

Defects can pin polar domain walls, lowering reversible susceptibility or requiring stronger switching fields. Repeated cycling may alter oxygen vacancy distributions, trapped charge or interface chemistry; both fatigue and apparent wake-up are processing-dependent. Retention reflects long-term stability at a given temperature and electric field, not merely the existence of one completed switching loop. Reliability data must include many independently fabricated devices and clear fail thresholds.

**Primary relationship.** A cycle-dependent remanent polarization Pr(N) is empirical; no universal single-exponential law applies. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **domain-wall motion, fatigue and retention**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A device switches successfully ten times, then seems to lose polarization. Compare direct switch-current records, leakage-corrected signals and post-cycle structural results; one explanation may be electrode degradation rather than domain exhaustion.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie–Weiss paraelectric permittivity** as an exercise in numerical reasoning. Its controllable variable is **Temperature above assumed Curie point**; all other quantities follow fixed assumptions. Set **Temperature above assumed Curie point = 608.33333 K**. With the implemented expression `5+80000/(T-400)`, the output is **389 relative permittivity**. Increase the control to **638.88889 K**. The new output is **339.883721 relative permittivity**. Thus the model output decreases over this interval, with secant slope **-1.60744186 (relative permittivity)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Accelerated tests require a defensible extrapolation model and cannot prove decade-long retention from a short test.

Begin with **cross-sectional transmission electron microscopy**, and record **sample preparation damage, oxide continuity, interdiffusion and field of view**. Cross-check with **X-ray reflectivity or scanning-probe measurements** rather than repeating the same calculation in a different plotting package. Because these methods probe different degrees of freedom, agreement under matched conditions raises confidence but need not provide a unique mechanism. For instance, a static electrical measurement may reflect a thin interface while magnetometry averages the entire specimen volume; an impedance-derived relaxation time may combine real dipole motion and electrode polarization. Independently calibrate the original instrument before attributing a disagreement to the specimen.

Perform a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Follow with a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **domain-wall motion, fatigue and retention**, but **leakage charge or electrostatic actuation rather than switching** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **PUND pulses, in-situ structural probes and frequency tests** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **domain-wall motion, fatigue and retention** affects the distinction between **reversible dielectric response versus remanent switching**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **389 relative permittivity** and **339.883721 relative permittivity** from the explicit expression for the stated two values of **Temperature above assumed Curie point**. Report a unit-consistent slope in (relative permittivity)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: Ferroelectric actuator or leaking capacitor?

### Diagnose the evidence, not just the material label

A nanoscale polar film shows a large loop and a strain signal, but its switching current may include injection and the displacement could come from electrostatic deflection. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Analyze the Curie–Weiss teaching relation above the supposed transition and a bounded small-signal piezoelectric estimate. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Use PUND, field reversal, interferometric strain and phase-sensitive structural tests on matched specimens. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **leakage charge or electrostatic actuation rather than switching** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** High apparent strain does not by itself prove an intrinsic piezoelectric coefficient.

### Five capstone examination questions

