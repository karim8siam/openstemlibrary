# Unit 8: Integrated selection, joining and qualification

**Guiding question:** How do metallurgists make traceable decisions when cost, processing and service performance all matter?

## Why this unit matters to metallurgical decisions

A laboratory weld-plus-heat-treatment process produces attractive test coupons, but a production geometry has a thicker wall, altered restraint and inconsistent thermocouple placement. This is a question about **manufacturing traceability** and about the difference between **coupon response versus production reliability**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Production specifications convert a scientific finding into a reproducible process with material traceability, manufacturing limits and acceptance criteria. A laboratory coupon validates neither a thick casting nor a constrained welded structure without geometry-representative evidence.

Define failure criteria before interpreting the data: allowable property intervals, unacceptable defect classes, permitted variation and the consequences of false acceptance. Keep a hold-out batch and retain instrument calibrations and raw observations. A design decision should explicitly record unresolved uncertainty.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **part geometry and process audit**. For any local observation, describe why its sampling plan represents the part. Treat **local treatment variation** as an explicit rival explanation and plan **independent held-out production parts** as an independent check.

## Lesson 8.1: Process maps and structure-property traceability

### Scientific foundation

A usable selection map tracks composition, processing history, structure, test method and property with batch identifiers. A nominal grade cannot stand in for an actual material state, particularly after deformation, heat treatment, joining or repair. Microstructure is a mediator between processing and service behavior rather than an independent input chosen arbitrarily.

**Governing relationship or decision rule:** A process-structure-property relation requires matched samples and controlled provenance, not correlation alone. Read every term in the equation as part of a declared specimen condition. In **process maps and structure-property traceability**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Build a three-batch traceability table with heat chemistry, furnace log, microscopy location, hardness distribution and held-out tensile tests. Define an escalation rule if one batch's core hardness differs materially from its surface.

A companion calculator called **Weld line energy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Welding travel speed = 3 mm/s**, the declared formula returns **800 J/mm**; at **Welding travel speed = 5 mm/s**, it returns **480 J/mm**. On this interval the modeled value decreases, and the two-point slope is **-160 J/mm per mm/s**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `0.8*20*150/v`. Model validity is limited to: **Illustrative arc 20 V ×150 A, efficiency eta=0.8, constant travel; actual weld pool geometry excluded**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A statistically impressive fitted process-property relation may be confounded by batch, operator or sampling location.

### Exercises and self-assessment

**Exercise 8.1A — Physical mechanism.** Which two metadata fields would most improve reproducibility if a previous heat-treatment run could not be recreated? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.1B — Numerical cross-check.** Recalculate **800 J/mm** from the companion formula at **3 mm/s** and compare with **480 J/mm** at **5 mm/s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 8.1C — Test design.** Propose a preparation or test matrix that addresses **local treatment variation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Lesson 8.2: Welding heat-affected zones and softening

### Scientific foundation

A weld consists of fusion zone, heat-affected regions and unaffected base metal; their local time-temperature paths alter grain size, precipitates and residual stresses. Some carbon steels form hard brittle products under certain cooling paths, while age-hardened aluminum may soften in the heat-affected region. The appropriate inspection is tied to alloy system, joint design and service loading.

**Governing relationship or decision rule:** Approximate line energy E_line=eta V I/v, with efficiency eta and travel speed v expressed consistently. Read every term in the equation as part of a declared specimen condition. In **welding heat-affected zones and softening**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Sketch a fictional cross-weld microhardness traverse and locate peaks or troughs relative to the fusion boundary. Pair it with macroetch and microscopic maps, and describe a controlled experiment that changes heat input.

A companion calculator called **Independent-counting fraction error** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Number of sampled points = 607.1429 samples**, the declared formula returns **0.017573376 fraction**; at **Number of sampled points = 885.7143 samples**, it returns **0.014549692 fraction**. On this interval the modeled value decreases, and the two-point slope is **-1.0854247e-05 fraction per samples**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `Math.sqrt(0.25*0.75/N)`. Model validity is limited to: **True hypothetical phase area fraction 0.25, independent points; correlated microstructure produces larger effective uncertainty**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Heat input per unit length does not uniquely define thermal history because geometry, efficiency, preheat and restraint vary.

### Exercises and self-assessment

**Exercise 8.2A — Physical mechanism.** Why could an alloy have an acceptable weld-center hardness yet fail beside the weld? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.2B — Numerical cross-check.** Recalculate **0.017573376 fraction** from the companion formula at **607.1429 samples** and compare with **0.014549692 fraction** at **885.7143 samples**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 8.2C — Test design.** Propose a preparation or test matrix that addresses **local treatment variation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_15 -->

## Lesson 8.3: Failure investigation and competing hypotheses

### Scientific foundation

Metallurgical failures may begin from a design stress concentrator, processing defect, inadequate material specification, service overload or environmental attack; fracture features alone do not establish culpability. An investigation should preserve evidence, document fracture origin and compare positive observations against plausible alternative scenarios. A good report separates what was measured from what was inferred.

**Governing relationship or decision rule:** Likelihood-based comparison asks whether evidence is expected under each competing mechanism, rather than treating one image as conclusive. Read every term in the equation as part of a declared specimen condition. In **failure investigation and competing hypotheses**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Create a failure tree for a snapped shaft: overload, corrosion fatigue, inclusion-initiated fatigue and quench crack. Specify at least two discriminating observations for each path and identify which tests would destroy critical evidence.

A companion calculator called **Weld line energy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Welding travel speed = 7 mm/s**, the declared formula returns **342.85714 J/mm**; at **Welding travel speed = 9 mm/s**, it returns **266.66667 J/mm**. On this interval the modeled value decreases, and the two-point slope is **-38.095238 J/mm per mm/s**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Do not use an isolated SEM image to declare an initiating mechanism; location, macroscopic loading and service history are critical.

### Exercises and self-assessment

**Exercise 8.3A — Physical mechanism.** How can a control specimen from an unfailed lot change the credibility of a proposed root cause? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.3B — Numerical cross-check.** Recalculate **342.85714 J/mm** from the companion formula at **7 mm/s** and compare with **266.66667 J/mm** at **9 mm/s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 8.3C — Test design.** Propose a preparation or test matrix that addresses **local treatment variation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Lesson 8.4: Selection using density, stiffness and cost

### Scientific foundation

Material selection should start from a functional objective and constraints: load, deflection, life, temperature, environment, repairability, manufacturing route and total cost. Screening indices such as E/rho or sigma_y/rho apply to specified geometries and constraints, not every component. High raw-material cost may be justified or overwhelmed by machining yield and qualification cost.

**Governing relationship or decision rule:** For fixed F and L, strength-limited tie mass scales with rho/sigma_allow; stiffness-limited tie mass scales with rho/E. Read every term in the equation as part of a declared specimen condition. In **selection using density, stiffness and cost**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For a tension tie carrying a known force, derive mass proportional to rho/sigma_allow when strength governs. Repeat for a stiffness-limited tie where mass scales with rho/E, and discuss which limit dominates a practical design.

A companion calculator called **Independent-counting fraction error** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Number of sampled points = 1164.286 samples**, the declared formula returns **0.01269027 fraction**; at **Number of sampled points = 1442.857 samples**, it returns **0.011399583 fraction**. On this interval the modeled value decreases, and the two-point slope is **-4.6332339e-06 fraction per samples**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Neither index covers joints, buckling, fire exposure, corrosion, embodied impact, supply risk or certification requirements.

### Exercises and self-assessment

**Exercise 8.4A — Physical mechanism.** Why does the optimum material for a tensile tie differ from that for a thin panel susceptible to buckling? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.4B — Numerical cross-check.** Recalculate **0.01269027 fraction** from the companion formula at **1164.286 samples** and compare with **0.011399583 fraction** at **1442.857 samples**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 8.4C — Test design.** Propose a preparation or test matrix that addresses **local treatment variation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_15 -->

## Lesson 8.5: Qualification, uncertainty and responsible publication

### Scientific foundation

Quality assurance distinguishes a reproducible calculation from a validated metallurgical process. Property requirements normally demand specified specimen geometry, calibration, sampling, heat traceability, test environment and statistical acceptance rules. Model uncertainty is separate from material scatter, equipment drift and instrument reading error, and each must be characterized for a defensible decision.

**Governing relationship or decision rule:** For independent random errors, combined standard uncertainty may be approximated by u_c=sqrt(sum u_i^2); systematic bias requires separate treatment. Read every term in the equation as part of a declared specimen condition. In **qualification, uncertainty and responsible publication**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Design a final fictional alloy-selection study with two heats, three process routes, independent microscopy and mechanical tests plus one held-out production-like part. List stopping criteria for nonuniformity and a versioned evidence package.

A companion calculator called **Weld line energy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Welding travel speed = 11 mm/s**, the declared formula returns **218.18182 J/mm**; at **Welding travel speed = 13 mm/s**, it returns **184.61538 J/mm**. On this interval the modeled value decreases, and the two-point slope is **-16.783217 J/mm per mm/s**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Synthetic educational values do not constitute mill certificates, code-compliant testing or real design allowables; independent review is mandatory for engineering service.

### Exercises and self-assessment

**Exercise 8.5A — Physical mechanism.** What evidence would justify retiring a simple model once a new batch departs from its predicted behavior? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.5B — Numerical cross-check.** Recalculate **218.18182 J/mm** from the companion formula at **11 mm/s** and compare with **184.61538 J/mm** at **13 mm/s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 8.5C — Test design.** Propose a preparation or test matrix that addresses **local treatment variation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Integrated investigation: A production gate for a joined alloy structure

### The evidence problem

A laboratory weld-plus-heat-treatment process produces attractive test coupons, but a production geometry has a thicker wall, altered restraint and inconsistent thermocouple placement. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate heat input, HAZ transformations, geometric thermal lag, residual stress and sampling uncertainty; design a hold-out qualification matrix and revision-controlled processing documentation. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **manufacturing traceability** and **coupon response versus production reliability** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Use code-applicable procedures, independent material certs, weld macrosections, traceable tests and production-like validation. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** This academic draft supplies no qualified weld procedure or design allowable. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **manufacturing traceability** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **coupon response versus production reliability** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **local treatment variation** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_15 -->

