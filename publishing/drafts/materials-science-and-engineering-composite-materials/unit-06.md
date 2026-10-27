# Unit 6: Damage, fracture, fatigue, and impact

**Guiding question:** Which competing failure mechanisms govern initiation, propagation, and residual strength?

## Why this unit matters to composite materials

A structural composite suffers a minor-looking strike and later buckles under compressive loading. This is a question about **multimode damage evolution** and the distinction between **initial nominal stress versus progressive fracture**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Composite damage is multi-mechanism: matrix cracks can precede delamination, fiber failure and residual compressive instability. An apparent surface condition is insufficient.

Mode-specific strength and fracture observations are needed, including impact history, layup, environment and inspection threshold.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **notch, cyclic history and environmental conditioning**. For any local observation, describe why its sampling plan represents the part. Treat **invisible interlaminar defects after impact** as an explicit rival explanation and plan **fractography and conditioned residual-strength coupons** as an independent check.

## Lesson 6.1: Fiber tension and matrix-dominated failure

### Scientific foundation

Longitudinal fiber fracture can dominate unidirectional tensile failure, while matrix cracks and interface debonds may appear first under transverse or off-axis loads. A nominal maximum-stress rule checks each stress component against a corresponding strength but does not predict interactions, progressive degradation or stochastic fiber breaks. Strain localization and free-edge stresses complicate coupon interpretation. Design allowables usually require statistically supported, conditioned material and process-specific data.

**Governing relationship or decision rule:** A simple directional index compares |sigma_i| to an appropriate mode- and sign-specific allowable. Read every term in the equation as part of a declared specimen condition. In **fiber tension and matrix-dominated failure**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Consider local lamina stresses sigma1=600 MPa, sigma2=35 MPa and tau12=25 MPa under a declared positive tension convention. Compare normalized values against hypothetical allowable 1200, 60 and 80 MPa. Identify which margin is lowest and explain why failure cannot be declared solely from those three independent ratios.

A companion calculator called **Directional strength-utilization index** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Positive longitudinal stress = 242.8571 MPa**, the declared formula returns **0.20238095 dimensionless**; at **Positive longitudinal stress = 385.7143 MPa**, it returns **0.32142857 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.00083333333 dimensionless per MPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `sigma/1200`. Model validity is limited to: **Unidirectional positive fiber-direction tension allowable 1200 MPa; a single uncoupled screening ratio**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A maximum-stress criterion is a screening rule, not a universal composite fracture law.

### Exercises and self-assessment

**Exercise 6.1A — Physical mechanism.** What micrograph would separate fiber tensile rupture from transverse matrix cracking after a mixed-mode coupon failure? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.1B — Numerical cross-check.** Recalculate **0.20238095 dimensionless** from the companion formula at **242.8571 MPa** and compare with **0.32142857 dimensionless** at **385.7143 MPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 6.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **invisible interlaminar defects after impact**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Lesson 6.2: Delamination and interlaminar fracture

### Scientific foundation

A laminate can separate between plies without breaking its fibers. Mode I opening, mode II sliding and mixed-mode fracture resistances are distinct and may depend on crack growth history, interfaces and bridging. Double-cantilever-beam and end-notched-flexure tests estimate particular quantities under standardized data reductions. A nominal interlaminar shear coupon does not measure mode-I fracture energy. Delamination can propagate after impact while surface damage appears slight.

**Governing relationship or decision rule:** Delamination growth is energetically plausible when mode-appropriate G reaches measured resistance, under relevant assumptions. Read every term in the equation as part of a declared specimen condition. In **delamination and interlaminar fracture**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

For a simple energy-balance demonstration compare energy release rate G=250 J/m² against illustrative critical value Gc=400 J/m², recognizing that this is not enough if mode mix or R-curve is unknown. Design a test to compare two interface film treatments, measuring initiation and propagation separately.

A companion calculator called **Mode-I delamination driving ratio** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mode-I release rate = 175 J/m2**, the declared formula returns **0.4375 dimensionless**; at **Mode-I release rate = 250 J/m2**, it returns **0.625 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.0025 dimensionless per J/m2**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `G/400`. Model validity is limited to: **Assumed independent fixed initiation resistance GIc=400 J/m2, pure opening mode, simple scalar comparison; no bridging or mixed mode**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Linear elastic G approaches need geometry, calibration and crack-front assumptions; mode mix varies along three-dimensional fronts.

### Exercises and self-assessment

**Exercise 6.2A — Physical mechanism.** Why can a specimen carry a high initial load yet have unstable delamination growth? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.2B — Numerical cross-check.** Recalculate **0.4375 dimensionless** from the companion formula at **175 J/m2** and compare with **0.625 dimensionless** at **250 J/m2**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 6.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **invisible interlaminar defects after impact**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_11 -->

## Lesson 6.3: Fatigue, environmental conditioning, and creep

### Scientific foundation

Composite fatigue can involve matrix cracking, interface damage, delamination and fiber breakage in evolving combinations. S–N curves depend on stress ratio, frequency, environment, geometry and failure definition; a stress limit from dry static tests cannot automatically transfer to wet cyclic service. Matrix-dominated deformation can be time-dependent, so higher test frequency may also change heating. Damage monitoring should distinguish cycle count from actual crack length or stiffness loss.

**Governing relationship or decision rule:** Fatigue evidence is a condition-specific relationship among cycle count, load history and a declared damage/failure criterion. Read every term in the equation as part of a declared specimen condition. In **fatigue, environmental conditioning, and creep**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Design a fatigue matrix varying only one primary variable at a time: stress ratio or humidity, with replicate coupons and temperature monitoring. Propose acoustic emission plus periodic compliance measures, and explain why neither signal alone gives a complete spatial damage map.

A companion calculator called **Directional strength-utilization index** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Positive longitudinal stress = 528.5714 MPa**, the declared formula returns **0.44047619 dimensionless**; at **Positive longitudinal stress = 671.4286 MPa**, it returns **0.55952381 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.00083333333 dimensionless per MPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Accelerated tests can introduce new mechanisms and should not be extrapolated across decades without validation.

### Exercises and self-assessment

**Exercise 6.3A — Physical mechanism.** What observation would prove that a frequency-induced lifetime change is mostly thermal rather than intrinsic cycle damage? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.3B — Numerical cross-check.** Recalculate **0.44047619 dimensionless** from the companion formula at **528.5714 MPa** and compare with **0.55952381 dimensionless** at **671.4286 MPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 6.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **invisible interlaminar defects after impact**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Lesson 6.4: Impact, barely visible damage, and CAI

### Scientific foundation

A low-velocity impact can generate internal delamination far wider than the visible surface dent. Subsequent compression-after-impact strength depends on sublaminate buckling, delamination size, stacking and support geometry. Impact energy alone does not uniquely define damage because contact stiffness, impactor shape and thickness change the stress field. Thin shells may perforate while thick laminates dissipate energy by layered damage. Residual strength must be measured in a suitable standardized fixture.

**Governing relationship or decision rule:** Residual compression strength is conditioned on measured impact-generated damage, fixture geometry and inspection limits. Read every term in the equation as part of a declared specimen condition. In **impact, barely visible damage, and cai**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Plan an impact series at several measured energies using a fixed impactor and specimen geometry. Record force–time history, ultrasonic C-scans and residual compression results. State why a smooth cosmetic exterior does not justify a part-release decision.

A companion calculator called **Mode-I delamination driving ratio** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mode-I release rate = 325 J/m2**, the declared formula returns **0.8125 dimensionless**; at **Mode-I release rate = 400 J/m2**, it returns **1 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.0025 dimensionless per J/m2**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Ultrasonic visibility and resolution depend on geometry, couplant and reconstruction settings; microcracks can evade one method.

### Exercises and self-assessment

**Exercise 6.4A — Physical mechanism.** What makes compression-after-impact a different design case from ordinary longitudinal compression? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.4B — Numerical cross-check.** Recalculate **0.8125 dimensionless** from the companion formula at **325 J/m2** and compare with **1 dimensionless** at **400 J/m2**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 6.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **invisible interlaminar defects after impact**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_11 -->

## Lesson 6.5: Joints, open holes, and structural repairs

### Scientific foundation

Bolted and bonded joints create three-dimensional load transfer, bearing, net-tension, shear-out and peel stresses. An adhesive bond may perform well in lap shear but be vulnerable to peel or contamination. Composite drilling can induce exit delamination; hole finish and fastener preload alter fatigue resistance. Scarf repairs and bonded doublers require controlled surface preparation and cure, with nondestructive inspection limits. Joining details can dominate system reliability even when parent laminate coupons appear robust.

**Governing relationship or decision rule:** Joint qualification requires locally appropriate failure-mode assessment, not only parent-laminate tensile allowables. Read every term in the equation as part of a declared specimen condition. In **joints, open holes, and structural repairs**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare two hypothetical joints carrying equal gross tensile force: a bolted two-hole lap and a bonded scarf. Build separate load paths, identify load eccentricity and likely critical surfaces, and specify tests for environmental exposure and fatigue.

A companion calculator called **Directional strength-utilization index** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Positive longitudinal stress = 814.2857 MPa**, the declared formula returns **0.67857143 dimensionless**; at **Positive longitudinal stress = 957.1429 MPa**, it returns **0.79761905 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.00083333333 dimensionless per MPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A joint's nominal section stress omits bearing contact, secondary bending and manufacturing flaws.

### Exercises and self-assessment

**Exercise 6.5A — Physical mechanism.** Why can increasing nominal adhesive area fail to improve strength when peel stresses dominate? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.5B — Numerical cross-check.** Recalculate **0.67857143 dimensionless** from the companion formula at **814.2857 MPa** and compare with **0.79761905 dimensionless** at **957.1429 MPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 6.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **invisible interlaminar defects after impact**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Integrated investigation: An impacted panel with little visible damage

### The evidence problem

A structural composite suffers a minor-looking strike and later buckles under compressive loading. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Map force history, internal delamination, sublaminate buckling and residual compression strength. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **multimode damage evolution** and **initial nominal stress versus progressive fracture** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Use controlled impact, ultrasound or tomography, fracture microscopy and conditioned residual-load tests. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Surface appearance and one impact-energy number are not adequate airworthiness or safety evidence. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **multimode damage evolution** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **initial nominal stress versus progressive fracture** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **invisible interlaminar defects after impact** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_11 -->

