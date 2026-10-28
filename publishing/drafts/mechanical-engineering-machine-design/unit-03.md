# Unit 03: Fatigue, Fracture and Durability

**Course Code**: MDS 203 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Fatigue, Fracture and Durability**.

# Unit 3 · Lesson 1: Stress cycles and amplitude

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A rotating component experiences fully reversed bending and positive
torque during each revolution. The objective is to develop a defendable preliminary calculation, identify its
governing assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you
should be able to explain the chosen physical model in words; state the controlling variables and units;
evaluate one illustrative example; and describe a failure mechanism that the equation alone does not capture.
The scope is a learning design review, not a released production drawing.
## Physical reasoning and load path

Fatigue analysis separates mean stress from alternating stress; two load histories with identical peaks can have
different life consequences. In practical machine design this idea interacts with the other topics in fatigue,
fracture and durability. Begin with the object whose motion, load or temperature needs to be predicted. Isolate
that object from its neighbors and list the contacts, applied loads and supports. If a force is transmitted
through a bearing, fastener or contact patch, record what is assumed about that interface. A model that changes
its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only
a short equation.


The working situation here is a synthetic example: A rotating component experiences fully reversed bending and
positive torque during each revolution. First identify the intended load path. Next distinguish quantities that
can be directly measured from quantities inferred from a simplified equation. Finally ask which part of the
assembly would change the result if it were flexible, worn or misaligned. This is not a generic safety-factor
exercise: the physically relevant uncertainty belongs at the specific interface where its cause arises. Describe
mean, alternating and maximum stress separately.
## Mathematical model, units and limits

One introductory relationship is **sigma_a = (sigma_max-sigma_min)/2**. Interpret each symbol before using
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

**Question:** Calculate alternating normal stress using max=130 MPa, min=-70 MPa. Using the explicit
relationship for this simplified case, the arithmetic is `(130-(-70))/2`. The computed result is **100 MPa**.
This is a synthetic, rounded result; it is not a measured or independently certified design capacity.
Recalculate with an independent calculator before passing it into a later sizing step. A result outside a
plausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that entering peak-to-peak range as amplitude doubles
the cyclic stress in the calculation. A responsible notebook records both the numerical output and the reason
why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;
check whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding
margin.
## Design alternatives and trade-offs

Reduce surface stress through geometry, rather than relying on a cosmetic finish. This is not automatically a
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

Record speed, direction reversals and overload events in a load history. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Use material fatigue data relevant to finish, size and exposure. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Entering peak-to-peak range as amplitude doubles the cyclic stress in the
calculation.** Another common error is to stop as soon as a hand calculation passes a nominal allowable. Real
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

1. **Model reconstruction:** For the situation “A rotating component experiences fully reversed bending and positive torque during each revolution.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **sigma_a = (sigma_max-sigma_min)/2**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **100 MPa** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Entering peak-to-peak range as amplitude doubles the cyclic stress in the calculation.” could occur. Propose one design modification based on “Reduce surface stress through geometry, rather than relying on a cosmetic finish.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Stress cycles and amplitude — revision A”. Include a named synthetic design
case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity
table, a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 3 · Lesson 2: Mean-stress correction

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A machine bracket experiences nonzero tensile mean stress from preload
plus fluctuating vibration. The objective is to develop a defendable preliminary calculation, identify its
governing assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you
should be able to explain the chosen physical model in words; state the controlling variables and units;
evaluate one illustrative example; and describe a failure mechanism that the equation alone does not capture.
The scope is a learning design review, not a released production drawing.
## Physical reasoning and load path

Goodman is a simple linear screening relation for positive mean stress and alternating stress when an endurance
limit and ultimate tensile strength are meaningful. In practical machine design this idea interacts with the
other topics in fatigue, fracture and durability. Begin with the object whose motion, load or temperature needs
to be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports. If a
force is transmitted through a bearing, fastener or contact patch, record what is assumed about that interface.
A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions
in SI units, not only a short equation.


The working situation here is a synthetic example: A machine bracket experiences nonzero tensile mean stress
from preload plus fluctuating vibration. First identify the intended load path. Next distinguish quantities that
can be directly measured from quantities inferred from a simplified equation. Finally ask which part of the
assembly would change the result if it were flexible, worn or misaligned. This is not a generic safety-factor
exercise: the physically relevant uncertainty belongs at the specific interface where its cause arises. Use
material fatigue data relevant to finish, size and exposure.
## Mathematical model, units and limits

One introductory relationship is **Goodman utilization = sigma_a/Se + sigma_m/Sut**. Interpret each symbol
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

**Question:** Calculate Goodman stress utilization using alternating=76 MPa, mean=38 MPa, Se=180 MPa, Sut=520
MPa. Using the explicit relationship for this simplified case, the arithmetic is `76/180+38/520`. The computed
result is **0.4953 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently
certified design capacity. Recalculate with an independent calculator before passing it into a later sizing
step. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not
automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that extrapolating a Goodman line to compressive mean
stress or unconventional materials without evidence is unsound. A responsible notebook records both the
numerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with
80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain
what happens to the corresponding margin.
## Design alternatives and trade-offs

Decrease tensile mean stress or apply a rigorously supported residual-stress treatment. This is not
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

Check actual stress ratio and fatigue data at the operating temperature. A good verification plan specifies the
specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be analyzed. Record
both passing and failing tests. If the inspected assembly disagrees with the simple model, investigate its
boundary conditions and material state before changing the spreadsheet constants. When test data do not yet
exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would have the
greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Retain cycle counts and overload history rather than average power alone. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Extrapolating a Goodman line to compressive mean stress or unconventional
materials without evidence is unsound.** Another common error is to stop as soon as a hand calculation passes a
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

1. **Model reconstruction:** For the situation “A machine bracket experiences nonzero tensile mean stress from preload plus fluctuating vibration.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **Goodman utilization = sigma_a/Se + sigma_m/Sut**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.4953 dimensionless** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Extrapolating a Goodman line to compressive mean stress or unconventional materials without evidence is unsound.” could occur. Propose one design modification based on “Decrease tensile mean stress or apply a rigorously supported residual-stress treatment.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Mean-stress correction — revision A”. Include a named synthetic design case, a
dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity table, a
failure-mode paragraph and a validation step. Make the distinction between a calculation that you have completed
and a test that still needs to happen explicit. The next design stage should inherit your assumptions as visible
inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons between
student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 3 · Lesson 3: Notch effects and fatigue strength

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A shoulder fillet on a transmission shaft interrupts otherwise uniform
stress. The objective is to develop a defendable preliminary calculation, identify its governing assumptions,
and plan a test that could show the calculation to be wrong. After this lesson, you should be able to explain
the chosen physical model in words; state the controlling variables and units; evaluate one illustrative
example; and describe a failure mechanism that the equation alone does not capture. The scope is a learning
design review, not a released production drawing.
## Physical reasoning and load path

A geometric theoretical concentration Kt and a fatigue concentration Kf are not identical; notch sensitivity q
depends on material and notch size. In practical machine design this idea interacts with the other topics in
fatigue, fracture and durability. Begin with the object whose motion, load or temperature needs to be predicted.
Isolate that object from its neighbors and list the contacts, applied loads and supports. If a force is
transmitted through a bearing, fastener or contact patch, record what is assumed about that interface. A model
that changes its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI
units, not only a short equation.


The working situation here is a synthetic example: A shoulder fillet on a transmission shaft interrupts
otherwise uniform stress. First identify the intended load path. Next distinguish quantities that can be
directly measured from quantities inferred from a simplified equation. Finally ask which part of the assembly
would change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise:
the physically relevant uncertainty belongs at the specific interface where its cause arises. Retain cycle
counts and overload history rather than average power alone.
## Mathematical model, units and limits

One introductory relationship is **Kf = 1+q*(Kt-1)**. Interpret each symbol before using numbers and confirm
that both sides have compatible dimensions. The equation describes only a limited idealization. It cannot on its
own provide a complete stress concentration, fatigue spectrum, thermal field, production tolerance or failure
probability. When the design is sensitive to parameters that do not appear in the expression, extend the model
or supplement it with measurement. All numerical values below are invented for teaching and should not be used
as component ratings.


A useful derivation strategy is to begin with a balance law or definition rather than memorizing a result. Draw
the section or contact area carrying the force. For static problems, write force and moment equilibrium; for
dynamic systems, include inertia and a time scale; for energy storage or dissipation, write the work–energy
balance. Then insert geometry: area, section modulus, rotational radius or contact length. Do not make a
constant dimensionless by accident: millimetres versus metres can change a calculated stress by a factor of one
million or more. Check the limiting case as the main dimension grows or load tends toward zero.
## Illustrative worked calculation

**Question:** Calculate fatigue notch concentration using Kt=2.2, q=0.7. Using the explicit relationship for
this simplified case, the arithmetic is `1+0.7*(2.2-1)`. The computed result is **1.84 dimensionless**. This is
a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with
an independent calculator before passing it into a later sizing step. A result outside a plausible physical
range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that using Kt for static stress but forgetting Kf in
alternating stress hides fatigue risk. A responsible notebook records both the numerical output and the reason
why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;
check whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding
margin.
## Design alternatives and trade-offs

Enlarge transition radius or remove the step using a different bearing arrangement. This is not automatically a
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

Inspect fillet radius, grinding direction and surface defects under magnification. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Report life as a model-dependent estimate with inspection provisions. Do not interpolate
beyond the physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Using Kt for static stress but forgetting Kf in alternating stress hides
fatigue risk.** Another common error is to stop as soon as a hand calculation passes a nominal allowable. Real
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

1. **Model reconstruction:** For the situation “A shoulder fillet on a transmission shaft interrupts otherwise uniform stress.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **Kf = 1+q*(Kt-1)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **1.84 dimensionless** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Using Kt for static stress but forgetting Kf in alternating stress hides fatigue risk.” could occur. Propose one design modification based on “Enlarge transition radius or remove the step using a different bearing arrangement.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Notch effects and fatigue strength — revision A”. Include a named synthetic
design case, a dated annotated sketch, the model equation, units, every assumed property, a value trace, a
sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a calculation
that you have completed and a test that still needs to happen explicit. The next design stage should inherit
your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record structure
makes comparisons between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 3 · Lesson 4: Cumulative damage models

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A hoist drive alternates light-duty cycles and occasional lifting at
maximum load. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

A linear cycle-fraction model sums n_i/N_i for distinct load levels; the approximate damage index is not a
deterministic fracture clock. In practical machine design this idea interacts with the other topics in fatigue,
fracture and durability. Begin with the object whose motion, load or temperature needs to be predicted. Isolate
that object from its neighbors and list the contacts, applied loads and supports. If a force is transmitted
through a bearing, fastener or contact patch, record what is assumed about that interface. A model that changes
its boundary conditions silently cannot be verified. Use a labelled sketch with dimensions in SI units, not only
a short equation.


The working situation here is a synthetic example: A hoist drive alternates light-duty cycles and occasional
lifting at maximum load. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Report life as a
model-dependent estimate with inspection provisions.
## Mathematical model, units and limits

One introductory relationship is **Miner damage D = sum(n_i/N_i)**. Interpret each symbol before using numbers
and confirm that both sides have compatible dimensions. The equation describes only a limited idealization. It
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

**Question:** Calculate Miner sum of two bins using n1=10000,N1=100000,n2=20000,N2=200000. Using the explicit
relationship for this simplified case, the arithmetic is `10000/100000+20000/200000`. The computed result is
**0.2 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified
design capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result
outside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new
discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that ignoring load sequence, corrosion or overload
interactions can make a Miner estimate nonconservative. A responsible notebook records both the numerical output
and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Apply condition monitoring and conservative inspection intervals to critical parts. This is not automatically a
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

Collect representative load histograms rather than assuming a single average event. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Describe mean, alternating and maximum stress separately. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Ignoring load sequence, corrosion or overload interactions can make a
Miner estimate nonconservative.** Another common error is to stop as soon as a hand calculation passes a nominal
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

1. **Model reconstruction:** For the situation “A hoist drive alternates light-duty cycles and occasional lifting at maximum load.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **Miner damage D = sum(n_i/N_i)**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **0.2 dimensionless** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Ignoring load sequence, corrosion or overload interactions can make a Miner estimate nonconservative.” could occur. Propose one design modification based on “Apply condition monitoring and conservative inspection intervals to critical parts.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Cumulative damage models — revision A”. Include a named synthetic design case,
a dated annotated sketch, the model equation, units, every assumed property, a value trace, a sensitivity table,
a failure-mode paragraph and a validation step. Make the distinction between a calculation that you have
completed and a test that still needs to happen explicit. The next design stage should inherit your assumptions
as visible inputs rather than silently reusing nominal dimensions. The same record structure makes comparisons
between student designs reproducible without implying that a laboratory result was obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

# Unit 3 · Lesson 5: Wear, fretting and environmental fatigue

**OpenSTEM Mechanical Engineering — Machine Design · unreviewed educational draft**

## Outcomes and the design question

The immediate engineering question is: A keyed rotating hub vibrates at small amplitude in a humid plant
environment. The objective is to develop a defendable preliminary calculation, identify its governing
assumptions, and plan a test that could show the calculation to be wrong. After this lesson, you should be able
to explain the chosen physical model in words; state the controlling variables and units; evaluate one
illustrative example; and describe a failure mechanism that the equation alone does not capture. The scope is a
learning design review, not a released production drawing.
## Physical reasoning and load path

Small-amplitude slip at contacts can degrade surfaces and nucleate cracks; corrosion changes local crack
behavior and invalidates many dry-air fatigue assumptions. In practical machine design this idea interacts with
the other topics in fatigue, fracture and durability. Begin with the object whose motion, load or temperature
needs to be predicted. Isolate that object from its neighbors and list the contacts, applied loads and supports.
If a force is transmitted through a bearing, fastener or contact patch, record what is assumed about that
interface. A model that changes its boundary conditions silently cannot be verified. Use a labelled sketch with
dimensions in SI units, not only a short equation.


The working situation here is a synthetic example: A keyed rotating hub vibrates at small amplitude in a humid
plant environment. First identify the intended load path. Next distinguish quantities that can be directly
measured from quantities inferred from a simplified equation. Finally ask which part of the assembly would
change the result if it were flexible, worn or misaligned. This is not a generic safety-factor exercise: the
physically relevant uncertainty belongs at the specific interface where its cause arises. Describe mean,
alternating and maximum stress separately.
## Mathematical model, units and limits

One introductory relationship is **sliding distance = velocity*time**. Interpret each symbol before using
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

**Question:** Calculate distance accumulated in micro-slip using v=0.00001 m/s, t=12 h. Using the explicit
relationship for this simplified case, the arithmetic is `0.00001*12*3600*1000`. The computed result is **432
mm**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.
Recalculate with an independent calculator before passing it into a later sizing step. A result outside a
plausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.


**Interpretation:** The number answers only the posed arithmetic question. A design release would require a
defined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate
assessment. The main danger in this particular lesson is that treating seal wear, corrosion and fatigue as
unrelated independent hazards misses interactions. A responsible notebook records both the numerical output and
the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its
base value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the
corresponding margin.
## Design alternatives and trade-offs

Change joint design or environment control before simply changing base metal. This is not automatically a
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

Inspect oxide debris, contact geometry, lubricant condition and loss of preload. A good verification plan
specifies the specimen, load sequence, sensor, calibration, acceptance threshold and how the result will be
analyzed. Record both passing and failing tests. If the inspected assembly disagrees with the simple model,
investigate its boundary conditions and material state before changing the spreadsheet constants. When test data
do not yet exist, label the numerical model as an unvalidated hypothesis and specify the measurement that would
have the greatest information value.


Start a three-point sensitivity audit. In case A, reduce the controlling load or speed by 15%; in case B use the
nominal estimate; in case C increase it by 15%. Repeat for the most uncertain dimension or coefficient, where
practical. Compare the resulting changes with the expected scatter of the chosen manufacturing process. A
threshold that is crossed by a small plausible input variation calls for redesign, tighter process control or
more information. Use material fatigue data relevant to finish, size and exposure. Do not interpolate beyond the
physical domain of the governing model.
## Failure-first engineering discussion

The most dangerous shortcut here is **Treating seal wear, corrosion and fatigue as unrelated independent hazards
misses interactions.** Another common error is to stop as soon as a hand calculation passes a nominal allowable.
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

1. **Model reconstruction:** For the situation “A keyed rotating hub vibrates at small amplitude in a humid plant environment.”, draw a labelled free-body or energy-flow diagram, define each numerical input and state two boundary conditions that would invalidate **sliding distance = velocity*time**. Estimate which input has the largest practical uncertainty.
2. **Sensitivity experiment:** Recompute the synthetic example result **432 mm** after increasing its principal design action by 20%. Explain whether the output changes linearly, nonlinearly or not at all, and demonstrate the dimensional consistency.
3. **Failure and evidence:** Investigate why “Treating seal wear, corrosion and fatigue as unrelated independent hazards misses interactions.” could occur. Propose one design modification based on “Change joint design or environment control before simply changing base metal.”, one bench test and one field inspection capable of detecting the relevant failure mode.

## Design notebook record

Create a one-page record titled “Wear, fretting and environmental fatigue — revision A”. Include a named
synthetic design case, a dated annotated sketch, the model equation, units, every assumed property, a value
trace, a sensitivity table, a failure-mode paragraph and a validation step. Make the distinction between a
calculation that you have completed and a test that still needs to happen explicit. The next design stage should
inherit your assumptions as visible inputs rather than silently reusing nominal dimensions. The same record
structure makes comparisons between student designs reproducible without implying that a laboratory result was
obtained.

---

**Academic and safety note:** This is an unreviewed educational draft. No illustrative strength, dimension, safety factor or simplified life equation is an approved industrial design.


---

