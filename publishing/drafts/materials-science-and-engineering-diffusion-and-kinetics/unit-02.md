# Unit 2: Fickian transport and boundary-value problems

**Guiding question:** How are transient concentration profiles predicted and checked?

## Physical map and learning outcomes

An imagined polymer sheet takes up an inert vapor after its gas environment undergoes a step change. The upstream chamber maintains a nominal composition, but external boundary films may alter the surface activity. Two sheet thicknesses are available; one is thin enough that both faces eventually interact. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Implement Fick’s second law using a finite-volume grid with no internal source and either fixed-concentration or finite-transfer boundaries. Demonstrate why the initial concentration profile and both face conditions are mandatory. Begin with a case that admits an approximate semi-infinite error-function solution, then show when the finite thickness makes that approximation fail. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 2.1: Steady Fickian diffusion

### Physical reasoning and derivation target

For constant D in a one-dimensional source-free slab at steady state, ∂²c/∂x² = 0 and the concentration profile is linear between fixed boundary concentrations. The flux scales as DΔc/L, with units determined by the concentration basis. This formula is a transport benchmark, not evidence that a specimen actually reached steady state.

### Laboratory thought experiment and numerical calculation

Take a membrane with two reservoirs at different dissolved-species concentrations. Compare predicted flux through thicknesses L and 2L, keeping the boundary activities fixed. Then ask whether reservoir depletion prevents a true steady regime.

The paired local calculator for this lesson is **Diffusion length over fixed time**. Use **Diffusivity value = 0.7571429 ×10⁻¹¹ m²/s** with the other parameters fixed. The model returns **165.09737 μm**. Repeat the computation at **Diffusivity value = 1.549143 ×10⁻¹¹ m²/s** to obtain **236.15491 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **characteristic √(Dt), t=3600 s, constant D; not a unique physical front location**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

The concentration drop in a boundary film or interface can invalidate the assumption that the entire drop occurs within the solid.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What measured spatial profile distinguishes an internal diffusion limitation from external mass-transfer resistance? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.7571429 ×10⁻¹¹ m²/s**, and recover **165.09737 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **The concentration drop in a boundary film or interface can invalidate the assumption that the entire drop occurs within the solid.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 2.2: Transient Fick's second law

### Physical reasoning and derivation target

Substituting J=−D∇c into conservation gives ∂c/∂t=D∇²c for constant scalar D without sources. The transient solution requires an initial profile and suitable boundary conditions. Failure to state these conditions makes a time-dependent calculation mathematically underdetermined.

### Laboratory thought experiment and numerical calculation

Initialize a slab with uniform tracer concentration and suddenly impose a fixed higher concentration at one face. Draw several profiles at increasing times, then calculate the characteristic length √(Dt) to judge when the remote face should respond.

The paired local calculator for this lesson is **Explicit solver stability ratio**. Use **Time step = 4.642857 s** with the other parameters fixed. The model returns **0.37142857 dimensionless**. Repeat the computation at **Time step = 7.186857 s** to obtain **0.57494857 dimensionless**; the output rises when the input rises. Record the expression and its model domain exactly: **r=DΔt/Δx², D=2×10⁻¹² m²/s, Δx=5 μm; explicit 1D constant-D scheme stable for r≤0.5**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Allowing diffusivity to depend on concentration introduces a nonlinear diffusion equation; applying a constant-D solution may produce an incorrect uptake curve.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What boundary experiment would test whether D changes across the sampled composition interval? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **4.642857 s**, and recover **0.37142857 dimensionless**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Allowing diffusivity to depend on concentration introduces a nonlinear diffusion equation; applying a constant-D solution may produce an incorrect uptake curve.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 2.3: Error-function penetration

### Physical reasoning and derivation target

For a semi-infinite solid with initial concentration c0 and a fixed surface concentration cs, the ideal profile satisfies (c−c0)/(cs−c0)=erfc[x/(2√Dt)]. The solution assumes constant D, an unchanging surface condition and a sample thick enough to avoid its rear face.

### Laboratory thought experiment and numerical calculation

A synthetic carburizing treatment holds a steel surface at fixed carbon activity. Use an illustrative D and elapsed time to calculate the concentration ratio at selected depths, then identify a depth where the semi-infinite approximation should fail.

The paired local calculator for this lesson is **Diffusion length over fixed time**. Use **Diffusivity value = 2.171429 ×10⁻¹¹ m²/s** with the other parameters fixed. The model returns **279.59154 μm**. Repeat the computation at **Diffusivity value = 2.963429 ×10⁻¹¹ m²/s** to obtain **326.62429 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **characteristic √(Dt), t=3600 s, constant D; not a unique physical front location**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Surface reaction kinetics, carbon-dependent diffusivity and changing austenite fractions mean actual carburizing profiles require more complex models.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which independent surface-concentration measurement would make an inferred diffusivity more credible? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **2.171429 ×10⁻¹¹ m²/s**, and recover **279.59154 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Surface reaction kinetics, carbon-dependent diffusivity and changing austenite fractions mean actual carburizing profiles require more complex models.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 2.4: Finite slabs and boundary resistance

### Physical reasoning and derivation target

A finite sheet cannot always be approximated as semi-infinite. Two free surfaces, insulating boundaries, symmetry planes and finite surface-transfer coefficients yield different eigenfunction solutions. The Biot-like ratio kL/D compares external transfer to internal diffusion in simple linear cases.

### Laboratory thought experiment and numerical calculation

Expose both sides of a thin polymer film to a new vapor activity, while comparing a thick film. Measure total uptake and spatial profiles to diagnose whether internal diffusion or surface transfer controls the time scale.

The paired local calculator for this lesson is **Explicit solver stability ratio**. Use **Time step = 9.185714 s** with the other parameters fixed. The model returns **0.73485714 dimensionless**. Repeat the computation at **Time step = 11.72971 s** to obtain **0.93837714 dimensionless**; the output rises when the input rises. Record the expression and its model domain exactly: **r=DΔt/Δx², D=2×10⁻¹² m²/s, Δx=5 μm; explicit 1D constant-D scheme stable for r≤0.5**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

The apparent concentration may couple to swelling or sorption; a single equilibrium partition coefficient may not apply during a changing activity step.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would varying thickness distinguish diffusion-limited uptake from an interface-controlled response? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **9.185714 s**, and recover **0.73485714 dimensionless**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **The apparent concentration may couple to swelling or sorption; a single equilibrium partition coefficient may not apply during a changing activity step.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 2.5: Numerical discretization and stability

### Physical reasoning and derivation target

The explicit finite-difference update for one-dimensional constant-D diffusion has a simple stability condition r=DΔt/(Δx)²≤1/2 with uniform spacing and no added reaction. A conservative finite-volume scheme additionally tracks face fluxes. Changing grid spacing without changing the time step can make a once-stable scheme fail.

### Laboratory thought experiment and numerical calculation

Implement explicit and backward-Euler schemes for the same step-profile initial condition. Check total inventory under no-flux boundaries and compare convergence when spatial cells are doubled. Report discretization error separately from measurement uncertainty.

The paired local calculator for this lesson is **Diffusion length over fixed time**. Use **Diffusivity value = 3.585714 ×10⁻¹¹ m²/s** with the other parameters fixed. The model returns **359.285 μm**. Repeat the computation at **Diffusivity value = 4.377714 ×10⁻¹¹ m²/s** to obtain **396.98579 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **characteristic √(Dt), t=3600 s, constant D; not a unique physical front location**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Numerical stability does not guarantee accuracy, and a nonconservative scheme can artificially gain mass while displaying a smooth-looking curve.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which grid-refinement and integral-balance tests should precede comparison with measured profiles? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **3.585714 ×10⁻¹¹ m²/s**, and recover **359.285 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Numerical stability does not guarantee accuracy, and a nonconservative scheme can artificially gain mass while displaying a smooth-looking curve.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Transient uptake in a finite membrane

### Scientific question and competing hypotheses

An imagined polymer sheet takes up an inert vapor after its gas environment undergoes a step change. The upstream chamber maintains a nominal composition, but external boundary films may alter the surface activity. Two sheet thicknesses are available; one is thin enough that both faces eventually interact.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Implement Fick’s second law using a finite-volume grid with no internal source and either fixed-concentration or finite-transfer boundaries. Demonstrate why the initial concentration profile and both face conditions are mandatory. Begin with a case that admits an approximate semi-infinite error-function solution, then show when the finite thickness makes that approximation fail.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Collect an uptake curve and a depth profile for both thicknesses. Compare apparent time-to-half-uptake scaling against L²; measure the chamber gas composition continuously. Use a blank holder and a no-sorption reference so a balance is possible.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Sorption-induced volume changes, concentration-dependent D and concentration-dependent partitioning are omitted. A numerically stable time step is not evidence that the physical boundary model is correct.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_2 -->

<!-- MODEL_3 -->

