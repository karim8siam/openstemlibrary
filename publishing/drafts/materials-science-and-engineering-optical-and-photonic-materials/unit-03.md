# Unit 3: Absorption, luminescence and optical defects

**Guiding question:** How do electronic states, lattice vibrations and structural imperfections determine the wavelength-dependent loss and emission of a material?

## Introduction and measurement challenges

A dark sample may be absorbing, scattering light outside collection optics, fluorescing outside the detection band or some combination. Quantitative spectroscopy needs optical-path and instrument geometry information before a material absorption coefficient is assigned.

Emission and absorption should be assessed through an energy and photon budget, accounting for reflected, transmitted, scattered and re-emitted power as distinct channels.

These five lessons emphasize **loss and light production**, and distinguish **true absorption versus scattering or re-emission**. To reproduce a study, specify **slab thickness, detector acceptance and pump spectrum** before collecting data; otherwise **surface haze, instrumental stray light or secondary luminescence** may mimic the desired optical response. A proposed independent validation is **integrating-sphere absorption plus angle-resolved scattering**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 3.1 — Absorption coefficient and attenuation length

### Physical mechanism and field interpretation

In a uniform non-scattering absorber, power density decays exponentially as optical path increases. Intensity absorption coefficient α is twice the field-amplitude attenuation coefficient if amplitudes follow exp(−αz/2). An independently measured slab transmittance includes entrance/exit Fresnel losses, so dividing a logarithmic loss by thickness without correcting for interfaces can overestimate bulk absorption. Thin films introduce coherent multiple reflections, and highly scattering media cannot always be described by one exponential beam model.

**Core equation and domain.** I(z)=I0exp(−αz), absorption length ℓabs=1/α, optical density OD=αL/ln(10) in the no-reflection limit. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**absorption coefficient and attenuation length**—the most consequential distinction in this unit is **true absorption versus scattering or re-emission**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Use a hypothetical polymer film with known thickness and an adjustable absorption coefficient to calculate internal attenuation. Then compare two films with equal internal absorption but different surface roughness; the detector may report different total transmission depending on its collection angle.

Perform a thought experiment: assume the original explanation is wrong and **surface haze, instrumental stray light or secondary luminescence** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **slab thickness, detector acceptance and pump spectrum** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Beer–Lambert internal transmitted power** isolates a single physical dependence, using **Intensity absorption coefficient** as its variable. Substitute **18.75 cm⁻¹** into its declared expression `100*Math.exp(-a*0.01)` to obtain **82.9029118 %**. For the second case use **37.5 cm⁻¹**, obtaining **68.7289279 %**. The output falls between these two cases. The finite-difference slope is **-0.75594581 (%)/(cm⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Uniform slab with 0.01 cm optical path and constant absorption coefficient; internal absorption only, ignores both Fresnel interfaces and scattering. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Strong photoluminescence can add detected light at other wavelengths; a broadband photodiode may therefore overstate transmitted pump power. Optical density uses base-ten logarithms while α commonly uses natural exponentials. Declare the definition before comparing values.

### Experimental characterization and controls

Conduct an **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result Follow with a **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface haze, instrumental stray light or secondary luminescence**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **absorption coefficient and attenuation length** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **slab thickness, detector acceptance and pump spectrum** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **absorption coefficient and attenuation length** depends on **loss and light production**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **82.9029118 %** for the first stated input and **68.7289279 %** for the second. Determine the finite-difference sensitivity **-0.75594581 (%)/(cm⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **surface haze, instrumental stray light or secondary luminescence** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **integrating-sphere absorption plus angle-resolved scattering**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_4 -->

## Lesson 3.2 — Band edges, allowed transitions and joint density of states

### Physical mechanism and field interpretation

A semiconductor absorbs interband photons only when energy, selection rules, momentum and occupied-state availability permit a transition. An indirect-gap semiconductor relies on phonon-assisted processes near its edge; direct-gap semiconductors can exhibit stronger near-edge absorption. Disorder and excitons alter simple textbook onsets. A Tauc plot can be informative only when the chosen exponent and absorption regime match the material and its transition type.

**Core equation and domain.** The photon energy threshold is roughly Eγ≥Eg for an allowed direct transition in a simplified band picture; absorption strength requires matrix elements and density of states. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**band edges, allowed transitions and joint density of states**—the most consequential distinction in this unit is **true absorption versus scattering or re-emission**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare silicon and a generic direct-gap III–V absorber under identical illumination. Ask which measurement can separate a genuine absorption edge from light lost into a roughened substrate. Describe how temperature-dependent spectra might shift and broaden the observed onset.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Ideal Urbach-tail absorbance sensitivity** isolates a single physical dependence, using **Photon energy** as its variable. Substitute **1.8125 eV** into its declared expression `2*Math.exp((E-1.9)/0.05)` to obtain **0.347547887 cm⁻¹**. For the second case use **1.84375 eV**, obtaining **0.649304935 cm⁻¹**. The output rises between these two cases. The finite-difference slope is **9.65622553 (cm⁻¹)/(eV)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Assumed α(E)=2 exp[(E−1.9)/0.05] cm⁻¹ with energy in eV; phenomenological absorption tail, no valid bandgap inference by itself. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A visually straight transformed absorption plot does not prove the selected transition exponent. Excitonic peaks, free-carrier absorption and thickness-dependent interference require care. Optical gap estimates may differ from transport gaps and photoluminescence peak energies.

### Experimental characterization and controls

Conduct an **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization Follow with a **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface haze, instrumental stray light or secondary luminescence**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **band edges, allowed transitions and joint density of states** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **slab thickness, detector acceptance and pump spectrum** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **band edges, allowed transitions and joint density of states** depends on **loss and light production**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.347547887 cm⁻¹** for the first stated input and **0.649304935 cm⁻¹** for the second. Determine the finite-difference sensitivity **9.65622553 (cm⁻¹)/(eV)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 3.3 — Urbach tails, localization and subgap states

### Physical mechanism and field interpretation

Disorder and phonon interactions frequently generate approximately exponential absorption tails near an electronic edge. An Urbach energy is a slope parameter of log absorption versus photon energy over an appropriate limited interval; it does not uniquely quantify every defect concentration. A single shallow tail may reflect different combinations of structural disorder, thermal broadening and exciton-phonon interactions. Proper analysis requires a measured dynamic range above instrumental stray-light background.

**Core equation and domain.** An idealized local-tail form is α(E)=α0exp[(E−E0)/EU]; EU is positive and has energy units. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**urbach tails, localization and subgap states**—the most consequential distinction in this unit is **true absorption versus scattering or re-emission**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Construct a synthetic exponential tail with a 0.05 eV scale and inspect a logarithmic graph. Suppose stray light imposes a floor at low absorption. Explain why fitting through the floor artificially flattens the inferred Urbach slope and may suggest a false material improvement.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Beer–Lambert internal transmitted power** isolates a single physical dependence, using **Intensity absorption coefficient** as its variable. Substitute **56.25 cm⁻¹** into its declared expression `100*Math.exp(-a*0.01)` to obtain **56.9782825 %**. For the second case use **75 cm⁻¹**, obtaining **47.2366553 %**. The output falls between these two cases. The finite-difference slope is **-0.519553451 (%)/(cm⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Phenomenological exponential behavior should not be extrapolated indefinitely, because oscillator strength and the higher-energy absorption regime impose other physics. An energy-dependent reflectance change can mimic an absorption change in uncorrected transmission.

### Experimental characterization and controls

Conduct an **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples Follow with a **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface haze, instrumental stray light or secondary luminescence**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **urbach tails, localization and subgap states** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **slab thickness, detector acceptance and pump spectrum** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **urbach tails, localization and subgap states** depends on **loss and light production**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **56.9782825 %** for the first stated input and **47.2366553 %** for the second. Determine the finite-difference sensitivity **-0.519553451 (%)/(cm⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 3.4 — Photoluminescence quantum yield and lifetime

### Physical mechanism and field interpretation

Luminescence follows absorbed energy through relaxation and radiative recombination. External photon quantum yield includes collection, reabsorption and extraction; an internal material quantum yield excludes some escape losses. Time-resolved spectra can separate fast and slow channels but the lifetime is not directly equal to quantum yield without a radiative-rate model. Concentration quenching, triplet dynamics, nonradiative interfaces and temperature changes matter for phosphors, quantum dots, defect centers and emissive polymers.

**Core equation and domain.** For competing single-exponential rates, ηinternal=kr/(kr+knr) and τ=1/(kr+knr). This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**photoluminescence quantum yield and lifetime**—the most consequential distinction in this unit is **true absorption versus scattering or re-emission**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare two coatings with equal total photoluminescence intensity but different thicknesses and outcoupling efficiencies. What data would establish that their radiative efficiencies genuinely differ? Include an integrating-sphere measurement and a lifetime analysis in your reasoning.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Ideal Urbach-tail absorbance sensitivity** isolates a single physical dependence, using **Photon energy** as its variable. Substitute **1.875 eV** into its declared expression `2*Math.exp((E-1.9)/0.05)` to obtain **1.21306132 cm⁻¹**. For the second case use **1.90625 eV**, obtaining **2.26629691 cm⁻¹**. The output rises between these two cases. The finite-difference slope is **33.7035388 (cm⁻¹)/(eV)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A brighter spectrum is not enough to infer fewer defects if absorption and extraction differ. Instrument response, photobleaching and pump reabsorption can corrupt the inferred kinetics. For multiexponential decay there is no single unique lifetime without a stated averaging convention.

### Experimental characterization and controls

Conduct an **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration Follow with a **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface haze, instrumental stray light or secondary luminescence**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **photoluminescence quantum yield and lifetime** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **slab thickness, detector acceptance and pump spectrum** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **photoluminescence quantum yield and lifetime** depends on **loss and light production**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.21306132 cm⁻¹** for the first stated input and **2.26629691 cm⁻¹** for the second. Determine the finite-difference sensitivity **33.7035388 (cm⁻¹)/(eV)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_5 -->

## Lesson 3.5 — Color centers, scattering and photodarkening

### Physical mechanism and field interpretation

Defects and impurities may create optically active transitions, trap carriers or form nanoscale refractive-index inhomogeneities. Scattering by sufficiently small inhomogeneities often follows a strong wavelength dependence, but real polycrystalline ceramics can contain pores and boundaries spanning multiple size regimes. A photodarkening experiment can alter the sample under illumination, making the probe itself part of its processing history. Annealing may remove absorbing centers while simultaneously changing microstructure.

**Core equation and domain.** Small-particle Rayleigh-type loss has an approximate fixed-geometry wavelength scaling αscatt∝λ⁻⁴, not a universal ceramic law. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**color centers, scattering and photodarkening**—the most consequential distinction in this unit is **true absorption versus scattering or re-emission**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Take a transparent ceramic that becomes cloudy after sintering. Suggest a sequence of transmission, haze, cross-sectional imaging and elemental spectroscopy that distinguishes residual pores from absorbing color centers. Predict contrasting angular scattering signatures.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Beer–Lambert internal transmitted power** isolates a single physical dependence, using **Intensity absorption coefficient** as its variable. Substitute **93.75 cm⁻¹** into its declared expression `100*Math.exp(-a*0.01)` to obtain **39.1605627 %**. For the second case use **112.5 cm⁻¹**, obtaining **32.4652467 %**. The output falls between these two cases. The finite-difference slope is **-0.357083516 (%)/(cm⁻¹)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The Rayleigh λ⁻⁴ scaling requires scatterers much smaller than wavelength and an appropriate weak-scattering regime. Mie scattering, multiple scattering and fluorescent emission can invalidate the proxy used in a simplified calculator.

### Experimental characterization and controls

A viable first study begins with **time-resolved photoluminescence**, recording **excitation fluence, instrument response and detection passband**. Verify the interpretation using **absolute quantum-yield photon balance**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum Follow with a **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface haze, instrumental stray light or secondary luminescence**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **color centers, scattering and photodarkening** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **slab thickness, detector acceptance and pump spectrum** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **color centers, scattering and photodarkening** depends on **loss and light production**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **39.1605627 %** for the first stated input and **32.4652467 %** for the second. Determine the finite-difference sensitivity **-0.357083516 (%)/(cm⁻¹)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Transparent luminescent coating

### The decision to be made

A coating emits blue-green light under UV excitation but transmission falls after aging. Investigators debate new absorbing color centers, particle growth and altered excitation absorption. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Compute Beer–Lambert loss and a synthetic Urbach tail; label both as separate idealized models, then propose a photon and energy balance. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Combine integrating-sphere measurements, time-resolved emission, scattering angular patterns and before/after microscopy. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A brighter or darker sample cannot be diagnosed from an uncorrected detector count.

### Five end-of-unit questions

