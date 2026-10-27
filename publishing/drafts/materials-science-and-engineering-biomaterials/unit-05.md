# Unit 5: Orthopedic, dental and structural biomaterials

**Guiding research question:** How do implants share load, integrate with hard tissue and resist long-term damage?

## Field context, scope and prerequisites

Orthopedic and dental materials combine complex contact mechanics, cyclic loading and evolving bone or connective-tissue environments. Tissue remodeling makes a device's load-sharing environment time-dependent. An implant interface can be chemically bonded, geometrically interlocked or mechanically fixed, with different failure modes. Wear debris and corrosion products can influence the local biological environment. This unit avoids instructions for surgical implantation and treats simulations as mechanical approximations, not patient outcomes.

The learning progression in **Orthopedic, dental and structural biomaterials** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Orthopedic, dental and structural biomaterials**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 5.1 — Bone hierarchy and anisotropic mechanics

### Mechanism, technical vocabulary and equation

Bone is hierarchical and anisotropic: mineral platelets, collagen architecture, osteonal or trabecular morphology and remodeling collectively influence stiffness and strength. Apparent cancellous-bone modulus depends strongly on density and orientation, while cortical bone is not a single isotropic material constant. An engineered substitute may match one compressive modulus yet differ markedly in toughness, fatigue, permeability and fixation. Characterize loading direction, wet state and strain rate when comparing specimens.

**Key relation.** Orthotropic linear elasticity links stress and strain through a direction-dependent stiffness tensor; scalar σ=Eε holds only for a specified uniaxial configuration.

### A specific design challenge

Contrast a longitudinal cortical-bone coupon, a transverse coupon and an open-cell scaffold with the same reported apparent modulus. List measurements that prevent the three from being treated as equivalent.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal parallel composite stiffness bound**, adjusts **Stiff phase volume fraction**. Using the declared expression `2+68*v`, insert **0.17777778 fraction** to obtain **14.0888889 GPa**. A controlled second input of **0.26666667 fraction** produces **20.1333333 GPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **68 (GPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** E1=70 GPa, E2=2 GPa, perfectly bonded aligned components under parallel strain; ignores porosity and tissue remodeling. ### Measurement plan with independent controls

A defensible first investigation of **bone hierarchy and anisotropic mechanics** uses **wet compression or fatigue with phase/microstructure analysis** and records **load direction, cycles, ion concentrations, wear or debris and phase fraction**. Pair it with **cross-sectional imaging, surface examination and independently manufactured batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not convert a literature range for human bone to an individual patient's performance or claim equivalence of architectures based on one uniaxial compressive test.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **bone hierarchy and anisotropic mechanics** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **14.088889 GPa** and **20.133333 GPa** from `2+68*v` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **bone hierarchy and anisotropic mechanics**, testing this lesson's claim while distinguishing **a surface-only measurement versus a bulk-sensitive characterization**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What orthogonal loading result would disprove an isotropic-bone assumption? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 5.2 — Calcium-phosphate ceramics and bioactive glasses

### Mechanism, technical vocabulary and equation

Hydroxyapatite, tricalcium phosphates and bioactive-glass systems can interact with physiological ionic environments, but dissolution and mechanical behavior depend on crystal phase, stoichiometry, porosity and processing. The term osteoconductive describes a context-dependent capacity for bone growth along a scaffold, not a universal in-vitro assay result. Brittle failure, particle generation and phase transformation can constrain applications. Phase identification and dissolution chemistry should be established before claiming a predictable biological response.

**Key relation.** A two-phase Voigt stiffness bound is E_V=φE1+(1−φ)E2 for a suitable aligned parallel-loading idealization, not a direct prediction of porous bone ingrowth.

### A specific design challenge

Compare two porous calcium-phosphate specimens with different phase mixtures. Plan X-ray diffraction, ion-release and wet mechanical tests before interpreting any cell culture endpoint.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative porous compressive strength**, adjusts **Porosity fraction**. Using the declared expression `100*Math.pow(1-p,2)`, insert **0.26333333 fraction** to obtain **54.2677778 MPa**. A controlled second input of **0.34444444 fraction** produces **42.9753086 MPa**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-139.22222 (MPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Nominal dense-matrix strength 100 MPa, quadratic scaling solely for sensitivity; not qualified for brittle fracture, fatigue or actual ceramics. ### Measurement plan with independent controls

A defensible first investigation of **calcium-phosphate ceramics and bioactive glasses** uses **wet compression or fatigue with phase/microstructure analysis** and records **load direction, cycles, ion concentrations, wear or debris and phase fraction**. Pair it with **cross-sectional imaging, surface examination and independently manufactured batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Avoid treating all calcium phosphates as chemically or mechanically interchangeable. Dissolution measured in a static buffer need not reproduce dynamic tissue exposure.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **calcium-phosphate ceramics and bioactive glasses** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **54.267778 MPa** and **42.975309 MPa** from `100*Math.pow(1-p,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **calcium-phosphate ceramics and bioactive glasses**, testing this lesson's claim while distinguishing **an apparent favorable result compared against its most plausible competing explanation**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How could a change in crystalline phase masquerade as improved porosity-controlled performance? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_8 -->

## Lesson 5.3 — Titanium alloys, corrosion and passive films

### Mechanism, technical vocabulary and equation

Titanium alloys often rely on passive surface oxides that influence electrochemical behavior. The interface may change through fretting, tribocorrosion, cleaning, sterilization and mechanical processing. Corrosion rates depend on electrolyte chemistry, potential, area, temperature and galvanic connections. A polished sample tested in saline at rest may miss damage from loaded contacts. Bulk alloy composition and as-finished surface chemistry should both be reported.

**Key relation.** Faraday-based mass estimates m=ItM/(nF) require a known reaction, current efficiency and oxidation state; corrosion-current measurements alone may not justify these assumptions.

### A specific design challenge

Construct an electrochemical and tribological comparison of two hypothetical implant-surface finishes, keeping alloy grade fixed. Specify corrosion-current measurements, surface microscopy and wear-debris collection.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal parallel composite stiffness bound**, adjusts **Stiff phase volume fraction**. Using the declared expression `2+68*v`, insert **0.35555556 fraction** to obtain **26.1777778 GPa**. A controlled second input of **0.44444444 fraction** produces **32.2222222 GPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **68 (GPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** E1=70 GPa, E2=2 GPa, perfectly bonded aligned components under parallel strain; ignores porosity and tissue remodeling. ### Measurement plan with independent controls

A defensible first investigation of **titanium alloys, corrosion and passive films** uses **wet compression or fatigue with phase/microstructure analysis** and records **load direction, cycles, ion concentrations, wear or debris and phase fraction**. Pair it with **cross-sectional imaging, surface examination and independently manufactured batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Low static corrosion current is not evidence of zero ion release or immunity to crevice conditions. Electrochemical tests need reference-electrode specification and defensible interpretation.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **titanium alloys, corrosion and passive films** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **26.177778 GPa** and **32.222222 GPa** from `2+68*v` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **titanium alloys, corrosion and passive films**, testing this lesson's claim while distinguishing **water-saturated versus dry specimens under the same nominal load**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which combined cyclic contact and electrochemical test could expose a failure missed by an immersion-only study? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 5.4 — Articulating bearings and wear particles

### Mechanism, technical vocabulary and equation

A bearing contact transmits compressive stress and tangential sliding under lubrication regimes that may change with motion and fluid composition. Wear volume depends on contact geometry, counterface roughness, load, cycles, fluid chemistry and wear mechanism. Particle size and chemistry matter biologically, but a simulator's particle count cannot be directly translated into a clinical prognosis. Distinguish adhesive, abrasive, fatigue and oxidative mechanisms and report both volumetric and mass wear with density assumptions.

**Key relation.** A simple empirical wear relation is V≈KWs/H, where V is volume loss, W load, s sliding distance, H hardness and K a calibrated dimensionless coefficient.

### A specific design challenge

Two bearing couples have similar loss of mass but very different generated particle-size distributions. Describe why an equal gravimetric value does not mean equal biological exposure.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Illustrative porous compressive strength**, adjusts **Porosity fraction**. Using the declared expression `100*Math.pow(1-p,2)`, insert **0.42555556 fraction** to obtain **32.998642 MPa**. A controlled second input of **0.50666667 fraction** produces **24.3377778 MPa**. Within these numerical bounds the output decreases; the finite-difference sensitivity is **-106.77778 (MPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Nominal dense-matrix strength 100 MPa, quadratic scaling solely for sensitivity; not qualified for brittle fracture, fatigue or actual ceramics. ### Measurement plan with independent controls

A defensible first investigation of **articulating bearings and wear particles** uses **wet compression or fatigue with phase/microstructure analysis** and records **load direction, cycles, ion concentrations, wear or debris and phase fraction**. Pair it with **cross-sectional imaging, surface examination and independently manufactured batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Archard's empirical law is not predictive outside its calibrated wear regime; it does not encode all lubrication and third-body effects.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **articulating bearings and wear particles** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **32.998642 MPa** and **24.337778 MPa** from `100*Math.pow(1-p,2)` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **articulating bearings and wear particles**, testing this lesson's claim while distinguishing **a small versus large geometry with equal bulk chemical composition**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** How would you distinguish true wear loss from fluid uptake of a polymer specimen? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_9 -->

## Lesson 5.5 — Osseointegration, fixation and interface micro-motion

### Mechanism, technical vocabulary and equation

Early fixation and eventual tissue integration are different states. Surface topography, chemistry and loading can influence interfacial behavior, but micromotion also depends on geometry and force pathways. Mechanical interlock should be assessed with relevant shear, push-out or fatigue configurations and justified biological observations. A high coating adhesion measurement does not guarantee stable fixation of the assembled device. Bone remodeling and patient factors prevent a universal interface-performance curve.

**Key relation.** Average nominal shear stress τ=F/A assumes an appropriately defined bonded area; real implant interface tractions are nonuniform.

### A specific design challenge

Compare a textured and a polished fixture of the same substrate composition. Define a blinded preclinical research protocol with mechanical, imaging and tissue response measures without treating it as surgical instruction.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal parallel composite stiffness bound**, adjusts **Stiff phase volume fraction**. Using the declared expression `2+68*v`, insert **0.53333333 fraction** to obtain **38.2666667 GPa**. A controlled second input of **0.62222222 fraction** produces **44.3111111 GPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **68 (GPa)/(fraction)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** E1=70 GPa, E2=2 GPa, perfectly bonded aligned components under parallel strain; ignores porosity and tissue remodeling. ### Measurement plan with independent controls

A defensible first investigation of **osseointegration, fixation and interface micro-motion** uses **wet compression or fatigue with phase/microstructure analysis** and records **load direction, cycles, ion concentrations, wear or debris and phase fraction**. Pair it with **cross-sectional imaging, surface examination and independently manufactured batches**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A single radiograph or push-out force does not establish lifetime clinical success. Test artifacts such as off-axis loading can dominate small-sample mechanical results.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **osseointegration, fixation and interface micro-motion** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **38.266667 GPa** and **44.311111 GPa** from `2+68*v` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **osseointegration, fixation and interface micro-motion**, testing this lesson's claim while distinguishing **a surface-only measurement versus a bulk-sensitive characterization**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What observation could separate coating delamination from loss of interlock at the tissue interface? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 5 capstone — integrated design review

**Capstone setting.** Design a requirements matrix for a hypothetical bone-facing porous implant: mechanics, fatigue, wear/ions, manufacturability, and evidence required before any translation.

1. **Define the device boundary.** For **orthopedic, dental and structural biomaterials**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **orthopedic, dental and structural biomaterials**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

