# Unit 1: Process Selection and Manufacturing Systems

**Guiding question:** How should a manufacturing route be selected when tolerances, quantities and economics conflict?

## System definition and process constraints

A manufacturer must deliver a mechanical bracket in three alloys at two production volumes. A route with the best nominal dimensional accuracy may be unprofitable at low quantity, while a low-unit-cost route may fail material integrity or traceability. Compare true cost per accepted part, process capability, lead time, safety, and production volume. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **route-selection requirements and qualified-volume estimate**. Its indispensable records include **material grade, functional release criteria, setups, yield, effective cycle times and line bottleneck**, and important counterevidence comes from **pilot route matrix and part/lot traceability inspection**. Before reading any calculated result, consider **whether a seemingly cheaper route fails capability or total accepted-unit cost**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 1.1 — Manufacturing route taxonomy and decision boundaries

### 1. Physics, chemistry and the function actually supplied

Casting distributes molten feed into a cavity; bulk forming reshapes solid stock plastically; machining removes chips; powder routes consolidate particulates; additive processes build selected regions; molding shapes polymer or ceramic feed; joining connects preforms. A part may require several routes in sequence, so the correct unit of selection is a qualified process chain. Geometry and mechanical properties impose hard constraints before economic scoring.

**Working relationship:** Feasible process chain = routes meeting minimum geometry, materials, safety and release criteria before cost ranking. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A complex stainless impeller can be cast, machined from billet or additively manufactured; compare quality assurance requirements at two batch sizes. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Single-process comparisons hide downstream finishing and inspection and may mistake a geometrically printable component for a performance-qualified component. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal cycle-time capacity**. Its computational expression is `3600/c`, with adjustable **Cycle time per part** in s/part. At 44 s/part the deterministic output is **81.818182 parts/h**; at 115 s/part it is **31.304348 parts/h**. The two-point sensitivity is -0.71146245 parts/h per s/part. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Continuous ideal operation, one part per cycle, no changeover, downtime or parallel stations; throughput must not be rounded up for actual orders. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Make a capability matrix with observed feature sizes, surface finish, achievable tolerances, batch yield and post-processing records. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Route flexibility reduces tooling commitment but may raise each-part cost and qualification burden. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Feasible process chain = routes meeting minimum geometry, materials, safety and release criteria before cost ranking.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 81.818182 parts/h from an input of 44 s/part; calculate a third point midway between 44 and 115, using the formula rather than copying the interactive output. Explain why a difference of -50.513834 parts/h is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A complex stainless impeller can be cast, machined from billet or additively manufactured; compare quality assurance requirements at two batch sizes.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Route flexibility reduces tooling commitment but may raise each-part cost and qualification burden.

## Lesson 1.2 — Manufacturing economics, cycle time and takt

### 1. Physics, chemistry and the function actually supplied

Takt follows customer demand while cycle time describes equipment output under defined operation. Setup, maintenance, yield and unplanned downtime change effective throughput; a nominal 60-second cycle never proves sixty good units per hour. Separate fixed investment, variable direct cost, scrap, rework, throughput and discounting of future cash flows to prevent unrealistic per-unit cost claims.

**Working relationship:** Good units per hour ≈ operating fraction × first-pass yield × 3600 / cycle time, for one independent station. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A machine meets a nominal cycle-time specification yet misses monthly orders after frequent changeovers and rework. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A nominal cycle time ignores material handling, staffing limits, bottlenecks and correlated line stoppages. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Qualified-part variable cost**. Its computational expression is `(12000+2000)/(1000*p/100)`, with adjustable **First-pass yield** in %. At 62 % the deterministic output is **22.580645 USD/qualified part**; at 83 % it is **16.86747 USD/qualified part**. The two-point sensitivity is -0.27205597 USD/qualified part per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A hypothetical batch incurs USD 12,000 variable and USD 2,000 setup cost for 1000 attempted units; rejects have no salvage and all fixed costs are assigned to passing units. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Collect timestamps for complete cycles, changeovers, scrap disposition and first-pass throughput over representative shifts. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Reducing a cycle may create more rejected material or require expensive tooling. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Good units per hour ≈ operating fraction × first-pass yield × 3600 / cycle time, for one independent station.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 22.580645 USD/qualified part from an input of 62 %; calculate a third point midway between 62 and 83, using the formula rather than copying the interactive output. Explain why a difference of -5.7131753 USD/qualified part is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A machine meets a nominal cycle-time specification yet misses monthly orders after frequent changeovers and rework.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Reducing a cycle may create more rejected material or require expensive tooling.

<!-- MODEL_0 -->

## Lesson 1.3 — Process capability versus design tolerances

### 1. Physics, chemistry and the function actually supplied

Dimensional tolerance describes the permissible product range; repeatability and capability describe actual process distributions under controlled conditions. A tight drawing tolerance cannot be met just by inspecting more parts. Datum strategy, thermal expansion, fixture contact and instrument uncertainty affect whether measured dimensions express the true part condition. Establish fit, function and safety limits before allocating tolerance budgets.

**Working relationship:** Worst-case stack-up can be bounded by the sum of constituent absolute tolerance limits, when correctly signed. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A 0.05 mm assembly clearance is assigned to individually machined parts without a stack-up or gauge-study plan. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Capability inferred from a small pilot may not survive tool wear, fixture swaps or inter-lot material variation. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal cycle-time capacity**. Its computational expression is `3600/c`, with adjustable **Cycle time per part** in s/part. At 58 s/part the deterministic output is **62.068966 parts/h**; at 127 s/part it is **28.346457 parts/h**. The two-point sensitivity is -0.48873201 parts/h per s/part. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Continuous ideal operation, one part per cycle, no changeover, downtime or parallel stations; throughput must not be rounded up for actual orders. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Run gauge repeatability and reproducibility analysis and dimensional inspection across independent production batches. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Loose tolerances may improve yield but harm assembly function; excessive precision may waste machining time. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Worst-case stack-up can be bounded by the sum of constituent absolute tolerance limits, when correctly signed.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 62.068966 parts/h from an input of 58 s/part; calculate a third point midway between 58 and 127, using the formula rather than copying the interactive output. Explain why a difference of -33.722509 parts/h is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A 0.05 mm assembly clearance is assigned to individually machined parts without a stack-up or gauge-study plan.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Loose tolerances may improve yield but harm assembly function; excessive precision may waste machining time.

## Lesson 1.4 — Design for manufacturing and assembly

### 1. Physics, chemistry and the function actually supplied

Feature accessibility, uniform sections, draft angles, tooling parting lines, joining clearance and number of setups strongly influence scrap and cycle time. A component optimized for finite-element mass alone can be impossible to fixture or inspect. Assembly simplification improves throughput when it preserves maintainability, repair and material separation, and may fail if it transfers difficult tolerance control to another stage.

**Working relationship:** Total route cost = tooling amortization + operations + inspection + rework + rejected material + logistics. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A thin-walled bracket is strong in simulation but requires multiple expensive setups and frequent scrap in milling. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Design-for-manufacture scores can conceal critical assembly damage or unsafe process constraints. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Qualified-part variable cost**. Its computational expression is `(12000+2000)/(1000*p/100)`, with adjustable **First-pass yield** in %. At 66 % the deterministic output is **21.212121 USD/qualified part**; at 86 % it is **16.27907 USD/qualified part**. The two-point sensitivity is -0.24665257 USD/qualified part per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** A hypothetical batch incurs USD 12,000 variable and USD 2,000 setup cost for 1000 attempted units; rejects have no salvage and all fixed costs are assigned to passing units. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Compare revisioned CAD parts through pilot fabrication, setup timing, assembly trials and functional release testing. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A slightly heavier near-net-shape design may yield less net waste and lower accepted-part cost. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Total route cost = tooling amortization + operations + inspection + rework + rejected material + logistics.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 21.212121 USD/qualified part from an input of 66 %; calculate a third point midway between 66 and 86, using the formula rather than copying the interactive output. Explain why a difference of -4.9330514 USD/qualified part is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A thin-walled bracket is strong in simulation but requires multiple expensive setups and frequent scrap in milling.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A slightly heavier near-net-shape design may yield less net waste and lower accepted-part cost.

<!-- MODEL_1 -->

## Lesson 1.5 — Manufacturing flow, bottlenecks and traceability

### 1. Physics, chemistry and the function actually supplied

Factory output follows the constraint station, not the arithmetic sum of isolated machine capacities. Buffers absorb short disturbances but increase inventory and defect quarantine complexity. Material identity, lot splits, machine program versions and operator interventions must travel with the workpiece to enable root-cause analysis. Little’s law links inventory, throughput and flow time only under suitable stable-system conditions.

**Working relationship:** For a stable system, work in process = throughput × average flow time with consistent units and boundaries. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A ten-station line has one unreliable furnace and a downstream inspection queue; adding two mills does not change shipped output. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Local machine utilization can rise while end-to-end lead time and rejected output worsen. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Ideal cycle-time capacity**. Its computational expression is `3600/c`, with adjustable **Cycle time per part** in s/part. At 71 s/part the deterministic output is **50.704225 parts/h**; at 139 s/part it is **25.899281 parts/h**. The two-point sensitivity is -0.3647786 parts/h per s/part. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Continuous ideal operation, one part per cycle, no changeover, downtime or parallel stations; throughput must not be rounded up for actual orders. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Build event logs tied to part/lot identifiers and measure queue times, constraint availability and shipments. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Buffers can prevent starvation but may hide recurring errors and increase working capital. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “For a stable system, work in process = throughput × average flow time with consistent units and boundaries.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 50.704225 parts/h from an input of 71 s/part; calculate a third point midway between 71 and 139, using the formula rather than copying the interactive output. Explain why a difference of -24.804945 parts/h is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A ten-station line has one unreliable furnace and a downstream inspection queue; adding two mills does not change shipped output.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Buffers can prevent starvation but may hide recurring errors and increase working capital.

## Unit 1 capstone — challenge, calculation, evidence and choice

**Integrated case:** A manufacturer must deliver a mechanical bracket in three alloys at two production volumes. A route with the best nominal dimensional accuracy may be unprofitable at low quantity, while a low-unit-cost route may fail material integrity or traceability. Compare true cost per accepted part, process capability, lead time, safety, and production volume.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **route-selection requirements and qualified-volume estimate**, recording **material grade, functional release criteria, setups, yield, effective cycle times and line bottleneck** and challenging the decision with **pilot route matrix and part/lot traceability inspection**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether a seemingly cheaper route fails capability or total accepted-unit cost**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

