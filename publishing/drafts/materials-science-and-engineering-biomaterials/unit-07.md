# Unit 7: Tissue engineering scaffolds and bioprinting

**Guiding research question:** How should architecture, transport, cells and manufacturing reproducibility be evaluated without equating cell survival with organ function?

## Field context, scope and prerequisites

Tissue engineering combines cells, material architecture, signals and a delivery context. Scaffold geometry may support transport and cell attachment, but neither guarantees tissue maturation. Perfusion, oxygen gradients, mechanical loading, biochemical factors and contamination all affect engineered constructs. A bioprinted structure must be judged after printing and conditioning, not solely from its intended digital geometry. Simple transport sliders reveal why thickness and perfusion matter, but do not predict cell fate or successful implantation.

The learning progression in **Tissue engineering scaffolds and bioprinting** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Tissue engineering scaffolds and bioprinting**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 7.1 — Pore architecture, connectivity and tortuosity

### Mechanism, technical vocabulary and equation

Scaffold porosity influences accessible volume, permeability, cell seeding, nutrient transport and mechanical stiffness. Equivalent pore diameter alone does not specify connected pathways or tortuosity. A network with large pores connected by narrow throats may have different flow resistance than one with uniform open channels. Surface roughness and chemistry further affect fluid wetting and protein conditioning. Quantitative characterization needs specimen-scale statistics rather than a single representative cross section.

**Key relation.** Darcy's law Q=−(kA/μ)(ΔP/L) defines permeability k for a suitable continuum porous-flow regime; sign depends on gradient convention.

### A specific design challenge

Compare a lattice made with straight-through channels and one with tortuous interconnected pores at equal solid fraction. Design micro-CT segmentation checks and a tracer-transport experiment.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **1D oxygen-like molecule diffusion distance**, adjusts **Elapsed time**. Using the declared expression `Math.sqrt(2*2e-9*t)*1e6`, insert **200.77778 s** to obtain **896.164667 µm RMS**. A controlled second input of **300.66667 s** produces **1096.6616 µm RMS**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.0071996 (µm RMS)/(s)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Constant D=2×10^-9 m²/s, one dimension, diffusion without cellular consumption, boundary loss or reaction; not oxygen sufficiency. ### Measurement plan with independent controls

A defensible first investigation of **pore architecture, connectivity and tortuosity** uses **micro-CT and tracer microscopy** and records **connected pore throat distributions, diffusional/convective transport and batch identity**. Pair it with **wet dimensional measurement, controlled perfusion and spatial biological sampling**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Apparent permeability inferred from one high-pressure point may reflect scaffold deformation. An imaging-derived pore network must be validated against actual flow accessibility.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **pore architecture, connectivity and tortuosity** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **896.16467 µm RMS** and **1096.6616 µm RMS** from `Math.sqrt(2*2e-9*t)*1e6` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **pore architecture, connectivity and tortuosity**, testing this lesson's claim while distinguishing **an apparent favorable result compared against its most plausible competing explanation**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What combination of imaging and tracer observation can show that a visually open pore is functionally blocked? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 7.2 — Oxygen diffusion and consumption

### Mechanism, technical vocabulary and equation

Cells consume dissolved oxygen while transport supplies it by diffusion or convection. As construct thickness grows, concentration gradients can form even when the outside medium is well supplied. A single diffusion length is a dimensional estimate; realistic oxygen profiles require uptake laws, boundary concentrations, geometry and possibly vascular or perfusion pathways. Oxygen tension, cell density and phenotype may vary spatially. A fluorescent viability stain can miss metabolic heterogeneity or transient stress.

**Key relation.** The root-mean-square diffusion distance in one Cartesian direction is ℓrms=sqrt(2Dt) for constant D and no consumption; with reaction, solve a reaction–diffusion model.

### A specific design challenge

Sketch oxygen profiles for a thin cell-free gel, a thick cell-free gel and a thick densely seeded gel. Specify sensor locations and a negative control.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Porosity-based permeability geometry factor**, adjusts **Void fraction**. Using the declared expression `Math.pow(e,3)/Math.pow(1-e,2)`, insert **0.38333333 fraction** to obtain **0.148125152 relative**. A controlled second input of **0.46111111 fraction** produces **0.337612333 relative**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4362638 (relative)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Kozeny-type geometric trend ε³/(1−ε)² without scale or tortuosity; not absolute permeability or cell-infiltration proof. ### Measurement plan with independent controls

A defensible first investigation of **oxygen diffusion and consumption** uses **micro-CT and tracer microscopy** and records **connected pore throat distributions, diffusional/convective transport and batch identity**. Pair it with **wet dimensional measurement, controlled perfusion and spatial biological sampling**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not infer adequate oxygenation from a diffusive RMS distance alone; it omits consumption, boundary depletion and time-dependent medium replacement.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **oxygen diffusion and consumption** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **0.14812515 relative** and **0.33761233 relative** from `Math.pow(e,3)/Math.pow(1-e,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **oxygen diffusion and consumption**, testing this lesson's claim while distinguishing **water-saturated versus dry specimens under the same nominal load**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which spatially resolved measurement could refute a homogeneous-concentration approximation? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_12 -->

## Lesson 7.3 — Mechanotransduction and culture loading

### Mechanism, technical vocabulary and equation

Cell signaling can respond to substrate stiffness, stress relaxation, adhesion-ligand mechanics and applied cyclic strain. Distinct cell types and differentiation states respond differently, so there is no universal function mapping scaffold modulus to cell fate. In a 3D construct, nominal external strain may not equal local cell strain because of pore geometry, fluid flow and nonuniform load sharing. Document frequency, amplitude, duty cycle, hydration and time relative to imaging or marker analysis.

**Key relation.** In a simplified linear continuum, local nominal stress σ≈E ε, but in 3D cells experience a nonuniform tensor field, not a universal scalar substrate signal.

### A specific design challenge

Compare a dynamic-loading culture with an unloaded control. Define a matrix of substrate modulus, cyclic strain and biological readouts that avoids confounding loading with oxygen delivery.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **1D oxygen-like molecule diffusion distance**, adjusts **Elapsed time**. Using the declared expression `Math.sqrt(2*2e-9*t)*1e6`, insert **400.55556 s** to obtain **1265.78917 µm RMS**. A controlled second input of **500.44444 s** produces **1414.84196 µm RMS**. Within these numerical bounds the output increases; the finite-difference sensitivity is **1.4921859 (µm RMS)/(s)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Constant D=2×10^-9 m²/s, one dimension, diffusion without cellular consumption, boundary loss or reaction; not oxygen sufficiency. ### Measurement plan with independent controls

A defensible first investigation of **mechanotransduction and culture loading** uses **micro-CT and tracer microscopy** and records **connected pore throat distributions, diffusional/convective transport and batch identity**. Pair it with **wet dimensional measurement, controlled perfusion and spatial biological sampling**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not interpret greater cell spreading as automatic evidence of enhanced tissue function. Injury-related signaling can accompany a visually organized actin cytoskeleton.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **mechanotransduction and culture loading** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **1265.7892 µm RMS** and **1414.842 µm RMS** from `Math.sqrt(2*2e-9*t)*1e6` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **mechanotransduction and culture loading**, testing this lesson's claim while distinguishing **a small versus large geometry with equal bulk chemical composition**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How could changed perfusion rather than direct mechanical sensing explain a loading-response difference? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 7.4 — Bioprinting, extrusion and shape fidelity

### Mechanism, technical vocabulary and equation

Bioink composition must balance flow during dispensing, shape retention, cell compatibility and crosslinking after placement. Shear-thinning or yield stress can make materials extrudable, but nozzle geometry and residence time can introduce stress or damage. A printed filament's actual width may differ from the CAD path due to swelling, spreading and crosslink dynamics. Sterility, crosslink reagent exposure and batch-to-batch cell properties make manufacturing repeatability challenging. Establish process windows empirically rather than assuming one printer setting transfers across materials.

**Key relation.** For a deposited filament with volume rate Q and stage speed v, nominal cross-sectional area A≈Q/v when deposition is continuous with negligible swelling and loss.

### A specific design challenge

A notional hydrogel ink yields fine lines at low flow but broad filaments at higher flow. Propose a design of experiments varying nozzle diameter and printing speed while recording post-cure geometry.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Porosity-based permeability geometry factor**, adjusts **Void fraction**. Using the declared expression `Math.pow(e,3)/Math.pow(1-e,2)`, insert **0.53888889 fraction** to obtain **0.736014742 relative**. A controlled second input of **0.61666667 fraction** produces **1.59587272 relative**. Within these numerical bounds the output increases; the finite-difference sensitivity is **11.055317 (relative)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Kozeny-type geometric trend ε³/(1−ε)² without scale or tortuosity; not absolute permeability or cell-infiltration proof. ### Measurement plan with independent controls

A defensible first investigation of **bioprinting, extrusion and shape fidelity** uses **micro-CT and tracer microscopy** and records **connected pore throat distributions, diffusional/convective transport and batch identity**. Pair it with **wet dimensional measurement, controlled perfusion and spatial biological sampling**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A successful empty-cell extrusion pattern does not prove acceptable survival or phenotype after including cells. An immediate viability measurement misses delayed effects.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **bioprinting, extrusion and shape fidelity** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **0.73601474 relative** and **1.5958727 relative** from `Math.pow(e,3)/Math.pow(1-e,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **bioprinting, extrusion and shape fidelity**, testing this lesson's claim while distinguishing **a surface-only measurement versus a bulk-sensitive characterization**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which measurement made after 24 hours could reveal poor shape fidelity that is invisible immediately after deposition? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_13 -->

## Lesson 7.5 — Reproducibility and preclinical boundaries

### Mechanism, technical vocabulary and equation

Scaffold studies require provenance for cell sources, passage numbers, matrix batches, donor variability and analytical endpoints. Independent biological replicates differ from repeated microscope fields taken from the same construct. Claims about regenerative benefit depend on controlled biological outcomes, not just material compatibility or static histology. Translational steps add manufacturing under quality systems, clinical indications, risk management and applicable oversight. Quantitative reporting should separate clearly specified research findings from candidate applications.

**Key relation.** For independent replicates xi, sample mean x̄=Σxi/n and standard error s/√n summarize the chosen endpoint only when the replicate unit is defensible.

### A specific design challenge

Develop a reporting checklist for three hypothetical bioprinted scaffold batches, with independent samples, geometry, oxygen maps, compression testing and cell phenotype readouts.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **1D oxygen-like molecule diffusion distance**, adjusts **Elapsed time**. Using the declared expression `Math.sqrt(2*2e-9*t)*1e6`, insert **600.33333 s** to obtain **1549.62361 µm RMS**. A controlled second input of **700.22222 s** produces **1673.58564 µm RMS**. Within these numerical bounds the output increases; the finite-difference sensitivity is **1.2409992 (µm RMS)/(s)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Constant D=2×10^-9 m²/s, one dimension, diffusion without cellular consumption, boundary loss or reaction; not oxygen sufficiency. ### Measurement plan with independent controls

A defensible first investigation of **reproducibility and preclinical boundaries** uses **micro-CT and tracer microscopy** and records **connected pore throat distributions, diffusional/convective transport and batch identity**. Pair it with **wet dimensional measurement, controlled perfusion and spatial biological sampling**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not label a laboratory demonstration an implant-ready tissue substitute. Batch homogeneity at the printer setting level is not biological reproducibility.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **reproducibility and preclinical boundaries** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **1549.6236 µm RMS** and **1673.5856 µm RMS** from `Math.sqrt(2*2e-9*t)*1e6` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **reproducibility and preclinical boundaries**, testing this lesson's claim while distinguishing **an apparent favorable result compared against its most plausible competing explanation**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What constitutes an independent replicate in a scaffold seeded with cells from one donor? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 7 capstone — integrated design review

**Capstone setting.** Compare a perfused, bioprinted 3D scaffold with a static-culture construct. Develop separate mechanical, transport, cell and manufacturing evidence tables.

1. **Define the device boundary.** For **tissue engineering scaffolds and bioprinting**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **tissue engineering scaffolds and bioprinting**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

