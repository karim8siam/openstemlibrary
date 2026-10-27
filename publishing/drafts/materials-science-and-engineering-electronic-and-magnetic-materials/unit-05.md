# Unit 5: Soft magnets, permanent magnets and dynamic loss

**Guiding research question:** Which energy terms determine core efficiency, magnetic memory and permanent-magnet performance?

## Physical context and experimental objectives

Soft magnets minimize unwanted hysteretic and dynamic loss while hard magnets maintain useful remanence and coercivity. Neither classification corresponds to a single material constant independent of geometry, frequency and microstructure.

A loop measured slowly is not necessarily representative of a driven motor or transformer. Eddy currents and domain-wall dynamics create amplitude- and frequency-dependent heating.

The five lessons in this unit emphasize **energy losses, anisotropy and engineering permanent magnets**. A central challenge is separating **coercive field versus intrinsic anisotropy or remanence**, because both may appear as a single output on an instrument display. Before interpreting response, establish **grain texture, wall pinning, drive rate, stress and waveform**. The most important rival explanation is **eddy loss, porosity or a different reversal mode**; an efficient validation strategy incorporates **minor-loop tests, microstructure imaging and dynamic core loss** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 5.1: Soft-magnetic permeability and domain-wall mobility

### Microscopic picture and applicable constitutive law

A soft magnetic material is chosen for large reversible magnetization and low coercive losses under an operating waveform. Permeability can be initial, incremental, differential or effective, and each definition has distinct experimental significance. Grain size, residual stress and insulating intergranular layers shape wall motion and high-frequency performance. High low-frequency permeability does not imply low core loss at switching frequencies.

**Primary relationship.** Small-signal permeability refers to dB/dH under specified bias and measurement conditions. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **soft-magnetic permeability and domain-wall mobility**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A motor designer compares two alloys by a single reported μr. Require B–H loops at matching flux amplitude and frequency, plus measured loss and saturation behavior to rank them for the intended duty cycle.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Lamination eddy-current loss proxy** as an exercise in numerical reasoning. Its controllable variable is **Frequency**; all other quantities follow fixed assumptions. Set **Frequency = 705.55556 Hz**. With the implemented expression `Math.pow(f/1000,2)`, the output is **0.497808642 normalized**. Increase the control to **1033.3333 Hz**. The new output is **1.06777778 normalized**. Thus the model output increases over this interval, with secant slope **0.00173888889 (normalized)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Reference unity at 1 kHz; Peddy ∝ f² for constant flux amplitude, thickness, resistivity and waveform. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Permeability diverges from constant values near saturation and can vary greatly after mechanical forming.

Perform a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Follow with a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **soft-magnetic permeability and domain-wall mobility**, but **eddy loss, porosity or a different reversal mode** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **minor-loop tests, microstructure imaging and dynamic core loss** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **soft-magnetic permeability and domain-wall mobility** affects the distinction between **coercive field versus intrinsic anisotropy or remanence**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.497808642 normalized** and **1.06777778 normalized** from the explicit expression for the stated two values of **Frequency**. Report a unit-consistent slope in (normalized)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **eddy loss, porosity or a different reversal mode** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **minor-loop tests, microstructure imaging and dynamic core loss** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_8 -->

## Lesson 5.2: Eddy currents, laminations and frequency scaling

### Microscopic picture and applicable constitutive law

A time-varying magnetic flux induces electric fields and circulating currents in conductive cores. The resulting Joule heating depends strongly on lamination thickness, conductivity, flux amplitude, waveform and frequency. Thin insulated sheets can suppress cross-sectional current loops; ferrites achieve high electrical resistivity but often lower saturation flux density. An ideal f² scaling model is a screening tool, not a universal total-loss model.

**Primary relationship.** In a classical thin-sheet limit, Peddy/V ∝ Bpeak² f² t²/ρ. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **eddy currents, laminations and frequency scaling**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A transformer core heats at high switching frequency. Vary sheet thickness with matched B amplitude and inspect whether loss follows the expected squared thickness dependence rather than assuming all heat comes from hysteresis.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Uniaxial anisotropy field** as an exercise in numerical reasoning. Its controllable variable is **Anisotropy energy density**; all other quantities follow fixed assumptions. Set **Anisotropy energy density = 173333.33 J/m³**. With the implemented expression `2*K/(1.25663706127e-06*1000000)/1000`, the output is **275.868568 kA/m**. Increase the control to **227777.78 J/m³**. The new output is **362.519593 kA/m**. Thus the model output increases over this interval, with secant slope **0.00159154943 (kA/m)/(J/m³)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Coherent rotation estimate with Ms=10^6 A/m; neglects reversal nucleation, multidomains and defects. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Strong skin effects, nonsinusoidal flux and domain-wall excess loss invalidate the simplest quadratic scaling.

Perform a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Follow with a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **eddy currents, laminations and frequency scaling**, but **eddy loss, porosity or a different reversal mode** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **minor-loop tests, microstructure imaging and dynamic core loss** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **eddy currents, laminations and frequency scaling** affects the distinction between **coercive field versus intrinsic anisotropy or remanence**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **275.868568 kA/m** and **362.519593 kA/m** from the explicit expression for the stated two values of **Anisotropy energy density**. Report a unit-consistent slope in (kA/m)/(J/m³), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 5.3: Coercivity, remanence and maximum energy product

### Microscopic picture and applicable constitutive law

Hard magnetic performance depends on maintaining magnetization against opposing fields and temperature. The useful second-quadrant demagnetization curve determines maximum (BH) energy product, subject to geometry and loading. High coercivity alone does not ensure high remanence, density or temperature stability; a high-energy magnet needs favorable combinations. Grain boundaries and crystallographic texture influence both reversal and average magnetization.

**Primary relationship.** Magnetic energy-product screening maximizes |B·H| in the second quadrant of the relevant loop. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **coercivity, remanence and maximum energy product**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Compare two permanent magnets with equal coercivity but different remanence. Plot their second-quadrant B–H curves and evaluate a load line before concluding which one provides a stronger working field.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Lamination eddy-current loss proxy** as an exercise in numerical reasoning. Its controllable variable is **Frequency**; all other quantities follow fixed assumptions. Set **Frequency = 1361.1111 Hz**. With the implemented expression `Math.pow(f/1000,2)`, the output is **1.85262346 normalized**. Increase the control to **1688.8889 Hz**. The new output is **2.85234568 normalized**. Thus the model output increases over this interval, with secant slope **0.00305 (normalized)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Quoted BHmax values assume a particular measurement temperature and do not determine every assembly’s working point.

Perform a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Follow with a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **coercivity, remanence and maximum energy product**, but **eddy loss, porosity or a different reversal mode** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **minor-loop tests, microstructure imaging and dynamic core loss** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **coercivity, remanence and maximum energy product** affects the distinction between **coercive field versus intrinsic anisotropy or remanence**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **1.85262346 normalized** and **2.85234568 normalized** from the explicit expression for the stated two values of **Frequency**. Report a unit-consistent slope in (normalized)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 5.4: Micromagnetics and reversal modes

### Microscopic picture and applicable constitutive law

Magnetic energy includes exchange, anisotropy, magnetostatic and Zeeman terms. Reversal may proceed through coherent rotation, curling, wall nucleation or pinning, depending on dimensions and defects. A coherent-rotation anisotropy field offers an upper benchmark for idealized cases, but measured coercive fields may be substantially smaller. Micromagnetic simulation demands mesh resolution below relevant exchange-length scales and credible boundary conditions.

**Primary relationship.** Ideal uniaxial anisotropy field Hk=2K/(μ0Ms), not generally equal to Hc. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **micromagnetics and reversal modes**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A small grain has a coercive field much below a calculated anisotropy field. Test whether multidomain reversal or surface nucleation is responsible through angular switching measurements and spatial imaging.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Uniaxial anisotropy field** as an exercise in numerical reasoning. Its controllable variable is **Anisotropy energy density**; all other quantities follow fixed assumptions. Set **Anisotropy energy density = 282222.22 J/m³**. With the implemented expression `2*K/(1.25663706127e-06*1000000)/1000`, the output is **449.170617 kA/m**. Increase the control to **336666.67 J/m³**. The new output is **535.821642 kA/m**. Thus the model output increases over this interval, with secant slope **0.00159154943 (kA/m)/(J/m³)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

A scalar single-domain formula cannot capture interacting grains, multidomain walls or complex sample geometry.

Perform a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Follow with a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **micromagnetics and reversal modes**, but **eddy loss, porosity or a different reversal mode** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **minor-loop tests, microstructure imaging and dynamic core loss** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **micromagnetics and reversal modes** affects the distinction between **coercive field versus intrinsic anisotropy or remanence**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **449.170617 kA/m** and **535.821642 kA/m** from the explicit expression for the stated two values of **Anisotropy energy density**. Report a unit-consistent slope in (kA/m)/(J/m³), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_9 -->

## Lesson 5.5: Magnetic heating and application-specific qualification

### Microscopic picture and applicable constitutive law

Core efficiency requires energy lost per cycle and repetition frequency, with separate hysteretic, eddy-current and excess-loss mechanisms where appropriate. Static loops alone miss rate dependence. Mechanical vibration and magnetostriction can also create audible noise and fatigue. A correct qualification plan measures actual temperature rise in representative cooling conditions and an electrical waveform that reflects the end application.

**Primary relationship.** For a measured B–H loop, loss density per cycle is ∮H dB; average power density is f∮H dB. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **magnetic heating and application-specific qualification**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

An inductor passes a quasistatic B–H test but overheats in a converter. Record high-frequency loop area, harmonic spectrum and temperature, then compare calorimetric loss with the integrated loop.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Lamination eddy-current loss proxy** as an exercise in numerical reasoning. Its controllable variable is **Frequency**; all other quantities follow fixed assumptions. Set **Frequency = 2016.6667 Hz**. With the implemented expression `Math.pow(f/1000,2)`, the output is **4.06694444 normalized**. Increase the control to **2344.4444 Hz**. The new output is **5.49641975 normalized**. Thus the model output increases over this interval, with secant slope **0.00436111111 (normalized)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Operating flux waveforms and cooling conditions must be fixed before applying catalog core-loss figures.

Perform a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Follow with a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **magnetic heating and application-specific qualification**, but **eddy loss, porosity or a different reversal mode** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **minor-loop tests, microstructure imaging and dynamic core loss** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **magnetic heating and application-specific qualification** affects the distinction between **coercive field versus intrinsic anisotropy or remanence**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **4.06694444 normalized** and **5.49641975 normalized** from the explicit expression for the stated two values of **Frequency**. Report a unit-consistent slope in (normalized)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: Transformer core under converter operation

### Diagnose the evidence, not just the material label

A soft magnetic core meets static permeability requirements but heats abnormally when driven by high-frequency pulses. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Test the normalized eddy loss scaling and benchmark the anisotropy field without mistaking either for total dissipated power. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Use waveform-resolved H and B measurements, temperature stabilization and independent calorimetry. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **eddy loss, porosity or a different reversal mode** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** Avoid applying a sine-wave catalog rating to an unmeasured PWM waveform.

### Five capstone examination questions

