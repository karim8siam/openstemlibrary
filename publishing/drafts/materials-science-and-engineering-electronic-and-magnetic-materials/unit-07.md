# Unit 7: Interfaces, functional oxides and coupled phenomena

**Guiding research question:** How do heterointerfaces and competing ferroic orders control nanoscale functionality?

## Physical context and experimental objectives

Heterostructures can combine ferromagnets, antiferromagnets, tunnel oxides and functional dielectrics, but each interface introduces chemical and structural variables. A nominal thickness is rarely enough to predict device yield.

Exchange bias can depend on cooling history and cycling, and resistive switching can arise from ionic motion rather than the intended coupled-order mechanism.

The five lessons in this unit emphasize **heterointerfaces, oxides and coupled order**. A central challenge is separating **intrinsic interface coupling versus extrinsic sample artifacts**, because both may appear as a single output on an instrument display. Before interpreting response, establish **roughness, layer thickness, oxidation and training history**. The most important rival explanation is **interdiffusion, pinholes or trapped charge**; an efficient validation strategy incorporates **cross-sectional microscopy and matched interface controls** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 7.1: Thin-film strain, texture and interface reconstruction

### Microscopic picture and applicable constitutive law

Film growth on a substrate introduces lattice mismatch, thermal contraction mismatch, nucleation textures and interface chemistry that alter electric and magnetic order. The nominal target composition may differ from a film after oxygen exchange or volatile-element loss. Strain can favor phases unavailable in bulk, but relaxation defects accumulate with thickness. Comparing different films requires matching actual composition, texture and residual stress rather than deposition settings alone.

**Primary relationship.** For a thin coherent cubic film, approximate mismatch f=(afilm−asubstrate)/asubstrate. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **thin-film strain, texture and interface reconstruction**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Two oxide films show different magnetic anisotropy although deposited with nominally equal recipes. Combine diffraction reciprocal-space maps, oxygen-sensitive analysis and thickness control to separate elastic strain from stoichiometry.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetic tunnel junction area resistance** as an exercise in numerical reasoning. Its controllable variable is **Nominal insulating barrier thickness**; all other quantities follow fixed assumptions. Set **Nominal insulating barrier thickness = 0.91111111 nm**. With the implemented expression `10*Math.exp(1.5*(t-1))`, the output is **8.75173319 ohm micrometer²**. Increase the control to **1.0666667 nm**. The new output is **11.0517092 ohm micrometer²**. Thus the model output increases over this interval, with secant slope **14.7855599 (ohm micrometer²)/(nm)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Phenomenological RA(1 nm)=10 Ω μm² and β=1.5 nm⁻¹; does not represent a certified stack. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Interdiffusion, dislocations and chemical valence shifts can produce similar electrical signatures.

### Counterfactual and model criticism

Suppose a measurement appears to support **thin-film strain, texture and interface reconstruction**, but **interdiffusion, pinholes or trapped charge** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **cross-sectional microscopy and matched interface controls** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **thin-film strain, texture and interface reconstruction** affects the distinction between **intrinsic interface coupling versus extrinsic sample artifacts**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **8.75173319 ohm micrometer²** and **11.0517092 ohm micrometer²** from the explicit expression for the stated two values of **Nominal insulating barrier thickness**. Report a unit-consistent slope in (ohm micrometer²)/(nm), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **interdiffusion, pinholes or trapped charge** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **cross-sectional microscopy and matched interface controls** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_12 -->

## Lesson 7.2: Exchange bias at ferro-antiferromagnet interfaces

### Microscopic picture and applicable constitutive law

When an antiferromagnetic layer couples to a ferromagnet, a shifted magnetic hysteresis loop may appear after suitable magnetic and thermal history. Exchange bias arises from interfacial spin arrangements and can decay over repeated cycling, a training effect. A simple interfacial energy divided by ferromagnetic moment per area estimates the bias field, but roughness, uncompensated spins and multiple domains complicate the result.

**Primary relationship.** Nominal Hex≈Jint/(μ0 Ms tFM) under a simplified exchange-bias energy model. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **exchange bias at ferro-antiferromagnet interfaces**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A heterostructure shows a loop shift after field cooling. Reverse the cooling field, run successive loops and compare with a nonmagnetic control interface to test whether exchange coupling is responsible.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Simplified exchange-bias field** as an exercise in numerical reasoning. Its controllable variable is **Interface coupling energy**; all other quantities follow fixed assumptions. Set **Interface coupling energy = 0.2 mJ/m²**. With the implemented expression `(J*1e-3)/(1.25663706127e-06*800000*10e-9)/1000`, the output is **19.8943679 kA/m**. Increase the control to **0.25 mJ/m²**. The new output is **24.8679599 kA/m**. Thus the model output increases over this interval, with secant slope **99.4718394 (kA/m)/(mJ/m²)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Nominal Ms=800 kA/m and ferromagnet thickness 10 nm, ideal single interfacial coupling; no training or nonuniform exchange. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

Exchange bias cannot be inferred from coercivity enhancement alone and varies with test temperature.

### Counterfactual and model criticism

Suppose a measurement appears to support **exchange bias at ferro-antiferromagnet interfaces**, but **interdiffusion, pinholes or trapped charge** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **cross-sectional microscopy and matched interface controls** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **exchange bias at ferro-antiferromagnet interfaces** affects the distinction between **intrinsic interface coupling versus extrinsic sample artifacts**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **19.8943679 kA/m** and **24.8679599 kA/m** from the explicit expression for the stated two values of **Interface coupling energy**. Report a unit-consistent slope in (kA/m)/(mJ/m²), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 7.3: Magnetic tunnel barriers and interface spin filtering

### Microscopic picture and applicable constitutive law

Spin-dependent tunnel transport depends exponentially on barrier thickness in simple pictures. Interface crystallinity, orbital symmetry and local oxidation state can determine transmission more strongly than a bulk electrode spin-polarization number. A thin pinhole can dominate current despite excellent average barrier quality. Reporting the resistance–area product is essential to distinguish changes in device area from changes in barrier properties.

**Primary relationship.** A schematic tunnel law is RA(t)=RA0 exp[β(t−t0)] for a specified stack. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **magnetic tunnel barriers and interface spin filtering**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A 0.2 nm nominal barrier increase raises RA sharply. Verify barrier continuity by microscopy and map short-circuit yield across many junction sizes before fitting an exponential and claiming coherent tunneling.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetic tunnel junction area resistance** as an exercise in numerical reasoning. Its controllable variable is **Nominal insulating barrier thickness**; all other quantities follow fixed assumptions. Set **Nominal insulating barrier thickness = 1.2222222 nm**. With the implemented expression `10*Math.exp(1.5*(t-1))`, the output is **13.9561243 ohm micrometer²**. Increase the control to **1.3777778 nm**. The new output is **17.6238264 ohm micrometer²**. Thus the model output increases over this interval, with secant slope **23.5780853 (ohm micrometer²)/(nm)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Real RA scaling may change with bias, defect-mediated transport, barrier height and junction perimeter.

### Counterfactual and model criticism

Suppose a measurement appears to support **magnetic tunnel barriers and interface spin filtering**, but **interdiffusion, pinholes or trapped charge** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **cross-sectional microscopy and matched interface controls** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **magnetic tunnel barriers and interface spin filtering** affects the distinction between **intrinsic interface coupling versus extrinsic sample artifacts**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **13.9561243 ohm micrometer²** and **17.6238264 ohm micrometer²** from the explicit expression for the stated two values of **Nominal insulating barrier thickness**. Report a unit-consistent slope in (ohm micrometer²)/(nm), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 7.4: Multiferroics and magnetoelectric effects

### Microscopic picture and applicable constitutive law

A multiferroic contains multiple primary ferroic order parameters in one phase, while engineered composites can couple separate piezoelectric and magnetostrictive materials. Magnetoelectric response should be described by a clearly defined derivative under mechanical and electromagnetic boundary conditions. Apparent electrically controlled magnetization may instead arise from Joule heating, electromigration or electrochemical valence changes. Device-level coupling requires evidence of reversible, non-destructive control.

**Primary relationship.** A linear response may be written P=αH under a carefully stated boundary convention. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **multiferroics and magnetoelectric effects**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

An oxide interface changes magnetic resistance under gate voltage. Compare gate-current transients, temperature rise and a mechanically matched control to distinguish charge accumulation from redox-mediated chemistry.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Simplified exchange-bias field** as an exercise in numerical reasoning. Its controllable variable is **Interface coupling energy**; all other quantities follow fixed assumptions. Set **Interface coupling energy = 0.3 mJ/m²**. With the implemented expression `(J*1e-3)/(1.25663706127e-06*800000*10e-9)/1000`, the output is **29.8415518 kA/m**. Increase the control to **0.35 mJ/m²**. The new output is **34.8151438 kA/m**. Thus the model output increases over this interval, with secant slope **99.4718394 (kA/m)/(mJ/m²)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Magnetoelectric coefficients use different conventions; report definition, geometry, units and bias.

### Counterfactual and model criticism

Suppose a measurement appears to support **multiferroics and magnetoelectric effects**, but **interdiffusion, pinholes or trapped charge** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **cross-sectional microscopy and matched interface controls** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **multiferroics and magnetoelectric effects** affects the distinction between **intrinsic interface coupling versus extrinsic sample artifacts**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **29.8415518 kA/m** and **34.8151438 kA/m** from the explicit expression for the stated two values of **Interface coupling energy**. Report a unit-consistent slope in (kA/m)/(mJ/m²), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_13 -->

## Lesson 7.5: Defect chemistry, aging and coupled reliability

### Microscopic picture and applicable constitutive law

Charged point defects, grain boundaries and interfaces link dielectric conduction, magnetic anisotropy and thermal stability. Oxygen vacancies can modify leakage and magnetism, so a single processing change has multiple plausible explanations. Humidity, field cycling and thermal stress can shift interface barrier heights or magnetic pinning populations. Screening a new coupled functionality should include degradation mechanisms that occur without obvious early failures.

**Primary relationship.** A time-dependent parameter drift must be reported as a distribution conditioned on storage and drive history. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **defect chemistry, aging and coupled reliability**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

After accelerated aging, a magnetic tunnel stack loses MR while its resistance increases. Distinguish barrier oxidation, metallic interdiffusion and magnetic anisotropy changes using structural and electrical comparisons with unaged controls.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetic tunnel junction area resistance** as an exercise in numerical reasoning. Its controllable variable is **Nominal insulating barrier thickness**; all other quantities follow fixed assumptions. Set **Nominal insulating barrier thickness = 1.5333333 nm**. With the implemented expression `10*Math.exp(1.5*(t-1))`, the output is **22.2554093 ohm micrometer²**. Increase the control to **1.6888889 nm**. The new output is **28.104183 ohm micrometer²**. Thus the model output increases over this interval, with secant slope **37.5992596 (ohm micrometer²)/(nm)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Correlated changes are not enough to identify a single atomic defect; independent chemical assays are essential.

### Counterfactual and model criticism

Suppose a measurement appears to support **defect chemistry, aging and coupled reliability**, but **interdiffusion, pinholes or trapped charge** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **cross-sectional microscopy and matched interface controls** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **defect chemistry, aging and coupled reliability** affects the distinction between **intrinsic interface coupling versus extrinsic sample artifacts**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **22.2554093 ohm micrometer²** and **28.104183 ohm micrometer²** from the explicit expression for the stated two values of **Nominal insulating barrier thickness**. Report a unit-consistent slope in (ohm micrometer²)/(nm), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: A new oxide magnetic interface

### Diagnose the evidence, not just the material label

A ferro-antiferromagnetic stack displays loop shifts, with RA varying strongly among devices. The mechanisms may involve interfacial exchange, compositional drift or tunnel defects. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Calculate the declared exchange-bias field and tunneling RA sensitivity, then test interface thickness and chemical continuity independently. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Combine field-cooling reversal, junction-area scaling, atomistic imaging and aging replicates. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **interdiffusion, pinholes or trapped charge** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** Large fitted exchange energy may merely compensate for an incorrect magnetic thickness.

### Five capstone examination questions

