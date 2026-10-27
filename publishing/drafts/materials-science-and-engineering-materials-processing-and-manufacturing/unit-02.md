# Unit 2: Casting and Solidification Processing

**Guiding question:** Which melt and mold variables determine defects and microstructure?

## System definition and process constraints

An aluminum housing experiences centerline shrinkage and dispersed gas pores despite acceptable outer dimensions. Design a controlled casting trial separating feeding, solidification rate, dissolved gas, melt cleanliness, and geometry, and explain why none can be inferred from a single radiograph. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **melt-lot chemistry and thermal history**. Its indispensable records include **mold geometry, metal temperature, porosity, feeding paths and section cooling curves**, and important counterevidence comes from **sectioned test castings, radiography and independent heats**. Before reading any calculated result, consider **which defect mechanism actually causes loss rather than assuming all pores are gas**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 2.1 — Heat flow and mold solidification

### 1. Physics, chemistry and the function actually supplied

Solidification releases latent heat at an advancing phase boundary while mold conduction and interfacial heat transfer remove energy. Chvorinov-type scaling connects time to casting volume divided by effective surface area but only within a specified material and mold system. Mold coatings, local chills and hot spots change actual heat extraction and local structure; feed-path freeze order matters more than a single global cooling time.

**Working relationship:** Ideal solidification time = mold constant × (volume / area)^exponent, often exponent near two for simplified conduction scaling. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A thick boss on a thin-walled casting develops localized shrinkage porosity despite a fast average cooling time. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** One empirical mold constant does not describe different alloys, pouring superheats or mold materials. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Chvorinov ideal solidification time**. Its computational expression is `4*m*m`, with adjustable **Casting volume-to-area ratio** in cm. At 1.2 cm the deterministic output is **5.76 min**; at 2.7 cm it is **29.16 min**. The two-point sensitivity is 15.6 min per cm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Chvorinov scaling with a hypothetical mold constant of 4 min/cm²; geometry, superheat, interfacial heat transfer and material family otherwise held constant. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use instrumented thermocouples, solidification curves, sectioned castings and correlated thermal-model benchmarks. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Rapid cooling can refine structure but increase stress, misruns or thermal-gradient defects. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Ideal solidification time = mold constant × (volume / area)^exponent, often exponent near two for simplified conduction scaling.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 5.76 min from an input of 1.2 cm; calculate a third point midway between 1.2 and 2.7, using the formula rather than copying the interactive output. Explain why a difference of 23.4 min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A thick boss on a thin-walled casting develops localized shrinkage porosity despite a fast average cooling time.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Rapid cooling can refine structure but increase stress, misruns or thermal-gradient defects.

## Lesson 2.2 — Gating, feeding and shrinkage defects

### 1. Physics, chemistry and the function actually supplied

Gating transports the melt; risers or feeders compensate volume change during solidification if pressure, path and timing permit. Turbulent flow can entrain oxides or air while overly restrictive gates create incomplete filling. Centerline shrinkage differs from dispersed gas porosity and oxide inclusions and demands different countermeasures.

**Working relationship:** Metal feed balance = solid casting mass + runners/risers + spills and returns, reconciled on a stated basis. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A redesigned runner reduces visual splash but increases feeding distance and worsens internal shrinkage. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A radiographic dark region alone cannot identify whether voids originated from gas, solidification shrinkage or entrained folds. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Liquid-to-solid volume shrinkage**. Its computational expression is `1000*s/100`, with adjustable **Volumetric solidification shrinkage** in %. At 3.5 % the deterministic output is **35 cm³**; at 8 % it is **80 cm³**. The two-point sensitivity is 10 cm³ per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A hypothetical 1000 cm³ liquid casting; shrinkage here is volumetric and excludes liquid cooling, feeding, porosity and constrained distortion. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Combine melt hydrogen or gas tests, riser freeze-time estimates, radiography and destructive metallography of mapped regions. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Large risers protect feeding at the cost of metal yield, energy and downstream removal. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Metal feed balance = solid casting mass + runners/risers + spills and returns, reconciled on a stated basis.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 35 cm³ from an input of 3.5 %; calculate a third point midway between 3.5 and 8, using the formula rather than copying the interactive output. Explain why a difference of 45 cm³ is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A redesigned runner reduces visual splash but increases feeding distance and worsens internal shrinkage.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Large risers protect feeding at the cost of metal yield, energy and downstream removal.

<!-- MODEL_2 -->

## Lesson 2.3 — Nucleation, grain refinement and segregation

### 1. Physics, chemistry and the function actually supplied

Solidification produces nucleation events and grain growth while solute partitioning produces composition gradients. Faster interface movement may reduce certain length scales but can trap solute, change dendrite morphology and affect subsequent homogenization. Inoculant efficacy depends on particles, alloy chemistry and thermal history; a small measured grain size does not certify fatigue performance.

**Working relationship:** A schematic local solute partition at interface uses C_s = k C_l under declared equilibrium partition coefficient k. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** Two heats with equal nominal alloy chemistry show different dendrite arm spacing and interdendritic brittle phases. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Non-equilibrium solidification, microsegregation and post-cast homogenization defeat naïve equilibrium use. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Chvorinov ideal solidification time**. Its computational expression is `4*m*m`, with adjustable **Casting volume-to-area ratio** in cm. At 1.5 cm the deterministic output is **9 min**; at 2.9 cm it is **33.64 min**. The two-point sensitivity is 17.6 min per cm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Chvorinov scaling with a hypothetical mold constant of 4 min/cm²; geometry, superheat, interfacial heat transfer and material family otherwise held constant. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure local chemistry, phase distribution and cooling histories from independent heats, not a single selected section. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Aggressive grain refinement may improve uniformity but add inclusions if inoculation is uncontrolled. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “A schematic local solute partition at interface uses C_s = k C_l under declared equilibrium partition coefficient k.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 9 min from an input of 1.5 cm; calculate a third point midway between 1.5 and 2.9, using the formula rather than copying the interactive output. Explain why a difference of 24.64 min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “Two heats with equal nominal alloy chemistry show different dendrite arm spacing and interdendritic brittle phases.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Aggressive grain refinement may improve uniformity but add inclusions if inoculation is uncontrolled.

## Lesson 2.4 — Casting processes: sand, die and investment

### 1. Physics, chemistry and the function actually supplied

Sand molds offer flexible size and geometry but different dimensional accuracy, surface finish and solidification behavior from high-pressure die or investment casting. Tooling, cycle times, parting geometry and alloy suitability determine selection. Thin sections can benefit from rapid high-pressure filling yet turbulence and trapped gas can complicate later heat treatment or welding.

**Working relationship:** Process choice must satisfy metal temperature, pressure, geometry, dimensional finish and release tests before unit-cost comparison. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A part specified in sand-cast aluminum is moved to die casting at much higher annual volume without revising porosity acceptance. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Capital cost per part ignores inspection, die maintenance, trapped gas, coating and metal-feed yields. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Liquid-to-solid volume shrinkage**. Its computational expression is `1000*s/100`, with adjustable **Volumetric solidification shrinkage** in %. At 4.5 % the deterministic output is **45 cm³**; at 9 % it is **90 cm³**. The two-point sensitivity is 10 cm³ per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A hypothetical 1000 cm³ liquid casting; shrinkage here is volumetric and excludes liquid cooling, feeding, porosity and constrained distortion. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Conduct process-specific pilot lots and cross-section porosity, dimensional and mechanical acceptance testing. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** High-cost tooling pays off only if actual qualified production volume and material performance justify it. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Process choice must satisfy metal temperature, pressure, geometry, dimensional finish and release tests before unit-cost comparison.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 45 cm³ from an input of 4.5 %; calculate a third point midway between 4.5 and 9, using the formula rather than copying the interactive output. Explain why a difference of 45 cm³ is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A part specified in sand-cast aluminum is moved to die casting at much higher annual volume without revising porosity acceptance.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. High-cost tooling pays off only if actual qualified production volume and material performance justify it.

<!-- MODEL_3 -->

## Lesson 2.5 — Cast quality assurance and process windows

### 1. Physics, chemistry and the function actually supplied

Foundry quality must be traced from melt lot through chemistry, temperature, degassing, pouring, cooling and inspection. Porosity mapping, tensile coupons and hardness tests do not interrogate the same failure mechanism. A statistical control window must remain tied to process settings actually measured and to regions where service stresses occur.

**Working relationship:** Qualified casting yield = accepted functional units / poured casting attempts with defined exclusions. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** An aluminum gearbox case passes coupon tensile tests but leaks pressure through a localized internal pore network. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Coupon strength sampled away from hotspots may miss the local defect population of a stressed feature. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Chvorinov ideal solidification time**. Its computational expression is `4*m*m`, with adjustable **Casting volume-to-area ratio** in cm. At 1.8 cm the deterministic output is **12.96 min**; at 3.2 cm it is **40.96 min**. The two-point sensitivity is 20 min per cm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Chvorinov scaling with a hypothetical mold constant of 4 min/cm²; geometry, superheat, interfacial heat transfer and material family otherwise held constant. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Link location-specific nondestructive tests to machined leakage, fatigue and sectioning results over several heats. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Excessive 100% nondestructive inspection may be costly without lowering upstream defect generation. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Qualified casting yield = accepted functional units / poured casting attempts with defined exclusions.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 12.96 min from an input of 1.8 cm; calculate a third point midway between 1.8 and 3.2, using the formula rather than copying the interactive output. Explain why a difference of 28 min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “An aluminum gearbox case passes coupon tensile tests but leaks pressure through a localized internal pore network.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Excessive 100% nondestructive inspection may be costly without lowering upstream defect generation.

## Unit 2 capstone — challenge, calculation, evidence and choice

**Integrated case:** An aluminum housing experiences centerline shrinkage and dispersed gas pores despite acceptable outer dimensions. Design a controlled casting trial separating feeding, solidification rate, dissolved gas, melt cleanliness, and geometry, and explain why none can be inferred from a single radiograph.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **melt-lot chemistry and thermal history**, recording **mold geometry, metal temperature, porosity, feeding paths and section cooling curves** and challenging the decision with **sectioned test castings, radiography and independent heats**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **which defect mechanism actually causes loss rather than assuming all pores are gas**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

