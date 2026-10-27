# Unit 6: Nonferrous structural alloy families

**Guiding question:** Why are alloy-family labels useful yet insufficient for selecting aluminum, copper, magnesium, titanium or nickel systems?

## Why this unit matters to metallurgical decisions

A design team compares aluminum, magnesium, titanium and nickel alloys using one chart of specific strength and proposes the lightest candidate for all components. This is a question about **alloy-specific matrix and precipitates** and about the difference between **specific properties versus service stability**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Aluminum, copper, magnesium, titanium and nickel alloys occupy different processing and environment regimes. A high specific-strength number cannot rescue a material whose stiffness, creep stability, oxidation resistance or joint performance violates a hard requirement. State alloy grade and metallurgical temper explicitly.

The mechanism of strengthening may be recoverable or vulnerable to thermal exposure. Compare candidate alloys with the relevant temperature-time history and product form, not values compiled from unrelated sheet, plate, casting and forging test coupons. Check that a reference property corresponds to an actual qualified condition.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **alloy designation and processing condition**. For any local observation, describe why its sampling plan represents the part. Treat **environment and joining response** as an explicit rival explanation and plan **verified specification and exposure tests** as an independent check.

## Lesson 6.1: Aluminum: wrought series and precipitation routes

### Scientific foundation

Aluminum alloys are often grouped by major solutes and by whether they respond to precipitation hardening. A nominally strong temper can lose properties after welding or prolonged thermal exposure, and wrought product form affects grain shape and texture. Strength-to-weight comparison must use design constraints, not density alone.

**Governing relationship or decision rule:** Specific stiffness E/rho and specific strength sigma_y/rho are screening measures, not full design criteria. Read every term in the equation as part of a declared specimen condition. In **aluminum: wrought series and precipitation routes**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare hypothetical aluminum alloys at 2700 kg/m³ and a steel at 7850 kg/m³ for equal-stress axial rods and equal-deflection beams. Show why equal-stiffness designs require more than comparing yield strength divided by density.

A companion calculator called **Specific stiffness comparison** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Density = 3342.857 kg/m³**, the declared formula returns **20.940171 GPa per (g/cm³)**; at **Density = 4285.714 kg/m³**, it returns **16.333333 GPa per (g/cm³)**. On this interval the modeled value decreases, and the two-point slope is **-0.0048860399 GPa per (g/cm³) per kg/m³**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `70/(rho/1000)`. Model validity is limited to: **Young modulus fixed at 70 GPa, mass density varied synthetically; a screening index for selected geometries**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Series numbering and temper suffixes refer to recognized specifications with product-dependent limits; do not infer certified property tables from invented values.

### Exercises and self-assessment

**Exercise 6.1A — Physical mechanism.** Why can welding alter an age-hardened aluminum heat-affected zone without melting it? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.1B — Numerical cross-check.** Recalculate **20.940171 GPa per (g/cm³)** from the companion formula at **3342.857 kg/m³** and compare with **16.333333 GPa per (g/cm³)** at **4285.714 kg/m³**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 6.1C — Test design.** Propose a preparation or test matrix that addresses **environment and joining response**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Lesson 6.2: Copper alloys, conductivity and cold work

### Scientific foundation

Pure copper's conductivity makes it valuable electrically, while brasses, bronzes and precipitation-hardened copper alloys trade conductivity against strengthening and corrosion behavior. Cold work raises hardness but may reduce formability; grain growth during service heating can alter properties. Conductivity is sensitive to dissolved solutes, defects and temperature.

**Governing relationship or decision rule:** At a given geometry, resistance R=rho_e L/A; distinguish electrical resistivity rho_e from mass density. Read every term in the equation as part of a declared specimen condition. In **copper alloys, conductivity and cold work**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Prepare a fictional four-condition copper strip study: annealed pure, cold-worked pure, annealed brass and cold-worked brass. Predict relative resistance and bend behavior while clearly separating composition and deformation effects.

A companion calculator called **Copper conductor resistance** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Copper conductor length = 2.928571 m**, the declared formula returns **0.050371429 ohm**; at **Copper conductor length = 4.342857 m**, it returns **0.074697143 ohm**. On this interval the modeled value increases, and the two-point slope is **0.0172 ohm per m**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `1.72e-8*L/1e-6`. Model validity is limited to: **Electrical resistivity 1.72e-8 ohm m and fixed area 1 mm² at a single temperature; no contact resistance**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Matthiessen-type resistivity additivity is an approximation; microstructure and scattering mechanisms may invalidate a linear extrapolation.

### Exercises and self-assessment

**Exercise 6.2A — Physical mechanism.** Why would a conductivity recovery signal after annealing not uniquely prove recrystallization? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.2B — Numerical cross-check.** Recalculate **0.050371429 ohm** from the companion formula at **2.928571 m** and compare with **0.074697143 ohm** at **4.342857 m**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 6.2C — Test design.** Propose a preparation or test matrix that addresses **environment and joining response**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_11 -->

## Lesson 6.3: Magnesium and formability at temperature

### Scientific foundation

Magnesium's HCP structure at ordinary temperatures offers fewer easily active independent slip systems than many FCC alloys, creating formability challenges that can be alleviated by texture control, alloying and elevated-temperature mechanisms. Casting and wrought products have different grain structures. Corrosion and galvanic compatibility may control applications more strongly than low density.

**Governing relationship or decision rule:** Resolved shear stress depends on crystal orientation and available deformation systems; total strain cannot be assigned to dislocation slip alone. Read every term in the equation as part of a declared specimen condition. In **magnesium and formability at temperature**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare room-temperature and moderately elevated-temperature deformation in a fictional magnesium sheet, then design EBSD and tension-compression asymmetry measurements that could reveal twinning and texture effects.

A companion calculator called **Specific stiffness comparison** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Density = 5228.571 kg/m³**, the declared formula returns **13.387978 GPa per (g/cm³)**; at **Density = 6171.429 kg/m³**, it returns **11.342593 GPa per (g/cm³)**. On this interval the modeled value decreases, and the two-point slope is **-0.0021693483 GPa per (g/cm³) per kg/m³**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Elevated temperature can also accelerate creep or corrosion-related changes, so a forming improvement is not automatically a service improvement.

### Exercises and self-assessment

**Exercise 6.3A — Physical mechanism.** How might twin formation make compressive and tensile stress-strain curves different? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.3B — Numerical cross-check.** Recalculate **13.387978 GPa per (g/cm³)** from the companion formula at **5228.571 kg/m³** and compare with **11.342593 GPa per (g/cm³)** at **6171.429 kg/m³**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 6.3C — Test design.** Propose a preparation or test matrix that addresses **environment and joining response**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Lesson 6.4: Titanium microstructures, alpha-beta control and contamination

### Scientific foundation

Commercial titanium alloys can contain alpha, beta or mixed structures, with oxygen and other interstitials strongly affecting mechanical behavior. Thermomechanical processing shapes prior-beta grains, colony structure and texture; service fatigue and dwell sensitivity cannot be predicted from phase fraction alone. Oxygen contamination during processing may embrittle near-surface material.

**Governing relationship or decision rule:** The phase fraction, morphology, texture and oxygen profile jointly contribute to performance; one ratio is insufficient. Read every term in the equation as part of a declared specimen condition. In **titanium microstructures, alpha-beta control and contamination**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For a hypothetical alpha-beta titanium forging, compare a coarse colony structure and refined equiaxed alpha at equal total phase fraction. Propose microscopy, chemistry and orientation-specific fatigue tests before choosing a route.

A companion calculator called **Copper conductor resistance** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Copper conductor length = 5.757143 m**, the declared formula returns **0.099022857 ohm**; at **Copper conductor length = 7.171429 m**, it returns **0.12334857 ohm**. On this interval the modeled value increases, and the two-point slope is **0.0172 ohm per m**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

The role of beta stabilizers and cooling rate is composition-specific; using universal alpha/beta transition temperatures is incorrect.

### Exercises and self-assessment

**Exercise 6.4A — Physical mechanism.** Why might a refined microstructure improve strength while changing crack-growth resistance in an unexpected direction? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.4B — Numerical cross-check.** Recalculate **0.099022857 ohm** from the companion formula at **5.757143 m** and compare with **0.12334857 ohm** at **7.171429 m**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 6.4C — Test design.** Propose a preparation or test matrix that addresses **environment and joining response**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_11 -->

## Lesson 6.5: Nickel superalloys and high-temperature stability

### Scientific foundation

Nickel-based superalloys exploit a gamma matrix and often ordered gamma-prime precipitates, with refractory solutes and grain-boundary chemistry affecting creep and oxidation. Coarsening, rafting and topologically close-packed phases can alter behavior during extended exposure. Directionally solidified and single-crystal blades eliminate or orient certain boundaries but introduce their own anisotropies and processing concerns.

**Governing relationship or decision rule:** A screening creep law may resemble dot(epsilon)=A sigma^n exp[-Q/(RT)], but A, n and Q are regime-specific. Read every term in the equation as part of a declared specimen condition. In **nickel superalloys and high-temperature stability**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Draw a simplified gamma/gamma-prime microstructure and compare stress-assisted directional coarsening to ordinary isotropic growth. List microscopy, diffraction and long-duration creep measurements needed to validate a high-temperature claim.

A companion calculator called **Specific stiffness comparison** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Density = 7114.286 kg/m³**, the declared formula returns **9.8393574 GPa per (g/cm³)**; at **Density = 8057.143 kg/m³**, it returns **8.6879433 GPa per (g/cm³)**. On this interval the modeled value decreases, and the two-point slope is **-0.0012211968 GPa per (g/cm³) per kg/m³**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

No toy model captures simultaneous oxidation, creep, fatigue and thermal-barrier coating interactions. Design allowables require qualified material and geometry.

### Exercises and self-assessment

**Exercise 6.5A — Physical mechanism.** What is lost when creep strength is reported without test temperature, stress, time-to-rupture and orientation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 6.5B — Numerical cross-check.** Recalculate **9.8393574 GPa per (g/cm³)** from the companion formula at **7114.286 kg/m³** and compare with **8.6879433 GPa per (g/cm³)** at **8057.143 kg/m³**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 6.5C — Test design.** Propose a preparation or test matrix that addresses **environment and joining response**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_10 -->

## Integrated investigation: An aerospace candidate alloy shortlist

### The evidence problem

A design team compares aluminum, magnesium, titanium and nickel alloys using one chart of specific strength and proposes the lightest candidate for all components. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Build separate service matrices for ambient tensile members, corrosion-exposed sheets and hot rotating components, separating stiffness, strength, oxidation and joining constraints. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **alloy-specific matrix and precipitates** and **specific properties versus service stability** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Cross-check manufacturer-qualified data for the exact product condition and prototype the governing failure mode under relevant environmental exposures. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** Density-only or alloy-family-only rankings can select unsafe materials. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **alloy-specific matrix and precipitates** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **specific properties versus service stability** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **environment and joining response** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_11 -->

