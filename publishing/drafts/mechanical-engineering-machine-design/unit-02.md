# Unit 02: Shafts, Fits and Torque Transmission

**Course Code**: MDS 202 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Shafts, Fits and Torque Transmission**.

# Unit 2 · Lesson 1: Torsional shear in solid shafts

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A mixer shaft transmits 180 N*m in a defined constant-speed operating
case. The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and
plan a test that could show the calculation to be wrong. After this lesson, you should be able to explain the
chosen physical model in words; state the controlling variables and units; evaluate one illustrative example;
and describe a failure mechanism that the equation alone does not capture. The scope is a learning design
review, not a released production drawing.
## Physical reasoning and load path

Pure torque produces shear stress that increases linearly with radius and reaches a maximum at the outside
surface of a circular shaft. In practical machine design this idea interacts with the other topics in shafts,
fits and torque transmission. Begin with the object whose motion, load or temperature needs to be predicted.
Isolate that object from its neighbors and list the contacts, applied loads and supports. If a force is
transmitted through a bearing, fastener or contact patch, record what is assumed about that interface. A model
that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI
units, not only a short equation.


The working situation here is a synthetic example: A mixer shaft transmits 180 N*m in a defined constant-speed
operating case. First identify the intended load path. Next distinguish quantities that can be directly measured
from quantities inferred from a simplified equation. Finally ask which part of the assembly would change the
result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically
relevant uncertainty belongs at the specific interface where its cause arises. Apply force equilibrium to obtain
reactions before local stress calculations.
## Mathematical model, units and limits

One introductory relationship is **tau_max = 16*T/(pi*d^3)**. Interpret each symbol before using numbers and
confirm that both sides have compatible dimensions. The equation describes only a limited idealization. It
cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field, production tolerance
or failure probability. When the design is sensitive to parameters that do not appear in the expression, extend
the model or supplement it with measurement. All numerical values below are invented for teaching and should not
be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate nominal torsional shaft stress using T=180 N m, diameter=0.032 m. Using the explicit
relationship for this simplified case, the arithmetic is `16*180/(pi*0.032**3)/1e6`. The computed result is
**27.98 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design
capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that calculating with diameter in millimetres while
using N*m without conversion creates a billion-fold scale error. A responsible notebook records both the
numerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with
80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain
what happens to the corresponding margin.
## Design alternatives and trade-offs

A hollow shaft may improve stiffness-to-mass but introduces wall and manufacturing limits. This is not
automatically a superior choice: changes in stiffness, manufacturing route and interfaces can produce secondary
effects. A feasible comparison considers available space, mass, local machining, inspectability, life-cycle
cost, and how a failed part can be replaced. The optimal geometry for nominal stress is rarely also the optimum
for assembly, stiffness and maintenance. Write at least two concepts and name the requirement that would make
you prefer one over the other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Confirm torque by calibrated motor current or inline torque sensor and inspect fillets. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Check torsion, bending and deflection at geometric transitions. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Calculating with diameter in millimetres while using N*m without
conversion creates a billion-fold scale error.** Another common error is to stop as soon as a hand calculation
passes a nominal allowable. Real machinery experiences transient load combinations, operator changes,
contamination and gradual loosening. A preliminary analysis needs a hazard review: identify an initiating event,
a progression mechanism, a consequence, a way to detect the developing problem and a mitigation independent of
the calculation. If the failure could injure a person, preserve layers of protection such as guarding,
interlocks and independent inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A mixer shaft transmits 180 N*m in a defined constant-speed operating case.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **tau_max = 16*T/(pi*d^3)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **27.98 MPa** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Calculating with diameter in millimetres while using N*m without conversion creates a billion-fold scale error.” could occur. Propose one design modification based on “A hollow shaft may improve stiffness-to-mass but introduces wall and manufacturing limits.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Torsional shear in solid shafts — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 2 · Lesson 2: Combined shaft bending and torsion

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A helical gear shaft supports a transverse mesh load beside an outboard
bearing. The objective is to develop a defendable preliminary calculation, identify its governing assumptions,
and plan a test that could show the calculation to be wrong. After this lesson, you should be able to explain
the chosen physical model in words; state the controlling variables and units; evaluate one illustrative
example; and describe a failure mechanism that the equation alone does not capture. The scope is a learning
design review, not a released production drawing.
## Physical reasoning and load path

A shaft carrying a gear transmits torque while gear forces and gravity introduce bending; nominal stresses can
be combined using distortion-energy theory. In practical machine design this idea interacts with the other
topics in shafts, fits and torque transmission. Begin with the object whose motion, load or temperature needs to
be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports. If a
force is transmitted through a bearing, fastener or contact patch, record what is assumed about that interface.
A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions
in SI units, not only a short equation.


The working situation here is a synthetic example: A helical gear shaft supports a transverse mesh load beside
an outboard bearing. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Check torsion, bending
and deflection at geometric transitions.
## Mathematical model, units and limits

One introductory relationship is **sigma_vm = sqrt((32*M/(pi*d^3))^2 + 3*(16*T/(pi*d^3))^2)**. Interpret each
symbol before using numbers and confirm that both sides have compatible dimensions. The equation describes only
a limited idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal
field, production tolerance or failure probability. When the design is sensitive to parameters that do not
appear in the expression, extend the model or supplement it with measurement. All numerical values below are
invented for teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate shaft combined von Mises stress using M=110 N m, T=180 N m, d=0.04 m. Using the explicit
relationship for this simplified case, the arithmetic is
`sqrt((32*110/(pi*0.04**3))**2+3*(16*180/(pi*0.04**3))**2)/1e6`. The computed result is **30.36 MPa**. This is a
synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an
independent calculator before passing it into a later sizing step. A result outside a plausible physical range
is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that applying pure-torsion sizing to a bent shaft
underestimates equivalent stress. A responsible notebook records both the numerical output and the reason why
the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check
whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding
margin.
## Design alternatives and trade-offs

Reposition gears or add bearing support before adding shaft mass. This is not automatically a superior choice:
changes in stiffness, manufacturing route and interfaces can produce secondary effects. A feasible comparison
considers available space, mass, local machining, inspectability, life-cycle cost, and how a failed part can be
replaced. The optimal geometry for nominal stress is rarely also the optimum for assembly, stiffness and
maintenance. Write at least two concepts and name the requirement that would make you prefer one over the other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Check bending-moment diagrams at shoulders, retaining grooves and keyways. A good verification plan specifies
the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed.
Record both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate
its boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Do not treat a hub or coupling as a featureless boundary condition. Do not interpolate beyond
the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Applying pure-torsion sizing to a bent shaft underestimates equivalent
stress.** Another common error is to stop as soon as a hand calculation passes a nominal allowable. Real
machinery experiences transient load combinations, operator changes, contamination and gradual loosening. A
preliminary analysis needs a hazard review: identify an initiating event, a progression mechanism, a
consequence, a way to detect the developing problem and a mitigation independent of the calculation. If the
failure could injure a person, preserve layers of protection such as guarding, interlocks and independent
inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A helical gear shaft supports a transverse mesh load beside an outboard bearing.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **sigma_vm = sqrt((32*M/(pi*d^3))^2 + 3*(16*T/(pi*d^3))^2)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **30.36 MPa** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Applying pure-torsion sizing to a bent shaft underestimates equivalent stress.” could occur. Propose one design modification based on “Reposition gears or add bearing support before adding shaft mass.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Combined shaft bending and torsion — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 2 · Lesson 3: Deflection and rotor alignment

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A long rotor shaft supports a concentrated center load between two
bearings. The objective is to develop a defendable preliminary calculation, identify its governing assumptions,
and plan a test that could show the calculation to be wrong. After this lesson, you should be able to explain
the chosen physical model in words; state the controlling variables and units; evaluate one illustrative
example; and describe a failure mechanism that the equation alone does not capture. The scope is a learning
design review, not a released production drawing.
## Physical reasoning and load path

Shaft stiffness affects gear meshing, coupling alignment, seal contact and critical speeds; passing a yield
check does not establish functional performance. In practical machine design this idea interacts with the other
topics in shafts, fits and torque transmission. Begin with the object whose motion, load or temperature needs to
be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports. If a
force is transmitted through a bearing, fastener or contact patch, record what is assumed about that interface.
A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions
in SI units, not only a short equation.


The working situation here is a synthetic example: A long rotor shaft supports a concentrated center load
between two bearings. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Do not treat a hub or
coupling as a featureless boundary condition.
## Mathematical model, units and limits

One introductory relationship is **simply supported midpoint deflection = F*L^3/(48*E*I)**. Interpret each
symbol before using numbers and confirm that both sides have compatible dimensions. The equation describes only
a limited idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal
field, production tolerance or failure probability. When the design is sensitive to parameters that do not
appear in the expression, extend the model or supplement it with measurement. All numerical values below are
invented for teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate beam deflection screen using F=500 N, L=0.4 m, E=210 GPa, d=0.025 m. Using the explicit
relationship for this simplified case, the arithmetic is `500*0.4**3/(48*210e9*(pi*0.025**4/64))*1e3`. The
computed result is **0.1656 mm**. This is a synthetic, rounded result; it is not a measured or independently
certified design capacity. Recalculate with an independent calculator before passing it into a later sizing
step. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not
automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that ignoring bearing compliance and concentrated loads
gives falsely small predicted deflection. A responsible notebook records both the numerical output and the
reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base
value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Reduce span or redistribute loads instead of increasing diameter alone. This is not automatically a superior
choice: changes in stiffness, manufacturing route and interfaces can produce secondary effects. A feasible
comparison considers available space, mass, local machining, inspectability, life-cycle cost, and how a failed
part can be replaced. The optimal geometry for nominal stress is rarely also the optimum for assembly, stiffness
and maintenance. Write at least two concepts and name the requirement that would make you prefer one over the
other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Measure shaft runout and bearing seat concentricity after installation. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Include manufacturing steps and alignment tolerances in the design plan. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Ignoring bearing compliance and concentrated loads gives falsely small
predicted deflection.** Another common error is to stop as soon as a hand calculation passes a nominal
allowable. Real machinery experiences transient load combinations, operator changes, contamination and gradual
loosening. A preliminary analysis needs a hazard review: identify an initiating event, a progression mechanism,
a consequence, a way to detect the developing problem and a mitigation independent of the calculation. If the
failure could injure a person, preserve layers of protection such as guarding, interlocks and independent
inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A long rotor shaft supports a concentrated center load between two bearings.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **simply supported midpoint deflection = F*L^3/(48*E*I)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.1656 mm** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Ignoring bearing compliance and concentrated loads gives falsely small predicted deflection.” could occur. Propose one design modification based on “Reduce span or redistribute loads instead of increasing diameter alone.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Deflection and rotor alignment — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 2 · Lesson 4: Keys, splines and interference fits

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A drive hub is assembled with a rectangular key and removable retainer.
The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

A key transfers tangential force over finite shear and bearing areas; splines distribute torque across multiple
teeth and interference fits rely on contact pressure. In practical machine design this idea interacts with the
other topics in shafts, fits and torque transmission. Begin with the object whose motion, load or temperature
needs to be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports.
If a force is transmitted through a bearing, fastener or contact patch, record what is assumed about that
interface. A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with
dimensions in SI units, not only a short equation.


The working situation here is a synthetic example: A drive hub is assembled with a rectangular key and removable
retainer. First identify the intended load path. Next distinguish quantities that can be directly measured from
quantities inferred from a simplified equation. Finally ask which part of the assembly would change the result
if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically relevant
uncertainty belongs at the specific interface where its cause arises. Include manufacturing steps and alignment
tolerances in the design plan.
## Mathematical model, units and limits

One introductory relationship is **key shear = 2*T/(d*b*L)**. Interpret each symbol before using numbers and
confirm that both sides have compatible dimensions. The equation describes only a limited idealization. It
cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field, production tolerance
or failure probability. When the design is sensitive to parameters that do not appear in the expression, extend
the model or supplement it with measurement. All numerical values below are invented for teaching and should not
be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate parallel key nominal shear using T=120 N m, d=0.03 m, b=0.008 m, L=0.045 m. Using the
explicit relationship for this simplified case, the arithmetic is `2*120/(0.03*0.008*0.045)/1e6`. The computed
result is **22.22 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified
design capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that using key length without accounting for the actual
loaded contact length exaggerates capacity. A responsible notebook records both the numerical output and the
reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base
value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Use a shrink fit or clamp hub where backlash and fretting dominate. This is not automatically a superior choice:
changes in stiffness, manufacturing route and interfaces can produce secondary effects. A feasible comparison
considers available space, mass, local machining, inspectability, life-cycle cost, and how a failed part can be
replaced. The optimal geometry for nominal stress is rarely also the optimum for assembly, stiffness and
maintenance. Write at least two concepts and name the requirement that would make you prefer one over the other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Inspect fit, contact marks, fretting debris and assembly retention. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Apply force equilibrium to obtain reactions before local stress calculations. Do not
interpolate beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Using key length without accounting for the actual loaded contact length
exaggerates capacity.** Another common error is to stop as soon as a hand calculation passes a nominal
allowable. Real machinery experiences transient load combinations, operator changes, contamination and gradual
loosening. A preliminary analysis needs a hazard review: identify an initiating event, a progression mechanism,
a consequence, a way to detect the developing problem and a mitigation independent of the calculation. If the
failure could injure a person, preserve layers of protection such as guarding, interlocks and independent
inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A drive hub is assembled with a rectangular key and removable retainer.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **key shear = 2*T/(d*b*L)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **22.22 MPa** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Using key length without accounting for the actual loaded contact length exaggerates capacity.” could occur. Propose one design modification based on “Use a shrink fit or clamp hub where backlash and fretting dominate.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Keys, splines and interference fits — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 2 · Lesson 5: Couplings and misalignment

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: Two separately mounted motors and reducers shift relative to one another
during heating. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

Rigid and flexible couplings transmit torque but cannot magically eliminate angular, axial or lateral
misalignment forces. In practical machine design this idea interacts with the other topics in shafts, fits and
torque transmission. Begin with the object whose motion, load or temperature needs to be predicted. Isolate that
object from its neighbors and list the contacts, applied loads and supports. If a force is transmitted through a
bearing, fastener or contact patch, record what is assumed about that interface. A model that changes its
boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only a
short equation.


The working situation here is a synthetic example: Two separately mounted motors and reducers shift relative to
one another during heating. First identify the intended load path. Next distinguish quantities that can be
directly measured from quantities inferred from a simplified equation. Finally ask which part of the assembly
would change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise:
the physically relevant uncertainty belongs at the specific interface where its cause arises. Apply force
equilibrium to obtain reactions before local stress calculations.
## Mathematical model, units and limits

One introductory relationship is **coupling power = T*omega**. Interpret each symbol before using numbers and
confirm that both sides have compatible dimensions. The equation describes only a limited idealization. It
cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field, production tolerance
or failure probability. When the design is sensitive to parameters that do not appear in the expression, extend
the model or supplement it with measurement. All numerical values below are invented for teaching and should not
be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate coupling transmitted power using torque=110 N m, speed=900 rpm. Using the explicit
relationship for this simplified case, the arithmetic is `110*(900*2*pi/60)/1000`. The computed result is
**10.37 kW**. This is a synthetic, rounded result; it is not a measured or independently certified design
capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that choosing a flexible coupling solely from torque
rating overlooks shaft reactions and speed limits. A responsible notebook records both the numerical output and
the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Use a spacer coupling where maintenance access and separation are important. This is not automatically a
superior choice: changes in stiffness, manufacturing route and interfaces can produce secondary effects. A
feasible comparison considers available space, mass, local machining, inspectability, life-cycle cost, and how a
failed part can be replaced. The optimal geometry for nominal stress is rarely also the optimum for assembly,
stiffness and maintenance. Write at least two concepts and name the requirement that would make you prefer one
over the other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Laser-align shafts and record operating-temperature alignment change. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Check torsion, bending and deflection at geometric transitions. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Choosing a flexible coupling solely from torque rating overlooks shaft
reactions and speed limits.** Another common error is to stop as soon as a hand calculation passes a nominal
allowable. Real machinery experiences transient load combinations, operator changes, contamination and gradual
loosening. A preliminary analysis needs a hazard review: identify an initiating event, a progression mechanism,
a consequence, a way to detect the developing problem and a mitigation independent of the calculation. If the
failure could injure a person, preserve layers of protection such as guarding, interlocks and independent
inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “Two separately mounted motors and reducers shift relative to one another during heating.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **coupling power = T*omega**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **10.37 kW** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Choosing a flexible coupling solely from torque rating overlooks shaft reactions and speed limits.” could occur. Propose one design modification based on “Use a spacer coupling where maintenance access and separation are important.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Couplings and misalignment — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

