# Unit 4: Polymers, sorting and molecular lifetimes

**Guiding question:** Which plastic routes preserve functional performance rather than just produce a recyclable label?

## The system before the material label

A mixed household-plastics stream contains incompatible polymers, pigments, food residue and multi-layer films. A packaging redesign could shift the balance among mechanical reprocessing, reuse and end-of-life leakage. A product comparison only becomes meaningful after its required service, physical boundaries, time and mandatory safety specifications are written down. The system may contain long-lived inventories, poorly measured return streams, process losses, upstream impacts and financial constraints. The engineering objective is to find the particular intervention that actually improves useful output per resource and reduces meaningful harms. The unit combines an explicit material mechanism with a data and decision workflow, rather than presenting recycling, repair, substitution or efficiency as universally superior.

An evidence-ready project in this unit starts with **polymer identity and performance over cycles**. Its indispensable records include **track polymer fraction, additives, melt history, functional quality and generated rejects**, and important counterevidence comes from **matched virgin controls, spectroscopy, rheology and mechanical testing**. Before reading any calculated result, consider **whether higher recovery lowers lifetime or increases leakage**. If the answer can be changed by a reasonable assumption about material quality or service life, the proper result is a bounded comparison and a plan to collect missing evidence, not a confident environmental winner.

## Unit project: challenge an appealing sustainability claim

Write an initial one-page decision specification for the case above. State the material in/out boundaries, the functional unit and a physically meaningful reference flow. Identify at least one mass-balance constraint and two competing mechanisms that might explain an observed difference. Then list the measurement owner, instrument or transaction log, geographic and temporal applicability, uncertainty and a specific control. Revisit this specification after each lesson. The five topics form parts of one investigation, not five disconnected sustainable-material slogans.

## Lesson 4.1 — Polymer identity and incompatible melt blending

### 1. Physics, chemistry and the function actually supplied

PET, HDPE, PP, PVC, polystyrene and multilayer structures have different chemistry, softening behavior and processing windows. Incompatible polymers can phase-separate and generate weak interfaces even when a blended pellet looks uniform. Small PVC contamination can degrade during processing of other polymers; moisture can promote hydrolysis in susceptible polyesters. Sortability is therefore a materials compatibility question, not just a labeling exercise.

**Working relationship:** Blend fraction φ_i = dry mass of polymer i / total dry polymer mass before processing. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A packaging line mixes clear PET bottles with PET-like multilayer packaging and reports high collection mass but brittle recycled sheet. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** A resin identification symbol does not certify material purity, food-contact suitability or available recycling infrastructure. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Hypothetical polymer-property retention**. Its computational expression is `100*Math.exp(-0.04*n)`, with adjustable **Reprocessing cycles** in cycles. At 2 cycles the deterministic output is **92.311635 % reference strength**; at 6 cycles it is **78.662786 % reference strength**. The two-point sensitivity is -3.4122121 % reference strength per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Arbitrary exponential demonstration, not a universal polymer degradation law; excludes additives and weathering. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Verify polymer identity by spectroscopy and process matched purity-controlled reference batches. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A multilayer film may improve food protection and reduce food waste while making high-grade material recovery more difficult. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Blend fraction φ_i = dry mass of polymer i / total dry polymer mass before processing.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 92.311635 % reference strength from an input of 2 cycles; calculate a third point midway between 2 and 6, using the formula rather than copying the interactive output. Explain why a difference of -13.648849 % reference strength is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A packaging line mixes clear PET bottles with PET-like multilayer packaging and reports high collection mass but brittle recycled sheet.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A multilayer film may improve food protection and reduce food waste while making high-grade material recovery more difficult.

## Lesson 4.2 — Mechanical recycling and molecular degradation

### 1. Physics, chemistry and the function actually supplied

Polymer melt processing exposes chains to temperature, shear, oxygen and moisture. Chain scission can lower molecular weight and mechanical performance, while branching or cross-linking can increase viscosity or embrittle material depending on resin. Colorants, fillers and contaminants change stability. Reprocessing cycles should be measured through rheology, spectroscopy and product testing rather than assumed to be indefinitely repeatable.

**Working relationship:** Relative retained property R = tested property after reprocessing / matched virgin baseline. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A recycled polypropylene product passes its first mechanical test but fails after accelerated weathering. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Single tensile strength data omit creep, impact, weathering and oxidative induction under service conditions. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Recovered compatible polymer**. Its computational expression is `500*(1-p/100)*0.8`, with adjustable **Non-target contamination fraction** in %. At 12 % the deterministic output is **352 kg**; at 33 % it is **268 kg**. The two-point sensitivity is -4 kg per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** 500 kg incoming dry plastic, non-target fraction p%, 80% recovery of compatible portion, constant process efficiency. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Track molecular-weight distribution, melt-flow characteristics and failure modes across controlled recycling cycles. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A cheaper resin with high recycled content may cause more replacements if fatigue or UV durability is insufficient. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Relative retained property R = tested property after reprocessing / matched virgin baseline.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 352 kg from an input of 12 %; calculate a third point midway between 12 and 33, using the formula rather than copying the interactive output. Explain why a difference of -84 kg is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A recycled polypropylene product passes its first mechanical test but fails after accelerated weathering.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A cheaper resin with high recycled content may cause more replacements if fatigue or UV durability is insufficient.

<!-- MODEL_6 -->

## Lesson 4.3 — Solvent dissolution and chemical recycling pathways

### 1. Physics, chemistry and the function actually supplied

Selective dissolution can separate a polymer from additives without necessarily breaking the polymer chain; depolymerization can produce monomers or other chemical feedstocks. Thermal conversion processes can generate multiple products requiring additional refining and may not constitute closed-loop material recycling. Solvent loss, separation energy, yields, impurities and emissions require full accounting. Labels such as chemical recycling should never substitute for an output-specific material balance.

**Working relationship:** Material-to-material yield = verified polymer-compatible recovered feedstock mass / incoming dry waste mass. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A company claims that all mixed plastic sent to a pyrolysis plant becomes new polymer. Trace gas, fuel, char, wax and chemical feedstocks. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Counting fuels or energy products as new polymer exaggerates circular closure. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Hypothetical polymer-property retention**. Its computational expression is `100*Math.exp(-0.04*n)`, with adjustable **Reprocessing cycles** in cycles. At 3 cycles the deterministic output is **88.692044 % reference strength**; at 7 cycles it is **75.578374 % reference strength**. The two-point sensitivity is -3.2784174 % reference strength per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Arbitrary exponential demonstration, not a universal polymer degradation law; excludes additives and weathering. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Audit input contaminants, product assays, destination certificates and continuous process energy. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** Chemical routes may address streams unsuitable for mechanical recycling but can consume significant energy and lose carbon as fuel or gas. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Material-to-material yield = verified polymer-compatible recovered feedstock mass / incoming dry waste mass.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 88.692044 % reference strength from an input of 3 cycles; calculate a third point midway between 3 and 7, using the formula rather than copying the interactive output. Explain why a difference of -13.11367 % reference strength is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A company claims that all mixed plastic sent to a pyrolysis plant becomes new polymer. Trace gas, fuel, char, wax and chemical feedstocks.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. Chemical routes may address streams unsuitable for mechanical recycling but can consume significant energy and lose carbon as fuel or gas.

## Lesson 4.4 — Bio-based, biodegradable and compostable distinctions

### 1. Physics, chemistry and the function actually supplied

Bio-based describes carbon origin, whereas biodegradability describes transformation under specified environmental conditions. A plastic may be fossil-derived yet biodegradable in an industrial system, or bio-based but persistent. Compostability claims depend on standardized conditions and actual collection and processing infrastructure. Land use, fertilizer, waste contamination and methane generation are relevant life-cycle considerations; labels alone cannot guarantee lower impacts.

**Working relationship:** Bio-based content fraction = verified biomass-derived carbon / defined total organic carbon basis. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** A city replaces conventional takeaway cups with compostable-coated paper while lacking a separate organics collection route. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Laboratory disintegration within a specified test does not imply rapid degradation in the ocean, soil or home compost. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Recovered compatible polymer**. Its computational expression is `500*(1-p/100)*0.8`, with adjustable **Non-target contamination fraction** in %. At 16 % the deterministic output is **336 kg**; at 36 % it is **256 kg**. The two-point sensitivity is -4 kg per %. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** 500 kg incoming dry plastic, non-target fraction p%, 80% recovery of compatible portion, constant process efficiency. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Check certification scope, local treatment acceptance and comparative disposal scenarios. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A compostable single-use item can still be inferior to a safely reused container in a high-return system. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Bio-based content fraction = verified biomass-derived carbon / defined total organic carbon basis.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 336 kg from an input of 16 %; calculate a third point midway between 16 and 36, using the formula rather than copying the interactive output. Explain why a difference of -80 kg is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “A city replaces conventional takeaway cups with compostable-coated paper while lacking a separate organics collection route.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A compostable single-use item can still be inferior to a safely reused container in a high-return system.

<!-- MODEL_7 -->

## Lesson 4.5 — Microplastics and leakage prevention

### 1. Physics, chemistry and the function actually supplied

Abrasion, fragmentation, textile laundering and poor containment create particles across the product life cycle. Particle count, mass and size distribution capture different exposure dimensions. Complex sampling and analytical blanks are essential because airborne particles can contaminate samples. Environmental persistence and biological harm vary by chemistry, particle morphology, additives and exposure; claims need specific evidence instead of extrapolation from a single laboratory test.

**Working relationship:** Leakage rate = measured lost polymer mass / service delivered, with size distributions reported separately. Keep the system boundary, physical units and quality specification visible before asserting an avoided impact.

### 2. A real engineering dilemma with rival explanations

**Problem statement:** Two synthetic textile fabrics release similar particle masses but very different counts. Decide what additional evidence is needed. Propose two rival mechanisms and one observation that differentiates them. Record timing, composition and functional performance before ranking either explanation.

**Constraint that can reverse the answer:** Comparing particle counts without detection limits and blank correction can reverse apparent rankings. Estimate which service, quality or environmental condition could reverse the conclusion.

### 3. Transparent synthetic calculation and sensitivity

The paired interactive card for this lesson is **Hypothetical polymer-property retention**. Its computational expression is `100*Math.exp(-0.04*n)`, with adjustable **Reprocessing cycles** in cycles. At 4 cycles the deterministic output is **85.214379 % reference strength**; at 8 cycles it is **72.614904 % reference strength**. The two-point sensitivity is -3.1498688 % reference strength per cycles. These are synthetic teaching calculations, not measurements. Independently verify units and a third input before interpretation.

**Why the numerical output has limits:** Arbitrary exponential demonstration, not a universal polymer degradation law; excludes additives and weathering. For a real decision, independently measure the variables that this illustrative formula holds constant.

### 4. Evidence protocol, sampling and falsification

**Specific investigation:** Use controlled wash cycles, procedural blanks, particle characterization and real sewer-pathway measurements. Define independent samples, record rejected outputs and capture instrument calibration and field-relevant service conditions.

 Verify both mass-balance closure and functionally qualified output; publish observations that contradict the preferred mechanism.

### 5. Design trade-off and conditions of adoption

**Trade-off:** A high-durability textile might reduce replacement production but still generate substantial shedding during use. Evaluate the trade-off only after minimum safety, quality and legal requirements are satisfied.

### 6. Three guided practice problems

**Question A — reconstruct the physical account.** Starting from “Leakage rate = measured lost polymer mass / service delivered, with size distributions reported separately.”, identify the relevant system, quantities, physical units and hidden assumptions. Draw material or energy arrows, label the conserved quantity and explain at least two potential losses or quality changes. **Solution guidance:** reconcile consistent physical units and include process losses.

**Question B — independent worked sensitivity.** Recalculate 85.214379 % reference strength from an input of 4 cycles; calculate a third point midway between 4 and 8, using the formula rather than copying the interactive output. Explain why a difference of -12.599475 % reference strength is not automatically a change in environmental benefit or service economics. **Solution guidance:** numerical sensitivity does not validate a site-specific benefit.

**Question C — design a decisive controlled comparison.** For “Two synthetic textile fabrics release similar particle masses but very different counts. Decide what additional evidence is needed.”, provide a sample plan, at least one suitable control and one evidence source that does not share the same central assumption as the model. Describe the plausible observation that would invalidate the preferred conclusion. **Solution guidance:** compare equivalent service and independently qualified outputs.

### 7. Decision memo and reader challenge

Write a memo that separates observations from synthetic assumptions and proposes a reversible pilot with explicit stop criteria. A high-durability textile might reduce replacement production but still generate substantial shedding during use.

## Unit 4 capstone — challenge, calculation, evidence and choice

**Integrated case:** A mixed household-plastics stream contains incompatible polymers, pigments, food residue and multi-layer films. A packaging redesign could shift the balance among mechanical reprocessing, reuse and end-of-life leakage.

1. **Service definition and counterfactual.** Define the actual useful function and service horizon, identify the current material or process, and explain what product/service alternative is realistically available in the decision location. List safety and legal criteria that must be met before comparing optional environmental benefits.
2. **Mass, energy and quality ledger.** Construct a table of incoming material, recovered output, contaminants, rejects and inventory changes. Add the largest energy and water flows. Any unaccounted balance residual must be visibly labeled instead of silently treated as saleable recovered material.
3. **Two quantitative sensitivities.** Recalculate the unit's two interactive models. Change the default assumptions to two defensible adverse scenarios. Explain what is synthetic and what measurements would be needed to convert the question into a supplier-specific evaluation.
4. **Independent audit.** Design a sampling plan using **polymer identity and performance over cycles**, recording **track polymer fraction, additives, melt history, functional quality and generated rejects** and challenging the decision with **matched virgin controls, spectroscopy, rheology and mechanical testing**. Explain how many independent production batches, assets or user cycles are needed before generalization and how the result could be biased by rejected output.
5. **Decision and falsification.** Present a one-page recommendation with a go/no-go pilot, responsible decision-maker, estimated economic and environmental trade-offs, and a measurement that would overturn your recommendation. Specifically challenge **whether higher recovery lowers lifetime or increases leakage**. No safety-critical release or environmental certification is authorized by the classroom exercises.

### After the capstone

Discuss whether a reduction in impact *per service* is likely to translate into lower *total* resource use. A more efficient or more recyclable product can still be produced in expanding quantities, and a durable product can still create local harms if its manufacturing is poorly controlled. Document the supply chain and user context in which the conclusion holds. A coherent sustainability argument preserves engineering functionality, mass conservation, traceability and the limits of the available evidence at the same time.

