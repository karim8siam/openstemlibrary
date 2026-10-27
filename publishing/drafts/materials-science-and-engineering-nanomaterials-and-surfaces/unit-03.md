# Unit 3: Nanomaterial synthesis, growth and processing

**Guiding question:** How can nucleation, growth, ligand chemistry and processing history be controlled separately?

## Introduction and measurement challenges

Nanomaterial synthesis is a coupled sequence of precursor activation, nuclei formation, transport-limited growth, passivation and workup. A nominal setpoint temperature is not necessarily the temperature or composition at active growth sites.

Process reproducibility needs time-resolved evidence and mass balances. Compare at least two independently synthesized batches, quantify tail populations and report purification losses rather than only displaying the most visually attractive micrographs.

These five lessons emphasize **nucleation and growth pathways**, and distinguish **nucleation rate versus subsequent growth rate**. To reproduce a study, specify **precursor conversion, temperature and mixing** before collecting data; otherwise **secondary nucleation or purification selection** may mimic the desired surface or nanoscale response. A proposed independent validation is **independent conversion kinetics and distribution tracking**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 3.1 — Nucleation kinetics and critical nuclei

### Physical mechanism and structural interpretation

Nucleation requires balancing a bulk free-energy driving term against the energetic cost of creating an interface. In the simplest homogeneous spherical model, a critical radius separates growing from shrinking clusters and a free-energy barrier controls the thermally activated nucleation rate. Heterogeneous nucleation at defects or vessel walls reduces the barrier by a geometry-dependent factor, while burst nucleation may narrow some distributions only when subsequent growth can be controlled. Supersaturation and reaction pathway are more informative than a recipe temperature alone.

**Core equation and domain.** For isotropic homogeneous spherical nuclei, r*=2γ/|Δgv| and ΔG*=16πγ³/(3Δgv²), where Δgv is volumetric driving free energy. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**nucleation kinetics and critical nuclei**—the most consequential distinction in this unit is **nucleation rate versus subsequent growth rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare rapid precursor activation with gradual monomer generation while measuring precursor conversion and size distributions over time. Identify whether a delayed onset indicates nucleation or instrument detection threshold.

Perform a thought experiment: assume the original explanation is wrong and **secondary nucleation or purification selection** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **precursor conversion, temperature and mixing** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Classical homogeneous nucleation barrier** isolates a single physical dependence, using **Driving free energy density** as its variable. Substitute **0.95 10^8 J/m³** into its declared expression `(16*Math.PI*Math.pow(0.1,3)/(3*Math.pow(g*1e8,2)))/(1.380649e-23*298)` to obtain **451.234029 kBT**. For the second case use **1.1 10^8 J/m³**, obtaining **336.560918 kBT**. The output falls between these two cases. The finite-difference slope is **-764.487404 (kBT)/(10^8 J/m³)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Homogeneous spherical nucleus with isotropic interfacial energy γ=0.1 J/m² at 298 K; assumes capillarity and continuum free energy. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

The classical nucleus is treated as if it possessed macroscopic surface tension; this may fail for clusters of only a few atoms. A nucleation barrier does not predict the distribution without kinetics and mass balance.

### Experimental characterization and controls

Conduct an **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. Follow with a **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **secondary nucleation or purification selection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **nucleation kinetics and critical nuclei** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **precursor conversion, temperature and mixing** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **nucleation kinetics and critical nuclei** depends on **nucleation and growth pathways**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **451.234029 kBT** for the first stated input and **336.560918 kBT** for the second. Determine the finite-difference sensitivity **-764.487404 (kBT)/(10^8 J/m³)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **secondary nucleation or purification selection** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **independent conversion kinetics and distribution tracking**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_4 -->

## Lesson 3.2 — Growth, diffusion and reaction limitation

### Physical mechanism and structural interpretation

After nucleation, growth can be limited by delivery of growth species, surface incorporation, chemical conversion or removal of byproducts. Diffusion-limited regimes often produce concentration gradients, whereas surface-reaction-limited growth can be sensitive to binding sites and facet chemistry. Distinguishing them requires kinetics under controlled stirring, concentration, temperature and specimen geometry. Faster growth is not always more uniform growth: heterogeneous fluxes produce broad size and shape distributions.

**Core equation and domain.** A diffusion field obeys ∂c/∂t=D∇²c under constant diffusivity without reaction; an interfacial incorporation law supplies the missing boundary condition. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**growth, diffusion and reaction limitation**—the most consequential distinction in this unit is **nucleation rate versus subsequent growth rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A nanowire batch lengthens when feed concentration increases but diameter stays nearly fixed. Test whether axial catalyst-mediated addition, sidewall passivation or time-dependent nucleation can explain the result.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **One-dimensional diffusion distance** isolates a single physical dependence, using **Diffusion time** as its variable. Substitute **907.5 s** into its declared expression `Math.sqrt(2*1e-18*t)*1e9` to obtain **42.6028168 nm**. For the second case use **1356.25 s**, obtaining **52.0816666 nm**. The output rises between these two cases. The finite-difference slope is **0.0211227851 (nm)/(s)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** One-dimensional diffusion displacement RMS sqrt(2Dt), D=10⁻¹⁸ m²/s constant, no trapping or advection. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Transport relations drawn from dilute solution can fail in viscous melts, gels or porous templates. Fitting a square-root growth law does not establish diffusion control unless independent trends support it.

### Experimental characterization and controls

Conduct an **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. Follow with a **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **secondary nucleation or purification selection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **growth, diffusion and reaction limitation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **precursor conversion, temperature and mixing** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **growth, diffusion and reaction limitation** depends on **nucleation and growth pathways**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **42.6028168 nm** for the first stated input and **52.0816666 nm** for the second. Determine the finite-difference sensitivity **0.0211227851 (nm)/(s)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 3.3 — Solution-phase nanoparticles and ligand control

### Physical mechanism and structural interpretation

Colloidal synthesis mixes precursor chemistry, solvent coordination, reductants, surfactants, surface ligands and thermal history. Ligands can slow selected facets and modify solubility, but nominal ligand concentration does not necessarily equal surface coverage. A high particle yield may coexist with unstable storage or difficult purification. Trace ionic impurities can dominate aggregation. The product should be defined by composition, crystal phase, size distribution, surface chemistry and residual free reagent, not by a photograph of colored liquid.

**Core equation and domain.** Surface occupancy is roughly Γ=N_bound/A, where the relevant accessible surface area and species-specific binding stoichiometry must be declared. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**solution-phase nanoparticles and ligand control**—the most consequential distinction in this unit is **nucleation rate versus subsequent growth rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Propose comparative characterization of an as-synthesized colloid and a purified fraction, recording elemental composition, particle core size, solution-phase free ligand and hydrodynamic behavior.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Classical homogeneous nucleation barrier** isolates a single physical dependence, using **Driving free energy density** as its variable. Substitute **1.25 10^8 J/m³** into its declared expression `(16*Math.PI*Math.pow(0.1,3)/(3*Math.pow(g*1e8,2)))/(1.380649e-23*298)` to obtain **260.632775 kBT**. For the second case use **1.4 10^8 J/m³**, obtaining **207.774852 kBT**. The output falls between these two cases. The finite-difference slope is **-352.38615 (kBT)/(10^8 J/m³)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Ligand exchange can etch, aggregate, oxidize or selectively lose particles. Optical absorbance alone cannot establish identical concentration and size between samples without calibrated extinction and baseline checks.

### Experimental characterization and controls

Conduct an **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. Follow with a **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **secondary nucleation or purification selection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **solution-phase nanoparticles and ligand control** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **precursor conversion, temperature and mixing** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **solution-phase nanoparticles and ligand control** depends on **nucleation and growth pathways**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **260.632775 kBT** for the first stated input and **207.774852 kBT** for the second. Determine the finite-difference sensitivity **-352.38615 (kBT)/(10^8 J/m³)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 3.4 — Physical vapor deposition and nanoscale films

### Physical mechanism and structural interpretation

Sputtering, evaporation and atomic layer deposition create films with different energetic-particle fluxes, nucleation densities and surface reaction histories. Nominal film thickness does not imply conformality in pores or complete coverage before islands coalesce. ALD can be self-limiting in favorable reaction windows, but precursor saturation and steric accessibility constrain it. Film stress, texture and defects can be as important to performance as thickness. Sidewall geometry changes the effective dose and local growth rate.

**Core equation and domain.** If ideal cycle growth is g nm/cycle, target thickness t≈Ng for N saturated cycles; incubation and depletion can make this linear estimate inaccurate. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**physical vapor deposition and nanoscale films**—the most consequential distinction in this unit is **nucleation rate versus subsequent growth rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A wafer has uniform thickness on flat test pads but a porous substrate shows little penetration. Compare planar ellipsometry, cross-sectional imaging and composition-depth profiling before calling the growth conformal.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **One-dimensional diffusion distance** isolates a single physical dependence, using **Diffusion time** as its variable. Substitute **1805 s** into its declared expression `Math.sqrt(2*1e-18*t)*1e9` to obtain **60.0832755 nm**. For the second case use **2253.75 s**, obtaining **67.1379178 nm**. The output rises between these two cases. The finite-difference slope is **0.0157206512 (nm)/(s)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A quartz-crystal microbalance estimates deposited mass under calibration assumptions; it is not a direct count of atomic layers on arbitrary surfaces. Re-entrant pores and high aspect ratios impose transport limitations.

### Experimental characterization and controls

Conduct an **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. Follow with a **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **secondary nucleation or purification selection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **physical vapor deposition and nanoscale films** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **precursor conversion, temperature and mixing** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **physical vapor deposition and nanoscale films** depends on **nucleation and growth pathways**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **60.0832755 nm** for the first stated input and **67.1379178 nm** for the second. Determine the finite-difference sensitivity **0.0157206512 (nm)/(s)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_5 -->

## Lesson 3.5 — Templates, self-assembly and post-processing

### Physical mechanism and structural interpretation

Self-assembly can order building blocks using intermolecular forces, capillary drying, magnetic interactions, polymer segregation or template confinement. The desired length scale is often fixed by particle size or block-copolymer dimensions; placement accuracy, defects and registration to macroscopic features require separate assessment. Thermal annealing changes grain size and interfaces but also can remove surface ligands or induce coarsening. Nanoimprint and lithographic patterning trade resolution for throughput, mask complexity and defect tolerance.

**Core equation and domain.** For an ideal 2D hexagonal lattice of nearest-neighbour spacing a, the primitive-cell area is A_cell=(sqrt(3)/2)a²; defects invalidate perfect-lattice density predictions. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**templates, self-assembly and post-processing**—the most consequential distinction in this unit is **nucleation rate versus subsequent growth rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Analyze a hexagonally packed particle monolayer with edge dislocations and cracks. What combination of electron microscopy, scattering and large-area optical mapping reveals both local order and production yield?

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Classical homogeneous nucleation barrier** isolates a single physical dependence, using **Driving free energy density** as its variable. Substitute **1.55 10^8 J/m³** into its declared expression `(16*Math.PI*Math.pow(0.1,3)/(3*Math.pow(g*1e8,2)))/(1.380649e-23*298)` to obtain **169.506227 kBT**. For the second case use **1.7 10^8 J/m³**, obtaining **140.913049 kBT**. The output falls between these two cases. The finite-difference slope is **-190.62119 (kBT)/(10^8 J/m³)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

High-resolution images of a selected microscopic domain cannot establish wafer-scale periodicity. Cracks from drying and particle redistribution during imaging can create structures absent from the operating state.

### Experimental characterization and controls

A viable first study begins with **controlled spectroscopy and spectrally calibrated detectors**, recording **source bandwidth, integration time and background traces**. Verify the interpretation using **size-distribution and chemical-state measurements independent of light emission**. Distinct techniques do not automatically provide independent evidence if they share the same mislabeled sample state or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting size, specify whether it means geometric diameter, coherent domain, hydrodynamic radius or an equivalent-sphere inference. Record solvent, drying, handling, storage, atmosphere and the time allowed for the material to equilibrate.

Conduct an **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. Follow with a **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **secondary nucleation or purification selection**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **templates, self-assembly and post-processing** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **precursor conversion, temperature and mixing** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **templates, self-assembly and post-processing** depends on **nucleation and growth pathways**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **169.506227 kBT** for the first stated input and **140.913049 kBT** for the second. Determine the finite-difference sensitivity **-190.62119 (kBT)/(10^8 J/m³)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Separating particle nucleation from subsequent growth

### The decision to be made

An experimental team reports a striking reduction in average particle size following a change in precursor timing. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Estimate how nucleation driving energy affects an ideal classical barrier; separately calculate diffusion displacement during the growth stage. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure conversion, number concentration and time-resolved particle distributions using independent synthesis batches. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Model barriers and diffusion length do not uniquely determine actual synthesis yield or dispersity.

### Five end-of-unit questions

