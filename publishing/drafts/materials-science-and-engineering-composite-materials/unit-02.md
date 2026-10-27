# Unit 2: Micromechanics, interfaces, and homogenization

**Guiding question:** How does microgeometry transmit load and determine effective engineering constants?

## Why this unit matters to composite materials

An aligned composite exhibits high axial stiffness yet unexpectedly poor wet transverse fracture resistance. This is a question about **load transfer and effective elastic bounds** and the distinction between **ideal composite modulus versus actual damage response**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Effective elastic moduli arise from boundary assumptions and microgeometry. Iso-strain and iso-stress idealizations illustrate sensitivity but do not identify failure initiation or long-term environmental fracture.

If measured modulus disagrees with a mixture estimate, inspect fiber fraction, orientation and matrix state before treating the difference as experimental noise.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **aligned fraction, constituent elasticity and interface condition**. For any local observation, describe why its sampling plan represents the part. Treat **fiber waviness or wet interphase damage** as an explicit rival explanation and plan **matched longitudinal and transverse tests with microstructure mapping** as an independent check.

## Lesson 2.1: Axial rule of mixtures

### Scientific foundation

For long aligned continuous fibers with perfect bonding and uniform axial strain, axial extensional stiffness is a weighted sum of constituent moduli. The relation is an effective modulus estimate, not an ultimate strength guarantee. Fiber waviness, load redistribution near breaks and thermally induced residual stress defeat its simplest assumptions. If the measured axial modulus is much lower than prediction, investigate alignment and fraction before asserting bad fiber quality. Modulus uses elastic slopes in a declared strain range.

**Governing relationship or decision rule:** E1≈Vf Ef+(1−Vf)Em under aligned iso-strain conditions. Read every term in the equation as part of a declared specimen condition. In **axial rule of mixtures**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Let a hypothetical fiber modulus be 230 GPa, matrix modulus 3 GPa, and fiber volume fraction 0.55. The ideal iso-strain prediction is 127.85 GPa. Sketch how a ten-degree waviness or 3% porosity might change the result without assuming either effect is a simple linear correction. Specify an independent measurement of Vf and orientation.

A companion calculator called **Aligned axial iso-strain modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.1928571 fraction**, the declared formula returns **46.778571 GPa**; at **Fiber volume fraction = 0.2857143 fraction**, it returns **67.857143 GPa**. On this interval the modeled value increases, and the two-point slope is **227 GPa per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `230*Vf+3*(1-Vf)`. Model validity is limited to: **Long straight aligned fibers, perfect bond, Ef=230 GPa and Em=3 GPa; only small-strain axial modulus**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The estimate applies to continuous aligned small-strain response and cannot predict compression failure, toughness or lateral shear.

### Exercises and self-assessment

**Exercise 2.1A — Physical mechanism.** What contradiction would tell you that an isostrain assumption has become inappropriate? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.1B — Numerical cross-check.** Recalculate **46.778571 GPa** from the companion formula at **0.1928571 fraction** and compare with **67.857143 GPa** at **0.2857143 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 2.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **fiber waviness or wet interphase damage**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.2: Transverse load transfer and bounds

### Scientific foundation

Loading normal to aligned fibers requires stress redistribution through the softer matrix and the interface. A simple iso-stress inverse mixture gives a lower-style bound for ideal serial geometry, while more realistic microstructures lie somewhere governed by geometry and boundary conditions. The transverse modulus can be much smaller than the axial modulus even at the same constituent volume fraction. Do not apply the axial mixture as though the material were isotropic.

**Governing relationship or decision rule:** 1/Etrans≈Vf/Ef+(1−Vf)/Em is a series-style idealization. Read every term in the equation as part of a declared specimen condition. In **transverse load transfer and bounds**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

With Ef=230 GPa, Em=3 GPa and Vf=0.55, compute inverse-mixture E2≈1/(0.55/230+0.45/3) GPa. Compare its scale to E1 and state why neither equation establishes measured transverse tensile strength. Propose transverse coupon tests with microscopy and a strain-field check.

A companion calculator called **Ideal inverse-mixture transverse modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.2857143 fraction**, the declared formula returns **4.1782007 GPa**; at **Fiber volume fraction = 0.3785714 fraction**, it returns **4.7895285 GPa**. On this interval the modeled value increases, and the two-point slope is **6.5835301 GPa per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `1/(Vf/230+(1-Vf)/3)`. Model validity is limited to: **Illustrative serial isostress idealization; Ef=230 GPa, Em=3 GPa; not measured true transverse property**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Inverse mixing assumes a simple stress field and omits constraint effects, packing, residual stress and interface damage.

### Exercises and self-assessment

**Exercise 2.2A — Physical mechanism.** Why can an increasing axial fiber fraction fail to improve a matrix-dominated transverse fracture mode? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.2B — Numerical cross-check.** Recalculate **4.1782007 GPa** from the companion formula at **0.2857143 fraction** and compare with **4.7895285 GPa** at **0.3785714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 2.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **fiber waviness or wet interphase damage**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.3: Shear-lag and critical fiber length

### Scientific foundation

Discontinuous reinforcements transmit axial force through interfacial shear over a transfer length. The frequently taught critical length lcrit≈sigma_f d/(2 tau_i) is a simplified constant-shear argument balancing force in a cylindrical fiber against perimeter shear. End zones remain underloaded and orientation efficiency matters. Interface strength inferred from a fragmentation test is not a universal adhesive property because fiber strength statistics, processing residual stresses and local debonding influence the estimate.

**Governing relationship or decision rule:** lcrit≈sigma_f d/(2 tau_i), cylindrical fiber, simplified interfacial shear transfer. Read every term in the equation as part of a declared specimen condition. In **shear-lag and critical fiber length**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Assume a fiber diameter 10 micrometers, a hypothetical fiber breaking stress 2 GPa and transfer shear stress 40 MPa. Calculate critical length 0.25 mm using consistent units. Compare fibers of length 0.1 and 5 mm, explaining why only the latter approaches long-fiber behavior in the elementary picture and why matrix damage changes the answer.

A companion calculator called **Aligned axial iso-strain modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.3785714 fraction**, the declared formula returns **88.935714 GPa**; at **Fiber volume fraction = 0.4714286 fraction**, it returns **110.01429 GPa**. On this interval the modeled value increases, and the two-point slope is **227 GPa per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Uniform transfer shear and constant fiber strength are rarely exact; the formula is not a design allowables method.

### Exercises and self-assessment

**Exercise 2.3A — Physical mechanism.** What failure observation distinguishes weak interfacial transfer from fiber failure caused by a surface flaw? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.3B — Numerical cross-check.** Recalculate **88.935714 GPa** from the companion formula at **0.3785714 fraction** and compare with **110.01429 GPa** at **0.4714286 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 2.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **fiber waviness or wet interphase damage**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.4: Interphase, adhesion, and environmental aging

### Scientific foundation

The fiber-matrix interphase may differ from bulk resin by chemistry, mobility, moisture uptake and residual stress. Stronger interface transfer is not always synonymous with better impact toughness, because delamination and pull-out can dissipate energy in some architectures. Surface treatment, sizing, plasma exposure and coupling chemistry can change both adhesion and processability. Water can diffuse along defects, change polymer properties or enable degradation, making a dry coupon correlation unreliable in humid service.

**Governing relationship or decision rule:** A credible interface assessment combines micromechanics with direct or orthogonal damage observations. Read every term in the equation as part of a declared specimen condition. In **interphase, adhesion, and environmental aging**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Design paired treated/untreated fiber laminates with identical fiber fraction and cure schedule. Measure transverse response, interlaminar fracture resistance and aged specimens after controlled conditioning. If a stronger interface increases the initiation load but shortens stable crack-growth displacement, explain the competing interpretation.

A companion calculator called **Ideal inverse-mixture transverse modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.4714286 fraction**, the declared formula returns **5.6104077 GPa**; at **Fiber volume fraction = 0.5642857 fraction**, it returns **6.7708698 GPa**. On this interval the modeled value increases, and the two-point slope is **12.497284 GPa per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Single-fiber pull-out tests probe particular stress states, not all laminate failure modes.

### Exercises and self-assessment

**Exercise 2.4A — Physical mechanism.** How would you detect a moisture-induced interphase change when gravimetric uptake is almost equal? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.4B — Numerical cross-check.** Recalculate **5.6104077 GPa** from the companion formula at **0.4714286 fraction** and compare with **6.7708698 GPa** at **0.5642857 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 2.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **fiber waviness or wet interphase damage**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.5: Thermal mismatch and residual microstress

### Scientific foundation

Constituents with different coefficients of thermal expansion constrain each other during cooling after cure. This generates residual local stresses even when an unconstrained part appears flat, and can affect transverse matrix cracking. Composite directional thermal expansion depends on phase stiffness and fractions; a naive volume-weighted expansion may neglect mechanics of constraint. A symmetric layup can eliminate some global coupling while retaining local microstresses. Tool expansion and vitrification timing also affect residual curvature.

**Governing relationship or decision rule:** Free thermal strain is alpha ΔT, but phase compatibility and stiffness govern constrained stress. Read every term in the equation as part of a declared specimen condition. In **thermal mismatch and residual microstress**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Calculate a free thermal strain from alpha=25e-6 /K and a 100 K temperature change: 0.0025. Compare a carbon-fiber-dominated zero-or-negative axial expansion pathway. Sketch a constrained matrix pocket and predict whether a microcrack might form during cooldown or during subsequent heating; propose a thermal cycling experiment.

A companion calculator called **Aligned axial iso-strain modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fiber volume fraction = 0.5642857 fraction**, the declared formula returns **131.09286 GPa**; at **Fiber volume fraction = 0.6571429 fraction**, it returns **152.17143 GPa**. On this interval the modeled value increases, and the two-point slope is **227 GPa per fraction**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Cure shrinkage, viscoelastic relaxation and nonuniform temperatures invalidate a purely elastic thermal mismatch estimate.

### Exercises and self-assessment

**Exercise 2.5A — Physical mechanism.** Why does a geometrically flat laminate still contain residual stress? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.5B — Numerical cross-check.** Recalculate **131.09286 GPa** from the companion formula at **0.5642857 fraction** and compare with **152.17143 GPa** at **0.6571429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 2.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **fiber waviness or wet interphase damage**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Integrated investigation: A modulus that fails to predict fracture

### The evidence problem

An aligned composite exhibits high axial stiffness yet unexpectedly poor wet transverse fracture resistance. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate iso-strain stiffness, transverse stress transfer, interface chemistry and environment-related changes. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **load transfer and effective elastic bounds** and **ideal composite modulus versus actual damage response** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Measure orientation, interphase, conditioned transverse strength and appropriate fracture energy with independent methods. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Simple elastic mixture bounds do not qualify interfaces or damage progression. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **load transfer and effective elastic bounds** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **ideal composite modulus versus actual damage response** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **fiber waviness or wet interphase damage** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_3 -->

