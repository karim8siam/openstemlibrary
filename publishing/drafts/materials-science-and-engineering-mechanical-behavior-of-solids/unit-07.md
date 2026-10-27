# Unit 7: Creep, relaxation and viscoelastic solids

**Guiding question:** How does deformation evolve under sustained stress and temperature?

## Physical map and learning outcomes

A polymer seal loses clamp load at a moderate temperature while a nearby metallic fixture accumulates sustained-load deformation. The two behaviors are mistakenly represented by the same stress–strain plot. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Calculate an illustrative activated creep rate and a Maxwell relaxation curve, clearly specifying whether force or displacement is controlled. Compare time scales with the service interval. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 7.1: Transient, steady and accelerating creep

### Physical reasoning and derivation target

Creep is time-dependent strain under sustained load; many high-temperature metallic tests exhibit transient, approximate steady and accelerating regimes. The minimum creep rate and time to rupture depend on stress, temperature, microstructure and environment. A single curve shape does not prove a particular deformation mechanism.

**Governing relationship and applicability:** creep rate dot-epsilon versus time under defined load mode. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Plot three fictional constant-stress creep curves and compare minimum rate and rupture time, holding temperature units absolute.

A related local calculator for this lesson is **Norton activated creep rate**. Use **Absolute temperature = 821.4286 K** with the other parameters fixed. The illustrative model returns **4.0122555e-10 s⁻¹**. Repeat the computation at **Absolute temperature = 901.4286 K** to obtain **1.5259274e-08 s⁻¹**; the output rises when the input rises. Record the expression and its model domain exactly: **Artificial A=100 s⁻¹ MPa⁻⁴, stress=40 MPa, n=4, Q=280 kJ/mol; not an engineering creep database**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Temperature drift and changing true stress during necking undermine a constant-stress interpretation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which continuous specimen-temperature measurement should accompany the strain curve? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **821.4286 K**, and recover **4.0122555e-10 s⁻¹**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Temperature drift and changing true stress during necking undermine a constant-stress interpretation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 7.2: Norton power law and activation

### Physical reasoning and derivation target

A frequently used empirical description takes strain rate proportional to stress raised to a power and an activated temperature factor. The stress exponent n and apparent activation energy are mechanism- and domain-dependent; a fit across a mechanism transition is unreliable. Extrapolation from short tests to long service lives can be especially uncertain.

**Governing relationship and applicability:** dot-epsilon=A sigma^n exp(-Q/RT) with unit-consistent A and fixed fitting domain. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare predicted rate changes after raising stress at fixed temperature and raising temperature at fixed stress.

A related local calculator for this lesson is **Maxwell stress relaxation**. Use **Elapsed time = 20.57143 h** with the other parameters fixed. The illustrative model returns **9.0046156 MPa**. Repeat the computation at **Elapsed time = 32.09143 h** to obtain **3.4478033 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **Initial stress=50 MPa, tau=12 h, fixed small imposed strain, ideal Maxwell element**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Oxidation and microstructural evolution may modify effective section and creep coefficients during a test.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which microscopy and atmosphere controls could reveal a changing deformation mechanism? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **20.57143 h**, and recover **9.0046156 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Oxidation and microstructural evolution may modify effective section and creep coefficients during a test.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 7.3: Stress relaxation and hereditary response

### Physical reasoning and derivation target

A displacement-controlled material can show decreasing stress over time, unlike constant-load creep in which strain generally grows. Linear viscoelastic springs and dashpots model time-dependent response through convolution or elementary networks. A Maxwell element relaxes exponentially under an imposed small step strain, while a Kelvin–Voigt element has a different step response.

**Governing relationship and applicability:** Maxwell sigma(t)=sigma_0 exp(-t/tau), tau=eta/E. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare constant extension and constant tensile force experiments on a polymer strip, drawing force and displacement histories.

A related local calculator for this lesson is **Norton activated creep rate**. Use **Absolute temperature = 964.2857 K** with the other parameters fixed. The illustrative model returns **1.7423859e-07 s⁻¹**. Repeat the computation at **Absolute temperature = 1044.286 K** to obtain **2.5296236e-06 s⁻¹**; the output rises when the input rises. Record the expression and its model domain exactly: **Artificial A=100 s⁻¹ MPa⁻⁴, stress=40 MPa, n=4, Q=280 kJ/mol; not an engineering creep database**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Temperature, physical aging, nonlinear strain and viscoplasticity can violate time-invariant linear viscoelasticity.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How do load-control versus displacement-control apparatus requirements change the observation? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **964.2857 K**, and recover **1.7423859e-07 s⁻¹**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Temperature, physical aging, nonlinear strain and viscoplasticity can violate time-invariant linear viscoelasticity.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 7.4: Creep damage, cavitation and rupture

### Physical reasoning and derivation target

High-temperature degradation may involve cavity nucleation, grain boundary sliding, oxidation, precipitate coarsening and local necking. A rupture time plotted against stress is a system-level outcome rather than a direct identification of an atomic mechanism. Multiaxial stress and weld microstructure can strongly affect location and progression of damage.

**Governing relationship and applicability:** creep rupture correlations require calibrated service-regime data. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Design fictional interrupted-creep tests with microscopy at fractional lifetimes rather than inspecting only failed specimens.

A related local calculator for this lesson is **Maxwell stress relaxation**. Use **Elapsed time = 41.14286 h** with the other parameters fixed. The illustrative model returns **1.621662 MPa**. Repeat the computation at **Elapsed time = 52.66286 h** to obtain **0.62092286 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **Initial stress=50 MPa, tau=12 h, fixed small imposed strain, ideal Maxwell element**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Accelerated testing can change the active mechanism, so extrapolation must be conditional on microstructural equivalence.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What evidence would falsify an accelerated-life transfer assumption? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **41.14286 h**, and recover **1.621662 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Accelerated testing can change the active mechanism, so extrapolation must be conditional on microstructural equivalence.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 7.5: Time–temperature superposition

### Physical reasoning and derivation target

For some thermorheologically simple polymers, viscoelastic curves measured at different temperatures can be shifted horizontally to form a master curve. The shift factor may approximately follow WLF or Arrhenius-type forms over restricted domains. Crystallization, moisture and transitions can invalidate a single master curve.

**Governing relationship and applicability:** E(t,T)≈E(t/a_T,T_ref) in a specified time–temperature superposition regime. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Build synthetic modulus relaxation curves around a reference temperature and test whether vertical shifts are also required.

A related local calculator for this lesson is **Norton activated creep rate**. Use **Absolute temperature = 1107.143 K** with the other parameters fixed. The illustrative model returns **1.5782978e-05 s⁻¹**. Repeat the computation at **Absolute temperature = 1187.143 K** to obtain **0.0001225736 s⁻¹**; the output rises when the input rises. Record the expression and its model domain exactly: **Artificial A=100 s⁻¹ MPa⁻⁴, stress=40 MPa, n=4, Q=280 kJ/mol; not an engineering creep database**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A visually smooth master curve is not independent proof of predictive validity outside the measurement window.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What validation experiment at an intermediate temperature would test the shift factors? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **1107.143 K**, and recover **1.5782978e-05 s⁻¹**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A visually smooth master curve is not independent proof of predictive validity outside the measurement window.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Creep versus relaxation in service

### Scientific question and competing hypotheses

A polymer seal loses clamp load at a moderate temperature while a nearby metallic fixture accumulates sustained-load deformation. The two behaviors are mistakenly represented by the same stress–strain plot.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Calculate an illustrative activated creep rate and a Maxwell relaxation curve, clearly specifying whether force or displacement is controlled. Compare time scales with the service interval.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Log true temperature and load/extension, repeat at a second condition and use interrupted microstructural observation where relevant.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Time–temperature shifting or a single stress exponent cannot substitute for service-specific long-term measurements.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_12 -->

<!-- MODEL_13 -->

