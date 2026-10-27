# Unit 4: Members, stability and multiaxial stress

**Guiding question:** How can engineers translate material response into component deformation?

## Physical map and learning outcomes

A hollow beam, a slender column and a notched plate use the same fictional alloy. A procurement team treats material yield strength as sufficient for all three designs and ignores boundary conditions. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Calculate bending stress and Euler ideal buckling load, estimate notch stress concentration and compare multiaxial stress measures with their corresponding applicability domains. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 4.1: Beam bending and elastic section modulus

### Physical reasoning and derivation target

Euler–Bernoulli beam theory links curvature to bending moment under small deflection and plane-section assumptions. The maximum bending normal stress for simple uniaxial bending scales as M c/I, making section geometry central to strength even when E and nominal material strength are unchanged.

**Governing relationship and applicability:** sigma_x=M y/I for elementary linear elastic bending. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare rectangular beams with equal area but different depth at identical bending moment and support span.

A related local calculator for this lesson is **Maximum elastic beam stress**. Use **Applied bending moment = 32.85714 N·m** with the other parameters fixed. The illustrative model returns **6.5714286 MPa**. Repeat the computation at **Applied bending moment = 64.05714 N·m** to obtain **12.811429 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Elastic beam, c=10 mm, I=50000 mm⁴, pure bending, no shear or local instability**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Shear deformation, large rotations and local buckling invalidate a thin-beam approximation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What ratio of beam depth to span signals a need to check transverse shear? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **32.85714 N·m**, and recover **6.5714286 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Shear deformation, large rotations and local buckling invalidate a thin-beam approximation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 4.2: Torsion of circular shafts

### Physical reasoning and derivation target

In small-strain linear elastic torsion of circular prismatic shafts, angular twist follows theta=T L/(GJ), and shear stress varies with radius. Thin-walled noncircular sections can warp, and torsional response depends strongly on boundary restrictions. Hollow shafts trade mass against polar moment in a geometry-dependent way.

**Governing relationship and applicability:** tau(r)=Tr/J, theta=TL/(GJ) for circular shafts. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare a solid round shaft and a hollow shaft with equal outside radius and load; compute their torsional compliance.

A related local calculator for this lesson is **Euler elastic column load**. Use **Effective pinned column length = 0.9714286 m** with the other parameters fixed. The illustrative model returns **41.834828 kN**. Repeat the computation at **Effective pinned column length = 1.291429 m** to obtain **23.671128 kN**; the output falls when the input rises. Record the expression and its model domain exactly: **E=200 GPa, I=2×10⁻⁸ m⁴, K=1, ideal slender pinned column, no imperfection**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A shaft with slots, keyways or elliptical cross-section does not follow the simple circular distribution.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What evidence of warping would require a different cross-sectional theory? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **0.9714286 m**, and recover **41.834828 kN**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A shaft with slots, keyways or elliptical cross-section does not follow the simple circular distribution.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 4.3: Buckling and structural instability

### Physical reasoning and derivation target

Euler elastic buckling gives a load scale proportional to flexural rigidity EI divided by effective length squared. Real columns contain geometric imperfection, residual stress and material nonlinearity, so the ideal eigenvalue is not automatically a permissible design load. Effective length reflects end rotation and translation constraints.

**Governing relationship and applicability:** P_cr=pi² E I/(K L)² for ideal elastic prismatic slender columns. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare a pinned-pinned and fixed-fixed ideal column of equal length, E and I while checking the implied ideal K factor.

A related local calculator for this lesson is **Maximum elastic beam stress**. Use **Applied bending moment = 88.57143 N·m** with the other parameters fixed. The illustrative model returns **17.714286 MPa**. Repeat the computation at **Applied bending moment = 119.7714 N·m** to obtain **23.954286 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Elastic beam, c=10 mm, I=50000 mm⁴, pure bending, no shear or local instability**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A stocky column may yield before ideal elastic buckling; unknown end conditions can dominate prediction error.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which displacement-field observation separates flexural instability from compressive crushing? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **88.57143 N·m**, and recover **17.714286 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A stocky column may yield before ideal elastic buckling; unknown end conditions can dominate prediction error.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 4.4: Stress concentration and notch geometry

### Physical reasoning and derivation target

Holes, grooves and sharp geometric transitions intensify local stress even when the nominal section force remains constant. Elastic stress concentration Kt depends on geometry and loading, while a material's notch sensitivity and local yielding determine whether the peak elastic stress predicts failure. A sharper notch is not mathematically identical to a finite crack.

**Governing relationship and applicability:** sigma_max=Kt sigma_nom for a specified elastic geometry. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare strain gauges near and far from a rounded hole under a fixed remote tensile stress.

A related local calculator for this lesson is **Euler elastic column load**. Use **Effective pinned column length = 1.542857 m** with the other parameters fixed. The illustrative model returns **16.584726 kN**. Repeat the computation at **Effective pinned column length = 1.862857 m** to obtain **11.376289 kN**; the output falls when the input rises. Record the expression and its model domain exactly: **E=200 GPa, I=2×10⁻⁸ m⁴, K=1, ideal slender pinned column, no imperfection**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Three-dimensional edge effects, free-surface constraints and nonlinear local plasticity challenge an elementary elastic Kt estimate.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What full-field measurement checks whether the local peak is where the model predicts? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **1.542857 m**, and recover **16.584726 kN**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Three-dimensional edge effects, free-surface constraints and nonlinear local plasticity challenge an elementary elastic Kt estimate.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 4.5: Combined loading and equivalent stress

### Physical reasoning and derivation target

Components often carry tension, torsion, bending and residual stress concurrently. Tensor stress transformation reveals principal values and invariants; a von Mises scalar is useful for assessing isotropic ductile yielding under certain assumptions but does not encode crack-opening traction or brittle cleavage. Failure criteria must fit the material and governing mechanism.

**Governing relationship and applicability:** sigma_VM=sqrt(sigma²+3 tau²) for axial stress plus a single shear component. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compute equivalent stress for invented combined axial tension and pure shear and compare with maximum-principal-stress ranking.

A related local calculator for this lesson is **Maximum elastic beam stress**. Use **Applied bending moment = 144.2857 N·m** with the other parameters fixed. The illustrative model returns **28.857143 MPa**. Repeat the computation at **Applied bending moment = 175.4857 N·m** to obtain **35.097143 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Elastic beam, c=10 mm, I=50000 mm⁴, pure bending, no shear or local instability**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A criterion calibrated in monotonic proportional loading may fail after load path reversal or damage accumulation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which stress component primarily opens a pre-existing tensile crack? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **144.2857 N·m**, and recover **28.857143 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A criterion calibrated in monotonic proportional loading may fail after load path reversal or damage accumulation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Geometry versus constituent strength

### Scientific question and competing hypotheses

A hollow beam, a slender column and a notched plate use the same fictional alloy. A procurement team treats material yield strength as sufficient for all three designs and ignores boundary conditions.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Calculate bending stress and Euler ideal buckling load, estimate notch stress concentration and compare multiaxial stress measures with their corresponding applicability domains.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Measure deflection curves and load–displacement histories with independent optical tracking. Survey dimensions and end constraints rather than assuming theoretical fixtures.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Nominal allowable stress cannot guarantee stability or exclude local cracking; component geometry is a first-class variable.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_6 -->

<!-- MODEL_7 -->

