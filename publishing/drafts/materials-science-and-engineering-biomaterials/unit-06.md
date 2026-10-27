# Unit 6: Blood-contacting devices and fluid–material interactions

**Guiding research question:** Why must blood compatibility be investigated under realistic flow conditions and multiple biological endpoints?

## Field context, scope and prerequisites

Blood-contacting devices face coupled adsorption, coagulation, platelet interactions, flow patterns and material degradation. A static incubation test may miss shear-dependent processes or stagnant recirculation zones. Simplified laminar-flow models are useful for unit checking but do not predict thrombosis, hemolysis or patient outcomes. Hemocompatibility evaluation is context dependent and is addressed by relevant ISO 10993 approaches and device-specific expectations. Maintain separation between fluid mechanics, surface observations and biological evidence.

The learning progression in **Blood-contacting devices and fluid–material interactions** moves from mechanistic ideas to testable measurements. In a biomaterials investigation, the state of a sample is inseparable from the method used to create that state. Before comparing two surfaces or two bulk materials, document manufacturing route, sterilization history, storage, hydration, temperature, medium chemistry, geometry and time since exposure. Identify whether each reported number is measured, inferred from an instrument model, fitted or only calculated as a teaching illustration. A surface signal may be dominated by an adsorbed conditioning film; a compression result may reflect drainage and platen friction; a chemical release signal may reflect contamination or sample recovery. These alternatives must be made testable, not removed by a persuasive narrative.

## Unit-level design studio

In **Blood-contacting devices and fluid–material interactions**, work with a fictional candidate material; do not perform human-use experiments. Choose a concrete intended function and list three nonnegotiable requirements. Select one property measurement, one mechanistic test and one control able to reveal a confounder. When there is insufficient evidence to select a material, explicitly state the missing test and its decision threshold. Maintain an evidence ledger separating literature-supported principles, calculated synthetic values and unresolved empirical claims. In this unit the corresponding numerical models are intentionally simple: they explore two selected dependencies, not a fully coupled human-system response.

## Lesson 6.1 — Hemocompatibility as a multi-endpoint concept

### Mechanism, technical vocabulary and equation

A blood-contacting surface may induce platelet adhesion or activation, influence coagulation pathways, damage cells or activate complement, depending on material, geometry and exposure. These are related but not interchangeable endpoints. Interpretation requires control of donor variability, anticoagulants, flow, duration and specimen area. In-vitro studies can identify hazards without proving outcomes in an assembled device. Report both direct material effects and flow-generated artifacts, with controls for contact to tubing, connectors and collection systems.

**Key relation.** Relative change ΔX/X0 requires baseline, time and sample-processing definitions before comparing any biological endpoint.

### A specific design challenge

Design a comparison of two hypothetical oxygenator tubing materials using standardized surface area and exposure time. Specify platelet, hemolysis and complement observations while keeping blood-source variability visible.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal rigid-tube Newtonian wall shear**, adjusts **Volumetric flow**. Using the declared expression `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))`, insert **63.333333 mL/min** to obtain **4.70391276 Pa**. A controlled second input of **90 mL/min** produces **6.68450761 Pa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.074272307 (Pa)/(mL/min)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Steady fully developed laminar flow, fluid viscosity 0.0035 Pa·s, fixed tube radius 1 mm; not whole-blood hemocompatibility. ### Measurement plan with independent controls

A defensible first investigation of **hemocompatibility as a multi-endpoint concept** uses **controlled flow loop and pressure transducers** and records **volumetric flow, viscosity, residence time, pressure and shear estimate**. Pair it with **blank loop without test coupon, surface imaging after standardized handling and exposure controls**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A low platelet count on a surface could reflect weak adhesion, strong activation followed by embolization, or sampling loss; a single endpoint does not establish compatibility.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **hemocompatibility as a multi-endpoint concept** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **4.7039128 Pa** and **6.6845076 Pa** from `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **hemocompatibility as a multi-endpoint concept**, testing this lesson's claim while distinguishing **a repeat measurement of one specimen versus an independently manufactured lot**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which experimental control distinguishes a material effect from a pump-induced blood damage artifact? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 6.2 — Laminar flow and wall shear estimates

### Mechanism, technical vocabulary and equation

For a Newtonian fluid in steady fully developed laminar flow through a rigid circular tube, velocity is parabolic and wall shear grows with flow rate. Blood is not Newtonian at every scale, and complex devices include branches, bends, pulsation, compliant walls and transition regions. A simple tube model therefore supplies an estimate for teaching, not a design guarantee. At interfaces, low shear and recirculation may encourage residence while very high shear may create other problems; neither has a universal safety threshold independent of device context.

**Key relation.** For steady Newtonian laminar flow in a rigid round tube, wall shear τw=4μQ/(πr³), with dynamic viscosity μ, flow Q and internal radius r.

### A specific design challenge

Compute nominal wall shear for two flow rates through the same tube, then name deviations caused by a stenosis, pulsatility and a change in temperature-dependent viscosity.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal rigid-tube Newtonian pressure loss**, adjusts **Volumetric flow**. Using the declared expression `8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000`, insert **90 mL/min** to obtain **2.67380304 kPa**. A controlled second input of **116.66667 mL/min** produces **3.46604098 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.029708923 (kPa)/(mL/min)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Poiseuille rigid circular tube, viscosity 0.0035 Pa·s, length 0.2 m, radius 1 mm, no entrance or pulsatile effects. ### Measurement plan with independent controls

A defensible first investigation of **laminar flow and wall shear estimates** uses **controlled flow loop and pressure transducers** and records **volumetric flow, viscosity, residence time, pressure and shear estimate**. Pair it with **blank loop without test coupon, surface imaging after standardized handling and exposure controls**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

Do not use Poiseuille estimates in a noncircular pore network or claim a shear value alone predicts platelet activation or hemolysis.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **laminar flow and wall shear estimates** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **2.673803 kPa** and **3.466041 kPa** from `8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **laminar flow and wall shear estimates**, testing this lesson's claim while distinguishing **a design input requirement compared against a physically measured acceptance criterion**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which experimental velocity-field observation would falsify the fully developed laminar assumption? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_10 -->

## Lesson 6.3 — Pressure drop, pumping and geometry

### Mechanism, technical vocabulary and equation

Pressure loss affects device operation and flow residence time, but geometry dependence is steep. In the Poiseuille limit, pressure drop varies as inverse radius to the fourth power. Real devices add entrance losses, bends, manifolds, porous structures and time-variable compliance. Pressure sensors require reference locations and calibration; a pressure-drop reading across an entire loop cannot isolate an individual component without a baseline. Fluid rheology and clot accumulation can alter resistance during use.

**Key relation.** Hagen–Poiseuille relation ΔP=8μLQ/(πr⁴) assumes steady incompressible Newtonian fully developed laminar flow, circular rigid tube and no entrance loss.

### A specific design challenge

A small reduction in inner radius greatly increases ideal pressure loss. Compare a baseline tube with a 10% smaller bore at constant flow and discuss which assumptions fail for blood-like suspensions.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal rigid-tube Newtonian wall shear**, adjusts **Volumetric flow**. Using the declared expression `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))`, insert **116.66667 mL/min** to obtain **8.66510246 Pa**. A controlled second input of **143.33333 mL/min** produces **10.6456973 Pa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.074272307 (Pa)/(mL/min)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Steady fully developed laminar flow, fluid viscosity 0.0035 Pa·s, fixed tube radius 1 mm; not whole-blood hemocompatibility. ### Measurement plan with independent controls

A defensible first investigation of **pressure drop, pumping and geometry** uses **controlled flow loop and pressure transducers** and records **volumetric flow, viscosity, residence time, pressure and shear estimate**. Pair it with **blank loop without test coupon, surface imaging after standardized handling and exposure controls**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A fitted hydrodynamic resistance from one operating point can conceal nonlinearity, elastic deformation or obstructive deposits. Never mistake an engineering pressure relation for a safety prediction.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **pressure drop, pumping and geometry** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **8.6651025 Pa** and **10.645697 Pa** from `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **pressure drop, pumping and geometry**, testing this lesson's claim while distinguishing **an as-fabricated surface versus the identical material after the intended finishing process**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What sensor placement and flow sweep would separate tube resistance from a connector loss? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Lesson 6.4 — Surface conditioning under flow

### Mechanism, technical vocabulary and equation

The conditioning layer of adsorbed proteins and platelets can change when transport continuously renews solutes. Stagnation zones, wall shear and concentration gradients influence both accumulation and removal. Sampling after pump shutdown may modify deposits. Useful comparative testing keeps specimen area, shear history, temperature and solution chemistry consistent and includes no-device loop controls. Surface characterization after flow should document fixation, rinsing and imaging changes, because processing can strip weakly adsorbed layers.

**Key relation.** For a dilute solute, convective–diffusive transport can be summarized by Pe=UL/D, but boundary geometry and binding control the interpretation.

### A specific design challenge

Compare a static protein-incubation assay with a perfusion assay under otherwise similar chemistry. Outline why different surface rankings might emerge without either method being technically wrong.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal rigid-tube Newtonian pressure loss**, adjusts **Volumetric flow**. Using the declared expression `8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000`, insert **143.33333 mL/min** to obtain **4.25827892 kPa**. A controlled second input of **170 mL/min** produces **5.05051686 kPa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.029708923 (kPa)/(mL/min)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Poiseuille rigid circular tube, viscosity 0.0035 Pa·s, length 0.2 m, radius 1 mm, no entrance or pulsatile effects. ### Measurement plan with independent controls

A defensible first investigation of **surface conditioning under flow** uses **controlled flow loop and pressure transducers** and records **volumetric flow, viscosity, residence time, pressure and shear estimate**. Pair it with **blank loop without test coupon, surface imaging after standardized handling and exposure controls**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A flow-loop result may reflect pump, tubing and anticoagulant interactions. Controls must account for the entire test system rather than the candidate coupon alone.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **surface conditioning under flow** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **4.2582789 kPa** and **5.0505169 kPa** from `8*0.0035*0.2*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,4))/1000` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **surface conditioning under flow**, testing this lesson's claim while distinguishing **an early time point versus a later time point using independently prepared samples**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** What measurement would reveal that the apparent surface signal is dominated by residence time instead of binding affinity? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

<!-- MODEL_11 -->

## Lesson 6.5 — Catheter coatings and flow-device failure analysis

### Mechanism, technical vocabulary and equation

Coatings seek to alter wetting, fouling, friction or chemical interactions, but they can delaminate, swell or shed fragments. A coating that performs well on a planar coupon may fail at connector transitions, bends or repeated flexion. Leachable chemistry, sterilization resistance and shelf-life changes should be considered alongside surface response. Flow performance metrics require geometry-specific limits and biological risk evaluation of the finished, processed device. No educational slider here establishes anti-thrombotic efficacy.

**Key relation.** Wear loss per cycle can be expressed Δm/N only after correcting for fluid uptake and collection efficiency; it is a descriptive quantity, not an exposure-risk score.

### A specific design challenge

Analyze a notional hydrophilic catheter coating that shows lower insertion friction but increasing particle shedding after repeated cycles. Create an evidence plan that treats debris release as a separate hazard.

### Synthetic numerical example — linked unit model

The unit's pedagogical formula card, **Ideal rigid-tube Newtonian wall shear**, adjusts **Volumetric flow**. Using the declared expression `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))`, insert **170 mL/min** to obtain **12.6262922 Pa**. A controlled second input of **196.66667 mL/min** produces **14.606887 Pa**. Within these numerical bounds the output increases; the finite-difference sensitivity is **0.074272307 (Pa)/(mL/min)**. Use coherent units before interpreting slope. The relation deliberately isolates a principle of this unit; where the lesson focuses on a different experimental observable, the model is a companion approximation rather than a simulation of the described biological system.

**Declared model assumptions:** Steady fully developed laminar flow, fluid viscosity 0.0035 Pa·s, fixed tube radius 1 mm; not whole-blood hemocompatibility. ### Measurement plan with independent controls

A defensible first investigation of **catheter coatings and flow-device failure analysis** uses **controlled flow loop and pressure transducers** and records **volumetric flow, viscosity, residence time, pressure and shear estimate**. Pair it with **blank loop without test coupon, surface imaging after standardized handling and exposure controls**. Specify an instrument or sample preparation blank before collecting results, and state the actual independent replicate unit: a newly fabricated specimen, an independently prepared fluid batch, a donor or a different processing run. Sampling multiple fields of one test piece is not necessarily independent evidence about manufacturing consistency. When data are correlated, a naive average over images may greatly overstate certainty. A suitable log should identify which material comparison was made, processing and exposure history, instrument resolution, sample geometry and any exclusions.

### Limits, alternative hypotheses and failure analysis

A promotional claim of 'non-thrombogenic' based on one static surface photograph is scientifically inadequate and potentially misleading.

### Knowledge check and worked reasoning

**Exercise A — conceptual distinction.** Explain which part of **catheter coatings and flow-device failure analysis** is intrinsic chemistry, which part depends on geometry or processing, and which part needs the proposed measurement. Provide a counterexample to a simple 'better material' ranking. *Reasoning guide:* an intrinsic molecular bond or bulk composition does not by itself specify the finished interface or its function; look for a condition whose change can reverse the result.

**Exercise B — reproducible numerical investigation.** Recompute the two values **12.626292 Pa** and **14.606887 Pa** from `4*0.0035*(Q*1e-6/60)/(Math.PI*Math.pow(0.001,3))` using the specified inputs. Report a unit conversion, the slope and the two endpoint values from the slider bounds. *Reasoning guide:* do not round intermediary SI conversions too early; state the simplified physical regime; the two values should follow the declared formula but are not observations.

**Exercise C — falsification and controls.** Design a two-condition experiment on **catheter coatings and flow-device failure analysis**, testing this lesson's claim while distinguishing **a repeat measurement of one specimen versus an independently manufactured lot**. Include a method blank, independent replicates, an uncertainty source, and one observation that would cause the preferred hypothesis to be rejected. *Reasoning guide:* change only one primary factor when possible; select an independent technique so that two readouts do not simply share the same bias.

**Discussion prompt.** Which accelerated flexion test could detect a coating failure invisible in a single wet-contact-angle measurement? A defensible answer distinguishes what the calculations show from what would require material characterization or a biological evaluation. State a practical go/no-go test and say which entity—a material lot, entire device or biological specimen—your conclusion actually concerns.

## Unit 6 capstone — integrated design review

**Capstone setting.** Build a risk-and-evidence matrix for a hypothetical blood-contacting tubing component, comparing baseline and coated versions under flow, sterilization and flexion.

1. **Define the device boundary.** For **blood-contacting devices and fluid–material interactions**, give the intended material role, expected exposure, important mechanical/environmental conditions and the distinction between a research specimen and a finished device. Explain why the same bulk chemistry can require different evidence for different use cases.
2. **Choose three measurable endpoints.** For each endpoint, propose an instrument, a sample preparation control, an independent replicate unit and an explicit result that would be incompatible with the favored design explanation. Justify how each endpoint bears on the decision.
3. **Audit both unit models.** Calculate an intermediate input and both endpoint values for the two offline model cards. Make a two-column table separating mathematical assumptions from additional information required to predict a physical or biological observation. Never rebrand the outputs as measured data.
4. **Challenge the experimental design.** List at least four credible confounders, including one related to geometry, one to chemistry or biological medium, one to manufacturing and one to measurement. Propose a practical low-cost control for each.
5. **Issue an evidence-limited decision.** Write a 200-word recommendation identifying what may be concluded, what would make the candidate unsafe or impractical, which follow-up experiment changes the ranking, and which decisions require specialized biological, clinical or regulatory review.

### Unit synthesis

In **blood-contacting devices and fluid–material interactions**, a useful answer links a stated requirement to an appropriate measurement and then to a documented decision. Avoid converting material popularity into evidence of suitability. Even if the synthetic relation is numerically stable across its slider range, real properties can vary across lots, environments and times. Successful learning means being able to describe a credible observation that overturns the preferred material choice. Retain provenance: a computed response is not measured performance, in-vitro evidence is not a clinical result, and a literature reference is not authorization to manufacture or implant a device.

