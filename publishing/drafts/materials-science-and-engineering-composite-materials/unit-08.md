# Unit 8: Testing, reliability, repair, and circularity

**Guiding question:** What evidence is necessary to justify a composite component through its entire life?

## Why this unit matters to composite materials

A startup has only attractive pilot-coupon tests for a composite enclosure intended for decades of service. This is a question about **reliability, observability and life-cycle evidence** and the distinction between **lab coupon repeatability versus production and service qualification**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Composites need an evidence chain from raw constituents through manufacturing and service inspection to repair or disposal. Precision in one coupon is not confidence for a population.

Declare limitations of a nondestructive detection method and the statistical hierarchy before deriving life predictions from observed laboratory scatter.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **batch provenance, environment, flaw detectability and maintenance**. For any local observation, describe why its sampling plan represents the part. Treat **sampling bias or unvalidated inspection procedure** as an explicit rival explanation and plan **independent lot sampling and documented hold-out component tests** as an independent check.

## Lesson 8.1: Mechanical testing and statistical allowables

### Scientific foundation

Tensile, compression, shear, fracture and impact fixtures probe different failure mechanisms and can produce different apparent material rankings. Coupon architecture, conditioning, dimensions and strain measurement must be controlled and recorded. A-basis or B-basis allowables are statistical concepts requiring appropriate sampling, distributional assumptions and production controls, not a convenient reduction factor on one mean. Repeat scans of one coupon are not independent manufactured specimens.

**Governing relationship or decision rule:** Qualification statements require representativeness, defined confidence and population coverage, plus traceable test conditions. Read every term in the equation as part of a declared specimen condition. In **mechanical testing and statistical allowables**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Construct a hierarchical qualification matrix spanning material lots, cure batches, panels, coupon positions, test temperatures and moisture conditions. Separate within-panel scatter from lot-to-lot variation and predeclare failure-mode acceptance before opening the results.

A companion calculator called **Illustrative ultrasonic POD curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Flaw size = 1.228571 mm**, the declared formula returns **9.8474942 % detection**; at **Flaw size = 2.357143 mm**, it returns **30.926207 % detection**. On this interval the modeled value increases, and the two-point slope is **18.677341 % detection per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `100/(1+Math.exp(-(a-3)/0.8))`. Model validity is limited to: **Hypothetical logistics-style curve midpoint 3 mm, width 0.8 mm; NOT a validated probability-of-detection result**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A nominal 95% confidence interval for an average is not automatically a lower tolerance bound for an individual manufactured part.

### Exercises and self-assessment

**Exercise 8.1A — Physical mechanism.** Why is a high test-sample count insufficient when every coupon comes from one panel? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.1B — Numerical cross-check.** Recalculate **9.8474942 % detection** from the companion formula at **1.228571 mm** and compare with **30.926207 % detection** at **2.357143 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 8.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **sampling bias or unvalidated inspection procedure**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Lesson 8.2: Nondestructive evaluation and damage observability

### Scientific foundation

Ultrasonic C-scan, phased array, thermography, shearography, radiography and acoustic emission have different sensitivities to porosity, delamination, disbonds and matrix microcracks. Detection thresholds change with part curvature, thickness, orientation and calibration artifacts. An inspection that finds no indication only bounds the detectable flaw set for that procedure. Probability of detection must consider representative flaw sizes, operators and conditions.

**Governing relationship or decision rule:** Detection capability is expressed conditionally on flaw type, size, geometry and procedure; absence of indications is not proof of absence of damage. Read every term in the equation as part of a declared specimen condition. In **nondestructive evaluation and damage observability**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Build a flaw library containing manufactured voids, inserts, wrinkles and impact damage, along with validated destructive section controls. Compare results from ultrasound and X-ray CT and document which defects each method misses.

A companion calculator called **Recovered fiber mass proxy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Material recovery yield = 27.14286 %**, the declared formula returns **20.357143 kg**; at **Material recovery yield = 40.71429 %**, it returns **30.535714 kg**. On this interval the modeled value increases, and the two-point slope is **0.75 kg per %**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `75*r/100`. Model validity is limited to: **Hypothetical 100 kg feed with 75 kg fiber; yield is retained fiber mass fraction; excludes quality losses, emissions, energy, circularity**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Artificial flat-bottom holes or inserted films may not reproduce real manufacturing defects or full inspection response.

### Exercises and self-assessment

**Exercise 8.2A — Physical mechanism.** What evidence is needed before interpreting a negative ultrasonic scan as a safety assurance? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.2B — Numerical cross-check.** Recalculate **20.357143 kg** from the companion formula at **27.14286 %** and compare with **30.535714 kg** at **40.71429 %**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 8.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **sampling bias or unvalidated inspection procedure**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_15 -->

## Lesson 8.3: Uncertainty, model validation, and digital twins

### Scientific foundation

A composite structural model contains constituent data, layup definition, mesh, failure criteria, boundary conditions and uncertain manufacturing state. Verifying that software solves the written equations is distinct from validating those equations against representative experiments. Fitting and testing on the same coupon series conceals out-of-sample error. Sensitivity studies should probe orientation, thickness and flaw populations as well as modulus inputs; it is misleading to adjust arbitrary constants until one test curve is matched.

**Governing relationship or decision rule:** Verification checks implementation; validation tests how well an explicitly bounded model represents independent observations. Read every term in the equation as part of a declared specimen condition. In **uncertainty, model validation, and digital twins**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Propose a progression from analytic laminate calculation to coupon finite element model, component test and blind hold-out assembly. Use recorded residuals and confidence limits, not just matching peak force. Include a falsification case that challenges the predicted failure location.

A companion calculator called **Illustrative ultrasonic POD curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Flaw size = 3.485714 mm**, the declared formula returns **64.728877 % detection**; at **Flaw size = 4.614286 mm**, it returns **88.265925 % detection**. On this interval the modeled value increases, and the two-point slope is **20.855612 % detection per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A beautifully converged mesh can yield a precisely wrong answer when loading or damage physics are misspecified.

### Exercises and self-assessment

**Exercise 8.3A — Physical mechanism.** Which independent test would most strongly falsify a model calibrated only on unnotched tension? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.3B — Numerical cross-check.** Recalculate **64.728877 % detection** from the companion formula at **3.485714 mm** and compare with **88.265925 % detection** at **4.614286 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 8.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **sampling bias or unvalidated inspection procedure**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Lesson 8.4: Inspection, bonded repair, and service decisions

### Scientific foundation

Field damage assessment begins with a credible record of impact, environment and load, followed by a mapped damage zone. The repair decision depends on accessible surfaces, allowable heating, adhesive shelf-life and verified bond quality. Cosmetic surface finish is not a sufficient criterion for returning a structural composite to service. Repairs create local changes of stiffness, residual stress and bondline chemistry; documentation should include training, tools, cure logs and post-repair inspection.

**Governing relationship or decision rule:** A repair must restore defined performance with traceable process and inspection evidence. Read every term in the equation as part of a declared specimen condition. In **inspection, bonded repair, and service decisions**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Write a repair decision tree distinguishing damage below inspection capability, visible delamination, through-thickness perforation and uncertain bond preparation. For each case state what information is still needed before any go/no-go decision, and how a controlled proof test might damage an already weakened structure.

A companion calculator called **Recovered fiber mass proxy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Material recovery yield = 54.28571 %**, the declared formula returns **40.714286 kg**; at **Material recovery yield = 67.85714 %**, it returns **50.892857 kg**. On this interval the modeled value increases, and the two-point slope is **0.75 kg per %**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Repair practices for aircraft or pressure systems must follow approved engineering instructions and applicable rules; an educational algorithm cannot authorize service.

### Exercises and self-assessment

**Exercise 8.4A — Physical mechanism.** Why is a successful tap test insufficient to qualify an adhesive repair? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.4B — Numerical cross-check.** Recalculate **40.714286 kg** from the companion formula at **54.28571 %** and compare with **50.892857 kg** at **67.85714 %**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 8.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **sampling bias or unvalidated inspection procedure**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_15 -->

## Lesson 8.5: Life-cycle inventories, recycling, and design for disassembly

### Scientific foundation

Crosslinked thermoset composites, thermoplastics and mineral-fiber products differ in separation, reprocessing and possible recovery pathways. Pyrolysis or solvolysis may recover fibers, but energy inputs, fiber damage, solvent management, emissions and lower-value applications matter. Mechanical size reduction changes reinforcement length; recovered fiber identity is not equivalent to virgin tow quality. Lightweighting can reduce use-phase energy for some vehicles while making manufacturing and recycling burdens larger; quantify the functional use case.

**Governing relationship or decision rule:** Functional-unit life-cycle assessment is a scenario-specific accounting framework, not an intrinsic material-property ranking. Read every term in the equation as part of a declared specimen condition. In **life-cycle inventories, recycling, and design for disassembly**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare two hypothetical panels delivering the same bending stiffness over a specified service life. Build inventories for feedstock, fabrication scrap, transport, repair, energy in use and end-of-life with regional scenarios. Define sensitivity to actual collection rate and recovery yield rather than claiming recycling benefits from lab feasibility alone.

A companion calculator called **Illustrative ultrasonic POD curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Flaw size = 5.742857 mm**, the declared formula returns **96.858563 % detection**; at **Flaw size = 6.871429 mm**, it returns **99.214942 % detection**. On this interval the modeled value increases, and the two-point slope is **2.0879304 % detection per mm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A process mass yield is not the same as closed-loop high-quality material recovery, and end-of-life pathways are highly location-dependent.

### Exercises and self-assessment

**Exercise 8.5A — Physical mechanism.** Why can a lighter thermoset panel be worse on some impact indicators than a heavier reparable alternative? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 8.5B — Numerical cross-check.** Recalculate **96.858563 % detection** from the companion formula at **5.742857 mm** and compare with **99.214942 % detection** at **6.871429 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 8.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **sampling bias or unvalidated inspection procedure**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_14 -->

## Integrated investigation: Qualification before market introduction

### The evidence problem

A startup has only attractive pilot-coupon tests for a composite enclosure intended for decades of service. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Plan independent manufacturing lots, environments, component loading, NDE detection limits, repair feasibility and end-of-life scenarios. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **reliability, observability and life-cycle evidence** and **lab coupon repeatability versus production and service qualification** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Run gated evidence reviews with traceable raw measurements, blind hold-outs and conservative limits of applicability. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Educational simulations, even numerically verified, cannot certify safety-critical performance. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **reliability, observability and life-cycle evidence** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **lab coupon repeatability versus production and service qualification** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **sampling bias or unvalidated inspection procedure** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_15 -->

