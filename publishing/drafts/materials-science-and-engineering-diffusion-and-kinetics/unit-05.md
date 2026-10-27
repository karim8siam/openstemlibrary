# Unit 5: Diffusion couples and materials processing

**Guiding question:** How do engineers translate transport theory into process schedules?

## Physical map and learning outcomes

A fictional manufacturing team wants a carbon-enriched layer of specified composition threshold below a steel surface. It also wants to limit dimensional change, oxidation and energy consumption. Its first estimate uses √Dt and equates the result directly with a finished hardness depth. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Use the erfc semi-infinite profile with a clearly stated fixed carbon surface composition. Solve for the location where the normalized concentration increment is one half; compare this position with √Dt. Separately fit synthetic reaction-layer thickness observations to x²=kpt to show why oxidation and carburization need distinct rate models. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 5.1: Diffusion couples and interfacial broadening

### Physical reasoning and derivation target

A planar diffusion couple between dissimilar alloys creates a concentration gradient whose width often grows on a √t scale under constant-coefficient assumptions. Multiple phases may form, and interfacial reactions can consume diffusing species, so a single error-function profile may not describe the entire couple.

### Laboratory thought experiment and numerical calculation

Join synthetic pure A and pure B blocks and anneal at one temperature for four durations. Measure profiles with an imagined line scan and test whether a chosen width metric scales with the square root of time.

The paired local calculator for this lesson is **Illustrative carburization half-rise depth**. Use **Holding time = 5245.714 s** with the other parameters fixed. The model returns **0.37840189 mm**. Repeat the computation at **Holding time = 10986.51 s** to obtain **0.54762207 mm**; the output rises when the input rises. Record the expression and its model domain exactly: **erfc(z)=0.5 at z≈0.476936; D=3×10⁻¹¹ m²/s, fixed surface concentration, semi-infinite**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Beam interaction volumes blur steep profiles, intermetallic growth may replace direct intermixing and volume changes can shift the original interface.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How can a non-diffusing marker distinguish a moving interface from laboratory-coordinate broadening? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **5245.714 s**, and recover **0.37840189 mm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Beam interaction volumes blur steep profiles, intermetallic growth may replace direct intermixing and volume changes can shift the original interface.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 5.2: Carburizing and case depth

### Physical reasoning and derivation target

Thermochemical surface hardening uses a combination of carbon surface supply, austenite diffusion and later transformations. A nominal case depth is defined by a property or composition threshold, not by the value √Dt alone. Processing temperatures and surface chemistry also influence distortion and final phase structure.

### Laboratory thought experiment and numerical calculation

Design a hypothetical steel case-hardening schedule with an illustrative carbon diffusivity and specified surface concentration. Find a concentration-threshold depth from the error-function solution and describe the quench characterization needed afterward.

The paired local calculator for this lesson is **Parabolic reaction-layer thickness**. Use **Oxidation duration = 10328.57 s** with the other parameters fixed. The model returns **1.760276 μm**. Repeat the computation at **Oxidation duration = 16078.97 s** to obtain **2.1962904 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **x²=kp t with kp=3×10⁻¹⁶ m²/s; ideal planar diffusion-limited layer, no spallation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Using one temperature-independent diffusivity across a ramp or across ferrite–austenite changes is not justified; a concentration threshold is not directly a hardness guarantee.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What measurements establish that the nominal concentration profile produces the intended mechanical response? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **10328.57 s**, and recover **1.760276 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Using one temperature-independent diffusivity across a ramp or across ferrite–austenite changes is not justified; a concentration threshold is not directly a hardness guarantee.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 5.3: Dopant diffusion in semiconductors

### Physical reasoning and derivation target

Controlled impurity diffusion can alter electrical conductivity by changing local dopant concentrations, yet total dopant count may differ from electrically active dopant concentration. Boundary conditions depend on finite-dose versus constant-source processing, and the measured junction depth is device- and measurement-specific.

### Laboratory thought experiment and numerical calculation

Compare a fixed dopant dose diffusing into silicon with an effectively maintained surface activity. Sketch Gaussian-like and erfc-like ideal solutions and describe how a four-point probe or profiling technique might constrain model parameters.

The paired local calculator for this lesson is **Illustrative carburization half-rise depth**. Use **Holding time = 15497.14 s** with the other parameters fixed. The model returns **0.65039441 mm**. Repeat the computation at **Holding time = 21237.94 s** to obtain **0.76139006 mm**; the output rises when the input rises. Record the expression and its model domain exactly: **erfc(z)=0.5 at z≈0.476936; D=3×10⁻¹¹ m²/s, fixed surface concentration, semi-infinite**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Clustering, electrical activation, implant damage and transient enhanced diffusion can invalidate a simple constant-D thermal schedule.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Why is electrical activation data required in addition to a dopant concentration profile? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **15497.14 s**, and recover **0.65039441 mm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Clustering, electrical activation, implant damage and transient enhanced diffusion can invalidate a simple constant-D thermal schedule.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 5.4: Oxidation and reaction-layer thickening

### Physical reasoning and derivation target

Under diffusion-limited planar growth with constant conditions, a reaction layer may approximately follow x²=kpt, whereas interface-reaction control can give near-linear x(t). Parabolic kinetics is evidence consistent with diffusion limitation but not a unique mechanistic proof.

### Laboratory thought experiment and numerical calculation

Track an imagined oxide thickness over several exposure times and fit both linear and parabolic laws with uncertainty. Inspect whether early transient growth or later spallation changes the apparent exponent.

The paired local calculator for this lesson is **Parabolic reaction-layer thickness**. Use **Oxidation duration = 20597.14 s** with the other parameters fixed. The model returns **2.4857882 μm**. Repeat the computation at **Oxidation duration = 26347.54 s** to obtain **2.8114521 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **x²=kp t with kp=3×10⁻¹⁶ m²/s; ideal planar diffusion-limited layer, no spallation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Temperature gradients, cracks, multilayer scales and changing oxygen activities make one rate constant inadequate; measuring only mass gain can conceal spallation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What additional phase and morphology evidence must accompany a claimed parabolic oxidation law? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **20597.14 s**, and recover **2.4857882 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Temperature gradients, cracks, multilayer scales and changing oxygen activities make one rate constant inadequate; measuring only mass gain can conceal spallation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 5.5: Homogenization of cast alloys

### Physical reasoning and derivation target

Solute segregation within dendrites can decay during solid-state homogenization. A simple Fourier mode decays exponentially as exp(−Dk²t); finer compositional wavelengths can smooth much faster than coarser ones. This enables a physical connection between casting microstructure length scale and anneal duration.

### Laboratory thought experiment and numerical calculation

Compare two synthetic castings with the same initial segregation amplitude but dendrite spacings differing by a factor of two. Predict relative decay times under a constant-D sinusoidal model.

The paired local calculator for this lesson is **Illustrative carburization half-rise depth**. Use **Holding time = 25748.57 s** with the other parameters fixed. The model returns **0.83835421 mm**. Repeat the computation at **Holding time = 31489.37 s** to obtain **0.92711365 mm**; the output rises when the input rises. Record the expression and its model domain exactly: **erfc(z)=0.5 at z≈0.476936; D=3×10⁻¹¹ m²/s, fixed surface concentration, semi-infinite**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Homogenization may dissolve precipitates, induce new phases or change grain structure; reducing compositional variance is not sufficient to guarantee adequate mechanical properties.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What evidence shows that homogenization improved material performance rather than merely reducing a composition gradient? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **25748.57 s**, and recover **0.83835421 mm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Homogenization may dissolve precipitates, induce new phases or change grain structure; reducing compositional variance is not sufficient to guarantee adequate mechanical properties.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Carburization schedule and oxidation trade-off

### Scientific question and competing hypotheses

A fictional manufacturing team wants a carbon-enriched layer of specified composition threshold below a steel surface. It also wants to limit dimensional change, oxidation and energy consumption. Its first estimate uses √Dt and equates the result directly with a finished hardness depth.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Use the erfc semi-infinite profile with a clearly stated fixed carbon surface composition. Solve for the location where the normalized concentration increment is one half; compare this position with √Dt. Separately fit synthetic reaction-layer thickness observations to x²=kpt to show why oxidation and carburization need distinct rate models.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Acquire depth-resolved carbon composition after the diffusion treatment and a separate hardness profile after quenching. Record furnace atmosphere, phase condition, thermocouple history and oxidation scale thickness; check at least two process durations.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

A concentration threshold is not a mechanical-property guarantee. The assumed D is a placeholder rather than measured carbon diffusivity, and the simplified treatment omits phase-dependent partitioning and quench-induced transformation.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_8 -->

<!-- MODEL_9 -->

