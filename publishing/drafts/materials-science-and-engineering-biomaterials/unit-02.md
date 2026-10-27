# Unit 2: Interfaces, proteins and host response

**Guiding research question:** What happens between first fluid contact and longer-term tissue responses at an engineered surface?

## Field context, scope and prerequisites

Surfaces are the first parts of a device encountered by fluid, proteins and cells. A nominally smooth solid quickly develops an adsorbed molecular layer whose composition and conformation can evolve. Cell adhesion may depend on which proteins are presented and how forces are transmitted through their bonds. A foreign-body response involves multiple cell populations and changes over time; it is not captured by a single cell-viability percentage. Distinguish adsorption kinetics, immune signaling, mechanical motion, infection risk and tissue organization. The models below illustrate transport and ideal occupancy only; they cannot predict clinical inflammation.

The learning progression in **Interfaces, proteins and host response** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Interfaces, proteins and host response**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 2.1 — Protein adsorption and dynamic exchange

### Mechanism, technical vocabulary and equation

Protein adsorption is competitive and dynamic. Molecules differ in concentration, affinity, orientation and propensity to unfold at interfaces. A protein-rich environment may exchange early adsorbates for others with different affinity or kinetic access; this is sometimes discussed as the Vroman effect under appropriate systems. Surface energy, charge, hydration and nanoroughness influence adsorption but rarely isolate it from solution chemistry. Surface-analytical evidence should identify which protein population was sampled and when, not infer an interfacial sequence from a single endpoint.

**Key relation.** Ideal single-species occupancy θ=KC/(1+KC) is useful for sensitivity but not a model of competitive plasma protein adsorption without additional species and kinetics.

### A specific design challenge

Expose two model surfaces to a hypothetical buffered albumin solution and to a mixed-protein surrogate. Sketch how occupancy and conformation could differ; define a time-series test capable of detecting exchange.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Idealized single-protein adsorption sites**, adjusts **Protein concentration**. Using the declared expression `100*(0.02*C)/(1+0.02*C)`, insert **33.333333 µg/mL** to obtain **40 % sites**. A controlled second input of **50 µg/mL** produces **50 % sites**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.6 (% sites)/(µg/mL)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Single protein, identical independent sites, illustrative K=0.02 mL/µg and fixed equilibrium; real biological fluids are competitive. ### Measurement plan with independent controls

A defensible first investigation of **protein adsorption and dynamic exchange** uses **surface spectroscopy and adsorption assays** and records **chemical composition, calibrated adsorption amount, contact time and medium**. Pair it with **appropriate blank solutions, time-series and orthogonal molecular characterization**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A Langmuir curve assumes identical independent sites and a single species; blood and interstitial fluids do not obey this simplification as a general law. The coverage slider is a mathematical contrast, not evidence that fouling has been prevented.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **protein adsorption and dynamic exchange** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **40 % sites** and **50 % sites** from `100*(0.02*C)/(1+0.02*C)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **protein adsorption and dynamic exchange**, testing this lesson's claim while distinguishing **an as-fabricated surface versus the identical material after the intended finishing process**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which measurement could distinguish conformational change from an increase in total protein mass? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 2.2 — Wetting, charge and hydration layers

### Mechanism, technical vocabulary and equation

Contact angle is a macroscopic probe of three-phase interactions. Dynamic wetting and hysteresis depend on surface roughness, chemistry, contamination and swelling. A hydrophilic surface may resist some non-specific adsorption by maintaining a hydration layer, but wettability alone does not prove reduced thrombosis, better integration or lower infection. Streaming potential, zeta potential and surface charge density are related but different observables. Measurements made on dry surfaces may not describe a fully hydrated polymer coating under shear.

**Key relation.** For an ideal smooth homogeneous nonreactive surface, Young's relation is γSV−γSL=γLV cosθ, with specified interfacial tensions and equilibrium assumptions.

### A specific design challenge

Compare two hydrogel-coated surfaces with similar apparent water contact angles but different charge and crosslink density. List additional probes needed to understand ionic adsorption and stability after sterilization.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Diffusive displacement near an interface**, adjusts **Diffusion time**. Using the declared expression `Math.sqrt(2*1e-11*t)*1e6`, insert **1220 s** to obtain **156.204994 µm RMS**. A controlled second input of **1616.6667 s** produces **179.814719 µm RMS**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.059520317 (µm RMS)/(s)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** 1D RMS displacement with constant D=10^-11 m²/s; no binding, convection, cells or chemical reaction. ### Measurement plan with independent controls

A defensible first investigation of **wetting, charge and hydration layers** uses **surface spectroscopy and adsorption assays** and records **chemical composition, calibrated adsorption amount, contact time and medium**. Pair it with **appropriate blank solutions, time-series and orthogonal molecular characterization**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not substitute one static contact angle for a complete surface chemical characterization. Rough and chemically heterogeneous materials can exhibit metastable angles and measurement-history dependence.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **wetting, charge and hydration layers** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **156.20499 µm RMS** and **179.81472 µm RMS** from `Math.sqrt(2*1e-11*t)*1e6` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **wetting, charge and hydration layers**, testing this lesson's claim while distinguishing **an early time point versus a later time point using independently prepared samples**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How could surface roughness reverse the interpretation of a single apparent contact angle measurement? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_2 -->

## Lesson 2.3 — Cell adhesion and the extracellular matrix

### Mechanism, technical vocabulary and equation

Anchorage-dependent cells often interact with surfaces through adsorbed extracellular-matrix proteins and receptor complexes such as integrins. Ligand presentation, steric access, nanoscale spacing and mechanical resistance affect signaling and spreading. Cell attachment count is not equivalent to differentiation or function. Surface treatments may increase adhesive ligands while also altering degradation or fouling. Live imaging, cell-type-specific markers and appropriately selected controls are needed to distinguish initial adhesion from sustained phenotypic response.

**Key relation.** Projected cell area A≈πr² is a geometric image approximation when a measured cell outline is replaced by an equivalent circle; it is not a mechanistic predictor of adhesion.

### A specific design challenge

A coating increases the number of adherent cells after four hours. Plan an assay matrix assessing cell number, area, viability and functional markers over several time points, including a bare-substrate control.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Idealized single-protein adsorption sites**, adjusts **Protein concentration**. Using the declared expression `100*(0.02*C)/(1+0.02*C)`, insert **66.666667 µg/mL** to obtain **57.1428571 % sites**. A controlled second input of **83.333333 µg/mL** produces **62.5 % sites**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.32142857 (% sites)/(µg/mL)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Single protein, identical independent sites, illustrative K=0.02 mL/µg and fixed equilibrium; real biological fluids are competitive. ### Measurement plan with independent controls

A defensible first investigation of **cell adhesion and the extracellular matrix** uses **surface spectroscopy and adsorption assays** and records **chemical composition, calibrated adsorption amount, contact time and medium**. Pair it with **appropriate blank solutions, time-series and orthogonal molecular characterization**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A dramatic fluorescence image can result from different seeding densities, staining efficiency or image thresholding. Avoid extrapolating one in-vitro cell line to host integration.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **cell adhesion and the extracellular matrix** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **57.142857 % sites** and **62.5 % sites** from `100*(0.02*C)/(1+0.02*C)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **cell adhesion and the extracellular matrix**, testing this lesson's claim while distinguishing **a repeat measurement of one specimen versus an independently manufactured lot**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which blinded image-analysis or independent marker would test whether an apparent adhesion increase is genuine? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 2.4 — Inflammation and foreign-body reaction

### Mechanism, technical vocabulary and equation

An implanted material can trigger damage responses, protein deposition, immune-cell recruitment, macrophage phenotypes, fibroblast activation and matrix remodeling. Outcomes depend on implant size, shape, motion, chemistry, debris, contamination and location. A fibrous capsule can be a measured histological feature, not necessarily a simple binary success or failure. Temporal data are essential: acute inflammatory signaling may be followed by resolution or persistent stimulation. Cell-based cytokine assays complement but do not replace more comprehensive biological evaluations.

**Key relation.** A response time course can be described descriptively by normalized signal S(t); no universal rate equation predicts individual host immune responses from surface chemistry alone.

### A specific design challenge

Design a hypothetical longitudinal study of a soft implant interface. Define time points, blinded histology variables, controls for incision trauma and a plan to separate sterile inflammation from infection.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Diffusive displacement near an interface**, adjusts **Diffusion time**. Using the declared expression `Math.sqrt(2*1e-11*t)*1e6`, insert **2013.3333 s** to obtain **200.665559 µm RMS**. A controlled second input of **2410 s** produces **219.544984 µm RMS**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.047595188 (µm RMS)/(s)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** 1D RMS displacement with constant D=10^-11 m²/s; no binding, convection, cells or chemical reaction. ### Measurement plan with independent controls

A defensible first investigation of **inflammation and foreign-body reaction** uses **surface spectroscopy and adsorption assays** and records **chemical composition, calibrated adsorption amount, contact time and medium**. Pair it with **appropriate blank solutions, time-series and orthogonal molecular characterization**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Labeling a macrophage population as exclusively 'good M2' or 'bad M1' oversimplifies state diversity. A single inflammatory marker cannot establish the overall safety of a device.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **inflammation and foreign-body reaction** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **200.66556 µm RMS** and **219.54498 µm RMS** from `Math.sqrt(2*1e-11*t)*1e6` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **inflammation and foreign-body reaction**, testing this lesson's claim while distinguishing **a design input requirement compared against a physically measured acceptance criterion**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Give an observation that would falsify the claim that a coating has reduced chronic inflammation. A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_3 -->

## Lesson 2.5 — Biological evaluation by contact and risk

### Mechanism, technical vocabulary and equation

Biological evaluation links the finished device's contact type, duration, materials and manufacturing hazards to appropriate endpoints. Literature history, chemical characterization and testing can all contribute, but no universal checklist makes every device safe. The FDA's September 2023 guidance clarifies a risk-based interpretation of ISO 10993-1; ISO 10993-1:2025 has partial U.S. FDA recognition and a transition from the 2018 edition through July 1, 2029 for the older declaration route. These are snapshots, not a substitute for checking current recognized standards and product-specific requirements. Treat risk-based evaluation as a documented scientific argument.

**Key relation.** Exposure depends on mass released, duration, contacting tissue and physiology; a hazard quotient is meaningful only with justified toxicological benchmarks and exposure assumptions.

### A specific design challenge

Compare an intact-skin sensor worn intermittently with a permanent blood-contacting implant. Construct two separate evidence maps and highlight why the latter may require attention to hemocompatibility and chronic exposure.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Idealized single-protein adsorption sites**, adjusts **Protein concentration**. Using the declared expression `100*(0.02*C)/(1+0.02*C)`, insert **100 µg/mL** to obtain **66.6666667 % sites**. A controlled second input of **116.66667 µg/mL** produces **70 % sites**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.2 (% sites)/(µg/mL)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Single protein, identical independent sites, illustrative K=0.02 mL/µg and fixed equilibrium; real biological fluids are competitive. ### Measurement plan with independent controls

A defensible first investigation of **biological evaluation by contact and risk** uses **surface spectroscopy and adsorption assays** and records **chemical composition, calibrated adsorption amount, contact time and medium**. Pair it with **appropriate blank solutions, time-series and orthogonal molecular characterization**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A test labeled 'non-cytotoxic' does not alone establish implantation safety or address all leachables and degradation products. A successful research assay is not an FDA authorization.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **biological evaluation by contact and risk** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **66.666667 % sites** and **70 % sites** from `100*(0.02*C)/(1+0.02*C)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **biological evaluation by contact and risk**, testing this lesson's claim while distinguishing **an as-fabricated surface versus the identical material after the intended finishing process**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What evidence about a changed sterilization process would trigger revisiting an existing biological risk assessment? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 2 capstone — integrated design review

**Capstone setting.** Propose a comparison of two hypothetical catheter coatings. Separate adsorbed-protein results, flow-condition measurements, chemical release and biological safety endpoints.

1. **Define the device boundary.** For **interfaces, proteins and host response**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **interfaces, proteins and host response**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

