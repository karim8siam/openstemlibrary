# Unit 4: Interfaces, microstructure and coupled driving forces

**Guiding question:** When does a bulk diffusion coefficient fail to capture real transport?

## Physical map and learning outcomes

Two porous oxide ceramics contain equal chemical compositions but have different grain sizes and pore connectivity. A tracer section exhibits a long tail in one specimen. The investigator attempts to fit one uniform diffusivity to both the central profile and the tail. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Construct separate conduction analogies for connected fast paths and lattice regions. Compare the parallel-path estimate with a series-path lower-bound. Map boundary coverage as a function of depth, and show how changing geometry alone alters effective permeability even if each phase’s intrinsic coefficient remains unchanged. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 4.1: Grain-boundary transport

### Physical reasoning and derivation target

Grain boundaries can provide pathways with mobilities different from bulk lattice diffusion. Their contributions depend on grain size, boundary connectivity, segregation and the ratio of penetration depth to geometric dimensions. Boundary transport often produces long concentration-profile tails, but the governing regime must be identified before a coefficient is estimated.

### Laboratory thought experiment and numerical calculation

Prepare two nominally identical polycrystals with different grain sizes and compare tracer penetration profiles after equal thermal exposure. Inspect whether the profiles can be decomposed into a lattice component and a boundary-enhanced tail.

The paired local calculator for this lesson is **Parallel-path effective diffusion estimate**. Use **Connected fast-path area fraction = 0.02857143 fraction** with the other parameters fixed. The model returns **2.8668571e-13 m²/s**. Repeat the computation at **Connected fast-path area fraction = 0.06057143 fraction** to obtain **6.0665371e-13 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **parallel conducting paths only, Dbulk=10⁻¹⁵ and Dfast=10⁻¹¹ m²/s; ignores tortuosity and segregation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Boundary phases and precipitation can block an apparently fast path; a smaller grain size is not universally equivalent to greater effective diffusivity.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What microstructural characterization would be needed before fitting a grain-boundary diffusion regime? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.02857143 fraction**, and recover **2.8668571e-13 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Boundary phases and precipitation can block an apparently fast path; a smaller grain size is not universally equivalent to greater effective diffusivity.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 4.2: Surface diffusion and capillarity

### Physical reasoning and derivation target

Atoms on a clean surface can diffuse under gradients of surface chemical potential, which may arise from curvature or composition. In some models the flux is related to ∇sμ, and surface diffusion can reshape features while conserving bulk volume. Local attachment and detachment kinetics may still influence the observed morphology.

### Laboratory thought experiment and numerical calculation

Imagine a sinusoidal surface corrugation on a single crystal that smooths during annealing. Record feature wavelength and amplitude, and compare two possible transport mechanisms with distinct wavelength dependences.

The paired local calculator for this lesson is **Electric-field ionic drift speed magnitude**. Use **Electric field magnitude = 2928.571 V/m** with the other parameters fixed. The model returns **97.099029 nm/s**. Repeat the computation at **Electric field magnitude = 4512.571 V/m** to obtain **149.61776 nm/s**; the output rises when the input rises. Record the expression and its model domain exactly: **Nernst–Einstein mobility, monovalent species, D=2×10⁻¹² m²/s, T=700 K; field kept constant**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Evaporation–condensation, viscous flow and surface reactions may also smooth the surface; observing a lower roughness alone does not identify surface diffusion.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which change in the feature wavelength would discriminate surface diffusion from another smoothing mechanism? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **2928.571 V/m**, and recover **97.099029 nm/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Evaporation–condensation, viscous flow and surface reactions may also smooth the surface; observing a lower roughness alone does not identify surface diffusion.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 4.3: Anisotropic diffusion tensors

### Physical reasoning and derivation target

In a low-symmetry crystal, the diffusivity may be a tensor rather than a scalar. The flux J=−D·∇c need not align with ∇c, and tensor components must satisfy appropriate symmetry and positivity constraints. Averaging crystals into a polycrystal can conceal directional transport.

### Laboratory thought experiment and numerical calculation

Expose single-crystal plates cut along different crystallographic directions to identical tracer doses. Estimate an effective diffusion length along each axis and compare the ratio with a proposed tensor description.

The paired local calculator for this lesson is **Parallel-path effective diffusion estimate**. Use **Connected fast-path area fraction = 0.08571429 fraction** with the other parameters fixed. The model returns **8.5805714e-13 m²/s**. Repeat the computation at **Connected fast-path area fraction = 0.1177143 fraction** to obtain **1.1780251e-12 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **parallel conducting paths only, Dbulk=10⁻¹⁵ and Dfast=10⁻¹¹ m²/s; ignores tortuosity and segregation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Mounting errors, crystallographic misorientation and damage near the cut surface can mimic anisotropy.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How should a rotation of the sample coordinate system transform the diffusivity tensor? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.08571429 fraction**, and recover **8.5805714e-13 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Mounting errors, crystallographic misorientation and damage near the cut surface can mimic anisotropy.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 4.4: Stress- and electric-field-assisted diffusion

### Physical reasoning and derivation target

Stress gradients and electrochemical potential gradients can contribute to the driving force for atomic or ionic migration. One must distinguish electron current, charged defect flux and neutral atom flux. For a species with effective charge, the electrochemical potential includes a zFφ contribution on a molar basis.

### Laboratory thought experiment and numerical calculation

Analyze a hypothetical ionic conductor under an applied potential difference and compare its flux to a zero-field concentration-gradient experiment. Include blocking versus nonblocking electrodes in the boundary model.

The paired local calculator for this lesson is **Electric-field ionic drift speed magnitude**. Use **Electric field magnitude = 5757.143 V/m** with the other parameters fixed. The model returns **190.88248 nm/s**. Repeat the computation at **Electric field magnitude = 7341.143 V/m** to obtain **243.40122 nm/s**; the output rises when the input rises. Record the expression and its model domain exactly: **Nernst–Einstein mobility, monovalent species, D=2×10⁻¹² m²/s, T=700 K; field kept constant**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Joule heating, electrochemical reactions and electromigration-induced stress may create an apparent mobility change that is not purely field driven.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which electrical control helps separate drift from temperature-mediated acceleration? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **5757.143 V/m**, and recover **190.88248 nm/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Joule heating, electrochemical reactions and electromigration-induced stress may create an apparent mobility change that is not purely field driven.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 4.5: Porosity, composites and effective transport

### Physical reasoning and derivation target

Transport through a multiphase specimen depends on connected pathways and tortuosity. An effective coefficient is geometry- and boundary-condition-dependent; simple mixture averages can be very poor near percolation or when one phase isolates the other. Partitioning at phase boundaries also matters.

### Laboratory thought experiment and numerical calculation

Build two synthetic diffusion networks with equal phase fractions but different connectivity. Compare through-thickness steady flux and explain why volume fraction alone cannot recover effective diffusivity.

The paired local calculator for this lesson is **Parallel-path effective diffusion estimate**. Use **Connected fast-path area fraction = 0.1428571 fraction** with the other parameters fixed. The model returns **1.4294286e-12 m²/s**. Repeat the computation at **Connected fast-path area fraction = 0.1748571 fraction** to obtain **1.7493966e-12 m²/s**; the output rises when the input rises. Record the expression and its model domain exactly: **parallel conducting paths only, Dbulk=10⁻¹⁵ and Dfast=10⁻¹¹ m²/s; ignores tortuosity and segregation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A measured leakage path at an edge can dominate permeability of a porous coating; the bulk composite model may then describe the wrong physical route.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which cross-sectional image or tracer map would reveal a short-circuit transport path? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.1428571 fraction**, and recover **1.4294286e-12 m²/s**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A measured leakage path at an edge can dominate permeability of a porous coating; the bulk composite model may then describe the wrong physical route.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Bulk versus boundary transport in a ceramic

### Scientific question and competing hypotheses

Two porous oxide ceramics contain equal chemical compositions but have different grain sizes and pore connectivity. A tracer section exhibits a long tail in one specimen. The investigator attempts to fit one uniform diffusivity to both the central profile and the tail.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Construct separate conduction analogies for connected fast paths and lattice regions. Compare the parallel-path estimate with a series-path lower-bound. Map boundary coverage as a function of depth, and show how changing geometry alone alters effective permeability even if each phase’s intrinsic coefficient remains unchanged.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Measure grain-size distributions and pore pathways by microscopy, perform a single-crystal or large-grain control, and measure tracer penetration from distinct specimen faces. Test whether the tail disappears when accessible surfaces are sealed.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

The two-path network is an illustrative effective-medium model, not a general grain-boundary diffusion solution. Boundary segregation, porosity and anisotropic defect chemistry may change the transport mechanism.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_6 -->

<!-- MODEL_7 -->

