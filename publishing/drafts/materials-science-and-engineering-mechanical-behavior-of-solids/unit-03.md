# Unit 3: Dislocations, crystals and deformation microstructures

**Guiding question:** How do crystal defects produce macroscopic strength?

## Physical map and learning outcomes

Two hypothetical steels have equal nominal chemistry but distinct grain sizes, textures and dislocation densities. A Hall–Petch fit gives an apparently excellent line even though changes in heat treatment also alter precipitation. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Compute predicted grain-size strengthening from a limited-range fit and resolved shear from a crystal orientation; draw causal pathways linking processing, microstructure, deformation and strength. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 3.1: Slip systems and resolved shear

### Physical reasoning and derivation target

In a single crystal the applied stress resolves onto particular slip directions and planes. Schmid factor m=cos phi cos lambda predicts the resolved shear component for a simple uniaxial state. Multiple slip, grain constraints and non-Schmid effects can alter activation, so the maximum m is only part of a predictive crystal plasticity model.

**Governing relationship and applicability:** tau_RSS=sigma cos(phi) cos(lambda) for uniaxial loading. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Rotate a synthetic single crystal relative to the tensile direction while keeping the load magnitude constant and rank candidate systems.

A related local calculator for this lesson is **Resolved shear stress**. Use **Angle to slip-plane normal = 16.42857 degrees** with the other parameters fixed. The illustrative model returns **203.47133 MPa**. Repeat the computation at **Angle to slip-plane normal = 29.22857 degrees** to obtain **185.12311 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **Uniaxial stress=300 MPa, slip direction angle lambda=45 degrees; Schmid-law geometry only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A slip trace does not uniquely identify Burgers vector or slip direction without crystallographic orientation data.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What diffraction measurement would identify which slip system was active? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **16.42857 degrees**, and recover **203.47133 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A slip trace does not uniquely identify Burgers vector or slip direction without crystallographic orientation data.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 3.2: Line defects, Burgers vectors and mobility

### Physical reasoning and derivation target

An edge or screw dislocation carries a Burgers vector characterizing the lattice mismatch around the line. Glide and climb transport defects through distinct mechanisms; climb generally requires diffusion-mediated point-defect exchange. The Peierls barrier and obstacles contribute to resistance but are sensitive to core structure and temperature.

**Governing relationship and applicability:** plastic shear gamma approximately rho_m b v t under constant mobile dislocation density and speed. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Use a slip-plane sketch to follow how one dislocation passage changes surface shape without translating every atom across the sample length.

A related local calculator for this lesson is **Hall–Petch proof stress**. Use **Mean grain diameter = 35.71429 μm** with the other parameters fixed. The illustrative model returns **208.7658 MPa**. Repeat the computation at **Mean grain diameter = 54.59429 μm** to obtain **187.97105 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **sigma0=100 MPa and k=0.65 MPa sqrt(m), illustrative limited-range grain strengthening**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Real dislocation lines are curved, interact and cross-slip; a line drawing does not yield a quantitative mobility law.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What microscopic image sequence would distinguish line glide from dislocation source multiplication? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **35.71429 μm**, and recover **208.7658 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Real dislocation lines are curved, interact and cross-slip; a line drawing does not yield a quantitative mobility law.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 3.3: Grain boundaries and strengthening

### Physical reasoning and derivation target

Grain boundaries impede some forms of dislocation transmission, so many polycrystalline metals exhibit an approximate Hall–Petch relation across a constrained grain-size range. The intercept and slope depend on composition, texture, rate and measurement convention. A single apparent inverse-square-root fit should not be extrapolated to nanoscale grains without new evidence.

**Governing relationship and applicability:** sigma_y=sigma_0+k_y d^(-1/2) over an identified domain. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare several invented annealed samples with controlled grain-size distributions, holding composition and texture as consistent as possible.

A related local calculator for this lesson is **Resolved shear stress**. Use **Angle to slip-plane normal = 39.28571 degrees** with the other parameters fixed. The illustrative model returns **164.18979 MPa**. Repeat the computation at **Angle to slip-plane normal = 52.08571 degrees** to obtain **130.3513 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **Uniaxial stress=300 MPa, slip direction angle lambda=45 degrees; Schmid-law geometry only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Precipitate changes and residual stress can correlate with grain size and create a misleading strengthening trend.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would a matched-heat-treatment control separate grain effects from precipitation effects? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **39.28571 degrees**, and recover **164.18979 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Precipitate changes and residual stress can correlate with grain size and create a misleading strengthening trend.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 3.4: Forest strengthening and dislocation density

### Physical reasoning and derivation target

Moving dislocations interact with forest dislocations; an illustrative Taylor relation links flow stress increment to G b sqrt(rho). Because density measures and interaction coefficients are uncertain, the relation is best used for scaling and interpretation. Recovery changes dislocation arrangement, so total density and mobile density need not respond identically.

**Governing relationship and applicability:** delta sigma≈alpha M G b sqrt(rho), illustrative average polycrystal model. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Estimate the strength ratio for fictional specimens differing fourfold in dislocation density while keeping G and b fixed.

A related local calculator for this lesson is **Hall–Petch proof stress**. Use **Mean grain diameter = 69.42857 μm** with the other parameters fixed. The illustrative model returns **178.00892 MPa**. Repeat the computation at **Mean grain diameter = 88.30857 μm** to obtain **169.16907 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **sigma0=100 MPa and k=0.65 MPa sqrt(m), illustrative limited-range grain strengthening**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Diffraction line broadening mixes crystallite size, microstrain and instrument broadening unless independently deconvolved.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What microscopy or diffraction cross-check would bound a dislocation-density estimate? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **69.42857 μm**, and recover **178.00892 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Diffraction line broadening mixes crystallite size, microstrain and instrument broadening unless independently deconvolved.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 3.5: Twins, transformations and texture

### Physical reasoning and derivation target

Mechanical twins reorient lattice regions through a coordinated shear, while martensitic transformations change crystal structures or variants by cooperative displacements. Their activation depends on stress, temperature and orientation, and both can interact with dislocation slip. Texture makes the aggregate response direction dependent.

**Governing relationship and applicability:** crystallographic compatibility and Schmid-type orientation arguments; model validity phase-dependent. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare stress–strain and orientation maps from samples strained along different directions in a strongly textured alloy.

A related local calculator for this lesson is **Resolved shear stress**. Use **Angle to slip-plane normal = 62.14286 degrees** with the other parameters fixed. The illustrative model returns **99.122645 MPa**. Repeat the computation at **Angle to slip-plane normal = 74.94286 degrees** to obtain **55.10814 MPa**; the output falls when the input rises. Record the expression and its model domain exactly: **Uniaxial stress=300 MPa, slip direction angle lambda=45 degrees; Schmid-law geometry only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Observing a banded contrast feature is not proof of twinning; slip bands and phase boundaries can look similar.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which before/after orientation relationship supports a twin interpretation? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **62.14286 degrees**, and recover **99.122645 MPa**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Observing a banded contrast feature is not proof of twinning; slip bands and phase boundaries can look similar.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Strengthening from microstructure

### Scientific question and competing hypotheses

Two hypothetical steels have equal nominal chemistry but distinct grain sizes, textures and dislocation densities. A Hall–Petch fit gives an apparently excellent line even though changes in heat treatment also alter precipitation.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Compute predicted grain-size strengthening from a limited-range fit and resolved shear from a crystal orientation; draw causal pathways linking processing, microstructure, deformation and strength.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Collect quantitative grain-size distributions, EBSD orientation data and microstructure controls. Perform a matched composition/aging experiment and use microscopy evidence of active slip.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

Correlation among microstructural features prevents unique mechanism attribution from a strength–grain size regression alone.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_4 -->

<!-- MODEL_5 -->

