# Unit 6: Particle Kinematics and Kinetics

# Unit 6 · Lesson 1 — Kinematics in one and two dimensions

**Unit objective:** Analyze how forces produce motion and how work and momentum summarize the resulting evolution.

## Why this concept matters

Particle position r(t) describes location, velocity is dr/dt and acceleration is dv/dt. With constant acceleration, v=v0+at and x=x0+v0 t+0.5 a t². Resolve axes and initial data before substituting. Constant acceleration formulas do not apply without qualification when acceleration depends on velocity or position. For projectiles under uniform gravity with negligible air resistance, horizontal velocity stays constant while vertical acceleration is -g.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

State the reference frame, initial conditions, and integration interval. Separate acceleration from velocity, then use work and momentum as cross-checks when the forces and time histories permit. A single numerical result must correspond to one precisely defined initial and final state.

## Deriving an appropriate model

Begin with a physically labeled drawing of **tool dropped in workshop**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`t=√(2h/g)`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

A change in velocity requires acceleration, but a nonzero velocity does not itself require net force in an inertial reference frame. Use an independent energy or impulse calculation to check a force-based solution wherever possible.

## Worked engineering illustration

**Context:** Tool dropped in workshop.

**Known information and task:** Dropped from rest over 2.0 m, g=9.81 m/s².

**Equation:** `t=√(2h/g)`.

**Reference outcome:** **≈0.639 s**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** Drop-zone controls must account for realistic release height and uncertainty. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using constant-velocity displacement for accelerated falling motion.

Keep the time interval and system boundary the same between any two methods being compared. One reliable cross-check is to solve a constant-force problem by three equivalent forms: acceleration integration, net work, and net impulse. If the three do not agree, check whether the force really is constant and whether the same start and end states were used.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For tool dropped in workshop, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `t=√(2h/g)`.

**Q2 · Computation and trend.** Reproduce the calculation **dropped from rest over 2.0 m, g=9.81 m/s²**, comparing with **≈0.639 s**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `t=√(2h/g)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for tool dropped in workshop but appears to be using constant-velocity displacement for accelerated falling motion. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **≈0.639 s** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: tool dropped in workshop. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 6 · Lesson 2 — Newtonian equations of motion

**Unit objective:** Analyze how forces produce motion and how work and momentum summarize the resulting evolution.

## Why this concept matters

Newton’s second law in an inertial frame states ΣF=ma for constant-mass particles. The net force produces acceleration, not velocity, so a moving object can have zero net force at constant speed. A free-body diagram provides all external forces. For a constrained motion, use axes aligned with convenient directions; a cable force may be unknown and must be solved together with acceleration. Friction models belong in the force balance rather than being added as an afterthought.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

State the reference frame, initial conditions, and integration interval. Separate acceleration from velocity, then use work and momentum as cross-checks when the forces and time histories permit. A single numerical result must correspond to one precisely defined initial and final state.

## Deriving an appropriate model

A change in velocity requires acceleration, but a nonzero velocity does not itself require net force in an inertial reference frame. Use an independent energy or impulse calculation to check a force-based solution wherever possible.

## Worked engineering illustration

**Context:** Cart on level test track.

**Known information and task:** Mass 12 kg, net horizontal force 42 N.

**Equation:** `a=F/m`.

**Reference outcome:** **3.5 m/s²**.

**Engineering interpretation:** The same applied force produces different acceleration if the payload changes. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Equating a nonzero resultant force with constant velocity.

Keep the time interval and system boundary the same between any two methods being compared. One reliable cross-check is to solve a constant-force problem by three equivalent forms: acceleration integration, net work, and net impulse. If the three do not agree, check whether the force really is constant and whether the same start and end states were used.

## Guided questions with answer criteria

**Q1 · Representation.** For cart on level test track, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `a=F/m`.

**Q2 · Computation and trend.** Reproduce the calculation **mass 12 kg, net horizontal force 42 n**, comparing with **3.5 m/s²**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `a=F/m` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for cart on level test track but appears to be equating a nonzero resultant force with constant velocity. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 6 · Lesson 3 — Curvilinear and normal-tangential motion

**Unit objective:** Analyze how forces produce motion and how work and momentum summarize the resulting evolution.

## Why this concept matters

For motion along a curved path, acceleration can be decomposed into tangential part dv/dt and normal part v²/ρ toward the center of curvature. Normal acceleration changes direction even at constant speed. In circular motion the curvature radius equals the circle radius. A centripetal force is not a new additional force; it is the inward component of the sum of actual forces. This distinction avoids double counting when analyzing roller coasters or turning vehicles.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

State the reference frame, initial conditions, and integration interval. Separate acceleration from velocity, then use work and momentum as cross-checks when the forces and time histories permit. A single numerical result must correspond to one precisely defined initial and final state.

## Deriving an appropriate model

A change in velocity requires acceleration, but a nonzero velocity does not itself require net force in an inertial reference frame. Use an independent energy or impulse calculation to check a force-based solution wherever possible.

## Worked engineering illustration

**Context:** Robot arm tip moving on a circle.

**Known information and task:** Speed 3 m/s and radius 1.5 m.

**Equation:** `a_n=v²/r`.

**Reference outcome:** **6 m/s²**.

**Engineering interpretation:** Tip-speed limits are set by acceleration capacity as well as angular speed. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Adding a fictitious centripetal force to an already complete force diagram.

Keep the time interval and system boundary the same between any two methods being compared. One reliable cross-check is to solve a constant-force problem by three equivalent forms: acceleration integration, net work, and net impulse. If the three do not agree, check whether the force really is constant and whether the same start and end states were used.

## Guided questions with answer criteria

**Q1 · Representation.** For robot arm tip moving on a circle, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `a_n=v²/r`.

**Q2 · Computation and trend.** Reproduce the calculation **speed 3 m/s and radius 1.5 m**, comparing with **6 m/s²**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `a_n=v²/r` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for robot arm tip moving on a circle but appears to be adding a fictitious centripetal force to an already complete force diagram. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 6 · Lesson 4 — Work-energy principle

**Unit objective:** Analyze how forces produce motion and how work and momentum summarize the resulting evolution.

## Why this concept matters

The work of a force is the integral of F·dr along the motion path. The net work equals the change in kinetic energy for a particle: W_net=(1/2)m(v2²−v1²). A constant force at an angle only contributes its component parallel to displacement. Conservative forces may be represented by changes in potential energy; friction and other dissipative forces reduce recoverable mechanical energy. Work-energy avoids solving time histories for many displacement-based questions, but not for all contact force estimates.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

State the reference frame, initial conditions, and integration interval. Separate acceleration from velocity, then use work and momentum as cross-checks when the forces and time histories permit. A single numerical result must correspond to one precisely defined initial and final state.

## Deriving an appropriate model

A change in velocity requires acceleration, but a nonzero velocity does not itself require net force in an inertial reference frame. Use an independent energy or impulse calculation to check a force-based solution wherever possible.

## Worked engineering illustration

**Context:** Manual pallet pull.

**Known information and task:** 100 N horizontal pull across 4 m with no other net work.

**Equation:** `W=F d`.

**Reference outcome:** **400 J**.

**Engineering interpretation:** Energy calculations are useful for preliminary braking and actuator sizing. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Mistaking force magnitude for work without multiplying by displacement and direction factor.

Keep the time interval and system boundary the same between any two methods being compared. One reliable cross-check is to solve a constant-force problem by three equivalent forms: acceleration integration, net work, and net impulse. If the three do not agree, check whether the force really is constant and whether the same start and end states were used.

## Guided questions with answer criteria

**Q1 · Representation.** For manual pallet pull, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `W=F d`.

**Q2 · Computation and trend.** Reproduce the calculation **100 n horizontal pull across 4 m with no other net work**, comparing with **400 J**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `W=F d` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for manual pallet pull but appears to be mistaking force magnitude for work without multiplying by displacement and direction factor. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 6 · Lesson 5 — Impulse, momentum, and collision

**Unit objective:** Analyze how forces produce motion and how work and momentum summarize the resulting evolution.

## Why this concept matters

Linear momentum p=mv changes according to net impulse J=∫F dt. A short high-force contact may impart the same impulse as a smaller force acting longer, but peak stress may differ. Conservation of momentum applies to a system only when the net external impulse is negligible over the interval. Collision restitution and energy losses require separate information; momentum conservation does not mean kinetic energy is always conserved. State the system boundary before solving impact.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

State the reference frame, initial conditions, and integration interval. Separate acceleration from velocity, then use work and momentum as cross-checks when the forces and time histories permit. A single numerical result must correspond to one precisely defined initial and final state.

## Deriving an appropriate model

A change in velocity requires acceleration, but a nonzero velocity does not itself require net force in an inertial reference frame. Use an independent energy or impulse calculation to check a force-based solution wherever possible.

## Worked engineering illustration

**Context:** Test carriage collision.

**Known information and task:** Mass 5 kg, speed changes from +3 m/s to -1 m/s.

**Equation:** `J=m(v2−v1)`.

**Reference outcome:** **-20 N·s**.

**Engineering interpretation:** Protective barrier design needs an impact duration estimate to assess average and peak forces. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Assuming mechanical energy conservation in an inelastic collision.

Keep the time interval and system boundary the same between any two methods being compared. One reliable cross-check is to solve a constant-force problem by three equivalent forms: acceleration integration, net work, and net impulse. If the three do not agree, check whether the force really is constant and whether the same start and end states were used.

## Guided questions with answer criteria

**Q1 · Representation.** For test carriage collision, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `J=m(v2−v1)`.

**Q2 · Computation and trend.** Reproduce the calculation **mass 5 kg, speed changes from +3 m/s to -1 m/s**, comparing with **-20 N·s**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `J=m(v2−v1)` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for test carriage collision but appears to be assuming mechanical energy conservation in an inelastic collision. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

