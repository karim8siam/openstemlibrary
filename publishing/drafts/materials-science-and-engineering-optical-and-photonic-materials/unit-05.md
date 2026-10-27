# Unit 5: Waveguides, optical fibers and integrated photonics

**Guiding question:** Which material and geometry parameters control supported modes, attenuation and practical optical interconnect reliability?

## Introduction and measurement challenges

Integrated photonics and fibers rely on modes rather than single rays. Geometry, refractive-index contrast and surface conditions jointly determine confinement and modal attenuation.

An optical link is a system of source, couplers, guides, connectors and detector. A low-loss bulk material by itself does not guarantee a low-loss fabricated waveguide.

These five lessons emphasize **guided electromagnetic modes**, and distinguish **bulk optical constants versus modal loss**. To reproduce a study, specify **core geometry, modal launch and wavelength** before collecting data; otherwise **coupler loss, bending or sidewall roughness** may mimic the desired optical response. A proposed independent validation is **length-series cut-back with mode-resolved imaging**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 5.1 — Confinement and effective refractive index

### Physical mechanism and field interpretation

Guided waves satisfy Maxwell boundary conditions in a transverse index profile and propagate with a modal propagation constant β. The effective index neff=β/k0 lies between appropriate material indices for many conventional dielectric guided modes; its wavelength dependence includes both material and waveguide dispersion. Mode area, confinement fraction and polarization depend strongly on geometry. A rib waveguide can support leakage modes even when a simple slab model predicts confinement, because etched sidewalls introduce additional dimensions.

**Core equation and domain.** A guided mode has β=neff(2π/λ0), where neff describes a mode rather than a bulk material index. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**confinement and effective refractive index**—the most consequential distinction in this unit is **bulk optical constants versus modal loss**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Consider a high-index core on a lower-index substrate. Increase core thickness while leaving wavelength fixed. Predict how mode confinement and effective index change, then explain why a measured phase delay cannot independently identify thickness and bulk material index.

Perform a thought experiment: assume the original explanation is wrong and **coupler loss, bending or sidewall roughness** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **core geometry, modal launch and wavelength** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Step-index fiber normalized frequency V** isolates a single physical dependence, using **Core radius** as its variable. Substitute **2.5 µm** into its declared expression `(2*Math.PI*a/1.55)*Math.sqrt(1.450*1.450-1.444*1.444)` to obtain **1.33540521 dimensionless**. For the second case use **3 µm**, obtaining **1.60248626 dimensionless**. The output rises between these two cases. The finite-difference slope is **0.534162085 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Circular ideal weak-guidance step-index fiber, λ=1.55 µm, ncore=1.450, nclad=1.444; LP11 cutoff V≈2.405 for idealized fiber. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Effective-index methods are approximations; sharp corners, high-index contrast, surface scattering and anisotropic materials can require vector finite-element or finite-difference eigenmode solvers. Optical confinement does not eliminate absorption from dopants or adjacent electrodes.

### Experimental characterization and controls

Conduct an **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples Follow with a **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **coupler loss, bending or sidewall roughness**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **confinement and effective refractive index** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **core geometry, modal launch and wavelength** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **confinement and effective refractive index** depends on **guided electromagnetic modes**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.33540521 dimensionless** for the first stated input and **1.60248626 dimensionless** for the second. Determine the finite-difference sensitivity **0.534162085 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **coupler loss, bending or sidewall roughness** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **length-series cut-back with mode-resolved imaging**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_8 -->

## Lesson 5.2 — Step-index fiber V number and modal cutoff

### Physical mechanism and field interpretation

The normalized frequency V combines core radius, vacuum wavelength and refractive-index contrast into one dimensionless measure for ideal circular step-index fibers. In weak guidance, the next higher-order LP11 mode reaches cutoff at about V=2.405; V below that threshold is a useful single-mode criterion for this idealized profile. This does not mean the fundamental mode disappears for small V, nor does it account for bend loss and manufacturing imperfections. Dopant diffusion and stress can produce graded profiles that change cutoff behavior.

**Core equation and domain.** V=(2πa/λ0)sqrt(ncore²−nclad²); for an ideal weak-guidance step-index fiber, LP11 appears near V≈2.405. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**step-index fiber v number and modal cutoff**—the most consequential distinction in this unit is **bulk optical constants versus modal loss**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Sweep core radius in the calculator with fixed indices and 1.55 µm wavelength. Determine which part of the range exceeds the next-mode cutoff. Then describe why an intentionally coiled sample may still lose light when the straight fiber is theoretically single-mode.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Fiber power after uniform dB attenuation** isolates a single physical dependence, using **Fiber length** as its variable. Substitute **20 km** into its declared expression `100*Math.pow(10,-0.2*L/10)` to obtain **39.8107171 %**. For the second case use **30 km**, obtaining **25.1188643 %**. The output falls between these two cases. The finite-difference slope is **-1.46918527 (%)/(km)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Fiber attenuation 0.2 dB/km constant across length; neglects splice losses, reflections and wavelength changes. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Real single-mode operation also depends on excitation and finite device length; a nominally multimode fiber may behave effectively single-mode when higher-order modes are strongly attenuated. Broadband fiber specifications require cutoff and loss tests at multiple wavelengths.

### Experimental characterization and controls

Conduct an **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration Follow with a **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **coupler loss, bending or sidewall roughness**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **step-index fiber v number and modal cutoff** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **core geometry, modal launch and wavelength** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **step-index fiber v number and modal cutoff** depends on **guided electromagnetic modes**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **39.8107171 %** for the first stated input and **25.1188643 %** for the second. Determine the finite-difference sensitivity **-1.46918527 (%)/(km)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 5.3 — Optical fiber attenuation and link budget

### Physical mechanism and field interpretation

Power decibels express logarithmic ratios, enabling additive bookkeeping of distributed attenuation, connectors and splices. A coefficient in dB/km is not numerically the same as a natural-exponential absorption coefficient in km⁻¹; conversion requires ln(10)/10 for power. Long-haul links may be limited by amplified spontaneous emission, chromatic dispersion or nonlinearities, not only passive attenuation. Fiber purity, hydrogen-related absorption, microbending and bends contribute differently across wavelength and operating environment.

**Core equation and domain.** Pout/Pin=10^(−αdB L/10), with αdB in dB/km and L in km for pure distributed power loss. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**optical fiber attenuation and link budget**—the most consequential distinction in this unit is **bulk optical constants versus modal loss**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

At an assumed 0.2 dB/km, calculate how much launched optical power survives 25 km before connectors. Add a pair of hypothetical splice losses and compare the total in linear percent versus dB. Explain why photon counting statistics affect low-power operation.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Step-index fiber normalized frequency V** isolates a single physical dependence, using **Core radius** as its variable. Substitute **3.5 µm** into its declared expression `(2*Math.PI*a/1.55)*Math.sqrt(1.450*1.450-1.444*1.444)` to obtain **1.8695673 dimensionless**. For the second case use **4 µm**, obtaining **2.13664834 dimensionless**. The output rises between these two cases. The finite-difference slope is **0.534162085 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A scalar attenuation model cannot identify Rayleigh scattering, OH absorption or bend-induced leakage individually. Connector return loss is distinct from insertion loss. Link margin should include aging and temperature extremes rather than relying only on an ideal best-case value.

### Experimental characterization and controls

Conduct an **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum Follow with a **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **coupler loss, bending or sidewall roughness**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **optical fiber attenuation and link budget** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **core geometry, modal launch and wavelength** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **optical fiber attenuation and link budget** depends on **guided electromagnetic modes**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.8695673 dimensionless** for the first stated input and **2.13664834 dimensionless** for the second. Determine the finite-difference sensitivity **0.534162085 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 5.4 — Waveguide dispersion and pulse spreading

### Physical mechanism and field interpretation

Optical pulses contain a range of frequencies. The frequency dependence of modal propagation constant defines group delay and its second derivative defines group-velocity dispersion. Even a material with weak intrinsic dispersion can support strongly dispersive guided modes near cutoff or anticrossings. The sign and magnitude of dispersion determine whether different spectral components spread or compress under a given chirp. Higher-order dispersion matters for short pulses and wide optical bandwidths.

**Core equation and domain.** β2=d²β/dω², with units s²/m; a common dispersion parameter is D=−(2πc/λ0²)β2. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**waveguide dispersion and pulse spreading**—the most consequential distinction in this unit is **bulk optical constants versus modal loss**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare two hypothetical waveguide geometries using the same glass. One has a small core and steep effective-index variation, the other a wide core. Explain why material composition alone is insufficient to predict their femtosecond-pulse response.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Fiber power after uniform dB attenuation** isolates a single physical dependence, using **Fiber length** as its variable. Substitute **40 km** into its declared expression `100*Math.pow(10,-0.2*L/10)` to obtain **15.8489319 %**. For the second case use **50 km**, obtaining **10 %**. The output falls between these two cases. The finite-difference slope is **-0.584893192 (%)/(km)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A Gaussian-pulse broadening formula based on second-order dispersion fails for higher-order dispersion, nonlinear self-phase modulation, polarization mode dispersion or strongly non-Gaussian input pulses. Uncertainty in pulse launch chirp can mimic dispersion changes.

### Experimental characterization and controls

Conduct an **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests Follow with a **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **coupler loss, bending or sidewall roughness**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **waveguide dispersion and pulse spreading** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **core geometry, modal launch and wavelength** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **waveguide dispersion and pulse spreading** depends on **guided electromagnetic modes**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **15.8489319 %** for the first stated input and **10 %** for the second. Determine the finite-difference sensitivity **-0.584893192 (%)/(km)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_9 -->

## Lesson 5.5 — Integrated waveguide processing and packaging

### Physical mechanism and field interpretation

Silicon nitride, silicon, silica, chalcogenides and polymers offer different trade-offs in transparency, index contrast, deposition temperature, stress and integration. Sidewall roughness creates scattering whose scaling may differ between TE and TM modes. Couplers bridge small chip modes to larger fiber modes, often dominating insertion loss. Packaging introduces thermo-mechanical stress and contamination that a lithographic simulation does not capture.

**Core equation and domain.** A simple cut-back fit uses Ltotal,dB≈αprop,dB/unit×length+Lcoup,in+Lcoup,out in an approximately linear regime. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**integrated waveguide processing and packaging**—the most consequential distinction in this unit is **bulk optical constants versus modal loss**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Write a process-control plan for a photonic chip containing an input coupler, a routed waveguide and an output grating. Separate wafer-level cut-back measurements from single-device spectral measurements; include a calibration structure that can identify coupler loss.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Step-index fiber normalized frequency V** isolates a single physical dependence, using **Core radius** as its variable. Substitute **4.5 µm** into its declared expression `(2*Math.PI*a/1.55)*Math.sqrt(1.450*1.450-1.444*1.444)` to obtain **2.40372938 dimensionless**. For the second case use **5 µm**, obtaining **2.67081043 dimensionless**. The output rises between these two cases. The finite-difference slope is **0.534162085 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A single transmission measurement cannot distinguish propagation loss from two unknown coupler losses. Cut-back requires comparable guides of multiple lengths and stable coupling conditions. A substrate crack or contamination defect cannot be repaired by re-fitting a mode index.

### Experimental characterization and controls

Conduct an **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval Follow with a **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **coupler loss, bending or sidewall roughness**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **integrated waveguide processing and packaging** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **core geometry, modal launch and wavelength** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **integrated waveguide processing and packaging** depends on **guided electromagnetic modes**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **2.40372938 dimensionless** for the first stated input and **2.67081043 dimensionless** for the second. Determine the finite-difference sensitivity **0.534162085 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Low-loss optical fiber splice package

### The decision to be made

A fiber segment passes a straight attenuation test but loses power when mounted in a curved housing. Production records contain nominal core radius and average dopant profile. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Sweep the V-number model and distributed attenuation independently, then compute a worst-case link margin when bends and splices introduce further loss. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Compare loose and mounted bend radii, record insertion/return loss, and repeat across independent cable and connector lots. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Single-mode cutoff and passive distributed loss do not determine packaging bend reliability.

### Five end-of-unit questions

