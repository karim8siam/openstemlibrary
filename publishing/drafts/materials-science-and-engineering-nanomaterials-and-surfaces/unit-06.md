# Unit 6: Quantum, electronic and photonic effects in nanostructures

**Guiding question:** When do geometric dimensions modify electronic states and optical response, and what mechanisms can masquerade as quantum size effects?

## Introduction and measurement challenges

Quantum and optical responses can be strongly size-dependent when structural dimensions approach wavefunction or electromagnetic characteristic scales. Equations for ideal wells, spheres and bulk dielectric functions are guiding models, not universal nanomaterial properties.

Surface states, dielectric surroundings, strain, composition gradients and ensemble polydispersity can move a spectral feature. An observed blue or red shift therefore needs at least one structurally independent test.

These five lessons emphasize **confinement and electronic interfaces**, and distinguish **intrinsic electronic states versus trap-mediated optical shifts**. To reproduce a study, specify **particle geometry, ligands, temperature and dielectric host** before collecting data; otherwise **surface defect emission or ensemble inhomogeneity** may mimic the desired surface or nanoscale response. A proposed independent validation is **absorption, time-resolved emission and composition checks**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 6.1 — Quantum confinement and effective mass

### Physical mechanism and structural interpretation

A charge carrier confined along one or more dimensions acquires discrete energy contributions when the confining length becomes comparable to its wavefunction scale. In semiconductor quantum wells, wires and dots, both effective masses and confinement directions influence transition energies. This effect is not guaranteed simply because a particle measures less than 100 nm; exciton Bohr radius, potential barriers and dielectric screening are key. Shape and strain shift electronic states and can compete with confinement.

**Core equation and domain.** For a one-dimensional infinite well, first confined kinetic energy E1=π²ℏ²/(2m*L²), with L in metres and effective mass m*. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**quantum confinement and effective mass**—the most consequential distinction in this unit is **intrinsic electronic states versus trap-mediated optical shifts**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare two semiconductor nanocrystal populations with similar composition but distinct diameters and passivating ligands. Plan an optical-absorption and photoluminescence experiment that separates size shifts from defect-related emission.

Perform a thought experiment: assume the original explanation is wrong and **surface defect emission or ensemble inhomogeneity** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **particle geometry, ligands, temperature and dielectric host** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Electron-in-a-box confinement energy** isolates a single physical dependence, using **Quantum well width** as its variable. Substitute **6.375 nm** into its declared expression `(Math.PI*Math.PI*Math.pow(6.62607015e-34/(2*Math.PI),2)/(2*0.13*9.1093837139e-31*Math.pow(L*1e-9,2)))/1.602176634e-19` to obtain **0.071173603 eV**. For the second case use **9.75 nm**, obtaining **0.0304277681 eV**. The output falls between these two cases. The finite-difference slope is **-0.01207284 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Infinite one-dimensional well, effective mass 0.13 m_e, single-particle ground-state contribution; ignores excitons, nonparabolicity and finite barriers. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Infinite-wall effective-mass formulas exaggerate quantization for finite barriers and may fail at very small sizes where band structure and atomistic chemistry matter.

### Experimental characterization and controls

Conduct an **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. Follow with a **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface defect emission or ensemble inhomogeneity**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **quantum confinement and effective mass** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle geometry, ligands, temperature and dielectric host** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **quantum confinement and effective mass** depends on **confinement and electronic interfaces**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.071173603 eV** for the first stated input and **0.0304277681 eV** for the second. Determine the finite-difference sensitivity **-0.01207284 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **surface defect emission or ensemble inhomogeneity** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **absorption, time-resolved emission and composition checks**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_10 -->

## Lesson 6.2 — Density of states in low-dimensional systems

### Physical mechanism and structural interpretation

In idealized electronic bands, the density-of-states energy dependence differs among three-dimensional bulk solids, two-dimensional wells, one-dimensional wires and zero-dimensional dots. Measured electronic spectra are smoothed by disorder, temperature, finite lifetimes and size dispersion. A sharp one-dimensional Van Hove feature can help identify subband structure, but additional evidence is needed to separate it from a localized defect or excitonic absorption. Electrodes and substrates perturb low-dimensional spectra.

**Core equation and domain.** For a parabolic 3D band, g3D(E)∝sqrt(E−Ec) above the edge; ideal 2D subbands contribute step-like constants and ideal 1D subbands produce inverse-square-root singularities. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**density of states in low-dimensional systems**—the most consequential distinction in this unit is **intrinsic electronic states versus trap-mediated optical shifts**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Sketch qualitative density of states for bulk, well, wire and dot, then describe how a broad size distribution turns sharp features into an ensemble band.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Coulomb charging energy of a nanosphere** isolates a single physical dependence, using **Particle radius** as its variable. Substitute **9 nm** into its declared expression `1.43996448/(2*5*r)` to obtain **0.0159996053 eV**. For the second case use **12.5 nm**, obtaining **0.0115197158 eV**. The output falls between these two cases. The finite-difference slope is **-0.00127996843 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Isolated spherical conductor model E=e²/(2C), C=4πε0εr r, εr=5 constant; quantum tunneling and electrochemical environment excluded. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Parabolic-band DOS expressions assume free-like carriers and neglect many-body interactions; they do not capture graphene Dirac cones or strongly correlated nanostructures automatically.

### Experimental characterization and controls

Conduct an **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. Follow with a **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface defect emission or ensemble inhomogeneity**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **density of states in low-dimensional systems** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle geometry, ligands, temperature and dielectric host** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **density of states in low-dimensional systems** depends on **confinement and electronic interfaces**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.0159996053 eV** for the first stated input and **0.0115197158 eV** for the second. Determine the finite-difference sensitivity **-0.00127996843 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 6.3 — Excitons, radiative recombination and surface traps

### Physical mechanism and structural interpretation

Optical excitation can generate correlated electron–hole states called excitons. In quantum dots the emission wavelength, quantum yield and lifetime depend on confinement, surface trap populations, passivation chemistry and nonradiative recombination. Apparent photoluminescence brightness additionally depends on pump absorption and collection optics. Defects may introduce sub-bandgap pathways that change emission even if the crystalline core size stays fixed. Time-resolved measurements can distinguish some kinetic mechanisms but rarely identify all traps uniquely.

**Core equation and domain.** For a single population, internal radiative fraction ηr=kr/(kr+knr), with separate radiative and nonradiative decay rates. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**excitons, radiative recombination and surface traps**—the most consequential distinction in this unit is **intrinsic electronic states versus trap-mediated optical shifts**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Two batches have the same absorption peak but different emission yields. Design a comparison using absolute photoluminescence quantum yield, time-resolved decay and chemical surface analysis.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Electron-in-a-box confinement energy** isolates a single physical dependence, using **Quantum well width** as its variable. Substitute **13.125 nm** into its declared expression `(Math.PI*Math.PI*Math.pow(6.62607015e-34/(2*Math.PI),2)/(2*0.13*9.1093837139e-31*Math.pow(L*1e-9,2)))/1.602176634e-19` to obtain **0.0167911602 eV**. For the second case use **16.5 nm**, obtaining **0.0106245719 eV**. The output falls between these two cases. The finite-difference slope is **-0.00182713727 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A short lifetime is not always evidence of traps: radiative and nonradiative rates must be considered together. Photobleaching and blinking can bias time-averaged signals.

### Experimental characterization and controls

Conduct an **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. Follow with a **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface defect emission or ensemble inhomogeneity**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **excitons, radiative recombination and surface traps** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle geometry, ligands, temperature and dielectric host** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **excitons, radiative recombination and surface traps** depends on **confinement and electronic interfaces**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.0167911602 eV** for the first stated input and **0.0106245719 eV** for the second. Determine the finite-difference sensitivity **-0.00182713727 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 6.4 — Metal nanostructures and localized plasmons

### Physical mechanism and structural interpretation

Conduction electrons in metallic nanoparticles can exhibit collective optical oscillations and electromagnetic near-field localization. Shape, size, surrounding refractive index and surface damping influence the resonance, while coupling between nearby particles leads to hybridized modes. Optical extinction equals absorption plus scattering; their relative fractions change with size and geometry. A strong color shift upon aggregation need not signal any change in chemical composition. Classical local electrodynamics may fail for atomic-sized junctions.

**Core equation and domain.** In the quasistatic small-sphere limit, polarizability scales as α∝r³(εp−εm)/(εp+2εm), where complex permittivities control resonance and loss. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**metal nanostructures and localized plasmons**—the most consequential distinction in this unit is **intrinsic electronic states versus trap-mediated optical shifts**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare isolated spherical gold-like particles with a dense cluster in a different solvent. Predict qualitative shifts in extinction and require microscopy plus refractive-index-controlled measurements.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Coulomb charging energy of a nanosphere** isolates a single physical dependence, using **Particle radius** as its variable. Substitute **16 nm** into its declared expression `1.43996448/(2*5*r)` to obtain **0.008999778 eV**. For the second case use **19.5 nm**, obtaining **0.00738443323 eV**. The output falls between these two cases. The finite-difference slope is **-0.000461527077 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A narrow optical resonance does not prove efficient photochemical charge generation; photothermal heating and antenna effects are competing explanations. Classical dipoles do not capture all retardation and multipolar effects.

### Experimental characterization and controls

Conduct an **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. Follow with a **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface defect emission or ensemble inhomogeneity**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **metal nanostructures and localized plasmons** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle geometry, ligands, temperature and dielectric host** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **metal nanostructures and localized plasmons** depends on **confinement and electronic interfaces**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.008999778 eV** for the first stated input and **0.00738443323 eV** for the second. Determine the finite-difference sensitivity **-0.000461527077 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_11 -->

## Lesson 6.5 — Single-electron charging and electronic transport

### Physical mechanism and structural interpretation

For small conductive islands, adding one electron can cost charging energy comparable with thermal energy, making discrete transport regimes experimentally accessible if tunnel resistances and temperature permit them. Nanowire devices additionally exhibit contact resistance, surface scattering, grain-boundary barriers and electrochemical gating. A nonlinear current-voltage curve alone is insufficient proof of Coulomb blockade, and charge noise can resemble switching behavior. Electrical breakdown can be dominated by interfaces rather than pristine bulk.

**Core equation and domain.** For isolated spherical conductor capacitance C≈4πε0εr r, nominal charging E_C=e²/(2C); observe charging effects only when relevant energies exceed broadening scales. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**single-electron charging and electronic transport**—the most consequential distinction in this unit is **intrinsic electronic states versus trap-mediated optical shifts**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Design a measurement of a single-electron island using temperature and gate dependence as discriminators rather than relying on one I–V trace.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Electron-in-a-box confinement energy** isolates a single physical dependence, using **Quantum well width** as its variable. Substitute **19.875 nm** into its declared expression `(Math.PI*Math.PI*Math.pow(6.62607015e-34/(2*Math.PI),2)/(2*0.13*9.1093837139e-31*Math.pow(L*1e-9,2)))/1.602176634e-19` to obtain **0.00732259568 eV**. For the second case use **23.25 nm**, obtaining **0.00535098108 eV**. The output falls between these two cases. The finite-difference slope is **-0.000584182104 (eV)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The capacitance of an isolated sphere is a crude proxy for a device near electrodes and substrates. Quantized level spacing and charging energy are different scales.

### Experimental characterization and controls

Conduct an **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. Follow with a **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface defect emission or ensemble inhomogeneity**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **single-electron charging and electronic transport** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **particle geometry, ligands, temperature and dielectric host** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **single-electron charging and electronic transport** depends on **confinement and electronic interfaces**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **0.00732259568 eV** for the first stated input and **0.00535098108 eV** for the second. Determine the finite-difference sensitivity **-0.000584182104 (eV)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Disentangling quantum dot shifts from surface-trap changes

### The decision to be made

A semiconductor quantum dot shows an emission shift and intensity increase after a new passivation step. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Calculate single-direction confinement energy and isolated-sphere charging scale to compare approximate energies. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure particle dimensions, absorption edge, time-resolved emission and surface chemical state in both batches. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Effective-mass box energies are not literal emission lines and bare capacitance is not a full device model.

### Five end-of-unit questions

