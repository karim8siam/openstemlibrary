# Unit 7: Nanostructured surfaces, wettability and coatings

**Guiding question:** How do chemistry, roughness, topography and interfaces jointly determine adhesion, wetting and coating behavior?

## Introduction and measurement challenges

Practical surface function combines molecular chemistry with multiscale topography, substrate mechanics and operating conditions. Wetting, adhesion, friction and barrier properties rarely follow from a single measurement such as static contact angle.

A convincing functional-surface claim includes state history, working fluid, temperature, surface aging and mechanically realistic wear tests. Distinguish a pristine laboratory demonstration from a durable manufactured product.

These five lessons emphasize **surface chemistry and morphology**, and distinguish **equilibrium wetting versus hysteretic metastable state**. To reproduce a study, specify **roughness, chemical history and environmental cycling** before collecting data; otherwise **surface contamination or trapped air pockets** may mimic the desired surface or nanoscale response. A proposed independent validation is **advancing/receding angles plus morphology and durability tests**. In a laboratory notebook, record whether a number is an assumed parameter, instrument measurement, derived material property or model fit. The same symbol might refer to bulk and device-level quantities, so include precise subscripts or captions.

## Prerequisite review and learning protocol

## Lesson 7.1 — Young contact angle and surface energies

### Physical mechanism and structural interpretation

A liquid droplet on an ideal smooth chemically homogeneous solid meets a three-phase line where interfacial free energies balance. The equilibrium Young angle helps connect wetting with solid-vapor, solid-liquid and liquid-vapor interfacial tensions. Real surfaces are rough, contaminated, viscoelastic or chemically heterogeneous, leading to advancing and receding contact angles rather than one unique angle. A static image of a drop is a measurement under a particular history, not necessarily an equilibrium material constant.

**Core equation and domain.** For ideal flat equilibrium wetting, γSV−γSL=γLV cosθ, with every interfacial energy in the same units. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**young contact angle and surface energies**—the most consequential distinction in this unit is **equilibrium wetting versus hysteretic metastable state**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare a freshly cleaned oxide to a hydrocarbon-contaminated replicate. Measure advancing and receding angles and record droplet age, humidity and substrate cleaning history.

Perform a thought experiment: assume the original explanation is wrong and **surface contamination or trapped air pockets** controls the measured trend. Sketch the alternative particle and interface state, locate which geometrical, transport or chemical pathway would change, and predict which observable would differ when you adjust **roughness, chemical history and environmental cycling** independently. A theory that explains a measured size-property trend only after its parameters are selected to fit the same observations is not yet a validated mechanism. An independent measurement should reduce freedom in the model, not merely add another unconstrained fitted constant.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Young equilibrium contact angle** isolates a single physical dependence, using **Surface-energy difference γSV−γSL** as its variable. Substitute **-22.5 mN/m** into its declared expression `Math.acos(dg/72)*180/Math.PI` to obtain **108.209957 degrees**. For the second case use **-15 mN/m**, obtaining **102.024699 degrees**. The output falls between these two cases. The finite-difference slope is **-0.824701024 (degrees)/(mN/m)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Smooth rigid chemically homogeneous planar solid, γLV=72 mN/m; ideal equilibrium under ambient conditions, ignores hysteresis. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Young equation cannot be used to infer both unknown solid interfacial energies from one water angle. Wicking and reaction with the solid complicate steady measurements.

### Experimental characterization and controls

Conduct an **replicate and uncertainty separation audit**: Distinguish repeated scans, different specimen preparations and independent synthesis runs in uncertainty estimates. Follow with a **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface contamination or trapped air pockets**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **young contact angle and surface energies** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **roughness, chemical history and environmental cycling** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **young contact angle and surface energies** depends on **surface chemistry and morphology**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **108.209957 degrees** for the first stated input and **102.024699 degrees** for the second. Determine the finite-difference sensitivity **-0.824701024 (degrees)/(mN/m)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

**C. Independent experimental design.** Design a controlled test that separates **surface contamination or trapped air pockets** from an intrinsic material mechanism. Include geometry, composition, medium, concentration, calibration, independent replicate batches and rejection criteria. *Solution guidance:* prioritize **advancing/receding angles plus morphology and durability tests**, describe a blank/reference sample, and give the outcome that would rule out your initial interpretation.

<!-- MODEL_12 -->

## Lesson 7.2 — Wenzel roughness and Cassie states

### Physical mechanism and structural interpretation

Roughness amplifies intrinsic wetting tendencies in the ideal Wenzel state where liquid fills surface texture. In a Cassie–Baxter state, droplets may sit across composite solid-air interfaces. Transitions depend on texture, pressure, defects and vibration. High contact angle does not necessarily mean low contact-angle hysteresis; droplet roll-off needs separate measurement. Superhydrophobic behavior is a coupled chemistry-topography phenomenon and can degrade after abrasion.

**Core equation and domain.** Wenzel cosθ*=r cosθY with true-to-projected area ratio r≥1; Cassie states require area-fraction terms and distinct geometry assumptions. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**wenzel roughness and cassie states**—the most consequential distinction in this unit is **equilibrium wetting versus hysteretic metastable state**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Analyze two rough textures that give the same static contact angle but different roll-off angles. Propose a pressure perturbation test for trapped air and a microscopic wetting-state inspection.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Wenzel apparent angle for an ideal rough surface** isolates a single physical dependence, using **True-to-projected surface-area ratio** as its variable. Substitute **1.375 dimensionless** into its declared expression `Math.acos(r*Math.cos(110*Math.PI/180))*180/Math.PI` to obtain **118.052324 degrees**. For the second case use **1.5625 dimensionless**, obtaining **122.303669 degrees**. The output rises between these two cases. The finite-difference slope is **22.6738396 (degrees)/(dimensionless)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

**Assumptions used for this calculation:** Chemically homogeneous fully wetted rough solid with intrinsic Young angle 110°, Wenzel cosθ*=r cosθ; no trapped air or metastable pinning. A good numerical agreement between two software implementations means only that the same chosen mathematical function has been evaluated consistently. It does not measure the properties of an actual specimen, identify its microscopic mechanism or validate a production design. Report synthetic values with explicit uncertainty status; do not attach fabricated experimental error bars. A smooth curve can still be physically inappropriate if the underlying approximations fail beyond their stated region.

### Scope, counterexamples and physical failure modes

Wenzel relation fails for partial air trapping, nonuniform chemistry and metastable pinned contact lines. The equation can predict a formal cosine outside [−1,1] if forced beyond its proper regime.

### Experimental characterization and controls

Conduct an **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. Follow with a **kinetic identifiability audit**: Determine whether two mechanisms produce indistinguishable trends within the tested time or concentration range. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface contamination or trapped air pockets**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **wenzel roughness and cassie states** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **roughness, chemical history and environmental cycling** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **wenzel roughness and cassie states** depends on **surface chemistry and morphology**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **118.052324 degrees** for the first stated input and **122.303669 degrees** for the second. Determine the finite-difference sensitivity **22.6738396 (degrees)/(dimensionless)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 7.3 — Thin-film adhesion, interfaces and residual stress

### Physical mechanism and structural interpretation

Nanometre-scale coatings may fail through decohesion, microcracking, thermal mismatch or interfacial chemical degradation. Film stress can be tensile or compressive depending on nucleation, growth energetics and thermal history. Adhesion cannot be established by surface roughness alone; oxide chemistry, contamination and pretreatment can dominate. A scratch test probes a mixed mechanical geometry and does not directly return a universal interface fracture toughness without interpretation.

**Core equation and domain.** For an ideal thin film, Stoney stress σf≈Es ts² Δκ/[6(1−νs)tf] with substrate elastic constants, substrate thickness ts, film thickness tf and curvature change Δκ. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**thin-film adhesion, interfaces and residual stress**—the most consequential distinction in this unit is **equilibrium wetting versus hysteretic metastable state**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Two coatings have equal thickness but different failure after thermal cycling. Map stress, adhesion, chemical profiles and crack initiation before ranking formulations.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Young equilibrium contact angle** isolates a single physical dependence, using **Surface-energy difference γSV−γSL** as its variable. Substitute **-7.5 mN/m** into its declared expression `Math.acos(dg/72)*180/Math.PI` to obtain **95.9791568 degrees**. For the second case use **0 mN/m**, obtaining **90 degrees**. The output falls between these two cases. The finite-difference slope is **-0.797220906 (degrees)/(mN/m)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Stoney curvature estimates assume a thin uniform film on a sufficiently thick linear-elastic substrate and require correct sign convention. Nanostructured porous coatings can violate continuum uniform-film assumptions.

### Experimental characterization and controls

Conduct an **units and dimensional consistency audit**: Show every physical input in SI equivalents; reject models whose equation combines geometry, energy and concentration with unspecified conversions. Follow with a **fit parameter covariance audit**: Identify parameters traded against each other by a model and obtain orthogonal observations to reduce nonuniqueness. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface contamination or trapped air pockets**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **thin-film adhesion, interfaces and residual stress** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **roughness, chemical history and environmental cycling** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **thin-film adhesion, interfaces and residual stress** depends on **surface chemistry and morphology**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **95.9791568 degrees** for the first stated input and **90 degrees** for the second. Determine the finite-difference sensitivity **-0.797220906 (degrees)/(mN/m)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Lesson 7.4 — Surface patterning, tribology and wear

### Physical mechanism and structural interpretation

Surface texture can control friction, lubrication retention, adhesion and wear debris formation. Nanoscale roughness may reduce real contact area in one regime and enhance asperity plowing in another. Lubricated, boundary-lubricated and dry contacts follow distinct mechanisms. Hard coatings fail when substrate support, adhesion or fatigue is inadequate even if measured hardness is high. Characterization should include changes during sliding, not only pristine topography.

**Core equation and domain.** Archard-type wear approximation V≈k WL/H uses dimensionless wear factor k, load W, sliding distance L and hardness H in an established wear regime. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**surface patterning, tribology and wear**—the most consequential distinction in this unit is **equilibrium wetting versus hysteretic metastable state**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Compare a polished substrate with a nanostructured solid-lubricant coating under controlled humidity and load. Measure friction trajectory, wear volume and microscopy of debris and transfer films.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Wenzel apparent angle for an ideal rough surface** isolates a single physical dependence, using **True-to-projected surface-area ratio** as its variable. Substitute **1.75 dimensionless** into its declared expression `Math.acos(r*Math.cos(110*Math.PI/180))*180/Math.PI` to obtain **126.765065 degrees**. For the second case use **1.9375 dimensionless**, obtaining **131.503365 degrees**. The output rises between these two cases. The finite-difference slope is **25.2709332 (degrees)/(dimensionless)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

A low coefficient of friction in one short test is not a lifetime guarantee. AFM nanoscale friction values cannot be scaled directly to large rolling contacts without contact mechanics.

### Experimental characterization and controls

Conduct an **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. Follow with a **safety and environmental boundary audit**: Separate measured exposure and environmental releases from size-based hazard assumptions; seek site-approved professional assessments. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface contamination or trapped air pockets**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **surface patterning, tribology and wear** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **roughness, chemical history and environmental cycling** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **surface patterning, tribology and wear** depends on **surface chemistry and morphology**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **126.765065 degrees** for the first stated input and **131.503365 degrees** for the second. Determine the finite-difference sensitivity **25.2709332 (degrees)/(dimensionless)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

<!-- MODEL_13 -->

## Lesson 7.5 — Antifouling, corrosion protection and functional surfaces

### Physical mechanism and structural interpretation

A protective nanocoating may work as a barrier, sacrificial chemistry, inhibitor-release layer or surface-energy modification. Biological antifouling requires control of protein adsorption, microbial adhesion and cleaning history. Nanoparticle additives can create unintended release pathways or defect-assisted corrosion. Long-term effectiveness needs wet adhesion, permeation, mechanical abrasion and environmental exposure studies. Attractive initial contact angles do not establish contamination resistance.

**Core equation and domain.** A simple barrier diffusion time scales as τ≈L²/D_eff, but real pinholes, swelling and interfacial pathways can dominate lifetime. This formula is not a universal property divorced from specimen geometry and environment. State whether it represents an ideal particle, a continuum interface, a measured ensemble, a chemical equilibrium or a device response. Before applying it, label all variables with their units, distinguish particle diameter from radius and check whether the sample is dry, dispersed, supported or functionalized. For the present topic—**antifouling, corrosion protection and functional surfaces**—the most consequential distinction in this unit is **equilibrium wetting versus hysteretic metastable state**. Explain how geometry, aggregation or sample environment could change the observation even if the underlying nominal chemical composition remained fixed.

### Example to reason through before computation

Evaluate a self-cleaning surface after repeated abrasion and water exposure. Separate photoinduced chemical degradation of contaminants from mere rolling-droplet removal.

### Worked numerical example: model sensitivity, not measured data

The companion synthetic calculator **Young equilibrium contact angle** isolates a single physical dependence, using **Surface-energy difference γSV−γSL** as its variable. Substitute **7.5 mN/m** into its declared expression `Math.acos(dg/72)*180/Math.PI` to obtain **84.0208432 degrees**. For the second case use **15 mN/m**, obtaining **77.9753008 degrees**. The output falls between these two cases. The finite-difference slope is **-0.806072318 (degrees)/(mN/m)**. This calculation is a reproducible sensitivity illustration from a separately defined teaching model in this unit; for some lessons its variable intentionally probes a related unit principle rather than simulating the full lesson apparatus.

### Scope, counterexamples and physical failure modes

Accelerated corrosion tests require careful correlation to service environments. A coating that impedes one electrolyte may fail in a different pH or under galvanic coupling.

### Experimental characterization and controls

Conduct an **instrument and background calibration audit**: Use independent reference materials and a blank with the same matrix, acquisition settings and specimen preparation. Follow with a **distribution and sampling bias audit**: Count independent specimens and particles separately and report excluded or indistinguishable objects. For a comparison of two candidate materials, test whether the difference persists after normalizing specimen geometry, concentration, environment and operating conditions. A relative difference that is smaller than the combined systematic uncertainty cannot support a confident material ranking. If no method can distinguish the claimed mechanism from **surface contamination or trapped air pockets**, explicitly label the explanation unresolved.

### Interpretive checkpoint: what would disprove the claim?

A report on **antifouling, corrosion protection and functional surfaces** should offer at least one observation incompatible with the preferred mechanism, not only conditions that produce a good fit. Predict how a result should respond to a controlled change in **roughness, chemical history and environmental cycling** and how an alternate mechanism would respond. Discuss whether the required test probes primary-particle structure, an interfacial chemical effect, a device-level consequence or an instrument artifact. A successful materials investigation is one in which these levels can be separated quantitatively rather than collapsed into the phrase 'nano enhancement'.

### Three exercises with solution guidance

**A. Conceptual discrimination.** Explain in your own words how **antifouling, corrosion protection and functional surfaces** depends on **surface chemistry and morphology**. Propose a competing cause of the same observed size-property trend, and draw the experiment that distinguishes it. *Solution guidance:* state the measurable quantity and the signs or features predicted by both explanations, then identify a genuinely independent observable.

**B. Quantitative replication.** Starting from the model expression, calculate **84.0208432 degrees** for the first stated input and **77.9753008 degrees** for the second. Determine the finite-difference sensitivity **-0.806072318 (degrees)/(mN/m)**, and specify which approximation would fail first under a much larger perturbation. *Solution guidance:* substitute the numbers with correctly converted units, calculate Δoutput/Δinput, and use the sign to check the trend.

## Integrated case study — Evaluating a durable water-repellent nanocoating

### The decision to be made

A textured coating shows a contact angle above 150 degrees but fails after abrasion and prolonged immersion. Begin with a table of proposed mechanisms, the specimen states and boundaries each requires, the most informative measurand and a condition on which rival predictions differ. Identify whether the performance metric concerns primary material, processed component or assembled system; agreement on nominal size does not make these levels interchangeable.

### Computational investigation and sensitivity

Contrast ideal Young and fully wetted Wenzel relations under their different assumptions. Compare the two models in this unit at their default values, evaluate their extreme values and construct a sensitivity table with one parameter changed at a time. Because the models describe separate simplified phenomena, never combine them into a manufactured product forecast without deriving the coupling assumptions. Where a response changes rapidly, consider uncertainty in the control variable as a significant source of output uncertainty. Explain what dimensional or sign checks prevent an incorrect implementation from passing unnoticed.

### Measurement plan and discriminating evidence

Measure hysteresis, tilt angle, wetting-state changes, adhesive failure and durability across replicate coated substrates. Specify sample traceability, environmental conditions, calibration frequency and blind references. Record which particle population, chemical species or device channel is observed and which fractions are excluded by sample preparation or detection. Each test should have a predeclared decision criterion and should evaluate multiple independently processed specimens. If fitted parameters are strongly correlated, add an independent measurement of the quantity that produces the degeneracy. **Model caution:** Static contact angle alone cannot certify superhydrophobic durability or roll-off performance.

### Five end-of-unit questions

