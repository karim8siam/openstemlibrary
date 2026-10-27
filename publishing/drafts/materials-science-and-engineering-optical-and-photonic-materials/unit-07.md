# Unit 7: Electro-optic, nonlinear and active photonic materials

**Guiding question:** When do field-driven index changes and nonlinear polarization improve modulation without creating excess loss or thermal drift?

## Introduction and measurement challenges

Active optical materials can change phase, amplitude or frequency under applied electric fields, optical intensity and temperature. At devices scales these perturbations overlap, and a spectrally shifted resonance may arise from heating rather than the intended electronic nonlinearity.

This unit treats modulation as a multiphysics inverse problem that must be judged by speed, insertion loss, power, endurance and reproducibility, not by maximum tuning range alone.

These five lessons emphasize **field-controlled optical response**, and distinguish **refractive phase change versus absorption or heat**. To reproduce a study, specify **RF frequency, temperature, optical power and sample orientation** before collecting data; otherwise **photothermal changes, electrodes or defects** may mimic the desired optical response. A proposed independent validation is **simultaneous phase, loss and fast modulation testing**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 7.1 — Electro-optic tensors and Pockels modulation

### Physical mechanism and field interpretation

Materials lacking inversion symmetry can show a linear change in refractive-index ellipsoid under an applied electric field, described by electro-optic tensor coefficients. The induced phase shift depends on crystal cut, polarization, modal overlap and electrode geometry. A useful modulator balances drive voltage, insertion loss, speed, RF impedance and thermal stability. A large bulk electro-optic coefficient does not guarantee low-voltage performance in a poorly overlapped thin-film device.

**Core equation and domain.** For a simple principal-axis Pockels response, Δ(1/n²)=rE and for small change Δn≈−½n³rE. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**electro-optic tensors and pockels modulation**—the most consequential distinction in this unit is **refractive phase change versus absorption or heat**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare a crystal modulator and an integrated thin-film design. Draw the optical mode and RF field; predict how moving electrodes closer might increase modulation efficiency while raising metal absorption. State an optical and an electrical control measurement.

Perform a thought experiment: assume the original explanation is wrong and **photothermal changes, electrodes or defects** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **RF frequency, temperature, optical power and sample orientation** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Thermo-optic resonant shift** isolates a single physical dependence, using **Temperature change** as its variable. Substitute **5 K** into its declared expression `(1550/4)*(1.8e-4*dT)` to obtain **0.34875 nm**. For the second case use **10 K**, obtaining **0.6975 nm**. The output rises between these two cases. The finite-difference slope is **0.06975 (nm)/(K)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** First-order perturbation λ0/ng×Δn with λ0=1550 nm, ng=4, dn/dT=1.8e−4/K; excludes thermal expansion and thermoelastic effects. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

The Pockels effect vanishes for ideal centrosymmetric bulk crystals by symmetry, though interfaces, strain or field-induced symmetry breaking complicate nanoscale observations. Fringing RF fields and optical-mode confinement must be included in a device model.

### Experimental characterization and controls

Conduct an **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum Follow with a **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **photothermal changes, electrodes or defects**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **electro-optic tensors and pockels modulation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **RF frequency, temperature, optical power and sample orientation** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **electro-optic tensors and pockels modulation** depends on **field-controlled optical response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.34875 nm** for the first stated input and **0.6975 nm** for the second. Determine the finite-difference sensitivity **0.06975 (nm)/(K)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **photothermal changes, electrodes or defects** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **simultaneous phase, loss and fast modulation testing**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_12 -->

## Lesson 7.2 — Thermo-optic tuning and resonant drift

### Physical mechanism and field interpretation

The refractive index of a waveguide changes with temperature, moving interference and cavity resonances. Thermal expansion changes geometric length, and mechanical stress may add photoelastic shifts. Microheaters exploit this response for tuning but introduce electric-power consumption and cross-talk. A measured wavelength shift versus heater power must not be reported as a material dn/dT unless thermal simulation or independent thermometry determines the actual optical-mode temperature change.

**Core equation and domain.** To first order, Δλres≈(λ0/ng)Δneff, where thermal expansion and strain can add separate terms. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**thermo-optic tuning and resonant drift**—the most consequential distinction in this unit is **refractive phase change versus absorption or heat**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Sweep the calculator through a modest temperature range using a first-order index coefficient. Compute shift per kelvin, then suggest why a fabricated resonator might shift at a different rate if its cross-section expands or a cladding has strong thermo-optic response.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Ideal Kerr nonlinear phase shift** isolates a single physical dependence, using **Optical power** as its variable. Substitute **0.5 W** into its declared expression `1.3*P*10` to obtain **6.5 rad**. For the second case use **0.75 W**, obtaining **9.75 rad**. The output rises between these two cases. The finite-difference slope is **13 (rad)/(W)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Effective fiber nonlinear coefficient γ=1.3 W⁻¹ km⁻¹, uniform power, L=10 km; neglects attenuation and dispersion. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Near phase changes and nonlinear absorption regimes, linear dn/dT may be inadequate. Spectrometer resolution, thermal hysteresis and thermal contact resistance need explicit controls. Material coefficients extracted from device shift are effective composite quantities unless de-embedded.

### Experimental characterization and controls

Conduct an **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests Follow with a **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **photothermal changes, electrodes or defects**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **thermo-optic tuning and resonant drift** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **RF frequency, temperature, optical power and sample orientation** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **thermo-optic tuning and resonant drift** depends on **field-controlled optical response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **6.5 rad** for the first stated input and **9.75 rad** for the second. Determine the finite-difference sensitivity **13 (rad)/(W)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 7.3 — Kerr response and self-phase modulation

### Physical mechanism and field interpretation

In Kerr-active media, the optical intensity modifies refractive index, changing the phase accumulated by a propagating wave. Spectral broadening arises because temporal intensity changes translate into time-dependent nonlinear phase. Effective waveguide nonlinearity depends on field confinement as well as bulk n2. Competing effects include two-photon absorption, free-carrier dispersion and Raman response; self-phase modulation does not automatically imply a useful frequency comb.

**Core equation and domain.** For lossless constant power over length L, nonlinear phase φNL=γPL; with attenuation replace L by an effective interaction length. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**kerr response and self-phase modulation**—the most consequential distinction in this unit is **refractive phase change versus absorption or heat**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

For the ideal power–phase calculator, double optical power and evaluate nonlinear phase accumulation. Then explain why a real long fiber with propagation loss develops less phase shift than γPL and why dispersion can change the observed spectrum.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Thermo-optic resonant shift** isolates a single physical dependence, using **Temperature change** as its variable. Substitute **15 K** into its declared expression `(1550/4)*(1.8e-4*dT)` to obtain **1.04625 nm**. For the second case use **20 K**, obtaining **1.395 nm**. The output rises between these two cases. The finite-difference slope is **0.06975 (nm)/(K)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The single-parameter Kerr phase ignores spatial modes, polarization, nonlinear absorption and pulsed dynamics. For very short pulses or near resonances, instantaneous n2 and weak-nonlinearity assumptions must be verified rather than assumed.

### Experimental characterization and controls

Conduct an **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval Follow with a **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **photothermal changes, electrodes or defects**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **kerr response and self-phase modulation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **RF frequency, temperature, optical power and sample orientation** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **kerr response and self-phase modulation** depends on **field-controlled optical response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.04625 nm** for the first stated input and **1.395 nm** for the second. Determine the finite-difference sensitivity **0.06975 (nm)/(K)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 7.4 — Frequency conversion and phase matching

### Physical mechanism and field interpretation

Second-order nonlinear polarization can couple optical waves at different frequencies in non-centrosymmetric media. Efficient conversion requires energy conservation, phase matching and sufficient modal overlap. Periodic poling enables quasi-phase matching through engineered reversal of nonlinear coefficient, not by changing photon energy conservation. Dispersion determines phase mismatch, while absorption and walk-off limit useful crystal length.

**Core equation and domain.** For second-harmonic generation, ω2=2ω1 and Δk=k(2ω1)−2k(ω1); quasi-phase matching adds an integer grating vector. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**frequency conversion and phase matching**—the most consequential distinction in this unit is **refractive phase change versus absorption or heat**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Propose a second-harmonic experiment with a tunable pump. Show what a quadratic low-power output trend suggests and why it does not alone prove coherent second-harmonic generation in the presence of fluorescence or stray pump harmonics.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Ideal Kerr nonlinear phase shift** isolates a single physical dependence, using **Optical power** as its variable. Substitute **1 W** into its declared expression `1.3*P*10` to obtain **13 rad**. For the second case use **1.25 W**, obtaining **16.25 rad**. The output rises between these two cases. The finite-difference slope is **13 (rad)/(W)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Conversion efficiency usually departs from simple quadratic scaling at depletion, walk-off or high loss. Temperature and poling-period tolerances can dominate production yield. Crystal-damage thresholds and laser safety require qualified procedures.

### Experimental characterization and controls

Conduct an **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios Follow with a **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **photothermal changes, electrodes or defects**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **frequency conversion and phase matching** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **RF frequency, temperature, optical power and sample orientation** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **frequency conversion and phase matching** depends on **field-controlled optical response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **13 rad** for the first stated input and **16.25 rad** for the second. Determine the finite-difference sensitivity **13 (rad)/(W)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_13 -->

## Lesson 7.5 — Electroabsorption and phase-change devices

### Physical mechanism and field interpretation

Electroabsorption exploits field-dependent absorption spectra in semiconductors, while some phase-change materials switch between states with different complex indices. Both can provide compact optical modulation but often introduce insertion loss and thermal complexity. A switching threshold measured on one nanoscale device may shift with contact resistance, heat sinking, cycling history and patterning. A practical evaluation separates reversible tuning, nonvolatile memory and damage-induced irreversible change.

**Core equation and domain.** The complex index ñ=n+iκ implies absorption α=4πκ/λ0 for a homogeneous wave with the stated time convention. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**electroabsorption and phase-change devices**—the most consequential distinction in this unit is **refractive phase change versus absorption or heat**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare a phase modulator and an absorptive modulator for a short-reach optical link. Define insertion loss, extinction ratio, bandwidth, switching energy and endurance, then explain why the best extinction ratio might not deliver the lowest system power.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Thermo-optic resonant shift** isolates a single physical dependence, using **Temperature change** as its variable. Substitute **25 K** into its declared expression `(1550/4)*(1.8e-4*dT)` to obtain **1.74375 nm**. For the second case use **30 K**, obtaining **2.0925 nm**. The output rises between these two cases. The finite-difference slope is **0.06975 (nm)/(K)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A large Δn derived from a mixture rule does not imply low loss if the extinction coefficient κ also changes. Device claims need endurance cycling, retention and programming distribution across independent devices.

### Experimental characterization and controls

Conduct an **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result Follow with a **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **photothermal changes, electrodes or defects**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **electroabsorption and phase-change devices** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **RF frequency, temperature, optical power and sample orientation** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **electroabsorption and phase-change devices** depends on **field-controlled optical response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.74375 nm** for the first stated input and **2.0925 nm** for the second. Determine the finite-difference sensitivity **0.06975 (nm)/(K)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Low-power photonic thermal phase shifter

### The decision to be made

An integrated resonator shifts wavelength when driven electrically. The designer attributes the entire shift to field-driven index change, but optical heating is also plausible. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Compare thermo-optic resonance shift and lossless Kerr phase in their declared domains; identify how thermal timescale differs from ultrafast field response. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure modulation frequency response, dissipated electrical power, local temperature proxies and simultaneous optical insertion loss. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** An identical steady-state wavelength shift can arise from different dynamics and cannot prove a specific nonlinear coefficient.

### Five end-of-unit questions

