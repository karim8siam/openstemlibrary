# Unit 1: Metallic structures, defects and quantitative micrographs

**Guiding question:** How does the arrangement of atoms and defects become a measurable engineering property?

## Why this unit matters to metallurgical decisions

An educational copper forging has two sections that show opposite hardness trends despite apparently comparable grain diameters. One section has stronger texture and a denser dislocation network, and the plan is to determine what explains the difference. This is a question about **defect state and orientation** and about the difference between **crystal slip versus boundary response**. A defensible answer identifies the alloy state and processing condition before comparing measured properties. It also names the potentially controlling failure mode, because a treatment that improves an uncomplicated strength result can make corrosion, distortion or fatigue worse. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Slip traces must be connected to grain orientation, and a micrograph of a deformed polycrystal should not be interpreted as the response of one perfectly aligned single crystal. Lattice friction, solute fields and dislocation junctions all modify the threshold for movement. Keep the resolved shear stress separate from the engineering stress displayed by the load cell.

A sampling plan should include texture, boundary misorientation and dislocation-sensitive contrast. When the apparent change is small, compare the expected signal with the spatial and angular resolution of the instrument. In a polycrystal, strong spatial contrast may be a real part of the phenomenon, rather than measurement noise.

The five lessons use distinct physical ideas but follow a common audit: establish a material state, derive an equation with dimensions, vary an input in a published range, articulate a rival explanation, and propose a separate instrument-based observation. The unit's two interactive models are deliberately narrower than any commercial metallurgy database. Use them to understand sensitivity, not to certify processing parameters.

## Measurement and conservation checkpoints

Write down the starting chemical composition and product form; define whether reported fractions are by area, mass, atoms or volume; and record the process history that could alter **orientation and test temperature**. For any local observation, describe why its sampling plan represents the part. Treat **microstructural sampling** as an explicit rival explanation and plan **orientation-independent diffraction** as an independent check.

## Lesson 1.1: Crystal structures and slip geometry

### Scientific foundation

Face-centered cubic, body-centered cubic and hexagonal close-packed structures offer different easy slip systems, stacking characteristics and temperature responses. Packing fraction alone does not predict ductility: available slip modes, critical resolved shear stress and grain constraint matter. Slip planes and directions must be expressed as crystallographic vectors, not inferred solely from a surface line.

**Governing relationship or decision rule:** For uniaxial loading, tau_RSS=sigma cos(phi)cos(lambda); the product of cosines is the Schmid factor. Read every term in the equation as part of a declared specimen condition. In **crystal structures and slip geometry**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Index two sets of diffraction peaks on imaginary FCC and BCC specimens, then predict where slip traces should lie on a polished grain. Compute the resolved shear stress from a 120 MPa tensile loading and an orientation factor 0.38; obtain 45.6 MPa before inferring slip activation.

A companion calculator called **Resolved shear stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Angle to slip plane normal = 41.42857 degrees**, the declared formula returns **51.60682 MPa**; at **Angle to slip plane normal = 47.85714 degrees**, it returns **46.183096 MPa**. On this interval the modeled value decreases, and the two-point slope is **-0.84369029 MPa per degrees**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `120*Math.cos(theta*Math.PI/180)*Math.cos(55*Math.PI/180)`. Model validity is limited to: **Uniaxial sigma=120 MPa; slip-direction angle fixed at 55 degrees; theta>=35 ensures geometrically compatible orthogonal plane normal and slip direction; Schmid factor <=0.5**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Texture and twinning may mimic a change in easy slip. Report orientation distributions and deformation temperature before generalizing a test from one single crystal to a polycrystal.

### Exercises and self-assessment

**Exercise 1.1A — Physical mechanism.** Why is an FCC alloy not automatically softer than a BCC alloy? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.1B — Numerical cross-check.** Recalculate **51.60682 MPa** from the companion formula at **41.42857 degrees** and compare with **46.183096 MPa** at **47.85714 degrees**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 1.1C — Test design.** Propose a preparation or test matrix that addresses **microstructural sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Lesson 1.2: Point defects, solutes and electrical resistance

### Scientific foundation

Vacancies support substitutional diffusion; interstitial atoms such as carbon can strongly distort iron lattices. Solute radius, valence and short-range order influence strengthening, conductivity and segregation, but size mismatch alone is not a universal predictor. Thermally activated equilibrium vacancy fractions are usually small and freeze-in during rapid cooling can be non-equilibrium.

**Governing relationship or decision rule:** An ideal dilute-equilibrium vacancy fraction satisfies c_v≈exp[-E_f/(k_B T)] when formation entropy is neglected. Read every term in the equation as part of a declared specimen condition. In **point defects, solutes and electrical resistance**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Take a teaching vacancy formation energy of 0.9 eV and estimate c_v=exp[-E_f/(k_B T)] at 900 K. Then compare the prediction to room temperature while noting that a quenched specimen retains excess vacancies and cannot be treated as instant equilibrium.

A companion calculator called **Hall–Petch illustrative yield stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Grain diameter = 37.14286 µm**, the declared formula returns **163.83714 MPa**; at **Grain diameter = 53.71429 µm**, it returns **151.39989 MPa**. On this interval the modeled value decreases, and the two-point slope is **-0.75052348 MPa per µm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

The browser expression is `90+0.45/Math.sqrt(d*1e-6)`. Model validity is limited to: **sigma0=90 MPa, ky=0.45 MPa sqrt(m), no extrapolation to nanograins or temperature effects**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Vacancy concentration is not directly equal to atomic diffusion rate, which also requires migration activation. Resistivity changes can include temperature, phonons and work hardening.

### Exercises and self-assessment

**Exercise 1.2A — Physical mechanism.** What experiment distinguishes vacancy annealing from solute precipitation when conductivity increases? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.2B — Numerical cross-check.** Recalculate **163.83714 MPa** from the companion formula at **37.14286 µm** and compare with **151.39989 MPa** at **53.71429 µm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 1.2C — Test design.** Propose a preparation or test matrix that addresses **microstructural sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_1 -->

## Lesson 1.3: Dislocations and forest strengthening

### Scientific foundation

A dislocation is a line defect with Burgers vector fixed by a circuit through the crystal. Mobile dislocations generate plastic strain, but their elastic fields obstruct one another; multiplication during deformation commonly increases flow stress. The Taylor relation is an estimate for one contribution, not an exact total yield strength.

**Governing relationship or decision rule:** The forest component can be approximated by Delta tau≈alpha G b sqrt(rho), with material- and microstructure-dependent alpha. Read every term in the equation as part of a declared specimen condition. In **dislocations and forest strengthening**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

For shear modulus 26 GPa, Burgers vector 0.286 nm, geometry factor 0.3 and forest density 1e14 m^-2, calculate alpha G b sqrt(rho)=22.3 MPa. Repeat at fourfold density and ask whether strength doubles or merely increases by a factor of two for this contribution.

A companion calculator called **Resolved shear stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Angle to slip plane normal = 54.28571 degrees**, the declared formula returns **40.178594 MPa**; at **Angle to slip plane normal = 60.71429 degrees**, it returns **33.668822 MPa**. On this interval the modeled value decreases, and the two-point slope is **-1.0126311 MPa per degrees**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Transmission-electron micrographs sample thin foils and dislocation character, annihilation and cell walls produce nonuniform obstacle networks. Do not extrapolate a density from one field without uncertainty.

### Exercises and self-assessment

**Exercise 1.3A — Physical mechanism.** Why does annealing reduce work hardening without necessarily changing composition? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.3B — Numerical cross-check.** Recalculate **40.178594 MPa** from the companion formula at **54.28571 degrees** and compare with **33.668822 MPa** at **60.71429 degrees**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 1.3C — Test design.** Propose a preparation or test matrix that addresses **microstructural sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Lesson 1.4: Grain boundaries, misorientation and grain size

### Scientific foundation

Grain boundaries are orientation discontinuities that impede slip and also provide diffusion paths and nucleation sites. High-angle and low-angle boundaries behave differently; counting all etched lines as equivalent grains is a stereological mistake. Hall–Petch strengthening is often useful over a verified size regime but can break down for nanocrystalline states or strongly textured microstructures.

**Governing relationship or decision rule:** Hall–Petch: sigma_y=sigma_0+k_y/sqrt(d) within its calibrated grain-size interval. Read every term in the equation as part of a declared specimen condition. In **grain boundaries, misorientation and grain size**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Using a synthetic sigma_0=90 MPa and k=0.45 MPa sqrt(m), calculate yield stress for grain sizes 16 micrometers and 64 micrometers. Compare predicted values with a measured distribution and explain how two-dimensional sections can bias grain size estimates.

A companion calculator called **Hall–Petch illustrative yield stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Grain diameter = 70.28571 µm**, the declared formula returns **143.67586 MPa**; at **Grain diameter = 86.85714 µm**, it returns **138.28472 MPa**. On this interval the modeled value decreases, and the two-point slope is **-0.32532702 MPa per µm**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

A grain-size correlation cannot prove grain boundaries caused a property change if porosity, texture and solute content co-varied.

### Exercises and self-assessment

**Exercise 1.4A — Physical mechanism.** What protocol tests whether a grain refinement benefit survives a change in specimen orientation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.4B — Numerical cross-check.** Recalculate **143.67586 MPa** from the companion formula at **70.28571 µm** and compare with **138.28472 MPa** at **86.85714 µm**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 1.4C — Test design.** Propose a preparation or test matrix that addresses **microstructural sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_1 -->

## Lesson 1.5: Metallography, phases and stereology

### Scientific foundation

Optical metallography, scanning electron microscopy, EBSD, diffraction and chemical mapping answer different questions. The area fraction on a random representative plane can estimate volume fraction under stereological assumptions, whereas etched contrast is not an independent chemical phase label. Sampling position and scale frequently dominate apparent microstructural differences.

**Governing relationship or decision rule:** For independent Bernoulli pixels, standard error of an area fraction is approximately sqrt[p(1-p)/N]; correlated images require effective sample size. Read every term in the equation as part of a declared specimen condition. In **metallography, phases and stereology**, a valid calculation requires the state of the metal, unit system and physical or geometrical meaning of each quantity. A composition nominally equal across specimens does not ensure identical segregation, dislocation density or precipitate population. An identical measured hardness does not ensure equal fatigue resistance. The point is to know which microstructural cause a chosen measurement can actually support.

### Worked metallurgical investigation

Count 125 bright pixels from 500 systematically sampled positions in a synthetic binary mask and estimate an area fraction 0.25. Compute binomial counting uncertainty as an educational lower bound and explain why spatial correlation makes it optimistic for real grains.

A companion calculator called **Resolved shear stress** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Angle to slip plane normal = 67.14286 degrees**, the declared formula returns **26.735646 MPa**; at **Angle to slip plane normal = 73.57143 degrees**, it returns **19.466253 MPa**. On this interval the modeled value decreases, and the two-point slope is **-1.1307944 MPa per degrees**. These are *worked calculations*, not fabricated experimental observations or properties of a real named alloy.

### Evidence, uncertainty, and a competing mechanism

Etching response varies with polishing, residual strain, grain orientation and contamination. Validate a suspected phase with at least one structure-sensitive technique.

### Exercises and self-assessment

**Exercise 1.5A — Physical mechanism.** How many independent cross-sections would you require before claiming a thick casting is homogeneous? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 1.5B — Numerical cross-check.** Recalculate **26.735646 MPa** from the companion formula at **67.14286 degrees** and compare with **19.466253 MPa** at **73.57143 degrees**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real alloy.

**Exercise 1.5C — Test design.** Propose a preparation or test matrix that addresses **microstructural sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_0 -->

## Integrated investigation: A mixed-grain forged copper study

### The evidence problem

An educational copper forging has two sections that show opposite hardness trends despite apparently comparable grain diameters. One section has stronger texture and a denser dislocation network, and the plan is to determine what explains the difference. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the metallurgical condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which treatment or alloy seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Map EBSD orientation, grain-boundary misorientation and local kernel-averaged misorientation before pairing with microhardness and a matched tensile specimen. Compare orientation-sensitive and dislocation-strength hypotheses. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **defect state and orientation** and **crystal slip versus boundary response** through the map. If an equilibrium calculation is used, include composition conservation and say nothing automatic about kinetics. If a strength relation is used, distinguish the contribution of one obstacle class from other strengthening or degradation modes. In case of thermal processing, use the actual specimen temperature trace rather than one nominal furnace set point. In case of damage, use local rather than average stress where geometry, flaws and residual stress are important.

Calculate outputs from both unit models at the midpoint and at an off-center slider position. Provide output units, fractional change, and a reason that the two mathematical relationships are related to different portions of the metallurgical question. Explain which constant would require independent experimental calibration and whether a plausible change in that constant could reverse the proposed design conclusion. A sensitivity result without a credible physical uncertainty model is a map of an equation, not evidence of service reliability.

### Validation plan, report, and counterfactual

Use reproducible image thresholding, calibrated orientation maps, independently reported grain-size distributions and replicate measurements in both sections. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing alloy families, write down the constraints that matter for weight, stiffness, temperature, oxidation and availability rather than reporting only one maximum strength metric.

**Known limits:** Texture and thickness-dependent constraint can defeat the assumption that a Hall–Petch fit is transferable. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **defect state and orientation** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **crystal slip versus boundary response** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **microstructural sampling** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_1 -->

