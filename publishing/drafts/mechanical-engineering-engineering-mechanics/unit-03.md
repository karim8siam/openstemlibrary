# Unit 3: Structural Trusses, Frames, and Machines

# Unit 3 · Lesson 1 — Two-force members and truss assumptions

**Unit objective:** Determine axial forces in trusses, reactions in frames, and action transmission in mechanical assemblies.

## Why this concept matters

A straight member connected only by ideal pins at both ends and carrying no intermediate load is a two-force member. End forces must be equal, opposite, and collinear; the member therefore carries axial tension or compression in the ideal model. Loads applied between joints introduce bending and invalidate the shortcut. Identify zero-force members from joint equilibrium before performing a full solution, but watch for supports or hidden loading. Internal truss forces are not identical to external support reactions.

We will use a deliberately simplified model first, then ask which real phenomena were discarded to obtain the simple equation. The difference between a teaching example and a credible design decision is largely in how those omissions are measured, documented, and tested.

Use the load path to decide which member or connection should be isolated. In an ideal truss, member action follows its axis; in a multi-force frame, shear and bending may be present. A method that solves reactions is not automatically a method for checking buckling or joint strength.

## Deriving an appropriate model

Begin with a physically labeled drawing of **roof truss diagonal**. Choose the boundary of the body or subassembly to be analyzed. Identify external actions, directions, distances, and material or contact hypotheses. Record data in a compact SI table before evaluating the mathematical relationship. If a force or moment depends on geometry, add the reference point and angle definition to the same drawing. This first modeling step should be intelligible without any calculation.

Next write the governing relation **`F_diag=1000/sin45°`**. State why it is applicable to the chosen idealization. Ask which quantities are known, which are unknown, and which additional balance or compatibility equations would be required if a quantity were changed. Algebra is the final step in a reasoning process, not the beginning. In particular, a mathematical solution may be internally consistent even though a physical connection has been modeled incorrectly.

A stiff-looking truss may contain a slender compression member whose buckling strength is low. Use a cut at a joint or along a member to inspect which action crosses the boundary.

## Worked engineering illustration

**Context:** Roof truss diagonal.

**Known information and task:** A diagonal at 45° delivers a vertical component of 1000 N.

**Equation:** `F_diag=1000/sin45°`.

**Reference outcome:** **1414.21 N axial magnitude**.

To reproduce the worked result, substitute the given numerical data with their units, evaluate the operations in a documented order, and round only the reported result. Label any signed component with its defined positive direction. Where the case is qualitative, present a symbolic balance and explain which remaining data determine its numerical value. A quick independent estimate should establish the expected order of magnitude before you trust the calculator. Do not confuse a condition derived for a particular ideal configuration with a general law that applies at every operating point.

**Engineering interpretation:** Member compression capacity requires stability checks beyond axial equilibrium. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Treating a member containing its own distributed weight as an exact two-force member.

A joint-force answer should satisfy both the local equilibrium equations and the whole-system reaction balance. At a truss joint with two unknown axial forces, two independent planar force equations can suffice. At a multi-force frame member, do not impose axial-only behavior. Reactions for the whole assembly should be solved before transferring them to a section when practical.

Complete two checks before closing your notebook. First, verify the physical dimensions of each side of the main equation. Second, reverse or perturb an input that has a clear geometric interpretation, then predict the effect on the output without touching a calculator. If the prediction and numerical evaluation disagree, investigate the axis definition, units, or selected formula. For a contact-bound problem, also verify that the computed state is compatible with the direction in which the contact can act.

## Guided questions with answer criteria

**Q1 · Representation.** For roof truss diagonal, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_diag=1000/sin45°`.

**Q2 · Computation and trend.** Reproduce the calculation **a diagonal at 45° delivers a vertical component of 1000 n**, comparing with **1414.21 N axial magnitude**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_diag=1000/sin45°` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for roof truss diagonal but appears to be treating a member containing its own distributed weight as an exact two-force member. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.

## Transfer investigation

A technician asks whether the result **1414.21 N axial magnitude** is enough to choose a replacement component. Write a short evaluation addressing (1) what has actually been computed, (2) which relevant loading states are absent, and (3) what evidence would establish a defensible rating. Relate each answer to the modeled device: roof truss diagonal. Explain why an exact numerical prediction of an ideal model may still be a poor predictor of an unmeasured real machine. Your recommendation must distinguish mathematics, assumptions, experimental measurements, and external engineering approval.



---

# Unit 3 · Lesson 2 — Method of joints

**Unit objective:** Determine axial forces in trusses, reactions in frames, and action transmission in mechanical assemblies.

## Why this concept matters

At an ideal pinned truss joint, sum horizontal and vertical forces separately. Solve joints with at most two unknown member forces; a simultaneous system may be needed at more complicated joints. Assume unknown axial member forces act away from the joint, corresponding to tension, then interpret a negative answer as compression. Force directions must follow actual member geometry. The procedure is local, so intermediate errors propagate through the structure if not checked.

Sign conventions are part of the model, not cosmetic decorations. A negative result is meaningful only after the assumed positive direction has been defined. It may indicate a real reversal, an unexpected contact state, or a modeling error; the diagram and independent checks decide which explanation fits.

Use the load path to decide which member or connection should be isolated. In an ideal truss, member action follows its axis; in a multi-force frame, shear and bending may be present. A method that solves reactions is not automatically a method for checking buckling or joint strength.

## Deriving an appropriate model

A stiff-looking truss may contain a slender compression member whose buckling strength is low. Use a cut at a joint or along a member to inspect which action crosses the boundary.

## Worked engineering illustration

**Context:** Triangular sign support.

**Known information and task:** A 600 N vertical joint load carried by two symmetric 60° members.

**Equation:** `2F sin60°=600`.

**Reference outcome:** **346.41 N each**.

**Engineering interpretation:** Joint solutions should reconstruct the applied load at every solved joint. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Using cos60° for the vertical component of a bar angled from the horizontal.

A joint-force answer should satisfy both the local equilibrium equations and the whole-system reaction balance. At a truss joint with two unknown axial forces, two independent planar force equations can suffice. At a multi-force frame member, do not impose axial-only behavior. Reactions for the whole assembly should be solved before transferring them to a section when practical.

## Guided questions with answer criteria

**Q1 · Representation.** For triangular sign support, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `2F sin60°=600`.

**Q2 · Computation and trend.** Reproduce the calculation **a 600 n vertical joint load carried by two symmetric 60° members**, comparing with **346.41 N each**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `2F sin60°=600` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for triangular sign support but appears to be using cos60° for the vertical component of a bar angled from the horizontal. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 3 · Lesson 3 — Method of sections

**Unit objective:** Determine axial forces in trusses, reactions in frames, and action transmission in mechanical assemblies.

## Why this concept matters

An imaginary cut through a truss exposes axial forces in the severed members. Choose a cut with no more than three unknown member forces for a single planar rigid-body section, then apply equilibrium to one side. Taking moments about the intersection of two cut members can isolate the third. Section choice often determines whether the arithmetic remains simple. A cut must not sever a support or miss a force that belongs on the selected part.

A mechanical principle can be learned from more than one representation: a labeled drawing, a scalar equation, a vector equation, an experimental trend, and a limiting case. Translating between these forms is a valuable skill because real engineering work rarely arrives as a perfectly prepared algebra exercise.

Use the load path to decide which member or connection should be isolated. In an ideal truss, member action follows its axis; in a multi-force frame, shear and bending may be present. A method that solves reactions is not automatically a method for checking buckling or joint strength.

## Deriving an appropriate model

A stiff-looking truss may contain a slender compression member whose buckling strength is low. Use a cut at a joint or along a member to inspect which action crosses the boundary.

## Worked engineering illustration

**Context:** Bridge truss panel.

**Known information and task:** Cut three members and take moments about a joint through two members.

**Equation:** `ΣM_joint=0`.

**Reference outcome:** **Third member isolated by moment balance**.

**Engineering interpretation:** This technique is efficient when only a few critical bars need checking. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Applying internal cut forces to both sections in the same free-body diagram.

A joint-force answer should satisfy both the local equilibrium equations and the whole-system reaction balance. At a truss joint with two unknown axial forces, two independent planar force equations can suffice. At a multi-force frame member, do not impose axial-only behavior. Reactions for the whole assembly should be solved before transferring them to a section when practical.

## Guided questions with answer criteria

**Q1 · Representation.** For bridge truss panel, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `ΣM_joint=0`.

**Q2 · Computation and trend.** Reproduce the calculation **cut three members and take moments about a joint through two members**, comparing with **Third member isolated by moment balance**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `ΣM_joint=0` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for bridge truss panel but appears to be applying internal cut forces to both sections in the same free-body diagram. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 3 · Lesson 4 — Frames, machines, and pins

**Unit objective:** Determine axial forces in trusses, reactions in frames, and action transmission in mechanical assemblies.

## Why this concept matters

Frames often contain multi-force members, so treating every link as purely axial produces a false model. Decompose the structure at internal pins; identify forces transmitted by each connection. Machine mechanisms can amplify an input force while reducing displacement, consistent with work conservation in an ideal lossless arrangement. Some parts transmit two components and torque through contact. Friction and finite pin size introduce additional effects not represented by a perfect hinge.

The central difficulty here is not remembering a formula but deciding whether the physical interaction has been represented faithfully. A successful calculation is one whose geometry, units, and chosen body can be explained to a colleague before the numerical result is shown. That discipline becomes more important as an assembly contains more components.

Use the load path to decide which member or connection should be isolated. In an ideal truss, member action follows its axis; in a multi-force frame, shear and bending may be present. A method that solves reactions is not automatically a method for checking buckling or joint strength.

## Deriving an appropriate model

A stiff-looking truss may contain a slender compression member whose buckling strength is low. Use a cut at a joint or along a member to inspect which action crosses the boundary.

## Worked engineering illustration

**Context:** Hand-operated press.

**Known information and task:** Input lever arm 0.6 m and output arm 0.08 m; ideal input 150 N.

**Equation:** `F_out=150×0.6/0.08`.

**Reference outcome:** **1125 N ideal output**.

**Engineering interpretation:** The ideal force is a preliminary estimate, not the permitted press load. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Applying work-based mechanical advantage without considering losses and linkage geometry.

A joint-force answer should satisfy both the local equilibrium equations and the whole-system reaction balance. At a truss joint with two unknown axial forces, two independent planar force equations can suffice. At a multi-force frame member, do not impose axial-only behavior. Reactions for the whole assembly should be solved before transferring them to a section when practical.

## Guided questions with answer criteria

**Q1 · Representation.** For hand-operated press, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `F_out=150×0.6/0.08`.

**Q2 · Computation and trend.** Reproduce the calculation **input lever arm 0.6 m and output arm 0.08 m; ideal input 150 n**, comparing with **1125 N ideal output**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `F_out=150×0.6/0.08` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for hand-operated press but appears to be applying work-based mechanical advantage without considering losses and linkage geometry. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

# Unit 3 · Lesson 5 — Internal force and load paths

**Unit objective:** Determine axial forces in trusses, reactions in frames, and action transmission in mechanical assemblies.

## Why this concept matters

External equilibrium is only the beginning of structural analysis: a cut can expose axial force, transverse shear, and bending moment carried by an individual section. The sign convention must accompany each result. Under ideal pin-jointed truss assumptions bending disappears in members, but actual welded or eccentric joints develop secondary bending. Track the applied load through members and supports; an unexplained stop in the load path often signals an omitted interaction.

Engineers often approach this subject in two directions: from a physical drawing to an equation, and from a computed answer back to a plausible physical action. Both directions matter. An unexplained number can be correct by coincidence, whereas a reproducible model can be corrected when assumptions change.

Use the load path to decide which member or connection should be isolated. In an ideal truss, member action follows its axis; in a multi-force frame, shear and bending may be present. A method that solves reactions is not automatically a method for checking buckling or joint strength.

## Deriving an appropriate model

A stiff-looking truss may contain a slender compression member whose buckling strength is low. Use a cut at a joint or along a member to inspect which action crosses the boundary.

## Worked engineering illustration

**Context:** Cantilevered equipment shelf.

**Known information and task:** Concentrated load 250 N at cantilever tip 0.5 m.

**Equation:** `M_root=250×0.5`.

**Reference outcome:** **125 N·m root moment**.

**Engineering interpretation:** An internal load path is necessary for mechanical fatigue and strength assessment. This calculation is an educational baseline. If dimensions shift, forces oscillate, joints deform or contacts disengage, reconstruct the model rather than carrying the same result forward unchanged. The central transferable skill is explaining how the physical assumptions give rise to the equation.

## Common failure and independent check

**Failure to avoid:** Concluding that zero net support motion means zero internal bending.

A joint-force answer should satisfy both the local equilibrium equations and the whole-system reaction balance. At a truss joint with two unknown axial forces, two independent planar force equations can suffice. At a multi-force frame member, do not impose axial-only behavior. Reactions for the whole assembly should be solved before transferring them to a section when practical.

## Guided questions with answer criteria

**Q1 · Representation.** For cantilevered equipment shelf, produce a free-body diagram or kinematic sketch with all force arrows, angles and relevant dimensions. Which objects are inside and outside your system boundary? Where would the representation fail if the connection were not ideal? Your response should contain enough information for another student to write the same equilibrium or motion equations.

**Answer criteria:** The boundary must be unambiguous; missing weight, reactions, or an applied couple should be identified when relevant. Direction arrows and a stated sign convention are mandatory. The explanatory text should identify the assumption most likely to fail in a real assembly. A drawing without dimensions or a boundary cannot fully justify `M_root=250×0.5`.

**Q2 · Computation and trend.** Reproduce the calculation **concentrated load 250 n at cantilever tip 0.5 m**, comparing with **125 N·m root moment**. Then change one meaningful input by 10% and predict whether the output should rise, fall or stay constant. Use the algebraic structure of `M_root=250×0.5` to explain the prediction, and calculate a revised value wherever the required numerical data are available.

**Answer criteria:** Show the original relationship before substitution. The baseline result should agree with the reference within sensible rounding. Do not assume every response is linear in the changed input: angular, quadratic and exponential effects may produce different relative changes. State whether geometry or the selected body boundary has changed along with the input; if so, the original equation may no longer be valid.

**Q3 · Fault diagnosis.** A peer supplies an answer for cantilevered equipment shelf but appears to be concluding that zero net support motion means zero internal bending. Explain what independent calculation or observation would reveal the problem. Would a negative sign necessarily prove that their calculation was wrong? Give a physically grounded explanation rather than a generic instruction to repeat the arithmetic.

**Answer criteria:** Name the suspected wrong assumption, the observation or alternate balance that could test it, and the role of direction conventions. Negative vector components may be physically valid; negative reactions in contacts that only push can invalidate the assumed contact state. The correct conclusion depends on the physical action being modeled, not simply whether the printed number is negative.



---

