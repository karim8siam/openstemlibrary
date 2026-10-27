# Unit 3: Solidification, segregation and foundry structure

**Guiding question:** Why do two castings with the same alloy composition sometimes have very different mechanical performance?

## Why this unit matters to metallurgical decisions

A thick pump housing has porosity near one internal corner and unexplained compositional banding, despite a mean composition that meets a target. This is a question about **solidification front and solute conservation** and about the difference between **feeding versus interface morphology**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Real casting structures inherit both the advancing solidification front and the liquid that feeds it. Solute rejection can make terminal liquid chemically distinct from the first solid; interdendritic regions can have different melting behavior. The thermal gradient and convection field must be treated as spatial conditions instead of one nominal cooling-rate number.

A small defect can become the limiting feature when fatigue or leak tightness governs. Measure extreme pore populations as well as mean porosity and record section depth. One polished plane is rarely enough to reconstruct a three-dimensional network of feeding deficiencies, entrained films or gas cavities.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **thermal gradient and melt transport**. For any local observation, describe why its sampling plan represents the part. Treat **defect localization** as an explicit rival explanation and plan **cross-sectional tomography** as an independent check.

## Lesson 3.1: Nucleation, inoculation and initial grains

### Scientific foundation

A cast microstructure depends on the potency and number of heterogeneous nucleation sites, cooling conditions and growth competition. Inoculants can promote equiaxed grains but their success depends on chemistry, fading and melt cleanliness. Many apparent grains are dendrite envelopes and should not be equated with individual solute precipitates.

**Governing relationship or decision rule:** If grain count per unit volume increases under otherwise equal conditions, a characteristic three-dimensional spacing scales roughly as N^(-1/3). Read every term in the equation as part of a declared specimen condition. In **nucleation, inoculation and initial grains**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare two hypothetical moulds with the same alloy but different effective nucleation density. Predict qualitative grain size and show why grain-refinement claims require representative sectioning and an identical thermal history.

A companion calculator called **Scheil residual-liquid enrichment** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fraction solid = 0.1142857 fraction**, the declared formula returns **0.042502372 fraction**; at **Fraction solid = 0.2285714 fraction**, it returns **0.045542003 fraction**. On this interval the modeled value increases, and the two-point slope is **0.026596776 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `0.04*Math.pow(1-fs,-0.5)`. Model validity is limited to: **Initial solute fraction 0.04, partition coefficient k=0.5, completely mixed liquid, zero solid back-diffusion; not final-eutectic predictor**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

More particles in the melt do not automatically create more effective nuclei; many remain inactive because of poor wetting, orientation or dissolution.

### Exercises and self-assessment

**Exercise 3.1A — Physical mechanism.** Which sectioning and chemical analysis would separate successful inoculation from improved cooling alone? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.1B — Numerical cross-check.** Recalculate **0.042502372 fraction** from the companion formula at **0.1142857 fraction** and compare with **0.045542003 fraction** at **0.2285714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 3.1C — Test design.** Propose a preparation or test matrix that addresses **defect localization**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.2: Dendrite morphology and thermal gradient

### Scientific foundation

At a moving solidification front, constitutional undercooling can destabilize a planar interface and favor cellular or dendritic growth. Primary spacing depends jointly on thermal gradient, growth velocity, interfacial physics and convection; there is no alloy-independent one-parameter law. Dendrite orientation may be epitaxial across adjacent grains.

**Governing relationship or decision rule:** A simplified stability criterion compares the actual liquid thermal gradient with the liquidus gradient generated by solute rejection. Read every term in the equation as part of a declared specimen condition. In **dendrite morphology and thermal gradient**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Draw the temperature and composition fields ahead of an imagined binary alloy front, vary the growth velocity with fixed thermal gradient and predict when constitutional undercooling becomes more likely. Describe where solute-rich interdendritic liquid accumulates.

A companion calculator called **Solidification shrinkage volume** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Starting liquid volume = 128.5714 cm³**, the declared formula returns **5.1428571 cm³**; at **Starting liquid volume = 182.8571 cm³**, it returns **7.3142857 cm³**. On this interval the modeled value increases, and the two-point slope is **0.04 cm³ per cm³**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `0.04*v`. Model validity is limited to: **Assumed 4% volume shrinkage from initial liquid volume; ideal conservation estimate, not a riser design**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A microscope image alone usually cannot recover the growth speed or actual front gradient; a calibrated thermal or simulation history is necessary.

### Exercises and self-assessment

**Exercise 3.2A — Physical mechanism.** Why are secondary dendrite arm spacings useful markers yet poor universal process clocks? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.2B — Numerical cross-check.** Recalculate **5.1428571 cm³** from the companion formula at **128.5714 cm³** and compare with **7.3142857 cm³** at **182.8571 cm³**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 3.2C — Test design.** Propose a preparation or test matrix that addresses **defect localization**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.3: Solute redistribution and microsegregation

### Scientific foundation

During non-equilibrium freezing, solid and liquid usually differ in solute concentration. The Scheil idealization assumes a well-mixed liquid, negligible diffusion in solid and constant partition coefficient; its calculated terminal enrichment can become unphysical near complete solidification because new phases intervene. Homogenization treatments attempt to reduce solid-state segregation but cannot automatically remove pores or inclusions.

**Governing relationship or decision rule:** Ideal Scheil residual liquid: c_L=c_0(1-f_s)^(k-1) under restrictive assumptions. Read every term in the equation as part of a declared specimen condition. In **solute redistribution and microsegregation**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Use initial solute fraction 0.04, k=0.5 and solid fraction 0.75 to obtain residual-liquid composition c_L=c0(1-f_s)^(k-1)=0.08. State the domain and contrast with an equilibrium solidification bound.

A companion calculator called **Scheil residual-liquid enrichment** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fraction solid = 0.3428571 fraction**, the declared formula returns **0.049343516 fraction**; at **Fraction solid = 0.4571429 fraction**, it returns **0.054289671 fraction**. On this interval the modeled value increases, and the two-point slope is **0.043278856 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Convection, back-diffusion and temperature-dependent k can invalidate a simple Scheil prediction. Do not apply it to multicomponent commercial alloy chemistry without appropriate phase accounting.

### Exercises and self-assessment

**Exercise 3.3A — Physical mechanism.** How would an EPMA traverse test the presence of coring across dendrite arms? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.3B — Numerical cross-check.** Recalculate **0.049343516 fraction** from the companion formula at **0.3428571 fraction** and compare with **0.054289671 fraction** at **0.4571429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 3.3C — Test design.** Propose a preparation or test matrix that addresses **defect localization**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.4: Shrinkage, feeding and casting defects

### Scientific foundation

Porosity can arise through insufficient feeding of solidification shrinkage, gas evolution or both; microscopy contrast alone seldom identifies the dominant origin. Oxide films and bifilms can reduce fatigue resistance even when standard bulk density seems acceptable. Directional solidification and riser placement are engineering design tasks tied to local thermal modulus and liquid permeability.

**Governing relationship or decision rule:** A bulk conservation estimate gives Delta V≈beta V_liquid; it ignores feeding efficiency and spatial solidification path. Read every term in the equation as part of a declared specimen condition. In **shrinkage, feeding and casting defects**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Construct a volume ledger for a fictional casting that contracts by 4% on freezing; calculate 8 cubic centimeters of feed volume for a 200 cubic-centimeter initially liquid region if the percentage refers to that initial volume. Discuss why this ideal volume is not a riser design.

A companion calculator called **Solidification shrinkage volume** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Starting liquid volume = 237.1429 cm³**, the declared formula returns **9.4857143 cm³**; at **Starting liquid volume = 291.4286 cm³**, it returns **11.657143 cm³**. On this interval the modeled value increases, and the two-point slope is **0.04 cm³ per cm³**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Feeding paths can block before the final volume contracts and hot tearing depends on strength and constraint near the solidus.

### Exercises and self-assessment

**Exercise 3.4A — Physical mechanism.** What evidence separates entrained gas bubbles from interdendritic shrinkage pores? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.4B — Numerical cross-check.** Recalculate **9.4857143 cm³** from the companion formula at **237.1429 cm³** and compare with **11.657143 cm³** at **291.4286 cm³**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 3.4C — Test design.** Propose a preparation or test matrix that addresses **defect localization**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.5: Solidification routes and additive manufacturing

### Scientific foundation

Casting, welding and directed-energy deposition involve different melt-pool thermal gradients and repeated reheating. Rapid solidification may refine cell spacing while increasing residual stress and retaining nonequilibrium segregation. Porosity, keyholing, lack of fusion and anisotropy demand independent evaluation rather than a single claim of fine microstructure.

**Governing relationship or decision rule:** A temperature gradient and interface velocity jointly control many freezing textures; neither is recovered uniquely from a single micrograph. Read every term in the equation as part of a declared specimen condition. In **solidification routes and additive manufacturing**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare a conventional cast coupon with a hypothetical powder-bed fusion coupon at equal chemistry. List predicted differences in grain texture, cooling rate, pores and residual stress, then design a microscopy-plus-mechanics qualification matrix.

A companion calculator called **Scheil residual-liquid enrichment** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Fraction solid = 0.5714286 fraction**, the declared formula returns **0.061101009 fraction**; at **Fraction solid = 0.6857143 fraction**, it returns **0.071350607 fraction**. On this interval the modeled value increases, and the two-point slope is **0.089683978 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Cooling rate is not identical everywhere within an additively manufactured part, and an observed cell size is only an indirect thermal-rate proxy.

### Exercises and self-assessment

**Exercise 3.5A — Physical mechanism.** Which independent measurements would test whether a process yields consistent properties over the build height? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.5B — Numerical cross-check.** Recalculate **0.061101009 fraction** from the companion formula at **0.5714286 fraction** and compare with **0.071350607 fraction** at **0.6857143 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 3.5C — Test design.** Propose a preparation or test matrix that addresses **defect localization**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Integrated investigation: Casting defects in a hypothetical pump housing

### The evidence problem

A thick pump housing has porosity near one internal corner and unexplained compositional banding, despite a mean composition that meets a target. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Build a directional-solidification hypothesis, compute a synthetic Scheil enrichment, and test feeding, dissolved gas and oxide entrainment as separate failure mechanisms. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **solidification front and solute conservation** and **feeding versus interface morphology** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Use X-ray CT, cut-up metallography, EPMA traverses and measured cooling curves with stated gauge locations. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** Riser design or fitness-for-service cannot be certified by one Scheil model. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **solidification front and solute conservation** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **feeding versus interface morphology** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **defect localization** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_5 -->

