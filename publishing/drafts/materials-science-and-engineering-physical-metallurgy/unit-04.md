# Unit 4: Deformation processing, recovery and grain control

**Guiding question:** How can rolling, forging and annealing tune grain structure while sometimes introducing anisotropy and damage?

## Why this unit matters to metallurgical decisions

A cold-rolled sheet has respectable average hardness but scattered large grains after annealing, with poor formability in one direction. This is a question about **strain history and stored energy** and about the difference between **recovery versus recrystallization**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Deformation adds stored energy while annealing can recover, recrystallize and grow grains in an overlapping schedule. The observable response therefore depends on prestrain, heating rate, hold duration and particle pinning. Do not interpret a particular hardness drop as a unique microstructural event without observing boundary and texture evolution.

Mechanical anisotropy depends on texture, inclusion alignment and specimen cut direction. Compare property distributions in multiple directions and through-thickness positions. A mean grain size can conceal abnormal grains; report the upper tail of grain-size distributions as well as the center.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **texture and dislocation structures**. For any local observation, describe why its sampling plan represents the part. Treat **spatial strain gradients** as an explicit rival explanation and plan **independent EBSD and mechanical tests** as an independent check.

## Lesson 4.1: Rolling reductions and true plastic strain

### Scientific foundation

Thickness reduction is commonly quoted as a percentage of original thickness, whereas true strain is logarithmic. Plane-strain rolling alters texture, dislocation density and grain elongation; multiple passes can distribute strain differently across thickness. Lubrication and friction may raise surface shear and increase heterogeneity.

**Governing relationship or decision rule:** True thickness strain magnitude: epsilon_true=ln(t0/tf) for homogeneous thickness compression. Read every term in the equation as part of a declared specimen condition. In **rolling reductions and true plastic strain**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For t0=10 mm and tf=6 mm, compute 40% engineering reduction and true compressive thickness strain ln(10/6)=0.511. Compare a one-pass schedule against two idealized passes with identical total thickness change.

A companion calculator called **Rolling true-thickness strain** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Final strip thickness = 3 mm**, the declared formula returns **1.2039728 dimensionless**; at **Final strip thickness = 4 mm**, it returns **0.91629073 dimensionless**. On this interval the modeled value decreases, and the two-point slope is **-0.28768207 dimensionless per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `Math.log(10/tf)`. Model validity is limited to: **Starting thickness 10 mm; uniform thickness compression; ignores spread, friction and redundant strain**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Thickness strain is not a universal equivalent plastic strain when width spread, elastic springback and nonuniform deformation occur.

### Exercises and self-assessment

**Exercise 4.1A — Physical mechanism.** Why can two sheets with the same final gauge have different through-thickness textures? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.1B — Numerical cross-check.** Recalculate **1.2039728 dimensionless** from the companion formula at **3 mm** and compare with **0.91629073 dimensionless** at **4 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 4.1C — Test design.** Propose a preparation or test matrix that addresses **spatial strain gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.2: Work hardening, storage energy and subgrains

### Scientific foundation

Cold working raises dislocation density, produces cells and orientation gradients and often reduces subsequent uniform elongation. Stored strain energy creates a driving force for recovery and recrystallization on heating; deformation temperature and dynamic recovery modify the result. Mechanical properties after working depend on strain path and prior grain size, not simply total reduction.

**Governing relationship or decision rule:** Taylor forest term Delta tau≈alpha G b sqrt(rho) is an illustrative contribution to flow stress. Read every term in the equation as part of a declared specimen condition. In **work hardening, storage energy and subgrains**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Use a synthetic Taylor relation to calculate forest shear stress for dislocation densities 1e13 and 9e13 m^-2. Discuss whether the observed difference could instead come from solute drag, second-phase particles or texture.

A companion calculator called **Simplified isothermal grain growth** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Annealing duration = 13.71429 h**, the declared formula returns **15.399443 µm**; at **Annealing duration = 20.57143 h**, it returns **17.484687 µm**. On this interval the modeled value increases, and the two-point slope is **0.30409805 µm per h**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `Math.sqrt(100+10*t)`. Model validity is limited to: **Initial grain diameter 10 µm, parabolic K=10 µm²/h; no pinning, abnormal growth or transient recrystallization**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

An increase in hardness is not a direct meter of total dislocation density; instrument load, grain size and precipitates affect it.

### Exercises and self-assessment

**Exercise 4.2A — Physical mechanism.** Which TEM or EBSD signatures distinguish dislocation cells from new strain-free grains? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.2B — Numerical cross-check.** Recalculate **15.399443 µm** from the companion formula at **13.71429 h** and compare with **17.484687 µm** at **20.57143 h**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 4.2C — Test design.** Propose a preparation or test matrix that addresses **spatial strain gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.3: Recovery and recrystallization

### Scientific foundation

Recovery rearranges and annihilates defects without necessarily producing a new population of high-angle grains; recrystallization produces grains with much lower stored deformation energy. Nucleation of recrystallized regions and boundary migration depend on stored-energy gradients, solute drag and particles. A single hardness drop does not prove that the whole sheet has recrystallized.

**Governing relationship or decision rule:** An Avrami-style fit X=1-exp[-(kt)^n] may describe a particular isothermal recrystallized fraction, not its unique mechanism. Read every term in the equation as part of a declared specimen condition. In **recovery and recrystallization**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare an invented hardness versus annealing-time curve against EBSD grain-orientation spread and high-angle boundary fraction. Define an onset, half-completion and completion threshold rather than calling one abrupt point the recrystallization temperature.

A companion calculator called **Rolling true-thickness strain** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Final strip thickness = 5 mm**, the declared formula returns **0.69314718 dimensionless**; at **Final strip thickness = 6 mm**, it returns **0.51082562 dimensionless**. On this interval the modeled value decreases, and the two-point slope is **-0.18232156 dimensionless per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

The so-called recrystallization temperature is process-dependent, not an immutable material constant; holding time and prior strain change it.

### Exercises and self-assessment

**Exercise 4.3A — Physical mechanism.** Why can moderate particle pinning delay boundary motion even when recovery is already advanced? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.3B — Numerical cross-check.** Recalculate **0.69314718 dimensionless** from the companion formula at **5 mm** and compare with **0.51082562 dimensionless** at **6 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 4.3C — Test design.** Propose a preparation or test matrix that addresses **spatial strain gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.4: Grain growth and Zener pinning

### Scientific foundation

After recrystallization, boundary-energy reduction can drive larger grains to consume smaller ones. Stable second-phase particles can restrain boundaries through Zener pinning, but pinning also depends on volume fraction, size distribution and particle coarsening. Abnormal grain growth produces a few very large grains that invalidate predictions from an average grain size alone.

**Governing relationship or decision rule:** One ideal curvature-driven kinetics form is d^2-d_0^2=Kt; K depends on temperature and boundary mobility. Read every term in the equation as part of a declared specimen condition. In **grain growth and zener pinning**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Using an illustrative d^2-d0^2=Kt law, calculate new grain size after 10 hours for d0=10 micrometers and K=10 micrometers^2 per hour. Compare this simple law against a bimodal distribution which shares the same average.

A companion calculator called **Simplified isothermal grain growth** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Annealing duration = 27.42857 h**, the declared formula returns **19.346465 µm**; at **Annealing duration = 34.28571 h**, it returns **21.044171 µm**. On this interval the modeled value increases, and the two-point slope is **0.24758214 µm per h**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

The parabolic exponent is an idealization; texture, solute drag and transient pinning may require other growth exponents.

### Exercises and self-assessment

**Exercise 4.4A — Physical mechanism.** How would you detect abnormal grain growth before it appears in a coarse area-average statistic? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.4B — Numerical cross-check.** Recalculate **19.346465 µm** from the companion formula at **27.42857 h** and compare with **21.044171 µm** at **34.28571 h**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 4.4C — Test design.** Propose a preparation or test matrix that addresses **spatial strain gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.5: Forging, texture and anisotropic performance

### Scientific foundation

Forging can close some voids, orient flow lines and refine structures, but it can also create laps, unrecrystallized bands and uneven strain. Crystallographic texture influences yield, r-values and directional fracture behavior. A process comparison is incomplete without specimen orientation and a realistic geometry, strain-temperature map and defect inspection.

**Governing relationship or decision rule:** A simple orientation ratio A=sigma_y,L/sigma_y,T describes one selected anisotropy metric, not a full yield surface. Read every term in the equation as part of a declared specimen condition. In **forging, texture and anisotropic performance**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Design tensile and bend tests in longitudinal, transverse and short-transverse orientations of a forged plate. Define a directional anisotropy index from two measured yield values rather than claiming 'isotropic' based on one axis.

A companion calculator called **Rolling true-thickness strain** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Final strip thickness = 7 mm**, the declared formula returns **0.35667494 dimensionless**; at **Final strip thickness = 8 mm**, it returns **0.22314355 dimensionless**. On this interval the modeled value decreases, and the two-point slope is **-0.13353139 dimensionless per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Flow-line appearance is not itself proof of enhanced toughness; inclusions and prior-austenite boundaries may introduce unfavorable fracture paths.

### Exercises and self-assessment

**Exercise 4.5A — Physical mechanism.** What sample locations are needed to test the claim that forging improved through-section uniformity? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.5B — Numerical cross-check.** Recalculate **0.35667494 dimensionless** from the companion formula at **7 mm** and compare with **0.22314355 dimensionless** at **8 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 4.5C — Test design.** Propose a preparation or test matrix that addresses **spatial strain gradients**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Integrated investigation: A cold-rolled sheet with abnormal annealed grains

### The evidence problem

A cold-rolled sheet has respectable average hardness but scattered large grains after annealing, with poor formability in one direction. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Link strain path, subgrain evolution, boundary pinning, abnormal growth and texture to a coupled experimental schedule and alternative models. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **strain history and stored energy** and **recovery versus recrystallization** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Compare independent sheets at multiple thickness locations using EBSD, grain-size tails, bend tests and cross-direction tension. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** An average grain size or one laboratory annealing run cannot establish manufacturing robustness. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **strain history and stored energy** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **recovery versus recrystallization** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **spatial strain gradients** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_7 -->

