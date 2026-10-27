# Unit 7: Strength, fracture, corrosion and reliability

**Guiding question:** How do metallurgists judge the trade-offs that turn attractive laboratory microstructures into risky products?

## Why this unit matters to metallurgical decisions

A shaft shows beach-mark-like patterns and corrosion products, while the initial inspection report attributes the failure to a single inclusion. This is a question about **damage initiation and progression** and about the difference between **nominal strength versus failure resistance**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

A material fails when a local combination of defects, stress, environmental chemistry and time exceeds a relevant damage resistance, which may be unrelated to its monotonic tensile strength. Uncertainty in the largest critical flaw and the true loading spectrum can dominate an apparently precise formula.

Fatigue and creep measurements often exhibit scatter and censoring. Report service-equivalent conditions, sample counts and control variables. A microstructural improvement established in a room-temperature static tensile test may not transfer to corrosion fatigue or elevated-temperature rupture.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **flaws, environment and loading spectrum**. For any local observation, describe why its sampling plan represents the part. Treat **rare initiation sites** as an explicit rival explanation and plan **fractography and replicated loading** as an independent check.

## Lesson 7.1: Combined strengthening mechanisms and superposition

### Scientific foundation

Solid solution, grain boundaries, work hardening and precipitation can all impede plastic flow, but simply adding every claimed strength increment can double-count mechanisms. Particle cutting, bypass and order strengthening occupy different regimes. A predicted strength must be matched with ductility, toughness and stability requirements.

**Governing relationship or decision rule:** Illustrative upper comparison: sigma≈sigma_0+sum Delta sigma_i; actual interaction may differ. Read every term in the equation as part of a declared specimen condition. In **combined strengthening mechanisms and superposition**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Using synthetic baseline strength 100 MPa and additions 80, 40 and 60 MPa, compare a naive 280 MPa sum with a root-sum-square interaction for the increments. State why neither is a calibration without real alloy data.

A companion calculator called **Crack-size limited nominal stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Crack size = 1.214286 mm**, the declared formula returns **578.23795 MPa**; at **Crack size = 2.178571 mm**, it returns **431.69909 MPa**. On this interval the modeled value decreases, and the two-point slope is **-151.96623 MPa per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `40/(1.12*Math.sqrt(Math.PI*a/1000))`. Model validity is limited to: **K=40 MPa sqrt(m), Y=1.12 fixed; elementary mode-I LEFM criterion only, no plane-strain or geometry validation**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Different strengthening barriers may not be statistically independent and residual stresses can shift an apparent yield threshold.

### Exercises and self-assessment

**Exercise 7.1A — Physical mechanism.** What experiments could distinguish precipitation strengthening from dislocation-density strengthening in an aged-and-worked sheet? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.1B — Numerical cross-check.** Recalculate **578.23795 MPa** from the companion formula at **1.214286 mm** and compare with **431.69909 MPa** at **2.178571 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 7.1C — Test design.** Propose a preparation or test matrix that addresses **rare initiation sites**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.2: Notches, fracture toughness and temperature

### Scientific foundation

Tensile strength is not fracture toughness. Critical stress intensity relates a crack's size, geometry and mode-I loading to a fracture resistance measured under specified constraints. Microstructural cleavage susceptibility and ductile tearing depend on temperature, thickness, grain boundaries and inclusions. A high-hardness product can fail abruptly in a notch-sensitive service environment.

**Governing relationship or decision rule:** Mode-I relation: K_I=Y sigma sqrt(pi a), with a defined for the chosen geometry. Read every term in the equation as part of a declared specimen condition. In **notches, fracture toughness and temperature**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For a fictional specimen with crack length 2 mm, Y=1.12 and K_Ic=40 MPa sqrt(m), compute nominal critical stress K/(Y sqrt(pi a)). Then discuss why plane-strain size validity and residual stress must be evaluated.

A companion calculator called **Relative creep stress sensitivity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Applied stress = 107.1429 MPa**, the declared formula returns **1.3178103 relative**; at **Applied stress = 135.7143 MPa**, it returns **3.3923626 relative**. On this interval the modeled value increases, and the two-point slope is **0.072609329 relative per MPa**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `Math.pow(s/100,4)`. Model validity is limited to: **Norton stress exponent n=4 at one temperature, normalized rate=1 at 100 MPa; no time-to-failure implied**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A test obtained on a thin section may not meet plane-strain conditions; cyclic stress-intensity limits and static K_Ic are not interchangeable.

### Exercises and self-assessment

**Exercise 7.2A — Physical mechanism.** Which fracture-surface features discriminate cleavage from ductile microvoid coalescence? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.2B — Numerical cross-check.** Recalculate **1.3178103 relative** from the companion formula at **107.1429 MPa** and compare with **3.3923626 relative** at **135.7143 MPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 7.2C — Test design.** Propose a preparation or test matrix that addresses **rare initiation sites**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.3: Fatigue, inclusions and surface condition

### Scientific foundation

Fatigue strength depends on stress amplitude, mean stress, load ratio, surface condition, residual stress and rare initiation sites. Large inclusions and machining scratches can matter more than average grain size in the long-life regime. S-N curves summarize a tested condition and cannot be transferred unchanged to different geometries or environments.

**Governing relationship or decision rule:** Stress amplitude sigma_a=(sigma_max-sigma_min)/2; stress ratio R=sigma_min/sigma_max. Read every term in the equation as part of a declared specimen condition. In **fatigue, inclusions and surface condition**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Design a fictional fatigue matrix with polished and rough specimens at two stress ratios; describe how a shift in initiation sites would be checked by fractography. Compute the alternate stress range for a chosen maximum and minimum load.

A companion calculator called **Crack-size limited nominal stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Crack size = 3.142857 mm**, the declared formula returns **359.42205 MPa**; at **Crack size = 4.107143 mm**, it returns **314.41056 MPa**. On this interval the modeled value decreases, and the two-point slope is **-46.678575 MPa per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Runouts are censored observations, not infinite fatigue lives. Statistical scatter must be represented rather than hidden behind one fitted line.

### Exercises and self-assessment

**Exercise 7.3A — Physical mechanism.** Why does an improvement in tensile yield stress not guarantee an improved high-cycle fatigue limit? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.3B — Numerical cross-check.** Recalculate **359.42205 MPa** from the companion formula at **3.142857 mm** and compare with **314.41056 MPa** at **4.107143 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 7.3C — Test design.** Propose a preparation or test matrix that addresses **rare initiation sites**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.4: Corrosion, sensitization and hydrogen effects

### Scientific foundation

Localized corrosion, galvanic coupling, intergranular attack, stress-corrosion cracking and hydrogen-assisted cracking are distinct mechanisms with different controlling environments. Welding or thermal exposure can change grain-boundary chemistry, precipitates and residual stresses. A clean shiny specimen after a short immersion is not evidence of long-term safety.

**Governing relationship or decision rule:** A simple galvanic potential ranking does not predict corrosion rate without kinetics, geometry and electrolyte transport. Read every term in the equation as part of a declared specimen condition. In **corrosion, sensitization and hydrogen effects**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare austenitic stainless coupons with distinct thermal histories in an explicitly controlled electrolyte; propose microscopy and electrochemical measurements to test chromium-depleted grain-boundary sensitization.

A companion calculator called **Relative creep stress sensitivity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Applied stress = 164.2857 MPa**, the declared formula returns **7.2844908 relative**; at **Applied stress = 192.8571 MPa**, it returns **13.833845 relative**. On this interval the modeled value increases, and the two-point slope is **0.22922741 relative per MPa**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Accelerated tests can change the mechanism; hydrogen embrittlement risk depends on material state, stress, potential and exposure history.

### Exercises and self-assessment

**Exercise 7.4A — Physical mechanism.** How would you distinguish grain-boundary corrosion from a mechanically driven intergranular fracture surface? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.4B — Numerical cross-check.** Recalculate **7.2844908 relative** from the companion formula at **164.2857 MPa** and compare with **13.833845 relative** at **192.8571 MPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 7.4C — Test design.** Propose a preparation or test matrix that addresses **rare initiation sites**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.5: Creep, diffusion and long-term damage

### Scientific foundation

At elevated temperatures deformation can involve dislocation glide and climb, diffusional flow, grain-boundary sliding and damage cavity formation. Apparent power-law stress exponents vary by regime; a laboratory steady-state trend cannot by itself predict component lifetime. Microstructural evolution during exposure may change the constitutive constants.

**Governing relationship or decision rule:** Within one calibrated regime, dot(epsilon)=A sigma^n exp[-Q/(RT)] is a possible empirical representation. Read every term in the equation as part of a declared specimen condition. In **creep, diffusion and long-term damage**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Calculate a toy creep-rate ratio for two stresses using exponent n=4, then estimate one-hour strain only under a hypothetical constant rate. Explain why tertiary creep, environmental oxidation and evolving precipitation invalidate that lifetime extrapolation.

A companion calculator called **Crack-size limited nominal stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Crack size = 5.071429 mm**, the declared formula returns **282.9449 MPa**; at **Crack size = 6.035714 mm**, it returns **259.35982 MPa**. On this interval the modeled value decreases, and the two-point slope is **-24.458605 MPa per mm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Temperature must be absolute in Arrhenius factors and comparisons must preserve stress units and phase state.

### Exercises and self-assessment

**Exercise 7.5A — Physical mechanism.** What observations show transition from secondary creep to cavitation-driven tertiary damage? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.5B — Numerical cross-check.** Recalculate **282.9449 MPa** from the companion formula at **5.071429 mm** and compare with **259.35982 MPa** at **6.035714 mm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 7.5C — Test design.** Propose a preparation or test matrix that addresses **rare initiation sites**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Integrated investigation: A fatigue-cracked shaft and corrosion question

### The evidence problem

A shaft shows beach-mark-like patterns and corrosion products, while the initial inspection report attributes the failure to a single inclusion. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Build rival hypotheses combining cyclic loads, pits, material cleanliness, residual stress and stress corrosion; map evidence along fracture propagation direction. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **damage initiation and progression** and **nominal strength versus failure resistance** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Preserve evidence, compare a companion shaft, examine chemistry and fractography, and reproduce exposure conditions using approved procedures. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** Initiation at a visible imperfection does not prove that imperfection is the sole root cause. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **damage initiation and progression** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **nominal strength versus failure resistance** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **rare initiation sites** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_13 -->

