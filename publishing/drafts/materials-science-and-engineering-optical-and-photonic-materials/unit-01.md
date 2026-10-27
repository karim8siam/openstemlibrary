# Unit 1: Optical fields, refractive index and interfaces

**Guiding question:** How can polarization and electromagnetic boundary conditions explain reflection, phase and energy transfer at an optical interface?

## Introduction and measurement challenges

An optical interface is a material boundary, not merely a ray-diagram corner. Maxwell boundary conditions determine reflected and transmitted amplitudes, while experimental detectors record power integrated over finite angles, positions and wavelengths. The connection between these descriptions must be made explicitly.

A phase reversal at a boundary can be hidden by intensity-only measurements; a polarimetric or interferometric measurement reveals information that an ordinary power meter discards. A useful material classification always states wavelength and optical environment.

These five lessons emphasize **electromagnetic boundary response**, and distinguish **field amplitude versus measured power**. To reproduce a study, specify **wavelength, angle, polarization and surface finish** before collecting data; otherwise **backside interference or diffuse reflection** may mimic the desired optical response. A proposed independent validation is **angle-resolved calibrated reflection and transmission**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

Start each study by sketching the optical interface or mode profile and locating energy channels: reflection, transmission, absorption, scattering, any luminescence and electrical conversion. Use a vacuum wavelength unless clearly stated otherwise. Predict limiting behavior of the equation and identify its domain before entering numbers. For numerical exercises, report input units, intermediate quantities, numerical precision and a reasonableness check. The two model cards in each unit are simple independent controls, not coupled predictions of a fabricated device. The capstone demands a falsifiable physical explanation and a feasible characterization plan.

## Lesson 1.1 — Maxwell waves in a material medium

### Physical mechanism and field interpretation

A monochromatic wave is a coupled electric and magnetic disturbance constrained by Maxwell curl equations. In a homogeneous isotropic nonmagnetic dielectric with weak loss, phase velocity is c/n and wave impedance is approximately the vacuum impedance divided by n. The electromagnetic energy flux follows the cycle-averaged Poynting vector; one must not assign a beam an energy purely from the electric-field amplitude without specifying impedance. The local polarizability of electrons and ions generates a wavelength-dependent displacement response, while magnetic permeability normally contributes little at optical frequencies for common transparent dielectrics.

**Core equation and domain.** For a plane wave in a lossless nonmagnetic dielectric, k=2πn/λ0, vphase=c/n and H=E/Z with Z≈Z0/n. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**maxwell waves in a material medium**—the most consequential distinction in this unit is **field amplitude versus measured power**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Compare a visible beam crossing from dry air into a clean optical glass plate with the same beam crossing an absorbing conductive oxide. Identify when a real n is a defensible description and when a complex index must be used. A boundary-condition calculation of reflected amplitude will not alone tell whether the transmitted beam heats the plate.

Perform a thought experiment: assume the original explanation is wrong and **backside interference or diffuse reflection** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **wavelength, angle, polarization and surface finish** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Normal-incidence Fresnel power reflection** isolates a single physical dependence, using **Refractive index** as its variable. Substitute **1.35625 dimensionless** into its declared expression `100*Math.pow((n-1)/(n+1),2)` to obtain **2.28595149 %**. For the second case use **1.6625 dimensionless**, obtaining **6.19145231 %**. The output rises between these two cases. The finite-difference slope is **12.7526557 (%)/(dimensionless)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

The units are important. A wavelength expressed in nanometres may require conversion before it enters a relation written with SI constants. Likewise, percent transmission cannot be added directly to a field amplitude, a logarithmic decibel value cannot be multiplied as a linear power fraction, and an extinction coefficient κ is not the same object as a fractional transmission deficit. Perform the limiting-case check in the model card: evaluate its lower and upper bounds and decide whether the output should remain positive, finite and consistent with its assumed geometry. Reproduce at least one result with a calculator that does not use this page's JavaScript.

**Assumptions used for this calculation:** Air to lossless nonmagnetic dielectric; normal incidence; one isolated flat interface. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

The scalar wave equation fails for strongly anisotropic, spatially dispersive or magneto-optic specimens. A phase index extracted from interference is not necessarily the energy transport velocity. Characterizing a rough interface requires scattering and surface topography in addition to a Fresnel calculation.

A fabricated specimen can disagree with the simple equation because of spectral bandwidth, wavelength calibration, thermal variation, dimensional uncertainty, polarization, surface roughness or a previously unmodeled optical path. Rather than minimizing every residual by adding parameters, ask which model assumptions are testable independently. Where the observed response contains a resonance or apparent threshold, check that the spectrometer and detector response are not creating the feature. Always separate repeat measurements on one specimen from separate fabrication runs; they quantify different components of uncertainty.

### Experimental characterization and controls

A viable first study begins with **spectrally calibrated reflectance and transmittance**, recording **source spectrum, incidence angle, numerical aperture and dark-corrected power**. Verify the interpretation using **independent ellipsometric phase and film-thickness measurements**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval Follow with a **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **backside interference or diffuse reflection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **maxwell waves in a material medium** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **wavelength, angle, polarization and surface finish** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **maxwell waves in a material medium** depends on **electromagnetic boundary response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **2.28595149 %** for the first stated input and **6.19145231 %** for the second. Determine the finite-difference sensitivity **12.7526557 (%)/(dimensionless)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **backside interference or diffuse reflection** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **angle-resolved calibrated reflection and transmission**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_0 -->

## Lesson 1.2 — Polarization, Jones vectors and birefringence

### Physical mechanism and field interpretation

A transverse vector field needs polarization information. Linear and circular states are coherent combinations of orthogonal components with different relative phases. In birefringent media the two eigenpolarizations may propagate with different phase indices; a waveplate converts phase difference into a changed output state. Ordinary and extraordinary rays in a uniaxial crystal are constrained by crystal orientation, not just color. Jones calculus is convenient for coherent completely polarized light, whereas Mueller and Stokes descriptions handle depolarization and partially polarized measurements.

**Core equation and domain.** For linear birefringence, retardance δ=(2π/λ0)ΔnL; the thickness, wavelength and propagation direction must be specified. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**polarization, jones vectors and birefringence**—the most consequential distinction in this unit is **field amplitude versus measured power**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Imagine cutting a quartz waveplate with a slightly wrong thickness. Predict the output of an input beam polarized at 45 degrees to its axes; then rotate the sample. A rotated high-contrast response suggests orientation sensitivity but is not yet proof of perfect half-wave or quarter-wave retardation.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Photon energy from vacuum wavelength** isolates a single physical dependence, using **Wavelength** as its variable. Substitute **662.5 nm** into its declared expression `1239.8419843320026/lam` to obtain **1.8714596 eV**. For the second case use **818.75 nm**, obtaining **1.51431082 eV**. The output falls between these two cases. The finite-difference slope is **-0.00228575218 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Vacuum photon energy hc/λ; assumes light can be represented by photons and wavelength is the vacuum wavelength. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

In a scattering film, depolarization can produce an apparent weak extinction ratio even with intrinsically large birefringence. Weak phase retardation can also result from sample strain. State waveplate order and wavelength; a plate tuned at one color is not universally achromatic.

### Experimental characterization and controls

A viable first study begins with **polarization-resolved optical analysis**, recording **polarizer extinction, polarization alignment and retardance sign**. Verify the interpretation using **Stokes polarimetry with angular rotation controls**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios Follow with a **spectral resolution audit**: check instrument function, stray-light floor, spectral sampling and wavelength calibration For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **backside interference or diffuse reflection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **polarization, jones vectors and birefringence** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **wavelength, angle, polarization and surface finish** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **polarization, jones vectors and birefringence** depends on **electromagnetic boundary response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.8714596 eV** for the first stated input and **1.51431082 eV** for the second. Determine the finite-difference sensitivity **-0.00228575218 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 1.3 — Fresnel boundary conditions and reflectance

### Physical mechanism and field interpretation

The tangential electric and magnetic fields obey continuity conditions when there is no singular surface current. At normal incidence between lossless nonmagnetic media, the reflected field amplitude has a simple refractive-index contrast; the power fraction is the squared magnitude of that amplitude. The transmitted power fraction is not merely the squared transmission-field amplitude, because the optical impedances differ. Multiple surfaces yield interference, so a glass window is not always modeled by one independent interface.

**Core equation and domain.** At normal incidence, R=|(n1−n2)/(n1+n2)|² when both indices are real; T=1−R only for one lossless isolated interface. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**fresnel boundary conditions and reflectance**—the most consequential distinction in this unit is **field amplitude versus measured power**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Estimate the reflectance of an uncoated n=1.50 glass-air boundary. What changes when the glass is placed behind a high-index coating? Separate measured return loss from a single-interface prediction. A low return signal might result from destructive interference rather than reduced total Fresnel reflection at both boundaries.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Normal-incidence Fresnel power reflection** isolates a single physical dependence, using **Refractive index** as its variable. Substitute **1.96875 dimensionless** into its declared expression `100*Math.pow((n-1)/(n+1),2)` to obtain **10.6481994 %**. For the second case use **2.275 dimensionless**, obtaining **15.1564594 %**. The output rises between these two cases. The finite-difference slope is **14.7208489 (%)/(dimensionless)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Oblique incidence, absorbing films, finite numerical aperture and surface roughness demand more elaborate amplitude coefficients. Energy accounting must include transmission and absorption. A reflected intensity curve fitted with a real refractive index can hide extinction or diffuse scattering.

### Experimental characterization and controls

A viable first study begins with **broadband variable-angle ellipsometry**, recording **model fit parameters, uncertainty correlations and actual surface roughness**. Verify the interpretation using **independent cross-sectional thickness metrology**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result Follow with a **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **backside interference or diffuse reflection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **fresnel boundary conditions and reflectance** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **wavelength, angle, polarization and surface finish** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **fresnel boundary conditions and reflectance** depends on **electromagnetic boundary response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **10.6481994 %** for the first stated input and **15.1564594 %** for the second. Determine the finite-difference sensitivity **14.7208489 (%)/(dimensionless)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 1.4 — Geometrical optics, Snell law and critical angle

### Physical mechanism and field interpretation

Phase matching of tangential wave vectors across a planar boundary gives the refraction law. Total internal reflection requires an incident medium of higher refractive index and an angle greater than the critical angle measured from the surface normal; the lower-index side still supports an evanescent field. The Goos–Hänchen shift and frustrated total internal reflection are reminders that rays approximate fields imperfectly. A real optical fiber does not become immune to bending, roughness or absorption merely because its index contrast meets the critical-angle criterion.

**Core equation and domain.** n1 sinθ1=n2 sinθ2; for n1>n2, θcritical=asin(n2/n1). This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**geometrical optics, snell law and critical angle**—the most consequential distinction in this unit is **field amplitude versus measured power**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Trace a beam inside an n=1.50 prism incident on an n=1.00 air boundary at three angles, including one below and one above the critical angle. Design a test that distinguishes specular total internal reflection from a metallic mirror using polarization and penetration-depth sensitivity.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Photon energy from vacuum wavelength** isolates a single physical dependence, using **Wavelength** as its variable. Substitute **975 nm** into its declared expression `1239.8419843320026/lam` to obtain **1.2716328 eV**. For the second case use **1131.25 nm**, obtaining **1.09599291 eV**. The output falls between these two cases. The finite-difference slope is **-0.0011240953 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Real fibers have finite core and mode profiles; numerical aperture and waveguide modes matter more than a simple zigzag ray for single-mode designs. Total internal reflection is neither required by all guiding technologies nor sufficient for negligible propagation loss.

### Experimental characterization and controls

A viable first study begins with **integrating-sphere absorption analysis**, recording **collected scattered and re-emitted channels and sphere correction**. Verify the interpretation using **collimated transmission with angular scattering scans**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization Follow with a **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **backside interference or diffuse reflection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **geometrical optics, snell law and critical angle** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **wavelength, angle, polarization and surface finish** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **geometrical optics, snell law and critical angle** depends on **electromagnetic boundary response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.2716328 eV** for the first stated input and **1.09599291 eV** for the second. Determine the finite-difference sensitivity **-0.0011240953 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_1 -->

## Lesson 1.5 — Photon description and optical energy balance

### Physical mechanism and field interpretation

A photon of vacuum wavelength λ0 has energy hc/λ0. This energy is independent of the refractive index of a transparent host; medium wavelength is λ0/n and cannot be inserted blindly into hc/λ without defining which momentum-energy convention is intended. Optical power corresponds to photon energy multiplied by photon arrival rate. Optical absorption redistributes energy into excited carriers, lattice vibrations, chemical change or luminescence; the external energy balance must track reflected, transmitted, scattered and emitted channels separately.

**Core equation and domain.** Eγ=hc/λ0; photon flux rate Ndot=P/Eγ for a narrowband beam of power P. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**photon description and optical energy balance**—the most consequential distinction in this unit is **field amplitude versus measured power**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

For a hypothetical detector illuminated at 550 nm with a known power, estimate photons incident per second and consider a detector whose external quantum efficiency is below unity. Explain why one absorbed photon need not always yield a measured electron, and why multiple-carrier gain complicates the interpretation.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Normal-incidence Fresnel power reflection** isolates a single physical dependence, using **Refractive index** as its variable. Substitute **2.58125 dimensionless** into its declared expression `100*Math.pow((n-1)/(n+1),2)` to obtain **19.4953842 %**. For the second case use **2.8875 dimensionless**, obtaining **23.5739912 %**. The output rises between these two cases. The finite-difference slope is **13.3179003 (%)/(dimensionless)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A photon-count estimate ignores spatial distribution, spectrum, polarization and dead time. Fluorescent quantum yield and photodetector responsivity are different quantities. Treat photothermal heating and photochemistry as potential hazards when raising irradiance.

### Experimental characterization and controls

A viable first study begins with **time-domain optical delay or ring-down measurements**, recording **instrument response, pulse spectrum and thermal drift**. Verify the interpretation using **a separately calibrated interferometric phase measurement**. Distinct techniques do not automatically provide independent evidence if they share the same incorrect thickness or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting optical powers, describe collection solid angle, detector sensitivity and the fate of reflected, transmitted and diffuse components. If the optical response depends on state history, state the order of measurements, any sample aging and the time allowed for thermal stabilization.

Conduct an **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples Follow with a **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **backside interference or diffuse reflection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **photon description and optical energy balance** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **wavelength, angle, polarization and surface finish** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **photon description and optical energy balance** depends on **electromagnetic boundary response**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **19.4953842 %** for the first stated input and **23.5739912 %** for the second. Determine the finite-difference sensitivity **13.3179003 (%)/(dimensionless)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Coated prism for low-reflection sensing

### The decision to be made

An optical bench shows unexpectedly weak reflectance from a coated prism. One team claims perfect antireflection, another proposes a wedge that redirects light beyond detector aperture. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Calculate Fresnel reflection and photon energy at two wavelengths, then establish the energy accounting that would be required to attribute lost detector power. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Re-measure with an integrating sphere and angle scanning; use ellipsometry to resolve phase and compare an uncoated reference prism. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A single reflected-power value cannot distinguish redirection, absorption or destructive interference.

### Five end-of-unit questions

1. Draw the optical configuration and mark phase, polarization, reflected/transmitted and absorbed/scattered pathways; give each relevant material parameter a unit.
2. Formulate two competing explanations for the observation, and identify the intervention under which their predictions diverge.
3. Calculate the response of both unit models at their slider endpoints, report units and find an approximation that limits each model.
4. Build an uncertainty and replication table separating calibration, fit-model choice, repeated measurements and independently processed specimens.
5. Write a short procurement or scientific decision stating demonstrated observations, synthetic computations, remaining uncertainties and required qualification evidence.

