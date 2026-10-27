# Unit 2: Thermodynamics, interfaces and colloidal stability

**Guiding question:** How do surface energies and solvent-mediated forces alter the free energy of nanoscale particles?

## Introduction and measurement challenges

At nanometre dimensions, interfacial terms can compete with volume terms in free energy. That explains many finite-size shifts but does not license transferring one interfacial-energy constant across different crystal facets, electrolytes or adsorbed species.

Stability is dynamic and environmentally contingent. During aging, dissolution, ripening, aggregation and chemical conversion can occur simultaneously. Study pH, ionic strength, surface ligands and solvent composition as independent, logged variables.

These five lessons emphasize **interfacial thermodynamics**, and distinguish **bulk chemical potential versus interfacial contribution**. To reproduce a study, specify **ionic strength, adsorbates and sample aging** before collecting data; otherwise **uncontrolled ligand desorption or precipitation** may mimic the desired surface or nanoscale response. A proposed independent validation is **time-resolved size distributions with orthogonal solution chemistry**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 2.1 — Surface free energy and capillarity

### Physical mechanism and structural interpretation

Creating new interface costs a free-energy contribution γA, where γ is an interfacial free energy rather than a universal surface tension for all solids. Small particles carry a larger surface contribution relative to their bulk volume. Crystal anisotropy creates different γ values for different facets; equilibrium shapes can be understood by minimizing total interfacial free energy subject to fixed volume. Adsorbates, oxidation and solvent chemistry change surface free energies and sometimes reverse facet preferences. Distinguish solid-vapor from solid-liquid quantities.

**Core equation and domain.** The capillarity approximation F≈Vf_bulk+ΣγiAi describes a specified configuration; varying the shape changes its area contributions. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**surface free energy and capillarity**—the most consequential distinction in this unit is **bulk chemical potential versus interfacial contribution**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare a faceted nanoparticle under clean vacuum with the same composition in water containing binding ligands. Ask which interface contributes to the total free energy and why a spherical shape is not guaranteed.

Perform a thought experiment: assume the original explanation is wrong and **uncontrolled ligand desorption or precipitation** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **ionic strength, adsorbates and sample aging** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Gibbs–Thomson spherical melting estimate** isolates a single physical dependence, using **Particle radius** as its variable. Substitute **8 nm** into its declared expression `1200*(1-0.25/r)` to obtain **1162.5 K**. For the second case use **14 nm**, obtaining **1178.57143 K**. The output rises between these two cases. The finite-difference slope is **2.67857143 (K)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Illustrative isotropic spherical particle; Tbulk=1200 K, interfacial-energy and latent-heat constants chosen to give ℓ=0.25 nm; excludes shape, chemistry and premelting. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Applying isotropic spherical formulas to reconstructed faceted nanoparticles can invert qualitative predictions. Interface energy is a property of a specified interface and thermodynamic state, not a scalar label for an element.

### Experimental characterization and controls

Conduct an **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. Follow with a **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **uncontrolled ligand desorption or precipitation**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **surface free energy and capillarity** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **ionic strength, adsorbates and sample aging** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **surface free energy and capillarity** depends on **interfacial thermodynamics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1162.5 K** for the first stated input and **1178.57143 K** for the second. Determine the finite-difference sensitivity **2.67857143 (K)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **uncontrolled ligand desorption or precipitation** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **time-resolved size distributions with orthogonal solution chemistry**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_2 -->

## Lesson 2.2 — Curvature-dependent phase stability and melting

### Physical mechanism and structural interpretation

Curved interfaces shift chemical potential relative to a flat interface. Gibbs–Thomson reasoning predicts changes in vapor pressure, equilibrium solubility, melting or growth under specified geometry and material constants. A small particle often exhibits melting-point depression compared with a bulk sample, but actual trends depend on shape, premelting, substrate support and interfacial energies. Empirical nanoscale melting behavior cannot be certified by one bulk-property formula. Temperature-dependent latent heat and different solid/liquid surface energies matter near transitions.

**Core equation and domain.** A pedagogic form is Tm(r)=Tm,∞(1−ℓ/r), where ℓ collects thermodynamic and interfacial parameters and is neither universal nor independent of particle chemistry. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**curvature-dependent phase stability and melting**—the most consequential distinction in this unit is **bulk chemical potential versus interfacial contribution**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare two idealized metallic spheres of different radii with a hypothetical particle supported on a substrate. Outline a differential scanning calorimetry study and clarify whether the measured feature is melting or another transformation.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Debye length in monovalent aqueous electrolyte** isolates a single physical dependence, using **Ionic strength** as its variable. Substitute **0.02575 mol/L** into its declared expression `0.304/Math.sqrt(I)` to obtain **1.89445794 nm**. For the second case use **0.038125 mol/L**, obtaining **1.55692846 nm**. The output falls between these two cases. The finite-difference slope is **-27.2751092 (nm)/(mol/L)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Approximate 298 K aqueous 1:1-electrolyte Debye length; continuum electrostatics, dilute solution and constant dielectric. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Classical capillarity becomes unreliable near molecular dimensions; the small-particle limit also violates the assumption of a bulk-like solid core. Do not extrapolate a formula until it predicts negative temperature.

### Experimental characterization and controls

Conduct an **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. Follow with a **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **uncontrolled ligand desorption or precipitation**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **curvature-dependent phase stability and melting** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **ionic strength, adsorbates and sample aging** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **curvature-dependent phase stability and melting** depends on **interfacial thermodynamics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.89445794 nm** for the first stated input and **1.55692846 nm** for the second. Determine the finite-difference sensitivity **-27.2751092 (nm)/(mol/L)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 2.3 — Electrostatic double layers and Debye length

### Physical mechanism and structural interpretation

Charged particles in electrolyte accumulate compensating ionic charge and perturb the surrounding potential. The Debye screening length decreases as ionic strength grows for a dilute electrolyte at fixed dielectric constant and temperature. Surface charge regulation means the potential itself may change when pH or salt changes. A shorter Debye length does not by itself establish aggregation, because van der Waals attraction, hydration, polymeric steric barriers and surface roughness also influence particle interactions.

**Core equation and domain.** For water near 298 K with a dilute monovalent electrolyte, λD≈0.304/sqrt(I[M]) nm; ionic strength I=0.5Σci zi² uses molar ion concentrations. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**electrostatic double layers and debye length**—the most consequential distinction in this unit is **bulk chemical potential versus interfacial contribution**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Design a salt-titration study on a colloid with measured electrophoretic mobility, particle size and visual precipitation. Distinguish shifts in screening from changes in ligand desorption or ionic bridging.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Gibbs–Thomson spherical melting estimate** isolates a single physical dependence, using **Particle radius** as its variable. Substitute **20 nm** into its declared expression `1200*(1-0.25/r)` to obtain **1185 K**. For the second case use **26 nm**, obtaining **1188.46154 K**. The output rises between these two cases. The finite-difference slope is **0.576923077 (K)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

The simple aqueous formula is approximate, generally unsuitable for concentrated electrolytes, multivalent correlations, nonaqueous solvents and highly charged non-linear electrostatic regimes.

### Experimental characterization and controls

Conduct an **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. Follow with a **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **uncontrolled ligand desorption or precipitation**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **electrostatic double layers and debye length** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **ionic strength, adsorbates and sample aging** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **electrostatic double layers and debye length** depends on **interfacial thermodynamics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1185 K** for the first stated input and **1188.46154 K** for the second. Determine the finite-difference sensitivity **0.576923077 (K)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 2.4 — Attraction, steric repulsion and aggregation

### Physical mechanism and structural interpretation

A colloidal particle pair experiences a competition between dispersion attraction, electrostatic forces, steric-layer overlap and possible solvent-structuring effects. Classical DLVO theory is a useful starting point for combinations of van der Waals attraction and double-layer repulsion, but it is not a complete description for brush-coated, biomolecular or strongly ionic surfaces. Aggregation rates reflect encounter frequency and energy barriers; irreversible sintering is different from weak reversible flocculation.

**Core equation and domain.** A schematic pair potential may be written U_total(h)=U_dispersion(h)+U_double_layer(h)+U_steric(h)+..., with separation h and explicitly selected boundary conditions. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**attraction, steric repulsion and aggregation**—the most consequential distinction in this unit is **bulk chemical potential versus interfacial contribution**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Two samples exhibit identical hydrodynamic diameters initially but diverge after pH adjustment. Require measurements of time-dependent cluster growth, electrophoretic mobility, composition and soluble contaminant concentration.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Debye length in monovalent aqueous electrolyte** isolates a single physical dependence, using **Ionic strength** as its variable. Substitute **0.0505 mol/L** into its declared expression `0.304/Math.sqrt(I)` to obtain **1.35278224 nm**. For the second case use **0.062875 mol/L**, obtaining **1.21236833 nm**. The output falls between these two cases. The finite-difference slope is **-11.3465786 (nm)/(mol/L)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Zeta potential is not identical to solid surface potential and a large magnitude is not a guarantee of long-term dispersion stability. Centrifugation, drying and dilution can alter the sampled population.

### Experimental characterization and controls

Conduct an **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. Follow with a **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **uncontrolled ligand desorption or precipitation**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **attraction, steric repulsion and aggregation** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **ionic strength, adsorbates and sample aging** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **attraction, steric repulsion and aggregation** depends on **interfacial thermodynamics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1.35278224 nm** for the first stated input and **1.21236833 nm** for the second. Determine the finite-difference sensitivity **-11.3465786 (nm)/(mol/L)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_3 -->

## Lesson 2.5 — Dissolution, Ostwald ripening and chemical environment

### Physical mechanism and structural interpretation

Small crystallites may dissolve into a surrounding solution and feed larger crystals, an evolution commonly called Ostwald ripening. Interfacial curvature creates a chemical-potential difference that can favor mass transfer. Diffusion-controlled and interface-reaction-controlled models predict different kinetic exponents; real systems also undergo aggregation, coalescence and ligand exchange. A particle-size increase during aging alone does not identify ripening. Solution saturation, pH and complexation can shift the process.

**Core equation and domain.** A simplified curvature solubility relation is c(r)/c∞=exp[2γVm/(rRT)], valid when the capillarity and dilute-solution assumptions hold. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**dissolution, ostwald ripening and chemical environment**—the most consequential distinction in this unit is **bulk chemical potential versus interfacial contribution**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Observe particle distributions and dissolved-species concentration at multiple aging times. A decreasing number of small particles with evidence of dissolved intermediates supports ripening more strongly than an increasing average diameter alone.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Gibbs–Thomson spherical melting estimate** isolates a single physical dependence, using **Particle radius** as its variable. Substitute **32 nm** into its declared expression `1200*(1-0.25/r)` to obtain **1190.625 K**. For the second case use **38 nm**, obtaining **1192.10526 K**. The output rises between these two cases. The finite-difference slope is **0.246710526 (K)/(nm)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Classical Lifshitz–Slyozov–Wagner scaling uses strong assumptions of dilute dispersion, approximately spherical particles and diffusion-controlled ripening; it must not be imposed on dense agglomerated batches.

### Experimental characterization and controls

A viable first study begins with **in-situ time-resolved imaging and carefully staged aliquots**, recording **elapsed reaction time, quench method and distribution widths**. Verify the interpretation using **an independent reaction-conversion or dissolved-species assay**. Distinct techniques do not automatically provide independent evidence if they share the same mislabeled sample state or calibration, so build an uncertainty map linking each instrument to the inferred result. In reporting size, specify whether it means geometric diameter, coherent domain, hydrodynamic radius or an equivalent-sphere inference. Record solvent, drying, handling, storage, atmosphere and the time allowed for the material to equilibrate.

Conduct an **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. Follow with a **surface aging and transformation audit**: Measure or monitor oxidation, ligand change, dissolution, humidity and morphology during handling and storage. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **uncontrolled ligand desorption or precipitation**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **dissolution, ostwald ripening and chemical environment** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **ionic strength, adsorbates and sample aging** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **dissolution, ostwald ripening and chemical environment** depends on **interfacial thermodynamics**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **1190.625 K** for the first stated input and **1192.10526 K** for the second. Determine the finite-difference sensitivity **0.246710526 (K)/(nm)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Diagnosing instability in a charged nanoparticle suspension

### The decision to be made

A dispersion remains stable in low-salt water but aggregates after an electrolyte change. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Compare screening length and a size-dependent capillarity estimate only within separate declared physics; do not combine them as an ad hoc force law. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Specify pH, electrophoretic mobility, time-resolved hydrodynamic distributions and ligand integrity measurements. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** A shorter screening length is not sufficient evidence for DLVO-controlled aggregation.

### Five end-of-unit questions

