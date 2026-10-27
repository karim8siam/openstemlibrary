# Unit 1: Biomaterial selection and structure–property relationships

**Guiding research question:** How do composition, architecture, loading and intended tissue contact define a useful biomaterial rather than merely a familiar substance?

## Field context, scope and prerequisites

A biomaterial may be a metal, ceramic, polymer, composite or living-material hybrid engineered to interact with a biological system for a specified purpose. The same chemical composition may be acceptable in one short-duration application and unsuitable in another. Design begins with the product and exposure scenario: an external dressing, a blood-contacting catheter, a temporary resorbable fixture and a load-bearing permanent implant impose different constraints. Mechanical strength alone does not establish safety; chemical extractables, particulate debris, corrosion, sterilization, shelf life and the tissue environment also matter. Use a multi-criteria requirement matrix instead of assuming that any single 'biocompatible material' will be universally compatible.

The learning progression in **Biomaterial selection and structure–property relationships** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Biomaterial selection and structure–property relationships**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 1.1 — Definitions, intended use and boundary conditions

### Mechanism, technical vocabulary and equation

The word biomaterial describes a function and context, not a single composition. Distinguish a bulk material property such as tensile modulus from a finished device characteristic such as fatigue life under physiological loading. An implant has geometry, coatings, joining methods, a manufacturing history, packaging and clinical use conditions. Even an apparently inert surface changes after adsorption of proteins and ionic species. Appropriate material choice depends on where it contacts the body, for how long, under what mechanical load, and what biological hazards can reasonably arise.

**Key relation.** A requirements vector can be written R=(contact category, duration, stress state, exposure chemistry, sterilization method, failure consequences); it is not reducible to one scalar score.

### A specific design challenge

Compare a silicone skin-contact pad and a silicone component on a long-term blood-contacting circuit. They can share monomer chemistry while differing in extraction requirements, platelet interactions, surface finish and evidence expected for a finished device.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Uniaxial linear-elastic stress**, adjusts **Engineering strain**. Using the declared expression `2000*eps`, insert **0.011888889 dimensionless** to obtain **23.7777778 MPa**. A controlled second input of **0.017333333 dimensionless** produces **34.6666667 MPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2000 (MPa)/(dimensionless)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Illustrative E=2 GPa, small-strain isotropic homogeneous solid; not living tissue, fatigue or a full implant stress model. ### Measurement plan with independent controls

A defensible first investigation of **definitions, intended use and boundary conditions** uses **tensile/compression testing with hydrated replicates** and records **stress–strain curve, specimen dimensions, loading rate and dry/wet state**. Pair it with **process-matched geometry, imaging of fracture surfaces and independent batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A trade-name polymer or 'medical grade' description does not establish biological safety of the actual finished item. A test coupon lacking adhesive, pigments, processing residues or sterilization history may be unrepresentative.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **definitions, intended use and boundary conditions** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **23.777778 MPa** and **34.666667 MPa** from `2000*eps` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **definitions, intended use and boundary conditions**, testing this lesson's claim while distinguishing **water-saturated versus dry specimens under the same nominal load**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Specify what evidence would change the initial material ranking after the intended contact site is revised. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 1.2 — Elasticity and mismatch with soft or hard tissues

### Mechanism, technical vocabulary and equation

Young's modulus relates uniaxial engineering stress to strain in a small-strain elastic regime. Tissue response is often anisotropic, viscoelastic and nonlinear; a single tissue modulus is therefore an approximation tied to a protocol. High stiffness can help maintain shape but concentrate load at an interface, while excessive compliance may permit buckling or migration. For porous structures, modulus depends on relative density, pore topology and strut deformation, not simply chemistry. Compare stress relaxation, cyclic response and rate dependence before inferring service performance.

**Key relation.** In linear uniaxial elasticity σ=E ε for a specified region; apparent compressive modulus of an open-cell scaffold may scale as E*/Es≈C(ρ*/ρs)^n under a chosen architecture.

### A specific design challenge

A rigid fixation component produces a different strain field than surrounding bone. Estimate the load-sharing trend in a simplified parallel-element calculation, then describe why biological remodeling and interface slip defeat a homogeneous-bar model.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Open-cell porosity–modulus scaling**, adjusts **Pore volume fraction**. Using the declared expression `2000*Math.pow(1-p,2)`, insert **0.26666667 fraction** to obtain **1075.55556 MPa**. A controlled second input of **0.35555556 fraction** produces **830.617284 MPa**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-2755.5556 (MPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Power-law teaching approximation E*=Es(1-p)^2, Es=2 GPa, prefactor unity; not fitted to a real scaffold or proven connectivity. ### Measurement plan with independent controls

A defensible first investigation of **elasticity and mismatch with soft or hard tissues** uses **tensile/compression testing with hydrated replicates** and records **stress–strain curve, specimen dimensions, loading rate and dry/wet state**. Pair it with **process-matched geometry, imaging of fracture surfaces and independent batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A low mismatch in catalog moduli alone does not guarantee integration, reduced pain or absence of local tissue response. Apparent modulus depends on hydration, orientation, loading rate and test method.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **elasticity and mismatch with soft or hard tissues** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **1075.5556 MPa** and **830.61728 MPa** from `2000*Math.pow(1-p,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **elasticity and mismatch with soft or hard tissues**, testing this lesson's claim while distinguishing **a small versus large geometry with equal bulk chemical composition**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Name one measurement showing that the assumed linear elastic region no longer applies. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_0 -->

## Lesson 1.3 — Metals, ceramics, polymers and composites

### Mechanism, technical vocabulary and equation

Metals offer electrical and thermal conductivity, toughness and possible corrosion issues; ceramics can provide hardness, chemical stability or bioactive interactions but may be brittle; polymers span flexible, viscoelastic and degradable classes; composites combine constituents with interfaces that introduce their own failure modes. Avoid assigning a material family one universal biocompatibility ranking. Titanium alloy fixation, alumina articulation, polyethylene bearings and hydrogel dressings solve distinct sets of mechanical and chemical problems. Composition, microstructure and finishing processes modify each family's behavior.

**Key relation.** For an ideal aligned two-phase composite loaded parallel to the phases, E_parallel=φE1+(1−φ)E2; this upper-bound simplification is not a measured scaffold modulus.

### A specific design challenge

Select candidate families for a hypothetical non-load-bearing porous spacer and for a high-cycle joint-bearing component; record which criteria cannot be decided without device geometry and testing.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Uniaxial linear-elastic stress**, adjusts **Engineering strain**. Using the declared expression `2000*eps`, insert **0.022777778 dimensionless** to obtain **45.5555556 MPa**. A controlled second input of **0.028222222 dimensionless** produces **56.4444444 MPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2000 (MPa)/(dimensionless)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Illustrative E=2 GPa, small-strain isotropic homogeneous solid; not living tissue, fatigue or a full implant stress model. ### Measurement plan with independent controls

A defensible first investigation of **metals, ceramics, polymers and composites** uses **tensile/compression testing with hydrated replicates** and records **stress–strain curve, specimen dimensions, loading rate and dry/wet state**. Pair it with **process-matched geometry, imaging of fracture surfaces and independent batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

The phrase 'ceramic is inert' can conceal wear debris, ion exchange and surface changes. Likewise, 'polymer is soft' is not a quantitative descriptor of creep, residual additives or fatigue.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **metals, ceramics, polymers and composites** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **45.555556 MPa** and **56.444444 MPa** from `2000*eps` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **metals, ceramics, polymers and composites**, testing this lesson's claim while distinguishing **a surface-only measurement versus a bulk-sensitive characterization**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Explain how reversing the loading direction can invalidate a rule-of-mixtures estimate. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 1.4 — Porosity, surface finish and manufacturing defects

### Mechanism, technical vocabulary and equation

Pore fraction controls transport space, structural connectivity and often effective stiffness. Porosity needs a definition: open, closed and total pores may differ, while 'average pore size' can hide a broad distribution with blocked throats. A polished bearing and a roughened bone-facing surface may require opposite topography goals. Process-induced voids, inclusions, residual stress and unbonded layers can dominate fatigue performance despite good average bulk material data. Quantitative microscopy and nondestructive inspection must specify resolution and sampling.

**Key relation.** For dry mass m, true solid density ρs and external envelope volume V, total porosity estimate ε=1−m/(ρs V), assuming no adsorbed fluids or composition ambiguity.

### A specific design challenge

Compare two nominally 65% porous scaffolds: one with disconnected pores and another with interconnected channels. Predict differences in flow access, permeability and compressive properties without claiming identical cell behavior.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Open-cell porosity–modulus scaling**, adjusts **Pore volume fraction**. Using the declared expression `2000*Math.pow(1-p,2)`, insert **0.44444444 fraction** to obtain **617.283951 MPa**. A controlled second input of **0.53333333 fraction** produces **435.555556 MPa**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-2044.4444 (MPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Power-law teaching approximation E*=Es(1-p)^2, Es=2 GPa, prefactor unity; not fitted to a real scaffold or proven connectivity. ### Measurement plan with independent controls

A defensible first investigation of **porosity, surface finish and manufacturing defects** uses **tensile/compression testing with hydrated replicates** and records **stress–strain curve, specimen dimensions, loading rate and dry/wet state**. Pair it with **process-matched geometry, imaging of fracture surfaces and independent batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Geometric porosity is not the same as fluid accessibility, and a nominal additive-manufacturing toolpath is not proof of realized pore connectivity.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **porosity, surface finish and manufacturing defects** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **617.28395 MPa** and **435.55556 MPa** from `2000*Math.pow(1-p,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **porosity, surface finish and manufacturing defects**, testing this lesson's claim while distinguishing **an apparent favorable result compared against its most plausible competing explanation**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Propose a destructive and a nondestructive method that can detect an invisible internal pore blockage. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_1 -->

## Lesson 1.5 — Design trade-offs and failure-mode prioritization

### Mechanism, technical vocabulary and equation

A material decision should make risks explicit before optimization. For load-bearing parts, consider peak and cyclic stresses, crack growth, wear and interface stability. For degradable devices, strength retention versus healing time may be more important than initial strength. Exposure chemistry, swelling, enzymatic cleavage and patient variability introduce uncertainty beyond static bench tests. Design controls should connect each requirement to measurable acceptance criteria, a verification test and an escalation rule when results deviate. Reject the idea that a single numerical 'biocompatibility score' can settle all these questions.

**Key relation.** For a simplified uniaxial element with allowable stress σallow and computed stress σmax, factor of safety N=σallow/σmax; defining σallow and the load distribution is the hard part.

### A specific design challenge

Build a risk table for a temporary porous bone filler. Include a wrong pore-size distribution, brittle strut fracture, process contamination, excessive degradation and an out-of-spec packaging seal. Rank by justified severity and available evidence rather than arbitrary total scores.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Uniaxial linear-elastic stress**, adjusts **Engineering strain**. Using the declared expression `2000*eps`, insert **0.033666667 dimensionless** to obtain **67.3333333 MPa**. A controlled second input of **0.039111111 dimensionless** produces **78.2222222 MPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2000 (MPa)/(dimensionless)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Illustrative E=2 GPa, small-strain isotropic homogeneous solid; not living tissue, fatigue or a full implant stress model. ### Measurement plan with independent controls

A defensible first investigation of **design trade-offs and failure-mode prioritization** uses **tensile/compression testing with hydrated replicates** and records **stress–strain curve, specimen dimensions, loading rate and dry/wet state**. Pair it with **process-matched geometry, imaging of fracture surfaces and independent batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A high calculated safety factor against monotonic yield does not ensure fatigue, biological safety, wear resistance or secure fixation under clinical use.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **design trade-offs and failure-mode prioritization** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **67.333333 MPa** and **78.222222 MPa** from `2000*eps` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **design trade-offs and failure-mode prioritization**, testing this lesson's claim while distinguishing **water-saturated versus dry specimens under the same nominal load**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** State two failure modes that could appear even when factor of safety exceeds two. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 1 capstone — integrated design review

**Capstone setting.** Specify a hypothetical external wearable support versus an implanted fixation system. Write different requirement tables and explain why no single material family is categorically best.

1. **Define the device boundary.** For **biomaterial selection and structure–property relationships**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **biomaterial selection and structure–property relationships**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

