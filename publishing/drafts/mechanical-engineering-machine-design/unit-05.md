# Unit 05: Bearings, Tribology and Sealing

**Course Code**: MDS 205 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Bearings, Tribology and Sealing**.

# Unit 5 · Lesson 1: Bearing reaction loads

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A shaft spans two bearings and carries a centered belt radial load. The
objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

Bearing load is determined by free-body equilibrium and support geometry before catalogue life equations can be
used. In practical machine design this idea interacts with the other topics in bearings, tribology and sealing.
Begin with the object whose motion, load or temperature needs to be predicted. Isolate that object from its
neighbors and list the contacts, applied loads and supports. If a force is transmitted through a bearing,
fastener or contact patch, record what is assumed about that interface. A model that changes its boundary
conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only a short
equation.


The working situation here is a synthetic example: A shaft spans two bearings and carries a centered belt radial
load. First identify the intended load path. Next distinguish quantities that can be directly measured from
quantities inferred from a simplified equation. Finally ask which part of the assembly would change the result
if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically relevant
uncertainty belongs at the specific interface where its cause arises. Calculate reactions and operating speed
before selecting a component.
## Mathematical model, units and limits

One introductory relationship is **single radial reaction = F/2 for a symmetric centered load**. Interpret each
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

**Question:** Calculate symmetric bearing reaction using radial load=1400 N, centered between supports. Using
the explicit relationship for this simplified case, the arithmetic is `1400/2`. The computed result is **700
N**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.
Recalculate with an independent calculator before passing it into a later sizing step. A result outside a
plausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that putting only tangential torque force into the
bearing calculation neglects radial belt tension. A responsible notebook records both the numerical output and
the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Spread support or relocate the driven pulley to reduce peak reaction. This is not automatically a superior
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

Measure alignment, mounting flatness and actual load direction. A good verification plan specifies the specimen,
load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record both
passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its boundary
conditions and material state before changing the spreadsheet constants. When test data do not yet exist, label
the numerical model as an unvalidated hypothesis and specify the measurement that would have the greatest
information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Treat lubrication, thermal expansion and dirt as system variables. Do not interpolate beyond
the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Putting only tangential torque force into the bearing calculation neglects
radial belt tension.** Another common error is to stop as soon as a hand calculation passes a nominal allowable.
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

1. **Model reconstruction:** For the situation “A shaft spans two bearings and carries a centered belt radial load.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **single radial reaction = F/2 for a symmetric centered load**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **700 N** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Putting only tangential torque force into the bearing calculation neglects radial belt tension.” could occur. Propose one design modification based on “Spread support or relocate the driven pulley to reduce peak reaction.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Bearing reaction loads — revision A”. Include a named synthetic design case, a
dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity table, a
failure-mode paragraph and a validation step. Make the distinction between a calculation that you have completed
and a test that still needs to happen explicit. The next design stage should inherit your assumptions as visible
inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons between
student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 5 · Lesson 2: Rolling bearing rating life

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A deep-groove ball bearing operates at stable load and speed in clean
conditions. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

Basic dynamic rating life follows a power law in dynamic capacity to equivalent bearing load under specified
assumptions and reliability definition. In practical machine design this idea interacts with the other topics in
bearings, tribology and sealing. Begin with the object whose motion, load or temperature needs to be predicted.
Isolate that object from its neighbors and list the contacts, applied loads and supports. If a force is
transmitted through a bearing, fastener or contact patch, record what is assumed about that interface. A model
that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI
units, not only a short equation.


The working situation here is a synthetic example: A deep-groove ball bearing operates at stable load and speed
in clean conditions. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Treat lubrication,
thermal expansion and dirt as system variables.
## Mathematical model, units and limits

One introductory relationship is **L10 million revolutions = (C/P)^p**. Interpret each symbol before using
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

**Question:** Calculate ball bearing basic L10 using C=22000 N, P=4500 N, exponent=3. Using the explicit
relationship for this simplified case, the arithmetic is `(22000/4500)**3`. The computed result is **116.9
million revolutions**. This is a synthetic, rounded result; it is not a measured or independently certified
design capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that calling L10 a guarantee of service lifetime
disregards contamination, lubrication and probability. A responsible notebook records both the numerical output
and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Increase bearing size, lower load or improve cleanliness instead of assuming linear life gains. This is not
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

Compare operating temperature, lubricant condition and vibration signatures with design assumptions. A good
verification plan specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the
result will be analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the
simple model, investigate its boundary conditions and material state before changing the spreadsheet constants.
When test data do not yet exist, label the numerical model as an unvalidated hypothesis and specify the
measurement that would have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Record assumptions behind any statistical rating-life estimate. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Calling L10 a guarantee of service lifetime disregards contamination,
lubrication and probability.** Another common error is to stop as soon as a hand calculation passes a nominal
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

1. **Model reconstruction:** For the situation “A deep-groove ball bearing operates at stable load and speed in clean conditions.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **L10 million revolutions = (C/P)^p**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **116.9 million revolutions** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Calling L10 a guarantee of service lifetime disregards contamination, lubrication and probability.” could occur. Propose one design modification based on “Increase bearing size, lower load or improve cleanliness instead of assuming linear life gains.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Rolling bearing rating life — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 5 · Lesson 3: Lubrication regimes and film formation

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A gearbox experiences cold startup followed by stabilized oil
temperature. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

Boundary, mixed and hydrodynamic contacts behave differently; film thickness depends on viscosity, speed, load
and geometry. In practical machine design this idea interacts with the other topics in bearings, tribology and
sealing. Begin with the object whose motion, load or temperature needs to be predicted. Isolate that object from
its neighbors and list the contacts, applied loads and supports. If a force is transmitted through a bearing,
fastener or contact patch, record what is assumed about that interface. A model that changes its boundary
conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only a short
equation.


The working situation here is a synthetic example: A gearbox experiences cold startup followed by stabilized oil
temperature. First identify the intended load path. Next distinguish quantities that can be directly measured
from quantities inferred from a simplified equation. Finally ask which part of the assembly would change the
result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically
relevant uncertainty belongs at the specific interface where its cause arises. Record assumptions behind any
statistical rating-life estimate.
## Mathematical model, units and limits

One introductory relationship is **dynamic viscosity mu = rho*kinematic_viscosity**. Interpret each symbol
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

**Question:** Calculate dynamic viscosity using rho=860 kg/m3, nu=65e-6 m2/s. Using the explicit relationship
for this simplified case, the arithmetic is `860*65e-6`. The computed result is **0.0559 Pa s**. This is a
synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an
independent calculator before passing it into a later sizing step. A result outside a plausible physical range
is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that using room-temperature viscosity for hot operation
may overestimate film thickness. A responsible notebook records both the numerical output and the reason why the
model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check
whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding
margin.
## Design alternatives and trade-offs

Change speed, material, lubricant grade or feed architecture based on film demand. This is not automatically a
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

Check oil temperature, debris trends and startup torque changes. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Arrange monitoring to discover damage before catastrophic seizure. Do not interpolate beyond
the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Using room-temperature viscosity for hot operation may overestimate film
thickness.** Another common error is to stop as soon as a hand calculation passes a nominal allowable. Real
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

1. **Model reconstruction:** For the situation “A gearbox experiences cold startup followed by stabilized oil temperature.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **dynamic viscosity mu = rho*kinematic_viscosity**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.0559 Pa s** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Using room-temperature viscosity for hot operation may overestimate film thickness.” could occur. Propose one design modification based on “Change speed, material, lubricant grade or feed architecture based on film demand.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Lubrication regimes and film formation — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 5 · Lesson 4: Journal bearing PV and friction

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A polymer-lined pivot supports a steady load in intermittent rotation.
The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

Pressure times sliding speed provides a preliminary screen for some plain-bearing applications, subject to
supplier limits and thermal balance. In practical machine design this idea interacts with the other topics in
bearings, tribology and sealing. Begin with the object whose motion, load or temperature needs to be predicted.
Isolate that object from its neighbors and list the contacts, applied loads and supports. If a force is
transmitted through a bearing, fastener or contact patch, record what is assumed about that interface. A model
that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI
units, not only a short equation.


The working situation here is a synthetic example: A polymer-lined pivot supports a steady load in intermittent
rotation. First identify the intended load path. Next distinguish quantities that can be directly measured from
quantities inferred from a simplified equation. Finally ask which part of the assembly would change the result
if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically relevant
uncertainty belongs at the specific interface where its cause arises. Arrange monitoring to discover damage
before catastrophic seizure.
## Mathematical model, units and limits

One introductory relationship is **PV = (F/(d*L))*(pi*d*n/60)**. Interpret each symbol before using numbers and
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

**Question:** Calculate journal bearing PV screen using F=600 N, d=0.025 m, L=0.035 m, n=600 rpm. Using the
explicit relationship for this simplified case, the arithmetic is `600/(0.025*0.035)*(pi*0.025*600/60)/1e6`. The
computed result is **0.5386 MPa m/s**. This is a synthetic, rounded result; it is not a measured or
independently certified design capacity. Recalculate with an independent calculator before passing it into a
later sizing step. A result outside a plausible physical range is evidence that units or assumptions may be
wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that a low PV value alone does not prove adequate wear
life or heat removal. A responsible notebook records both the numerical output and the reason why the model is
incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check whether the
response is linear, quadratic or more sensitive, and explain what happens to the corresponding margin.
## Design alternatives and trade-offs

Consider rolling bearings or self-lubricating liners where maintenance access is poor. This is not automatically
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

Monitor running clearance, temperature and surface damage after life testing. A good verification plan specifies
the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed.
Record both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate
its boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Calculate reactions and operating speed before selecting a component. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **A low PV value alone does not prove adequate wear life or heat removal.**
Another common error is to stop as soon as a hand calculation passes a nominal allowable. Real machinery
experiences transient load combinations, operator changes, contamination and gradual loosening. A preliminary
analysis needs a hazard review: identify an initiating event, a progression mechanism, a consequence, a way to
detect the developing problem and a mitigation independent of the calculation. If the failure could injure a
person, preserve layers of protection such as guarding, interlocks and independent inspection.


To reason about robustness, imagine that one input parameter is wrong in the adverse direction. Would the system
simply lose accuracy, gradually wear, unexpectedly stop, or release stored energy? That distinction affects both
instrumentation and maintenance intervals. Reject the assumption that a neat mathematical expression guarantees
a graceful failure. The engineering result is an argument with explicitly limited evidence; it must remain open
to revision when a test, field incident or supplier change supplies new information.
## Exercises and guided self-check

1. **Model reconstruction:** For the situation “A polymer-lined pivot supports a steady load in intermittent rotation.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **PV = (F/(d*L))*(pi*d*n/60)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.5386 MPa m/s** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “A low PV value alone does not prove adequate wear life or heat removal.” could occur. Propose one design modification based on “Consider rolling bearings or self-lubricating liners where maintenance access is poor.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Journal bearing PV and friction — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 5 · Lesson 5: Sealing and contamination control

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A dusty process line exposes a rotating seal lip to abrasive particles.
The objective is to develop a defendable preliminary calculation, identify its governing assumptions, and plan a
test that could show the calculation to be wrong. After this lesson, you should be able to explain the chosen
physical model in words; state the controlling variables and units; evaluate one illustrative example; and
describe a failure mechanism that the equation alone does not capture. The scope is a learning design review,
not a released production drawing.
## Physical reasoning and load path

A seal must exclude particles and moisture while accommodating pressure, shaft speed, eccentricity and lubricant
compatibility. In practical machine design this idea interacts with the other topics in bearings, tribology and
sealing. Begin with the object whose motion, load or temperature needs to be predicted. Isolate that object from
its neighbors and list the contacts, applied loads and supports. If a force is transmitted through a bearing,
fastener or contact patch, record what is assumed about that interface. A model that changes its boundary
conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only a short
equation.


The working situation here is a synthetic example: A dusty process line exposes a rotating seal lip to abrasive
particles. First identify the intended load path. Next distinguish quantities that can be directly measured from
quantities inferred from a simplified equation. Finally ask which part of the assembly would change the result
if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the physically relevant
uncertainty belongs at the specific interface where its cause arises. Calculate reactions and operating speed
before selecting a component.
## Mathematical model, units and limits

One introductory relationship is **surface speed v = pi*d*n/60**. Interpret each symbol before using numbers and
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

**Question:** Calculate seal surface speed using shaft diameter=0.03 m, speed=900 rpm. Using the explicit
relationship for this simplified case, the arithmetic is `pi*0.03*900/60`. The computed result is **1.414 m/s**.
This is a synthetic, rounded result; it is not a measured or independently certified design capacity.
Recalculate with an independent calculator before passing it into a later sizing step. A result outside a
plausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that choosing seals from nominal bore diameter alone
ignores wear, temperature and shaft finish. A responsible notebook records both the numerical output and the
reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base
value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Add an exclusion labyrinth before the primary seal to reduce particle loading. This is not automatically a
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

Inspect contact tracks, lip orientation, leakage and ingress after thermal cycles. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Treat lubrication, thermal expansion and dirt as system variables. Do not interpolate beyond
the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Choosing seals from nominal bore diameter alone ignores wear, temperature
and shaft finish.** Another common error is to stop as soon as a hand calculation passes a nominal allowable.
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

1. **Model reconstruction:** For the situation “A dusty process line exposes a rotating seal lip to abrasive particles.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **surface speed v = pi*d*n/60**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **1.414 m/s** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Choosing seals from nominal bore diameter alone ignores wear, temperature and shaft finish.” could occur. Propose one design modification based on “Add an exclusion labyrinth before the primary seal to reduce particle loading.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Sealing and contamination control — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

