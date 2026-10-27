# Unit 8: Circular design, economics and audit-ready decisions

**Guiding question:** What makes a reuse, remanufacture or recycling program economically and environmentally credible?

## The system before the material label

A manufacturer considers product-as-a-service for industrial pumps, take-back programs, repair modules and recycled feedstocks. Customer utilization, return rates, labor, transport and material specifications determine performance. A product comparison only becomes meaningful after its required service, physical boundaries, time and mandatory safety specifications are written down. The system may contain long-lived inventories, poorly measured return streams, process losses, upstream impacts and financial constraints. The engineering objective is to find the particular intervention that actually improves useful output per resource and reduces meaningful harms. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting recycling, repair, substitution or efficiency as universally superior.

An evidence-ready project in this unit starts with **financial and environmental performance per delivered service**. Its indispensable records include **retain qualified returns, revenues, repair hours, utilization, quality rejects and compliance costs**, and important counterevidence comes from **real-world pilot tracking with low/base/high scenarios**. Before reading any calculated result, consider **which bottleneck changes break-even and triggers a stop decision**. If the answer can be changed by a reasonable assumption about material quality or service life, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident environmental winner.

## Unit project: challenge an appealing sustainability claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the functional unit and a physically meaningful reference flow. Identify at least one mass-balance constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, geographic and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected sustainable-material slogans.

## Lesson 8.1 — Remanufacturing and product quality gates

### 1. Physics, chemistry and the function actually supplied

Remanufacturing restores an existing product core to specified performance through inspection, replacement, machining, assembly and qualification. It differs from simple resale or uncontrolled repair because documented product-level acceptance is essential. Core availability, hidden defects and dimensional tolerance determine process yield; parts rejected after assessment remain costs. Warranty obligations and configuration changes must be modeled.

**Working relationship:** Cost per qualified unit = (core procurement + inspection + processing + rejected-core costs) / units passing release. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A pump remanufacturer buys used cores but a third have damaged housings unsuitable for safe restoration. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Dividing costs by all received cores artificially improves estimated profit and environmental intensity. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Return system burden**. Its computational expression is `25/n+1`, with adjustable **Achieved delivery cycles** in cycles. At 9 cycles the deterministic output is **3.7777778 kg CO₂e/delivery**; at 25 cycles it is **2 kg CO₂e/delivery**. The two-point sensitivity is -0.11111111 kg CO₂e/delivery per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Synthetic container production 25 kg CO₂e, 1 kg CO₂e each return-and-clean cycle; only achieved cycles counted. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use batch-level records of rejection reasons, replacement parts, final testing and returns. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Aggressive intake increases volume but can lower yield and make remanufacturing less attractive than new production. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Cost per qualified unit = (core procurement + inspection + processing + rejected-core costs) / units passing release.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 3.7777778 kg CO₂e/delivery from an input of 9 cycles; calculate a third point midway between 9 and 25, using the formula rather than copying the interactive output. Explain why a difference of -1.7777778 kg CO₂e/delivery is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A pump remanufacturer buys used cores but a third have damaged housings unsuitable for safe restoration.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Aggressive intake increases volume but can lower yield and make remanufacturing less attractive than new production.

## Lesson 8.2 — Return logistics and reuse break-even

### 1. Physics, chemistry and the function actually supplied

Reverse logistics has uncertain collection rates, timing, geography and contamination. Reusable packaging must complete enough safe service cycles to offset its initial manufacturing and collection burden. Break-even depends on achieved uses rather than planned uses. Washing, inspection, theft, loss and return travel are material flows that should not be ignored. A deposit can improve recovery but adds payment and administrative costs.

**Working relationship:** Reuse impact per delivery = manufacture impact / achieved cycles + handling + cleaning + return transport per cycle. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A reusable shipping crate is heavier than a disposable cardboard box and returns on partially empty trucks. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Assuming a 100% return rate eliminates the very uncertainty that often determines program failure. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Five-year cash-flow NPV**. Its computational expression is `-40000+c*(1-Math.pow(1.08,-5))/0.08`, with adjustable **Net yearly cash flow** in USD/year. At 7000 USD/year the deterministic output is **-12051.03 USD**; at 19500 USD/year it is **37857.846 USD**. The two-point sensitivity is 3.99271 USD per USD/year. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** $40,000 initial investment, five annual end-of-year level net cash flows, fixed nominal discount 8%, no taxes or terminal value. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Pilot actual return cycles with loss tracking and calculate break-even across routes. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A reuse system can work well in dense local loops but fail environmentally or financially across sparse routes. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Reuse impact per delivery = manufacture impact / achieved cycles + handling + cleaning + return transport per cycle.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate -12051.03 USD from an input of 7000 USD/year; calculate a third point midway between 7000 and 19500, using the formula rather than copying the interactive output. Explain why a difference of 49908.875 USD is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A reusable shipping crate is heavier than a disposable cardboard box and returns on partially empty trucks.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A reuse system can work well in dense local loops but fail environmentally or financially across sparse routes.

<!-- MODEL_14 -->

## Lesson 8.3 — Product-as-a-service and incentive design

### 1. Physics, chemistry and the function actually supplied

Selling service rather than product ownership can reward durability, maintainability and utilization, but only if contracts align incentives. Providers may oversupply replacements to avoid downtime or keep inefficient equipment in service to defer capital spending. Service-level agreements should specify repair response, efficiency and safe retirement; economic risk transfers among provider and customer. A rental system with low utilization can require more equipment than customer ownership.

**Working relationship:** Profit per service hour = revenue per hour − maintenance − depreciation − logistics − financing per delivered hour. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A provider offers pump-hours for a monthly fee and guarantees uninterrupted operation using spare units. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Assuming all installed capacity produces billable service ignores idle units and downtime. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Return system burden**. Its computational expression is `25/n+1`, with adjustable **Achieved delivery cycles** in cycles. At 12 cycles the deterministic output is **3.0833333 kg CO₂e/delivery**; at 28 cycles it is **1.8928571 kg CO₂e/delivery**. The two-point sensitivity is -0.074404762 kg CO₂e/delivery per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Synthetic container production 25 kg CO₂e, 1 kg CO₂e each return-and-clean cycle; only achieved cycles counted. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Track utilization, faults, part swaps, energy efficiency and customer acceptance. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Sharing can lower the material stock per user but raises logistics and wear when poorly scheduled. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Profit per service hour = revenue per hour − maintenance − depreciation − logistics − financing per delivered hour.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 3.0833333 kg CO₂e/delivery from an input of 12 cycles; calculate a third point midway between 12 and 28, using the formula rather than copying the interactive output. Explain why a difference of -1.1904762 kg CO₂e/delivery is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A provider offers pump-hours for a monthly fee and guarantees uninterrupted operation using spare units.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Sharing can lower the material stock per user but raises logistics and wear when poorly scheduled.

## Lesson 8.4 — Product passports, EPR and procurement data

### 1. Physics, chemistry and the function actually supplied

Producer-responsibility schemes, procurement rules and traceability systems can shape circular incentives. Extended producer responsibility shifts some end-of-life obligations to producers under particular laws, but collection, recycling and fee structures vary. A product passport can help repairers and recyclers access information, provided data are accurate, accessible and interoperable. Claims must follow the legal status for the specific sector and market rather than copying broad EU policy headlines.

**Working relationship:** Traceability completeness = fields verified and relevant to the declared use / required fields for that use. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** An electronics brand exports to several countries and publishes a universal passport that omits hazardous-component location. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A compliance label is not a substitute for confirming the applicable regulation and its implementation date. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Five-year cash-flow NPV**. Its computational expression is `-40000+c*(1-Math.pow(1.08,-5))/0.08`, with adjustable **Net yearly cash flow** in USD/year. At 9500 USD/year the deterministic output is **-2069.2546 USD**; at 22000 USD/year it is **47839.621 USD**. The two-point sensitivity is 3.99271 USD per USD/year. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** $40,000 initial investment, five annual end-of-year level net cash flows, fixed nominal discount 8%, no taxes or terminal value. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Review product-specific legislation and data lineage with independent compliance specialists. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Rich documentation increases upfront costs but can reduce disassembly errors and improve compliance evidence. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Traceability completeness = fields verified and relevant to the declared use / required fields for that use.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate -2069.2546 USD from an input of 9500 USD/year; calculate a third point midway between 9500 and 22000, using the formula rather than copying the interactive output. Explain why a difference of 49908.875 USD is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “An electronics brand exports to several countries and publishes a universal passport that omits hazardous-component location.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Rich documentation increases upfront costs but can reduce disassembly errors and improve compliance evidence.

<!-- MODEL_15 -->

## Lesson 8.5 — Decision portfolios, financing and performance KPIs

### 1. Physics, chemistry and the function actually supplied

Circular investment choices should be assessed as portfolios under constraints, not reduced to a single recycled-content target. Net present value reflects discounted cash flows; an environmental objective may also depend on emissions, critical-resource reliance and harm reduction not captured by cash price. Monitoring needs service-denominated KPIs, measured material recovery, quality retention, safety and social performance. Scenario analysis should reveal which policy, recovery or energy-price assumptions reverse the choice.

**Working relationship:** NPV = Σ_t CF_t/(1+r)^t − initial investment, using a defined discount rate and period. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A company has funds for either a sorting system, a repair hub, or factory energy efficiency. Compare budget, deliverable service and uncertain prices. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A positive NPV under one assumed return rate is not robust evidence of commercial viability. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Return system burden**. Its computational expression is `25/n+1`, with adjustable **Achieved delivery cycles** in cycles. At 15 cycles the deterministic output is **2.6666667 kg CO₂e/delivery**; at 31 cycles it is **1.8064516 kg CO₂e/delivery**. The two-point sensitivity is -0.053763441 kg CO₂e/delivery per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Synthetic container production 25 kg CO₂e, 1 kg CO₂e each return-and-clean cycle; only achieved cycles counted. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Create low/base/high scenarios, measure pilot conversion and establish stop criteria before scaling. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** The best first project may be the one that tests the most uncertain bottleneck cheaply, not the largest theoretical impact. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “NPV = Σ_t CF_t/(1+r)^t − initial investment, using a defined discount rate and period.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 2.6666667 kg CO₂e/delivery from an input of 15 cycles; calculate a third point midway between 15 and 31, using the formula rather than copying the interactive output. Explain why a difference of -0.86021505 kg CO₂e/delivery is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A company has funds for either a sorting system, a repair hub, or factory energy efficiency. Compare budget, deliverable service and uncertain prices.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. The best first project may be the one that tests the most uncertain bottleneck cheaply, not the largest theoretical impact.

## Unit 8 capstone — challenge, calculation, evidence and choice

**Integrated case:** A manufacturer considers product-as-a-service for industrial pumps, take-back programs, repair modules and recycled feedstocks. Customer utilization, return rates, labor, transport and material specifications determine performance.

1. **Service definition and counterfactual.** Define the actual useful function and service horizon, identify the current material or process, and explain what product/service alternative is realistically available in the decision location. List safety and legal criteria that must be met before comparing optional environmental benefits.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted balance residual must be visibly labeled instead of silently treated as saleable recovered material.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **financial and environmental performance per delivered service**, recording **retain qualified returns, revenues, repair hours, utilization, quality rejects and compliance costs** and challenging the decision with **real-world pilot tracking with low/base/high scenarios**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and environmental trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **which bottleneck changes break-even and triggers a stop decision**. No safety-critical release or environmental certification is authorized by the classroom exercises.

### After the capstone

Discuss whether a reduction in impact *per service* is likely to translate into lower *total* resource use. A more efficient or more recyclable product can still be produced in expanding quantities, and a durable product can still create local harms if its manufacturing is poorly controlled. Document the supply chain and user context in which the conclusion holds. A coherent sustainability argument preserves engineering functionality, mass conservation, traceability and the limits of the available evidence at the same time.

