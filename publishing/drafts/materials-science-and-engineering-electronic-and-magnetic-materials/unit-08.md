# Unit 8: Measurement, reproducibility and engineering decisions

**Guiding research question:** What measurements and uncertainty budgets justify a real electronic or magnetic material choice?

## Physical context and experimental objectives

Measurement defines the meaning of magnetic and dielectric property tables. Geometry correction, fixture calibration, temperature stabilization and uncertainty are parts of materials science, not clerical afterthoughts.

Device qualification requires representative samples and drift monitoring; the best-fitting synthetic curve only demonstrates that software implements a selected equation.

The five lessons in this unit emphasize **metrology, uncertainty and component design**. A central challenge is separating **formula parameter versus reliably measured device property**, because both may appear as a single output on an instrument display. Before interpreting response, establish **traceability, geometry, sweep conditions and independent fabrication**. The most important rival explanation is **field distortion, calibration drift and device aging**; an efficient validation strategy incorporates **reference standards, paired replicates and accelerated stress** from the outset. These distinctions prevent a successful curve fit from being mistaken for an independent explanation of microscopic mechanism.

## Before you calculate

## Unit map

## Lesson 8.1: B–H measurements and demagnetizing corrections

### Microscopic picture and applicable constitutive law

Magnetic material characterization may report B–H loops, M–H loops, susceptibility and remanent magnetic moment, which are related but not interchangeable. A long solenoid establishes a nominal magnetizing H from turns per length and current in an ideal limit, while pickup coils measure flux changes. Sample geometry, incomplete flux closure, gap fields and winding errors bias inferred permeability and loss. Always document whether reported H is externally applied or internally corrected.

**Primary relationship.** For a long coil H≈NI/ℓ; for magnetic material B=μ0(H+M). This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **b–h measurements and demagnetizing corrections**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A sample measured in a vibrating-sample magnetometer seems to saturate at a lower field than in a closed toroid. Estimate demagnetization and compare measurement definitions before naming a material transition.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetizing field in a test solenoid** as an exercise in numerical reasoning. Its controllable variable is **Coil current**; all other quantities follow fixed assumptions. Set **Coil current = 1.1888889 A**. With the implemented expression `200*I/0.5`, the output is **475.555556 A/m**. Increase the control to **1.7333333 A**. The new output is **693.333333 A/m**. Thus the model output increases over this interval, with secant slope **400 (A/m)/(A)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Long-solenoid approximation N=200, magnetic path length=0.5 m; result is H, not B, and ignores demagnetization. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

The simple NI/ℓ formula is a nominal excitation field and should not be treated as an exact internal field.

### Counterfactual and model criticism

Suppose a measurement appears to support **b–h measurements and demagnetizing corrections**, but **field distortion, calibration drift and device aging** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **reference standards, paired replicates and accelerated stress** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **b–h measurements and demagnetizing corrections** affects the distinction between **formula parameter versus reliably measured device property**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **475.555556 A/m** and **693.333333 A/m** from the explicit expression for the stated two values of **Coil current**. Report a unit-consistent slope in (A/m)/(A), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

**C — Measurement design.** Specify an experiment separating **field distortion, calibration drift and device aging** from the mechanism discussed in this lesson. Include temperature, sample dimensions, sample-independent replication, instrument background, control specimens and a predeclared rejection criterion. *Answer direction:* use **reference standards, paired replicates and accelerated stress** and state which result would invalidate the interpretation rather than simply refining its fit.

<!-- MODEL_14 -->

## Lesson 8.2: Impedance spectroscopy, phase and calibration

### Microscopic picture and applicable constitutive law

Impedance spectroscopy returns complex voltage/current response over frequency. Extracted capacitance and permittivity depend on whether a series or parallel circuit representation is selected and on electrode geometry. Calibration should remove open fixtures, shorts and residual cable effects; moisture and temperature shifts can dominate low-frequency measurements. A fitted equivalent circuit is useful only when parameter identifiability is tested.

**Primary relationship.** For phasors, Z(ω)=V(ω)/I(ω); ideal C has Z=1/(iωC). This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **impedance spectroscopy, phase and calibration**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A capacitor appears to have a negative capacitance at high frequency. Check series inductance, phase calibration and fixture resonances before invoking exotic material physics.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Volumetric hysteresis loss rate** as an exercise in numerical reasoning. Its controllable variable is **Repetition frequency**; all other quantities follow fixed assumptions. Set **Repetition frequency = 173.33333 Hz**. With the implemented expression `500*f`, the output is **86666.6667 W/m³**. Increase the control to **227.77778 Hz**. The new output is **113888.889 W/m³**. Thus the model output increases over this interval, with secant slope **500 (W/m³)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

**Model boundary.** Assumed constant cycle loop area 500 J/m³; not valid if loop area changes with f, amplitude or temperature. Other variables, including temperature, composition and interfaces, are held constant even where they might change under laboratory conditions. The numerical estimate should therefore be read as conditional on its explicit parameters. If the stated physical regime cannot be verified, present the output as a sensitivity demonstration rather than a prediction or nominal catalog material value. In research notes, copy the assumptions with the number so a future user cannot detach a formula result from its domain of validity.

### Observational strategy and rival explanations

A single RC arc does not uniquely identify a specific grain boundary or electrode layer.

### Counterfactual and model criticism

Suppose a measurement appears to support **impedance spectroscopy, phase and calibration**, but **field distortion, calibration drift and device aging** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **reference standards, paired replicates and accelerated stress** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **impedance spectroscopy, phase and calibration** affects the distinction between **formula parameter versus reliably measured device property**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **86666.6667 W/m³** and **113888.889 W/m³** from the explicit expression for the stated two values of **Repetition frequency**. Report a unit-consistent slope in (W/m³)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 8.3: Magnetometry, microscopy and independent probes

### Microscopic picture and applicable constitutive law

Bulk magnetometry measures an integrated moment, while microscopy and scattering can reveal domain orientation, local structure and ordering wave vectors. Magnetic force microscopy detects force gradients and can be affected by tip fields; magnetic diffraction has its own resolution and sensitivity limits. A proper interpretation uses complementary probes because neither a loop nor an image uniquely identifies the underlying moment arrangement.

**Primary relationship.** Measured total moment m relates to average magnetization M by m=MV for a uniformly magnetic sample. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **magnetometry, microscopy and independent probes**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A patterned magnetic film shows unexpected small remanence. Compare magnetic imaging and field-dependent structural measurements to separate compensated domains from an unanticipated nonmagnetic volume fraction.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetizing field in a test solenoid** as an exercise in numerical reasoning. Its controllable variable is **Coil current**; all other quantities follow fixed assumptions. Set **Coil current = 2.2777778 A**. With the implemented expression `200*I/0.5`, the output is **911.111111 A/m**. Increase the control to **2.8222222 A**. The new output is **1128.88889 A/m**. Thus the model output increases over this interval, with secant slope **400 (A/m)/(A)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Sample holder subtraction, imaging tip artifacts and incomplete field calibration require explicit controls.

### Counterfactual and model criticism

Suppose a measurement appears to support **magnetometry, microscopy and independent probes**, but **field distortion, calibration drift and device aging** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **reference standards, paired replicates and accelerated stress** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **magnetometry, microscopy and independent probes** affects the distinction between **formula parameter versus reliably measured device property**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **911.111111 A/m** and **1128.88889 A/m** from the explicit expression for the stated two values of **Coil current**. Report a unit-consistent slope in (A/m)/(A), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Lesson 8.4: Uncertainty, replication and model discrimination

### Microscopic picture and applicable constitutive law

Measurement uncertainty includes calibration, environmental drift, sample heterogeneity and model assumptions. Averaging repeated cycles of one specimen increases precision of that particular observation but does not measure batch-to-batch reproducibility. A valid confidence interval depends on the sampling hierarchy and correlated errors. Pre-registration of failure thresholds and a rival-hypothesis test prevents a simulation with free parameters from being mistaken for independent verification.

**Primary relationship.** For independent errors, first-order propagation uses Var(y)≈Σi(∂y/∂xi)²Var(xi). This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **uncertainty, replication and model discrimination**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

A team measures 100 I–V sweeps on one magnetic tunnel junction and claims excellent manufacturing yield. Design a nested experiment across positions, wafers and process batches, and report effect sizes rather than sweep counts as sample sizes.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Volumetric hysteresis loss rate** as an exercise in numerical reasoning. Its controllable variable is **Repetition frequency**; all other quantities follow fixed assumptions. Set **Repetition frequency = 282.22222 Hz**. With the implemented expression `500*f`, the output is **141111.111 W/m³**. Increase the control to **336.66667 Hz**. The new output is **168333.333 W/m³**. Thus the model output increases over this interval, with secant slope **500 (W/m³)/(Hz)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Never attach arbitrary error bars to formula-generated CSV values; those values have no measurement uncertainty distribution.

### Counterfactual and model criticism

Suppose a measurement appears to support **uncertainty, replication and model discrimination**, but **field distortion, calibration drift and device aging** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **reference standards, paired replicates and accelerated stress** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **uncertainty, replication and model discrimination** affects the distinction between **formula parameter versus reliably measured device property**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **141111.111 W/m³** and **168333.333 W/m³** from the explicit expression for the stated two values of **Repetition frequency**. Report a unit-consistent slope in (W/m³)/(Hz), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

<!-- MODEL_15 -->

## Lesson 8.5: Device selection, thermal limits and ethical reporting

### Microscopic picture and applicable constitutive law

Materials selection requires translating measured response into a component-level operating window. For magnets include field, temperature, demagnetization and dynamic heating. For dielectrics include leakage, endurance, breakdown statistics and humidity. For spin devices include retention, energy per switch, error rate and fabrication yield. Safety and environmental constraints matter alongside performance: some functional elements require controlled handling and end-of-life plans.

**Primary relationship.** Evaluate a component with operating limits and measured distributions, not a single nominal property number. This equation has meaning only when the relevant material state and field convention are defined. It may describe a homogeneous constitutive response, a thermodynamic approximation, a finite-geometry component, or a phenomenological fit. Note which interpretation applies here. For **device selection, thermal limits and ethical reporting**, specify the specimen scale at which the coefficient is defined and the experimental conditions that could change it. An observed trend is not enough to identify the microscopic carriers, local moments or order-parameter dynamics; a second observable is needed to test the proposed mechanism.

Build a decision table comparing dielectric or magnetic candidates under a fixed mission profile. Weight traceable measured properties, reliability evidence, fabrication compatibility and cost; mark unknowns as missing, not zero.

### Worked numerical sensitivity calculation — explicitly synthetic

Use the separate teaching calculator **Magnetizing field in a test solenoid** as an exercise in numerical reasoning. Its controllable variable is **Coil current**; all other quantities follow fixed assumptions. Set **Coil current = 3.3666667 A**. With the implemented expression `200*I/0.5`, the output is **1346.66667 A/m**. Increase the control to **3.9111111 A**. The new output is **1564.44444 A/m**. Thus the model output increases over this interval, with secant slope **400 (A/m)/(A)**. The numerical exercise is related to the unit's physical relationships but does not claim to represent a complete experiment or device. For example, a unit investigating dynamic magnetic response can use a simple anisotropy sensitivity without assuming its own specimen reverses as an ideal macrospin.

### Observational strategy and rival explanations

Teaching formulas are not process recipes, medical device approvals or electrical safety certifications.

### Counterfactual and model criticism

Suppose a measurement appears to support **device selection, thermal limits and ethical reporting**, but **field distortion, calibration drift and device aging** causes the same visible trend. Vary an independent condition deliberately, such as electrode material, specimen thickness, drive frequency, temperature, field orientation, waiting time or sample history. Predict the direction and magnitude each mechanism would produce before collecting new data. The objective of **reference standards, paired replicates and accelerated stress** is to find an observation that at least one rival hypothesis cannot explain without changing extra free parameters. This avoids circular reasoning in which the model is considered proven because its coefficient was tuned to reproduce a single observation.

### Problems and brief solution directions

**A — Conceptual comparison.** Explain how **device selection, thermal limits and ethical reporting** affects the distinction between **formula parameter versus reliably measured device property**. Propose two microscopic mechanisms for the same sign of change. *Answer direction:* specify one diagnostic that measures structure or occupancy and another measuring electrical or magnetic response; describe the outcome that would falsify your preferred interpretation.

**B — Reproduce and extend.** Calculate **1346.66667 A/m** and **1564.44444 A/m** from the explicit expression for the stated two values of **Coil current**. Report a unit-consistent slope in (A/m)/(A), and contrast it with a differential slope where the model is nonlinear. *Answer direction:* work from the fixed assumptions, calculate Δy/Δx and check the output trend from the sign of the expression.

## Integrated university case study: Standards-aware component materials choice

### Diagnose the evidence, not just the material label

An engineering team must select a dielectric or magnetic candidate for a thermally stressed system using fragmented supplier data and a small laboratory dataset. Make a table of controlled process variables, directly observed measurements, inferred properties and uncontrolled alternatives. The specimen may be a film, pellet, patterned junction, magnetic core or composite, so identify the region contributing most strongly to the recorded signal. Give a physical description of the measurement geometry and a unit-checked equation for converting raw data into a proposed material property. An inference based on a bulk property may be invalid when interfaces dominate the measurement. No result of the exercise is a validated procurement or device-design figure.

### Joint modeling and sensitivity analysis

Calibrate the nominal solenoid field and translate measured loop area into dissipated power at operating frequency, then compare against measured temperatures. Use both unit models at their default values, then perturb each controllable input individually. Compute relative sensitivity (Δy/y)/(Δx/x) where the quantities are nonzero, and distinguish a finite-difference trend from proof of causality. For an exponential model, a narrow uncertainty in the barrier or thickness can dominate all other precision claims; for a geometric model, area and thickness metrology may dominate; for a magnetic relation, a demagnetizing correction may decide which internal field is actually relevant. Avoid combining unrelated outputs into a synthetic physical property merely because two plots can be overlaid.

### Evidence required for a decision

Build an uncertainty budget, independent lot replication plan and predeclared operating envelope. Report instrument calibration separately from repeatability, compare matched control specimens, and state the number of distinct fabrication lots. Trace any composition assignment to a structural or chemical measurement, not a deposition recipe. An independent test is valuable when it distinguishes **field distortion, calibration drift and device aging** from the mechanism under investigation. If both explain the data, report the state as ambiguous. The decision note should state whether evidence is a hypothesis, a numerical sensitivity, a measured laboratory observation, or representative operating-condition qualification. **Caution:** A model validated numerically has not been validated as a safe design criterion.

### Five capstone examination questions

