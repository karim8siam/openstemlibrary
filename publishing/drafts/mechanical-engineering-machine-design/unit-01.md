# Unit 01: Design Requirements, Load Paths and Failure Criteria

**Course Code**: MDS 201 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Design Requirements, Load Paths and Failure Criteria**.

# Unit 1 · Lesson 1: Requirements and acceptance criteria

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A packaging conveyor must operate across startup, steady motion and jam
release; each mode gives different design load. The objective is to develop a defendable preliminary
calculation, identify its governing assumptions, and plan a test that could show the calculation to be wrong.
After this lesson, you should be able to explain the chosen physical model in words; state the controlling
variables and units; evaluate one illustrative example; and describe a failure mechanism that the equation alone
does not capture. The scope is a learning design review, not a released production drawing.
## Physical reasoning and load path

Convert customer function into measurable peak torque, duty duration, speed, allowable displacement, reliability
target and service environment; ambiguous words like robust or quiet are not acceptance criteria. In practical
machine design this idea interacts with the other topics in design requirements, load paths and failure
criteria. Begin with the object whose motion, load or temperature needs to be predicted. Isolate that object
from its neighbors and list the contacts, applied loads and supports. If a force is transmitted through a
bearing, fastener or contact patch, record what is assumed about that interface. A model that changes its
boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only a
short equation.


The working situation here is a synthetic example: A packaging conveyor must operate across startup, steady
motion and jam release; each mode gives different design load. First identify the intended load path. Next
distinguish quantities that can be directly measured from quantities inferred from a simplified equation.
Finally ask which part of the assembly would change the result if it were flexible, worn or misaligned. This is
not a generic safety-factor exercise: the physically relevant uncertainty belongs at the specific interface
where its cause arises. Write functional requirements with a unit and numerical acceptance threshold.
## Mathematical model, units and limits

One introductory relationship is **utilization = predicted demand / allowable demand**. Interpret each symbol
before using numbers and confirm that both sides have compatible dimensions. The equation describes only a
limited idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal
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

**Question:** Calculate requirements capacity screening using demand=6.6 kN, allowable=10 kN. Using the explicit
relationship for this simplified case, the arithmetic is `6.6/10`. The computed result is **0.66
dimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design
capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that treating the customer's nominal power rating as
the maximum possible shaft load conceals transients. A responsible notebook records both the numerical output
and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Separate mandatory constraints from preferences, and do not invent a safety factor before loads are known. This
is not automatically a superior choice: changes in stiffness, manufacturing route and interfaces can produce
secondary effects. A feasible comparison considers available space, mass, local machining, inspectability, life-
cycle cost, and how a failed part can be replaced. The optimal geometry for nominal stress is rarely also the
optimum for assembly, stiffness and maintenance. Write at least two concepts and name the requirement that would
make you prefer one over the other.


For a component subjected to the conditions described above, first ask whether the load can be reduced at its
source. Then ask whether its point of application can be moved to change the load path. Only then consider
increasing section size or material grade. For example, a stronger alloy may raise a static strength margin
without changing shaft deflection materially, because its elastic modulus is similar to that of other common
steels. This distinction between material strength and geometry-driven rigidity prevents a frequent early-design
error.
## Verification plan and sensitivity audit

Interview operators; document cycles and test the worst credible operating state. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Separate normal operating loads from foreseeable abnormal and misuse loads. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Treating the customer's nominal power rating as the maximum possible shaft
load conceals transients.** Another common error is to stop as soon as a hand calculation passes a nominal
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

1. **Model reconstruction:** For the situation “A packaging conveyor must operate across startup, steady motion and jam release; each mode gives different design load.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **utilization = predicted demand / allowable demand**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.66 dimensionless** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Treating the customer's nominal power rating as the maximum possible shaft load conceals transients.” could occur. Propose one design modification based on “Separate mandatory constraints from preferences, and do not invent a safety factor before loads are known.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Requirements and acceptance criteria — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 1 · Lesson 2: Load spectra and free-body diagrams

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: An overhung pulley creates a bending moment even when torque is perfectly
steady. The objective is to develop a defendable preliminary calculation, identify its governing assumptions,
and plan a test that could show the calculation to be wrong. After this lesson, you should be able to explain
the chosen physical model in words; state the controlling variables and units; evaluate one illustrative
example; and describe a failure mechanism that the equation alone does not capture. The scope is a learning
design review, not a released production drawing.
## Physical reasoning and load path

Identify static forces, inertial effects, self-weight, shock and thermal growth; trace each applied action
through bearings, hubs and fasteners to ground. In practical machine design this idea interacts with the other
topics in design requirements, load paths and failure criteria. Begin with the object whose motion, load or
temperature needs to be predicted. Isolate that object from its neighbors and list the contacts, applied loads
and supports. If a force is transmitted through a bearing, fastener or contact patch, record what is assumed
about that interface. A model that changes its boundary conditions silently cannot be verified. Use a labelled
sketch with dimensions in SI units, not only a short equation.


The working situation here is a synthetic example: An overhung pulley creates a bending moment even when torque
is perfectly steady. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Separate normal
operating loads from foreseeable abnormal and misuse loads.
## Mathematical model, units and limits

One introductory relationship is **equivalent moment = sqrt(Mx^2 + My^2)**. Interpret each symbol before using
numbers and confirm that both sides have compatible dimensions. The equation describes only a limited
idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field,
production tolerance or failure probability. When the design is sensitive to parameters that do not appear in
the expression, extend the model or supplement it with measurement. All numerical values below are invented for
teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate support bending from pulley force using F=850 N, overhang=0.12 m. Using the explicit
relationship for this simplified case, the arithmetic is `850*0.12`. The computed result is **102 N m**. This is
a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with
an independent calculator before passing it into a later sizing step. A result outside a plausible physical
range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that omitting the belt radial reaction when sizing the
input bearing makes an apparently adequate assembly unreliable. A responsible notebook records both the
numerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with
80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain
what happens to the corresponding margin.
## Design alternatives and trade-offs

Move the pulley toward its bearing to reduce moment rather than simply increasing material. This is not
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

Draw a free-body diagram for every component and reconcile reaction sums. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Account for environmental degradation and dimensional uncertainties. Do not interpolate beyond
the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Omitting the belt radial reaction when sizing the input bearing makes an
apparently adequate assembly unreliable.** Another common error is to stop as soon as a hand calculation passes
a nominal allowable. Real machinery experiences transient load combinations, operator changes, contamination and
gradual loosening. A preliminary analysis needs a hazard review: identify an initiating event, a progression
mechanism, a consequence, a way to detect the developing problem and a mitigation independent of the
calculation. If the failure could injure a person, preserve layers of protection such as guarding, interlocks
and independent inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “An overhung pulley creates a bending moment even when torque is perfectly steady.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **equivalent moment = sqrt(Mx^2 + My^2)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **102 N m** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Omitting the belt radial reaction when sizing the input bearing makes an apparently adequate assembly unreliable.” could occur. Propose one design modification based on “Move the pulley toward its bearing to reduce moment rather than simply increasing material.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Load spectra and free-body diagrams — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 1 · Lesson 3: Equivalent stress and ductile yielding

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A drive pin carries both axial assembly load and transverse drive shear.
The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

Distortion-energy theory combines normal and shear stresses in a ductile, approximately isotropic material under
elastic loading. In practical machine design this idea interacts with the other topics in design requirements,
load paths and failure criteria. Begin with the object whose motion, load or temperature needs to be predicted.
Isolate that object from its neighbors and list the contacts, applied loads and supports. If a force is
transmitted through a bearing, fastener or contact patch, record what is assumed about that interface. A model
that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI
units, not only a short equation.


The working situation here is a synthetic example: A drive pin carries both axial assembly load and transverse
drive shear. First identify the intended load path. Next distinguish quantities that can be directly measured
from quantities inferred from a simplified equation. Finally ask which part of the assembly would change the
result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically
relevant uncertainty belongs at the specific interface where its cause arises. Account for environmental
degradation and dimensional uncertainties.
## Mathematical model, units and limits

One introductory relationship is **von Mises stress = sqrt(sigma^2 + 3*tau^2)**. Interpret each symbol before
using numbers and confirm that both sides have compatible dimensions. The equation describes only a limited
idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field,
production tolerance or failure probability. When the design is sensitive to parameters that do not appear in
the expression, extend the model or supplement it with measurement. All numerical values below are invented for
teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate combined nominal elastic stress using normal=110 MPa, shear=40 MPa. Using the explicit
relationship for this simplified case, the arithmetic is `sqrt(110**2+3*40**2)`. The computed result is **130
MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.
Recalculate with an independent calculator before passing it into a later sizing step. A result outside a
plausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that combining stresses with arithmetic addition
instead of a justified failure criterion distorts utilization. A responsible notebook records both the numerical
output and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%
of its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens
to the corresponding margin.
## Design alternatives and trade-offs

Compare a larger diameter with a different heat treatment or reduced applied load. This is not automatically a
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

Check measured yield properties, residual stress and multiaxial load directions. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Retain the underlying evidence and decision maker for each assumption. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Combining stresses with arithmetic addition instead of a justified failure
criterion distorts utilization.** Another common error is to stop as soon as a hand calculation passes a nominal
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

1. **Model reconstruction:** For the situation “A drive pin carries both axial assembly load and transverse drive shear.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **von Mises stress = sqrt(sigma^2 + 3*tau^2)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **130 MPa** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Combining stresses with arithmetic addition instead of a justified failure criterion distorts utilization.” could occur. Propose one design modification based on “Compare a larger diameter with a different heat treatment or reduced applied load.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Equivalent stress and ductile yielding — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 1 · Lesson 4: Brittle failure and crack sensitivity

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A cast support bracket has a small surface flaw near a sharp transition.
The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

Brittle or low-toughness materials can fracture with small plastic deformation; maximum principal stress alone
does not resolve the effect of existing cracks. In practical machine design this idea interacts with the other
topics in design requirements, load paths and failure criteria. Begin with the object whose motion, load or
temperature needs to be predicted. Isolate that object from its neighbors and list the contacts, applied loads
and supports. If a force is transmitted through a bearing, fastener or contact patch, record what is assumed
about that interface. A model that changes its boundary conditions silently cannot be verified. Use a labelled
sketch with dimensions in SI units, not only a short equation.


The working situation here is a synthetic example: A cast support bracket has a small surface flaw near a sharp
transition. First identify the intended load path. Next distinguish quantities that can be directly measured
from quantities inferred from a simplified equation. Finally ask which part of the assembly would change the
result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically
relevant uncertainty belongs at the specific interface where its cause arises. Retain the underlying evidence
and decision maker for each assumption.
## Mathematical model, units and limits

One introductory relationship is **stress intensity KI = Y*sigma*sqrt(pi*a)**. Interpret each symbol before
using numbers and confirm that both sides have compatible dimensions. The equation describes only a limited
idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field,
production tolerance or failure probability. When the design is sensitive to parameters that do not appear in
the expression, extend the model or supplement it with measurement. All numerical values below are invented for
teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate surface-crack intensity screen using Y=1.12, sigma=95 MPa, a=0.002 m. Using the explicit
relationship for this simplified case, the arithmetic is `1.12*95*sqrt(pi*0.002)`. The computed result is
**8.434 MPa sqrt(m)**. This is a synthetic, rounded result; it is not a measured or independently certified
design capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that substituting yield strength for fracture toughness
ignores crack propagation and temperature dependence. A responsible notebook records both the numerical output
and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Reduce peak stress and remove sharp geometry; choose a more damage-tolerant material. This is not automatically
a superior choice: changes in stiffness, manufacturing route and interfaces can produce secondary effects. A
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

Require inspected flaw bounds and relevant fracture-toughness data before accepting flaw tolerance. A good
verification plan specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the
result will be analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the
simple model, investigate its boundary conditions and material state before changing the spreadsheet constants.
When test data do not yet exist, label the numerical model as an unvalidated hypothesis and specify the
measurement that would have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Write functional requirements with a unit and numerical acceptance threshold. Do not
interpolate beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Substituting yield strength for fracture toughness ignores crack
propagation and temperature dependence.** Another common error is to stop as soon as a hand calculation passes a
nominal allowable. Real machinery experiences transient load combinations, operator changes, contamination and
gradual loosening. A preliminary analysis needs a hazard review: identify an initiating event, a progression
mechanism, a consequence, a way to detect the developing problem and a mitigation independent of the
calculation. If the failure could injure a person, preserve layers of protection such as guarding, interlocks
and independent inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A cast support bracket has a small surface flaw near a sharp transition.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **stress intensity KI = Y*sigma*sqrt(pi*a)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **8.434 MPa sqrt(m)** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Substituting yield strength for fracture toughness ignores crack propagation and temperature dependence.” could occur. Propose one design modification based on “Reduce peak stress and remove sharp geometry; choose a more damage-tolerant material.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Brittle failure and crack sensitivity — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 1 · Lesson 5: Design uncertainty and reliability

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: Two suppliers quote the same nominal strength but different production
variability. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

Material scatter, dimensional tolerance, uncertain loads and model idealization should be kept distinct instead
of hidden in a single oversized factor. In practical machine design this idea interacts with the other topics in
design requirements, load paths and failure criteria. Begin with the object whose motion, load or temperature
needs to be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports.
If a force is transmitted through a bearing, fastener or contact patch, record what is assumed about that
interface. A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with
dimensions in SI units, not only a short equation.


The working situation here is a synthetic example: Two suppliers quote the same nominal strength but different
production variability. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Write functional
requirements with a unit and numerical acceptance threshold.
## Mathematical model, units and limits

One introductory relationship is **margin = allowable / predicted response**. Interpret each symbol before using
numbers and confirm that both sides have compatible dimensions. The equation describes only a limited
idealization. It cannot on its own provide a complete stress concentration, fatigue spectrum, thermal field,
production tolerance or failure probability. When the design is sensitive to parameters that do not appear in
the expression, extend the model or supplement it with measurement. All numerical values below are invented for
teaching and should not be used as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate uncertainty margin using allowable=145 MPa, prediction=93 MPa. Using the explicit
relationship for this simplified case, the arithmetic is `145/93`. The computed result is **1.559
dimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design
capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that reporting five decimal places in an estimated
endurance limit falsely implies precision. A responsible notebook records both the numerical output and the
reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base
value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Design for inspectability and replaceable parts when uncertainty cannot be eliminated. This is not automatically
a superior choice: changes in stiffness, manufacturing route and interfaces can produce secondary effects. A
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

Build a measured-data plan and a sensitivity table for load, diameter and strength. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Separate normal operating loads from foreseeable abnormal and misuse loads. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Reporting five decimal places in an estimated endurance limit falsely
implies precision.** Another common error is to stop as soon as a hand calculation passes a nominal allowable.
Real machinery experiences transient load combinations, operator changes, contamination and gradual loosening. A
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

1. **Model reconstruction:** For the situation “Two suppliers quote the same nominal strength but different production variability.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **margin = allowable / predicted response**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **1.559 dimensionless** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Reporting five decimal places in an estimated endurance limit falsely implies precision.” could occur. Propose one design modification based on “Design for inspectability and replaceable parts when uncertainty cannot be eliminated.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Design uncertainty and reliability — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

