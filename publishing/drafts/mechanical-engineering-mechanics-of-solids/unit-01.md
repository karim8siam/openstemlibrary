# Unit 1: Stress, Strain and Elastic Response

# Unit 1, Lesson 1 — Traction vectors and cut planes

**Learning target.** Turn loads and measured dimensional changes into reproducible stress–strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `sigma_avg=F/A = 24000/(120×10^-6) Pa`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Cutting an imaginary plane through a loaded solid exposes the force per area transmitted across that plane. Its normal component creates normal stress, and its in-plane component creates shear stress. The traction vector depends on plane orientation even when the underlying stress state is unchanged. Average traction is defensible only over an area for which resultant force and area are both well defined.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** A flat connector plate receives 24 kN normal to a 120 mm² net cut section. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_avg=F/A = 24000/(120×10^-6) Pa`.

A reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **traction vectors and cut planes**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** A flat connector plate receives 24 kN normal to a 120 mm² net cut section.

**Equation:** `sigma_avg=F/A = 24000/(120×10^-6) Pa`.

**Reference answer:** **200 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Net-section tension checks must be separated from bearing and tear-out checks. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using gross area when a bolt hole removes part of the net section.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 MPa**, including units.

*Answer guidance:* Use `sigma_avg=F/A = 24000/(120×10^-6) Pa` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using gross area when a bolt hole removes part of the net section.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Record whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 1, Lesson 2 — Engineering and true stress

**Learning target.** Turn loads and measured dimensional changes into reproducible stress–strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `sigma_true≈sigma_eng(1+e_eng)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Engineering stress uses the original specimen area, while true stress uses instantaneous area. Their difference becomes substantial after plastic deformation and localization. Under uniform volume-preserving plastic deformation before necking, the often-used approximation sigma_true=sigma_eng(1+e_eng) can be useful; it does not extend uncritically past diffuse necking. Data acquisition must specify which quantity was plotted.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** At 10% engineering strain a specimen carries 300 MPa engineering stress before necking. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_true≈sigma_eng(1+e_eng)`.

A reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **engineering and true stress**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** At 10% engineering strain a specimen carries 300 MPa engineering stress before necking.

**Equation:** `sigma_true≈sigma_eng(1+e_eng)`.

**Reference answer:** **330 MPa (uniform-volume approximation)**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Fitting a plasticity law requires the correct stress and strain measure. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Applying the simple true-stress conversion after necking has made strain highly nonuniform.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **330 MPa (uniform-volume approximation)**, including units.

*Answer guidance:* Use `sigma_true≈sigma_eng(1+e_eng)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *applying the simple true-stress conversion after necking has made strain highly nonuniform.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Record whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 1, Lesson 3 — Axial strain and displacement

**Learning target.** Turn loads and measured dimensional changes into reproducible stress–strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `e=0.125/250`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Engineering axial strain e=(L−L0)/L0 is the average extension divided by initial gauge length. A displacement between grips is not necessarily the displacement of a specimen gauge section because the testing machine and fixtures deform. Small strain is a linear approximation to a spatially varying deformation field. State the reference state before comparing two readings.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** A 250 mm gauge region extends by 0.125 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `e=0.125/250`.

A reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **axial strain and displacement**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** A 250 mm gauge region extends by 0.125 mm.

**Equation:** `e=0.125/250`.

**Reference answer:** **0.0005 = 500 microstrain**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Extensometers measure a chosen length, which may exclude grip compliance. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Mixing grip motion with direct gauge-extension measurements.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.0005 = 500 microstrain**, including units.

*Answer guidance:* Use `e=0.125/250` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *mixing grip motion with direct gauge-extension measurements.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Record whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 1, Lesson 4 — Poisson contraction and elastic constants

**Learning target.** Turn loads and measured dimensional changes into reproducible stress–strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `e_trans=−nu×e_axial`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For uniaxial isotropic linear elasticity, lateral strain is approximately minus Poisson ratio times axial strain. This small-strain relation is not a general law for anisotropic composites or nonlinear rubbers. When isotropy is warranted, E, G and Poisson ratio are related by E=2G(1+nu). Admissible elastic constants also respect material stability constraints.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** An isotropic coupon has axial strain 1200 microstrain and nu=0.29. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `e_trans=−nu×e_axial`.

A reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **poisson contraction and elastic constants**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** An isotropic coupon has axial strain 1200 microstrain and nu=0.29.

**Equation:** `e_trans=−nu×e_axial`.

**Reference answer:** **−348 microstrain**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Lateral gauges provide a cross-check for a reported elastic Poisson ratio. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assuming transverse strain must always have the same sign as longitudinal strain.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **−348 microstrain**, including units.

*Answer guidance:* Use `e_trans=−nu×e_axial` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assuming transverse strain must always have the same sign as longitudinal strain.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Record whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 1, Lesson 5 — Elastic modulus and proportional response

**Learning target.** Turn loads and measured dimensional changes into reproducible stress–strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `E=Δsigma/Δe`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Within a linear elastic range, E is the slope of stress versus axial strain; it is not yield stress, hardness or ultimate tensile strength. A secant estimate across a nonlinear range can differ from the tangent modulus. Materials with rate or temperature dependence must be characterized at the relevant conditions. Zero-load offsets and fixture displacement can bias an apparent slope.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** An elastic specimen increases stress by 80 MPa as strain increases by 0.0004. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `E=Δsigma/Δe`.

A reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **elastic modulus and proportional response**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** An elastic specimen increases stress by 80 MPa as strain increases by 0.0004.

**Equation:** `E=Δsigma/Δe`.

**Reference answer:** **200 GPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A modulus helps predict deformation, but allowable stress requires additional strength data. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Treating elastic stiffness and failure strength as interchangeable material properties.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 GPa**, including units.

*Answer guidance:* Use `E=Δsigma/Δe` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *treating elastic stiffness and failure strength as interchangeable material properties.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Record whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

