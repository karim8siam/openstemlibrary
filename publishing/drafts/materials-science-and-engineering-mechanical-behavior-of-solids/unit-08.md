# Unit 8: Testing, uncertainty and engineering decisions

**Guiding question:** How can a defensible material selection be made from imperfect measurements?

## Physical map and learning outcomes

A notional safety-critical component has candidate metal, polymer and ceramic options. Each has an attractive laboratory property and a critical missing datum, including fatigue uncertainty, time dependence or flaw statistics. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Create a decision matrix using stiffness, strength, reliability, manufacturability and uncertainty. Demonstrate that missing evidence can dominate a small predicted performance advantage. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 8.1: Tensile test standards and traceability

### Physical reasoning and derivation target

A tensile test report needs specimen geometry, material orientation, preparation, loading rate, strain measurement and machine calibration. Reproducibility requires traceability of the load cell and extensometer and attention to alignment. A compliance correction can move the apparent initial modulus substantially.

**Governing relationship and applicability:** force/displacement to engineering stress/strain requires original area and gauge length. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Audit a fictional tensile CSV with force, crosshead position and optical gauge markers before selecting a fit interval.

A related local calculator for this lesson is **Illustrative Vickers hardness**. Use **Average imprint diagonal = 0.3 mm** with the other parameters fixed. The illustrative model returns **20.6119 HV**. Repeat the computation at **Average imprint diagonal = 0.468 mm** to obtain **8.4697156 HV**; the output falls when the input rises. Record the expression and its model domain exactly: **Load=9.81 N, ideal diamond indentation relation; hardness number only, no tensile strength conversion**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Crosshead displacement includes fixture deformation; calling its slope Young modulus without correction is misleading.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What metadata enable another lab to reconstruct the stated proof stress? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **0.3 mm**, and recover **20.6119 HV**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Crosshead displacement includes fixture deformation; calling its slope Young modulus without correction is misleading.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 8.2: Indentation hardness and contact

### Physical reasoning and derivation target

Indentation tests infer a response from an imprint geometry or load–depth trace, which reflects plasticity, elasticity, pile-up or sink-in, and surface preparation. For Vickers hardness, a standardized geometric relation converts applied force and diagonal length to hardness number. Hardness is not a universal direct surrogate for tensile strength or wear resistance.

**Governing relationship and applicability:** HV≈0.1891 F(N)/d(mm)^2 in standard SI-compatible numerical convention. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare two fictional imprints at equal applied load but different diagonal lengths, with microscopy scale calibration.

A related local calculator for this lesson is **Weibull survival probability**. Use **Applied tensile stress = 100 MPa** with the other parameters fixed. The illustrative model returns **0.97102682 probability**. Repeat the computation at **Applied tensile stress = 144.8 MPa** to obtain **0.76261314 probability**; the output falls when the input rises. Record the expression and its model domain exactly: **Hypothetical m=6, scale=180 MPa, fixed geometry and flaw population; not structural certification**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Thin coatings, substrate influence and residual stress can alter apparent hardness; conversion across material families is unreliable.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which cross-sectional measurement would reveal substrate influence? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **100 MPa**, and recover **0.97102682 probability**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Thin coatings, substrate influence and residual stress can alter apparent hardness; conversion across material families is unreliable.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 8.3: Full-field displacement and digital image correlation

### Physical reasoning and derivation target

Digital image correlation tracks pattern motion across image sequences, converting displacement to spatial strain after camera calibration and smoothing. Gauge size, correlation subset and differentiation amplify different uncertainties. A colorful contour plot is not a quantitative strain measurement unless the optical method is validated.

**Governing relationship and applicability:** strain derives from spatial gradients of a calibrated displacement field. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare a synthetic homogeneous-strain image pair with one containing a localized band using two subset sizes.

A related local calculator for this lesson is **Illustrative Vickers hardness**. Use **Average imprint diagonal = 0.6 mm** with the other parameters fixed. The illustrative model returns **5.152975 HV**. Repeat the computation at **Average imprint diagonal = 0.768 mm** to obtain **3.1451263 HV**; the output falls when the input rises. Record the expression and its model domain exactly: **Load=9.81 N, ideal diamond indentation relation; hardness number only, no tensile strength conversion**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Lighting, out-of-plane motion and poor pattern contrast may create false local hotspots.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which rigid-body-motion control would detect apparent strain from camera movement? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **0.6 mm**, and recover **5.152975 HV**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Lighting, out-of-plane motion and poor pattern contrast may create false local hotspots.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 8.4: Weibull variability for brittle fracture

### Physical reasoning and derivation target

Brittle failure is often governed by a population of flaws, making specimen volume, surface finish and loading geometry relevant to strength variability. A two-parameter Weibull survival expression may summarize hypothetical data, but its shape and scale must be fitted for a specified specimen population and effective stressed volume. It is not a universal material constant.

**Governing relationship and applicability:** P_survival=exp[-(sigma/sigma0)^m] in a fixed reference population. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Plot survival probability for a fictional ceramic under changing tensile stress and compare two invented Weibull moduli.

A related local calculator for this lesson is **Weibull survival probability**. Use **Applied tensile stress = 180 MPa** with the other parameters fixed. The illustrative model returns **0.36787944 probability**. Repeat the computation at **Applied tensile stress = 224.8 MPa** to obtain **0.022496459 probability**; the output falls when the input rises. Record the expression and its model domain exactly: **Hypothetical m=6, scale=180 MPa, fixed geometry and flaw population; not structural certification**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Independent identically distributed flaw assumptions can fail when defects cluster or the population changes across manufacturing batches.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which censored dataset and specimen-size study are needed before extrapolating survival? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **180 MPa**, and recover **0.36787944 probability**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Independent identically distributed flaw assumptions can fail when defects cluster or the population changes across manufacturing batches.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 8.5: Design allowables, selection and ethical reporting

### Physical reasoning and derivation target

A component decision combines mechanical tests with load spectra, inspection limits, manufacturing tolerances, operating environment, cost and consequences of failure. A factor of safety cannot substitute for an unknown defect distribution or unverified model regime. Design allowables are statistical, configuration-specific quantities rather than a chosen textbook strength divided by a convenient number.

**Governing relationship and applicability:** explicit constraints, uncertainty propagation and documented testing for the actual service case. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare fictional alloy, polymer and ceramic selections for a load-carrying bracket with competing stiffness, fatigue and service-temperature requirements.

A related local calculator for this lesson is **Illustrative Vickers hardness**. Use **Average imprint diagonal = 0.9 mm** with the other parameters fixed. The illustrative model returns **2.2902111 HV**. Repeat the computation at **Average imprint diagonal = 1.068 mm** to obtain **1.626365 HV**; the output falls when the input rises. Record the expression and its model domain exactly: **Load=9.81 N, ideal diamond indentation relation; hardness number only, no tensile strength conversion**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Overconfident precision or unreported missing tests can turn a pedagogical model into an unsafe manufacturing claim.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which additional measurement most reduces decision uncertainty before selecting the material? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **0.9 mm**, and recover **2.2902111 HV**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Overconfident precision or unreported missing tests can turn a pedagogical model into an unsafe manufacturing claim.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Choosing a material with an evidence ledger

### Scientific question and competing hypotheses

A notional safety-critical component has candidate metal, polymer and ceramic options. Each has an attractive laboratory property and a critical missing datum, including fatigue uncertainty, time dependence or flaw statistics.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Create a decision matrix using stiffness, strength, reliability, manufacturability and uncertainty. Demonstrate that missing evidence can dominate a small predicted performance advantage.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Require calibrated mechanical tests, batch traceability, inspection sensitivity, validated service spectra and an independent review of design allowables.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

The textbook models and synthetic datasets are educational exercises, not qualification data or permission to release a safety-critical product.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_14 -->

<!-- MODEL_15 -->

