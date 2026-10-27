# Unit 4: Magnetic moments, exchange and domains

**Guiding research question:** How do atomic magnetic moments and collective order appear in macroscopic measurements?

## Physical context and experimental objectives

Magnetic response emerges from electron spin, orbital moment, exchange interactions, anisotropy and microstructure. A response function at a fixed temperature does not identify whether moments are correlated or independently fluctuating.

Magnetization M has units A/m, field H has units A/m, and induction B has units T; mixing them can create order-of-magnitude errors in magnetic-circuit analysis.

The five lessons in this unit emphasize **local moments, collective exchange and magnetic domains**. A central challenge is separating **applied magnetic H versus induction B and magnetization M**, because both may appear as a single output on an instrument display. Before interpreting response, establish **temperature, geometry, orientation and chemical disorder**. The most important rival explanation is **Curie impurity tail, demagnetization or secondary magnetic phase**; an efficient validation strategy incorporates **field- and temperature-dependent magnetometry with phase analysis** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 4.1: Spin, orbital contributions and the Bohr magneton

### Microscopic picture and applicable constitutive law

Electron magnetic moments originate from spin and orbital angular momentum, modified by crystal fields and spin–orbit coupling. The Bohr magneton supplies an atomic energy scale but does not mean every ion has a one-Bohr-magneton moment. Magnetic susceptibility is the differential response under defined conditions; it cannot alone reveal the distribution of local moments. In materials with strong correlations, the number and state of unpaired electrons also depend on temperature and chemistry.

**Primary relationship.** For one moment magnitude μ, a field interaction has energy scale |ΔU|≈μB. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **spin, orbital contributions and the bohr magneton**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Compare a magnetic salt and a nonmagnetic host containing trace paramagnetic impurities. Use magnetization against field and temperature to separate a smooth host background from a low-temperature Curie tail.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie paramagnetic susceptibility** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 188.88889 K**. With the implemented expression `1.5/T`, the output is **0.00794117647 dimensionless**. Increase the control to **233.33333 K**. The new output is **0.00642857143 dimensionless**. Thus the model output decreases over this interval, with secant slope **-3.40336134e-05 (dimensionless)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Noninteracting paramagnetic limit χ=C/T with assumed C=1.5 K; no Curie–Weiss offset. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Magnetic moment measured for a specimen is not the same thing as magnetization per unit volume or mass.

Perform a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Follow with a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **spin, orbital contributions and the bohr magneton**, but **Curie impurity tail, demagnetization or secondary magnetic phase** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **field- and temperature-dependent magnetometry with phase analysis** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **spin, orbital contributions and the bohr magneton** affects the distinction between **applied magnetic H versus induction B and magnetization M**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.00794117647 dimensionless** and **0.00642857143 dimensionless** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (dimensionless)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **Curie impurity tail, demagnetization or secondary magnetic phase** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **field- and temperature-dependent magnetometry with phase analysis** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_6 -->

## Lesson 4.2: Diamagnetism, paramagnetism and susceptibility

### Microscopic picture and applicable constitutive law

Diamagnetic induction opposes an applied field and typically gives small negative susceptibility, whereas ideal paramagnetism aligns fluctuating independent moments and gives positive susceptibility. Ferromagnetism involves collective order; therefore a susceptibility curve should not be classified from its sign alone. Temperature-invariant backgrounds, holders and impurity tails must be subtracted cautiously. A Curie law is a limiting high-temperature approximation rather than a proof of noninteracting spins.

**Primary relationship.** The simplest Curie-law susceptibility is χ=C/T for weak fields and independent moments. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **diamagnetism, paramagnetism and susceptibility**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Plot χT and χ versus T for a dilute magnetic specimen. Predict how a simple Curie response differs from a Curie–Weiss fit and plan an impurity assay to test whether the tail is extrinsic.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Single Bohr-magneton Zeeman energy** as an exercise in numerical reasoning. Its controllable variable is **Flux density**; all other quantities follow fixed assumptions. Set **Flux density = 1.7333333 T**. With the implemented expression `9.2740100657e-24/(1.602176634e-19*1e-3)*B`, the output is **0.100331951 meV**. Increase the control to **2.2777778 T**. The new output is **0.131846474 meV**. Thus the model output increases over this interval, with secant slope **0.057883818 (meV)/(T)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Absolute energy μ_B B for magnitude of one Bohr magneton; spin orientation and g factors not included. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

High-field saturation and nonlinear Brillouin response fall outside a small-field Curie model.

Perform a **evidence independence audit**: Do not mistake repeated sweeps of the same specimen for independent fabrication replicates; include calibration controls. Follow with a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **diamagnetism, paramagnetism and susceptibility**, but **Curie impurity tail, demagnetization or secondary magnetic phase** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **field- and temperature-dependent magnetometry with phase analysis** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **diamagnetism, paramagnetism and susceptibility** affects the distinction between **applied magnetic H versus induction B and magnetization M**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.100331951 meV** and **0.131846474 meV** from the explicit expression for the stated two values of **Flux density**. Report a unit-consistent slope in (meV)/(T), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 4.3: Exchange, ferro- and antiferromagnetic order

### Microscopic picture and applicable constitutive law

Exchange energy depends on quantum-mechanical electronic structure and can favor parallel or antiparallel neighboring moments. A ferromagnet has net aligned moments at equilibrium, while a compensated antiferromagnet may have little net moment despite strong microscopic order. Ferrimagnets contain unequal opposing sublattices and can show compensation temperatures. Bulk magnetometry is therefore insufficient for distinguishing all ordering patterns.

**Primary relationship.** A common model is H=−Σij Jij Si·Sj, with sign convention stated explicitly. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **exchange, ferro- and antiferromagnetic order**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A specimen shows near-zero moment below an anomaly. Compare a truly nonmagnetic phase with a compensated antiferromagnet using temperature dependence, magnetic diffraction or element-resolved probes.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie paramagnetic susceptibility** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 277.77778 K**. With the implemented expression `1.5/T`, the output is **0.0054 dimensionless**. Increase the control to **322.22222 K**. The new output is **0.00465517241 dimensionless**. Thus the model output decreases over this interval, with secant slope **-1.67586207e-05 (dimensionless)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

The Heisenberg Hamiltonian is simplified and exchange constants are not generally transferable across compositions.

Perform a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Follow with a **sample provenance audit**: Separate nominal composition from independently measured chemistry, phase fraction, texture and prior cycling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **exchange, ferro- and antiferromagnetic order**, but **Curie impurity tail, demagnetization or secondary magnetic phase** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **field- and temperature-dependent magnetometry with phase analysis** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **exchange, ferro- and antiferromagnetic order** affects the distinction between **applied magnetic H versus induction B and magnetization M**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.0054 dimensionless** and **0.00465517241 dimensionless** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (dimensionless)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 4.4: Demagnetizing fields and sample shape

### Microscopic picture and applicable constitutive law

The magnetic field inside a finite specimen differs from the applied field because its own magnetization creates a demagnetizing contribution. For ellipsoids in a uniform approximation, Hint=Happlied−NM with geometry-dependent N. A long slender rod along its axis and a thin plate normal to its surface have markedly different apparent loop shapes even when they contain the same intrinsic material. Reporting an uncorrected coercivity without orientation and shape can mislead comparisons.

**Primary relationship.** In SI, B=μ0(H+M), with H and M in A/m and B in tesla. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **demagnetizing fields and sample shape**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Measure the same magnetic composition in a long rod and disk. Predict the different apparent approach to saturation using demagnetizing factors, then test whether intrinsic anisotropy extracted after correction agrees.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Single Bohr-magneton Zeeman energy** as an exercise in numerical reasoning. Its controllable variable is **Flux density**; all other quantities follow fixed assumptions. Set **Flux density = 2.8222222 T**. With the implemented expression `9.2740100657e-24/(1.602176634e-19*1e-3)*B`, the output is **0.163360997 meV**. Increase the control to **3.3666667 T**. The new output is **0.194875521 meV**. Thus the model output increases over this interval, with secant slope **0.057883818 (meV)/(T)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

For irregular components N is spatially variable and a single scalar correction is usually an approximation.

Perform a **geometry and boundary conditions audit**: Specify electrode area, film thickness, test shape, magnetic demagnetization, substrate stress and edge effects. Follow with a **units and constitutive definitions audit**: Check E in V/m, D and P in C/m², H and M in A/m, and B in T; declare SI and any conversions. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **demagnetizing fields and sample shape**, but **Curie impurity tail, demagnetization or secondary magnetic phase** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **field- and temperature-dependent magnetometry with phase analysis** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **demagnetizing fields and sample shape** affects the distinction between **applied magnetic H versus induction B and magnetization M**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.163360997 meV** and **0.194875521 meV** from the explicit expression for the stated two values of **Flux density**. Report a unit-consistent slope in (meV)/(T), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_7 -->

## Lesson 4.5: Anisotropy, magnetostriction and domain walls

### Microscopic picture and applicable constitutive law

Crystal symmetry, shape, interfaces and stress determine preferred magnetization directions. Magnetostriction couples magnetic order to mechanical strain, while reciprocal stress changes magnetic anisotropy. Domains reduce magnetostatic energy but introduce wall energies and pinning barriers, producing hysteresis. The measured coercive field is controlled by how reversal begins and propagates, not only by the magnitude of a tabulated anisotropy constant.

**Primary relationship.** For uniaxial coherent rotation, μ0Hk≈2K/Ms under the model assumptions. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **anisotropy, magnetostriction and domain walls**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Rotate a single-crystal sample through the same magnetic field while recording torque. Compare the anisotropy signature with a polycrystal and test whether mechanical stress changes the easy direction.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Curie paramagnetic susceptibility** as an exercise in numerical reasoning. Its controllable variable is **Absolute temperature**; all other quantities follow fixed assumptions. Set **Absolute temperature = 366.66667 K**. With the implemented expression `1.5/T`, the output is **0.00409090909 dimensionless**. Increase the control to **411.11111 K**. The new output is **0.00364864865 dimensionless**. Thus the model output decreases over this interval, with secant slope **-9.95085995e-06 (dimensionless)/(K)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

A coherent-rotation estimate often overpredicts practical reversal fields because real samples nucleate domains.

Perform a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Follow with a **frequency and waveform audit**: Keep track of angular frequency versus hertz, drive amplitude, phase convention, rate dependence and transient settling. Note each control variable on the data sheet. Compare specimens fabricated independently rather than mistaking repeated sweeps of one piece for proof of reproducibility. Record the observed distribution, not just the best individual device or highest signal; the weak tail can determine whether a material is useful. Do not assign imaginary experimental error bars to formula-generated teaching points.

### Counterfactual and model criticism

Suppose a measurement appears to support **anisotropy, magnetostriction and domain walls**, but **Curie impurity tail, demagnetization or secondary magnetic phase** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **field- and temperature-dependent magnetometry with phase analysis** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **anisotropy, magnetostriction and domain walls** affects the distinction between **applied magnetic H versus induction B and magnetization M**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **0.00409090909 dimensionless** and **0.00364864865 dimensionless** from the explicit expression for the stated two values of **Absolute temperature**. Report a unit-consistent slope in (dimensionless)/(K), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: An anomalous low-temperature magnetic response

### Diagnose the evidence, not just the material label

A newly synthesized oxide shows a small low-temperature moment, but the sample could have dilute impurities, canting or an unsuspected ferrimagnetic secondary phase. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Calculate the simple Curie trend and the Zeeman energy scale, then determine which effects require collective ordering measurements. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Measure zero-field-cooled and field-cooled curves, element-sensitive phase composition and directional loops. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **Curie impurity tail, demagnetization or secondary magnetic phase** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** One magnetization anomaly is insufficient to establish a new ordered phase.

### Five capstone examination questions

