# Unit 8: Experiments, numerical inversion and engineering decisions

**Guiding question:** How are credible kinetic coefficients estimated and used?

## Physical map and learning outcomes

An invented factory must choose one of three heating schedules to meet a diffusion-length specification while limiting grain growth. Only four synthetic concentration data points are available from a prototype, and the fitted Arrhenius parameters are strongly correlated. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Fit an effective D to synthetic profiles, propagate ±10% time and ±5 K temperature uncertainty, and compare processing times required at candidate temperatures using an Arrhenius ratio. Document process constraints and whether the fitted model predicts outside the experimental calibration range. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 8.1: Diffusivity measurements and inverse inference

### Physical reasoning and derivation target

Diffusivity may be estimated from concentration profiles, tracer experiments, mass uptake, permeation breakthrough or relaxation curves. Each experiment measures a response influenced by geometry, boundary conditions and instrument sensitivity. The fitted parameter is often an effective quantity specific to the model.

### Laboratory thought experiment and numerical calculation

Fit a synthetic uptake curve using two candidate D values and a surface transfer coefficient. Explore the parameter combinations that reproduce the same first few data points.

The paired local calculator for this lesson is **Temperature-dependent process time**. Use **Holding temperature = 735.7143 K** with the other parameters fixed. The model returns **250010.35 s**. Repeat the computation at **Holding temperature = 831.7143 K** to obtain **28546.755 s**; the output falls when the input rises. Record the expression and its model domain exactly: **same D×t target across temperatures, Q=115 kJ/mol, reference hold=3600 s at 950 K**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Inverse problems can have nonunique solutions; a narrow confidence interval from a restrictive fit may hide a large structural modeling error.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What second observable would improve identifiability of D and the surface transfer coefficient? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **735.7143 K**, and recover **250010.35 s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Inverse problems can have nonunique solutions; a narrow confidence interval from a restrictive fit may hide a large structural modeling error.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 8.2: Uncertainty and parameter correlations

### Physical reasoning and derivation target

Uncertainty propagates from temperature, time, profile calibration and sample geometry into inferred diffusion coefficients. In an Arrhenius fit, D0 and Q are strongly correlated when the measured temperature range is narrow, so reporting either without covariance can be misleading.

### Laboratory thought experiment and numerical calculation

Add plausible synthetic noise to ln D across four temperatures, refit multiple times and compare predicted D within and outside the measured range.

The paired local calculator for this lesson is **Relative thermal penetration budget**. Use **Hold time = 7185.714 s** with the other parameters fixed. The model returns **328.30735 μm**. Repeat the computation at **Hold time = 11176.11 s** to obtain **409.44073 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **single spatial dimension, uniform D=1.5×10⁻¹¹ m²/s; neglects ramp, phase changes, surfaces**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Independent random noise calculations do not cover systematic temperature offsets or model-regime changes; extrapolated uncertainty can be much larger.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which calibration standard constrains temperature error in an activation-energy estimate? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **7185.714 s**, and recover **328.30735 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Independent random noise calculations do not cover systematic temperature offsets or model-regime changes; extrapolated uncertainty can be much larger.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 8.3: Model validation and mesh convergence

### Physical reasoning and derivation target

Computational diffusion models should satisfy conservation, physical bounds, unit consistency and grid convergence. Cross-checking a code against an analytic constant-D solution tests its implementation, while validation against separate experimental observations tests scientific adequacy. These are different standards of evidence.

### Laboratory thought experiment and numerical calculation

Compare explicit finite-volume and implicit finite-difference solutions for a sealed one-dimensional slab. Track mass residual and profile distance from a known Fourier solution across mesh refinements.

The paired local calculator for this lesson is **Temperature-dependent process time**. Use **Holding temperature = 907.1429 K** with the other parameters fixed. The model returns **7161.8912 s**. Repeat the computation at **Holding temperature = 1003.143 K** to obtain **1664.685 s**; the output falls when the input rises. Record the expression and its model domain exactly: **same D×t target across temperatures, Q=115 kJ/mol, reference hold=3600 s at 950 K**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A numerically converged wrong boundary condition remains wrong; synthetic benchmark agreement does not validate the actual material's diffusivity.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which experiment would test the chosen boundary and material-property assumptions independently? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **907.1429 K**, and recover **7161.8912 s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A numerically converged wrong boundary condition remains wrong; synthetic benchmark agreement does not validate the actual material's diffusivity.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 8.4: Process optimization and trade-offs

### Physical reasoning and derivation target

A longer, hotter treatment can accelerate homogenization or case penetration but may increase oxidation, grain growth, energy consumption and distortion. Optimization should balance multiple objectives and practical constraints rather than maximize diffusion distance alone.

### Laboratory thought experiment and numerical calculation

For a fictional processing plant, compare three temperature-time schedules using an Arrhenius D and a fixed diffusion-length requirement. Add cost and microstructure constraints before selecting an option.

The paired local calculator for this lesson is **Relative thermal penetration budget**. Use **Hold time = 14311.43 s** with the other parameters fixed. The model returns **463.32648 μm**. Repeat the computation at **Hold time = 18301.83 s** to obtain **523.95365 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **single spatial dimension, uniform D=1.5×10⁻¹¹ m²/s; neglects ramp, phase changes, surfaces**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Economic and environmental costs cannot be obtained from a diffusion coefficient; equipment utilization, process atmosphere and scrap rate need their own evidence.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What decision would change if the estimated activation energy were 20% wrong? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **14311.43 s**, and recover **463.32648 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Economic and environmental costs cannot be obtained from a diffusion coefficient; equipment utilization, process atmosphere and scrap rate need their own evidence.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 8.5: Responsible kinetic reporting

### Physical reasoning and derivation target

Scientific conclusions must disclose synthetic versus observed values, the complete transport equation, units, geometry, boundary conditions, fit range and uncertainty. Repository code and plots should be reproducible; safety-critical design requires validated data, expert review and relevant standards.

### Laboratory thought experiment and numerical calculation

Write a method section for a fictional diffusion-couple study, including temperature measurements, sample preparation, calibration, time points, raw data retention and a falsifiable rival mechanism.

The paired local calculator for this lesson is **Temperature-dependent process time**. Use **Holding temperature = 1078.571 K** with the other parameters fixed. The model returns **634.69541 s**. Repeat the computation at **Holding temperature = 1174.571 K** to obtain **222.52423 s**; the output falls when the input rises. Record the expression and its model domain exactly: **same D×t target across temperatures, Q=115 kJ/mol, reference hold=3600 s at 950 K**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A polished interactive chart does not prove material behavior; neither a small fit residual nor an AI-generated explanation replaces the actual experiment.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What minimum evidence package would allow an independent researcher to repeat the proposed analysis? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1078.571 K**, and recover **634.69541 s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A polished interactive chart does not prove material behavior; neither a small fit residual nor an AI-generated explanation replaces the actual experiment.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Inverse transport model for a manufacturing decision

### Scientific question and competing hypotheses

An invented factory must choose one of three heating schedules to meet a diffusion-length specification while limiting grain growth. Only four synthetic concentration data points are available from a prototype, and the fitted Arrhenius parameters are strongly correlated.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Fit an effective D to synthetic profiles, propagate ±10% time and ±5 K temperature uncertainty, and compare processing times required at candidate temperatures using an Arrhenius ratio. Document process constraints and whether the fitted model predicts outside the experimental calibration range.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Validate the schedule on a new specimen and a second thickness, then collect an independently measured profile and microstructure image. Report the held-out prediction error separately from the fit residual. Keep the processing recommendation conditional until the out-of-sample evidence is available.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Numerical optimizer success does not certify industrial robustness. The unknown temperature dependence of competing damage, surface reactions and energy costs must be addressed before selecting an actual production schedule.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_14 -->

<!-- MODEL_15 -->

