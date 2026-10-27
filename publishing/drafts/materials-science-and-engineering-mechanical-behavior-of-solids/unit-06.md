# Unit 6: Fatigue, damage accumulation and durability

**Guiding question:** Why can components fail under repeated loads below monotonic strength?

## Physical map and learning outcomes

An imagined drive bracket experiences daytime start-stop peaks and long periods of vibration. A simplistic Miner estimate uses a single S–N curve from polished laboratory coupons. This fictional situation will be revisited in the integrated project. Start by distinguishing direct observations from physical descriptions and from parameters that a mathematical model proposes to infer. Write a list of controlled quantities, including applied load or displacement, specimen temperature, fixture constraints and the observation interval. Do not assume that a smooth stress–strain curve establishes homogeneous deformation or excludes hidden failure mechanisms.

Reconstruct stress cycles, calculate amplitude and R, test a two-level nominal Miner sum and compare with an approximate Paris-law crack-growth interval. The mathematics provides a disciplined way to compare outcomes but still depends on geometry, load history and the meaning of stress and strain. Across the five lessons, students should practice setting up a concrete force or energy balance, evaluating at least one numerical scale, and proposing a measurement that would discriminate among mechanisms. A complete argument identifies what a result cannot establish, even when a plotted trend agrees with an intuitive expectation.

## Units and model limits

For each lesson decide whether its quantity is a force, pressure, strain, fracture driving force, cycle count, time-dependent rate, geometric length or dimensionless survival probability. A second unit conversion must be reproducible from the first. Distinguish pascal and megapascal, newtons and kilonewtons, meters and millimeters, and engineering and logarithmic strain. Scaling mistakes can change component predictions by many orders of magnitude.

## Lesson 6.1: Stress amplitude, mean stress and load ratio

### Physical reasoning and derivation target

An imposed cyclic history is defined by its maximum, minimum, mean and amplitude, with stress ratio R=sigma_min/sigma_max. Two cycles with identical amplitude but different mean stress can produce different fatigue response, especially when the crack remains open for differing portions of each cycle.

**Governing relationship and applicability:** sigma_a=(sigma_max-sigma_min)/2, sigma_m=(sigma_max+sigma_min)/2. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compute cycle descriptors for fully reversed and pulsating tensile loads using a clearly specified sign convention.

A related local calculator for this lesson is **Paris crack-growth rate**. Use **Stress intensity range = 7.428571 MPa√m** with the other parameters fixed. The illustrative model returns **4.0993586 nm/cycle**. Repeat the computation at **Stress intensity range = 13.50857 MPa√m** to obtain **24.650644 nm/cycle**; the output rises when the input rises. Record the expression and its model domain exactly: **Synthetic C=10⁻¹¹ m/cycle/(MPa√m)³ and m=3; intermediate Paris regime only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Local plastic strain and residual stress can make nominal elastic cycle descriptors inadequate for a notch root.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** How would a recorded strain loop differ between elastic and plastically cycling specimens? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **7.428571 MPa√m**, and recover **4.0993586 nm/cycle**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Local plastic strain and residual stress can make nominal elastic cycle descriptors inadequate for a notch root.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 6.2: S–N curves and fatigue limits

### Physical reasoning and derivation target

An S–N representation relates stress amplitude or range to cycles-to-failure for specified loading, environment, geometry and survival conditions. Some alloys exhibit an approximate endurance region while others do not show a true horizontal asymptote. Scatter and right-censored runouts require statistical treatment.

**Governing relationship and applicability:** Basquin-type sigma_a=sigma_f' (2N_f)^b only in suitable fitted range. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Design a fictional constant-amplitude fatigue test matrix with multiple specimens per stress level and runout criterion.

A related local calculator for this lesson is **Plastic strain-life amplitude**. Use **Cycles to failure = 28928.57 cycles** with the other parameters fixed. The illustrative model returns **0.084095296 percent**. Repeat the computation at **Cycles to failure = 44848.57 cycles** to obtain **0.066075401 percent**; the output falls when the input rises. Record the expression and its model domain exactly: **Coffin–Manson plastic term with epsilon_f prime=0.35 and c=-0.55; not total strain-life law**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

An unreported survival percentile or coupon finish makes a single S–N curve unsafe for design extrapolation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What data are required to report confidence in a design-life estimate? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **28928.57 cycles**, and recover **0.084095296 percent**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **An unreported survival percentile or coupon finish makes a single S–N curve unsafe for design extrapolation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 6.3: Strain-life and cyclic plasticity

### Physical reasoning and derivation target

Low-cycle fatigue often needs a strain-based description since plastic strain is not negligible at the critical site. The Coffin–Manson relation gives a power-law approximation for plastic strain amplitude and reversals to failure, combined with an elastic Basquin term when appropriate. Stabilized hysteresis parameters must be defined.

**Governing relationship and applicability:** epsilon_a≈sigma_f'/E (2N_f)^b+epsilon_f' (2N_f)^c with fitted regime. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare two fictional materials with different fatigue ductility coefficients under matched plastic strain amplitude.

A related local calculator for this lesson is **Paris crack-growth rate**. Use **Stress intensity range = 18.28571 MPa√m** with the other parameters fixed. The illustrative model returns **61.141458 nm/cycle**. Repeat the computation at **Stress intensity range = 24.36571 MPa√m** to obtain **144.65633 nm/cycle**; the output rises when the input rises. Record the expression and its model domain exactly: **Synthetic C=10⁻¹¹ m/cycle/(MPa√m)³ and m=3; intermediate Paris regime only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

Cyclic softening, nonproportional loading and thermal transients may invalidate fixed-parameter strain-life extrapolation.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What cyclic loop measurements are needed to identify the fitted parameters? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **18.28571 MPa√m**, and recover **61.141458 nm/cycle**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **Cyclic softening, nonproportional loading and thermal transients may invalidate fixed-parameter strain-life extrapolation.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 6.4: Long crack propagation and Paris relation

### Physical reasoning and derivation target

When linear elastic fracture mechanics is applicable, intermediate-regime fatigue crack growth may be summarized by da/dN=C(Delta K)^m. Near-threshold and near-instability regimes lie outside the basic Paris window. Stress ratio, environment, crack closure and plasticity can shift apparent coefficients.

**Governing relationship and applicability:** da/dN=C(Delta K)^m, empirical mode-I interval. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Fit a log-log slope from synthetic da/dN data and estimate cycles for a discrete sequence of crack lengths under fixed nominal loading.

A related local calculator for this lesson is **Plastic strain-life amplitude**. Use **Cycles to failure = 57357.14 cycles** with the other parameters fixed. The illustrative model returns **0.057713633 percent**. Repeat the computation at **Cycles to failure = 73277.14 cycles** to obtain **0.050439277 percent**; the output falls when the input rises. Record the expression and its model domain exactly: **Coffin–Manson plastic term with epsilon_f prime=0.35 and c=-0.55; not total strain-life law**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

A Paris law calibrated for one stress ratio cannot be transferred blindly to variable amplitude or corrosion fatigue.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** Which growth-rate data would expose deviation near threshold? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **57357.14 cycles**, and recover **0.057713633 percent**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **A Paris law calibrated for one stress ratio cannot be transferred blindly to variable amplitude or corrosion fatigue.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Lesson 6.5: Sequence effects and Miner damage

### Physical reasoning and derivation target

A linear damage sum D=sum(n_i/N_i) offers a simple bookkeeping estimate for multilevel cyclic histories but assumes no sequence interaction. Overloads can retard or accelerate subsequent crack growth, and local damage may include residual stresses and plasticity that vary through the history.

**Governing relationship and applicability:** Palmgren–Miner D=sum n_i/N_i under a particular fatigue assessment approximation. This relationship provides a starting point only; identify each symbol's units and the regime in which its derivation applies.

### Laboratory thought experiment and numerical calculation

Compare high-low and low-high loading sequences with the same nominal Miner sum and predict why failures may differ.

A related local calculator for this lesson is **Paris crack-growth rate**. Use **Stress intensity range = 29.14286 MPa√m** with the other parameters fixed. The illustrative model returns **247.51207 nm/cycle**. Repeat the computation at **Stress intensity range = 35.22286 MPa√m** to obtain **436.99226 nm/cycle**; the output rises when the input rises. Record the expression and its model domain exactly: **Synthetic C=10⁻¹¹ m/cycle/(MPa√m)³ and m=3; intermediate Paris regime only**. These results are **synthetic arithmetic**, not measured coefficients or validated engineering values. If the output is stress, express the pressure dimensions and define the section; if it is a load, check the corresponding support and safety domain. If it represents strain, identify engineering versus true strain and keep it dimensionless. If it is a lifetime, creep rate or crack-growth rate, name the loading and calibration domain before comparison. If it represents a survival probability, verify it lies between zero and one.

### Competing explanations and experimental controls

The condition D=1 is a heuristic in many contexts, not a universal thermodynamic failure law.

### Model-to-measurement translation

### Solved reasoning audit and assessment

**Reasoning exercise.** What randomized load-spectrum experiment tests the sequence-independent assumption? Begin with the force balance, constitutive law and appropriate support conditions. Show the expression corresponding to the local calculator, substitute **29.14286 MPa√m**, and recover **247.51207 nm/cycle**. Explain the sign and the units. Then predict the changed output at the second input before using the model. If the sensitivity is small, discuss whether real experimental resolution could distinguish the cases. If it is large, specify a practical uncertainty bound for the input and ask whether that uncertainty dominates the inferred output.

**Instructor check.** A satisfactory answer must distinguish this lesson's physical claim from a convenient mathematical approximation, and it must confront the alternative mechanism: **The condition D=1 is a heuristic in many contexts, not a universal thermodynamic failure law.**. The submitted method should include one independent measurement, one falsification criterion, and a concise statement of what the result would *not* permit the engineer to conclude. Numerical correctness alone is insufficient when the wrong strain measure, a physically impossible structural boundary, or an inappropriate strength or stiffness was chosen.

## Integrated investigation: Fatigue under mixed duty cycles

### Scientific question and competing hypotheses

An imagined drive bracket experiences daytime start-stop peaks and long periods of vibration. A simplistic Miner estimate uses a single S–N curve from polished laboratory coupons.

Frame two hypotheses that predict distinguishable observations rather than two labels for the same curve. One may ascribe the response to intrinsic material deformation; the other may emphasize geometry, microstructure, contact conditions or evolving damage. For each hypothesis identify what must remain fixed when comparing specimens. Define a primary observable with units and measurement precision, then propose a negative control and a distinct hold-out test. The fabricated dataset in this book can support method practice only; it cannot adjudicate real mechanisms.

### Mathematical program and result interpretation

Reconstruct stress cycles, calculate amplitude and R, test a two-level nominal Miner sum and compare with an approximate Paris-law crack-growth interval.

Begin with force and moment equilibrium, the displacement or strain field, and a constitutive relationship. State whether small strains, isotropy, smooth geometry, elastic loading and constant temperature are supported by observations or imposed assumptions. Compare the loading time with characteristic relaxation or damage time only when relevant. Derive the support and contact boundary conditions from the proposed fixture, not from a diagram chosen for convenience. If a numerical model is selected, report the solution scheme and a convergence tolerance; if an analytic approximation is used, report the time and geometry window in which it applies.

Use both illustrative models in this unit to create sensitivity plots. Vary one input at a time, translate plotted outputs into coherent dimensional statements, and explain how a different trend would appear if the competing hypothesis were true. Where a model predicts local stress, do not replace it with a coupon strength without examining defect sensitivity and constraint. Where it represents a probability or failure life, identify the flaw population and load spectrum, and never extrapolate a fit across a mechanism transition without evidence.

### Experimental design and quality controls

Record actual load spectra and surface condition, perform runout-aware replicate fatigue tests and inspect initiation locations; include a changed sequence as control.

Plan a sequence with specimen preparation, before-treatment measurement, treatment logging, after-treatment measurement and a repeated control. For each measurement record resolution, calibration, location on the specimen, loading history and a plausible systematic uncertainty. Use more than one load level and at least one geometry or processing perturbation so a mechanism can be distinguished from a single endpoint. A blind second observer should be able to reconstruct the processing history and recalculate the central result from raw data without relying on an author's narrative.

### Limitations, risks and defensible conclusions

A smooth cumulative damage number is not evidence that overload retardation, corrosion or notch-local plasticity was represented.

Suppose a fitted synthetic stress–strain or lifetime curve passes through all plotted points. That demonstrates arithmetic compatibility with a chosen model but does not prove a dislocation mechanism, reliable fracture performance or safety outside the fitted stress, temperature and environment range. A persuasive engineering recommendation should specify the material's composition and processing history, uncertainty in constitutive parameters, competing damage mechanisms, anticipated operating range, and the data that would reverse the decision.

### Capstone deliverables

1. A force balance or energy balance with sign conventions, dimensions and geometry.
2. An independently reproducible numerical calculation from a specified initial value.
3. A synthetic stress, strain, crack-growth or time-series graph labelled as illustrative, with assumptions.
4. A one-page experimental design including at least two independent controls and two time points.
5. A failure analysis naming a competing mechanism and an observation that would favor it.
6. A conclusion separating the mathematical demonstration from unverified real material strength and component reliability.

### Interactive demonstrations

<!-- MODEL_10 -->

<!-- MODEL_11 -->

