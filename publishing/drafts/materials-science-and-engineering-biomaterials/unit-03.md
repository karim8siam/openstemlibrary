# Unit 3: Hydrogels, soft biomaterials and rheology

**Guiding research question:** How do polymer networks support mechanical function, hydration and transport without treating the hydrogel as homogeneous water?

## Field context, scope and prerequisites

Hydrogels are crosslinked polymer networks containing substantial water, but their mechanics and transport cannot be inferred from water content alone. Network topology, ionization, polymer-solvent interactions, mesh size and crosslink lifetimes affect swelling, permeability and stress relaxation. Chemical crosslinking differs from reversible physical associations. Biological use adds constraints on extractables, residual initiators, fragility, dehydration and sterilization. Simple network models reveal trends only when chain elasticity and ideal mixing assumptions hold.

The learning progression in **Hydrogels, soft biomaterials and rheology** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Hydrogels, soft biomaterials and rheology**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 3.1 — Crosslink density and small-strain elasticity

### Mechanism, technical vocabulary and equation

An ideal elastomeric network gains elastic resistance from constrained polymer-chain conformations. In an affine or phantom network approximation, shear modulus can scale with the density of elastically active chains and thermal energy, but real hydrogels include dangling ends, entanglements and inhomogeneous crosslinks. Modulus measured by shear rheometry or compression depends on frequency, geometry and solvent exchange. A stiffer network may alter diffusion and swelling; it is not necessarily stronger under tear, cyclic fatigue or puncture.

**Key relation.** In an ideal entropic network, G≈νRT when ν is the molar density of elastically active chains per m³; the prefactor depends on network model.

### A specific design challenge

Make two networks with the same polymer chemistry but differing crosslink densities. Predict storage modulus and qualitative swelling tendencies, while identifying possible changes in defect concentration.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal hydrogel network shear modulus**, adjusts **Active-chain molar density**. Using the declared expression `nu*8.314462618*298/1000`, insert **23 mol/m³** to obtain **56.9873268 kPa**. A controlled second input of **34 mol/m³** produces **84.2421352 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4777099 (kPa)/(mol/m³)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Ideal network G=νRT at T=298 K; dangling strands, phantom-network correction, entanglement, swelling and nonlinear strain omitted. ### Measurement plan with independent controls

A defensible first investigation of **crosslink density and small-strain elasticity** uses **oscillatory rheometry and swelling gravimetry** and records **G prime, G double-prime, equilibrium ratio, sample thickness and solvent chemistry**. Pair it with **creep or relaxation assay with wall-slip control and independent network chemistry**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not infer molecular mesh size exactly from one modulus unless the network model and solvent state are supported. Loss modulus is not interchangeable with storage modulus.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **crosslink density and small-strain elasticity** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **56.987327 kPa** and **84.242135 kPa** from `nu*8.314462618*298/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **crosslink density and small-strain elasticity**, testing this lesson's claim while distinguishing **a small versus large geometry with equal bulk chemical composition**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which frequency-dependent rheology result could signal that the purely elastic approximation is incomplete? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 3.2 — Swelling thermodynamics and osmotic stress

### Mechanism, technical vocabulary and equation

Water uptake is a competition between polymer-solvent mixing, ion osmotic pressure and network elasticity. Charged gels may swell strongly at low ionic strength and collapse when screening grows, depending on chemistry and pH. The mass swelling ratio and volume swelling ratio differ when polymer and fluid densities differ. Boundary constraints can create appreciable stresses and nonuniform swelling. Comparing two formulations requires equilibration time, medium composition, specimen geometry and a precise drying protocol.

**Key relation.** An ideal dilute solute contribution Π≈cRT has pressure units when c is mol/m³, R is J/(mol K), and T is K; actual gel swelling needs additional terms.

### A specific design challenge

A hydrogel patch swells in deionized water but less in physiological saline surrogate. Build a falsifiable explanation using charge screening and determine what independent chemical measurements are needed.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Dilute solution osmotic pressure**, adjusts **Solute concentration**. Using the declared expression `c*8.314462618*298/1000`, insert **34 mol/m³** to obtain **84.2421352 kPa**. A controlled second input of **45 mol/m³** produces **111.496944 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4777099 (kPa)/(mol/m³)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Ideal van’t Hoff Π=cRT at T=298 K; gel elasticity, ion activity and fixed charges omitted. ### Measurement plan with independent controls

A defensible first investigation of **swelling thermodynamics and osmotic stress** uses **oscillatory rheometry and swelling gravimetry** and records **G prime, G double-prime, equilibrium ratio, sample thickness and solvent chemistry**. Pair it with **creep or relaxation assay with wall-slip control and independent network chemistry**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A measured water-mass gain is not equal to free solute concentration inside the network. The ideal osmotic law ignores ion correlations, polymer interactions and network stress.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **swelling thermodynamics and osmotic stress** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **84.242135 kPa** and **111.49694 kPa** from `c*8.314462618*298/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **swelling thermodynamics and osmotic stress**, testing this lesson's claim while distinguishing **a surface-only measurement versus a bulk-sensitive characterization**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Why might a saline swelling test give a different result even when the same dry polymer mass is used? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_4 -->

## Lesson 3.3 — Viscoelasticity and time-dependent relaxation

### Mechanism, technical vocabulary and equation

A hydrogel can relax stress at fixed strain and creep under fixed stress because molecular strands and water migrate. A single Maxwell element has an exponential stress-relaxation function and an associated time constant; real gels frequently require spectra of modes. Temperature and hydration can shift the response without any change in chemistry. A mechanically suitable material should be tested under application-relevant frequencies, strain amplitudes and time scales. Shear-thinning injectability does not automatically imply retention of load-bearing stiffness after injection.

**Key relation.** A Maxwell element at fixed imposed strain has σ(t)=σ0 exp(−t/τ), where τ=η/E for a series spring-dashpot model.

### A specific design challenge

In a stress-relaxation test, a gel initially supports load but loses half the stress within seconds. Compare a single-mode fit against a two-mode alternative and design a hold-and-recovery protocol.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal hydrogel network shear modulus**, adjusts **Active-chain molar density**. Using the declared expression `nu*8.314462618*298/1000`, insert **45 mol/m³** to obtain **111.496944 kPa**. A controlled second input of **56 mol/m³** produces **138.751752 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4777099 (kPa)/(mol/m³)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Ideal network G=νRT at T=298 K; dangling strands, phantom-network correction, entanglement, swelling and nonlinear strain omitted. ### Measurement plan with independent controls

A defensible first investigation of **viscoelasticity and time-dependent relaxation** uses **oscillatory rheometry and swelling gravimetry** and records **G prime, G double-prime, equilibrium ratio, sample thickness and solvent chemistry**. Pair it with **creep or relaxation assay with wall-slip control and independent network chemistry**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Extrapolating a relaxation curve fitted over ten seconds to months is unsupported. Test whether the sample experienced dehydration, wall slip or nonlinear strain.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **viscoelasticity and time-dependent relaxation** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **111.49694 kPa** and **138.75175 kPa** from `nu*8.314462618*298/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **viscoelasticity and time-dependent relaxation**, testing this lesson's claim while distinguishing **an apparent favorable result compared against its most plausible competing explanation**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How would you distinguish genuine polymer relaxation from sample slippage at the rheometer plates? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 3.4 — Mass transport through hydrated networks

### Mechanism, technical vocabulary and equation

Solute transport in gels depends on diffusion, electrostatic partitioning, binding, convection and degradation. Diffusivity depends on solute radius, network structure and test medium; a dye can have different transport behavior from a drug or a protein. Early diffusion may be approximated by Fickian laws, but swelling during the experiment changes path length and potentially diffusivity. Permeability measurements should be separated from diffusion coefficients when pressure-driven flow is present. Mass balance prevents confusion between uptake, retention and release.

**Key relation.** A one-dimensional characteristic diffusion time scales approximately as L²/D for constant D and fixed slab geometry; exact coefficients depend on boundary conditions.

### A specific design challenge

For two hydrogel thicknesses, estimate a time-scale ratio from L²/D, then explain why the ratio could break down for a strongly swelling, binding network.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Dilute solution osmotic pressure**, adjusts **Solute concentration**. Using the declared expression `c*8.314462618*298/1000`, insert **56 mol/m³** to obtain **138.751752 kPa**. A controlled second input of **67 mol/m³** produces **166.006561 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4777099 (kPa)/(mol/m³)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Ideal van’t Hoff Π=cRT at T=298 K; gel elasticity, ion activity and fixed charges omitted. ### Measurement plan with independent controls

A defensible first investigation of **mass transport through hydrated networks** uses **oscillatory rheometry and swelling gravimetry** and records **G prime, G double-prime, equilibrium ratio, sample thickness and solvent chemistry**. Pair it with **creep or relaxation assay with wall-slip control and independent network chemistry**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A cumulative fluorescence signal can be distorted by quenching, photobleaching, adsorption to container walls or incomplete extraction; calibrate mass with independent standards.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **mass transport through hydrated networks** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **138.75175 kPa** and **166.00656 kPa** from `c*8.314462618*298/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **mass transport through hydrated networks**, testing this lesson's claim while distinguishing **water-saturated versus dry specimens under the same nominal load**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which control separates irreversible binding from a genuinely small diffusion coefficient? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_5 -->

## Lesson 3.5 — Adhesive, injectable and self-healing hydrogels

### Mechanism, technical vocabulary and equation

Tissue adhesives require interfacial work of adhesion, wet mechanical strength and tolerable chemical reactivity. Injectable networks require delivery forces that are compatible with intended handling and gelation behavior after placement. Self-healing in oscillatory rheology is not identical to reliable healing of a macroscopic damaged structure. Reversible bonds can support rapid recovery but introduce creep and environmental sensitivity. Water, salts, proteins and sterilization may all change adhesive chemistry. Analyze the whole application process rather than choosing material from one laboratory shear modulus.

**Key relation.** Energy release rate Gc=Ureleased/Anew crack is an interfacial fracture measure when work and new area are properly defined; adhesion force by itself is geometry-dependent.

### A specific design challenge

Evaluate a notional injectable gel for a temporary tissue spacer. Record syringe extrusion force, setting time, hydrated burst pressure or tensile adhesion, and degradation/fragmentation behavior.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal hydrogel network shear modulus**, adjusts **Active-chain molar density**. Using the declared expression `nu*8.314462618*298/1000`, insert **67 mol/m³** to obtain **166.006561 kPa**. A controlled second input of **78 mol/m³** produces **193.261369 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **2.4777099 (kPa)/(mol/m³)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Ideal network G=νRT at T=298 K; dangling strands, phantom-network correction, entanglement, swelling and nonlinear strain omitted. ### Measurement plan with independent controls

A defensible first investigation of **adhesive, injectable and self-healing hydrogels** uses **oscillatory rheometry and swelling gravimetry** and records **G prime, G double-prime, equilibrium ratio, sample thickness and solvent chemistry**. Pair it with **creep or relaxation assay with wall-slip control and independent network chemistry**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A material that reforms modulus after 30 seconds in a shear cycle may still fail adhesively on wet tissue. In-vitro gelation is not proof of clinical deliverability.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **adhesive, injectable and self-healing hydrogels** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **166.00656 kPa** and **193.26137 kPa** from `nu*8.314462618*298/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **adhesive, injectable and self-healing hydrogels**, testing this lesson's claim while distinguishing **a small versus large geometry with equal bulk chemical composition**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What result would demonstrate cohesive failure rather than debonding from the substrate? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 3 capstone — integrated design review

**Capstone setting.** Compare two hydrogel candidates for a nonimplant demonstration dressing. Include network mechanics, water-vapor transport, adhesive failure and potential leachables.

1. **Define the device boundary.** For **hydrogels, soft biomaterials and rheology**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **hydrogels, soft biomaterials and rheology**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

