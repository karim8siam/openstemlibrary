# Unit 5: Cracks, fracture resistance and toughness

**Guiding question:** When does a flawed solid become unstable?

## Physical map and learning outcomes

A fictional structural plate has several mapped surface indications and a load estimate with substantial uncertainty. A simplified screening calculation uses one flaw size and a constant geometry factor. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Evaluate K for several flaw-size and stress combinations; use G=K²/E-prime only with the correct elastic assumptions. Sketch a growth resistance curve and discuss unstable crack extension. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 5.1: Crack-tip geometry and stress intensity

### Physical reasoning and derivation target

Near a sharp crack in a linear elastic body, the asymptotic stress field scales with K/sqrt(2 pi r), with angular dependence and distinct opening, sliding and tearing modes. A geometry factor Y modifies K=Y sigma sqrt(pi a). The singularity describes an ideal continuum limit, not unlimited physical stress at atomic distances.

**Governing relationship and applicability:** mode I K_I=Y sigma sqrt(pi a) for specified geometry. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare two fictional plates with identical remote stress but different crack lengths, avoiding the edge of a finite-width correction's validity range.

A related local calculator for this lesson is **Mode I stress-intensity estimate**. Use **Crack depth = 0.8857143 mm** with the other parameters fixed. The illustrative model returns **5.9079904 MPa√m**. Repeat the computation at **Crack depth = 1.653714 mm** to obtain **8.0727815 MPa√m**; the output rises when the input rises. Record the expression and its model domain exactly: **Y=1.12 fixed illustrative geometry, remote tensile stress=100 MPa, LEFM assumptions**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Plasticity, finite geometry, residual stress and uncertain flaw shape can invalidate a constant-Y LEFM calculation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What independent flaw-sizing method would bound error in K? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **0.8857143 mm**, and recover **5.9079904 MPa√m**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Plasticity, finite geometry, residual stress and uncertain flaw shape can invalidate a constant-Y LEFM calculation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 5.2: Griffith energy balance and G

### Physical reasoning and derivation target

A crack advances when the available release of elastic potential energy makes growth energetically possible and other conditions are met. For isotropic linear elasticity a relation G=K²/E' links energy release to stress intensity, with plane-stress or plane-strain modulus convention. A fracture toughness reported without thickness and specimen conditions may not be transferable.

**Governing relationship and applicability:** G=K_I²/E' in linear elastic mode I with the correct constraint modulus. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Use a hypothetical plate to evaluate how G scales when remote stress is doubled at fixed crack length.

A related local calculator for this lesson is **Elastic energy release rate**. Use **Mode I stress intensity = 10.71429 MPa√m** with the other parameters fixed. The illustrative model returns **521.79963 J/m²**. Repeat the computation at **Mode I stress intensity = 16.15429 MPa√m** to obtain **1186.1861 J/m²**; the output rises when the input rises. Record the expression and its model domain exactly: **Plane-strain E-prime=220000 MPa; G=K²/E-prime, ideal isotropic linear elastic fracture**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Surface energy alone does not represent ductile dissipation, crack bridging or process-zone energy in tough materials.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which measured load–displacement quantity can independently estimate energy release? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **10.71429 MPa√m**, and recover **521.79963 J/m²**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Surface energy alone does not represent ductile dissipation, crack bridging or process-zone energy in tough materials.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 5.3: Plastic zone and fracture-process zone

### Physical reasoning and derivation target

Small-scale yielding permits an outer elastic K field while a near-tip region undergoes plastic deformation. Plane stress and plane strain produce different plastic-zone approximations and toughness behavior. Fracture process zones in polymers, concrete and ceramics may include crazes, microcracks or bridging instead of metal-like dislocation flow.

**Governing relationship and applicability:** r_p proportional to (K/sigma_y)² with convention-dependent prefactor. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare an illustrative plastic zone estimate for identical K and yield strength under two ideal constraints.

A related local calculator for this lesson is **Mode I stress-intensity estimate**. Use **Crack depth = 2.257143 mm** with the other parameters fixed. The illustrative model returns **9.43132 MPa√m**. Repeat the computation at **Crack depth = 3.025143 mm** to obtain **10.918574 MPa√m**; the output rises when the input rises. Record the expression and its model domain exactly: **Y=1.12 fixed illustrative geometry, remote tensile stress=100 MPa, LEFM assumptions**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A small numerical estimate does not prove the test specimen satisfies all relevant size and constraint requirements.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would specimen thickness alter a measured crack resistance curve? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **2.257143 mm**, and recover **9.43132 MPa√m**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A small numerical estimate does not prove the test specimen satisfies all relevant size and constraint requirements.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 5.4: R-curves and stable crack extension

### Physical reasoning and derivation target

Some materials display increasing crack resistance as a crack grows due to bridging, plasticity or microstructural shielding. The applied driving-force curve and resistance curve determine stable versus unstable extensions in a given geometry. A one-number initiation toughness cannot describe the entire trajectory when an R-curve is pronounced.

**Governing relationship and applicability:** crack growth condition G_applied >= R(a), stability based on slope comparison. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Sketch applied G(a) and R(a) for a fictional toughened ceramic, marking possible stable intersection and tangent instability.

A related local calculator for this lesson is **Elastic energy release rate**. Use **Mode I stress intensity = 20.42857 MPa√m** with the other parameters fixed. The illustrative model returns **1896.9388 J/m²**. Repeat the computation at **Mode I stress intensity = 25.86857 MPa√m** to obtain **3041.7409 J/m²**; the output rises when the input rises. Record the expression and its model domain exactly: **Plane-strain E-prime=220000 MPa; G=K²/E-prime, ideal isotropic linear elastic fracture**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Machine stiffness and specimen geometry influence stability; a visually steep curve cannot be classified without energy accounting.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which unloading-compliance measurement could estimate incremental crack length? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **20.42857 MPa√m**, and recover **1896.9388 J/m²**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Machine stiffness and specimen geometry influence stability; a visually steep curve cannot be classified without energy accounting.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 5.5: Fractography and failure reconstruction

### Physical reasoning and derivation target

Fracture surfaces preserve evidence of crack origin, propagation direction and final overload, but morphological features depend on material, mode and environment. A valid root-cause investigation connects fractography with loads, flaw population, manufacturing history and chemistry rather than assigning a cause from one micrograph.

**Governing relationship and applicability:** fracture inference requires multiple independent indicators and uncertainty statements. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Plan a blind comparison of two failed fasteners, one with fatigue initiation and one with a single overload, using complementary records.

A related local calculator for this lesson is **Mode I stress-intensity estimate**. Use **Crack depth = 3.628571 mm** with the other parameters fixed. The illustrative model returns **11.958062 MPa√m**. Repeat the computation at **Crack depth = 4.396571 mm** to obtain **13.162853 MPa√m**; the output rises when the input rises. Record the expression and its model domain exactly: **Y=1.12 fixed illustrative geometry, remote tensile stress=100 MPa, LEFM assumptions**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Corrosion, rubbing after failure and handling contamination can obscure fracture markings; visual appearance alone is insufficient proof.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What chain-of-custody and load-history evidence would strengthen a causation claim? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **3.628571 mm**, and recover **11.958062 MPa√m**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Corrosion, rubbing after failure and handling contamination can obscure fracture markings; visual appearance alone is insufficient proof.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Fracture driving force in a flawed plate

### Scientific question and competing hypotheses

A fictional structural plate has several mapped surface indications and a load estimate with substantial uncertainty. A simplified screening calculation uses one flaw size and a constant geometry factor.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Evaluate K for several flaw-size and stress combinations; use G=K²/E-prime only with the correct elastic assumptions. Sketch a growth resistance curve and discuss unstable crack extension.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Acquire nondestructive flaw-sizing measurements with uncertainty bounds and confirm fracture mode and thickness constraints. Compare an independent toughness specimen.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Crack growth prediction is sensitive to residual stress, three-dimensional flaw shape, constraints and subcritical environmental effects.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_8 -->

<!-- MODEL_9 -->

