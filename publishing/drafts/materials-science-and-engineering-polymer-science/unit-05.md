# Unit 5: Mechanical behavior, fracture and long-term durability

**Guiding question:** How can designers connect tensile response, fatigue and environmental aging to service failure?

## Why this unit matters to polymer science

An injection-molded housing fractures after repeated cleaning while initial tensile tests met the specification. This is a question about **localized deformation and damage** and the distinction between **initial tensile strength versus environmental and long-time fracture**. A defensible answer identifies chain chemistry, molecular distribution, processing path and morphology before comparing measured properties. It also names the potentially controlling failure mode: a formulation that optimizes short-term stiffness, melt-flow index or optical clarity can still worsen creep resistance, process stability, environmental cracking or barrier lifetime. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Service fracture depends on a flaw population coupled to stress history, media and local morphology. Initial short-term tensile strength cannot isolate slow crack growth or environmental stress cracking.

Map the surface and internal origins of damage; compare dry and wet controls and account for how machining or molding introduced residual stresses.

## Measurement and conservation checkpoints

Write down the starting chain chemistry, distribution, additive package and processing history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **notch geometry, loading rate, exposure and processing direction**. For any local observation, describe why its sampling plan represents the part. Treat **molded-in residual stress or surface defects** as an explicit rival explanation and plan **fractography with matched environment controls** as an independent check.

## Lesson 5.1: Elastic modulus, yield and drawing

### Scientific foundation

A tensile stress–strain curve for a polymer depends on temperature, strain rate, specimen conditioning and orientation. The initial slope reflects stiffness in a prescribed small-strain window; yield can involve localized shear transformations or crazing, followed by neck propagation and molecular drawing. Some specimens fail before a clear yield event. Engineering and true stress differ as cross-sectional area changes, especially after necking, so a long necked specimen cannot be described by a single uniform strain.

**Governing relationship or decision rule:** Within a measured small-strain linear range, engineering stress σ≈E ε; nominal stress uses original cross-sectional area. Read every term in the equation as part of a declared specimen condition. In **elastic modulus, yield and drawing**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Use the linear-elastic slider with E=1.2 GPa and strains up to 3% to estimate nominal stresses before yielding. Then draw a plausible schematic curve for a ductile semicrystalline material, labeling initial slope, yield, necking and strain hardening. Specify which portions no longer follow Hooke's law, and compare results at different strain rates with matched specimen geometry.

A companion calculator called **Linear-elastic tensile stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Engineering tensile strain = 0.5142857 %**, the declared formula returns **6.1714286 MPa**; at **Engineering tensile strain = 0.9285714 %**, it returns **11.142857 MPa**. On this interval the modeled value increases, and the two-point slope is **12 MPa per %**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `1200*e/100`. Model validity is limited to: **Small-strain isotropic linear elastic approximation E=1200 MPa, no yield or environmental effects; limit before nonlinear response**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The elastic slider holds E fixed and cannot model damage, large-strain plasticity, neck geometry or moisture conditioning. Strain at break without test speed and gauge length is not a transferable specification.

### Exercises and self-assessment

**Exercise 5.1A — Physical mechanism.** Why may two tensile specimens show the same initial modulus but markedly different elongation at break? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.1B — Numerical cross-check.** Recalculate **6.1714286 MPa** from the companion formula at **0.5142857 %** and compare with **11.142857 MPa** at **0.9285714 %**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 5.1C — Test design.** Propose a synthesis, processing or test matrix that addresses **molded-in residual stress or surface defects**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.2: Crazing, shear yielding and toughening

### Scientific foundation

Local plasticity around a stress concentrator can proceed through shear yielding or craze formation, depending on polymer chemistry, stress state, temperature and deformation rate. Crazes contain fibrils and microvoids and can absorb energy before they become cracks. Rubber-particle toughening redistributes stress and may promote extensive matrix yielding, but particle size, adhesion and glassy matrix state influence the benefit. Increasing nominal elongation alone is not a robust measure of crack-initiation resistance.

**Governing relationship or decision rule:** A valid fracture-mechanism claim combines calibrated mechanical test conditions with local crack-tip deformation evidence. Read every term in the equation as part of a declared specimen condition. In **crazing, shear yielding and toughening**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare notched and unnotched specimen responses before and after adding a hypothetical rubber modifier. Measure the deformation zone with microscopy and obtain instrumented impact energy and slow-rate fracture results. Identify whether low-temperature impact toughness improves at the expense of stiffness or heat deflection. Specify particle-size distribution, processing-induced voids and interfacial chemistry.

A companion calculator called **Illustrative mode-I crack intensity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Initial crack length = 178.5714 µm**, the declared formula returns **0.6631915 MPa sqrt(m)**; at **Initial crack length = 262.8571 µm**, it returns **0.80462377 MPa sqrt(m)**. On this interval the modeled value increases, and the two-point slope is **0.00167801 MPa sqrt(m) per µm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `1.12*25*Math.sqrt(Math.PI*a*1e-6)`. Model validity is limited to: **Nominal tensile stress=25 MPa, Y=1.12, geometry-specific LEFM; no polymer viscoelasticity, plastic zone or crack-growth law**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Impact numbers depend heavily on notch shape, specimen dimensions, impact speed and thermal history; they are not intrinsic fracture toughness constants. Modifiers can reduce strength or raise processing complexity.

### Exercises and self-assessment

**Exercise 5.2A — Physical mechanism.** What microstructural evidence would support energy dissipation by rubber-induced shear yielding rather than simply a lower modulus? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.2B — Numerical cross-check.** Recalculate **0.6631915 MPa sqrt(m)** from the companion formula at **178.5714 µm** and compare with **0.80462377 MPa sqrt(m)** at **262.8571 µm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 5.2C — Test design.** Propose a synthesis, processing or test matrix that addresses **molded-in residual stress or surface defects**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.3: Crack-driving force and environmental stress cracking

### Scientific foundation

A pre-existing flaw raises local tensile stress. For a limited linear-elastic geometry, mode-I intensity scales as K=Yσsqrt(πa), where the physical flaw length definition and geometry factor must match the actual component. Polymers, however, often show nonlinear viscoelastic and plastic zones, so conventional LEFM can be invalid. Environmental stress cracking may occur under sustained strain in the presence of specific surface-active agents without gross chemical dissolution.

**Governing relationship or decision rule:** K_I=Y σ sqrt(πa) in geometry- and scale-appropriate linear elastic fracture mechanics, not an all-purpose polymer lifetime law. Read every term in the equation as part of a declared specimen condition. In **crack-driving force and environmental stress cracking**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

With nominal tensile stress 25 MPa and Y=1.12, use the flaw-length slider to compare K for cracks of 100 and 400 µm; doubling crack depth does not double K because dependence is a square root. Propose separate air and detergent exposure tests on specimens with identical notch preparation. Compare actual fracture surfaces rather than attributing every difference to surface energy.

A companion calculator called **Linear-elastic tensile stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Engineering tensile strain = 1.342857 %**, the declared formula returns **16.114286 MPa**; at **Engineering tensile strain = 1.757143 %**, it returns **21.085714 MPa**. On this interval the modeled value increases, and the two-point slope is **12 MPa per %**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

The synthetic K calculation is not a fracture criterion without a measured material resistance and valid test geometry. Plastic zones, time dependence and solvent uptake may invalidate LEFM assumptions.

### Exercises and self-assessment

**Exercise 5.3A — Physical mechanism.** Why can a molded product fail in detergent at an applied stress lower than its short-term dry tensile strength? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.3B — Numerical cross-check.** Recalculate **16.114286 MPa** from the companion formula at **1.342857 %** and compare with **21.085714 MPa** at **1.757143 %**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 5.3C — Test design.** Propose a synthesis, processing or test matrix that addresses **molded-in residual stress or surface defects**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Lesson 5.4: Fatigue and cyclic hysteresis

### Scientific foundation

Polymers dissipate energy during cycling, and the resulting hysteresis can raise local temperature when heat cannot escape. Fatigue can involve crack initiation near inclusions, crazing, interface delamination or pre-existing flaws. A single stress-life curve does not universally characterize a material: mean stress, waveform, frequency, humidity, thermal boundary conditions and specimen thickness matter. Time-dependent damage and thermal softening may interact during tests.

**Governing relationship or decision rule:** Cycle damage must be referenced to stress amplitude, mean stress, thermal state and observed damage mechanisms; there is no universal polymer fatigue threshold. Read every term in the equation as part of a declared specimen condition. In **fatigue and cyclic hysteresis**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Design a fatigue matrix with at least two frequencies and load ratios, recording surface temperature in addition to cycle count and crack length. Ask whether a shorter apparent life at high frequency is due to faster intrinsic damage or heat buildup. Compare thermal images, stiffness change and fracture origins from representative failed specimens.

A companion calculator called **Illustrative mode-I crack intensity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Initial crack length = 347.1429 µm**, the declared formula returns **0.92467067 MPa sqrt(m)**; at **Initial crack length = 431.4286 µm**, it returns **1.0308309 MPa sqrt(m)**. On this interval the modeled value increases, and the two-point slope is **0.0012595278 MPa sqrt(m) per µm**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Frequency changes the heating rate and relaxation times together; accelerated cycles may change the failure mechanism. Extrapolating a high-cycle branch without confidence intervals is unsafe.

### Exercises and self-assessment

**Exercise 5.4A — Physical mechanism.** How would you distinguish self-heating from chemical aging as the cause of reduced fatigue life? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.4B — Numerical cross-check.** Recalculate **0.92467067 MPa sqrt(m)** from the companion formula at **347.1429 µm** and compare with **1.0308309 MPa sqrt(m)** at **431.4286 µm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 5.4C — Test design.** Propose a synthesis, processing or test matrix that addresses **molded-in residual stress or surface defects**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_9 -->

## Lesson 5.5: Oxidation, UV exposure and physical aging

### Scientific foundation

Polymer service deterioration may involve chain scission, crosslinking, additive loss, photo-oxidation, hydrolysis or purely physical densification. UV exposure generally affects surfaces more strongly than thick interiors, especially when absorbers or pigments screen light. Oxidative induction time is an assay under defined conditions, not a field-life clock. Glassy polymers can slowly densify after quenching without chemical reactions, altering creep and embrittlement.

**Governing relationship or decision rule:** Chemical degradation changes molecular constitution; physical aging changes nonequilibrium structure without requiring bond cleavage. Read every term in the equation as part of a declared specimen condition. In **oxidation, uv exposure and physical aging**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare outdoor-exposed coupons with controls held at matched temperatures in the dark. Measure FTIR carbonyl-region changes, SEC molar-mass shifts, color and mechanical response at surface and core. Add a humidity-controlled series when hydrolysis is plausible. State whether reported strength loss is more consistent with oxidation depth gradients or altered crystallinity.

A companion calculator called **Linear-elastic tensile stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Engineering tensile strain = 2.171429 %**, the declared formula returns **26.057143 MPa**; at **Engineering tensile strain = 2.585714 %**, it returns **31.028571 MPa**. On this interval the modeled value increases, and the two-point slope is **12 MPa per %**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Accelerated lamp tests alter dose spectrum, humidity and temperature relative to outdoors. Chemical index changes require baseline normalization, and no generic conversion factor maps laboratory hours to service years.

### Exercises and self-assessment

**Exercise 5.5A — Physical mechanism.** Why does increased modulus after long storage sometimes accompany worse impact resistance even with little new oxidation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 5.5B — Numerical cross-check.** Recalculate **26.057143 MPa** from the companion formula at **2.171429 %** and compare with **31.028571 MPa** at **2.585714 %**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 5.5C — Test design.** Propose a synthesis, processing or test matrix that addresses **molded-in residual stress or surface defects**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_8 -->

## Integrated investigation: Unexpected cracks in service

### The evidence problem

An injection-molded housing fractures after repeated cleaning while initial tensile tests met the specification. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which polymerization route or formulated resin seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Track weld lines, mold orientation, notch state, residual stress, detergent effects and long-term loading. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **localized deformation and damage** and **initial tensile strength versus environmental and long-time fracture** through the map. For polymer mixing, show composition conservation and do not infer processing kinetics from a static phase diagram. For a melt-state relation, distinguish relaxation time from shear-rate-dependent flow and actual process heating. For chemical function, distinguish molecular diffusion, partitioning, chain mobility and chemical degradation. Use the actual specimen time–temperature history instead of only a machine-temperature set point. For damage, compare local flaw driving force with rate- and environment-dependent measured fracture resistance.

### Validation plan, report, and counterfactual

Compare matched chemical exposure and dry controls, fracture origins, processing directions and stress intensity only where LEFM holds. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing polymer families, write down the constraints that matter for stiffness, creep, permeability, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** High dry tensile strength alone does not prove environmental stress crack resistance. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **localized deformation and damage** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **initial tensile strength versus environmental and long-time fracture** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **molded-in residual stress or surface defects** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_9 -->

