# Unit 6: Reaction kinetics and phase transformations

**Guiding question:** How can a process be favorable yet proceed slowly?

## Physical map and learning outcomes

A hypothetical alloy initially holds a supersaturated solute. After isothermal holding, a diffraction signal attributed to precipitates increases with time. A fitting program reports an Avrami exponent, but the researcher cannot yet distinguish fresh nucleation from growth of nuclei already present. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including imposed sample temperature, the physical boundary and the observation interval. Do not assume that the smoothness of a concentration profile confirms the absence of reactions or short-circuit paths.

Calculate first-order and generalized Avrami-type conversion trajectories on identical time axes. Compare the early and late slopes and identify how an incubation time changes fitted parameters. Estimate a classical capillarity critical radius independently, explaining why a critical radius is not a prediction of the number of nuclei formed per second. The mathematics provides a disciplined way to compare outcomes but still depends on the geometry and the meaning of the concentration variable. Across the five lessons, students should practice setting up a concrete mass or species balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson name whether its quantity is a flux, a concentration, a diffusivity, a rate constant, a transformed fraction, a physical length or a dimensionless numerical-stability ratio. A second unit conversion must be reproducible from the first. Any use of kelvin, micrometers, nanometers, molar activation energy or flux orientation should be explicit, because changing units silently can alter a processing decision by orders of magnitude.

## Lesson 6.1: Rate laws and apparent reaction order

### Physical reasoning and derivation target

A rate law expresses how an observed conversion rate depends on selected concentrations or pressures in a specified regime. Elementary molecularity and empirically fitted reaction order are not interchangeable. In heterogeneous reactions, transport limitations may produce apparent rate behavior unrelated to surface elementary steps.

### Laboratory thought experiment and numerical calculation

Use invented concentration-versus-time measurements from a batch reaction to compare zero-, first- and second-order linearizations and check residual plots, not only line fit coefficients.

The paired local calculator for this lesson is **First-order conversion**. Use **Reaction time = 342.8571 s** with the other parameters fixed. The model returns **0.40207247 fraction**. Repeat the computation at **Reaction time = 726.8571 s** to obtain **0.66387955 fraction**; the output rises when the input rises. Record the expression and its model domain exactly: **X=1−exp(−kt), constant k=0.0015 s⁻¹, single lumped first-order reaction**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Temperature drift and catalyst deactivation can masquerade as a changed reaction order, and fitted exponents outside the observed range need not predict mechanisms.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would varying particle size help diagnose whether transport rather than chemistry controls the observed rate? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **342.8571 s**, and recover **0.40207247 fraction**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Temperature drift and catalyst deactivation can masquerade as a changed reaction order, and fitted exponents outside the observed range need not predict mechanisms.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 6.2: Activated rate processes

### Physical reasoning and derivation target

Arrhenius rate constants k=A exp(−Ea/RT) are often useful over limited temperature ranges; activation energy is obtained from the slope of ln k versus 1/T, with units of J/mol. Microscopic transition-state expressions introduce an additional temperature dependence in the prefactor and should not be confused with a universal constant A.

### Laboratory thought experiment and numerical calculation

Fit synthetic rates at three temperatures to a straight Arrhenius line and compute a predicted intermediate rate. Then examine what a systematic curvature might imply.

The paired local calculator for this lesson is **Avrami-type transformed fraction**. Use **Isothermal hold duration = 1028.571 s** with the other parameters fixed. The model returns **0.38457085 fraction**. Repeat the computation at **Isothermal hold duration = 1604.571 s** to obtain **0.72506923 fraction**; the output rises when the input rises. Record the expression and its model domain exactly: **X=1−exp[−(kt)^n], k=7×10⁻⁴ s⁻¹, n=2.2, empirical; no incubation delay**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A changing catalytic surface or competing pathways can produce an apparent Ea that is not an elementary energy barrier.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What controlled experiment would show that a fitted barrier represents a changed pathway rather than experimental heating error? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1028.571 s**, and recover **0.38457085 fraction**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A changing catalytic surface or competing pathways can produce an apparent Ea that is not an elementary energy barrier.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 6.3: Classical nucleation kinetics

### Physical reasoning and derivation target

A transformed phase may require a critical fluctuation to overcome an interface-cost barrier even when bulk free energy favors transformation. Under an ideal spherical homogeneous-capillarity model, the critical radius scales as 2γ/abs(Δgv); heterogeneous nucleation can be much easier because the interfacial geometry changes.

### Laboratory thought experiment and numerical calculation

Calculate critical radii at two assumed driving magnitudes and discuss why greater undercooling can change both nucleation driving force and atomic mobility.

The paired local calculator for this lesson is **First-order conversion**. Use **Reaction time = 1028.571 s** with the other parameters fixed. The model returns **0.78623054 fraction**. Repeat the computation at **Reaction time = 1412.571 s** to obtain **0.87983111 fraction**; the output rises when the input rises. Record the expression and its model domain exactly: **X=1−exp(−kt), constant k=0.0015 s⁻¹, single lumped first-order reaction**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

The capillarity approximation assumes sharp interfaces and simple γ, and it cannot determine a real transformation rate without nucleation site statistics and kinetic prefactors.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which microstructural observation would distinguish heterogeneous nucleation from bulk homogeneous nucleation? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1028.571 s**, and recover **0.78623054 fraction**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **The capillarity approximation assumes sharp interfaces and simple γ, and it cannot determine a real transformation rate without nucleation site statistics and kinetic prefactors.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 6.4: Avrami-type transformation curves

### Physical reasoning and derivation target

A common empirical description of transformed fraction is X(t)=1−exp[−(kt)^n]. Parameters summarize growth and nucleation behavior over a specified range; the exponent n is not automatically a unique dimensionality or mechanism identifier. Impingement, incubation time and spatial heterogeneity complicate interpretation.

### Laboratory thought experiment and numerical calculation

Generate a synthetic transformation fraction at several hold times, fit n and k, then perturb one early-time datum to see how strongly the inferred exponent changes.

The paired local calculator for this lesson is **Avrami-type transformed fraction**. Use **Isothermal hold duration = 2057.143 s** with the other parameters fixed. The model returns **0.8925227 fraction**. Repeat the computation at **Isothermal hold duration = 2633.143 s** to obtain **0.97849275 fraction**; the output rises when the input rises. Record the expression and its model domain exactly: **X=1−exp[−(kt)^n], k=7×10⁻⁴ s⁻¹, n=2.2, empirical; no incubation delay**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

A transformed fraction inferred from DSC heat release may differ from XRD phase fraction if latent heat varies or baseline correction is weak.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which complementary measurement would verify that the transformed fraction has physical meaning? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **2057.143 s**, and recover **0.8925227 fraction**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A transformed fraction inferred from DSC heat release may differ from XRD phase fraction if latent heat varies or baseline correction is weak.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Lesson 6.5: Diffusion- versus interface-controlled growth

### Physical reasoning and derivation target

Interface motion may be controlled by supply of diffusing species, attachment kinetics or mixed regimes. Pure diffusion-controlled layer growth often has a characteristic square-root time dependence, while a constant interface-limited velocity can lead to near-linear growth at first.

### Laboratory thought experiment and numerical calculation

Compare two fictional precipitation reactions with identical equilibrium driving forces but different diffusion lengths. Define the front position and check the apparent power law over multiple decades in time.

The paired local calculator for this lesson is **First-order conversion**. Use **Reaction time = 1714.286 s** with the other parameters fixed. The model returns **0.92357371 fraction**. Repeat the computation at **Reaction time = 2098.286 s** to obtain **0.95703754 fraction**; the output rises when the input rises. Record the expression and its model domain exactly: **X=1−exp(−kt), constant k=0.0015 s⁻¹, single lumped first-order reaction**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output represents a rate, compare the proposed observation interval with the reciprocal rate. If it represents a length, verify dimensional scaling and relate it to a physical specimen dimension. If it represents a fraction, confirm that it remains in its allowed interval. If it represents flux, convert the result to total inventory change using an explicitly chosen area and time.

### Competing explanations and experimental controls

Different time exponents can arise from changing driving force or morphology; finite-time fits do not directly reveal a microscopic controlling step.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would a changed initial particle radius test the proposed rate-controlling mechanism? Begin with the governing balance and appropriate boundary conditions. Show the expression corresponding to the local calculator, substitute **1714.286 s**, and recover **0.92357371 fraction**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Different time exponents can arise from changing driving force or morphology; finite-time fits do not directly reveal a microscopic controlling step.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong frame, a physically impossible concentration boundary, or an inappropriate phase-specific diffusivity was chosen.

## Integrated investigation: Separating nucleation from transport-limited growth

### Scientific question and competing hypotheses

A hypothetical alloy initially holds a supersaturated solute. After isothermal holding, a diffraction signal attributed to precipitates increases with time. A fitting program reports an Avrami exponent, but the researcher cannot yet distinguish fresh nucleation from growth of nuclei already present.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the time evolution to a homogeneous bulk diffusivity; the other may emphasize a boundary step, spatial heterogeneity or phase change. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Calculate first-order and generalized Avrami-type conversion trajectories on identical time axes. Compare the early and late slopes and identify how an incubation time changes fitted parameters. Estimate a classical capillarity critical radius independently, explaining why a critical radius is not a prediction of the number of nuclei formed per second.

Begin with a local or integrated species balance. State whether sources, sinks, strain, moving interfaces and specimen volume changes are absent by observation or absent only by assumption. Show how the characteristic transport length and process time enter a dimensionless comparison; an observation interval short compared with L²/D interrogates a different regime from a long dwell. Derive the leading boundary condition from the actual proposed apparatus. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where the model represents transformed fraction, avoid substituting that fraction for a mechanical property without independent evidence. Where it represents a diffusion length, name the width or threshold convention, and do not extrapolate a one-phase coefficient through a phase transformation.

### Experimental design and quality controls

Collect microscopy at multiple time points, quantify particle counts and distributions, and measure composition changes rather than relying only on total diffraction intensity. Compare samples with intentionally changed heterogeneous nucleation site density.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each collected measurement record resolution, calibration, spatial location and a plausible systematic uncertainty. Use more than one time point and at least one geometric or compositional perturbation so a rate can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Transformation exponents are useful phenomenology but seldom identify a unique microscopic mechanism. Calibrated diffraction intensity can be influenced by strain and texture as well as phase fraction.

Suppose the synthetic fit residuals are smaller than all plotted symbols. That result demonstrates only that the chosen mathematical function can describe the synthetic observations at the chosen resolution. It does not prove a microscopic jump mechanism, validate extrapolation beyond the tested temperature interval, or establish manufacturing safety. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in kinetic parameters, competing deterioration mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A conservation equation written with signs, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic concentration or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion that separates the demonstrated mathematical relationship from the unverified behavior of a real material.

### Interactive demonstrations

<!-- MODEL_10 -->

<!-- MODEL_11 -->

