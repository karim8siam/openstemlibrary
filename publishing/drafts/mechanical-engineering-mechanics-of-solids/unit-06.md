# Unit 6: Multiaxial Stress and Yield Criteria

# Unit 6, Lesson 1 — Stress components and equilibrium

**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `mean_normal=(sigma_x+sigma_y)/2`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

On a small material element, normal and shear stresses appear on several faces. Moment equilibrium requires the conventional shear components tau_xy=tau_yx in a classical continuum without couple stresses. The Cauchy stress tensor compactly encodes the plane-dependent traction. A plane-stress model assumes stress normal to a thin free surface is negligible; it is not the same as uniform strain.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** In 2D sigma_x=80 MPa, sigma_y=20 MPa, tau_xy=30 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `mean_normal=(sigma_x+sigma_y)/2`.

A coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stress components and equilibrium**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** In 2D sigma_x=80 MPa, sigma_y=20 MPa, tau_xy=30 MPa.

**Equation:** `mean_normal=(sigma_x+sigma_y)/2`.

**Reference answer:** **50 MPa mean normal stress**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Component conventions must be documented when importing FE results. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assuming shear on one element face has no complementary shear on the adjacent face.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **50 MPa mean normal stress**, including units.

*Answer guidance:* Use `mean_normal=(sigma_x+sigma_y)/2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assuming shear on one element face has no complementary shear on the adjacent face.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Check a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 6, Lesson 2 — Plane-stress transformation

**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_n=80cos²30°+20sin²30°`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Normal stress acting on a plane rotated by angle theta follows sigma_n=sigma_x cos²theta+sigma_y sin²theta+2 tau_xy sin theta cos theta, with appropriate positive-angle and stress convention. The shear transformation uses corresponding sign terms. A principal plane carries no in-plane shear. Test the equation at theta=0 and theta=90° as independent boundary checks.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** Plane stress sigma_x=80, sigma_y=20 and tau_xy=0 MPa, rotated 30°. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_n=80cos²30°+20sin²30°`.

A coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **plane-stress transformation**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** Plane stress sigma_x=80, sigma_y=20 and tau_xy=0 MPa, rotated 30°.

**Equation:** `sigma_n=80cos²30°+20sin²30°`.

**Reference answer:** **65 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Stress transformation helps interpret off-axis strain gauges. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Using degrees as radians in a trigonometric library.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **65 MPa**, including units.

*Answer guidance:* Use `sigma_n=80cos²30°+20sin²30°` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *using degrees as radians in a trigonometric library.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Check a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 6, Lesson 3 — Principal stress and Mohr circle

**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_1=60+sqrt(40²+30²)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

In a plane stress state, principal in-plane values are sigma_avg ±sqrt(((sigma_x−sigma_y)/2)²+tau_xy²). Their sum equals sigma_x+sigma_y and principal-plane shear vanishes. The out-of-plane third principal stress equals zero only in the plane stress idealization. Ranking maximum and minimum principal stresses requires including that third value for full three-dimensional comparisons.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** Plane stress sigma_x=100, sigma_y=20 and tau=30 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_1=60+sqrt(40²+30²)`.

A coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **principal stress and mohr circle**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** Plane stress sigma_x=100, sigma_y=20 and tau=30 MPa.

**Equation:** `sigma_1=60+sqrt(40²+30²)`.

**Reference answer:** **110 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Brittle failure checks often consider tensile principal stress. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Ignoring the zero third principal when using a 3D failure criterion.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **110 MPa**, including units.

*Answer guidance:* Use `sigma_1=60+sqrt(40²+30²)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *ignoring the zero third principal when using a 3d failure criterion.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Check a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 6, Lesson 4 — Generalized Hooke law and plane strain

**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `epsilon_x=(sigma_x−nu sigma_y)/E`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Isotropic small-strain elasticity relates axial strain to all normal stresses through e_x=[sigma_x−nu(sigma_y+sigma_z)]/E. Thus a uniaxial strain response is not simply sigma_x/E when substantial lateral stresses exist. Under plane strain, out-of-plane strain is constrained to zero and sigma_z is generally nonzero. Plane stress instead sets sigma_z approximately zero.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** E=200 GPa, nu=0.3, sigma_x=120 MPa, sigma_y=40 MPa, sigma_z=0. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `epsilon_x=(sigma_x−nu sigma_y)/E`.

A coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **generalized hooke law and plane strain**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** E=200 GPa, nu=0.3, sigma_x=120 MPa, sigma_y=40 MPa, sigma_z=0.

**Equation:** `epsilon_x=(sigma_x−nu sigma_y)/E`.

**Reference answer:** **540 microstrain**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Thick constrained components require the right strain boundary model. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assuming zero out-of-plane strain implies zero out-of-plane stress.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **540 microstrain**, including units.

*Answer guidance:* Use `epsilon_x=(sigma_x−nu sigma_y)/E` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assuming zero out-of-plane strain implies zero out-of-plane stress.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Check a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 6, Lesson 5 — Von Mises and Tresca checks

**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_vm=sqrt(sigma_x²−sigma_x sigma_y+sigma_y²+3tau²)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For isotropic ductile metals under a plane stress approximation, von Mises equivalent stress is sqrt(sigma_x²−sigma_x sigma_y+sigma_y²+3 tau_xy²). It compares a multiaxial stress state to a uniaxial yielding characterization, not to ultimate strength automatically. Tresca uses maximum difference of principal stresses and can be more conservative for some states. Neither is a fatigue-life law.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** Plane stress sigma_x=100 MPa, sigma_y=0, tau_xy=50 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_vm=sqrt(sigma_x²−sigma_x sigma_y+sigma_y²+3tau²)`.

A coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **von mises and tresca checks**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** Plane stress sigma_x=100 MPa, sigma_y=0, tau_xy=50 MPa.

**Equation:** `sigma_vm=sqrt(sigma_x²−sigma_x sigma_y+sigma_y²+3tau²)`.

**Reference answer:** **132.29 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Material yield checks need a chosen criterion and a strength value at operating conditions. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Treating equivalent stress as a measured physical stress on one specific face.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **132.29 MPa**, including units.

*Answer guidance:* Use `sigma_vm=sqrt(sigma_x²−sigma_x sigma_y+sigma_y²+3tau²)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *treating equivalent stress as a measured physical stress on one specific face.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Check a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

