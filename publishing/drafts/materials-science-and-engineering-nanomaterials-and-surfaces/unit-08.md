# Unit 8: Applications, reproducibility, environment and safe design

**Guiding question:** How can nanoscale evidence be translated into robust product decisions without overstating performance, environmental safety or scale-up success?

## Introduction and measurement challenges

Applications involve multiple length scales and competing measures of success: property improvement, manufacturability, stability, environmental transport and acceptable occupational controls. No nanoscale formula substitutes for product qualification.

A research proposal should contain performance controls, uncertainty-aware comparisons, batch reproducibility and a strategy for identifying undesired released or transformed material. Measurement and safety claims must be independent of promotional targets.

These five lessons emphasize **fitness for intended use**, and distinguish **nominal synthesis size versus in-use transported form**. To reproduce a study, specify **batch repeatability, flow and exposure pathway** before collecting data; otherwise **transformation, dissolution and assay interference** may mimic the desired surface or nanoscale response. A proposed independent validation is **mass balance and independent validated endpoints**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 8.1 — Nanocomposites and multifunctional integration

### Physical mechanism and structural interpretation

Nanoparticle fillers can change stiffness, barrier performance, conductivity and heat transport when interfaces and dispersion are engineered. High intrinsic filler conductivity does not imply a highly conductive composite: contact resistance, orientation and percolation determine network connectivity. Likewise, stiff fillers can weaken a matrix if poorly bonded or agglomerated. Scaling from a small cast film to continuous manufacturing introduces residence-time distributions and shear histories that affect filler networks.

**Core equation and domain.** An ideal parallel rule-of-mixtures modulus E≈φEf+(1−φ)Em is an upper-bound-like approximation under strong alignment and load transfer, not a generic random nanocomposite law. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**nanocomposites and multifunctional integration**—the most consequential distinction in this unit is **nominal synthesis size versus in-use transported form**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare a polymer with 1 and 10 volume-percent platelets while recording processing temperature, dispersion quality, mechanical tests and barrier performance. Define whether a gain is per mass or per thickness.

Perform a thought experiment: assume the original explanation is wrong and **transformation, dissolution and assay interference** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **batch repeatability, flow and exposure pathway** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Stokes settling speed for dense nano spheres** isolates a single physical dependence, using **Sphere radius** as its variable. Substitute **71.25 nm** into its declared expression `(2/9)*1000*9.81*Math.pow(r*1e-9,2)/0.001*1e9` to obtain **11.0669063 nm/s**. For the second case use **132.5 nm**, obtaining **38.272625 nm/s**. The output rises between these two cases. The finite-difference slope is **0.444175 (nm/s)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Dilute spheres with density excess 1000 kg/m³ in waterlike fluid η=0.001 Pa s, low Reynolds number; neglect Brownian motion and aggregation. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A single dramatic microscopy view cannot certify bulk percolation. Rule-of-mixtures models may fail when interfaces dominate or the matrix microstructure changes during processing.

### Experimental characterization and controls

Conduct an **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. Follow with a **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **transformation, dissolution and assay interference**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **nanocomposites and multifunctional integration** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **batch repeatability, flow and exposure pathway** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **nanocomposites and multifunctional integration** depends on **fitness for intended use**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **11.0669063 nm/s** for the first stated input and **38.272625 nm/s** for the second. Determine the finite-difference sensitivity **0.444175 (nm/s)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **transformation, dissolution and assay interference** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **mass balance and independent validated endpoints**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_14 -->

## Lesson 8.2 — Biointerfaces, delivery and assay interference

### Physical mechanism and structural interpretation

Nanomaterial interaction with biological media depends on hydrodynamic size, surface charge, protein corona, dissolution and time-dependent agglomeration. Cellular uptake is not equivalent to therapeutic delivery, nor does fluorescence guarantee retained particle integrity. Assay interference can arise through light scattering, absorption, redox catalysis or binding of test dyes. Toxicity and intended function must be evaluated for the particular formulation, dose metric, route and exposed population.

**Core equation and domain.** Dose metrics may include administered mass/volume, particle number/volume, external area/volume or delivered mass/area; do not interchange them. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**biointerfaces, delivery and assay interference**—the most consequential distinction in this unit is **nominal synthesis size versus in-use transported form**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A nanoparticle formulation appears to improve cell viability in a colorimetric assay. Design controls for direct nanoparticle–reagent interaction and compare orthogonal biological endpoints.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Stokes–Einstein translational diffusivity** isolates a single physical dependence, using **Hydrodynamic radius** as its variable. Substitute **28.75 nm** into its declared expression `(1.380649e-23*298/(6*Math.PI*0.001*r*1e-9))*1e12` to obtain **7.59207648 µm²/s**. For the second case use **40.625 nm**, obtaining **5.37285413 µm²/s**. The output falls between these two cases. The finite-difference slope is **-0.186881883 (µm²/s)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Hydrodynamic sphere in Newtonian waterlike medium η=0.001 Pa s at 298 K, no slip and negligible interactions or confinement. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Nominal administered mass can differ from delivered cell-surface dose after settling and diffusion. This textbook does not validate biological safety or provide medical-use instructions.

### Experimental characterization and controls

Conduct an **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. Follow with a **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **transformation, dissolution and assay interference**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **biointerfaces, delivery and assay interference** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **batch repeatability, flow and exposure pathway** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **biointerfaces, delivery and assay interference** depends on **fitness for intended use**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **7.59207648 µm²/s** for the first stated input and **5.37285413 µm²/s** for the second. Determine the finite-difference sensitivity **-0.186881883 (µm²/s)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 8.3 — Environmental transport, release and transformation

### Physical mechanism and structural interpretation

Engineered nanomaterials can dissolve, aggregate, adsorb natural organic matter, settle, disperse or transform into new phases in air, soil and water. Release during manufacture, use, recycling and disposal is not equivalent to exposure. Particle surface coatings may age; dissolved ions can drive a response originally attributed to particles. Environmental mobility is controlled by hydrodynamics, particle interactions and the receiving medium rather than nominal primary size alone.

**Core equation and domain.** For small isolated spheres in viscous low-Re flow, v=(2/9)Δρ g r²/η; diffusion coefficient follows D=kBT/(6πηrH). This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**environmental transport, release and transformation**—the most consequential distinction in this unit is **nominal synthesis size versus in-use transported form**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Set up a conceptual fate model for a product that loses particles during washing. Track particle mass and dissolved species separately, and identify sampling biases for filters and detection instruments.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Stokes settling speed for dense nano spheres** isolates a single physical dependence, using **Sphere radius** as its variable. Substitute **193.75 nm** into its declared expression `(2/9)*1000*9.81*Math.pow(r*1e-9,2)/0.001*1e9` to obtain **81.8351563 nm/s**. For the second case use **255 nm**, obtaining **141.7545 nm/s**. The output rises between these two cases. The finite-difference slope is **0.978275 (nm/s)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Simple Stokes settling ignores aggregation, density gradients and turbulent flow; nanometre particles can have Brownian mixing competing with gravitational drift.

### Experimental characterization and controls

Conduct an **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. Follow with a **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **transformation, dissolution and assay interference**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **environmental transport, release and transformation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **batch repeatability, flow and exposure pathway** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **environmental transport, release and transformation** depends on **fitness for intended use**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **81.8351563 nm/s** for the first stated input and **141.7545 nm/s** for the second. Determine the finite-difference sensitivity **0.978275 (nm/s)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 8.4 — Reproducibility, reference materials and quality control

### Physical mechanism and structural interpretation

Trustworthy nanomaterial measurements require standardized terminology, appropriate reference materials, calibration, replicate synthesis batches and transparent data analysis. A method can be highly precise while biased by incomplete sampling. NIST particle standards can help instrument checks but are not substitute certified standards for every material and property. Traceability requires identifying measurand, environment, uncertainty budget and calibration chain. Statistical comparisons across batches must separate within-batch variation from run-to-run processing differences.

**Core equation and domain.** A combined standard uncertainty can be estimated by u_c²≈Σ(∂y/∂xi)²u_i² for independent inputs; covariance terms must be included when errors are correlated. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**reproducibility, reference materials and quality control**—the most consequential distinction in this unit is **nominal synthesis size versus in-use transported form**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Draft an acceptance plan for nominal 30 nm particles: primary core size by microscopy, colloidal size by DLS, chemistry by spectroscopy, agglomerate content and storage stability, each with method and target metric.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Stokes–Einstein translational diffusivity** isolates a single physical dependence, using **Hydrodynamic radius** as its variable. Substitute **52.5 nm** into its declared expression `(1.380649e-23*298/(6*Math.PI*0.001*r*1e-9))*1e12` to obtain **4.15756569 µm²/s**. For the second case use **64.375 nm**, obtaining **3.3906361 µm²/s**. The output falls between these two cases. The finite-difference slope is **-0.0645835448 (µm²/s)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A nominal diameter on a product sheet need not be its measured mean, median or upper tail in the operating medium. Avoid unwarranted precision and always state which certified reference material was used.

### Experimental characterization and controls

Conduct an **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. Follow with a **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **transformation, dissolution and assay interference**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **reproducibility, reference materials and quality control** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **batch repeatability, flow and exposure pathway** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **reproducibility, reference materials and quality control** depends on **fitness for intended use**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **4.15756569 µm²/s** for the first stated input and **3.3906361 µm²/s** for the second. Determine the finite-difference sensitivity **-0.0645835448 (µm²/s)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_15 -->

## Lesson 8.5 — Responsible scale-up, worker controls and lifecycle

### Physical mechanism and structural interpretation

Translating nanoparticles into a useful material requires cost, yield, variability, waste management, industrial hygiene and end-of-life considerations. Closed handling, containment and validated exposure measurement may matter more than headline particle diameter. Nanoparticles can be embedded in solid matrices or exist as airborne dry powders, producing very different exposure opportunities. Performance comparisons should include life cycle inventory, realistic failure modes, feedstock supply and repairability rather than extrapolating from a single laboratory demonstration.

**Core equation and domain.** Functional yield Y=N_pass/N_total and cost per acceptable unit C_accept≈C_total/N_pass are distinct from chemical mass yield; state the acceptance tests used. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**responsible scale-up, worker controls and lifecycle**—the most consequential distinction in this unit is **nominal synthesis size versus in-use transported form**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare a solvent-intensive colloid synthesis with a dry-film deposition route using batch yield, energy per delivered functional area, waste processing, repeatability and worker exposure pathways.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Stokes settling speed for dense nano spheres** isolates a single physical dependence, using **Sphere radius** as its variable. Substitute **316.25 nm** into its declared expression `(2/9)*1000*9.81*Math.pow(r*1e-9,2)/0.001*1e9` to obtain **218.030656 nm/s**. For the second case use **377.5 nm**, obtaining **310.663625 nm/s**. The output rises between these two cases. The finite-difference slope is **1.512375 (nm/s)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

This manuscript does not provide process safety thresholds, regulatory approvals or certified toxicology. Consult institution-specific safety professionals and current local rules; never treat a formula chart as a risk assessment.

### Experimental characterization and controls

Conduct an **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. Follow with a **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **transformation, dissolution and assay interference**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **responsible scale-up, worker controls and lifecycle** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **batch repeatability, flow and exposure pathway** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **responsible scale-up, worker controls and lifecycle** depends on **fitness for intended use**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **218.030656 nm/s** for the first stated input and **310.663625 nm/s** for the second. Determine the finite-difference sensitivity **1.512375 (nm/s)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Deciding whether a dispersed nanomaterial is ready for scale-up

### The decision to be made

A proof-of-concept material improves a laboratory measurement but exhibits size drift during storage and release under washing. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Compare ideal settling and Brownian diffusivity across realistic hydrodynamic size ranges, stating particle-density and viscosity assumptions. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Specify batch QC, discharge capture, chemical transformation studies, use-phase metrics and occupational controls. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Synthetic hydrodynamic models do not constitute a safety assessment or environmental fate forecast.

### Five end-of-unit questions

