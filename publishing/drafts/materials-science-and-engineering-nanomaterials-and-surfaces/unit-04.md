# Unit 4: Nanoscale characterization and uncertainty

**Guiding question:** What does each instrument actually measure, and how can multiple signals support a defensible structural claim?

## Introduction and measurement challenges

Nanometrology is an inference problem: an instrument measures a physical signal, and software maps that signal to descriptors such as diameter, phase, roughness and surface composition. This mapping includes assumptions.

Cross-check methods that sense genuinely different physical quantities. Microscopy, scattering, diffraction and spectroscopy may each be internally consistent yet answer different size and chemistry questions. State instrument resolution, standards, substrate effects and selection rules.

These five lessons emphasize **method-specific measurands**, and distinguish **coherent crystallite size versus hydrodynamic aggregate size**. To reproduce a study, specify **sample preparation, calibration and analysis protocol** before collecting data; otherwise **instrument broadening or beam-induced modification** may mimic the desired surface or nanoscale response. A proposed independent validation is **calibrated microscopy plus diffraction and solvent-state scattering**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 4.1 — Electron microscopy and specimen artifacts

### Physical mechanism and structural interpretation

Scanning electron microscopy images surface-generated electron signals while transmission electron microscopy involves electrons transmitted and scattered through thin specimens. Image contrast depends on detector geometry, composition, thickness, diffraction and sample preparation. A microscope magnification label alone does not certify size accuracy. Sample drying and electron-beam irradiation may modify soft materials, oxides and beam-sensitive nanocrystals. An adequately reported microscopy analysis includes calibration, unbiased field selection and distribution statistics.

**Core equation and domain.** Projected area equivalent diameter is d_A=2sqrt(A_projected/π); this is a two-dimensional descriptor and not automatically a 3D particle diameter. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**electron microscopy and specimen artifacts**—the most consequential distinction in this unit is **coherent crystallite size versus hydrodynamic aggregate size**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare TEM core diameter with SEM aggregate morphology for the same nanopowder. Design a blinded counting protocol that rejects overlapping particles and records the rejected fraction.

Perform a thought experiment: assume the original explanation is wrong and **instrument broadening or beam-induced modification** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **sample preparation, calibration and analysis protocol** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Scherrer coherence length estimate** isolates a single physical dependence, using **Corrected diffraction peak FWHM** as its variable. Substitute **0.425 degrees** into its declared expression `0.9*0.15406/((b*Math.PI/180)*Math.cos(20*Math.PI/180))` to obtain **19.8920842 nm**. For the second case use **0.65 degrees**, obtaining **13.0063627 nm**. The output falls between these two cases. The finite-difference slope is **-30.6032065 (nm)/(degrees)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** K=0.9, Cu Kα λ=0.15406 nm, Bragg angle θ=20°, β is strain- and instrument-corrected FWHM in radians; length is coherent domain not particle diameter. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A single dramatic micrograph cannot establish purity, typical size, production yield or absence of sub-resolution material. Contrast transfer and beam damage require controls for quantitative interpretation.

### Experimental characterization and controls

Conduct an **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. Follow with a **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **instrument broadening or beam-induced modification**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **electron microscopy and specimen artifacts** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **sample preparation, calibration and analysis protocol** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **electron microscopy and specimen artifacts** depends on **method-specific measurands**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **19.8920842 nm** for the first stated input and **13.0063627 nm** for the second. Determine the finite-difference sensitivity **-30.6032065 (nm)/(degrees)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **instrument broadening or beam-induced modification** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **calibrated microscopy plus diffraction and solvent-state scattering**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_6 -->

## Lesson 4.2 — X-ray diffraction and coherent crystallite size

### Physical mechanism and structural interpretation

Diffraction describes periodic electron-density arrangements, not simply physical particle dimensions. Broad diffraction peaks may arise from small coherent domains, lattice microstrain, stacking disorder and instrumental convolution. The Scherrer expression supplies a provisional coherence length from corrected width, but it is not a full microstructure analysis. A nanocrystal can be larger than its coherent domains and a polycrystalline grain need not be one particle. Rietveld refinement can assist phase analysis if the structural and instrument models are appropriate.

**Core equation and domain.** Scherrer D≈Kλ/(β cosθ), where β is sample-related broadening in radians at Bragg angle θ and K is a shape factor. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**x-ray diffraction and coherent crystallite size**—the most consequential distinction in this unit is **coherent crystallite size versus hydrodynamic aggregate size**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A broad peak appears after milling. Measure an instrumental standard and multiple reflections at distinct diffraction angles before concluding the particles have shrunk.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **XPS substrate intensity attenuation** isolates a single physical dependence, using **Uniform overlayer thickness** as its variable. Substitute **3 nm** into its declared expression `100*Math.exp(-t/(3*Math.cos(45*Math.PI/180)))` to obtain **24.3116734 %**. For the second case use **4.5 nm**, obtaining **11.987325 %**. The output falls between these two cases. The finite-difference slope is **-8.21623229 (%)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Simple planar overlayer with effective attenuation length 3 nm, detection angle 45° relative to surface normal, no elastic effects or roughness. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Do not use raw FWHM without subtracting instrument broadening by a justified line-profile method. Unknown peak overlap, texture and amorphous background can defeat simplified size estimates.

### Experimental characterization and controls

Conduct an **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. Follow with a **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **instrument broadening or beam-induced modification**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **x-ray diffraction and coherent crystallite size** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **sample preparation, calibration and analysis protocol** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **x-ray diffraction and coherent crystallite size** depends on **method-specific measurands**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **24.3116734 %** for the first stated input and **11.987325 %** for the second. Determine the finite-difference sensitivity **-8.21623229 (%)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 4.3 — Atomic force microscopy and tip convolution

### Physical mechanism and structural interpretation

An atomic-force microscope tracks force-related cantilever response to infer a surface height map. Lateral feature width is broadened by finite tip radius; vertical displacement has a different calibration pathway. Adhesive forces, feedback bandwidth, humidity and surface compliance can alter apparent topography. Tapping and contact modes impose different forces, so results from fragile polymers or loosely bound particles may differ. Phase or force maps require models; visually striking color differences need not be chemical maps.

**Core equation and domain.** RMS roughness Sq=sqrt[(1/A)∫(z−zmean)²dA] for an explicitly specified sampled area and preprocessing convention. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**atomic force microscopy and tip convolution**—the most consequential distinction in this unit is **coherent crystallite size versus hydrodynamic aggregate size**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare AFM line profiles over nanoparticles deposited on a substrate with corresponding electron micrographs. Explain why particle height may be more reliable than lateral width in the presence of tip convolution.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Scherrer coherence length estimate** isolates a single physical dependence, using **Corrected diffraction peak FWHM** as its variable. Substitute **0.875 degrees** into its declared expression `0.9*0.15406/((b*Math.PI/180)*Math.cos(20*Math.PI/180))` to obtain **9.66186947 nm**. For the second case use **1.1 degrees**, obtaining **7.68557799 nm**. The output falls between these two cases. The finite-difference slope is **-8.7835177 (nm)/(degrees)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

AFM height data can include scan drift, plane subtraction artifacts, tip contamination and deformation. A reported root-mean-square roughness must include scan area, spatial filtering and sampling density.

### Experimental characterization and controls

Conduct an **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. Follow with a **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **instrument broadening or beam-induced modification**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **atomic force microscopy and tip convolution** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **sample preparation, calibration and analysis protocol** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **atomic force microscopy and tip convolution** depends on **method-specific measurands**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **9.66186947 nm** for the first stated input and **7.68557799 nm** for the second. Determine the finite-difference sensitivity **-8.7835177 (nm)/(degrees)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 4.4 — Surface-sensitive spectroscopy and information depth

### Physical mechanism and structural interpretation

X-ray photoelectron spectroscopy detects emitted photoelectrons whose escape probability decays with depth, making the technique sensitive to near-surface chemistry. Chemical shifts are affected by oxidation state, charging and screening. Raman spectroscopy interrogates vibrations but depends on laser wavelength, optical penetration, heating and selection rules. Secondary-ion mass spectrometry is highly sensitive but can distort relative intensities through matrix effects. Complementary tools reduce ambiguity only if each controls different confounders.

**Core equation and domain.** A simple overlayer model gives I_sub(t)/I_sub(0)=exp[−t/(λ_eff cosθ)] with θ measured from the surface normal. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**surface-sensitive spectroscopy and information depth**—the most consequential distinction in this unit is **coherent crystallite size versus hydrodynamic aggregate size**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A thin oxide coats a conductive nanoparticle support. Compare an XPS attenuation estimate, Raman signatures and cross-sectional elemental mapping, and ask which technique constrains thickness versus chemistry.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **XPS substrate intensity attenuation** isolates a single physical dependence, using **Uniform overlayer thickness** as its variable. Substitute **6 nm** into its declared expression `100*Math.exp(-t/(3*Math.cos(45*Math.PI/180)))` to obtain **5.91057466 %**. For the second case use **7.5 nm**, obtaining **2.91431931 %**. The output falls between these two cases. The finite-difference slope is **-1.99750356 (%)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

XPS intensity attenuation assumes smooth layers with uniform thickness and known attenuation length; rough particles and differential charging make fitted oxide thickness model-dependent.

### Experimental characterization and controls

Conduct an **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. Follow with a **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **instrument broadening or beam-induced modification**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **surface-sensitive spectroscopy and information depth** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **sample preparation, calibration and analysis protocol** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **surface-sensitive spectroscopy and information depth** depends on **method-specific measurands**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **5.91057466 %** for the first stated input and **2.91431931 %** for the second. Determine the finite-difference sensitivity **-1.99750356 (%)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_7 -->

## Lesson 4.5 — Scattering, porosimetry and multi-technique inference

### Physical mechanism and structural interpretation

Dynamic light scattering estimates translational diffusion using intensity fluctuations and maps it to an equivalent hydrodynamic size only after choosing a solvent model. Small-angle X-ray scattering samples ensemble electron-density contrasts and can reveal correlation lengths or shape-dependent form factors. Gas physisorption yields accessible area or pore metrics using adsorption models. No single technique uniquely distinguishes primary crystallite, isolated particle, cluster and pore. A robust report uses orthogonal methods plus controls of sample state.

**Core equation and domain.** In a dilute Newtonian solvent, D=kBT/(6πηrH) converts diffusivity to hydrodynamic radius using viscosity η and temperature T. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**scattering, porosimetry and multi-technique inference**—the most consequential distinction in this unit is **coherent crystallite size versus hydrodynamic aggregate size**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A dispersion looks monodisperse in TEM but DLS reports a broad hydrodynamic tail. Hypothesize sparse clusters, solvation shells and preparation artifacts; propose tests on both original dispersion and a dried replicate.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Scherrer coherence length estimate** isolates a single physical dependence, using **Corrected diffraction peak FWHM** as its variable. Substitute **1.325 degrees** into its declared expression `0.9*0.15406/((b*Math.PI/180)*Math.cos(20*Math.PI/180))` to obtain **6.38047984 nm**. For the second case use **1.55 degrees**, obtaining **5.45428115 nm**. The output falls between these two cases. The finite-difference slope is **-4.11643861 (nm)/(degrees)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Gas-adsorption BET area may be inappropriate for certain microporous chemistries and reactive surfaces without checks. SAXS inversion is often nonunique without geometry or distribution constraints.

### Experimental characterization and controls

A viable first study begins with **rheology, suspension stability and sedimentation monitoring**, recording **solvent viscosity, temperature and storage history**. Verify the interpretation using **a particle-number or mass-balanced sample assay**. Distinct techniques do not automatically provide independent evidence if they share the same mislabeled sample state or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting size, specify whether it means geometric diameter, coherent domain, hydrodynamic radius or an equivalent-sphere inference. Record solvent, drying, handling, storage, atmosphere and the time allowed for the material to equilibrate.

Conduct an **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. Follow with a **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **instrument broadening or beam-induced modification**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **scattering, porosimetry and multi-technique inference** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **sample preparation, calibration and analysis protocol** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **scattering, porosimetry and multi-technique inference** depends on **method-specific measurands**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **6.38047984 nm** for the first stated input and **5.45428115 nm** for the second. Determine the finite-difference sensitivity **-4.11643861 (nm)/(degrees)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Reconciling three conflicting size measurements

### The decision to be made

An XRD analysis, a TEM analysis and DLS produce three different nominal particle sizes for the same powder. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Quantify coherent-domain estimates but explicitly separate them from electron-image geometry and hydrodynamic equivalents. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Use an instrument standard, repeat specimen preparation and cross-method population matching to explain inconsistencies. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Method differences can be valid and should not be averaged into one false precise diameter.

### Five end-of-unit questions

