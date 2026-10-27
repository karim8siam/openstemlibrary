# Unit 3: Anisotropic elasticity and single-ply mechanics

**Guiding question:** How do directions and stress transformation alter a unidirectional ply response?

## Why this unit matters to composite materials

Two laboratories obtain different 45-degree modulus values on apparently identical tape. This is a question about **orthotropic constitutive response** and the distinction between **material-axis parameters versus global stress**. A defensible answer identifies fiber architecture, reinforcement and matrix properties, fabrication route, part geometry and loading direction before comparing measured performance. It also names the relevant failure mechanism: a design that maximizes axial stiffness can simultaneously increase sensitivity to delamination, compression after impact, moisture, manufacturing wrinkles or difficult field repairs. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Engineering constants describe properties along designated material axes; the response in global coordinates requires tensor transformations and precise shear definitions.

Small-strain plane stress is useful for a thin ply away from constrained boundaries, whereas local peel and interlaminar stresses remain three-dimensional.

## Measurement and conservation checkpoints

Write down constituent identities, reinforcement form, interphase treatment, stacking sequence, process history and part geometry; define whether fractions are measured by area, mass or volume; and record the process history that could alter **strain definition, ply angle and specimen conditioning**. For any local observation, describe why its sampling plan represents the part. Treat **tab-induced stress concentration or material nonlinearity** as an explicit rival explanation and plan **digital image correlation plus calibrated strain gauges** as an independent check.

## Lesson 3.1: Orthotropic elastic constants

### Scientific foundation

An orthotropic lamina has distinct axial and transverse Young's moduli, in-plane shear modulus and Poisson couplings. In plane stress the compliance matrix contains 1/E1, 1/E2, −nu12/E1 and 1/G12; reciprocity requires nu12/E1=nu21/E2 for linear elastic thermodynamic consistency. Calling a unidirectional ply isotropic can severely underpredict off-axis shear strains. Properties refer to material axes and specific conditioning. Engineering shear gamma12 is not the tensorial strain epsilon12.

**Governing relationship or decision rule:** nu21=nu12 E2/E1 for reciprocal orthotropic plane-stress elasticity. Read every term in the equation as part of a declared specimen condition. In **orthotropic elastic constants**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Take E1=135 GPa, E2=9 GPa, G12=5 GPa and nu12=0.28. Compute nu21=nu12 E2/E1≈0.0187 and check positivity of the compliance matrix. Discuss why assigning nu21=0.28 violates reciprocal symmetry. State which coupon tests identify each parameter and whether direct shear measurement is robust.

A companion calculator called **Reciprocal Poisson ratio** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Transverse modulus = 6.142857 GPa**, the declared formula returns **0.012740741 dimensionless**; at **Transverse modulus = 9.285714 GPa**, it returns **0.019259259 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.0020740741 dimensionless per GPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `0.28*E2/135`. Model validity is limited to: **E1=135 GPa, nu12=0.28, reciprocal plane-stress orthotropic linear elasticity**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

These constants assume a linear elastic, homogeneous ply at a declared scale. Damage and temperature can make them nonlinear.

### Exercises and self-assessment

**Exercise 3.1A — Physical mechanism.** What additional observation is needed before applying room-temperature elastic constants after water conditioning? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.1B — Numerical cross-check.** Recalculate **0.012740741 dimensionless** from the companion formula at **6.142857 GPa** and compare with **0.019259259 dimensionless** at **9.285714 GPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 3.1C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **tab-induced stress concentration or material nonlinearity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.2: Plane-stress reduced stiffness

### Scientific foundation

Under plane stress, a lamina's normal stress vector relates to strain through the reduced stiffness Q matrix; Q11=E1/(1−nu12 nu21), Q22=E2/(1−nu12 nu21) and Q12=nu12 E2/(1−nu12 nu21). The shear term Q66=G12 uses engineering shear. The matrix must be symmetric and physically positive definite. A large Q11 does not imply a high interlaminar tensile resistance. Working in consistent GPa, MPa or Pa is essential when integrating laminate stiffness.

**Governing relationship or decision rule:** Q11=E1/(1−nu12 nu21), with nu21=nu12 E2/E1. Read every term in the equation as part of a declared specimen condition. In **plane-stress reduced stiffness**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

For an ideal lamina E1=135 GPa, E2=9 GPa, nu12=0.28 and G12=5 GPa, evaluate the common denominator and Q11. Compare direct division by E1 as an approximation and comment on the numerical difference. Describe a unit test verifying the assembled Q matrix symmetry.

A companion calculator called **Local shear from global axial tension** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Ply angle = 25.71429 degrees**, the declared formula returns **39.091574 MPa**; at **Ply angle = 38.57143 degrees**, it returns **48.746396 MPa**. On this interval the modeled value increases, and the two-point slope is **0.75093056 MPa per degrees**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

The browser expression is `100*Math.abs(Math.sin(theta*Math.PI/180)*Math.cos(theta*Math.PI/180))`. Model validity is limited to: **Global uniaxial tensile stress 100 MPa, ideal stress tensor rotation; shear sign omitted; does not assess failure**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Q is a two-dimensional linear model; three-dimensional free-edge stresses require additional theory.

### Exercises and self-assessment

**Exercise 3.2A — Physical mechanism.** Why should Q12 and Q21 be identical despite different E1 and E2? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.2B — Numerical cross-check.** Recalculate **39.091574 MPa** from the companion formula at **25.71429 degrees** and compare with **48.746396 MPa** at **38.57143 degrees**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 3.2C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **tab-induced stress concentration or material nonlinearity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.3: Off-axis transformation

### Scientific foundation

Rotating a ply changes the components of stress and strain relative to its fiber axes. A global normal stress can create local shear at 45 degrees even if the global shear is zero. Off-axis tensile coupons can therefore be sensitive to matrix shear behavior and end constraints. Transformation of stiffness is not the same as simply replacing E1 by E1 cos²theta + E2 sin²theta. The compliance rotation contains fourth powers and coupling terms, and signs depend on convention.

**Governing relationship or decision rule:** Under uniaxial global stress, |tau12|=|sigma_x sin(theta) cos(theta)|. Read every term in the equation as part of a declared specimen condition. In **off-axis transformation**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

For a uniform global uniaxial stress sigma_x=100 MPa, evaluate local shear magnitude |tau12|=sigma_x |sin theta cos theta| at 0 and 45 degrees. Compare 0 and 50 MPa and explain which axis carries transverse stress. Propose digital image correlation to inspect strain nonuniformity.

A companion calculator called **Reciprocal Poisson ratio** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Transverse modulus = 12.42857 GPa**, the declared formula returns **0.025777778 dimensionless**; at **Transverse modulus = 15.57143 GPa**, it returns **0.032296296 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.0020740741 dimensionless per GPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Stress transformation does not predict failure unless coupled to suitable strengths and interaction criteria.

### Exercises and self-assessment

**Exercise 3.3A — Physical mechanism.** Why can a 45-degree coupon appear much softer than a zero-degree coupon without fiber weakening? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.3B — Numerical cross-check.** Recalculate **0.025777778 dimensionless** from the companion formula at **12.42857 GPa** and compare with **0.032296296 dimensionless** at **15.57143 GPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 3.3C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **tab-induced stress concentration or material nonlinearity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Lesson 3.4: Directional modulus and stiffness polar plots

### Scientific foundation

Apparent modulus varies continuously with loading angle for an orthotropic ply. In transformed compliance, 1/Ex(theta)=S11 c^4 + S22 s^4 +(2 S12+S66)s²c², where c=cos(theta), s=sin(theta). This relation can generate a polar plot of the elastic response but assumes stress uniformity and no damage. The 45-degree modulus is not generally the arithmetic average of E1 and E2. Stress concentrations around tabs and grips can confuse experimental verification.

**Governing relationship or decision rule:** Ex(theta) follows transformed compliance, not a linear interpolation of direction cosines. Read every term in the equation as part of a declared specimen condition. In **directional modulus and stiffness polar plots**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare predicted Ex at theta=0, 45 and 90 degrees using a fixed Q or compliance data set. Check limiting angles against E1 and E2 and require symmetry about theta sign for pure axial modulus. If a coupon measurement lies outside a plausible range, check alignment, thickness and strain calibration before changing constitutive parameters.

A companion calculator called **Local shear from global axial tension** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Ply angle = 51.42857 degrees**, the declared formula returns **48.746396 MPa**; at **Ply angle = 64.28571 degrees**, it returns **39.091574 MPa**. On this interval the modeled value decreases, and the two-point slope is **-0.75093056 MPa per degrees**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Classical homogeneous lamina formulas can fail near free edges, holes and delaminations; a laminate may not share single-ply symmetry.

### Exercises and self-assessment

**Exercise 3.4A — Physical mechanism.** How can a polar modulus graph hide an interface problem until large strain? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.4B — Numerical cross-check.** Recalculate **48.746396 MPa** from the companion formula at **51.42857 degrees** and compare with **39.091574 MPa** at **64.28571 degrees**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 3.4C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **tab-induced stress concentration or material nonlinearity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_5 -->

## Lesson 3.5: Thermal and moisture expansion in plies

### Scientific foundation

Orthotropic layers can expand differently along and across their reinforcements. Temperature and moisture changes introduce eigenstrains, so a laminate may deform even under zero external loads. Hygrothermal strains are transformed to global axes like other strain tensors but can produce bending or twist depending on stacking asymmetry. A property change due to moisture plasticization is separate from swelling strain and may need time-dependent diffusion analysis. Moisture effects also depend on edge exposure.

**Governing relationship or decision rule:** Free orthotropic strains are epsilon_1^T=alpha1 ΔT and epsilon_2^T=alpha2 ΔT before restraint. Read every term in the equation as part of a declared specimen condition. In **thermal and moisture expansion in plies**, a valid calculation requires material-axis orientation, fiber and matrix fractions, specimen conditions, an explicit unit system and geometrically defined quantities. The same nominal fiber/matrix formulation may conceal different tow waviness, stacking sequence, porosity, cure state or interlaminar integrity. An unchanged axial elastic slope does not establish equivalent transverse fracture resistance, compression-after-impact strength or fatigue lifetime. Interpret a measured value only in its actual loading direction and microstructural condition.

### Worked composite investigation

Compare a zero-degree ply and a 90-degree ply during a controlled temperature rise. Specify alpha1=1e-6 /K and alpha2=30e-6 /K as synthetic inputs; compute free strains for 80 K heating. Describe an unsymmetric two-ply stack and predict an observable curvature without pretending a simple free-strain formula provides exact bending radius.

A companion calculator called **Reciprocal Poisson ratio** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Transverse modulus = 18.71429 GPa**, the declared formula returns **0.038814815 dimensionless**; at **Transverse modulus = 21.85714 GPa**, it returns **0.045333333 dimensionless**. On this interval the modeled value increases, and the two-point slope is **0.0020740741 dimensionless per GPa**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real composite system.

### Evidence, uncertainty, and a competing mechanism

Moisture equilibrium and temperature gradients are not always achieved; coatings and adhesive bonds modify constraints.

### Exercises and self-assessment

**Exercise 3.5A — Physical mechanism.** How can a composite panel warp without any mechanically applied bending moment? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 3.5B — Numerical cross-check.** Recalculate **0.038814815 dimensionless** from the companion formula at **18.71429 GPa** and compare with **0.045333333 dimensionless** at **21.85714 GPa**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real composite specimen.

**Exercise 3.5C — Test design.** Propose a fabrication, conditioning or test matrix that addresses **tab-induced stress concentration or material nonlinearity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_4 -->

## Integrated investigation: Off-axis coupons and inconsistent constants

### The evidence problem

Two laboratories obtain different 45-degree modulus values on apparently identical tape. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which reinforcement architecture or processing route seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Reconstruct orthotropic axes, strain definitions, compliance reciprocity and coupon end constraints. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **orthotropic constitutive response** and **material-axis parameters versus global stress** through the map. For micromechanics, state axial or transverse boundary assumptions and measure fiber fraction independently. For an orthotropic lamina, transform elastic constants with explicit material axes. For a laminate, calculate through-thickness stiffness and test bending-extension coupling. For manufacturing, distinguish commanded temperature from actual part cure and flow history. For damage, match local crack or impact driving force with mode-appropriate conditioned fracture resistance.

### Validation plan, report, and counterfactual

Perform directional strain-field mapping and matched humidity and thermal history tests. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing composite families, write down the constraints that matter for directional stiffness, delamination toughness, impact damage, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Ideal plane-stress transformations omit edge stress concentrations and softening. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **orthotropic constitutive response** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **material-axis parameters versus global stress** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **tab-induced stress concentration or material nonlinearity** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_5 -->

