# Unit 4: Machining, Abrasion and Surface Finishing

**Guiding question:** How can dimensional quality be balanced with tool wear and productivity?

## System definition and process constraints

A machined titanium component passes dimensional inspection at the start of a shift but produces inconsistent surfaces after two hours. Compare cutting parameters, tool condition, fixturing, coolant and vibration with measurable forces and surface integrity. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **machining forces and surface-integrity measurements**. Its indispensable records include **spindle speed, removal volume, vibration, tool wear, coolant and surface damage**, and important counterevidence comes from **profilometry, metrology and destructive material checks**. Before reading any calculated result, consider **whether nominally high throughput is offset by scrap or fatigue-sensitive surface layers**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 4.1 — Orthogonal cutting, chips and shear deformation

### 1. Physics, chemistry and the function actually supplied

Machining separates chips through highly localized shear, friction and temperature rise. Cutting speed, feed and depth change chip thickness, cutting force, heat distribution and tool wear. Specific cutting energy may rise at small chip thickness because ploughing contributes to force; metal removal is not proportional to useful cutting alone.

**Working relationship:** Turning speed in m/min = π × workpiece diameter (mm) × spindle revolutions per minute / 1000. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A short-chip recipe for a tough alloy reduces chip tangling but accelerates crater wear. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Steady ideal cutting relations omit chatter, interrupted contact and time-dependent wear. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal turning cutting speed**. Its computational expression is `Math.PI*60*N/1000`, with adjustable **Spindle speed** in rev/min. At 640 rev/min the deterministic output is **120.63716 m/min**; at 1560 rev/min it is **294.05307 m/min**. The two-point sensitivity is 0.18849556 m/min per rev/min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 60 mm workpiece diameter, no speed reduction with tool engagement or changes in surface diameter. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Record chip morphology, force, tool temperatures where feasible and actual accepted surface roughness across wear stages. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Fast cutting shortens cycle time but can raise insert consumption and scrap. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Turning speed in m/min = π × workpiece diameter (mm) × spindle revolutions per minute / 1000.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 120.63716 m/min from an input of 640 rev/min; calculate a third point midway between 640 and 1560, using the formula rather than copying the interactive output. Explain why a difference of 173.41591 m/min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A short-chip recipe for a tough alloy reduces chip tangling but accelerates crater wear.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Fast cutting shortens cycle time but can raise insert consumption and scrap.

## Lesson 4.2 — Milling kinematics and chatter

### 1. Physics, chemistry and the function actually supplied

Milling has intermittent tooth engagement; tooth pass frequency and machine dynamics can excite resonances. Spindle speed, number of teeth, feed per tooth, width of engagement and axial depth jointly affect stable cutting. A feed change alone cannot be interpreted without the machine/tool/fixture dynamic stiffness.

**Working relationship:** Nominal removal rate = width of cut × axial depth × feed travel speed, with consistent volume units. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A thin-wall milled part chatters only in one corner and then fails a surface integrity requirement. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Static-force calculations omit regenerative chatter and deflection of thin walls. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal milling metal-removal rate**. Its computational expression is `8*2*f/1000`, with adjustable **Feed rate** in mm/min. At 210 mm/min the deterministic output is **3.36 cm³/min**; at 480 mm/min it is **7.68 cm³/min**. The two-point sensitivity is 0.016 cm³/min per mm/min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Width of cut 8 mm and depth 2 mm; constant engagement, uniform material removal and no acceleration or chip evacuation losses. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Collect accelerometer spectra, spindle load, actual cut engagement and profilometry for unstable regions. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Higher material removal rate may reduce cycle time but destroy surface quality and tool life. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Nominal removal rate = width of cut × axial depth × feed travel speed, with consistent volume units.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 3.36 cm³/min from an input of 210 mm/min; calculate a third point midway between 210 and 480, using the formula rather than copying the interactive output. Explain why a difference of 4.32 cm³/min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A thin-wall milled part chatters only in one corner and then fails a surface integrity requirement.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Higher material removal rate may reduce cycle time but destroy surface quality and tool life.

<!-- MODEL_6 -->

## Lesson 4.3 — Tool wear, temperature and surface integrity

### 1. Physics, chemistry and the function actually supplied

Flank wear, crater wear, chipping and built-up edge are different mechanisms. They depend on thermal loads, tool/coating chemistry and contact. Surface integrity includes residual stress, microhardness change, microcracks and transformed phases, not only roughness. A tool can produce dimensional accuracy while leaving a damaged subsurface.

**Working relationship:** Useful wear monitoring compares measured wear metric against release threshold at specified material removal. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A ground nickel alloy is dimensionally correct but presents tensile surface residual stress and reduced fatigue life. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A single Taylor tool-life exponent cannot universally predict each failure mode or a new alloy. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal turning cutting speed**. Its computational expression is `Math.PI*60*N/1000`, with adjustable **Spindle speed** in rev/min. At 820 rev/min the deterministic output is **154.56636 m/min**; at 1720 rev/min it is **324.21236 m/min**. The two-point sensitivity is 0.18849556 m/min per rev/min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 60 mm workpiece diameter, no speed reduction with tool engagement or changes in surface diameter. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Map tool-edge images, hardness depth profiles, roughness and surface stress with controlled stock and process lots. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Longer tool life may require slower production but can reduce downstream rework and expensive component failures. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Useful wear monitoring compares measured wear metric against release threshold at specified material removal.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 154.56636 m/min from an input of 820 rev/min; calculate a third point midway between 820 and 1720, using the formula rather than copying the interactive output. Explain why a difference of 169.646 m/min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A ground nickel alloy is dimensionally correct but presents tensile surface residual stress and reduced fatigue life.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Longer tool life may require slower production but can reduce downstream rework and expensive component failures.

## Lesson 4.4 — Abrasive finishing and grinding burns

### 1. Physics, chemistry and the function actually supplied

Grinding includes many abrasive contacts, mechanical ploughing and thermal energy. Wheel specification, bond, grit, dressing, coolant and chip removal affect roughness and burn risk. Rehardening or tempering damage can occur below the surface without obvious discoloration. Surface finish acceptance should consider residual stress and material properties.

**Working relationship:** Grinding energy per removed volume = measured power × process time / measured removed volume. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A hardened bearing race shows fine Ra values but cracks after service because of local thermal damage. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Power averaged over the whole machine can exaggerate or hide actual wheel-work interaction and burn events. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal milling metal-removal rate**. Its computational expression is `8*2*f/1000`, with adjustable **Feed rate** in mm/min. At 260 mm/min the deterministic output is **4.16 cm³/min**; at 520 mm/min it is **8.32 cm³/min**. The two-point sensitivity is 0.016 cm³/min per mm/min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Width of cut 8 mm and depth 2 mm; constant engagement, uniform material removal and no acceleration or chip evacuation losses. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use in-process power data, metallography and appropriate hardness/residual stress checks after dressing cycles. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Aggressive removal improves rate but can exceed local thermal damage limits. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Grinding energy per removed volume = measured power × process time / measured removed volume.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 4.16 cm³/min from an input of 260 mm/min; calculate a third point midway between 260 and 520, using the formula rather than copying the interactive output. Explain why a difference of 4.16 cm³/min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A hardened bearing race shows fine Ra values but cracks after service because of local thermal damage.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Aggressive removal improves rate but can exceed local thermal damage limits.

<!-- MODEL_7 -->

## Lesson 4.5 — Surface texture, metrology and deburring

### 1. Physics, chemistry and the function actually supplied

Ra is one average amplitude descriptor, not a complete measure of texture, waviness, peaks, directionality or edge quality. Functional sealing, lubricant retention and fatigue may require different texture descriptors. Burrs threaten assembly and safety, while over-deburring can alter critical dimensions. Gauge contact force and filtering can change measured outcomes.

**Working relationship:** Surface assessment must specify measurement length, filter cutoff, tool orientation and acceptance metric. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** Two sealing faces have the same Ra but different leakage because their lay direction and peak distributions differ. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Comparisons without matching filtering and sampling paths can mistake a change in metrology for improved production. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal turning cutting speed**. Its computational expression is `Math.PI*60*N/1000`, with adjustable **Spindle speed** in rev/min. At 1000 rev/min the deterministic output is **188.49556 m/min**; at 1880 rev/min it is **354.37165 m/min**. The two-point sensitivity is 0.18849556 m/min per rev/min. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 60 mm workpiece diameter, no speed reduction with tool engagement or changes in surface diameter. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Validate profilometer settings, repeat paths across workpiece and check sealing or wear under functional loads. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Fine polishing improves cosmetics but may remove beneficial texture or consume excessive process time. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Surface assessment must specify measurement length, filter cutoff, tool orientation and acceptance metric.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 188.49556 m/min from an input of 1000 rev/min; calculate a third point midway between 1000 and 1880, using the formula rather than copying the interactive output. Explain why a difference of 165.87609 m/min is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “Two sealing faces have the same Ra but different leakage because their lay direction and peak distributions differ.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Fine polishing improves cosmetics but may remove beneficial texture or consume excessive process time.

## Unit 4 capstone — challenge, calculation, evidence and choice

**Integrated case:** A machined titanium component passes dimensional inspection at the start of a shift but produces inconsistent surfaces after two hours. Compare cutting parameters, tool condition, fixturing, coolant and vibration with measurable forces and surface integrity.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **machining forces and surface-integrity measurements**, recording **spindle speed, removal volume, vibration, tool wear, coolant and surface damage** and challenging the decision with **profilometry, metrology and destructive material checks**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether nominally high throughput is offset by scrap or fatigue-sensitive surface layers**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

