# Unit 8: Impulse-Momentum and Engineering Mechanisms

# Unit 8 · Lesson 1 — Linkage position and velocity

**Unit objective:** Connect equilibrium and dynamics to real design decisions and communicate model limitations.

## Why this concept matters

A planar linkage relates input angle and displacement to output motion through geometric constraints. A simple slider-crank approximately maps rotation into translation, but the exact nonlinear relationship depends on crank and connecting-rod lengths. Position closure equations should be differentiated carefully to obtain velocities; a constant input angular speed does not imply constant output slider speed. Near a dead-center configuration, numerical sensitivity and force amplification may become extreme.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Build the analysis around one operating state of the complete machine. Internal force and power transformations should be traceable from input through each connection to the load and back to the supports. Friction, efficiency, dynamic loads and certification are separate issues.

## Deriving an appropriate model

Begin with a physically labeled drawing of **slider-crank linkage**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`x=r cosθ+√(l²−r² sin²θ)`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

The load passes through every connected component, including those not shown in an idealized force equation. Trace power, force, torque, speed, and reactions through the same operating state.

## Worked engineering illustration

**Context:** Slider-crank linkage.

**Known information and task:** Crank r=0.05 m, rod l=0.20 m, θ=60°.

**Equation:** `x=r cosθ+√(l²−r² sin²θ)`.

**Reference outcome:** **≈0.2203 m**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** Mechanism clearance and interference checks should precede dynamic force calculations. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Replacing exact linkage geometry with x=r cosθ far outside the long-rod limit.

Certification and physical testing cannot be inferred from successful output of an educational simulator. Across a transmission, angular speed ratio and torque ratio are related through conservation of power only after efficiency and operation direction are specified. A large output force does not by itself establish safe travel, locking, or mechanical integrity.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For slider-crank linkage, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `x=r cosθ+√(l²−r² sin²θ)`.

**Q2 · Computation and trend.** Reproduce the calculation **crank r=0.05 m, rod l=0.20 m, θ=60°**, comparing with **≈0.2203 m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `x=r cosθ+√(l²−r² sin²θ)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for slider-crank linkage but appears to be replacing exact linkage geometry with x=r cosθ far outside the long-rod limit. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **≈0.2203 m** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: slider-crank linkage. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 8 · Lesson 2 — Mechanical advantage and virtual work

**Unit objective:** Connect equilibrium and dynamics to real design decisions and communicate model limitations.

## Why this concept matters

An ideal lossless mechanism obeys input work equal to output work. In a quasistatic displacement ratio, F_in dx_in≈F_out dx_out. Mechanical advantage therefore changes with geometric configuration. A machine does not create energy; very large ideal output force accompanies a very small output displacement and may correspond to a near-singular pose. Real efficiencies, friction, stiffness, and locking must be treated explicitly.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Build the analysis around one operating state of the complete machine. Internal force and power transformations should be traceable from input through each connection to the load and back to the supports. Friction, efficiency, dynamic loads and certification are separate issues.

## Deriving an appropriate model

The load passes through every connected component, including those not shown in an idealized force equation. Trace power, force, torque, speed, and reactions through the same operating state.

## Worked engineering illustration

**Context:** Manual lever lifting a load.

**Known information and task:** Input travel 0.45 m, output travel 0.06 m, 100 N input.

**Equation:** `F_out=100×.45/.06`.

**Reference outcome:** **750 N ideal output**.

**Engineering interpretation:** Safe working capacity requires strength and stability independent of energy accounting. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Applying constant mechanical advantage across a nonlinear linkage stroke.

Certification and physical testing cannot be inferred from successful output of an educational simulator. Across a transmission, angular speed ratio and torque ratio are related through conservation of power only after efficiency and operation direction are specified. A large output force does not by itself establish safe travel, locking, or mechanical integrity.

## Guided questions with answer criteria

**Q1 · Representation.** For manual lever lifting a load, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_out=100×.45/.06`.

**Q2 · Computation and trend.** Reproduce the calculation **input travel 0.45 m, output travel 0.06 m, 100 n input**, comparing with **750 N ideal output**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_out=100×.45/.06` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for manual lever lifting a load but appears to be applying constant mechanical advantage across a nonlinear linkage stroke. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 8 · Lesson 3 — Dimensions, similitude, and scaling

**Unit objective:** Connect equilibrium and dynamics to real design decisions and communicate model limitations.

## Why this concept matters

Before numerical computation, verify that each equation is dimensionally consistent. Newtons are kg·m/s², moments are N·m, impulse N·s, and both kinetic energy and mechanical work are joules. Matching nondimensional groups can help transfer experiments between scales, but geometric similarity alone rarely preserves all mechanical behavior. A scaled structure may have different gravity-to-strength ratios or Reynolds numbers. Report reference units, conversions, and nondimensional assumptions.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Build the analysis around one operating state of the complete machine. Internal force and power transformations should be traceable from input through each connection to the load and back to the supports. Friction, efficiency, dynamic loads and certification are separate issues.

## Deriving an appropriate model

The load passes through every connected component, including those not shown in an idealized force equation. Trace power, force, torque, speed, and reactions through the same operating state.

## Worked engineering illustration

**Context:** Prototype lifting beam.

**Known information and task:** Length doubles, geometrically similar area scales by factor four.

**Equation:** `A_new/A_old=(2)²`.

**Reference outcome:** **4**.

**Engineering interpretation:** Scale-model data must be interpreted under relevant force and material similitude. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assuming structural mass or surface area doubles when length doubles.

Certification and physical testing cannot be inferred from successful output of an educational simulator. Across a transmission, angular speed ratio and torque ratio are related through conservation of power only after efficiency and operation direction are specified. A large output force does not by itself establish safe travel, locking, or mechanical integrity.

## Guided questions with answer criteria

**Q1 · Representation.** For prototype lifting beam, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `A_new/A_old=(2)²`.

**Q2 · Computation and trend.** Reproduce the calculation **length doubles, geometrically similar area scales by factor four**, comparing with **4**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `A_new/A_old=(2)²` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for prototype lifting beam but appears to be assuming structural mass or surface area doubles when length doubles. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 8 · Lesson 4 — Uncertainty, safety factors, and verification

**Unit objective:** Connect equilibrium and dynamics to real design decisions and communicate model limitations.

## Why this concept matters

A computed load depends on geometry, material properties, measurements, and modeling choices. Sensitivity analysis asks how output changes when inputs vary, not just how a central estimate looks. A safety factor compares nominal capacity and demand under a defined criterion; it does not automatically address instability, fatigue, or dynamic amplification. Separate verification of numerical implementation from validation of the physical assumptions. Independent hand estimates, measurements, and controlled comparisons are complementary.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Build the analysis around one operating state of the complete machine. Internal force and power transformations should be traceable from input through each connection to the load and back to the supports. Friction, efficiency, dynamic loads and certification are separate issues.

## Deriving an appropriate model

The load passes through every connected component, including those not shown in an idealized force equation. Trace power, force, torque, speed, and reactions through the same operating state.

## Worked engineering illustration

**Context:** Test stand load estimate.

**Known information and task:** Nominal force 850 N and rated capacity 1700 N.

**Equation:** `SF_nominal=1700/850`.

**Reference outcome:** **2.0 nominal**.

**Engineering interpretation:** Engineering decisions require an explicit load case and relevant code/standard where applicable. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Claiming a factor of safety is verified without establishing applicable failure modes.

Certification and physical testing cannot be inferred from successful output of an educational simulator. Across a transmission, angular speed ratio and torque ratio are related through conservation of power only after efficiency and operation direction are specified. A large output force does not by itself establish safe travel, locking, or mechanical integrity.

## Guided questions with answer criteria

**Q1 · Representation.** For test stand load estimate, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `SF_nominal=1700/850`.

**Q2 · Computation and trend.** Reproduce the calculation **nominal force 850 n and rated capacity 1700 n**, comparing with **2.0 nominal**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `SF_nominal=1700/850` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for test stand load estimate but appears to be claiming a factor of safety is verified without establishing applicable failure modes. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 8 · Lesson 5 — Integrated mechanism engineering case

**Unit objective:** Connect equilibrium and dynamics to real design decisions and communicate model limitations.

## Why this concept matters

Analyze a small powered hoist using a single consistent model: load weight produces cable tension, drum radius maps tension into torque, and transmission efficiency changes required motor-side torque. During acceleration, inertia and rotational dynamics must be included instead of assuming statics. The load path includes cable, drum, shaft, bearings, mounts, and supporting structure. The same system can be studied with free-body diagrams, power balance, angular acceleration, and uncertainty bounds.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Build the analysis around one operating state of the complete machine. Internal force and power transformations should be traceable from input through each connection to the load and back to the supports. Friction, efficiency, dynamic loads and certification are separate issues.

## Deriving an appropriate model

The load passes through every connected component, including those not shown in an idealized force equation. Trace power, force, torque, speed, and reactions through the same operating state.

## Worked engineering illustration

**Context:** Workshop hoist drum.

**Known information and task:** Load 120 kg; drum radius 0.12 m; static hold condition.

**Equation:** `T=mg; M_drum=T r`.

**Reference outcome:** **T≈1177.2 N; M≈141.26 N·m**.

**Engineering interpretation:** A full equipment design must include certification, wire-rope standards, impact load, braking redundancy and appropriate supervision. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Treating static holding torque as the full torque requirement for acceleration or emergency braking.

Certification and physical testing cannot be inferred from successful output of an educational simulator. Across a transmission, angular speed ratio and torque ratio are related through conservation of power only after efficiency and operation direction are specified. A large output force does not by itself establish safe travel, locking, or mechanical integrity.

## Guided questions with answer criteria

**Q1 · Representation.** For workshop hoist drum, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `T=mg; M_drum=T r`.

**Q2 · Computation and trend.** Reproduce the calculation **load 120 kg; drum radius 0.12 m; static hold condition**, comparing with **T≈1177.2 N; M≈141.26 N·m**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `T=mg; M_drum=T r` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for workshop hoist drum but appears to be treating static holding torque as the full torque requirement for acceleration or emergency braking. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

