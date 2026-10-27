# Unit 5: Manufacturing, cure, consolidation, and defects

**Guiding question:** How does the manufacturing process create the structure and flaw population?

## Why this unit matters to composite materials

A larger curved panel develops dry regions and wrinkles despite passing flat-coupon process trials. This is a question about **process-driven consolidation and defect distribution** and the distinction between **machine setpoints versus verified internal material state**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Processing is a material transformation, not merely a logistics step. Flow, consolidation, reaction kinetics and cool-down establish the defect population and residual state.

Scale-up trials need measurements from actual thick regions, corners, ply drops and bondlines rather than only ideal flat coupons.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **actual thermal history, flow path and pressure**. For any local observation, describe why its sampling plan represents the part. Treat **race tracking or buried tow wrinkle** as an explicit rival explanation and plan **sensor log comparison with ultrasound and destructive sections** as an independent check.

## Lesson 5.1: Thermoset cure kinetics and vitrification

### Scientific foundation

Thermoset composites often cure through temperature-dependent chemical reactions followed by vitrification as the network glass transition rises. Cure exotherm, thick-section heat transfer, mobility and tool thermal history interact. Degree of cure is not synonymous with temperature or a single hold time; a resin can show spatial gradients. Excessive peak temperature can generate residual stress or degrade material. A simple first-order conversion relation may be instructive but rarely predicts a real autoclave cycle.

**Governing relationship or decision rule:** An illustrative first-order conversion model is alpha=1−exp(−kt); k must be independently measured. Read every term in the equation as part of a declared specimen condition. In **thermoset cure kinetics and vitrification**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare two hypothetical panels with identical measured surface cure temperature but different midplane exotherms. Use a one-parameter exponential teaching law only to show sensitivity, then propose embedded thermocouples, DSC residual enthalpy and DMA Tg to establish actual cure.

A companion calculator called **Ideal first-order cure conversion** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Isothermal cure time = 17.14286 min**, the declared formula returns **45.118836 % conversion**; at **Isothermal cure time = 34.28571 min**, it returns **69.880579 % conversion**. On this interval the modeled value increases, and the two-point slope is **1.444435 % conversion per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `100*(1-Math.exp(-0.035*t))`. Model validity is limited to: **Hypothetical first-order rate 0.035/min, isothermal, no diffusion limitation or cure exotherm**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Cure kinetics can be autocatalytic and diffusion-controlled, and uncured constituents may require hazardous-handling procedures.

### Exercises and self-assessment

**Exercise 5.1A — Physical mechanism.** Why is an oven setpoint insufficient evidence that the resin reached a uniform cured state? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.1B — Numerical cross-check.** Recalculate **45.118836 % conversion** from the companion formula at **17.14286 min** and compare with **69.880579 % conversion** at **34.28571 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 5.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **race tracking or buried tow wrinkle**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.2: Prepreg, layup, and autoclave consolidation

### Scientific foundation

Prepreg layup controls fiber direction and resin content prior to cure. Debulking, bag sealing, vacuum integrity, compaction pressure and resin flow affect voids and local thickness. A manufacturer can meet average fiber fraction while leaving wrinkles near a corner or porosity at a spar transition. Resin bleed and volatile removal interact with gelation; indiscriminate pressure increases do not guarantee defect-free laminates. Traceability must follow individual prepreg batches and out-times.

**Governing relationship or decision rule:** Local thickness, void content and fiber orientation are measurable results of the process, not guaranteed by commanded pressure. Read every term in the equation as part of a declared specimen condition. In **prepreg, layup, and autoclave consolidation**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Draft a layup traveller recording ply orientation, material lot, refrigerated storage, out-time, bag leak check, tool ID and cure sensor locations. Predict two signatures for trapped air versus volatile outgassing and design an inspection series to discriminate them.

A companion calculator called **Darcy superficial infusion velocity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Porous permeability = 15 10^-12 m2**, the declared formula returns **3 micrometers/s**; at **Porous permeability = 22 10^-12 m2**, it returns **4.4 micrometers/s**. On this interval the modeled value increases, and the two-point slope is **0.2 micrometers/s per 10^-12 m2**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `K*1e-12*100000/0.5*1000000`. Model validity is limited to: **Pressure gradient 100 kPa/m, viscosity 0.5 Pa s, one-dimensional Darcy flow without race tracking or variable cure viscosity**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A process log documents setpoints but not the actual internal microstructure or fracture resistance.

### Exercises and self-assessment

**Exercise 5.2A — Physical mechanism.** Which manufacturing observation would most directly refute a claim of uniform consolidation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.2B — Numerical cross-check.** Recalculate **3 micrometers/s** from the companion formula at **15 10^-12 m2** and compare with **4.4 micrometers/s** at **22 10^-12 m2**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 5.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **race tracking or buried tow wrinkle**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.3: Resin infusion and flow front control

### Scientific foundation

Liquid composite molding drives resin through a porous fiber preform. Permeability depends on reinforcement packing, tow architecture and direction; Darcy's law is an idealized low-Reynolds-number description. Race tracking can cause edge flow ahead of bulk impregnation, trapping dry regions. Resin viscosity and pot life evolve during filling, so a successful bench wet-out result may not scale to a thicker part. Tooling and infusion strategy must control leak paths and vents.

**Governing relationship or decision rule:** Superficial Darcy velocity magnitude is |v|=K|grad p|/mu in an ideal porous medium. Read every term in the equation as part of a declared specimen condition. In **resin infusion and flow front control**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Suppose pressure gradient 100 kPa/m, permeability 1e−11 m² and viscosity 0.5 Pa s. Compute superficial Darcy speed 2e−6 m/s; emphasize the distinction from actual local pore velocity. Explain how an edge gap can change flow-front topology at unchanged average permeability.

A companion calculator called **Ideal first-order cure conversion** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Isothermal cure time = 51.42857 min**, the declared formula returns **83.470111 % conversion**; at **Isothermal cure time = 68.57143 min**, it returns **90.928205 % conversion**. On this interval the modeled value increases, and the two-point slope is **0.43505545 % conversion per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Darcy idealization neglects dual-scale tow impregnation, cure viscosity change and severe race tracking.

### Exercises and self-assessment

**Exercise 5.3A — Physical mechanism.** Why can increasing vacuum fail to remove a dry region behind an advanced edge flow front? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.3B — Numerical cross-check.** Recalculate **83.470111 % conversion** from the companion formula at **51.42857 min** and compare with **90.928205 % conversion** at **68.57143 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 5.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **race tracking or buried tow wrinkle**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.4: Thermoplastic consolidation and welding

### Scientific foundation

Thermoplastic composite tapes can be heated, placed and consolidated without chemical thermoset curing, but intimate contact and polymer chain interdiffusion at a bond are still required. Insufficient surface temperature, pressure or dwell leads to voids and weak interlaminar interfaces. Excess temperature may induce oxidation or degradation. Crystallization and cooling rate alter stiffness and shrinkage. Laser heating, induction and resistance welding create different thermal distributions.

**Governing relationship or decision rule:** Bond quality depends on intimate contact, sufficient segmental mobility and controlled solidification without damaging the material. Read every term in the equation as part of a declared specimen condition. In **thermoplastic consolidation and welding**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare two weld coupons with the same nominal peak setpoint but different contact pressures and dwell times. Propose thermography, cross-section porosity, lap-shear testing and failure-surface examination. Separate bond formation kinetics from apparent resin softening observed in a short temperature ramp.

A companion calculator called **Darcy superficial infusion velocity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Porous permeability = 29 10^-12 m2**, the declared formula returns **5.8 micrometers/s**; at **Porous permeability = 36 10^-12 m2**, it returns **7.2 micrometers/s**. On this interval the modeled value increases, and the two-point slope is **0.2 micrometers/s per 10^-12 m2**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A temperature history alone does not establish interface healing; contamination and roughness must be measured.

### Exercises and self-assessment

**Exercise 5.4A — Physical mechanism.** Why might a weld pass an initial shear test yet fail under cyclic peel loading? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.4B — Numerical cross-check.** Recalculate **5.8 micrometers/s** from the companion formula at **29 10^-12 m2** and compare with **7.2 micrometers/s** at **36 10^-12 m2**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 5.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **race tracking or buried tow wrinkle**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.5: Automated placement, inspection, and process scale

### Scientific foundation

Automated fiber placement can improve geometric repeatability while producing tow gaps, overlaps, wrinkles and steering defects. These are not all equivalent to fiber-volume loss: overlap may create local thickness and buckling effects, while a gap can redistribute load. Defect severity depends on size, orientation, laminate position and load path. Machine sensor output can detect process anomalies but must be calibrated against actual part state. Process scale-up changes geometric constraints and inspection access.

**Governing relationship or decision rule:** Manufacturing qualification requires spatially representative defect and response measurements linked to process settings. Read every term in the equation as part of a declared specimen condition. In **automated placement, inspection, and process scale**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare a small flat coupon with a curved stiffened panel placed using identical nominal tow settings. Map curvature, steering radius, compaction temperature and tow tension. Select defect populations to track using profilometry, ultrasound and sections; link each to a particular expected strength effect.

A companion calculator called **Ideal first-order cure conversion** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Isothermal cure time = 85.71429 min**, the declared formula returns **95.021293 % conversion**; at **Isothermal cure time = 102.8571 min**, it returns **97.267628 % conversion**. On this interval the modeled value increases, and the two-point slope is **0.13103618 % conversion per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

A camera may detect visible surface gaps but miss buried waviness or bond defects.

### Exercises and self-assessment

**Exercise 5.5A — Physical mechanism.** Which additional inspection would distinguish a harmless surface tow overlap from a structural ply wrinkle? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.5B — Numerical cross-check.** Recalculate **95.021293 % conversion** from the companion formula at **85.71429 min** and compare with **97.267628 % conversion** at **102.8571 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 5.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **race tracking or buried tow wrinkle**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Integrated investigation: Resin-starved corners in scaled manufacturing

### The evidence problem

A larger curved panel develops dry regions and wrinkles despite passing flat-coupon process trials. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate tow geometry, Darcy-like porous flow, pressure control, thermal gradients and cure-dependent viscosity. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **process-driven consolidation and defect distribution** and **machine setpoints versus verified internal material state** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Combine tooling sensor logs with mapped defect sections and orthogonal NDE; test a deliberately controlled revised process. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** A machine setting is not the same as verified local material quality. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **process-driven consolidation and defect distribution** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **machine setpoints versus verified internal material state** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **race tracking or buried tow wrinkle** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_9 -->

