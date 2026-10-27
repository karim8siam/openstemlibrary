# Unit 3: Atomic mechanisms and temperature dependence

**Guiding question:** Why do composition, defects and temperature change diffusion rates?

## Physical map and learning outcomes

Two furnaces advertise the same nominal peak temperature but use different heating ramps. A tracer is deposited on a polycrystalline alloy with non-equilibrium vacancy content from earlier processing. A colleague proposes comparing final profiles after equal clock times at peak temperature. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Compute D(T) from an illustrative Arrhenius expression and integrate ∫D[T(t)]dt numerically for each full thermal trajectory. Predict a diffusion length from each diffusion clock. Refit a straight line to synthetic ln D versus 1/T data and examine the sensitivity to a ±5 K temperature calibration offset. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 3.1: Vacancy-mediated substitutional diffusion

### Physical reasoning and derivation target

Substitutional atoms usually exchange positions with vacancies. An effective tracer diffusivity depends on vacancy availability, jump frequency, geometry and correlation factors. Equilibrium vacancy populations typically increase with temperature, but non-equilibrium quenching can retain excess vacancies and change early-time transport.

### Laboratory thought experiment and numerical calculation

Anneal a hypothetical substitutional isotope tracer at several temperatures. Compare the profile width in a well-annealed specimen and a quenched specimen with a larger initial excess vacancy concentration.

The paired local calculator for this lesson is **Activated bulk diffusivity**. Use **Temperature = 750 K** with the other parameters fixed. The model returns **7.1499988e-16 m²/s**. Repeat the computation at **Temperature = 862 K** to obtain **1.6279945e-14 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **D0=2×10⁻⁵ m²/s, Q=150 kJ/mol, one transport mechanism, T in kelvin**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Radiotracer broadening can be influenced by grain-boundary paths; simple bulk vacancy theory may not explain near-surface tails.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which thermal pre-treatment would test whether non-equilibrium vacancies cause the early fast transport? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **750 K**, and recover **7.1499988e-16 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Radiotracer broadening can be influenced by grain-boundary paths; simple bulk vacancy theory may not explain near-surface tails.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 3.2: Interstitial migration

### Physical reasoning and derivation target

Small solutes such as hydrogen or carbon may migrate between interstitial sites in an appropriate host lattice. Their rates and activation barriers differ from substitutional motion, but trapping at dislocations, vacancies or precipitates can lead to non-Fickian effective kinetics.

### Laboratory thought experiment and numerical calculation

Contrast carbon diffusion in austenite with a much slower substitutional alloying solute using a conceptual heat-treatment schedule. Calculate √(Dt) for each illustrative coefficient before deciding how deep each profile might penetrate.

The paired local calculator for this lesson is **Ratio of diffusivities at two temperatures**. Use **Second temperature = 871.4286 K** with the other parameters fixed. The model returns **0.67412779 D(T)/D(900 K)**. Repeat the computation at **Second temperature = 967.4286 K** to obtain **2.3123941 D(T)/D(900 K)**; the output rises when the input rises. Record the expression and its model domain exactly: **D0 cancels; Q=90 kJ/mol, reference T=900 K, one Arrhenius regime**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Interstitial motion is not always fast if strong traps are present; solubility, phase structure and chemical potential must accompany diffusivity data.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How can a desorption time series reveal trapping rather than a single constant interstitial D? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **871.4286 K**, and recover **0.67412779 D(T)/D(900 K)**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Interstitial motion is not always fast if strong traps are present; solubility, phase structure and chemical potential must accompany diffusivity data.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 3.3: Arrhenius diffusivity

### Physical reasoning and derivation target

Over an appropriate single-mechanism temperature range, D=D0 exp(−Q/RT), where Q is molar activation energy and T is kelvin. A plot of ln D against 1/T has slope −Q/R. Temperature dependence should be inferred from several measurements with uncertainty, not assigned from two poorly calibrated points.

### Laboratory thought experiment and numerical calculation

Use synthetic D values at four temperatures to recover an activation-energy estimate from a linear fit, and compare the result with a separate temperature-independent D0 assumption.

The paired local calculator for this lesson is **Activated bulk diffusivity**. Use **Temperature = 950 K** with the other parameters fixed. The model returns **1.1314003e-13 m²/s**. Repeat the computation at **Temperature = 1062 K** to obtain **8.383011e-13 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **D0=2×10⁻⁵ m²/s, Q=150 kJ/mol, one transport mechanism, T in kelvin**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Curvature in an Arrhenius graph may signal phase transitions, mechanism changes, segregation, or measurement offsets; extrapolation beyond a validated range is risky.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What observation would show the fitted activation energy is not constant over the entire temperature range? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **950 K**, and recover **1.1314003e-13 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Curvature in an Arrhenius graph may signal phase transitions, mechanism changes, segregation, or measurement offsets; extrapolation beyond a validated range is risky.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 3.4: Tracer, intrinsic and interdiffusion coefficients

### Physical reasoning and derivation target

Tracer diffusivity characterizes labelled atoms in an otherwise chemically equivalent population; intrinsic diffusion measures component flux relative to a specified lattice frame; interdiffusion describes profile evolution in a composition gradient. Their numerical equality is not general. In binary substitutional alloys, vacancy flux and thermodynamic factors matter.

### Laboratory thought experiment and numerical calculation

Place inert Kirkendall markers near the interface of a synthetic binary diffusion couple. Predict how unequal intrinsic atomic fluxes could displace the marker plane while the chemical profile broadens.

The paired local calculator for this lesson is **Ratio of diffusivities at two temperatures**. Use **Second temperature = 1042.857 K** with the other parameters fixed. The model returns **5.1943241 D(T)/D(900 K)**. Repeat the computation at **Second temperature = 1138.857 K** to obtain **12.459969 D(T)/D(900 K)**; the output rises when the input rises. Record the expression and its model domain exactly: **D0 cancels; Q=90 kJ/mol, reference T=900 K, one Arrhenius regime**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Interdiffusion profiles alone cannot uniquely recover two intrinsic diffusion coefficients without marker or additional kinetic information.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Why is a frame of reference essential before comparing intrinsic fluxes? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1042.857 K**, and recover **5.1943241 D(T)/D(900 K)**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Interdiffusion profiles alone cannot uniquely recover two intrinsic diffusion coefficients without marker or additional kinetic information.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 3.5: Temperature jumps and nonisothermal schedules

### Physical reasoning and derivation target

When D varies with time because T(t) changes and the material stays in one diffusion regime, the integrated diffusion time ∫D[T(t)]dt replaces a constant Dt for certain simplified solutions. Heating ramps can therefore contribute materially to total penetration even when nominal dwell times match.

### Laboratory thought experiment and numerical calculation

Compare a slow furnace ramp to a rapid induction ramp, both followed by a hold at the same target temperature. Numerically integrate illustrative D(T) across each schedule and compare their effective diffusion lengths.

The paired local calculator for this lesson is **Activated bulk diffusivity**. Use **Temperature = 1150 K** with the other parameters fixed. The model returns **3.0757364e-12 m²/s**. Repeat the computation at **Temperature = 1262 K** to obtain **1.2376463e-11 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **D0=2×10⁻⁵ m²/s, Q=150 kJ/mol, one transport mechanism, T in kelvin**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Thermal gradients and simultaneous phase transitions invalidate a single uniform-T diffusion-clock approximation; controls must verify actual specimen temperatures.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What temperature measurement determines whether the stated furnace ramp equals the specimen's thermal history? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1150 K**, and recover **3.0757364e-12 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Thermal gradients and simultaneous phase transitions invalidate a single uniform-T diffusion-clock approximation; controls must verify actual specimen temperatures.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Temperature-program selection for tracer annealing

### Scientific question and competing hypotheses

Two furnaces advertise the same nominal peak temperature but use different heating ramps. A tracer is deposited on a polycrystalline alloy with non-equilibrium vacancy content from earlier processing. A colleague proposes comparing final profiles after equal clock times at peak temperature.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Compute D(T) from an illustrative Arrhenius expression and integrate ∫D[T(t)]dt numerically for each full thermal trajectory. Predict a diffusion length from each diffusion clock. Refit a straight line to synthetic ln D versus 1/T data and examine the sensitivity to a ±5 K temperature calibration offset.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Use a dummy sample with a bonded thermocouple to obtain internal temperature response; vary preannealing to remove excess point defects; record actual specimen residence time above a specified temperature. Acquire depth profiles after both schedules.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

The diffusion-clock reduction assumes one mechanism and a spatially uniform specimen temperature. Phase changes and vacancy relaxation may make a single D(T) representation scientifically inappropriate.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_4 -->

<!-- MODEL_5 -->

