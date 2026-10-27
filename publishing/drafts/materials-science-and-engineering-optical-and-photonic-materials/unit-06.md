# Unit 6: Light-emitting materials, lasers and detectors

**Guiding question:** How do carriers, photons, microstructure and interfaces interact to determine optical emission, gain and photoresponse?

## Introduction and measurement challenges

The emitting or detecting specimen is both a material and an electrical device. Carriers interact with phonons, defects and heterointerfaces while photons interact with optical confinement and escape paths.

Optical output must be normalized against injection, absorption, spectral bandwidth and temperature before radiative efficiency, responsivity or threshold are inferred.

These five lessons emphasize **radiative device physics**, and distinguish **internal recombination versus extraction or collection**. To reproduce a study, specify **drive current, temperature, geometry and calibrated spectral response** before collecting data; otherwise **carrier leakage or thermal quenching** may mimic the desired optical response. A proposed independent validation is **time-resolved luminescence plus absolute photon balance**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 6.1 — Radiative and nonradiative recombination

### Physical mechanism and field interpretation

Injected electrons and holes can radiatively recombine or lose energy through phonons, surfaces and defects. The simplest branching-ratio description helps explain why a large radiative rate can improve intrinsic quantum yield. Actual light-emitting diodes involve carrier injection imbalance, Auger processes, exciton quenching, optical extraction and temperature dependence. A brightness improvement due to better outcoupling is not evidence that the internal material has fewer recombination defects.

**Core equation and domain.** For one population ηrad=kr/(kr+knr); ηexternal also depends on extraction and carrier injection. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**radiative and nonradiative recombination**—the most consequential distinction in this unit is **internal recombination versus extraction or collection**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Sweep the assumed nonradiative rate while holding the radiative rate fixed. Compare the resulting ideal internal fraction with a hypothetical LED external quantum efficiency. List which losses lie outside the single-population calculator.

Perform a thought experiment: assume the original explanation is wrong and **carrier leakage or thermal quenching** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **drive current, temperature, geometry and calibrated spectral response** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Radiative fraction from competing lifetimes** isolates a single physical dependence, using **Nonradiative rate** as its variable. Substitute **1.2125e+08 s⁻¹** into its declared expression `100*1e8/(1e8+knr)` to obtain **45.1977401 %**. For the second case use **2.325e+08 s⁻¹**, obtaining **30.075188 %**. The output falls between these two cases. The finite-difference slope is **-1.35933053e-07 (%)/(s⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Simple single-population branching ratio with radiative rate kr=10⁸ s⁻¹ and competing knr; not full LED external efficiency. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Lifetimes from time-resolved photoluminescence can involve multiple populations, trapping and photon recycling. An internal efficiency inferred from one exponential model may be wrong for coupled quantum wells or disordered emitters.

### Experimental characterization and controls

Conduct an **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration Follow with a **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **carrier leakage or thermal quenching**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **radiative and nonradiative recombination** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **drive current, temperature, geometry and calibrated spectral response** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **radiative and nonradiative recombination** depends on **radiative device physics**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **45.1977401 %** for the first stated input and **30.075188 %** for the second. Determine the finite-difference sensitivity **-1.35933053e-07 (%)/(s⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **carrier leakage or thermal quenching** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **time-resolved luminescence plus absolute photon balance**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_10 -->

## Lesson 6.2 — Semiconductor heterostructures and confinement

### Physical mechanism and field interpretation

Quantum wells and heterostructures localize carrier wavefunctions through band offsets and geometrical confinement. Strain alters band structure and defect formation; thin layers enhance interface sensitivity. Emission wavelength can be engineered by composition and confinement, but the relation is not determined by a bulk band gap alone. Nonradiative centers at interfaces, polarization fields and alloy disorder may reshape emission spectra.

**Core equation and domain.** A rough confinement-energy scale is ΔE∝ħ²/(m*L²), with effective mass and boundary conditions specified. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**semiconductor heterostructures and confinement**—the most consequential distinction in this unit is **internal recombination versus extraction or collection**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare a thick direct-gap semiconductor film with a thin quantum well of similar nominal composition. Predict a possible shift in emission energy and state measurements needed to separate confinement from strain and compositional differences.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Emitted photon energy for wavelength** isolates a single physical dependence, using **Emission wavelength** as its variable. Substitute **537.5 nm** into its declared expression `1239.8419843320026/lam` to obtain **2.30668276 eV**. For the second case use **606.25 nm**, obtaining **2.04510018 eV**. The output falls between these two cases. The finite-difference slope is **-0.00380483754 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Photon energy hc/λ; not equal to semiconductor band gap in all cases because of Stokes shift and spectral broadening. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Infinite-square-well energy estimates are pedagogic starting points, not a complete device band calculation. Real heterostructures require finite barriers, multiple bands, Coulomb interaction, built-in fields and temperature effects.

### Experimental characterization and controls

Conduct an **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum Follow with a **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **carrier leakage or thermal quenching**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **semiconductor heterostructures and confinement** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **drive current, temperature, geometry and calibrated spectral response** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **semiconductor heterostructures and confinement** depends on **radiative device physics**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **2.30668276 eV** for the first stated input and **2.04510018 eV** for the second. Determine the finite-difference sensitivity **-0.00380483754 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 6.3 — Stimulated emission and laser thresholds

### Physical mechanism and field interpretation

Stimulated emission adds coherent photons to a cavity mode in the presence of inversion or more general optical gain conditions. A laser reaches threshold when round-trip modal gain balances total cavity losses in a simplified steady-state description. Gain depends on carrier density, overlap, linewidth and temperature, while output power depends on coupling and thermal dissipation. Device aging, catastrophic optical damage and current crowding require dedicated reliability measurements.

**Core equation and domain.** Ideal cavity threshold modal gain gth≈αinternal+(1/2L)ln[1/(R1R2)] for a simple linear cavity. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**stimulated emission and laser thresholds**—the most consequential distinction in this unit is **internal recombination versus extraction or collection**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

For a notional Fabry–Pérot semiconductor laser, compare threshold changes when one mirror reflectivity is reduced. Explain why lowering mirror loss can reduce threshold yet also change slope efficiency and useful extracted power.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Radiative fraction from competing lifetimes** isolates a single physical dependence, using **Nonradiative rate** as its variable. Substitute **3.4375e+08 s⁻¹** into its declared expression `100*1e8/(1e8+knr)` to obtain **22.5352113 %**. For the second case use **4.55e+08 s⁻¹**, obtaining **18.018018 %**. The output falls between these two cases. The finite-difference slope is **-4.06039843e-08 (%)/(s⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Threshold conditions must include internal absorption and modal confinement, and may fail for high-β nanolasers or strongly transient pumping. Population inversion of a bare material is not itself proof of lasing without spectral and coherence measurements.

### Experimental characterization and controls

Conduct an **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests Follow with a **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **carrier leakage or thermal quenching**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **stimulated emission and laser thresholds** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **drive current, temperature, geometry and calibrated spectral response** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **stimulated emission and laser thresholds** depends on **radiative device physics**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **22.5352113 %** for the first stated input and **18.018018 %** for the second. Determine the finite-difference sensitivity **-4.06039843e-08 (%)/(s⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 6.4 — Spectral emission, LEDs and color conversion

### Physical mechanism and field interpretation

An LED spectrum arises from transitions across a range of energies rather than a single ideal wavelength. Semiconductor emission, phosphor conversion and down-converting quantum dots each introduce efficiency and lifetime trade-offs. The photon energy hc/λ maps spectral position, but optical power per nanometre and photon counts per nanometre require different weights. Perceived color also depends on observer sensitivity and spectral composition rather than only peak wavelength.

**Core equation and domain.** Photon energy E(eV)≈1239.841984/λ0(nm); total emitted photon rate integrates Pλ/(hc/λ) over spectrum. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**spectral emission, leds and color conversion**—the most consequential distinction in this unit is **internal recombination versus extraction or collection**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Calculate photon energy at a red and blue emission wavelength. For equal radiant powers, identify which source emits more photons per second. Explain how a phosphor-converted white LED introduces Stokes loss and possible spectral aging.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Emitted photon energy for wavelength** isolates a single physical dependence, using **Emission wavelength** as its variable. Substitute **675 nm** into its declared expression `1239.8419843320026/lam` to obtain **1.83680294 eV**. For the second case use **743.75 nm**, obtaining **1.66701443 eV**. The output falls between these two cases. The finite-difference slope is **-0.00246965101 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Electroluminescence quantum yield and photoluminescence quantum yield are different tests. A narrow emission peak does not ensure high color-rendering quality, lifetime or eye safety. Avoid interpreting peak-wavelength energy as an exact band gap.

### Experimental characterization and controls

Conduct an **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval Follow with a **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **carrier leakage or thermal quenching**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **spectral emission, leds and color conversion** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **drive current, temperature, geometry and calibrated spectral response** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **spectral emission, leds and color conversion** depends on **radiative device physics**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.83680294 eV** for the first stated input and **1.66701443 eV** for the second. Determine the finite-difference sensitivity **-0.00246965101 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_11 -->

## Lesson 6.5 — Photodetectors, responsivity and noise

### Physical mechanism and field interpretation

A detector converts optical input into charge, voltage or count events. External responsivity is electrical current per optical watt under calibrated wavelength and bias; it is related to quantum efficiency when each collected photon contributes one electron without internal gain. Dark current, shot noise, thermal noise, excess multiplication noise and bandwidth establish detectivity. A highly absorbing film might perform poorly as a detector if traps slow extraction or leak current.

**Core equation and domain.** Without internal gain, Rλ=ηext qλ0/(hc) in A/W with λ0 in metres. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**photodetectors, responsivity and noise**—the most consequential distinction in this unit is **internal recombination versus extraction or collection**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare two otherwise identical photodiodes, one with a thicker absorbing layer. Predict the competing changes in absorption, transit time and capacitance. Specify a measurement of impulse response alongside a spectral responsivity scan.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Radiative fraction from competing lifetimes** isolates a single physical dependence, using **Nonradiative rate** as its variable. Substitute **5.6625e+08 s⁻¹** into its declared expression `100*1e8/(1e8+knr)` to obtain **15.0093809 %**. For the second case use **6.775e+08 s⁻¹**, obtaining **12.8617363 %**. The output falls between these two cases. The finite-difference slope is **-1.93046699e-08 (%)/(s⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Responsivity measured under one illumination level may fail to predict large-signal saturation or very weak-signal detection. Avalanche multiplication changes the simple one-electron-per-photon relation; temperature and background illumination must be documented.

### Experimental characterization and controls

Conduct an **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios Follow with a **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **carrier leakage or thermal quenching**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **photodetectors, responsivity and noise** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **drive current, temperature, geometry and calibrated spectral response** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **photodetectors, responsivity and noise** depends on **radiative device physics**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **15.0093809 %** for the first stated input and **12.8617363 %** for the second. Determine the finite-difference sensitivity **-1.93046699e-08 (%)/(s⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Efficient red semiconductor light source

### The decision to be made

A red light source shows improved measured radiant output after a coating redesign. Investigators want to claim that the quantum well gained radiative efficiency. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Calculate the ideal radiative branching ratio and photon energy; distinguish radiative efficiency, extraction and electrical injection in a full energy budget. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure absolute emission in an integrating sphere, time-resolved photoluminescence and electrical characteristics at controlled junction temperature. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A change in external brightness does not uniquely identify a microscopic recombination improvement.

### Five end-of-unit questions

