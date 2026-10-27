# Unit 4: Thin films, interference coatings and resonators

**Guiding question:** How can optical path and boundary phase be engineered into spectral filters without overlooking absorption, angle and fabrication tolerance?

## Introduction and measurement challenges

Dielectric stacks turn nanometre-scale thickness differences into visible changes in spectral response. Their design requires complex amplitudes and phase, because the sum of reflected powers is generally not the reflected power of the coherent system.

Fabrication tolerances, strain, roughness and environmental aging can dominate differences between a clean transfer-matrix prediction and a manufactured coating.

These five lessons emphasize **coherent layer interference**, and distinguish **single-interface losses versus multilayer interference**. To reproduce a study, specify **film thickness, incidence angle and deposition gradients** before collecting data; otherwise **roughness or absorbing interfaces** may mimic the desired optical response. A proposed independent validation is **angle-resolved reflectometry and cross-sectional metrology**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 4.1 — Optical phase in multilayer stacks

### Physical mechanism and field interpretation

A dielectric layer accumulates propagation phase according to refractive index, thickness and incidence angle. Multiple interfaces produce repeated reflections and coherent superposition, which can amplify or cancel net reflected power. Transfer matrices combine propagation and interface conditions for planar stratified materials. Real deposition processes often yield a graded composition, nonuniform thickness or substrate backside reflection that makes a nominal thin-film design differ from optical measurement.

**Core equation and domain.** For a single normal-incidence layer, quarter-wave optical thickness requires n d=λ0/4; multilayer phase is not equivalent to summing individual reflected powers. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**optical phase in multilayer stacks**—the most consequential distinction in this unit is **single-interface losses versus multilayer interference**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Evaluate a single coating intended to reduce reflection near 600 nm. Move the design wavelength across the visible band and ask whether the minimum stays fixed under oblique illumination. Explain why placing a film on both sides of a window requires treatment of two optical paths.

Perform a thought experiment: assume the original explanation is wrong and **roughness or absorbing interfaces** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **film thickness, incidence angle and deposition gradients** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Quarter-wave dielectric-layer thickness** isolates a single physical dependence, using **Design vacuum wavelength** as its variable. Substitute **475 nm** into its declared expression `lam/(4*1.45)` to obtain **81.8965517 nm**. For the second case use **550 nm**, obtaining **94.8275862 nm**. The output rises between these two cases. The finite-difference slope is **0.172413793 (nm)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Normal incidence, nonabsorbing material n=1.45, quarter-wave optical thickness and zero dispersion. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A quarter-wave thickness rule does not by itself guarantee zero reflection; ideal single-layer antireflection at normal incidence also requires the appropriate matching index. Absorbing or birefringent films need complex and polarization-dependent analysis.

### Experimental characterization and controls

Conduct an **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization Follow with a **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **roughness or absorbing interfaces**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **optical phase in multilayer stacks** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **film thickness, incidence angle and deposition gradients** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **optical phase in multilayer stacks** depends on **coherent layer interference**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **81.8965517 nm** for the first stated input and **94.8275862 nm** for the second. Determine the finite-difference sensitivity **0.172413793 (nm)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **roughness or absorbing interfaces** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **angle-resolved reflectometry and cross-sectional metrology**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_6 -->

## Lesson 4.2 — Antireflection coatings and spectral bandwidth

### Physical mechanism and field interpretation

An ideal antireflection layer uses destructive interference of front and rear interface reflections. Broadband performance requires multiple effective optical admittances, graded media or nanostructuring; all add processing and contamination challenges. Even a perfectly optimized coating can have angle- and polarization-dependent color shifts because optical thickness changes along oblique paths. In solar covers and lenses, scratch resistance and environmental durability may outweigh a small gain in initial normal-incidence transmission.

**Core equation and domain.** For air–film–substrate matching at normal incidence, nfilm≈sqrt(nair nsubstrate) under ideal lossless single-wavelength conditions. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**antireflection coatings and spectral bandwidth**—the most consequential distinction in this unit is **single-interface losses versus multilayer interference**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Design a comparison among an uncoated glass plate, a single-layer quarter-wave coating and a multilayer broad-band design. Specify reflectance from both sides over incidence angle and wavelength, then propose an accelerated durability test.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Fabry–Pérot ideal power transmission** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **600 nm** into its declared expression `100/(1+(4*0.3/Math.pow(1-0.3,2))*Math.pow(Math.sin(2*Math.PI*1.5*1000/lam),2))` to obtain **100 %**. For the second case use **650 nm**, obtaining **31.8366543 %**. The output falls between these two cases. The finite-difference slope is **-1.36326691 (%)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Symmetric lossless cavity with mirror power reflectance R=0.3, spacer thickness 1000 nm, n=1.5; no phase shifts or angle effects. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Do not claim a broadband benefit from a plot computed only at the design wavelength. Coating stress, adhesion, moisture uptake and cleaning abrasion must be evaluated on production-representative surfaces. A model ignoring substrate rear-surface interference may misplace fringes.

### Experimental characterization and controls

Conduct an **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples Follow with a **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **roughness or absorbing interfaces**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **antireflection coatings and spectral bandwidth** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **film thickness, incidence angle and deposition gradients** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **antireflection coatings and spectral bandwidth** depends on **coherent layer interference**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **100 %** for the first stated input and **31.8366543 %** for the second. Determine the finite-difference sensitivity **-1.36326691 (%)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 4.3 — Bragg stacks and photonic stop bands

### Physical mechanism and field interpretation

Alternating high- and low-index quarter-wave layers can create a stop band through repeated coherent interference. Index contrast increases spectral reflectance and affects stop-band width, while the number of periods controls edge steepness and peak reflectance in an ideal uniform stack. Introducing a defect layer may create a localized transmission resonance. Optical thickness control, interface roughness and thermal stress become more demanding as the layer count rises.

**Core equation and domain.** The nominal Bragg center for normal incidence obeys nHdH=nLdL=λ0/4; full spectra require coherent multilayer calculations. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**bragg stacks and photonic stop bands**—the most consequential distinction in this unit is **single-interface losses versus multilayer interference**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare two Bragg mirrors with the same central wavelength but different index contrast. Distinguish increased reflectance caused by index contrast from increased reflectance caused by additional periods. How would a thickness gradient appear in spatially resolved spectra?

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Quarter-wave dielectric-layer thickness** isolates a single physical dependence, using **Design vacuum wavelength** as its variable. Substitute **625 nm** into its declared expression `lam/(4*1.45)` to obtain **107.758621 nm**. For the second case use **700 nm**, obtaining **120.689655 nm**. The output rises between these two cases. The finite-difference slope is **0.172413793 (nm)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The intuitive quarter-wave picture does not prove complete three-dimensional photonic band gaps. A one-dimensional stack blocks certain incident modes; polarization, angle, absorption and termination affect the spectrum. A high reflectance at one wavelength does not imply acceptable laser-damage performance.

### Experimental characterization and controls

Conduct an **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration Follow with a **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **roughness or absorbing interfaces**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **bragg stacks and photonic stop bands** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **film thickness, incidence angle and deposition gradients** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **bragg stacks and photonic stop bands** depends on **coherent layer interference**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **107.758621 nm** for the first stated input and **120.689655 nm** for the second. Determine the finite-difference sensitivity **0.172413793 (nm)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 4.4 — Fabry–Pérot resonances and linewidth

### Physical mechanism and field interpretation

Two partially reflecting interfaces support multiple-pass interference and sharp transmission maxima when round-trip phase is an integer multiple of 2π. A higher mirror reflectance often sharpens resonances but reduces bandwidth; absorption can spoil peak throughput. The free spectral range and cavity linewidth depend on phase accumulation, dispersion and mirror phase shifts. Thermal drift can move a resonance by many linewidths in a high-Q device, and environmental vibration matters for macroscopic cavities.

**Core equation and domain.** Ideal Airy transmission at normal incidence: T=1/[1+F sin²(δ/2)] with F=4R/(1−R)² and δ=4πnL/λ0. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**fabry–pérot resonances and linewidth**—the most consequential distinction in this unit is **single-interface losses versus multilayer interference**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Plot the synthetic transmission of an ideal millimetre-scale optical-path spacer across wavelength and locate adjacent peaks. Explain why a resonance appears at a wavelength different from the one predicted by a constant index when the actual coating disperses.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Fabry–Pérot ideal power transmission** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **700 nm** into its declared expression `100/(1+(4*0.3/Math.pow(1-0.3,2))*Math.pow(Math.sin(2*Math.PI*1.5*1000/lam),2))` to obtain **40.0486285 %**. For the second case use **750 nm**, obtaining **100 %**. The output rises between these two cases. The finite-difference slope is **1.19902743 (%)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The Airy formula in the calculator assumes symmetric lossless reflectors; a lossy asymmetric cavity needs coupled-mode or transfer-matrix analysis. Quality factor Q=λ/Δλ requires a consistent definition of full width and can vary with wavelength.

### Experimental characterization and controls

Conduct an **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum Follow with a **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **roughness or absorbing interfaces**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **fabry–pérot resonances and linewidth** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **film thickness, incidence angle and deposition gradients** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **fabry–pérot resonances and linewidth** depends on **coherent layer interference**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **40.0486285 %** for the first stated input and **100 %** for the second. Determine the finite-difference sensitivity **1.19902743 (%)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_7 -->

## Lesson 4.5 — Microcavities, defect modes and integrated filters

### Physical mechanism and field interpretation

Localized optical modes can emerge from ring resonators, point defects in photonic crystals or microdisks. Their use depends on optical confinement, radiation leakage, absorption, coupling and fabrication reproducibility. High intrinsic quality factor and high through-port extinction are not equivalent objectives; coupling must be engineered for the intended readout. Backscattering can split resonances into doublets, and nonlinear thermal effects can distort what appears to be a symmetric spectral line.

**Core equation and domain.** For small loss and one isolated resonance, Qloaded−1=Qintrinsic−1+Qcoupling−1 (inverse-Q addition). This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**microcavities, defect modes and integrated filters**—the most consequential distinction in this unit is **single-interface losses versus multilayer interference**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Suppose a fabricated ring exhibits broad resonance dips but a simulated isolated cavity has high intrinsic Q. List measurements that distinguish material absorption, sidewall roughness, excess coupling and instrument resolution. Identify which parameter each measurement constrains.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Quarter-wave dielectric-layer thickness** isolates a single physical dependence, using **Design vacuum wavelength** as its variable. Substitute **775 nm** into its declared expression `lam/(4*1.45)` to obtain **133.62069 nm**. For the second case use **850 nm**, obtaining **146.551724 nm**. The output rises between these two cases. The finite-difference slope is **0.172413793 (nm)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A photonic-crystal band structure calculation assumes a unit cell and perfectly periodic boundaries unless defects are explicitly included. Device performance requires coupling, out-of-plane radiation and packaging tests; no one-parameter slider captures these losses.

### Experimental characterization and controls

A viable first study begins with **resonance linewidth characterization**, recording **laser wavelength trace, sweep direction and instrument resolution**. Verify the interpretation using **time-domain decay or independently calibrated high-resolution spectroscopy**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests Follow with a **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **roughness or absorbing interfaces**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **microcavities, defect modes and integrated filters** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **film thickness, incidence angle and deposition gradients** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **microcavities, defect modes and integrated filters** depends on **coherent layer interference**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **133.62069 nm** for the first stated input and **146.551724 nm** for the second. Determine the finite-difference sensitivity **0.172413793 (nm)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Fabricated multilayer interference filter

### The decision to be made

A fabricated wavelength filter has its stop-band minimum shifted from the design value. The coating team suspects deposition thickness drift; the optical team proposes index dispersion or substrate reflections. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Estimate quarter-wave design thickness and examine an ideal Fabry–Pérot fringe sequence; do not conflate this single cavity model with a multilayer stack solver. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Cross-section several wafer positions, measure reflectance versus angle/polarization and fit a transfer-matrix model with physically bounded layer variables. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A fitting algorithm can trade off thickness and index without proving either nominal layer value.

### Five end-of-unit questions

