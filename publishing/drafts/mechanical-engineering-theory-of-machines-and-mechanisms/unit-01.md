# Unit 01: Mechanisms, Topology and Mobility

**Course Code**: TMM 201 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Mechanisms, Topology and Mobility**.

# U01-L01 — Kinematic pairs and degrees of freedom

**Unit 1: Mechanisms, Topology and Mobility · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** What prevents a nominally moving linkage from having an unwanted degree of freedom?

**Scenario:** A hinge cover contains five moving members connected by pin joints, with the machine base counted as the frame. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `DOF = 3(N−1)−2J1−J2 for a planar assembly with independent constraints`.

The mobility calculation is a first topology filter, not a substitute for a closure Jacobian or a physical assembly check. Start from a list of bodies rather than a list of manufactured components. Include the ground as a link and assign every joint a constraint type. For a general planar rigid body, three coordinates are available: two translations and one rotation. Revolute and prismatic constraints each remove two relative freedoms in the common idealized model. The mobility count works when constraints are independent. Close one loop by writing both horizontal and vertical position equations; the derivatives of these equations form the local Jacobian. A small determinant does not by itself prove the physical mechanism has a defect, but a loss of Jacobian rank can reveal a toggle, redundancy or branch ambiguity. This matters most near the intended operating boundary, where manufacturing tolerances have disproportionate influence.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** N=6 links including frame; J1=7 independent lower pairs; J2=0.

**Calculation — Planar mobility count:** **1 DOF**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Applying the planar count blindly when joints are redundant or overconstrained.

**Specific sensitivity investigation:** Keep the number of links but exchange a revolute joint for a prismatic joint. Check which relative motion is permitted and how that alters the reachable workspace. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Make a linkage from cardboard and map independent link motions before and after adding one pin. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** What prevents a nominally moving linkage from having an unwanted degree of freedom? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Kinematic pairs and degrees of freedom** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U01-L02 — Link classification and kinematic chains

**Unit 1: Mechanisms, Topology and Mobility · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** When is a component a separate link rather than part of the same rigid body?

**Scenario:** A welded bracket and bolted plate can move as one rigid link despite containing several manufactured parts. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `A link is a rigid body with a specified set of connections`.

Rigid link idealization suppresses small elastic deflections, clearance and manufacturing looseness; document why each can be neglected. Start from a list of bodies rather than a list of manufactured components. Include the ground as a link and assign every joint a constraint type. For a general planar rigid body, three coordinates are available: two translations and one rotation. Revolute and prismatic constraints each remove two relative freedoms in the common idealized model. The mobility count works when constraints are independent. Close one loop by writing both horizontal and vertical position equations; the derivatives of these equations form the local Jacobian. A small determinant does not by itself prove the physical mechanism has a defect, but a loss of Jacobian rank can reveal a toggle, redundancy or branch ambiguity. This matters most near the intended operating boundary, where manufacturing tolerances have disproportionate influence.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Three moving elements and one fixed frame; assume each fastened subpart moves as one link.

**Calculation — Rotating assembly effective link count:** **3 moving rigid bodies**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Treating every physical part number as a separate moving kinematic element.

**Specific sensitivity investigation:** Draw the same assembly with an alternate frame attachment. Explain why the apparent motion of every other link changes even if the physical joint graph does not. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Color connected bodies that share zero relative motion and redraw the simplified chain. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** When is a component a separate link rather than part of the same rigid body? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Link classification and kinematic chains** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U01-L03 — Lower and higher pairs

**Unit 1: Mechanisms, Topology and Mobility · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why does a cam contact require different constraint treatment from a pin joint?

**Scenario:** A roller follower maintains contact with a rotating cam profile but may separate when normal force becomes zero. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `For planar motion, a revolute or prismatic pair removes two relative DOF`.

The contact condition is unilateral; penetration is prevented but tension cannot be carried across an unbonded contact. Start from a list of bodies rather than a list of manufactured components. Include the ground as a link and assign every joint a constraint type. For a general planar rigid body, three coordinates are available: two translations and one rotation. Revolute and prismatic constraints each remove two relative freedoms in the common idealized model. The mobility count works when constraints are independent. Close one loop by writing both horizontal and vertical position equations; the derivatives of these equations form the local Jacobian. A small determinant does not by itself prove the physical mechanism has a defect, but a loss of Jacobian rank can reveal a toggle, redundancy or branch ambiguity. This matters most near the intended operating boundary, where manufacturing tolerances have disproportionate influence.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** One relative rotational freedom remains from three relative planar freedoms.

**Calculation — Revolute joint constraints:** **2 constraints**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming an intermittent higher pair always constrains the system exactly like a permanent pin.

**Specific sensitivity investigation:** Imagine the contact is no longer maintained during one part of the cycle. State which unilateral force condition is violated, and which degrees of freedom become temporarily available. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Observe roller–cam contact at several speeds and mark any loss of contact. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why does a cam contact require different constraint treatment from a pin joint? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Lower and higher pairs** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U01-L04 — Planar constraint graphs

**Unit 1: Mechanisms, Topology and Mobility · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** How can a graph show closed loops yet hide an overconstraint?

**Scenario:** Two intended parallel links are assembled with slightly mismatched hole spacing and bind during rotation. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `J(x)=∂f/∂x maps coordinate changes into constraint errors`.

Constraint rank, not link count alone, determines instantaneous independent motion at a particular configuration. Start from a list of bodies rather than a list of manufactured components. Include the ground as a link and assign every joint a constraint type. For a general planar rigid body, three coordinates are available: two translations and one rotation. Revolute and prismatic constraints each remove two relative freedoms in the common idealized model. The mobility count works when constraints are independent. Close one loop by writing both horizontal and vertical position equations; the derivatives of these equations form the local Jacobian. A small determinant does not by itself prove the physical mechanism has a defect, but a loss of Jacobian rank can reveal a toggle, redundancy or branch ambiguity. This matters most near the intended operating boundary, where manufacturing tolerances have disproportionate influence.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Residual components fx=0.0006 m and fy=−0.0008 m.

**Calculation — Loop closure residual norm:** **0.001 m**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Assuming topological connectivity guarantees geometric compatibility.

**Specific sensitivity investigation:** Introduce a duplicate constraint and show why simple scalar degree-of-freedom arithmetic may count it incorrectly. Compare the constraint Jacobian rank. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Sketch a link-joint incidence diagram and numerically inspect the closure residual near several input angles. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** How can a graph show closed loops yet hide an overconstraint? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Planar constraint graphs** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

# U01-L05 — Mobility singularities and assembly branches

**Unit 1: Mechanisms, Topology and Mobility · University-level learning draft · All examples synthetic**

## Engineering question and geometry

**Question:** Why does a seemingly simple linkage suddenly become hard to move near alignment?

**Scenario:** Three bar centers approach a straight line and the output response becomes highly sensitive to tolerances. Begin by drawing the machine in one reference configuration, identifying the ground, the input actuator and the intended output variable. Treat the device as a rigid planar assembly only if its geometry and operating conditions justify that approximation. Mark fixed points, moving joints, relevant dimensions, motion signs and any physical stop or contact condition. A computer animation is useful for communicating the proposed motion, but it cannot demonstrate that the physical parts have sufficient clearance or that the arrangement is safe.

## Principle, constraints and derivation

**Governing relation:** `det(J)=0 identifies certain square-Jacobian singularities`.

Near singularity, minor clearance can dominate the predicted configuration and reaction loads; an infinitesimal solution may become practically unusable. Start from a list of bodies rather than a list of manufactured components. Include the ground as a link and assign every joint a constraint type. For a general planar rigid body, three coordinates are available: two translations and one rotation. Revolute and prismatic constraints each remove two relative freedoms in the common idealized model. The mobility count works when constraints are independent. Close one loop by writing both horizontal and vertical position equations; the derivatives of these equations form the local Jacobian. A small determinant does not by itself prove the physical mechanism has a defect, but a loss of Jacobian rank can reveal a toggle, redundancy or branch ambiguity. This matters most near the intended operating boundary, where manufacturing tolerances have disproportionate influence.

Define each independent quantity and units before substitution. If a formula contains an angle derivative, convert degrees to radians and apply the chain rule to move from angle to time. For a constrained mechanism, first solve position closure and then differentiate to obtain velocity and acceleration. For a loaded mechanism, separate the purely kinematic result from required contact reactions and input torque. Identify when the formula assumes a fixed pivot, a constant input speed, a continuously engaged contact, or one assembly branch. A physically meaningful calculation states its domain, not just its output.

## Worked numerical case

**Illustrative inputs:** Output error 2 mm for a 0.5 mm link-length error near a sensitive configuration.

**Calculation — Local sensitivity estimate:** **4 dimensionless**. These values were chosen for teaching, not measured from machinery. Put each input and its unit on a separate line in a reproducible calculation sheet, then verify the arithmetic with an independent computation. The sign of a rotational quantity indicates orientation; it does not imply an error. When the output is a force, check the implied work and reaction path. When it is a geometric dimension, check the assembly envelope and the full intended motion cycle, not only the illustrated pose.

**Sanity test:** Vary one relevant parameter by 10% and classify the resulting trend as linear, inverse, quadratic or configuration-dependent. Consider a near-limit case and ask which assumption would fail first. The calculation cannot independently prove its own assumptions: a derived value must eventually be compared with a separate observation, compatible published reference or physically grounded second model.

## Engineering interpretation and counterexample

**Frequent mistake:** Crossing a toggle position without checking the available assembly branch.

**Specific sensitivity investigation:** Approach a toggle from both sides. Decide whether a continuously tracked branch is still available and predict how a small pin offset changes the reachable configuration. State what is held fixed, what changes and whether the output should be continuous. For closed-loop linkages, a second numerical solution may correspond to a different assembly branch; continuous angle tracking and a small closure residual are essential. For cams, belts, transmissions and vibration models, identify contact state, speed range and sources of energy dissipation. If a model produces exceptionally high speed or force near an ideal singularity, report the sensitivity and stop short of treating an unbounded prediction as achievable hardware performance.

A result matters when it can influence an engineering decision: mechanism selection, operating speed, joint configuration, allowable tolerance or actuator requirement. Always distinguish theoretical feasibility from reliability over many cycles. Geometry can be correct while friction, wear, fatigue, excessive contact stress or dynamic instability invalidates the design. A response that is numerically precise but sensitive to unmeasured clearances should be given as a qualified estimate rather than a certified value.

## Test and reproducibility plan

**Investigation:** Sweep a driver angle and plot the smallest Jacobian singular value near an alignment. Record the drawing and initial settings before running the test. An appropriate student exercise can use slow, guarded motion, video tracking, or a separate numerical implementation; an energized high-speed experiment needs professional safety controls. Document reference length, sampling interval, calibration method and expected uncertainty. Compare at least three configurations, including a near-boundary case if it can be studied safely. Keep synthetic values separated from measured observations, and do not count the same input data as independent validation.

The report should contain a labeled schematic, equations, raw input table, one calculated output and its units, a sensitivity result and a discrepancy explanation. If an observed path differs from the model, consider perspective error, misidentified joints, slippage, structural flexibility, bearing clearance and unintended motion. Decide which extra measurement would distinguish the most plausible causes. A useful verification plan explains not only what evidence would support a model but what evidence would require it to be revised.

## Exercises and assessment

1. **Numerical variation:** Recalculate the worked example after changing one driving parameter by 15%. State the new answer, its units and the percentage change. Identify any hidden domain restriction, such as a minimum rod length or positive stiffness.
2. **Mechanism reasoning:** Why does a seemingly simple linkage suddenly become hard to move near alignment? Contrast the original situation with a changed link, joint, contact condition or speed regime. Draw the new physical picture and explain which equation remains valid, requires modification or fails.
3. **Model critique:** Design an independent test for the proposed investigation, including measured variables, instrument calibration, repeatability, one confounding factor and a rejection criterion.

## Design review conclusion

**Mobility singularities and assembly branches** provides one part of a complete machine analysis. Deliver a brief calculation memo with an explicit operating range and at least one technical limitation. Evaluate the result against mechanism geometry and energy conservation, and list any unresolved requirements for guards, rated components, fatigue testing, maintenance or industrial standards before suggesting construction. A model is only one line of evidence; physical tests and responsible engineering judgment remain necessary.


---

