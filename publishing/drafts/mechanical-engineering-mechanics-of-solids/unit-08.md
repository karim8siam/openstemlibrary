# Unit 8: Testing, Models and Engineering Decisions

# Unit 8, Lesson 1 — Tensile test and offset yield

**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `E=Δsigma/Δepsilon`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

The tensile curve depends on strain measurement, cross-section definition, grip alignment, strain rate and temperature. An offset yield estimate constructs a line parallel to the elastic slope, shifted along the strain axis; it does not identify a unique intrinsic event in every material. Ultimate engineering stress and true stress after necking must not be conflated. Include machine compliance correction when needed.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** An initial linear segment changes stress by 100 MPa over strain change 0.0005. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `E=Δsigma/Δepsilon`.

An accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **tensile test and offset yield**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** An initial linear segment changes stress by 100 MPa over strain change 0.0005.

**Equation:** `E=Δsigma/Δepsilon`.

**Reference answer:** **200 GPa initial tangent estimate**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Test reports should identify specimen standard and uncertainty. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Calling the largest engineering tensile stress the elastic modulus.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 GPa initial tangent estimate**, including units.

*Answer guidance:* Use `E=Δsigma/Δepsilon` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *calling the largest engineering tensile stress the elastic modulus.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Design the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 8, Lesson 2 — Strain gauge conversion

**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `ΔR/R=GF epsilon`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A resistance strain gauge uses gauge factor GF=(ΔR/R)/epsilon along a specified sensing direction. Wheatstone bridge circuitry turns tiny resistance changes into a measurable voltage; completion and temperature compensation matter. A single gauge reports one local component, not a complete three-dimensional stress tensor. Gauge placement, bonding and lead resistance may dominate experimental error.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** A gauge of GF=2.1 experiences longitudinal strain 600 microstrain. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `ΔR/R=GF epsilon`.

An accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **strain gauge conversion**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** A gauge of GF=2.1 experiences longitudinal strain 600 microstrain.

**Equation:** `ΔR/R=GF epsilon`.

**Reference answer:** **0.00126 = 0.126%**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Strain gauges validate local model predictions when coordinate alignment is known. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Treating a uniaxial gauge reading as the entire principal stress state.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.00126 = 0.126%**, including units.

*Answer guidance:* Use `ΔR/R=GF epsilon` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *treating a uniaxial gauge reading as the entire principal stress state.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Design the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 8, Lesson 3 — Uncertainty and sensitivity

**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `I_new/I_old=(1.02)^3`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A dimension measured with uncertainty contributes nonlinearly to properties such as rectangular beam I∝h³ and shaft stress tau∝d^−3. First-order relative uncertainty propagation can estimate influence when errors are small and independent; correlation and systematic bias need additional treatment. Report uncertainty and resolution rather than implying unlimited digits from a computer.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** The height of a rectangular beam has a +2% change, with width fixed. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `I_new/I_old=(1.02)^3`.

An accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **uncertainty and sensitivity**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** The height of a rectangular beam has a +2% change, with width fixed.

**Equation:** `I_new/I_old=(1.02)^3`.

**Reference answer:** **1.061208, a 6.12% increase**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Tolerance prioritization can focus on the dimensions with strongest sensitivity. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assuming a 2% depth change produces only a 2% change in bending stiffness.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.061208, a 6.12% increase**, including units.

*Answer guidance:* Use `I_new/I_old=(1.02)^3` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assuming a 2% depth change produces only a 2% change in bending stiffness.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Design the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 8, Lesson 4 — Finite-element mesh convergence

**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `relative_change=(2.2−2.0)/2.2`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Finite-element answers are numerical approximations to a specified boundary-value model. Mesh refinement tests whether the discrete approximation stabilizes for a selected quantity, but sharp corners can create mathematical singularities whose peak stresses do not converge. A local displacement and an averaged reaction are often better convergence checks than the single largest nodal stress. Compare to at least one analytical benchmark.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** A scalar displacement estimate changes from 2.0 to 2.2 mm after refinement. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `relative_change=(2.2−2.0)/2.2`.

An accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **finite-element mesh convergence**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** A scalar displacement estimate changes from 2.0 to 2.2 mm after refinement.

**Equation:** `relative_change=(2.2−2.0)/2.2`.

**Reference answer:** **9.09% relative coarse-to-fine change**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Verification and experimental validation must remain separate activities. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Interpreting numerical convergence as proof that physical supports and loads were modeled correctly.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **9.09% relative coarse-to-fine change**, including units.

*Answer guidance:* Use `relative_change=(2.2−2.0)/2.2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *interpreting numerical convergence as proof that physical supports and loads were modeled correctly.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Design the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 8, Lesson 5 — Integrated member design review

**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `utilization=stress/allowable`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

A plausible solid-mechanics decision checks loading, internal actions, constitutive law, peak stress, displacement, stability, fatigue and manufacturing tolerances. If an input is based on a specification rather than a measurement, identify it as assumed. Choose a concept that is safe under credible load cases and that can be produced and inspected economically, but do not infer formal compliance from classroom tools.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** A member has estimated service stress 60 MPa and stated classroom allowable 120 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `utilization=stress/allowable`.

An accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **integrated member design review**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** A member has estimated service stress 60 MPa and stated classroom allowable 120 MPa.

**Equation:** `utilization=stress/allowable`.

**Reference answer:** **0.50 for this one screening criterion**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A design-review matrix records unresolved risks and evidence owners. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Treating a single stress utilization as proof against buckling, fatigue and fracture.

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.50 for this one screening criterion**, including units.

*Answer guidance:* Use `utilization=stress/allowable` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *treating a single stress utilization as proof against buckling, fatigue and fracture.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Design the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

