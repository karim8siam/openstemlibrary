# Unit 2: Yielding, work hardening and flow

**Guiding question:** What changes when deformation becomes irreversible?

## Physical map and learning outcomes

A synthetic sheet-metal forming trial shows no sharp yield point, then undergoes a reverse loading cycle. An analyst applies the first-loading stress curve to predict springback after reversal. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Construct 0.2 percent offset proof stress, separate plastic from elastic strain, evaluate a work-hardening fit on the admissible range, and compare an isotropic versus a kinematic-hardening illustration. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 2.1: Yield criterion and proof stress

### Physical reasoning and derivation target

Yielding in metals reflects the onset of widespread irreversible plastic flow, and the definition of a practical yield point depends on the material and method. An offset proof stress uses a line parallel to the initial elastic slope, commonly at 0.2 percent plastic strain for relevant alloys. It is a convention, not a universal microscopic threshold.

**Governing relationship and applicability:** sigma_0.2 is the intersection of stress–strain data with epsilon=sigma/E+0.002. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Obtain a synthetic stress–strain curve lacking a sharp yield point; construct the offset line and estimate where it intersects the curve.

A related local calculator for this lesson is **Offset yield-section load**. Use **Original section area = 52.85714 mm²** with the other parameters fixed. The illustrative model returns **13.214286 kN**. Repeat the computation at **Original section area = 89.65714 mm²** to obtain **22.414286 kN**; the output rises when the input rises. Record the expression and its model domain exactly: **Illustrative proof stress=250 MPa, uniaxial average stress, no stability or defect allowance**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Noisy extensometer data, machine compliance and curved initial seating can displace the constructed proof point.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What material response makes an offset criterion preferable to a first-deviation criterion? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **52.85714 mm²**, and recover **13.214286 kN**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Noisy extensometer data, machine compliance and curved initial seating can displace the constructed proof point.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 2.2: Plastic flow and incompressibility

### Physical reasoning and derivation target

For many dense metals in typical plastic deformation, plastic volume change is small compared with shape change. Equivalent plastic strain summarizes the history of deviatoric plastic increments and is not identical to the measured axial total strain. Hydrostatic stress influences void evolution even when it does not drive von Mises yielding directly.

**Governing relationship and applicability:** von Mises equivalent stress sigma_eq=sqrt(3 J2) under isotropic J2 plasticity. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare tension and compression of nominally the same alloy, then analyze diameter changes rather than using only axial actuator travel.

A related local calculator for this lesson is **Nonlinear Ramberg–Osgood strain**. Use **Applied nominal stress = 157.1429 MPa** with the other parameters fixed. The illustrative model returns **0.00075679918 strain**. Repeat the computation at **Applied nominal stress = 233.9429 MPa** to obtain **0.0012065479 strain**; the output rises when the input rises. Record the expression and its model domain exactly: **Simplified epsilon=sigma/E+(sigma/K)^n with E=210000 MPa, K=1100 MPa, n=6; fitted only within fictional regime**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Damage, porosity and pressure-dependent solids can violate the isochoric-plasticity approximation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which volume-change observation suggests dilatancy or void growth? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **157.1429 MPa**, and recover **0.00075679918 strain**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Damage, porosity and pressure-dependent solids can violate the isochoric-plasticity approximation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 2.3: Hardening and Considère instability

### Physical reasoning and derivation target

Plastic deformation changes dislocation structure and can raise the stress needed for further flow. True stress versus true plastic strain is often represented empirically by a power law over a limited range. Under uniform tension, onset of diffuse necking is linked to the condition d sigma_true/d epsilon_true=sigma_true, not merely to a visible neck.

**Governing relationship and applicability:** Hollomon sigma=K epsilon_p^n over fitted range; Considère criterion for ideal tensile instability. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare two invented flow curves with different strain-hardening exponents and predict which supports more uniform extension.

A related local calculator for this lesson is **Offset yield-section load**. Use **Original section area = 118.5714 mm²** with the other parameters fixed. The illustrative model returns **29.642857 kN**. Repeat the computation at **Original section area = 155.3714 mm²** to obtain **38.842857 kN**; the output rises when the input rises. Record the expression and its model domain exactly: **Illustrative proof stress=250 MPa, uniaxial average stress, no stability or defect allowance**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Rate sensitivity, anisotropy and nonuniform fields can shift the applicability of a simple instability rule.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would changing strain rate reveal a contribution to necking beyond work hardening? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **118.5714 mm²**, and recover **29.642857 kN**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Rate sensitivity, anisotropy and nonuniform fields can shift the applicability of a simple instability rule.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 2.4: Temperature and rate effects on flow

### Physical reasoning and derivation target

Plastic strength can depend strongly on temperature and strain rate because thermal activation helps dislocations cross obstacles. An Arrhenius-like rate expression is an approximation that needs stated mechanism and stress normalization. Room-temperature data cannot be extrapolated to hot forming without testing for dynamic recovery, recrystallization and other changes.

**Governing relationship and applicability:** strain rate dot-epsilon=delta L rate/L0 for small uniform strains. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Test an ideal metal at two temperatures and two extension rates, adjusting nominal strain rate for the gauge length.

A related local calculator for this lesson is **Nonlinear Ramberg–Osgood strain**. Use **Applied nominal stress = 294.2857 MPa** with the other parameters fixed. The illustrative model returns **0.0017680167 strain**. Repeat the computation at **Applied nominal stress = 371.0857 MPa** to obtain **0.0032410471 strain**; the output rises when the input rises. Record the expression and its model domain exactly: **Simplified epsilon=sigma/E+(sigma/K)^n with E=210000 MPa, K=1100 MPa, n=6; fitted only within fictional regime**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Machine control may not impose a constant true strain rate after necking, and local heating can distort apparent rate dependence.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What extra temperature measurement would identify self-heating during rapid deformation? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **294.2857 MPa**, and recover **0.0017680167 strain**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Machine control may not impose a constant true strain rate after necking, and local heating can distort apparent rate dependence.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 2.5: Bauschinger effect and path dependence

### Physical reasoning and derivation target

A previously strained metal often yields differently after load reversal because internal stress fields and dislocation arrangements retain a memory of loading path. Isotropic hardening models expand a yield surface, while kinematic hardening translates it; neither is universally adequate. Springback depends on elastic stiffness and residual stress after forming.

**Governing relationship and applicability:** path-dependent elastic-plastic constitutive models; no single scalar hardening curve. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Prestrain a thin strip in tension, unload, reverse in compression and compare the reverse onset with a monotonic control.

A related local calculator for this lesson is **Offset yield-section load**. Use **Original section area = 184.2857 mm²** with the other parameters fixed. The illustrative model returns **46.071429 kN**. Repeat the computation at **Original section area = 221.0857 mm²** to obtain **55.271429 kN**; the output rises when the input rises. Record the expression and its model domain exactly: **Illustrative proof stress=250 MPa, uniaxial average stress, no stability or defect allowance**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Fixture backlash, buckling in compression and changing sample section can mimic a reversed-yield shift.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which strain-controlled reversal experiment would separate microstructural memory from testing artifacts? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **184.2857 mm²**, and recover **46.071429 kN**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Fixture backlash, buckling in compression and changing sample section can mimic a reversed-yield shift.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Offset yield and path-dependent response

### Scientific question and competing hypotheses

A synthetic sheet-metal forming trial shows no sharp yield point, then undergoes a reverse loading cycle. An analyst applies the first-loading stress curve to predict springback after reversal.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Construct 0.2 percent offset proof stress, separate plastic from elastic strain, evaluate a work-hardening fit on the admissible range, and compare an isotropic versus a kinematic-hardening illustration.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Repeat the test with axial extensometry and strain-controlled reversal, recording force-zero drift and any buckling risk. Compare two rolling orientations.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

A fitted monotonic hardening exponent does not describe multiaxial reversal without an appropriate path-dependent constitutive model.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_2 -->

<!-- MODEL_3 -->

