# Unit 2: Alloy chemistry and thermodynamic maps

**Guiding question:** What can composition and phase diagrams predict, and what do they leave unknown?

## Why this unit matters to metallurgical decisions

A fictional binary alloy calculator predicts a single-phase field at its nominal concentration, yet a held-out specimen reveals a weak second diffraction signal after cooling. This is a question about **equilibrium composition and activities** and about the difference between **phase fractions versus local chemistry**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

The equilibrium chart is a guide to what phases may minimize Gibbs energy at the stated conditions, not a history of how the specimen arrived there. In multicomponent alloys, apparently binary endpoints shift as third and fourth solutes change chemical activity. Plot the state point and write the assumed fixed variables before drawing a tie line.

Mass-balance calculations require careful distinction among weight, atomic and volume fractions. If a phase calculator predicts a nonzero fraction below a detection threshold, report both the prediction and detection limit. A missing peak may reflect texture or insufficient sensitivity rather than the absence of a thermodynamically favored state.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **phase diagram and database conditions**. For any local observation, describe why its sampling plan represents the part. Treat **nonequilibrium segregation** as an explicit rival explanation and plan **multiple chemistry-sensitive sites** as an independent check.

## Lesson 2.1: Substitutional solutions and Hume–Rothery heuristics

### Scientific foundation

The classic size, crystal structure, electronegativity and valence heuristics give tendencies toward substitutional solubility, not proofs of complete miscibility. Ordering, magnetism and temperature can alter chemical activities. Mixing enthalpy and entropy provide a clearer explanation of why alloys separate or remain soluble in a particular region.

**Governing relationship or decision rule:** Ideal binary mixing: Delta S_mix=-R[x ln x+(1-x)ln(1-x)]. Read every term in the equation as part of a declared specimen condition. In **substitutional solutions and hume–rothery heuristics**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Calculate an ideal configurational mixing entropy at equiatomic binary composition, Delta S_mix=-R[x ln x+(1-x)ln(1-x)], and the corresponding -TDelta S contribution at 900 K. Then discuss what non-ideal interaction energy might overcome that gain.

A companion calculator called **Ideal binary configurational entropy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mole fraction of B = 0.1785714 fraction**, the declared formula returns **3.901315 J/(mol K)**; at **Mole fraction of B = 0.3071429 fraction**, it returns **5.1283231 J/(mol K)**. On this interval the modeled value increases, and the two-point slope is **9.5433959 J/(mol K) per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `-8.314462618*(x*Math.log(x)+(1-x)*Math.log(1-x))`. Model validity is limited to: **Ideal random substitutional mixing, entropy only; no ordering or excess interaction enthalpy**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Do not describe an alloy as single phase on nominal chemistry alone; examine an equilibrium assessment and a sample processed along a known thermal route.

### Exercises and self-assessment

**Exercise 2.1A — Physical mechanism.** When can rapid quenching create a compositionally uniform but metastable solid solution? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.1B — Numerical cross-check.** Recalculate **3.901315 J/(mol K)** from the companion formula at **0.1785714 fraction** and compare with **5.1283231 J/(mol K)** at **0.3071429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 2.1C — Test design.** Propose a preparation or test matrix that addresses **nonequilibrium segregation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.2: Lever rules and binary equilibria

### Scientific foundation

A tie line defines compositions of coexisting phases at specified temperature and pressure. The lever rule closes a component balance on a consistent weight or mole basis; it does not predict size, shape or spatial distribution of the phases. Density differences must be included when converting mass fractions to volume fractions.

**Governing relationship or decision rule:** For two phases, f_beta=(c_0-c_alpha)/(c_beta-c_alpha) on one consistent composition and phase-fraction basis. Read every term in the equation as part of a declared specimen condition. In **lever rules and binary equilibria**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Use synthetic c_alpha=0.1, c_beta=0.7 and bulk c0=0.34 on an identical fraction basis. Compute f_beta=(0.34-0.10)/(0.70-0.10)=0.4 and verify total solute balance to machine precision.

A companion calculator called **Equilibrium beta-phase mass fraction** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Overall solute fraction = 0.2714286 fraction**, the declared formula returns **0.28571429 fraction**; at **Overall solute fraction = 0.3571429 fraction**, it returns **0.42857143 fraction**. On this interval the modeled value increases, and the two-point slope is **1.6666667 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `(c-0.1)/0.6`. Model validity is limited to: **Two hypothetical phases with endpoints c_alpha=0.1 and c_beta=0.7 at one temperature, equal composition basis**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

The formula fails outside the tie-line interval, and nonequilibrium segregation can invalidate the assumed endpoint compositions.

### Exercises and self-assessment

**Exercise 2.2A — Physical mechanism.** How would a volume fraction differ if the two phases have unequal mass densities? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.2B — Numerical cross-check.** Recalculate **0.28571429 fraction** from the companion formula at **0.2714286 fraction** and compare with **0.42857143 fraction** at **0.3571429 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 2.2C — Test design.** Propose a preparation or test matrix that addresses **nonequilibrium segregation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.3: Iron-carbon chart and equilibrium caveats

### Scientific foundation

The iron–carbon diagram is indispensable for steel and cast-iron microstructure, but the commonly taught iron–cementite diagram is metastable relative to graphite in suitable conditions. Austenite, ferrite and cementite are phases; pearlite is a two-phase microconstituent, not a single phase. Magnetic ordering complicates ferrite free energy and modern assessments can refine conventional boundaries.

**Governing relationship or decision rule:** Within a specified two-phase tie line, phase fractions are obtained by mass balance; property and kinetic predictions require additional relations. Read every term in the equation as part of a declared specimen condition. In **iron-carbon chart and equilibrium caveats**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Compare hypoeutectoid and hypereutectoid steels near the eutectoid reaction. Draw the proeutectoid product and the later pearlite fraction separately; label whether any carbon value is wt% rather than atom fraction.

A companion calculator called **Ideal binary configurational entropy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mole fraction of B = 0.4357143 fraction**, the declared formula returns **5.6942341 J/(mol K)**; at **Mole fraction of B = 0.5642857 fraction**, it returns **5.6942341 J/(mol K)**. On this interval the modeled value changes nonmonotonically or remains nearly unchanged, and the two-point slope is **0 J/(mol K) per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Do not blindly assign a textbook diagram to every alloyed steel, and distinguish long-time equilibrium from products formed along a CCT path.

### Exercises and self-assessment

**Exercise 2.3A — Physical mechanism.** Why would equal total carbon content not guarantee equal hardness after two different cooling schedules? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.3B — Numerical cross-check.** Recalculate **5.6942341 J/(mol K)** from the companion formula at **0.4357143 fraction** and compare with **5.6942341 J/(mol K)** at **0.5642857 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 2.3C — Test design.** Propose a preparation or test matrix that addresses **nonequilibrium segregation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Lesson 2.4: Multicomponent phase calculations and CALPHAD

### Scientific foundation

Industrial alloys are multicomponent, so binary plots rarely determine precipitation fractions or solidification sequences uniquely. CALPHAD assessments fit Gibbs-energy models to evaluated measurements and calculate equilibrium or metastable constrained states. Thermodynamic databases differ in their assessed phases and composition validity windows, and uncertainty may be larger than a plotted line suggests.

**Governing relationship or decision rule:** Equilibrium minimizes total Gibbs energy G_total=sum_phi n_phi G_phi over admissible phase amounts subject to element conservation. Read every term in the equation as part of a declared specimen condition. In **multicomponent phase calculations and calphad**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For a conceptual Fe–Cr–Ni alloy, fix two bulk compositions and temperature, then compare equilibrium phases with a frozen substitutional-diffusion constraint. Record database name, version, phase suppression and all units before describing the changes.

A companion calculator called **Equilibrium beta-phase mass fraction** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Overall solute fraction = 0.4428571 fraction**, the declared formula returns **0.57142857 fraction**; at **Overall solute fraction = 0.5285714 fraction**, it returns **0.71428571 fraction**. On this interval the modeled value increases, and the two-point slope is **1.6666667 fraction per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

A software result is not an experimental observation. Small composition differences and undeclared inactive phases can strongly change an output.

### Exercises and self-assessment

**Exercise 2.4A — Physical mechanism.** How could you independently cross-check a surprising predicted sigma-phase fraction? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.4B — Numerical cross-check.** Recalculate **0.57142857 fraction** from the companion formula at **0.4428571 fraction** and compare with **0.71428571 fraction** at **0.5285714 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 2.4C — Test design.** Propose a preparation or test matrix that addresses **nonequilibrium segregation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_3 -->

## Lesson 2.5: Chemical driving force versus industrial process windows

### Scientific foundation

Thermodynamic stability bounds what can form in equilibrium, whereas finite diffusion length and spatial temperature gradients determine what commonly forms. The same nominal solution-treatment temperature can create heterogeneous constituent dissolution across a thick billet. A validated process window therefore needs temperature exposure, geometry, environmental condition and a relevant microstructural target.

**Governing relationship or decision rule:** A characteristic diffusion distance can scale as ell≈sqrt(Dt), not a universal exact front location. Read every term in the equation as part of a declared specimen condition. In **chemical driving force versus industrial process windows**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Approximate diffusion distance as sqrt(Dt) at fixed D=5e-15 m²/s and t=3600 s, then compare it to half a 20-micrometer particle. Explain how a two-order-of-magnitude diffusivity error changes the conclusion.

A companion calculator called **Ideal binary configurational entropy** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Mole fraction of B = 0.6928571 fraction**, the declared formula returns **5.1283231 J/(mol K)**; at **Mole fraction of B = 0.8214286 fraction**, it returns **3.901315 J/(mol K)**. On this interval the modeled value decreases, and the two-point slope is **-9.5433959 J/(mol K) per fraction**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

A uniform diffusion coefficient ignores grain boundaries, nonideal activities and dissolution-interface reaction rates; it must not be used to issue heat-treatment instructions for unknown alloys.

### Exercises and self-assessment

**Exercise 2.5A — Physical mechanism.** What is the smallest independent observation that could show dissolution remains incomplete? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 2.5B — Numerical cross-check.** Recalculate **5.1283231 J/(mol K)** from the companion formula at **0.6928571 fraction** and compare with **3.901315 J/(mol K)** at **0.8214286 fraction**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 2.5C — Test design.** Propose a preparation or test matrix that addresses **nonequilibrium segregation**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_2 -->

## Integrated investigation: An ambiguous binary alloy phase prediction

### The evidence problem

A fictional binary alloy calculator predicts a single-phase field at its nominal concentration, yet a held-out specimen reveals a weak second diffraction signal after cooling. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Recalculate a tie-line and test whether local segregation, metastability, contamination or texture could explain the signal; build a mass-balance table before interpreting intensities. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **equilibrium composition and activities** and **phase fractions versus local chemistry** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

### Validation plan, report, and counterfactual

Acquire matrix-corrected chemistry maps, multiple diffraction geometries and documented thermal paths across a series of compositions. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** Equilibrium computation is neither a phase-identification instrument nor a kinetic model. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **equilibrium composition and activities** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **phase fractions versus local chemistry** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **nonequilibrium segregation** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_3 -->

