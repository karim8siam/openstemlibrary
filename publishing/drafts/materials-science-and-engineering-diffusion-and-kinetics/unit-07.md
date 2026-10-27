# Unit 7: Microstructural evolution and heat treatments

**Guiding question:** Why does processing history govern microstructure at the same composition?

## Physical map and learning outcomes

A rolled alloy is annealed long enough that precipitates coarsen, grains grow and dislocation density declines. A single microhardness curve shows an early maximum followed by decline. A technician attributes the decline solely to particle growth. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Build an ideal cube-law precipitate-radius model and a separate square-law grain-size model. Plot their rates in a common time interval without equating the model constants or units. Construct a diagnostic table linking plausible microstructure responses to hardness, texture and electrical resistivity. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 7.1: Precipitation hardening sequences

### Physical reasoning and derivation target

Supersaturated alloys may form clusters, coherent precipitates and coarser particles along a sequence governed by nucleation, solute diffusion and interface energetics. Strength can peak before the thermodynamic equilibrium microstructure is achieved; overaging often reduces obstacle effectiveness despite continued transformation.

### Laboratory thought experiment and numerical calculation

Construct synthetic hardness-versus-aging-time curves at two temperatures and connect their peak shifts with accelerated transport and precipitation. Specify transmission microscopy or scattering needed to substantiate the explanation.

The paired local calculator for this lesson is **Ostwald coarsening radius**. Use **Aging duration = 4285.714 s** with the other parameters fixed. The model returns **15.897597 nm**. Repeat the computation at **Aging duration = 9085.714 s** to obtain **16.795541 nm**; the output rises when the input rises. Record the expression and its model domain exactly: **R³=R0³+Kt, R0=15 nm, K=0.15 nm³/s; dilute diffusion-controlled spherical approximation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Hardness trends alone cannot determine precipitate chemistry or distribution; competing recovery and grain growth processes may also alter strength.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which pair of microstructural metrics helps distinguish strengthening from recovery? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **4285.714 s**, and recover **15.897597 nm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Hardness trends alone cannot determine precipitate chemistry or distribution; competing recovery and grain growth processes may also alter strength.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 7.2: Coarsening and Ostwald ripening

### Physical reasoning and derivation target

For an ideal diffusion-controlled dispersed phase, a characteristic particle size may obey R³−R0³=Kt in an appropriate Lifshitz–Slyozov–Wagner limit. Coarsening redistributes mass among particles and can reduce total interface area, but volume fraction and diffusion assumptions matter.

### Laboratory thought experiment and numerical calculation

Use invented particle radii at several aging times to fit a cubic growth trend. Check if the particle-size distribution changes, not merely the average radius.

The paired local calculator for this lesson is **Idealized grain-growth size**. Use **Annealing duration = 8571.429 s** with the other parameters fixed. The model returns **15.343682 μm**. Repeat the computation at **Annealing duration = 13371.43 s** to obtain **18.20518 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **G²=G0²+Kt, G0=8 μm and K=0.02 μm²/s, isotropic unpinned grains**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Elastic interactions, high particle fraction and nonspherical shapes violate classical dilute-system theory and can change the exponent.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would a change in particle number density help test whether coarsening rather than fresh nucleation dominates? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **8571.429 s**, and recover **15.343682 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Elastic interactions, high particle fraction and nonspherical shapes violate classical dilute-system theory and can change the exponent.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 7.3: Grain growth and boundary mobility

### Physical reasoning and derivation target

Normal grain growth can be approximated by G^n−G0^n=Kt for suitable definitions and regimes. The exponent and rate depend on boundary mobility, curvature pressure, anisotropy and pinning. Solute drag and second-phase particles can severely reduce growth.

### Laboratory thought experiment and numerical calculation

Compare a clean synthetic polycrystal and a particle-pinned one at equal temperature. Track grain-size distributions, and evaluate whether using a single average obscures abnormal growth.

The paired local calculator for this lesson is **Ostwald coarsening radius**. Use **Aging duration = 12857.14 s** with the other parameters fixed. The model returns **17.439049 nm**. Repeat the computation at **Aging duration = 17657.14 s** to obtain **18.19497 nm**; the output rises when the input rises. Record the expression and its model domain exactly: **R³=R0³+Kt, R0=15 nm, K=0.15 nm³/s; dilute diffusion-controlled spherical approximation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A microscopy area-to-diameter conversion and incomplete three-dimensional sampling can change measured growth exponents.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What statistically adequate image analysis would support a claimed pinning effect? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **12857.14 s**, and recover **17.439049 nm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A microscopy area-to-diameter conversion and incomplete three-dimensional sampling can change measured growth exponents.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 7.4: Recovery and recrystallization

### Physical reasoning and derivation target

Stored deformation energy can drive dislocation rearrangement and formation of new low-dislocation-density grains during annealing. Recovery may reduce residual stress before significant new-grain formation, and recrystallization kinetics depend on prior cold work and heating history.

### Laboratory thought experiment and numerical calculation

Take two imaginary cold-rolled alloy strips with different reductions and anneal them at the same temperature. Compare hardness, diffraction peak width and orientation maps over time.

The paired local calculator for this lesson is **Idealized grain-growth size**. Use **Annealing duration = 17142.86 s** with the other parameters fixed. The model returns **20.1707 μm**. Repeat the computation at **Annealing duration = 21942.86 s** to obtain **22.424476 μm**; the output rises when the input rises. Record the expression and its model domain exactly: **G²=G0²+Kt, G0=8 μm and K=0.02 μm²/s, isotropic unpinned grains**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Thermal exposure can also cause precipitation or grain growth, confounding an interpretation based solely on decreasing hardness.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which orientation-resolved measurement separates recovery from recrystallization? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **17142.86 s**, and recover **20.1707 μm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Thermal exposure can also cause precipitation or grain growth, confounding an interpretation based solely on decreasing hardness.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 7.5: Sintering and densification

### Physical reasoning and derivation target

Sintering couples surface curvature, grain-boundary transport, bulk diffusion, pore movement and sometimes viscous flow. Neck formation does not guarantee densification, because some surface-diffusion mechanisms redistribute material without reducing the total pore volume.

### Laboratory thought experiment and numerical calculation

Model a powder compact with evolving neck size and porosity under two hypothetical temperature programs. Record linear shrinkage, density and grain size as distinct outputs.

The paired local calculator for this lesson is **Ostwald coarsening radius**. Use **Aging duration = 21428.57 s** with the other parameters fixed. The model returns **18.747619 nm**. Repeat the computation at **Aging duration = 26228.57 s** to obtain **19.406996 nm**; the output rises when the input rises. Record the expression and its model domain exactly: **R³=R0³+Kt, R0=15 nm, K=0.15 nm³/s; dilute diffusion-controlled spherical approximation**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Rapid grain growth can trap pores and lower final density; a densification prediction requires transport and mechanical boundary conditions beyond a single Arrhenius rate.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How can simultaneous dilatometry and microscopy distinguish neck growth from true densification? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **21428.57 s**, and recover **18.747619 nm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Rapid grain growth can trap pores and lower final density; a densification prediction requires transport and mechanical boundary conditions beyond a single Arrhenius rate.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Competing coarsening and grain-growth processes

### Scientific question and competing hypotheses

A rolled alloy is annealed long enough that precipitates coarsen, grains grow and dislocation density declines. A single microhardness curve shows an early maximum followed by decline. A technician attributes the decline solely to particle growth.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Build an ideal cube-law precipitate-radius model and a separate square-law grain-size model. Plot their rates in a common time interval without equating the model constants or units. Construct a diagnostic table linking plausible microstructure responses to hardness, texture and electrical resistivity.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Use quantitative particle radius distributions, electron backscatter diffraction and dislocation-density-sensitive diffraction analysis across aging times. Repeat after a controlled pre-strain change to test the influence of recrystallization.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Classical coarsening assumes a dilute population and simplified interfacial energy; ideal grain-growth laws ignore pinning and abnormal growth. Hardness cannot uniquely deconvolve these concurrent contributions.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_12 -->

<!-- MODEL_13 -->

