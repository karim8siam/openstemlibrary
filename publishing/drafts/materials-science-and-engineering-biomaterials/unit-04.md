# Unit 4: Biodegradation, resorption and controlled release

**Guiding research question:** What evidence connects a time-dependent mass change with retained function, products of degradation and exposure?

## Field context, scope and prerequisites

A degradable biomedical material must be understood as an evolving system. Molecular-weight loss, mass loss, strength loss, erosion and biological clearance are different observables. A slowly eroding specimen can lose strength early because chain scission precedes visible mass change. Local pH and biological chemistry alter hydrolysis; cells and enzymes complicate a simple stirred-bath experiment. Release kinetics cannot stand alone: drug identity and potency, total dose, byproducts and exposure location are outside a generic material-only slider.

The learning progression in **Biodegradation, resorption and controlled release** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Biodegradation, resorption and controlled release**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 4.1 — Bulk versus surface erosion

### Mechanism, technical vocabulary and equation

Hydrolyzable polymers may undergo bulk chain scission when water enters rapidly compared with bond cleavage, whereas surface erosion can arise when cleavage or surface processes outpace penetration. These descriptions are limiting regimes, not binary labels that remain fixed throughout product life. Crystallinity, specimen thickness, catalytic end groups and fluid renewal influence observations. A uniform mass-loss equation cannot describe local hollowing, autocatalysis or erosion fronts without additional spatial variables.

**Key relation.** A characteristic diffusion time τD≈L²/D can be compared with reaction time τR≈1/k; their ratio distinguishes transport-limited from reaction-limited tendencies.

### A specific design challenge

Imagine a thick resorbable rod and a thin film of the same polymer. Compare water penetration and chemical bond scission times, then propose sectioning and molecular-weight methods to identify the dominant regime.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative first-order remaining mass**, adjusts **Elapsed time**. Using the declared expression `100*Math.exp(-0.012*t)`, insert **40 days** to obtain **61.8783392 % remaining**. A controlled second input of **60 days** produces **48.6752256 % remaining**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-0.66015568 (% remaining)/(days)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Assumed effective rate 0.012 day^-1 for a declared mass population in well-controlled conditions; not a real hydrolysis or device-strength dataset. ### Measurement plan with independent controls

A defensible first investigation of **bulk versus surface erosion** uses **size-exclusion analysis and mass-loss assay** and records **molecular-weight distributions, fluid pH, strength retention and material balance**. Pair it with **chemical-product identification with a process blank and complete collection plan**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Visible disappearance is not evidence that all products were cleared, nor that mechanical safety was maintained throughout degradation.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **bulk versus surface erosion** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **61.878339 % remaining** and **48.675226 % remaining** from `100*Math.exp(-0.012*t)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **bulk versus surface erosion**, testing this lesson's claim while distinguishing **an early time point versus a later time point using independently prepared samples**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which observation would show that nominal surface erosion actually includes substantial bulk chain scission? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 4.2 — Hydrolysis, chain scission and autocatalysis

### Mechanism, technical vocabulary and equation

Esters and other labile bonds can cleave through reactions whose rates depend on local water content, temperature, pH and catalytic species. Simple first-order models predict exponential survival of a chosen chemical population under constant conditions, not the exact mechanical or mass state of a complex polymer. Acidic products trapped inside a thick specimen may accelerate internal degradation; therefore cross-sectional microstructure can differ from surface observations. Molecular-weight distributions often provide more informative early indicators than dry-mass measurements alone.

**Key relation.** For a specifically defined surviving fraction under constant effective rate k, f(t)=exp(−kt); the measured fraction must be declared before interpretation.

### A specific design challenge

Prepare a conceptual time-series for a degradable polymer disc in buffered solution. Compare number-average molecular weight, mass, compressive strength and fluid pH at each sampling time.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative reservoir release fraction**, adjusts **Elapsed time**. Using the declared expression `100*(1-Math.exp(-0.035*t))`, insert **30 days** to obtain **65.0062251 % released**. A controlled second input of **40 days** produces **75.3403036 % released**. Within these numerical bounds the output increases; the finite-difference sensitivity is **1.0334079 (% released)/(days)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Assumed well-mixed single-reservoir first-order rate 0.035 day^-1 and no burst; not a drug-release or dosing prediction. ### Measurement plan with independent controls

A defensible first investigation of **hydrolysis, chain scission and autocatalysis** uses **size-exclusion analysis and mass-loss assay** and records **molecular-weight distributions, fluid pH, strength retention and material balance**. Pair it with **chemical-product identification with a process blank and complete collection plan**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Fitting an exponential to mass data does not prove first-order chain scission kinetics. Quenching, drying, solvent extraction and buffer renewal can each modify the measured trajectory.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **hydrolysis, chain scission and autocatalysis** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **65.006225 % released** and **75.340304 % released** from `100*(1-Math.exp(-0.035*t))` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **hydrolysis, chain scission and autocatalysis**, testing this lesson's claim while distinguishing **a repeat measurement of one specimen versus an independently manufactured lot**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How could an autocatalytic interior be detected before visible fragmentation occurs? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_6 -->

## Lesson 4.3 — Drug release versus swelling and diffusion

### Mechanism, technical vocabulary and equation

Release systems can combine drug dissolution, partitioning, diffusion, swelling, matrix erosion and binding. Sink conditions are critical: a receiver medium near saturation can suppress apparent release even when the matrix has remaining mobile payload. A burst release may arise from surface-associated drug, cracks or loading heterogeneity. Fitting a single curve is not mechanistic proof. Independent swelling and degradation measurements, along with calibrated mass balance, are required to distinguish transport and reaction contributions.

**Key relation.** In a lumped well-mixed notional reservoir, released fraction F(t)=1−exp(−kt) with constant k and no initial burst; this is a teaching function only.

### A specific design challenge

Compare two synthetic reservoir-release curves with identical half-times but different early burst fractions. Design a sampling plan that would detect the difference without overinterpreting the curve.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative first-order remaining mass**, adjusts **Elapsed time**. Using the declared expression `100*Math.exp(-0.012*t)`, insert **80 days** to obtain **38.2892886 % remaining**. A controlled second input of **100 days** produces **30.1194212 % remaining**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-0.40849337 (% remaining)/(days)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Assumed effective rate 0.012 day^-1 for a declared mass population in well-controlled conditions; not a real hydrolysis or device-strength dataset. ### Measurement plan with independent controls

A defensible first investigation of **drug release versus swelling and diffusion** uses **size-exclusion analysis and mass-loss assay** and records **molecular-weight distributions, fluid pH, strength retention and material balance**. Pair it with **chemical-product identification with a process blank and complete collection plan**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A first-order reservoir model has no spatial concentration field and should not be presented as a predictive clinical dosing tool. Pharmaceutical release requires product-specific analytical and clinical evidence.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **drug release versus swelling and diffusion** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **38.289289 % remaining** and **30.119421 % remaining** from `100*Math.exp(-0.012*t)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **drug release versus swelling and diffusion**, testing this lesson's claim while distinguishing **a design input requirement compared against a physically measured acceptance criterion**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which early-time dataset would invalidate a single well-mixed exponential release hypothesis? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 4.4 — Strength retention, fatigue and evolving interfaces

### Mechanism, technical vocabulary and equation

A resorbable fixation construct should maintain function long enough for tissue processes to take over. Initial tensile strength, current stiffness, crack density and fatigue resistance need not decay at the same rate. Cyclic loading can amplify flaws while degradation changes geometry and microstructure. A safety analysis combines worst-reasonable loading, evolving defect populations, environmental media and the consequences of earlier-than-expected fragmentation. Animal-model or clinical success cannot be inferred from one accelerated soak test.

**Key relation.** For an illustrative monotonic retention function S(t)=S0 exp(−ks t), ks is a fitted effective loss rate, not a universally transferable material constant.

### A specific design challenge

For a degradable temporary fixation pin, propose a graph of load-carrying capacity over time and a separate uncertain healing-demand curve. Show how an apparently adequate initial margin can reverse mid-course.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative reservoir release fraction**, adjusts **Elapsed time**. Using the declared expression `100*(1-Math.exp(-0.035*t))`, insert **50 days** to obtain **82.6226057 % released**. A controlled second input of **60 days** produces **87.7543572 % released**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.51317515 (% released)/(days)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Assumed well-mixed single-reservoir first-order rate 0.035 day^-1 and no burst; not a drug-release or dosing prediction. ### Measurement plan with independent controls

A defensible first investigation of **strength retention, fatigue and evolving interfaces** uses **size-exclusion analysis and mass-loss assay** and records **molecular-weight distributions, fluid pH, strength retention and material balance**. Pair it with **chemical-product identification with a process blank and complete collection plan**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A dry-room mechanical test may overstate wet performance. Accelerated temperature tests can change mechanisms instead of merely making the same mechanism faster.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **strength retention, fatigue and evolving interfaces** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **82.622606 % released** and **87.754357 % released** from `100*(1-Math.exp(-0.035*t))` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **strength retention, fatigue and evolving interfaces**, testing this lesson's claim while distinguishing **an as-fabricated surface versus the identical material after the intended finishing process**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What observation would reveal that dry-mass loss and strength retention have become decoupled? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_7 -->

## Lesson 4.5 — Degradation products, clearance and risk

### Mechanism, technical vocabulary and equation

Degradation can release monomers, oligomers, ions, fillers and particles. Their amount, speciation and exposure pathway influence hazards; a small total mass may still warrant scrutiny when local concentrations are high. Chemical identity and product-specific toxicological assessment matter more than declaring a polymer 'bioresorbable'. Dissolved products, particulates and retained fragments should be considered separately, with a mass balance accounting for both receiver fluid and residual material. Qualification requires the relevant finished-device context and current regulatory expectations.

**Key relation.** Mass closure error δ=(minitial−mrecovered_all)/minitial can indicate missing pathways but does not alone identify chemical toxicity.

### A specific design challenge

Design a closed material-accounting worksheet for an eroding polymer composite: original mass, recovered solid, solution oligomers, dissolved ions and an unrecovered residual. Discuss independent analytical methods.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative first-order remaining mass**, adjusts **Elapsed time**. Using the declared expression `100*Math.exp(-0.012*t)`, insert **120 days** to obtain **23.6927759 % remaining**. A controlled second input of **140 days** produces **18.6373976 % remaining**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-0.25276891 (% remaining)/(days)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Assumed effective rate 0.012 day^-1 for a declared mass population in well-controlled conditions; not a real hydrolysis or device-strength dataset. ### Measurement plan with independent controls

A defensible first investigation of **degradation products, clearance and risk** uses **size-exclusion analysis and mass-loss assay** and records **molecular-weight distributions, fluid pH, strength retention and material balance**. Pair it with **chemical-product identification with a process blank and complete collection plan**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A 'complete disappearance' photograph is not proof of safe clearance; sample filtering can hide particles and extraction recovery may be incomplete.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **degradation products, clearance and risk** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **23.692776 % remaining** and **18.637398 % remaining** from `100*Math.exp(-0.012*t)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **degradation products, clearance and risk**, testing this lesson's claim while distinguishing **an early time point versus a later time point using independently prepared samples**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which additional characterization is required when dissolved-mass accounting fails despite apparently complete erosion? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 4 capstone — integrated design review

**Capstone setting.** Compare two hypothetical absorbable sutures under a common loading program, including strength decay, products, aqueous chemistry and uncertainties in accelerated testing.

1. **Define the device boundary.** For **biodegradation, resorption and controlled release**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **biodegradation, resorption and controlled release**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

