# Unit 1: Conservation, flux and microscopic motion

**Guiding question:** How can material move without creating or destroying atoms?

## Physical map and learning outcomes

A research group joins two synthetic compositionally distinct metallic blocks. It uses a color-map renderer to create concentration profiles after three anneal durations. An intern treats all apparent broadening as a bulk diffusivity even though the coupon may contain connected porosity near the joining plane. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Define a one-dimensional slice with an explicit sign convention. Derive the integrated material balance across its boundaries and then compute steady J from two separate gradients. Generate an independent random-walk ensemble using a displacement variance 2Dt and explain why the distribution width changes while the expected net displacement of a tagged tracer remains zero. Contrast the broadening profile with the net species transport caused by an initial composition gradient. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 1.1: Diffusion versus convection

### Physical reasoning and derivation target

Diffusion is caused by fluctuations and gradients in chemical potential, while advection carries species with bulk matter. In a solid coupon with no mean lattice motion, a concentration profile can broaden because individual atoms execute thermally activated random hops. In a melt or gas stream, advection may dominate the net transport.

### Laboratory thought experiment and numerical calculation

Compare two dye-tracer experiments: a motionless gel and a circulating liquid. Assign a material velocity to one experiment and not the other; write the conservation law for both situations. Quantify what a stationary camera could misinterpret as molecular diffusion.

The paired local calculator for this lesson is **Steady Fickian molar flux magnitude**. Use **Diffusion path thickness = 0.0008857143 m** with the other parameters fixed. The model returns **2.2580645e-05 mol/(m² s)**. Repeat the computation at **Diffusion path thickness = 0.001653714 m** to obtain **1.2093988e-05 mol/(m² s)**; the output falls when the input rises. Record the expression and its model domain exactly: **D=1×10⁻¹⁰ m²/s, Δc=200 mol/m³, fixed surface concentrations, planar steady state; returns positive flux magnitude**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A photographed color front is not necessarily a local composition profile. Optical absorption may be nonlinear with concentration and fluid circulation can resemble high diffusivity.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which additional measurement separates genuine molecular mixing from unnoticed bulk flow? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.0008857143 m**, and recover **2.2580645e-05 mol/(m² s)**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A photographed color front is not necessarily a local composition profile. Optical absorption may be nonlinear with concentration and fluid circulation can resemble high diffusivity.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 1.2: Flux, units and signs

### Physical reasoning and derivation target

The flux J describes the quantity crossing unit area per unit time. A molar concentration gradient and a mass-concentration gradient require different flux units; a negative sign in Fick's first law indicates net motion down concentration when D is positive. Define the positive axis before interpreting a negative calculated number.

### Laboratory thought experiment and numerical calculation

A diffusion couple joins A-rich and B-rich blocks. Fix a surface normal into the B-rich half, measure concentrations at two points, and calculate the apparent steady flux on a mole-per-volume basis.

The paired local calculator for this lesson is **One-dimensional random-walk RMS displacement**. Use **Elapsed time = 1178.571 s** with the other parameters fixed. The model returns **217.12406 μm**. Repeat the computation at **Elapsed time = 1810.571 s** to obtain **269.11495 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **1D unbiased uncorrelated random walk, D=2×10⁻¹¹ m²/s, no boundaries**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Thickness uncertainty affects the gradient directly; an apparent flux may instead be transport along a porous interface. Distinguish a true steady state from a convenient snapshot.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would reversing the coordinate axis change the sign of flux without changing physics? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1178.571 s**, and recover **217.12406 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Thickness uncertainty affects the gradient directly; an apparent flux may instead be transport along a porous interface. Distinguish a true steady state from a convenient snapshot.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 1.3: Conservation in a control volume

### Physical reasoning and derivation target

For a species with concentration c, local conservation is ∂c/∂t = −∇·J + s, where s is the net production rate per unit volume. A no-source diffusion model sets s=0, but an interfacial chemical reaction can introduce a sink for one species and a source for another. Integrating over the whole sample tests boundary accounting.

### Laboratory thought experiment and numerical calculation

Take a thin planar slab with fluxes entering and leaving its two faces. Use their numerical difference to estimate accumulation over a fixed duration; compare with a mass assay and include any species captured at the surface.

The paired local calculator for this lesson is **Steady Fickian molar flux magnitude**. Use **Diffusion path thickness = 0.002257143 m** with the other parameters fixed. The model returns **8.8607595e-06 mol/(m² s)**. Repeat the computation at **Diffusion path thickness = 0.003025143 m** to obtain **6.611258e-06 mol/(m² s)**; the output falls when the input rises. Record the expression and its model domain exactly: **D=1×10⁻¹⁰ m²/s, Δc=200 mol/m³, fixed surface concentrations, planar steady state; returns positive flux magnitude**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A net concentration change is not proof of diffusion alone if adsorption, reaction, evaporation or volumetric swelling changes the measured volume.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What balance residual would expose a missing surface flux or reaction term? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.002257143 m**, and recover **8.8607595e-06 mol/(m² s)**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A net concentration change is not proof of diffusion alone if adsorption, reaction, evaporation or volumetric swelling changes the measured volume.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 1.4: Random walks and mean-square displacement

### Physical reasoning and derivation target

An unbiased, statistically independent, one-dimensional hop model predicts mean-square displacement proportional to elapsed time; for constant diffusivity, ⟨x²⟩ = 2Dt. The factor depends on dimension: three-dimensional isotropic displacement has ⟨r²⟩ = 6Dt. A single tracer's path remains irregular and cannot represent the ensemble average.

### Laboratory thought experiment and numerical calculation

Generate many synthetic walker trajectories with random ±a jumps at fixed time steps. Plot the distribution after 10, 100 and 1000 jumps, then estimate D from ensemble mean-square displacement rather than a final net displacement of one walker.

The paired local calculator for this lesson is **One-dimensional random-walk RMS displacement**. Use **Elapsed time = 2307.143 s** with the other parameters fixed. The model returns **303.78564 μm**. Repeat the computation at **Elapsed time = 2939.143 s** to obtain **342.87857 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **1D unbiased uncorrelated random walk, D=2×10⁻¹¹ m²/s, no boundaries**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Correlated hops, trapping, anisotropy and boundaries break the simplest independent-walk assumptions; a fitted apparent D may vary with time.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What plot of mean-square displacement versus time would challenge normal diffusion? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **2307.143 s**, and recover **303.78564 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Correlated hops, trapping, anisotropy and boundaries break the simplest independent-walk assumptions; a fitted apparent D may vary with time.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 1.5: Chemical potential as driving force

### Physical reasoning and derivation target

Chemical potential is more general than a raw concentration difference. In nonideal solutions, atoms may move up a concentration gradient while still moving down an electrochemical or diffusional potential gradient. Local equilibrium assumptions permit flux-force relations involving a mobility and ∇μ rather than treating D as universally constant.

### Laboratory thought experiment and numerical calculation

Compare a binary regular solution near a miscibility gap with a dilute ideal solution. Sketch the curvature of free energy and identify where a composition gradient fails to capture the sign of chemical driving force.

The paired local calculator for this lesson is **Steady Fickian molar flux magnitude**. Use **Diffusion path thickness = 0.003628571 m** with the other parameters fixed. The model returns **5.511811e-06 mol/(m² s)**. Repeat the computation at **Diffusion path thickness = 0.004396571 m** to obtain **4.5489992e-06 mol/(m² s)**; the output falls when the input rises. Record the expression and its model domain exactly: **D=1×10⁻¹⁰ m²/s, Δc=200 mol/m³, fixed surface concentrations, planar steady state; returns positive flux magnitude**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A large negative chemical-potential slope does not by itself determine the kinetics: mobility can be small and flux can be redirected by stress or electric fields.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which simultaneous chemical and transport measurements are required to infer a mobility independently of a driving force? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **0.003628571 m**, and recover **5.511811e-06 mol/(m² s)**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A large negative chemical-potential slope does not by itself determine the kinetics: mobility can be small and flux can be redirected by stress or electric fields.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Tracer balance across a stationary diffusion couple

### Scientific question and competing hypotheses

A research group joins two synthetic compositionally distinct metallic blocks. It uses a color-map renderer to create concentration profiles after three anneal durations. An intern treats all apparent broadening as a bulk diffusivity even though the coupon may contain connected porosity near the joining plane.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Define a one-dimensional slice with an explicit sign convention. Derive the integrated material balance across its boundaries and then compute steady J from two separate gradients. Generate an independent random-walk ensemble using a displacement variance 2Dt and explain why the distribution width changes while the expected net displacement of a tagged tracer remains zero. Contrast the broadening profile with the net species transport caused by an initial composition gradient.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Measure a cross-section at zero time, run the same thermal schedule with no compositional contrast, and inspect the interface for porosity or cracks. Compare a bulk profile acquired away from the edge with a surface map; fit a separate coefficient only if those paths can be physically distinguished.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

The visualized profiles are generated from equations and not direct observations. A concentration-dependent partial molar volume, interfacial reaction or initial mixing during joining would invalidate the simplest volume-conserving model.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_0 -->

<!-- MODEL_1 -->

