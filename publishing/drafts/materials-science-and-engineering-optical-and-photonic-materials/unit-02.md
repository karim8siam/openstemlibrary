# Unit 2: Optical dispersion, glass chemistry and anisotropy

**Guiding question:** What can a dispersion model reveal about group delay, chromatic aberration and the limits of transparent material design?

## Introduction and measurement challenges

A glass is not characterized by one timeless refractive-index number. Its dispersive response is sensitive to bond chemistry, oscillator frequencies, temperature and wavelength, and derivative quantities such as group index can amplify fit uncertainty.

This unit separates optical phase, pulse envelopes and anisotropic eigenmodes. It deliberately prevents a fitted refractive index from being extrapolated through a resonance or treated as a universal supplier certificate.

These five lessons emphasize **dispersion of bound-charge response**, and distinguish **phase index versus pulse delay**. To reproduce a study, specify **temperature, polarization and spectral calibration** before collecting data; otherwise **unknown coating thickness or residual absorption** may mimic the desired optical response. A proposed independent validation is **multi-wavelength ellipsometry with time-of-flight measurement**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 2.1 — Electronic oscillators and refractive dispersion

### Physical mechanism and field interpretation

Bound charges respond with frequency-dependent phase and amplitude. Far from a resonance their induced polarization shifts the real refractive index; near resonance the response often becomes strongly dispersive and absorptive. The damped-Lorentz oscillator supplies physical intuition, but its coefficients are not automatically transferable to a chemically complex glass. Causality couples broadband absorption and refraction through Kramers–Kronig reasoning; an arbitrary transparent-region fit must not be extrapolated across an absorption band.

**Core equation and domain.** A common transparent-region form is n²(λ)=1+Σ Bj λ²/(λ²−Cj), where λ and sqrt(Cj) use consistent wavelength units. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**electronic oscillators and refractive dispersion**—the most consequential distinction in this unit is **phase index versus pulse delay**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare a crown-type optical glass with a doped oxide film by measuring transmission and ellipsometry over a specified spectral band. Ask how a model with only real n can match phase but fail power conservation if absorption is neglected.

Perform a thought experiment: assume the original explanation is wrong and **unknown coating thickness or residual absorption** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **temperature, polarization and spectral calibration** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Illustrative silica Sellmeier phase index** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **0.63125 µm** into its declared expression `Math.sqrt(1+(0.6961663*lam*lam)/(lam*lam-0.0684043*0.0684043)+(0.4079426*lam*lam)/(lam*lam-0.1162414*0.1162414)+(0.8974794*lam*lam)/(lam*lam-9.896161*9.896161))` to obtain **1.45706308 dimensionless**. For the second case use **0.8125 µm**, obtaining **1.45310424 dimensionless**. The output falls between these two cases. The finite-difference slope is **-0.0218418536 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Fused-silica example using commonly tabulated Sellmeier coefficients, wavelength in micrometers; transparent region only, ignores temperature and impurity changes. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Dispersion is temperature-dependent and can be modified by stress, dopants and crystallinity. A fitted Sellmeier pole is usually outside the allowed transparent region; do not confuse the numerical location of a fitted pole with a laboratory-verified isolated electronic transition.

### Experimental characterization and controls

Conduct an **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios Follow with a **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **unknown coating thickness or residual absorption**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **electronic oscillators and refractive dispersion** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **temperature, polarization and spectral calibration** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **electronic oscillators and refractive dispersion** depends on **dispersion of bound-charge response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.45706308 dimensionless** for the first stated input and **1.45310424 dimensionless** for the second. Determine the finite-difference sensitivity **-0.0218418536 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **unknown coating thickness or residual absorption** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **multi-wavelength ellipsometry with time-of-flight measurement**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_2 -->

## Lesson 2.2 — Sellmeier fitting and model extrapolation

### Physical mechanism and field interpretation

A Sellmeier equation compresses phase-index measurements into a compact rational function. It is useful inside a calibrated transparency window and can produce misleading singularities when extrapolated. The fit quality depends on wavelength coverage, thermal state and the reproducibility of glass composition. Model coefficients may be chosen to approximate a particular fused-silica grade; a manufacturing certificate is still required for real device procurement. Uncertainty in fit coefficients becomes more important when derivative properties, such as group delay, are calculated.

**Core equation and domain.** For n(λ)=sqrt[1+Σ Bjλ²/(λ²−Cj)], n must be real only where the radicand and transparency assumptions permit. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**sellmeier fitting and model extrapolation**—the most consequential distinction in this unit is **phase index versus pulse delay**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compute an idealized silica phase index at several near-infrared wavelengths. Fit a simple Cauchy expression to a narrow subset, then compare extrapolated values outside the fitting region. The smaller residual inside the fit is not sufficient evidence of a better microscopic description.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Cauchy-model group refractive index** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **0.9 µm** into its declared expression `1.45+0.012/(lam*lam)` to obtain **1.46481481 dimensionless**. For the second case use **1.05 µm**, obtaining **1.46088435 dimensionless**. The output falls between these two cases. The finite-difference slope is **-0.0262030738 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** n(λ)=1.45+0.004/λ² where λ is in µm; ng=n−λ dn/dλ; illustrative coefficients not a glass certificate. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Absorption, ultraviolet resonance edges and infrared multiphonon response invalidate a lossless Sellmeier model outside its stated interval. Geometrical measurement of optical thickness alone usually cannot independently identify both film thickness and refractive index.

### Experimental characterization and controls

Conduct an **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result Follow with a **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **unknown coating thickness or residual absorption**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **sellmeier fitting and model extrapolation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **temperature, polarization and spectral calibration** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **sellmeier fitting and model extrapolation** depends on **dispersion of bound-charge response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.46481481 dimensionless** for the first stated input and **1.46088435 dimensionless** for the second. Determine the finite-difference sensitivity **-0.0262030738 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 2.3 — Phase index versus group index

### Physical mechanism and field interpretation

An optical carrier propagates with phase velocity while a slowly modulated pulse envelope propagates with group velocity in suitable weakly dispersive media. Group index is a derivative quantity, so even a small error in refractive-index versus wavelength can produce a large inferred timing error. In lossy or anomalously dispersive systems, the group velocity can cease to be a useful measure of signal-front or energy transport. Timing measurements of fiber links mix material dispersion, waveguide dispersion, source chirp and temperature drift.

**Core equation and domain.** ng=n−λ0(dn/dλ0); group delay τg=ngL/c, provided a meaningful group velocity exists. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**phase index versus group index**—the most consequential distinction in this unit is **phase index versus pulse delay**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

For an assumed Cauchy law n=1.45+0.004/λ² with λ in micrometres, differentiate it and evaluate group index. Compare optical phase delay and pulse-envelope delay over the same distance. Discuss how a clock calibration can masquerade as a material effect.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Illustrative silica Sellmeier phase index** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **0.99375 µm** into its declared expression `Math.sqrt(1+(0.6961663*lam*lam)/(lam*lam-0.0684043*0.0684043)+(0.4079426*lam*lam)/(lam*lam-0.1162414*0.1162414)+(0.8974794*lam*lam)/(lam*lam-9.896161*9.896161))` to obtain **1.45049653 dimensionless**. For the second case use **1.175 µm**, obtaining **1.44833531 dimensionless**. The output falls between these two cases. The finite-difference slope is **-0.0119239887 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The group index computed by differentiation is conditional on a narrowband pulse and smooth transparent response. Chromatic dispersion is not just a group-index value at one wavelength; it requires the slope versus wavelength or frequency.

### Experimental characterization and controls

Conduct an **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization Follow with a **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **unknown coating thickness or residual absorption**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **phase index versus group index** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **temperature, polarization and spectral calibration** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **phase index versus group index** depends on **dispersion of bound-charge response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.45049653 dimensionless** for the first stated input and **1.44833531 dimensionless** for the second. Determine the finite-difference sensitivity **-0.0119239887 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 2.4 — Abbe number and lens material trade-offs

### Physical mechanism and field interpretation

Abbe number summarizes visible-range index dispersion using selected reference wavelengths. A high Abbe number commonly corresponds to reduced color-dependent focal shift, but it is not a standalone assessment of lens quality. A lens pair can compensate chromatic errors by combining positive and negative powers with distinct dispersion; the final behavior also depends on geometry and partial dispersion. Novel optical glass may improve one chromatic metric yet suffer from cost, chemical durability, transmittance or thermal expansion.

**Core equation and domain.** For standard Fraunhofer reference lines, Vd=(nd−1)/(nF−nC); identify which chosen wavelength convention the supplier uses. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**abbe number and lens material trade-offs**—the most consequential distinction in this unit is **phase index versus pulse delay**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Consider a two-element achromat. Hold the total paraxial focal power fixed while changing the glass pair; show qualitatively why two glasses with identical Abbe numbers cannot generate classic first-order chromatic correction without other degrees of freedom.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Cauchy-model group refractive index** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **1.2 µm** into its declared expression `1.45+0.012/(lam*lam)` to obtain **1.45833333 dimensionless**. For the second case use **1.35 µm**, obtaining **1.45658436 dimensionless**. The output falls between these two cases. The finite-difference slope is **-0.011659808 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

High-order aberrations, finite bandwidth, coating reflectance and nonlinear spectral behavior escape one-number material descriptors. An Abbe number inferred from a noisy index fit needs uncertainty in each reference line.

### Experimental characterization and controls

Conduct an **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples Follow with a **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **unknown coating thickness or residual absorption**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **abbe number and lens material trade-offs** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **temperature, polarization and spectral calibration** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **abbe number and lens material trade-offs** depends on **dispersion of bound-charge response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.45833333 dimensionless** for the first stated input and **1.45658436 dimensionless** for the second. Determine the finite-difference sensitivity **-0.011659808 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_3 -->

## Lesson 2.5 — Crystal optical axes and effective index

### Physical mechanism and field interpretation

A dielectric tensor gives different field responses along symmetry axes, and polarization eigenmodes depend on propagation direction. In a uniaxial crystal, the extraordinary index changes with angle relative to the optic axis, while the ordinary index remains fixed at a given wavelength and temperature. Walk-off between energy flow and wave-vector direction can shift beams in nonlinear crystals and polarizing components. Fabrication strain and thermal birefringence create nonidealities even in nominally isotropic substrates.

**Core equation and domain.** In a uniaxial transparent medium the extraordinary effective index follows 1/neff²=cos²θ/no²+sin²θ/ne² under a specified angle convention. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**crystal optical axes and effective index**—the most consequential distinction in this unit is **phase index versus pulse delay**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Map the polarization response of a rotated crystal plate using a polarizer, analyzer and reference sample. Explain what extra geometric information is needed before fitting angular intensity data to a birefringence value.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Illustrative silica Sellmeier phase index** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **1.35625 µm** into its declared expression `Math.sqrt(1+(0.6961663*lam*lam)/(lam*lam-0.0684043*0.0684043)+(0.4079426*lam*lam)/(lam*lam-0.1162414*0.1162414)+(0.8974794*lam*lam)/(lam*lam-9.896161*9.896161))` to obtain **1.44627934 dimensionless**. For the second case use **1.5375 µm**, obtaining **1.44417307 dimensionless**. The output falls between these two cases. The finite-difference slope is **-0.0116207547 (dimensionless)/(µm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A scalar index measured on one crystal face cannot represent all propagation directions. Anisotropic absorption, surface wedges, multiple reflections and imperfect polarization should be tested before asserting intrinsic material anisotropy.

### Experimental characterization and controls

A viable first study begins with **fiber or planar waveguide cut-back**, recording **multiple sample lengths, mode launch and connector repeatability**. Verify the interpretation using **a modal profile measurement and separate coupler calibration**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration Follow with a **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **unknown coating thickness or residual absorption**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **crystal optical axes and effective index** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **temperature, polarization and spectral calibration** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **crystal optical axes and effective index** depends on **dispersion of bound-charge response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.44627934 dimensionless** for the first stated input and **1.44417307 dimensionless** for the second. Determine the finite-difference sensitivity **-0.0116207547 (dimensionless)/(µm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Precision delay element for an interferometer

### The decision to be made

A laboratory needs a stable glass delay element with controlled optical phase and pulse timing over a narrow band. Phase-index fits are available, but their temperature coefficients and wavelength coverage differ. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Compare the silica Sellmeier curve and the illustrative Cauchy group-index curve without treating them as measurements of identical materials; derive the timing effect of an index uncertainty. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure calibrated spectral phase and actual pulse delay; monitor temperature and reject extrapolations beyond the fitted transparent window. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A small phase-index fitting residual does not guarantee an accurate derivative or group-delay prediction.

### Five end-of-unit questions

