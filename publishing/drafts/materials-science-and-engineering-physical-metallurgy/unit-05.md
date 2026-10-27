# Unit 5: Steels, cast irons and heat treatment

**Guiding question:** How should steel and cast iron microstructures be selected, verified and protected from over-interpretation?

## Why this unit matters to metallurgical decisions

A fictional steel gear has very high surface hardness but inconsistent core properties and severe dimensional change after quenching. This is a question about **austenite conditioning and steel product** and about the difference between **surface hardness versus through hardenability**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

In steels, carbon transport, austenite conditioning and transformation kinetics combine with part size to determine the final section. An ideal TTT or CCT curve is prepared for a specific starting state and cannot simply be copied onto another steel grade. A product labelled martensitic can also include retained austenite, carbides or gradients.

A material-processing statement should include the actual centerline cooling history and a cross-sectional hardness or phase map. An excellent surface reading can coexist with an inadequately hardened center; conversely, excessive stress and distortion can reduce the usefulness of an otherwise hard condition.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **composition, section size and cooling history**. For any local observation, describe why its sampling plan represents the part. Treat **retained stress and phase gradients** as an explicit rival explanation and plan **cross-sectional hardness and diffraction** as an independent check.

## Lesson 5.1: Steel grades, deoxidation and inclusions

### Scientific foundation

Steel behavior depends on carbon, manganese, chromium, nickel, molybdenum, sulfur, phosphorus, nitrogen and cleanliness as well as structure. Grades specify requirements that may include composition, product form and processing, and cannot be replaced by a generic label like 'mild steel'. Inclusion shape and orientation affect fatigue, machinability and toughness even when bulk carbon is unchanged.

**Governing relationship or decision rule:** Material qualification combines chemistry, process route, microstructure, dimension and condition-specific mechanical testing. Read every term in the equation as part of a declared specimen condition. In **steel grades, deoxidation and inclusions**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare two hypothetical low-carbon heats with equal reported yield stress but different elongated sulfide inclusion distributions. Propose transverse impact and fracture-surface tests that could detect a toughness difference.

A companion calculator called **Fictional Jominy hardness profile** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Distance from quenched end = 7.142857 mm**, the declared formula returns **43.785781 HRC**; at **Distance from quenched end = 14.28571 mm**, it returns **37.601911 HRC**. On this interval the modeled value decreases, and the two-point slope is **-0.86574189 HRC per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `30+25*Math.exp(-z/12)`. Model validity is limited to: **Hypothetical HRC profile, never measured, unrelated to an actual grade; only a curve-shape illustration**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A chemistry certificate cannot prove phase fraction, surface decarburization, inclusion morphology or heat-treatment consistency.

### Exercises and self-assessment

**Exercise 5.1A — Physical mechanism.** Why is an average inclusion count insufficient for a rare initiation-controlled failure mode? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.1B — Numerical cross-check.** Recalculate **43.785781 HRC** from the companion formula at **7.142857 mm** and compare with **37.601911 HRC** at **14.28571 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 5.1C — Test design.** Propose a preparation or test matrix that addresses **retained stress and phase gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.2: Annealing, normalizing and spheroidizing

### Scientific foundation

Different thermal routes aim at stress relief, grain refinement, softening or carbide spheroidization. Full annealing, process annealing, normalizing and spheroidizing are not synonyms; their usefulness depends on prior structure and steel grade. Heating can dissolve some constituents, but grain coarsening and decarburization can create unintended trade-offs.

**Governing relationship or decision rule:** Cooling-path time and relevant phase fractions, not nominal furnace set point alone, govern the resulting microstructure. Read every term in the equation as part of a declared specimen condition. In **annealing, normalizing and spheroidizing**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For the same invented medium-carbon steel, predict broad morphology differences after a slow furnace cool and an air cool from an austenitizing state. Suggest quantitative grain and hardness comparisons without prescribing real furnace set points.

A companion calculator called **Thermal Fourier-number estimate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Cooling or heating time = 69.28571 s**, the declared formula returns **6.9285714 dimensionless**; at **Cooling or heating time = 103.4286 s**, it returns **10.342857 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.1 dimensionless per s**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `1e-5*t/(0.01*0.01)`. Model validity is limited to: **Thermal diffusivity 1e-5 m²/s, length 10 mm; conduction scale only, not a phase or quench predictor**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Cooling media labels by themselves do not specify the thermal history of a thick or thin section; actual centerline curves matter.

### Exercises and self-assessment

**Exercise 5.2A — Physical mechanism.** Why may spheroidized carbides improve machining yet reduce as-treated strength? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.2B — Numerical cross-check.** Recalculate **6.9285714 dimensionless** from the companion formula at **69.28571 s** and compare with **10.342857 dimensionless** at **103.4286 s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 5.2C — Test design.** Propose a preparation or test matrix that addresses **retained stress and phase gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.3: Quenching, hardenability and section size

### Scientific foundation

Hardness refers to indentation resistance at a measured position; hardenability is the capacity to form a hard transformation product deep into a section under an imposed cooling condition. Alloy additions can shift transformation curves and change through-hardening, while quenching raises risks of distortion, residual stress and cracking. The Jominy end-quench method ranks depth response but must be interpreted with section geometry.

**Governing relationship or decision rule:** A simplified cooling timescale scales with L²/alpha for conduction length L and thermal diffusivity alpha. Read every term in the equation as part of a declared specimen condition. In **quenching, hardenability and section size**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Sketch two hypothetical Jominy hardness-versus-distance profiles with equal near-end hardness and different decay lengths. Then explain which one suggests greater hardenability and which additional information is required to qualify a thick shaft.

A companion calculator called **Fictional Jominy hardness profile** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Distance from quenched end = 21.42857 mm**, the declared formula returns **34.191931 HRC**; at **Distance from quenched end = 28.57143 mm**, it returns **32.311562 HRC**. On this interval the modeled value decreases, and the two-point slope is **-0.2632517 HRC per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

A fixed cooling rate at one surface does not imply a uniform rate through the part. Do not prescribe quenchants or loads from simplified slider output.

### Exercises and self-assessment

**Exercise 5.3A — Physical mechanism.** Why can a steel with higher maximum surface hardness have worse through-section hardening? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.3B — Numerical cross-check.** Recalculate **34.191931 HRC** from the companion formula at **21.42857 mm** and compare with **32.311562 HRC** at **28.57143 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 5.3C — Test design.** Propose a preparation or test matrix that addresses **retained stress and phase gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.4: Tempering, retained austenite and dimensional stability

### Scientific foundation

Temper treatments redistribute carbon, relieve stresses and evolve carbide populations in martensitic steels; strength and toughness usually trade off, but secondary hardening complicates blanket rules. Retained austenite can influence distortion, transformation-induced strain and fatigue; diffraction measurement requires crystallographic and texture correction. Surface and core may temper differently in constrained large sections.

**Governing relationship or decision rule:** A time-temperature parameter may correlate specific validated tempers, but no single universal correlation predicts every alloy's response. Read every term in the equation as part of a declared specimen condition. In **tempering, retained austenite and dimensional stability**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Track fictional hardness, retained-austenite fraction and length change across four carefully labeled post-quench states. Predict which independent signals would distinguish stress relaxation from phase decomposition.

A companion calculator called **Thermal Fourier-number estimate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Cooling or heating time = 137.5714 s**, the declared formula returns **13.757143 dimensionless**; at **Cooling or heating time = 171.7143 s**, it returns **17.171429 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.1 dimensionless per s**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

A single hardness minimum or dilatometry signal cannot uniquely identify carbide species or retained austenite; confirm with diffraction or microscopy.

### Exercises and self-assessment

**Exercise 5.4A — Physical mechanism.** Why is a 'tempering temperature' meaningless without soak time, initial state and actual part temperature? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.4B — Numerical cross-check.** Recalculate **13.757143 dimensionless** from the companion formula at **137.5714 s** and compare with **17.171429 dimensionless** at **171.7143 s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 5.4C — Test design.** Propose a preparation or test matrix that addresses **retained stress and phase gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.5: Cast irons: graphite forms, matrices and trade-offs

### Scientific foundation

Gray cast iron, ductile iron and compacted-graphite iron differ not only in total carbon but in graphite morphology and matrix constitution. Graphite shape changes local stress concentration, damping and machining behavior; austempered ductile iron adds strong dependence on heat-treatment route. Thin-wall and thick-section cooling may form different structures in the same casting.

**Governing relationship or decision rule:** Mechanical response depends jointly on graphite shape, graphite fraction and matrix phase distribution. Read every term in the equation as part of a declared specimen condition. In **cast irons: graphite forms, matrices and trade-offs**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare a gray-iron flange and a ductile-iron bracket under tensile and vibrational service; identify where damping or castability might favor the former and fatigue-sensitive ductility might favor the latter.

A companion calculator called **Fictional Jominy hardness profile** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Distance from quenched end = 35.71429 mm**, the declared formula returns **31.274667 HRC**; at **Distance from quenched end = 42.85714 mm**, it returns **30.702891 HRC**. On this interval the modeled value decreases, and the two-point slope is **-0.080048639 HRC per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Graphite nodularity and nodule count require defined image-analysis protocols. It is unsafe to infer load capacity from graphite area fraction alone.

### Exercises and self-assessment

**Exercise 5.5A — Physical mechanism.** What paired tensile and microscopy tests would demonstrate a nodularity-related performance difference? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.5B — Numerical cross-check.** Recalculate **31.274667 HRC** from the companion formula at **35.71429 mm** and compare with **30.702891 HRC** at **42.85714 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 5.5C — Test design.** Propose a preparation or test matrix that addresses **retained stress and phase gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Integrated investigation: A mismatched steel gear case and core

### The evidence problem

A fictional steel gear has very high surface hardness but inconsistent core properties and severe dimensional change after quenching. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate surface carbon, phase identity, through-thickness cooling, retained austenite, tempering and geometric restraint; evaluate hardness versus hardenability. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **austenite conditioning and steel product** and **surface hardness versus through hardenability** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Use calibrated hardness traverses, phase-sensitive diffraction, verified chemistry depth profiles and measurements of actual thermal histories. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** A target hardness alone is not a safe gear design or production recipe. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **austenite conditioning and steel product** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **surface hardness versus through hardenability** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **retained stress and phase gradients** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_9 -->

