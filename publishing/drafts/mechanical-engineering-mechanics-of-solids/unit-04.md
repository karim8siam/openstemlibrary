# Unit 4: Beam Stress and Internal Resultants

# Unit 4, Lesson 1 — Shear-force and moment diagrams

**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `M_max=PL/4`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For a beam with distributed transverse loading, internal shear and moment are related to load and position through differential equilibrium: dV/dx=−w and dM/dx=V under a consistent sign convention. Concentrated forces jump the shear diagram; applied couples jump the moment diagram. An extremum in M often occurs where V crosses zero. The diagrams must satisfy total load and support reaction balance.

The essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.

**Context:** A 4 m simply supported beam carries a centered 10 kN point load. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `M_max=PL/4`.

A force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear-force and moment diagrams**.

If the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.

## Worked example and interpretation

**Situation:** A 4 m simply supported beam carries a centered 10 kN point load.

**Equation:** `M_max=PL/4`.

**Reference answer:** **10 kN m**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Bending stress checks start with the actual critical moment section. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Drawing a triangular shear diagram for a beam with only a point load.

A negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **10 kN m**, including units.

*Answer guidance:* Use `M_max=PL/4` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *drawing a triangular shear diagram for a beam with only a point load.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Compare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 4, Lesson 2 — Elastic bending stress

**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `sigma_max=6M/(bh²)`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

For homogeneous linear elastic symmetric beams in pure bending, |sigma|=|M|c/I. The rectangular-section maximum reduces to 6M/(bh²). This result neglects significant shear deformation, inelasticity and local stress concentrations. Orientation matters because bending stiffness depends on depth cubed. A beam section may yield or buckle locally before an elementary formula remains reliable.

Use the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.

**Context:** A 40 mm by 80 mm rectangle resists bending moment 2 kN m about its strong axis. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `sigma_max=6M/(bh²)`.

A force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **elastic bending stress**.

The model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.

## Worked example and interpretation

**Situation:** A 40 mm by 80 mm rectangle resists bending moment 2 kN m about its strong axis.

**Equation:** `sigma_max=6M/(bh²)`.

**Reference answer:** **46.875 MPa**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Section orientation frequently controls both strength and deflection. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Substituting width for depth in the squared denominator.

Linear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **46.875 MPa**, including units.

*Answer guidance:* Use `sigma_max=6M/(bh²)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *substituting width for depth in the squared denominator.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Compare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 4, Lesson 3 — Neutral axis and transformed sections

**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `|sigma|=E kappa |y|`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

In a homogeneous elastic beam under pure bending, the neutral axis passes through the centroid. A composite beam of bonded materials can be handled by a transformed-section approach if strain compatibility and linear elasticity hold. Modulus ratios weight transformed areas; the neutral axis need not coincide with geometric centroid. Connector slip undermines composite action.

An instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.

**Context:** Two bonded layers experience common curvature kappa=0.001 1/m; a fiber lies 20 mm from the neutral axis, E=70 GPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `|sigma|=E kappa |y|`.

A force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **neutral axis and transformed sections**.

An independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.

## Worked example and interpretation

**Situation:** Two bonded layers experience common curvature kappa=0.001 1/m; a fiber lies 20 mm from the neutral axis, E=70 GPa.

**Equation:** `|sigma|=E kappa |y|`.

**Reference answer:** **1.4 MPa at the fiber**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** Layer bonding and interface shear deserve explicit validation. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Assuming the neutral axis of dissimilar bonded materials is always at geometric mid-depth.

Safety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.4 MPa at the fiber**, including units.

*Answer guidance:* Use `|sigma|=E kappa |y|` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *assuming the neutral axis of dissimilar bonded materials is always at geometric mid-depth.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Compare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 4, Lesson 4 — Area second moments and beam geometry

**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `I=bh³/12`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

The centroidal I of a solid rectangular area for bending about its horizontal axis is bh³/12. I is a geometry quantity, not a material property; EI is a bending rigidity. When parts are moved away from the neutral axis, the parallel-axis term Ad² increases I. Cutouts subtract their own area moments and shifted contributions. CAD-generated values should still be unit checked.

The word “strength” is not interchangeable with “stiffness.” Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.

**Context:** A rectangular section has b=50 mm and h=100 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `I=bh³/12`.

A force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **area second moments and beam geometry**.

A true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.

## Worked example and interpretation

**Situation:** A rectangular section has b=50 mm and h=100 mm.

**Equation:** `I=bh³/12`.

**Reference answer:** **4.1667e6 mm⁴**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** An optimized cross-section places material where its bending contribution is greatest. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Entering an area in mm² where an I in mm⁴ is required.

Failure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **4.1667e6 mm⁴**, including units.

*Answer guidance:* Use `I=bh³/12` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *entering an area in mm² where an i in mm⁴ is required.* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Compare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

# Unit 4, Lesson 5 — Beam shear and interface forces

**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `q=VQ/I`, reconstruct the teaching example and identify one condition where the relation must be modified.

## Physical model

Under transverse loading, beam shear stress changes across the depth; thin web geometry often carries most of the vertical shear. Shear flow q=VQ/I can estimate the longitudinal force per unit length that connectors must transfer between built-up components. Fastener spacing follows from allowable fastener shear per pitch only with a defensible joint model. A local concentrated load may cause web crippling outside simple beam theory.

For a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.

**Context:** An interface has V=12 kN, Q=2e4 mm³ and I=8e6 mm⁴. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.

## Governing relationship and assumptions

**Teaching relation:** `q=VQ/I`.

A force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **beam shear and interface forces**.

Checking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.

## Worked example and interpretation

**Situation:** An interface has V=12 kN, Q=2e4 mm³ and I=8e6 mm⁴.

**Equation:** `q=VQ/I`.

**Reference answer:** **30 N/mm shear flow**.

Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.

**Engineering relevance:** A row of connectors must pass the interface force while limiting slip. Real use requires verified component-specific inputs; this example is not a certified working load.

## Diagnosing a false conclusion

**Common error:** Confusing shear flow N/mm with shear stress N/mm².

Do not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.

## Exercises and answer criteria

**1. Reconstruct.** Draw the section, mark all inputs and reproduce **30 N/mm shear flow**, including units.

*Answer guidance:* Use `q=VQ/I` with correct dimensions. Confirm the sign and the physical meaning of the quantity.

**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.

*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.

**3. Diagnose.** Explain why this error matters: *confusing shear flow n/mm with shear stress n/mm².* Propose a measurement or alternate equation that exposes it.

*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.

## Transfer to a real engineering study

Compare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.


---

