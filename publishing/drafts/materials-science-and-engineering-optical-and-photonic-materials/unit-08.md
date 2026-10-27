# Unit 8: Nanophotonics, optical metrology and engineering qualification

**Guiding question:** How should an optical material claim be tested, uncertainty-quantified and translated into a reliable device specification?

## Introduction and measurement challenges

Nanoscale optical resonances provide large sensitivities but are also vulnerable to dimensional disorder, environmental drift and numerical-model degeneracy. An optical spectrum rarely identifies morphology uniquely.

A reliable materials decision connects calibration, independent structural measurements, environmental testing and manufacturing variation to a declared acceptance criterion.

These five lessons emphasize **nanoscale optics and verification**, and distinguish **intrinsic optical quality versus extrinsic specimen variability**. To reproduce a study, specify **particle size, surface condition and instrument resolution** before collecting data; otherwise **nonspecific response, instrument drift or model degeneracy** may mimic the desired optical response. A proposed independent validation is **blinded controls with independent morphology measurement**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 8.1 — Plasmonic and dielectric nanoresonators

### Physical mechanism and field interpretation

Metal nanoparticles can sustain collective charge oscillations, while high-index dielectric particles support electric and magnetic Mie-type resonances. Their spectral signatures depend on shape, local environment, size distributions and near-field coupling. Strong local field enhancement can be useful for sensing but increases sensitivity to contamination and thermal damage. A measured absorption peak that moves upon analyte exposure is not automatically selective; nonspecific adsorption and solvent index changes can cause a similar shift.

**Core equation and domain.** A resonance sensor is commonly characterized by S=dλres/dnambient, but sensing figure of merit also depends on linewidth and noise. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**plasmonic and dielectric nanoresonators**—the most consequential distinction in this unit is **intrinsic optical quality versus extrinsic specimen variability**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Propose a sensor comparison between gold nanostructures and high-index dielectric resonators. Specify what microscopy, refractive-index controls and blank buffer measurements would distinguish geometric fabrication variation from a chemically specific binding event.

Perform a thought experiment: assume the original explanation is wrong and **nonspecific response, instrument drift or model degeneracy** controls the measured trend. Sketch the alternate optical path, locate which energy channel or wavefront would be altered, and predict which observable would differ when you adjust **particle size, surface condition and instrument resolution** independently. A theory that explains a spectral curve only after its parameters are chosen to match that same curve is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Rayleigh-type wavelength scaling** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **475 nm** into its declared expression `Math.pow(550/lam,4)` to obtain **1.79753071 relative**. For the second case use **550 nm**, obtaining **1 relative**. The output falls between these two cases. The finite-difference slope is **-0.0106337428 (relative)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Idealized scatter-loss proxy proportional to λ⁻⁴ at fixed particle-size distribution, normalized to 550 nm; not a measured glass or haze spectrum. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A dipolar quasistatic model is inadequate for particles comparable to wavelength, nonlocal effects or strong interparticle coupling. Detection limit requires noise, drift, recovery and false-positive measurements, not merely spectral sensitivity in nm/RIU.

### Experimental characterization and controls

Conduct an **safety and aging audit**: document photodarkening, photobleaching, optical power density and representative operating-condition tests Follow with a **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **nonspecific response, instrument drift or model degeneracy**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **plasmonic and dielectric nanoresonators** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle size, surface condition and instrument resolution** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **plasmonic and dielectric nanoresonators** depends on **nanoscale optics and verification**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.79753071 relative** for the first stated input and **1 relative** for the second. Determine the finite-difference sensitivity **-0.0106337428 (relative)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **nonspecific response, instrument drift or model degeneracy** from an intrinsic material mechanism. Include sample geometry, source spectrum, polarization, calibration, measurement replication and rejection criteria. *Solution guidance:* prioritize **blinded controls with independent morphology measurement**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_14 -->

## Lesson 8.2 — Rayleigh loss and structural disorder

### Physical mechanism and field interpretation

Subwavelength density fluctuations scatter optical power with a strong wavelength dependence. The familiar inverse-fourth-power law is an idealized result under fixed scatterer statistics; real fibers and films contain broad spatial-frequency distributions and correlated disorder. Optical attenuation may be dominated by a small number of large defects rather than the bulk average composition. Identifying the mechanism requires both wavelength-resolved loss and structural analysis.

**Core equation and domain.** An illustrative fixed-disorder loss ratio is α(λ)/α(λref)≈(λref/λ)⁴ for Rayleigh-dominated scattering. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**rayleigh loss and structural disorder**—the most consequential distinction in this unit is **intrinsic optical quality versus extrinsic specimen variability**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Use the normalized λ⁻⁴ calculator as a reference curve. Compare a fabricated transparent ceramic whose scattering decreases more slowly with wavelength. Propose two microstructural explanations and a measurement capable of rejecting each.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Optical resonator quality factor** isolates a single physical dependence, using **Resonance linewidth** as its variable. Substitute **0.5075 nm** into its declared expression `1550/dw` to obtain **3054.18719 dimensionless**. For the second case use **0.75625 nm**, obtaining **2049.58678 dimensionless**. The output falls between these two cases. The finite-difference slope is **-4038.59463 (dimensionless)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Q≈λ0/Δλ for narrow resonances at 1550 nm, with a consistently defined linewidth; assumes spectral Q estimates apply. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the optical constants of a specimen, prove its microstructure or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A Rayleigh scaling fit over a narrow wavelength interval can be accidental. Do not infer an absolute absorption coefficient from a normalized scattering proxy. Integrating-sphere transmission and angular-resolved haze should be reported alongside total attenuation.

### Experimental characterization and controls

Conduct an **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval Follow with a **independent specimens audit**: distinguish repeated readings of one device from separately fabricated and randomly selected samples For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **nonspecific response, instrument drift or model degeneracy**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **rayleigh loss and structural disorder** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle size, surface condition and instrument resolution** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **rayleigh loss and structural disorder** depends on **nanoscale optics and verification**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **3054.18719 dimensionless** for the first stated input and **2049.58678 dimensionless** for the second. Determine the finite-difference sensitivity **-4038.59463 (dimensionless)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 8.3 — Spectroscopic ellipsometry and inverse problems

### Physical mechanism and field interpretation

Ellipsometry measures the amplitude ratio and phase difference between two reflected polarization components. Optical constants and thickness are inferred using an assumed layer model, and the inverse problem may be nonunique. Correlated fitted thickness and index can generate apparently precise results even when each parameter is poorly identified. Physical dispersion constraints, multiple incidence angles and independent stylus or electron-microscopy thickness measurements improve robustness.

**Core equation and domain.** The measured complex ratio is ρ=rp/rs=tanΨ exp(iΔ); extracting ñ and thickness requires a physically constrained forward model. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**spectroscopic ellipsometry and inverse problems**—the most consequential distinction in this unit is **intrinsic optical quality versus extrinsic specimen variability**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Fit an optical thin film as a single homogeneous layer and then as a graded layer. If both produce similar residuals, describe an independent observation that would favor one physical interpretation without inventing certainty.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Rayleigh-type wavelength scaling** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **625 nm** into its declared expression `Math.pow(550/lam,4)` to obtain **0.59969536 relative**. For the second case use **700 nm**, obtaining **0.381117243 relative**. The output falls between these two cases. The finite-difference slope is **-0.0029143749 (relative)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Instrument alignment, backside reflection, surface roughness and depolarization invalidate overly simple models. A numerical fit error is not a materials property error bar unless model inadequacy and sample variability have been addressed.

### Experimental characterization and controls

Conduct an **units and wavelength audit**: identify vacuum versus medium wavelengths and distinguish optical power dB from field-amplitude ratios Follow with a **model identification audit**: test multiple plausible thickness/index/absorption or mode-coupling explanations for the same optical spectrum For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **nonspecific response, instrument drift or model degeneracy**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **spectroscopic ellipsometry and inverse problems** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle size, surface condition and instrument resolution** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **spectroscopic ellipsometry and inverse problems** depends on **nanoscale optics and verification**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.59969536 relative** for the first stated input and **0.381117243 relative** for the second. Determine the finite-difference sensitivity **-0.0029143749 (relative)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 8.4 — Resonator Q and measurement resolution

### Physical mechanism and field interpretation

An optical quality factor compares stored energy with dissipated energy per radian of oscillation and is often approximated spectrally by center wavelength over resonance linewidth. The observed linewidth includes external coupling and intrinsic loss, and instrument resolution can make a narrow resonance appear broader. Thermal drift during a wavelength sweep can distort lineshapes. Spectral Q alone does not specify fabrication yield, thermal noise or the accessible cavity field.

**Core equation and domain.** Qloaded≈λ0/ΔλFWHM when Δλ≪λ0 and the scan is calibrated; 1/Qloaded=1/Qintrinsic+1/Qcoupling. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**resonator q and measurement resolution**—the most consequential distinction in this unit is **intrinsic optical quality versus extrinsic specimen variability**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

At a fixed center wavelength of 1550 nm, compare linewidths from 2 nm down to 0.01 nm. Explain why a spectrometer with resolution comparable to the linewidth cannot reliably report the narrowest value without appropriate characterization.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Optical resonator quality factor** isolates a single physical dependence, using **Resonance linewidth** as its variable. Substitute **1.005 nm** into its declared expression `1550/dw` to obtain **1542.28856 dimensionless**. For the second case use **1.25375 nm**, obtaining **1236.29113 dimensionless**. The output falls between these two cases. The finite-difference slope is **-1230.14042 (dimensionless)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The relation Q=λ/Δλ presumes an isolated narrow resonance and an appropriate linewidth definition; broad, asymmetric, multimode or strongly time-varying spectra require a different analysis. Loaded and intrinsic Q must be differentiated.

### Experimental characterization and controls

Conduct an **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result Follow with a **energy conservation audit**: check reflected, transmitted, absorbed, scattered and emitted optical powers, with a clear accounting interval For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **nonspecific response, instrument drift or model degeneracy**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **resonator q and measurement resolution** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle size, surface condition and instrument resolution** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **resonator q and measurement resolution** depends on **nanoscale optics and verification**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1542.28856 dimensionless** for the first stated input and **1236.29113 dimensionless** for the second. Determine the finite-difference sensitivity **-1230.14042 (dimensionless)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_15 -->

## Lesson 8.5 — Optical materials qualification, safety and lifecycle

### Physical mechanism and field interpretation

Material selection for photonics spans optical dispersion, transmission, coating uniformity, processing temperature, thermo-mechanical mismatch, radiation durability, cost, repairability and supplier traceability. A spectacular single-device spectrum is not a production specification. Qualification requires distinct specimens and fabrication lots, representative environments and predeclared acceptance criteria. Some apparently sustainable optical materials contain hazardous processing reagents or cannot be recovered economically after packaging.

**Core equation and domain.** A decision matrix should distinguish pass/fail constraints from weighted preferences and propagate the uncertainty of performance margins. This formula is not a universal 'optical property' divorced from the experimental geometry. State whether it refers to a field amplitude, power fraction, bulk constitutive coefficient, eigenmode property or device transfer characteristic. Before applying it, label its independent variables and units, and clarify whether the wavelength lies in vacuum or within a material. For the present topic—**optical materials qualification, safety and lifecycle**—the most consequential distinction in this unit is **intrinsic optical quality versus extrinsic specimen variability**. Explain how a change of measurement collection angle or device geometry could affect the result without a change in the underlying chemical composition.

### Example to reason through before computation

Prepare a comparison of silica, polymer and chalcogenide devices for a specified near-infrared use case. Reject any choice whose absorption, thermal range or chemical compatibility violates a hard requirement, even if its nonlinear coefficient looks attractive.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Rayleigh-type wavelength scaling** isolates a single physical dependence, using **Vacuum wavelength** as its variable. Substitute **775 nm** into its declared expression `Math.pow(550/lam,4)` to obtain **0.253655304 relative**. For the second case use **850 nm**, obtaining **0.175297231 relative**. The output falls between these two cases. The finite-difference slope is **-0.00104477431 (relative)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Theoretical figures omit procurement, yield and calibration risk; demonstrate reproducibility across fabrication lots before using measurements as nominal catalog values. High optical intensities, lasers, UV radiation and processing chemicals require appropriate facility training and safety assessment.

### Experimental characterization and controls

Conduct an **geometry and modes audit**: report beam size, numerical aperture, layer thickness, waveguide cross-section and polarization Follow with a **temperature and drift audit**: record thermal history, warmup time and wavelength drift rather than subtracting a trend after seeing the result For a comparison of two candidate materials, test whether the difference persists after normalizing geometry, wavelengths and device operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **nonspecific response, instrument drift or model degeneracy**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **optical materials qualification, safety and lifecycle** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle size, surface condition and instrument resolution** and how an alternate mechanism would respond. Discuss whether the required test probes a microscopic variable, a device-level energy channel or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'optical performance'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **optical materials qualification, safety and lifecycle** depends on **nanoscale optics and verification**. Propose a competing cause of the same spectral or power trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.253655304 relative** for the first stated input and **0.175297231 relative** for the second. Determine the finite-difference sensitivity **-0.00104477431 (relative)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Photonic sensor qualification for chemical monitoring

### The decision to be made

A nanoscale spectral sensor produces narrow resonances and large shifts in one laboratory. At a second facility it drifts during cleaning and exposes unexpected false positives. Begin with a table of hypothesized causes, the optical boundary conditions each requires, the most informative measurable quantity and a test condition on which its prediction differs from a competitor. Identify whether the candidate performance metric concerns material, component or assembled system. The three are not interchangeable, even when they all display wavelength-resolved plots.

### Computational investigation and sensitivity

Explore a Rayleigh loss proxy and spectral quality-factor limits without claiming they determine analyte selectivity; build a measurement and false-positive uncertainty budget. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine their results into a manufactured device forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Use controlled blank chemicals, environmental sweeps, calibration transfers, microscopy and blind replicate tests across multiple production lots. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record both the intended optical channel and the channels not collected by the apparatus. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Q and wavelength sensitivity alone do not establish detection specificity or commercial reliability.

### Five end-of-unit questions

