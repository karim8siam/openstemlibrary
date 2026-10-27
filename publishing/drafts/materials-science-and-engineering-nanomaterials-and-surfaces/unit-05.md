# Unit 5: Adsorption, catalysis and surface chemistry

**Guiding question:** How does the density and chemical nature of accessible sites control adsorption and catalytic turnover?

## Introduction and measurement challenges

The density, chemical environment and accessibility of surface sites often matter more than total nominal particle area. Adsorption and reaction kinetics cannot be interpreted correctly without specifying competing species and actual exposure conditions.

Surface studies should compare fresh and aged specimens, account for any dissolved or homogeneous reactants, and distinguish instantaneous activity from long-term selectivity and deactivation. Normalization alone does not identify a mechanism.

These five lessons emphasize **adsorption and reaction kinetics**, and distinguish **site density versus apparent macroscopic rate**. To reproduce a study, specify **reactant coverage, surface aging and transport** before collecting data; otherwise **mass-transfer limitation or dissolved catalyst** may mimic the desired surface or nanoscale response. A proposed independent validation is **blank controls and independently measured accessible sites**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 5.1 — Surface adsorption and coverage definitions

### Physical mechanism and structural interpretation

Adsorption can arise from physisorption, chemisorption, ligand coordination, electrostatic interactions or solvent-mediated binding. Surface coverage is meaningful only after defining site density and which molecule occupies each site. An adsorption isotherm relates equilibrium composition to a surface occupancy, but measured solution depletion also reflects precipitation, vessel walls and interparticle partitioning. Surface functionalization can transform reaction selectivity without significantly changing total external area.

**Core equation and domain.** Ideal Langmuir occupancy θ=Kc/(1+Kc), derived by balancing adsorption and desorption at independent identical sites. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**surface adsorption and coverage definitions**—the most consequential distinction in this unit is **site density versus apparent macroscopic rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A dye adsorbs onto oxide nanoparticles. Measure solution blanks, vessel adsorption and dissolved species to ensure apparent uptake represents real particle binding.

Perform a thought experiment: assume the original explanation is wrong and **mass-transfer limitation or dissolved catalyst** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **reactant coverage, surface aging and transport** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Langmuir ideal site occupancy** isolates a single physical dependence, using **Adsorbate concentration** as its variable. Substitute **125.875 µmol/L** into its declared expression `100*(0.1*c)/(1+0.1*c)` to obtain **92.6402944 %**. For the second case use **250.75 µmol/L**, obtaining **96.1649089 %**. The output rises between these two cases. The finite-difference slope is **0.0282251414 (%)/(µmol/L)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Single-site independent adsorption, K=10^5 L/mol; c input µmol/L so Kc=0.1c; no interactions, competition or irreversible chemistry. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

A Langmuir fit can look convincing for heterogeneous surfaces over a narrow concentration span. Site non-equivalence, cooperativity and multilayer coverage violate its assumptions.

### Experimental characterization and controls

Conduct an **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. Follow with a **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **mass-transfer limitation or dissolved catalyst**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **surface adsorption and coverage definitions** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **reactant coverage, surface aging and transport** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **surface adsorption and coverage definitions** depends on **adsorption and reaction kinetics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **92.6402944 %** for the first stated input and **96.1649089 %** for the second. Determine the finite-difference sensitivity **0.0282251414 (%)/(µmol/L)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **mass-transfer limitation or dissolved catalyst** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **blank controls and independently measured accessible sites**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_8 -->

## Lesson 5.2 — Catalytic activity, selectivity and site normalization

### Physical mechanism and structural interpretation

The rate of a surface reaction can depend on reactant adsorption, desorption, bond activation and product inhibition. Mass-normalized rate, geometric-area-normalized rate and turnover frequency answer different questions. A nanoparticle with more exposed surface may produce more total output without having more active sites per square metre. Shape-selective catalysis requires consideration of facets, strain, defects and reconstruction under reactive conditions. Some highly active-looking tests actually operate in diffusion-limited regimes.

**Core equation and domain.** If r is molecules converted per second and Nsite the number of catalytic active sites, TOF=r/Nsite has units s⁻¹ subject to an explicit site definition. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**catalytic activity, selectivity and site normalization**—the most consequential distinction in this unit is **site density versus apparent macroscopic rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare two supported catalysts of equal metal mass but different measured exposed sites. Normalize rate by an independently estimated site population and perform blank support controls.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Surface-reaction Arrhenius temperature ratio** isolates a single physical dependence, using **Temperature** as its variable. Substitute **315 K** into its declared expression `Math.exp(-(45000/8.314462618)*(1/T-1/298))` to obtain **2.66490338 relative**. For the second case use **327.5 K**, obtaining **5.13438649 relative**. The output rises between these two cases. The finite-difference slope is **0.197558649 (relative)/(K)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Rate constant relative to 298 K; activation energy 45 kJ/mol fixed, neglects diffusion control, coverage changes and mechanism shifts. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Never report turnover frequency as established when site density is guessed from nominal particle area. Activation energies from apparent rates may mix surface and mass-transport phenomena.

### Experimental characterization and controls

Conduct an **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. Follow with a **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **mass-transfer limitation or dissolved catalyst**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **catalytic activity, selectivity and site normalization** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **reactant coverage, surface aging and transport** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **catalytic activity, selectivity and site normalization** depends on **adsorption and reaction kinetics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **2.66490338 relative** for the first stated input and **5.13438649 relative** for the second. Determine the finite-difference sensitivity **0.197558649 (relative)/(K)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 5.3 — Chemical functionalization, graft density and ligands

### Physical mechanism and structural interpretation

Surface grafts alter charge, wetting, biointeractions, colloidal stability and electronic coupling. Covalent silane chemistry, thiol monolayers and polymer brushes each have different substrate specificity and desorption pathways. Grafting density depends on geometric area and number of bound chains, but aggregation can bury portions of nominally exposed surface. Chemical proof requires distinguishing bound from unbound ligands and measuring whether a treatment damages the substrate.

**Core equation and domain.** A nominal grafting density σ=N_chain/A_accessible is not an occupancy fraction unless the footprint of each chain is defined. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**chemical functionalization, graft density and ligands**—the most consequential distinction in this unit is **site density versus apparent macroscopic rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Choose between a charged short ligand and a neutral polymer brush to stabilize particles in saline liquid. Specify ionic strength and how displacement of the original layer will be tested.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Langmuir ideal site occupancy** isolates a single physical dependence, using **Adsorbate concentration** as its variable. Substitute **375.625 µmol/L** into its declared expression `100*(0.1*c)/(1+0.1*c)` to obtain **97.4068071 %**. For the second case use **500.5 µmol/L**, obtaining **98.0411361 %**. The output rises between these two cases. The finite-difference slope is **0.00507971179 (%)/(µmol/L)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

XPS atomic fractions do not directly convert into molecules per nm² without attenuation, background and geometry models. Heating to remove ligands may induce sintering.

### Experimental characterization and controls

Conduct an **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. Follow with a **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **mass-transfer limitation or dissolved catalyst**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **chemical functionalization, graft density and ligands** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **reactant coverage, surface aging and transport** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **chemical functionalization, graft density and ligands** depends on **adsorption and reaction kinetics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **97.4068071 %** for the first stated input and **98.0411361 %** for the second. Determine the finite-difference sensitivity **0.00507971179 (%)/(µmol/L)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 5.4 — Thermally activated reactions and transport

### Physical mechanism and structural interpretation

At a fixed reaction mechanism, the Arrhenius equation describes the temperature sensitivity of a kinetic rate coefficient. The apparent activation energy of nanoparticle catalysis need not equal one elementary barrier because coverage, phase changes, diffusion and deactivation also vary with temperature. Temperature measured at a heater may differ from local catalyst temperature. Nanoparticle heating under illumination can arise from genuine photothermal effects, yet simultaneous photochemistry requires additional controls to isolate.

**Core equation and domain.** For constant Ea, k(T)/k(T0)=exp[−Ea/R(1/T−1/T0)], with kelvin temperatures and J/mol Ea. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**thermally activated reactions and transport**—the most consequential distinction in this unit is **site density versus apparent macroscopic rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

An observed reaction rate doubles after temperature increases. Compare rates at several controlled temperatures, independent thermometry and reactant diffusion measurements before fitting one activation energy.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Surface-reaction Arrhenius temperature ratio** isolates a single physical dependence, using **Temperature** as its variable. Substitute **340 K** into its declared expression `Math.exp(-(45000/8.314462618)*(1/T-1/298))` to obtain **9.42657545 relative**. For the second case use **352.5 K**, obtaining **16.5769826 relative**. The output rises between these two cases. The finite-difference slope is **0.572032573 (relative)/(K)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Do not infer a photochemical charge-transfer mechanism solely from a rate enhancement under light: optical heating, mass transport and reactive intermediates can reproduce trends.

### Experimental characterization and controls

Conduct an **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. Follow with a **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **mass-transfer limitation or dissolved catalyst**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **thermally activated reactions and transport** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **reactant coverage, surface aging and transport** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **thermally activated reactions and transport** depends on **adsorption and reaction kinetics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **9.42657545 relative** for the first stated input and **16.5769826 relative** for the second. Determine the finite-difference sensitivity **0.572032573 (relative)/(K)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_9 -->

## Lesson 5.5 — Deactivation, poisoning and structure-sensitive reactivity

### Physical mechanism and structural interpretation

Supported metal nanocatalysts can lose activity from sintering, dissolution, surface poisoning, ligand rearrangement, oxidation or coke deposition. Distinguishing them requires post-reaction morphology, chemical composition and in-situ or operando measurements when feasible. Recovery of activity after cleaning can implicate reversible blocking, but it is not proof that the primary mechanism remained unchanged. A claim of chemical stability must include the expected number of operating cycles and leaching limits.

**Core equation and domain.** A simple first-order deactivation approximation a(t)=exp(−kd t) is useful for describing trends but cannot identify the microscopic cause of kd. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**deactivation, poisoning and structure-sensitive reactivity**—the most consequential distinction in this unit is **site density versus apparent macroscopic rate**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

A catalyst deactivates after ten runs. Ask whether its mass, exposed area, oxidation state or support structure changed and whether dissolved metal could have become a homogeneous catalyst.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Langmuir ideal site occupancy** isolates a single physical dependence, using **Adsorbate concentration** as its variable. Substitute **625.375 µmol/L** into its declared expression `100*(0.1*c)/(1+0.1*c)` to obtain **98.4261263 %**. For the second case use **750.25 µmol/L**, obtaining **98.6846432 %**. The output rises between these two cases. The finite-difference slope is **0.00207020545 (%)/(µmol/L)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Ex-situ imaging after cooling may miss transient active phases. Rate comparisons must normalize feed, recovery, mass balance and sample history.

### Experimental characterization and controls

Conduct an **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. Follow with a **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **mass-transfer limitation or dissolved catalyst**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **deactivation, poisoning and structure-sensitive reactivity** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **reactant coverage, surface aging and transport** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **deactivation, poisoning and structure-sensitive reactivity** depends on **adsorption and reaction kinetics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **98.4261263 %** for the first stated input and **98.6846432 %** for the second. Determine the finite-difference sensitivity **0.00207020545 (%)/(µmol/L)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Testing a functionalized nanoparticle catalyst

### The decision to be made

Ligand-treated catalyst particles appear more active, although measured mass and total area change little. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Calculate ideal adsorption occupancy and a separate Arrhenius temperature sensitivity; consider site blocking and transport. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Design selectivity, leaching, blank-substrate and turnover-frequency-normalized tests over repeated cycles. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Isotherm fit plus Arrhenius trend does not prove a unique catalytic mechanism.

### Five end-of-unit questions

