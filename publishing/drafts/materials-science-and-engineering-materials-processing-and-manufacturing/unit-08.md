# Unit 8: Quality, Digital Process Control and Industrial Scale-up

**Guiding question:** When can a laboratory process be called robust enough for production?

## System definition and process constraints

A pilot line builds flawless demonstrators but its production line misses cost and capability targets. Separate engineering repeatability, measurement system variation, sampling bias, machine maintenance, throughput, and qualified yield before scaling capital investment. A process comparison only becomes meaningful after the part function, equipment boundaries, batch size and mandatory safety and release specifications are written down. The system may contain machine setup changes, scrap and rework streams, queue delays, process losses and financial constraints. The engineering objective is to find the particular intervention that actually delivers qualified parts reliably with justified material, energy and safety burdens. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting one manufacturing process as universally superior.

An evidence-ready project in this unit starts with **metrology, within-lot and across-lot evidence**. Its indispensable records include **gauge uncertainty, control chart validity, first-pass yield, downtime and total cost**, and important counterevidence comes from **independent pilot cohorts and external model/process validation**. Before reading any calculated result, consider **which unobserved drift or bottleneck invalidates the proposed factory scale-up**. If the answer can be changed by a reasonable assumption about material grade, process variability or service conditions, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident qualified manufacturing recommendation.

## Unit project: challenge an appealing manufacturing performance claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the qualified part or service definition and a physically meaningful production baseline. Identify at least one material-flow constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, machine, material-batch and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected process recipes.

## Lesson 8.1 — Metrology, gauge studies and measurement uncertainty

### 1. Physics, chemistry and the function actually supplied

Every measurement contains variation from the measurand, instrument, environment, operator and measurement procedure. A process cannot be shown capable if the gauge has comparable spread to the allowed tolerance. Calibration and traceability differ from measurement-system suitability; high numerical display resolution is not evidence of accuracy.

**Working relationship:** Observed variance can contain process, repeatability and reproducibility components, interpreted under the study design. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A factory reports excellent dimensional repeatability using an uncalibrated digital gauge that shifts across operators. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Gauge bias and nonlinear response can remain even when repeatability appears very small. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Cp under fixed specification width**. Its computational expression is `0.30/(6*s)`, with adjustable **Observed within-subgroup sigma** in mm. At 0.03 mm the deterministic output is **1.6666667 Cp**; at 0.065 mm it is **0.76923077 Cp**. The two-point sensitivity is -25.641026 Cp per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed total specification tolerance 0.30 mm; sigma stable and estimated by valid rational subgroup method; Cp does not describe process centering or final defect rate. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Perform gauge R&R, bias, linearity and stability studies with traceable standards and representative parts. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** More precision equipment may be wasteful if process control rather than measurement dominates variability. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Observed variance can contain process, repeatability and reproducibility components, interpreted under the study design.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1.6666667 Cp from an input of 0.03 mm; calculate a third point midway between 0.03 and 0.065, using the formula rather than copying the interactive output. Explain why a difference of -0.8974359 Cp is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A factory reports excellent dimensional repeatability using an uncalibrated digital gauge that shifts across operators.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. More precision equipment may be wasteful if process control rather than measurement dominates variability.

## Lesson 8.2 — SPC, Cp and Cpk interpretation

### 1. Physics, chemistry and the function actually supplied

Statistical process control tracks process stability; capability indices compare variation and centering against engineering specifications. Cp measures spread relative to tolerance but does not test centering, while Cpk additionally accounts for the mean location. These indices require suitable data assumptions, subgroup strategy, and an in-control process before routine interpretation.

**Working relationship:** Cp = (upper specification − lower specification)/(6 × estimated within-process standard deviation). Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A shaft line reports Cp = 1.7 but produces undersize parts because the distribution is off center. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Mixtures of tooling populations, drifting centers and autocorrelation can invalidate a single capability score. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Good-unit cost after reject loss**. Its computational expression is `(1000*12+2000)/(1000*p/100)`, with adjustable **First-pass yield** in %. At 62 % the deterministic output is **22.580645 USD/accepted part**; at 83 % it is **16.86747 USD/accepted part**. The two-point sensitivity is -0.27205597 USD/accepted part per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** One invented lot of 1000 attempted parts, USD 12 variable cost each, USD 2000 setup, rejects have zero salvage; no inventory or rework effects. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use rational subgroup control charts, measurement-system studies and independently verified final defect counts. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Over-tight control can raise unnecessary inspection cost; under-controlled drift increases field failures. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Cp = (upper specification − lower specification)/(6 × estimated within-process standard deviation).”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 22.580645 USD/accepted part from an input of 62 %; calculate a third point midway between 62 and 83, using the formula rather than copying the interactive output. Explain why a difference of -5.7131753 USD/accepted part is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A shaft line reports Cp = 1.7 but produces undersize parts because the distribution is off center.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Over-tight control can raise unnecessary inspection cost; under-controlled drift increases field failures.

<!-- MODEL_14 -->

## Lesson 8.3 — Design of experiments and causal process windows

### 1. Physics, chemistry and the function actually supplied

A one-factor-at-a-time trial can miss interactions between temperature, pressure, speed, chemistry and geometry. Factorial experimental designs and response surfaces support causal inference when trials are randomized or otherwise designed to limit confounding. Replicates must be independent material lots or machine runs, not repeated readings of one output.

**Working relationship:** In a two-factor interaction model, response = intercept + aA + bB + cAB + error, with coded independent factors. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A sintering process improves on one shift but it is unclear whether furnace zone, atmosphere or binder lot caused it. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Correlations in uncontrolled production logs are not proof of causation. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Cp under fixed specification width**. Its computational expression is `0.30/(6*s)`, with adjustable **Observed within-subgroup sigma** in mm. At 0.035 mm the deterministic output is **1.4285714 Cp**; at 0.07 mm it is **0.71428571 Cp**. The two-point sensitivity is -20.408163 Cp per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed total specification tolerance 0.30 mm; sigma stable and estimated by valid rational subgroup method; Cp does not describe process centering or final defect rate. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Plan randomization, blocking, replication and predeclared responses with safety bounds on trial parameters. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Experimental exploration consumes material but can prevent expensive full-scale process mistakes. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “In a two-factor interaction model, response = intercept + aA + bB + cAB + error, with coded independent factors.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1.4285714 Cp from an input of 0.035 mm; calculate a third point midway between 0.035 and 0.07, using the formula rather than copying the interactive output. Explain why a difference of -0.71428571 Cp is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A sintering process improves on one shift but it is unclear whether furnace zone, atmosphere or binder lot caused it.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Experimental exploration consumes material but can prevent expensive full-scale process mistakes.

## Lesson 8.4 — Digital twins, sensing and closed-loop control

### 1. Physics, chemistry and the function actually supplied

A manufacturing digital twin is useful only when it links state estimates, measurable inputs and validated prediction targets. Temperature and vibration sensors can reveal drift but also generate false alarms; edge-cloud pipelines may introduce latency and time-alignment errors. Closed-loop control must respect equipment constraints, stability and safe interlocks.

**Working relationship:** Feedback error = measured setpoint departure, filtered and acted on within actuator limits and delays. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A thermal-processing line installs cameras and anomaly scores but rejects more good parts after a sensor drift. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A model trained on one alloy and machine may fail under different feedstock, geometry or maintenance. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Good-unit cost after reject loss**. Its computational expression is `(1000*12+2000)/(1000*p/100)`, with adjustable **First-pass yield** in %. At 66 % the deterministic output is **21.212121 USD/accepted part**; at 86 % it is **16.27907 USD/accepted part**. The two-point sensitivity is -0.24665257 USD/accepted part per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** One invented lot of 1000 attempted parts, USD 12 variable cost each, USD 2000 setup, rejects have zero salvage; no inventory or rework effects. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Validate sensors against reference instruments and test model drift, false positives and equipment-safe fallback behavior. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Automation may improve consistency but creates software maintenance and cybersecurity obligations. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Feedback error = measured setpoint departure, filtered and acted on within actuator limits and delays.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 21.212121 USD/accepted part from an input of 66 %; calculate a third point midway between 66 and 86, using the formula rather than copying the interactive output. Explain why a difference of -4.9330514 USD/accepted part is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A thermal-processing line installs cameras and anomaly scores but rejects more good parts after a sensor drift.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Automation may improve consistency but creates software maintenance and cybersecurity obligations.

<!-- MODEL_15 -->

## Lesson 8.5 — Scale-up, qualified yield and economic thresholds

### 1. Physics, chemistry and the function actually supplied

Scaling multiplies technical uncertainties: heat-transfer geometry, machine uptime, supplier variation, staffing, scrap and inventory all change. Mean lab yield is not enough to justify a production forecast; cost per accepted part includes setup and every rejected attempt. Stage-gated pilots limit losses and establish measurable no-go thresholds.

**Working relationship:** Cost per good unit = total attempted-unit costs and setup / accepted units for a defined batch. Keep the system boundary, physical units and quality specification visible before asserting a process improvement.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A prototype casting and machining process meets performance but yields only 60% acceptable units after a production transfer. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Pilot volumes may be cherry-picked, while factory constraints, defects and field returns emerge after ramp-up. Estimate which microstructural, dimensional, reliability or safety condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Cp under fixed specification width**. Its computational expression is `0.30/(6*s)`, with adjustable **Observed within-subgroup sigma** in mm. At 0.04 mm the deterministic output is **1.25 Cp**; at 0.08 mm it is **0.625 Cp**. The two-point sensitivity is -15.625 Cp per mm. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Fixed total specification tolerance 0.30 mm; sigma stable and estimated by valid rational subgroup method; Cp does not describe process centering or final defect rate. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Measure independent lots, stable demand, uptime, total rejected mass, customer returns and actual gross margins before expansion. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A slower but robust process can outperform an aggressive process once downtime and rejection are counted. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Cost per good unit = total attempted-unit costs and setup / accepted units for a defined batch.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 1.25 Cp from an input of 0.04 mm; calculate a third point midway between 0.04 and 0.08, using the formula rather than copying the interactive output. Explain why a difference of -0.625 Cp is not automatically a change in qualified part performance or factory economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A prototype casting and machining process meets performance but yields only 60% acceptable units after a production transfer.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A slower but robust process can outperform an aggressive process once downtime and rejection are counted.

## Unit 8 capstone — challenge, calculation, evidence and choice

**Integrated case:** A pilot line builds flawless demonstrators but its production line misses cost and capability targets. Separate engineering repeatability, measurement system variation, sampling bias, machine maintenance, throughput, and qualified yield before scaling capital investment.

1. **Service definition and counterfactual.** Define the required part function, load and service constraints, the baseline manufacturing route and a credible alternative that meets the same specification. Write down safety, qualification and regulatory constraints before comparing throughput and accepted-part cost.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted loss must be recorded rather than counted as qualified production output.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **metrology, within-lot and across-lot evidence**, recording **gauge uncertainty, control chart validity, first-pass yield, downtime and total cost** and challenging the decision with **independent pilot cohorts and external model/process validation**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and manufacturing trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **which unobserved drift or bottleneck invalidates the proposed factory scale-up**. No safety-critical release or product qualification is authorized by the classroom exercises.

### After the capstone

Compare qualified output per production hour, process materials consumed and critical quality metrics over several lots. A machine that cuts faster can still ship fewer accepted parts if defects or downtime increase. Document material batches, equipment state and acceptance criteria under which the selected process works. A credible manufacturing conclusion preserves part functionality, dimensional control, material history, safety requirements and uncertainty together.

