# Unit 3: Deformation Processing and Metal Forming

**Guiding question:** How do stress, strain, friction and temperature govern forming limits?

## System definition and process constraints

A steel strip exits a rolling train with variable thickness, edge cracking and residual curvature. Diagnose force, roll wear, lubrication, texture and thermal gradients using separated process measurements rather than attributing every defect to excessive strain. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **measured flow conditions and deformation maps**. Its indispensable records include **strain paths, force, friction, temperature, tooling wear and residual stress**, and important counterevidence comes from **orientation-specific property testing and forming-limit evidence**. Before reading any calculated result, consider **whether increased reduction induces local tearing or nonuniform stresses**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 3.1 — Stress, strain and constitutive response

### 1. Physics, chemistry and the function actually supplied

Plastic deformation begins after yielding and is governed by strain hardening, temperature, strain rate and microstructure. Engineering strain and true logarithmic strain are not interchangeable at large uniform extensions, and homogeneous uniaxial assumptions collapse after necking. Flow stress needed by forming simulations must be measured under relevant thermal and strain-rate conditions.

**Working relationship:** Homogeneous axial true strain = ln(final gauge length / initial gauge length). Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A forming simulation using room-temperature engineering stress data underpredicts warm press loads and springback. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Compression, multiaxial flow, localization and friction change the deformation path beyond simple extension. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **True strain under uniaxial extension**. Its computational expression is `Math.log(L/50)`, with adjustable **Final gauge length** in mm. At 68 mm the deterministic output is **0.3074847 dimensionless**; at 95 mm it is **0.64185389 dimensionless**. The two-point sensitivity is 0.012384044 dimensionless per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Initial gauge length 50 mm; homogeneous uniaxial deformation with length measured consistently; necking makes uniform strain inference invalid. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure true stress–strain over valid uniform ranges and compare thermomechanical tests with local strain fields. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Higher strain hardening can suppress localization but raise equipment force and tooling loads. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Homogeneous axial true strain = ln(final gauge length / initial gauge length).”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 0.3074847 dimensionless from an input of 68 mm; calculate a third point midway between 68 and 95, using the formula rather than copying the interactive output. Explain why a difference of 0.33436919 dimensionless is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A forming simulation using room-temperature engineering stress data underpredicts warm press loads and springback.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Higher strain hardening can suppress localization but raise equipment force and tooling loads.

## Lesson 3.2 — Rolling contact, reduction and elastic flattening

### 1. Physics, chemistry and the function actually supplied

Rolling uses friction to pull work through a converging gap while plastic flow reduces thickness. Contact length, roll bending, separating force, speed, lubricant and temperature affect dimensional profile. Neutral point and friction vary along the bite; equations with constant mean flow stress are only first-order estimates.

**Working relationship:** First-order force ≈ mean pressure × strip width × projected roll contact length. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A strip rolling mill achieves central gauge but shows thicker edges and roll surface damage. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Actual roll flattening, entry/exit tension, thermal crowning and lubrication shift force and thickness. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Illustrative rolling separating force**. Its computational expression is `0.25*0.04*k*1000000`, with adjustable **Mean flow stress** in MPa. At 160 MPa the deterministic output is **1600000 N**; at 290 MPa it is **2900000 N**. The two-point sensitivity is 10000 N per MPa. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Constant contact length 0.04 m and width 0.25 m, mean pressure equal to flow stress, no friction/redundant work correction; not a mill setup calculation. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure force traces, contact geometry, strip profile across width and incoming microstructure under controlled passes. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** More aggressive reduction lowers pass count but can exceed torque limits or cause edge cracking. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “First-order force ≈ mean pressure × strip width × projected roll contact length.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1600000 N from an input of 160 MPa; calculate a third point midway between 160 and 290, using the formula rather than copying the interactive output. Explain why a difference of 1300000 N is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A strip rolling mill achieves central gauge but shows thicker edges and roll surface damage.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. More aggressive reduction lowers pass count but can exceed torque limits or cause edge cracking.

<!-- MODEL_4 -->

## Lesson 3.3 — Forging flow, dies and defect prevention

### 1. Physics, chemistry and the function actually supplied

Forging redirects plastic flow under compressive stress; grain-flow alignment and closure of voids may improve certain properties when performed within suitable conditions. Dead-metal zones, laps, underfill, dies, chilling and segregation can create harmful defects. Forging ratio alone does not guarantee an acceptable component.

**Working relationship:** Nominal reduction ratio = initial section area / final section area for idealized drawing or upset geometry. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A forged crankshaft has improved longitudinal strength but shows folds near a sharp die corner. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Flow lines are not direct measurements of all properties, and high reduction can worsen laps and die wear. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **True strain under uniaxial extension**. Its computational expression is `Math.log(L/50)`, with adjustable **Final gauge length** in mm. At 73 mm the deterministic output is **0.37843644 dimensionless**; at 100 mm it is **0.69314718 dimensionless**. The two-point sensitivity is 0.011655954 dimensionless per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Initial gauge length 50 mm; homogeneous uniaxial deformation with length measured consistently; necking makes uniform strain inference invalid. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use interrupted process trials, macroetch sections, nondestructive inspection and property tests by orientation. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Better grain flow often trades against die complexity, finishing stock and press tonnage. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Nominal reduction ratio = initial section area / final section area for idealized drawing or upset geometry.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 0.37843644 dimensionless from an input of 73 mm; calculate a third point midway between 73 and 100, using the formula rather than copying the interactive output. Explain why a difference of 0.31471074 dimensionless is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A forged crankshaft has improved longitudinal strength but shows folds near a sharp die corner.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Better grain flow often trades against die complexity, finishing stock and press tonnage.

## Lesson 3.4 — Extrusion, drawing and residual stress

### 1. Physics, chemistry and the function actually supplied

In extrusion, a billet is forced through a die; drawing pulls stock through a reduction. Friction, redundant shear, deformation heating and die angle drive force and surface quality. Residual stress can develop across thick/thin sections and cause distortion during machining. Lubrication failure may create surface cracking or pickup even if diameter appears correct.

**Working relationship:** Area reduction ratio = initial cross-sectional area / exit area, with true area strain ln(A0/Af) for volume-conserving flow. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** An extruded profile bows during secondary machining because trapped residual stresses redistribute. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Nonuniform temperature and strain invalidates a single scalar strain as a complete stress-state description. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Illustrative rolling separating force**. Its computational expression is `0.25*0.04*k*1000000`, with adjustable **Mean flow stress** in MPa. At 180 MPa the deterministic output is **1800000 N**; at 310 MPa it is **3100000 N**. The two-point sensitivity is 10000 N per MPa. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Constant contact length 0.04 m and width 0.25 m, mean pressure equal to flow stress, no friction/redundant work correction; not a mill setup calculation. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure exit temperature, force, die wear, profile curvature and residual stress before and after stress relief. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Higher reductions can improve throughput but increase press load, die damage and local overheating. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Area reduction ratio = initial cross-sectional area / exit area, with true area strain ln(A0/Af) for volume-conserving flow.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1800000 N from an input of 180 MPa; calculate a third point midway between 180 and 310, using the formula rather than copying the interactive output. Explain why a difference of 1300000 N is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “An extruded profile bows during secondary machining because trapped residual stresses redistribute.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Higher reductions can improve throughput but increase press load, die damage and local overheating.

<!-- MODEL_5 -->

## Lesson 3.5 — Sheet forming limits and springback

### 1. Physics, chemistry and the function actually supplied

Sheet forming combines membrane stretching, bending and contact friction. Forming-limit diagrams represent empirically determined strain-localization boundaries for a material and thickness; their use requires strain path and measurement context. Springback arises from elastic recovery after nonuniform plastic loading and depends on geometry, yield behavior and tooling.

**Working relationship:** Qualitative springback sensitivity rises with elastic modulus to yield-stress ratio and section geometry; no universal one-factor law. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** An automotive panel passes a thickness check but exhibits springback and localized necking at a draw-bead transition. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Forming limit data measured on monotonic paths may not predict complex non-proportional industrial paths. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **True strain under uniaxial extension**. Its computational expression is `Math.log(L/50)`, with adjustable **Final gauge length** in mm. At 78 mm the deterministic output is **0.44468582 dimensionless**; at 104 mm it is **0.73236789 dimensionless**. The two-point sensitivity is 0.011064695 dimensionless per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Initial gauge length 50 mm; homogeneous uniaxial deformation with length measured consistently; necking makes uniform strain inference invalid. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Collect grid strain maps, local thinning, press force and scanned final curvature across coil lots. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Stronger sheets may reduce mass but demand more complex compensation, lubrication and tooling. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Qualitative springback sensitivity rises with elastic modulus to yield-stress ratio and section geometry; no universal one-factor law.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 0.44468582 dimensionless from an input of 78 mm; calculate a third point midway between 78 and 104, using the formula rather than copying the interactive output. Explain why a difference of 0.28768207 dimensionless is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “An automotive panel passes a thickness check but exhibits springback and localized necking at a draw-bead transition.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Stronger sheets may reduce mass but demand more complex compensation, lubrication and tooling.

## Unit 3 capstone — challenge, calculation, evidence and choice

**Integrated case:** A steel strip exits a rolling train with variable thickness, edge cracking and residual curvature. Diagnose force, roll wear, lubrication, texture and thermal gradients using separated process measurements rather than attributing every defect to excessive strain.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **measured flow conditions and deformation maps**, recording **strain paths, force, friction, temperature, tooling wear and residual stress** and challenging the decision with **orientation-specific property testing and forming-limit evidence**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether increased reduction induces local tearing or nonuniform stresses**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

