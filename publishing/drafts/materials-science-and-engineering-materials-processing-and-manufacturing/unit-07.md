# Unit 7: Joining, Heat Treatment and Surface Engineering

**Guiding question:** How do process thermal histories produce joints, phases and residual stresses?

## System definition and process constraints

A welded and heat-treated steel assembly meets visual inspection but fails a fatigue test. Diagnose thermal cycles, filler/base chemistry, HAZ hardness, incomplete fusion, surface condition, distortion and inspection limitations before approving a rework method. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **interface and heat-treatment qualification**. Its indispensable records include **heat input, thermal-cycle logs, weld and HAZ examination, chemistry and surface state**, and important counterevidence comes from **specific destructive/NDT release methods and component-level tests**. Before reading any calculated result, consider **whether acceptable visual appearance hides local property failures**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 7.1 — Fusion welding thermal cycles

### 1. Physics, chemistry and the function actually supplied

Welding creates a fusion zone and heat-affected zone with different peak temperatures and cooling rates. Travel speed and net heat input influence fusion geometry and microstructure but weld quality also depends on joint preparation, filler chemistry and restraint. A continuous bead may appear acceptable while hiding incomplete fusion or solidification cracks.

**Working relationship:** Simplified line energy ≈ process efficiency × voltage × current / travel speed. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A welded structural detail fails bend testing despite visually uniform bead width and measured current. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Fixed efficiency and steady electrical conditions omit varying arc transfer, fit-up and cooling paths. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Illustrative weld line energy**. Its computational expression is `0.75*20*150/v`, with adjustable **Travel speed** in mm/s. At 5 mm/s the deterministic output is **450 J/mm**; at 13 mm/s it is **173.07692 J/mm**. The two-point sensitivity is -34.615385 J/mm per mm/s. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 V, 150 A and thermal efficiency 0.75, steady bead; not a qualified weld procedure or a prediction of fusion, microstructure or distortion. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Log current/voltage waveforms, travel speed and thermocouple histories; section welds and test representative joints. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** More heat can aid fusion yet enlarge the HAZ and increase distortion. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Simplified line energy ≈ process efficiency × voltage × current / travel speed.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 450 J/mm from an input of 5 mm/s; calculate a third point midway between 5 and 13, using the formula rather than copying the interactive output. Explain why a difference of -276.92308 J/mm is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A welded structural detail fails bend testing despite visually uniform bead width and measured current.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. More heat can aid fusion yet enlarge the HAZ and increase distortion.

## Lesson 7.2 — Solid-state joining and interfaces

### 1. Physics, chemistry and the function actually supplied

Friction stir and diffusion bonding exploit interfacial contact, heat and deformation without conventional bulk fusion in the same manner as arc welding. Surface films, contact pressure, dwell time and cleanliness determine bond integrity; distinct materials can form brittle reaction layers. Robust joining requires actual interface testing, not simply a programmed tool travel path.

**Working relationship:** Nominal joint efficiency = measured joint strength / specified parent-metal strength using matched test method. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A friction-stir aluminum joint shows good external appearance but a tunnel defect along the root. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A single strength ratio hides local fracture path, fatigue and corrosion differences. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal diffusion distance**. Its computational expression is `Math.sqrt(2*1e-11*t*60)*1000000`, with adjustable **Hold duration** in min. At 58 min the deterministic output is **263.81812 µm**; at 158 min it is **435.43082 µm**. The two-point sensitivity is 1.716127 µm per min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** One-dimensional characteristic sqrt(2Dt), D=1e−11 m²/s fixed; real D is strongly temperature- and composition-dependent, boundary conditions and phase effects omitted. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure tool forces, macrosections, hardness profiles and shear/tensile/fatigue results across multiple weld lots. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Solid-state joining reduces some fusion defects but introduces tool wear and geometry access limits. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Nominal joint efficiency = measured joint strength / specified parent-metal strength using matched test method.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 263.81812 µm from an input of 58 min; calculate a third point midway between 58 and 158, using the formula rather than copying the interactive output. Explain why a difference of 171.6127 µm is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A friction-stir aluminum joint shows good external appearance but a tunnel defect along the root.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Solid-state joining reduces some fusion defects but introduces tool wear and geometry access limits.

<!-- MODEL_12 -->

## Lesson 7.3 — Heat-treatment kinetics, quenching and tempering

### 1. Physics, chemistry and the function actually supplied

Austenitizing, solution treatment, aging, quenching and tempering change phases, precipitates and defect populations through thermal history. Cooling media and section thickness affect transformation and residual stress. Diffusion-based characteristic lengths can guide thought but cannot substitute transformation diagrams, measured furnace uniformity or chemistry-dependent kinetics.

**Working relationship:** Characteristic one-dimensional diffusion length ≈ sqrt(2 × diffusivity × hold time) for fixed D. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A batch of thick steel shafts reaches the furnace setpoint but retains soft cores and quench distortion. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Diffusivity changes exponentially with temperature and may differ by species, phase and concentration. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Illustrative weld line energy**. Its computational expression is `0.75*20*150/v`, with adjustable **Travel speed** in mm/s. At 6.5 mm/s the deterministic output is **346.15385 J/mm**; at 14 mm/s it is **160.71429 J/mm**. The two-point sensitivity is -24.725275 J/mm per mm/s. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 V, 150 A and thermal efficiency 0.75, steady bead; not a qualified weld procedure or a prediction of fusion, microstructure or distortion. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use calibrated thermocouples on representative loads, phase/hardness depth mapping and dimensional metrology. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Fast quench raises hardenability but can increase cracking and distortion. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Characteristic one-dimensional diffusion length ≈ sqrt(2 × diffusivity × hold time) for fixed D.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 346.15385 J/mm from an input of 6.5 mm/s; calculate a third point midway between 6.5 and 14, using the formula rather than copying the interactive output. Explain why a difference of -185.43956 J/mm is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A batch of thick steel shafts reaches the furnace setpoint but retains soft cores and quench distortion.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Fast quench raises hardenability but can increase cracking and distortion.

## Lesson 7.4 — Coatings, case hardening and surface transformation

### 1. Physics, chemistry and the function actually supplied

Surface treatments change a thin zone or add an external barrier while bulk material remains different. Diffusion treatments, PVD, thermal spray and conversion films use different physical mechanisms. Coating adhesion, porosity, thermal mismatch, residual stress and substrate preparation govern performance; thickness alone does not prove suitability.

**Working relationship:** Wear reduction must be demonstrated as measured wear volume or rate under matched loading, not inferred from coating hardness alone. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A wear-resistant coating delaminates early because surface preparation was changed before deposition. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A high coating hardness may coexist with brittle interface failure and poor edge coverage. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal diffusion distance**. Its computational expression is `Math.sqrt(2*1e-11*t*60)*1000000`, with adjustable **Hold duration** in min. At 77 min the deterministic output is **303.97368 µm**; at 174 min it is **456.94639 µm**. The two-point sensitivity is 1.5770382 µm per min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** One-dimensional characteristic sqrt(2Dt), D=1e−11 m²/s fixed; real D is strongly temperature- and composition-dependent, boundary conditions and phase effects omitted. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use cross-section thickness maps, adhesion testing, wear trials and environmental conditioning. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A thicker film may improve barrier life but increase stress, material use and cost. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Wear reduction must be demonstrated as measured wear volume or rate under matched loading, not inferred from coating hardness alone.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 303.97368 µm from an input of 77 min; calculate a third point midway between 77 and 174, using the formula rather than copying the interactive output. Explain why a difference of 152.9727 µm is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A wear-resistant coating delaminates early because surface preparation was changed before deposition.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A thicker film may improve barrier life but increase stress, material use and cost.

<!-- MODEL_13 -->

## Lesson 7.5 — Inspection and joining acceptance

### 1. Physics, chemistry and the function actually supplied

Safety-critical joining qualification uses defined acceptance criteria and relevant non-destructive and destructive methods. Radiography and ultrasonic testing differ in detectability for crack orientation, geometry and material; a pass in one method is not universally a pass in another. Sampling plans must account for correlated defects and procedure changes.

**Working relationship:** Defect detection probability varies by flaw type, size, orientation, instrument and qualified technique. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A supplier qualifies a new weld parameter set using only visual checks and two tensile coupons. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** No NDT method can establish the absolute absence of every defect or guarantee future service life. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Illustrative weld line energy**. Its computational expression is `0.75*20*150/v`, with adjustable **Travel speed** in mm/s. At 8 mm/s the deterministic output is **281.25 J/mm**; at 15.5 mm/s it is **145.16129 J/mm**. The two-point sensitivity is -18.145161 J/mm per mm/s. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 V, 150 A and thermal efficiency 0.75, steady bead; not a qualified weld procedure or a prediction of fusion, microstructure or distortion. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Run qualified NDT procedures, trace reject maps to sections and test configuration-representative joints. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Tighter inspection adds cost and should also feed upstream root-cause correction. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Defect detection probability varies by flaw type, size, orientation, instrument and qualified technique.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 281.25 J/mm from an input of 8 mm/s; calculate a third point midway between 8 and 15.5, using the formula rather than copying the interactive output. Explain why a difference of -136.08871 J/mm is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A supplier qualifies a new weld parameter set using only visual checks and two tensile coupons.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Tighter inspection adds cost and should also feed upstream root-cause correction.

## Unit 7 capstone — challenge, calculation, evidence and choice

**Integrated case:** A welded and heat-treated steel assembly meets visual inspection but fails a fatigue test. Diagnose thermal cycles, filler/base chemistry, HAZ hardness, incomplete fusion, surface condition, distortion and inspection limitations before approving a rework method.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **interface and heat-treatment qualification**, recording **heat input, thermal-cycle logs, weld and HAZ examination, chemistry and surface state** and challenging the decision with **specific destructive/NDT release methods and component-level tests**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether acceptable visual appearance hides local property failures**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

