# Unit 1: Force Systems, Vectors, and Coordinates

# Unit 1 · Lesson 1 — Vectors, units, and coordinates

**Unit objective:** Express forces as vectors, determine moments and couples, and replace distributed actions with properly located resultants.

## Why this concept matters

A force requires magnitude, direction, sense, and point of application. A positive x component does not by itself tell you whether a cable is in tension. Resolve the geometry from a sketch before writing signs. With a force of magnitude F inclined by theta from the positive horizontal, Fx = F cos(theta) and Fy = F sin(theta). Both components retain units of newtons, while the direction angle is dimensionless in the trigonometric function. Coordinate choices are arbitrary but must be documented.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Draw the force arrows on a single set of axes. Each component and each moment term carries a sign, and the sign can only be assigned after the reference orientation is fixed. If you move an applied force to another point on a rigid body, add the necessary couple to preserve the equivalent loading.

## Deriving an appropriate model

Begin with a physically labeled drawing of **cable at a temporary scaffold joint**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`F_x=550 cos 35°, F_y=550 sin 35°`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

An independent sketch may reveal that the effective moment arm is shorter than the visible distance between connection points. Resolve quantities on a single axis before comparing two alternative designs.

## Worked engineering illustration

**Context:** Cable at a temporary scaffold joint.

**Known information and task:** Resolve 550 N at 35 degrees above the positive x-axis.

**Equation:** `F_x=550 cos 35°, F_y=550 sin 35°`.

**Reference outcome:** **450.53 N and 315.48 N**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** An installer may specify cable tension while a structural drawing specifies global components; they are not interchangeable. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Confusing an angle measured from a vertical line with an angle measured from the x-axis.

If geometry changes, verify both the direction of each force and the position of its line of action. For a 2D resultant, compare component sums with the magnitude rather than adding magnitudes directly. A 3-4-5 component triangle provides an elementary magnitude check. For moments, carry N·m and verify the sign of r_x F_y−r_y F_x from a sketch.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For cable at a temporary scaffold joint, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_x=550 cos 35°, F_y=550 sin 35°`.

**Q2 · Computation and trend.** Reproduce the calculation **resolve 550 n at 35 degrees above the positive x-axis**, comparing with **450.53 N and 315.48 N**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_x=550 cos 35°, F_y=550 sin 35°` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for cable at a temporary scaffold joint but appears to be confusing an angle measured from a vertical line with an angle measured from the x-axis. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **450.53 N and 315.48 N** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: cable at a temporary scaffold joint. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 1 · Lesson 2 — Resultants and vector addition

**Unit objective:** Express forces as vectors, determine moments and couples, and replace distributed actions with properly located resultants.

## Why this concept matters

Multiple concurrent forces can be replaced by their vector sum for predicting net translational action. Sum x components and y components separately, then calculate magnitude using the Pythagorean rule. The inverse tangent alone may lose the quadrant, so use atan2(Fy,Fx). The resultant is zero when every coordinate sum is zero, which is necessary for equilibrium but not sufficient when moments remain. A graphical polygon can expose an incorrect direction, yet it cannot substitute for an accurate numerical calculation.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Draw the force arrows on a single set of axes. Each component and each moment term carries a sign, and the sign can only be assigned after the reference orientation is fixed. If you move an applied force to another point on a rigid body, add the necessary couple to preserve the equivalent loading.

## Deriving an appropriate model

An independent sketch may reveal that the effective moment arm is shorter than the visible distance between connection points. Resolve quantities on a single axis before comparing two alternative designs.

## Worked engineering illustration

**Context:** Three ropes pulling on a rigging ring.

**Known information and task:** Combine (300,0), (-100,220) and (-80,-120) N.

**Equation:** `R=(120,100) N`.

**Reference outcome:** **156.20 N at 39.81°**.

**Engineering interpretation:** Designing a sling bracket requires the actual vector load and its direction, not the total of cable readings. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Adding force magnitudes without preserving directions.

If geometry changes, verify both the direction of each force and the position of its line of action. For a 2D resultant, compare component sums with the magnitude rather than adding magnitudes directly. A 3-4-5 component triangle provides an elementary magnitude check. For moments, carry N·m and verify the sign of r_x F_y−r_y F_x from a sketch.

## Guided questions with answer criteria

**Q1 · Representation.** For three ropes pulling on a rigging ring, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `R=(120,100) N`.

**Q2 · Computation and trend.** Reproduce the calculation **combine (300,0), (-100,220) and (-80,-120) n**, comparing with **156.20 N at 39.81°**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `R=(120,100) N` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for three ropes pulling on a rigging ring but appears to be adding force magnitudes without preserving directions. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 1 · Lesson 3 — Position vectors and moments

**Unit objective:** Express forces as vectors, determine moments and couples, and replace distributed actions with properly located resultants.

## Why this concept matters

A force at an offset can cause rotation even when its translational component is modest. The moment about O is r cross F; in a plane its scalar z component equals x Fy minus y Fx. The location vector must run from the moment center to the force application point. The perpendicular distance formulation M=F d_perp is equivalent if the shortest distance to the line of action is used. State clockwise and counterclockwise signs explicitly and keep newton-metres distinct from newtons.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Draw the force arrows on a single set of axes. Each component and each moment term carries a sign, and the sign can only be assigned after the reference orientation is fixed. If you move an applied force to another point on a rigid body, add the necessary couple to preserve the equivalent loading.

## Deriving an appropriate model

An independent sketch may reveal that the effective moment arm is shorter than the visible distance between connection points. Resolve quantities on a single axis before comparing two alternative designs.

## Worked engineering illustration

**Context:** Hand force on a control lever.

**Known information and task:** Apply (0,-120) N at r=(0.35,0.08) m.

**Equation:** `M_z=0.35(-120)-0.08(0)`.

**Reference outcome:** **-42 N·m clockwise**.

**Engineering interpretation:** Torque-sensitive fasteners and access handles are evaluated using a line of action, not just hand-force magnitude. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using the full lever length as distance when the force is not perpendicular.

If geometry changes, verify both the direction of each force and the position of its line of action. For a 2D resultant, compare component sums with the magnitude rather than adding magnitudes directly. A 3-4-5 component triangle provides an elementary magnitude check. For moments, carry N·m and verify the sign of r_x F_y−r_y F_x from a sketch.

## Guided questions with answer criteria

**Q1 · Representation.** For hand force on a control lever, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `M_z=0.35(-120)-0.08(0)`.

**Q2 · Computation and trend.** Reproduce the calculation **apply (0,-120) n at r=(0.35,0.08) m**, comparing with **-42 N·m clockwise**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `M_z=0.35(-120)-0.08(0)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for hand force on a control lever but appears to be using the full lever length as distance when the force is not perpendicular. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 1 · Lesson 4 — Couples and equivalent force systems

**Unit objective:** Express forces as vectors, determine moments and couples, and replace distributed actions with properly located resultants.

## Why this concept matters

Two equal opposite parallel forces separated by a distance create a pure couple: net force vanishes while the moment remains. A couple moment is a free vector under rigid-body mechanics and can be moved without altering external effect. An arbitrary system may be reduced at a chosen point to a resultant force R and resultant moment M_O. Moving the point changes the moment by a cross-product term, but does not change the physical loading. This equivalence applies to the whole rigid body, not automatically to internal stresses.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Draw the force arrows on a single set of axes. Each component and each moment term carries a sign, and the sign can only be assigned after the reference orientation is fixed. If you move an applied force to another point on a rigid body, add the necessary couple to preserve the equivalent loading.

## Deriving an appropriate model

An independent sketch may reveal that the effective moment arm is shorter than the visible distance between connection points. Resolve quantities on a single axis before comparing two alternative designs.

## Worked engineering illustration

**Context:** A two-handed wheel adjustment.

**Known information and task:** Use two 75 N opposite forces 0.28 m apart.

**Equation:** `M=75×0.28`.

**Reference outcome:** **21 N·m**.

**Engineering interpretation:** Wheel and valve-actuator specifications commonly distinguish operating torque from net external force. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Dropping the couple because the two applied forces sum to zero.

If geometry changes, verify both the direction of each force and the position of its line of action. For a 2D resultant, compare component sums with the magnitude rather than adding magnitudes directly. A 3-4-5 component triangle provides an elementary magnitude check. For moments, carry N·m and verify the sign of r_x F_y−r_y F_x from a sketch.

## Guided questions with answer criteria

**Q1 · Representation.** For a two-handed wheel adjustment, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `M=75×0.28`.

**Q2 · Computation and trend.** Reproduce the calculation **use two 75 n opposite forces 0.28 m apart**, comparing with **21 N·m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `M=75×0.28` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for a two-handed wheel adjustment but appears to be dropping the couple because the two applied forces sum to zero. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 1 · Lesson 5 — Force-system design workshop

**Unit objective:** Express forces as vectors, determine moments and couples, and replace distributed actions with properly located resultants.

## Why this concept matters

A coherent free-body diagram begins with a defined boundary and a deliberately chosen reference frame. A bracket can be subjected simultaneously to point forces, an applied couple, and weight acting at its mass center. Reducing all actions to a chosen origin simplifies external equilibrium but can hide where local peak stresses develop. Present both the reduced force-couple pair and the original loading diagram when handing the analysis to a designer. Sensitivity to dimension tolerances should be checked before accepting the answer.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Draw the force arrows on a single set of axes. Each component and each moment term carries a sign, and the sign can only be assigned after the reference orientation is fixed. If you move an applied force to another point on a rigid body, add the necessary couple to preserve the equivalent loading.

## Deriving an appropriate model

An independent sketch may reveal that the effective moment arm is shorter than the visible distance between connection points. Resolve quantities on a single axis before comparing two alternative designs.

## Worked engineering illustration

**Context:** Equipment bracket with point force and couple.

**Known information and task:** At x=0.4 m apply downward 300 N; also apply +25 N·m couple.

**Equation:** `M_O=-300×0.4+25`.

**Reference outcome:** **-95 N·m**.

**Engineering interpretation:** The reduced moment is an equilibrium bookkeeping device; detailed local component sizing still needs stress analysis. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Treating a pure moment as though it has a point of application like a force.

If geometry changes, verify both the direction of each force and the position of its line of action. For a 2D resultant, compare component sums with the magnitude rather than adding magnitudes directly. A 3-4-5 component triangle provides an elementary magnitude check. For moments, carry N·m and verify the sign of r_x F_y−r_y F_x from a sketch.

## Guided questions with answer criteria

**Q1 · Representation.** For equipment bracket with point force and couple, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `M_O=-300×0.4+25`.

**Q2 · Computation and trend.** Reproduce the calculation **at x=0.4 m apply downward 300 n; also apply +25 n·m couple**, comparing with **-95 N·m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `M_O=-300×0.4+25` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for equipment bracket with point force and couple but appears to be treating a pure moment as though it has a point of application like a force. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

