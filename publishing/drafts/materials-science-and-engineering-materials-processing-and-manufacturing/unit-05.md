# Unit 5: Powder Processing and Additive Manufacturing

**Guiding question:** Which powder and layer variables govern acceptable printed component properties?

## System definition and process constraints

A powder-bed metal part with apparently good geometry fails fatigue screening. Distinguish pore morphology, build orientation, lack-of-fusion regions, powder reuse, residual stress and post-processing using build-by-build traceable evidence. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **powder batch identity and build/thermal logs**. Its indispensable records include **particle distribution, chemistry, layer sequence, post-treatment, void morphology and coupon location**, and important counterevidence comes from **cross-build qualification and nondestructive mapping against functional tests**. Before reading any calculated result, consider **whether build settings and coupon performance represent the critical interior geometry**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 5.1 — Powder characterization and handling

### 1. Physics, chemistry and the function actually supplied

Particle-size distribution, morphology, chemistry, moisture, satellites and contamination influence spreading, packing and sintering or melting. Bulk density is not identical to true solid density; apparent flowability tests depend on test apparatus. Fine powders have potential combustible dust and inhalation hazards requiring engineered controls and qualified supervision.

**Working relationship:** A powder mass balance separates incoming powder, built mass, recoverable excess, screened rejects and hazardous waste. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A reused alloy powder spreads unevenly despite matching a supplier median particle-size specification. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Median particle size hides tails of the distribution and condition changes during reuse. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Powder-bed layer-count estimate**. Its computational expression is `Math.ceil(20/t)`, with adjustable **Nominal layer thickness** in mm. At 0.04 mm the deterministic output is **500 layers**; at 0.08 mm it is **250 layers**. The two-point sensitivity is -6250 layers per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 mm build height, ideal slicing, no recoater gaps, adaptive layers, contour differences or dimensional compensation. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Run particle imaging, oxygen/moisture analyses, flow tests and build-density coupons on traceable powder lots. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Wider powder reuse can lower material expenditure but raises variability and screening needs. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “A powder mass balance separates incoming powder, built mass, recoverable excess, screened rejects and hazardous waste.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 500 layers from an input of 0.04 mm; calculate a third point midway between 0.04 and 0.08, using the formula rather than copying the interactive output. Explain why a difference of -250 layers is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A reused alloy powder spreads unevenly despite matching a supplier median particle-size specification.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Wider powder reuse can lower material expenditure but raises variability and screening needs.

## Lesson 5.2 — Powder-bed fusion thermal pathways

### 1. Physics, chemistry and the function actually supplied

Localized fusion creates moving melt pools with steep gradients, thermal cycling and rapid solidification. Insufficient energy can leave lack-of-fusion defects; excessive local input can promote vaporization, keyhole pores or spatter. Energy density summaries are helpful screening coordinates but do not uniquely characterize melt pool dynamics because beam diameter, path and absorption matter.

**Working relationship:** Nominal volumetric energy density = beam power / (scan speed × hatch spacing × layer thickness). Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** Two laser powder-bed recipes have identical volumetric energy density but different pore shapes and tensile anisotropy. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A constant energy-density value does not imply equivalent absorbed energy, laser spot or scan strategies. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Powder-based feed for qualified part**. Its computational expression is `500/(p/100)`, with adjustable **Material utilization fraction** in %. At 38 % the deterministic output is **1315.7895 g feed**; at 69 % it is **724.63768 g feed**. The two-point sensitivity is -19.069413 g feed per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A 500 g delivered part and one lumped utilization factor; ignores chemistry drift, contamination, non-recyclable support, powder ageing and transport. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Link build logs, optical melt-pool signals, CT inspection and orientation-specific mechanical tests. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Increasing laser energy may reduce incomplete fusion while creating new defects and residual stress. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Nominal volumetric energy density = beam power / (scan speed × hatch spacing × layer thickness).”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1315.7895 g feed from an input of 38 %; calculate a third point midway between 38 and 69, using the formula rather than copying the interactive output. Explain why a difference of -591.15179 g feed is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “Two laser powder-bed recipes have identical volumetric energy density but different pore shapes and tensile anisotropy.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Increasing laser energy may reduce incomplete fusion while creating new defects and residual stress.

<!-- MODEL_8 -->

## Lesson 5.3 — Build orientation, supports and layer strategies

### 1. Physics, chemistry and the function actually supplied

Layer-by-layer construction produces stair-step surfaces and direction-dependent thermal histories. Orientation changes support requirement, critical overhangs, accessible powder evacuation and loaded tensile direction. Nominal layer count is not equal to elapsed build time because scanning and recoating times vary with cross-sectional area.

**Working relationship:** Ideal layer count = ceiling(build height / programmed nominal layer thickness). Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** An aerospace lattice can be printed with fewer supports in one orientation but fails post-process inspection near blind passages. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Actual slicing may use variable layers, correction offsets and periodic pauses. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Powder-bed layer-count estimate**. Its computational expression is `Math.ceil(20/t)`, with adjustable **Nominal layer thickness** in mm. At 0.05 mm the deterministic output is **400 layers**; at 0.09 mm it is **223 layers**. The two-point sensitivity is -4425 layers per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 mm build height, ideal slicing, no recoater gaps, adaptive layers, contour differences or dimensional compensation. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Inspect supports, scan strategy, trapped powder and specimen anisotropy in a replicated design-of-experiments matrix. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Shorter builds can trade off against surface integrity or inaccessible supports. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Ideal layer count = ceiling(build height / programmed nominal layer thickness).”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 400 layers from an input of 0.05 mm; calculate a third point midway between 0.05 and 0.09, using the formula rather than copying the interactive output. Explain why a difference of -177 layers is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “An aerospace lattice can be printed with fewer supports in one orientation but fails post-process inspection near blind passages.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Shorter builds can trade off against surface integrity or inaccessible supports.

## Lesson 5.4 — Binder jetting and post-build consolidation

### 1. Physics, chemistry and the function actually supplied

Binder jetting shapes powder with fluid binders, followed by curing, debinding, sintering or infiltration depending on material. Shrinkage depends on green density, particle packing, binder removal and spatial thermal history. Post-sintering machining may still be necessary for interfaces, and strength cannot be inferred from the as-printed geometry.

**Working relationship:** For uniform mass and isotropic shrinkage, final length = initial length × (initial density/final density)^(1/3). Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A binder-jetted steel part is within shape tolerance as green body but distorts after densification. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Binder decomposition gases, anisotropy and nonuniform density violate homogeneous assumptions. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Powder-based feed for qualified part**. Its computational expression is `500/(p/100)`, with adjustable **Material utilization fraction** in %. At 44 % the deterministic output is **1136.3636 g feed**; at 74 % it is **675.67568 g feed**. The two-point sensitivity is -15.356265 g feed per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A 500 g delivered part and one lumped utilization factor; ignores chemistry drift, contamination, non-recyclable support, powder ageing and transport. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure green density maps, debinding mass-loss curves, post-sinter dimensions and porosity by region. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Higher green packing may reduce shrink but complicate binder infiltration or printing. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “For uniform mass and isotropic shrinkage, final length = initial length × (initial density/final density)^(1/3).”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1136.3636 g feed from an input of 44 %; calculate a third point midway between 44 and 74, using the formula rather than copying the interactive output. Explain why a difference of -460.68796 g feed is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A binder-jetted steel part is within shape tolerance as green body but distorts after densification.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Higher green packing may reduce shrink but complicate binder infiltration or printing.

<!-- MODEL_9 -->

## Lesson 5.5 — AM validation, repair and qualification

### 1. Physics, chemistry and the function actually supplied

Printed material properties reflect feedstock, machine calibration, scan plan, post-treatment and design geometry. A tensile coupon placed at one build corner may not represent critical internal surfaces or unsupported passages. Repair and post-process changes can alter defect population and often trigger qualification changes for regulated components.

**Working relationship:** Release requires conformance to part-specific acceptance tests, not simply matching nominal printer settings. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A printed orthopedic fixture passes tensile coupons but fails nondestructive inspection near an internal channel. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Machine logs and parameter signatures cannot alone demonstrate every hidden defect is absent. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Powder-bed layer-count estimate**. Its computational expression is `Math.ceil(20/t)`, with adjustable **Nominal layer thickness** in mm. At 0.06 mm the deterministic output is **334 layers**; at 0.1 mm it is **200 layers**. The two-point sensitivity is -3350 layers per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed 20 mm build height, ideal slicing, no recoater gaps, adaptive layers, contour differences or dimensional compensation. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Develop build-to-build traceability and a qualified combination of imaging, coupons, dimensional and fatigue testing. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** More extensive qualification raises upfront cost but limits high-consequence field failures. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Release requires conformance to part-specific acceptance tests, not simply matching nominal printer settings.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 334 layers from an input of 0.06 mm; calculate a third point midway between 0.06 and 0.1, using the formula rather than copying the interactive output. Explain why a difference of -134 layers is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A printed orthopedic fixture passes tensile coupons but fails nondestructive inspection near an internal channel.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. More extensive qualification raises upfront cost but limits high-consequence field failures.

## Unit 5 capstone — challenge, calculation, evidence and choice

**Integrated case:** A powder-bed metal part with apparently good geometry fails fatigue screening. Distinguish pore morphology, build orientation, lack-of-fusion regions, powder reuse, residual stress and post-processing using build-by-build traceable evidence.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **powder batch identity and build/thermal logs**, recording **particle distribution, chemistry, layer sequence, post-treatment, void morphology and coupon location** and challenging the decision with **cross-build qualification and nondestructive mapping against functional tests**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether build settings and coupon performance represent the critical interior geometry**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

