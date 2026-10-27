# Unit 1: Stress, strain and recoverable deformation

**Guiding question:** How do forces, geometry and constitutive response combine to determine deformation?

## Physical map and learning outcomes

Two invented aluminum coupons have identical stress–strain curves if crosshead travel is treated as specimen extension; optical gauge readings show a different elastic slope. The task is to identify compliance contamination and report the observable with its correct gauge basis. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Build a load–extension data table and independently calculate stress, engineering strain, true strain during uniform deformation, transverse strain and elastic energy density. Fit the elastic slope only after examining residuals and gauge calibration. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 1.1: Traction and Cauchy stress

### Physical reasoning and derivation target

A loaded solid transmits internal forces across imaginary cuts, and the traction vector depends on the orientation of the chosen cut. Its normal and shear components are resolved from a stress tensor rather than a single universal load-over-area number. Engineering axial stress F/A0 is a useful average for a uniform tensile coupon but is not the complete local state at a hole or grip.

**Governing relationship and applicability:** sigma=F/A0, principal stresses and traction t(n)=sigma·n. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Contrast a smooth tensile bar with an eccentrically gripped bar at identical machine load; sketch free bodies, estimate nominal stress and explain the bent bar's extra moment.

A related local calculator for this lesson is **Nominal tensile stress**. Use **Applied force = 7.285714 kN** with the other parameters fixed. The illustrative model returns **60.714286 MPa**. Repeat the computation at **Applied force = 14.32571 kN** to obtain **119.38095 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Initial section A0=120 mm²; engineering stress for centered uniaxial loading, no local concentration**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A measured actuator force does not reveal the spatial stress field, especially at contacts, cutouts and grips.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What independent displacement or strain-field measurement would reveal a hidden bending moment? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **7.285714 kN**, and recover **60.714286 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A measured actuator force does not reveal the spatial stress field, especially at contacts, cutouts and grips.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 1.2: Axial engineering strain and true strain

### Physical reasoning and derivation target

Engineering axial strain compares extension with an original gauge length, whereas logarithmic true strain integrates incremental changes in current length. At small strains they agree approximately; at larger uniform stretches their difference becomes important. Changing gauge length changes an averaged strain when deformation is localized, so the gauge definition belongs in every report.

**Governing relationship and applicability:** e=(L-L0)/L0, epsilon_true=ln(1+e) for homogeneous uniaxial extension. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Measure extension of an illustrative 50 mm gauge and calculate engineering strain and ln(L/L0) at two loads; compare them as necking begins.

A related local calculator for this lesson is **Elastic extension of a bar**. Use **Original bar length = 178.5714 mm** with the other parameters fixed. The illustrative model returns **0.071428571 mm**. Repeat the computation at **Original bar length = 250.5714 mm** to obtain **0.10022857 mm**; the output rises when the input rises. Record the expression and its model domain exactly: **F=8000 N, E=200000 MPa, A=100 mm², uniform small-strain linear elasticity**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A clip-on extensometer may miss strain outside its knife edges and a crosshead measurement includes machine compliance.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which gauge-independent observation marks the beginning of localized strain? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **178.5714 mm**, and recover **0.071428571 mm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A clip-on extensometer may miss strain outside its knife edges and a crosshead measurement includes machine compliance.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 1.3: Elastic constants and directional response

### Physical reasoning and derivation target

Young modulus relates uniaxial stress and elastic strain in a specified direction and regime. Shear modulus and bulk modulus describe different deformation modes. For an isotropic linear elastic solid E=2G(1+nu), but a textured crystal or laminate generally needs more independent stiffness coefficients. A scalar modulus does not establish anisotropic compliance.

**Governing relationship and applicability:** sigma=E epsilon, E=2G(1+nu) only for isotropic linear elasticity. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare two coupons cut parallel and transverse to a rolling direction; construct a small-load strain experiment with longitudinal and transverse gauges.

A related local calculator for this lesson is **Nominal tensile stress**. Use **Applied force = 19.85714 kN** with the other parameters fixed. The illustrative model returns **165.47619 MPa**. Repeat the computation at **Applied force = 26.89714 kN** to obtain **224.14286 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Initial section A0=120 mm²; engineering stress for centered uniaxial loading, no local concentration**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A straight stress–strain segment may contain fixture compliance and does not establish isotropy over all directions.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which off-axis test could falsify an isotropic model? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **19.85714 kN**, and recover **165.47619 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A straight stress–strain segment may contain fixture compliance and does not establish isotropy over all directions.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 1.4: Poisson effect and volumetric strain

### Physical reasoning and derivation target

Transverse contraction under uniaxial tension is summarized by a Poisson ratio only within a well-described elastic regime. For isotropic infinitesimal strain, volumetric strain is approximately the sum of the three normal strains. Auxetic microstructures can have negative effective Poisson ratios without contradicting thermodynamics if the full elastic stability conditions are respected.

**Governing relationship and applicability:** nu=-epsilon_trans/epsilon_axial, small strain convention. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Track axial and lateral optical marks on a polymer strip in a low-strain cycle and estimate nu from signed strain ratios.

A related local calculator for this lesson is **Elastic extension of a bar**. Use **Original bar length = 307.1429 mm** with the other parameters fixed. The illustrative model returns **0.12285714 mm**. Repeat the computation at **Original bar length = 379.1429 mm** to obtain **0.15165714 mm**; the output rises when the input rises. Record the expression and its model domain exactly: **F=8000 N, E=200000 MPa, A=100 mm², uniform small-strain linear elasticity**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Large deformation, near-incompressible response and strain-dependent modulus invalidate naive use of a constant small-strain Poisson ratio.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would lateral and longitudinal strain measurements diagnose the assumed elastic regime? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **307.1429 mm**, and recover **0.12285714 mm**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Large deformation, near-incompressible response and strain-dependent modulus invalidate naive use of a constant small-strain Poisson ratio.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 1.5: Elastic energy, compliance and unloading

### Physical reasoning and derivation target

Reversible linear elasticity stores strain energy density equal to the area under a loading curve. For a uniaxial Hookean material it is sigma²/(2E); a hysteresis loop represents dissipated mechanical work per volume when cyclic loading includes loss. Structural stiffness also depends on specimen dimensions and support conditions, not just a material's E.

**Governing relationship and applicability:** u=integral(sigma d epsilon)=sigma²/(2E) in one-dimensional linear elasticity. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Plot load–extension during three small cycles and compare the slopes and enclosed areas after correcting test-machine compliance.

A related local calculator for this lesson is **Nominal tensile stress**. Use **Applied force = 32.42857 kN** with the other parameters fixed. The illustrative model returns **270.2381 MPa**. Repeat the computation at **Applied force = 39.46857 kN** to obtain **328.90476 MPa**; the output rises when the input rises. Record the expression and its model domain exactly: **Initial section A0=120 mm²; engineering stress for centered uniaxial loading, no local concentration**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A nominally closed loop may arise from instrument drift, while a true loop does not identify a unique microscopic damping mechanism.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What control test separates actuator hysteresis from specimen dissipation? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **32.42857 kN**, and recover **270.2381 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A nominally closed loop may arise from instrument drift, while a true loop does not identify a unique microscopic damping mechanism.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Strain measurement under nominally uniform tension

### Scientific question and competing hypotheses

Two invented aluminum coupons have identical stress–strain curves if crosshead travel is treated as specimen extension; optical gauge readings show a different elastic slope. The task is to identify compliance contamination and report the observable with its correct gauge basis.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Build a load–extension data table and independently calculate stress, engineering strain, true strain during uniform deformation, transverse strain and elastic energy density. Fit the elastic slope only after examining residuals and gauge calibration.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Compare machine-travel versus optical-extension measurements at three load levels and repeat with a second gauge length. Inspect alignment with a bending-sensitive strain-gauge arrangement.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Mechanical properties inferred from actuator travel cannot be presented as specimen modulus unless the compliance and alignment assumptions have been tested.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_0 -->

<!-- MODEL_1 -->

