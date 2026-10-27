# Unit 4: Mechanical properties, damage and reliability

> **Guiding question:** How do laboratory stress–strain curves become safe design constraints under real loading?

## Conceptual overview

Mechanical performance has an unusually strong dependence on geometry. Stress and strain normalize a tensile measurement, but even those quantities require care because the conventional definitions use initial area and gauge length. After necking, the local cross section changes; an engineering stress curve and a local true-stress description answer different questions. For linear reversible deformation, axial extension scales with force and length and inversely with area and modulus. This is why a designer can increase stiffness by changing geometry without changing alloy.

A strong material is not automatically damage tolerant. Crack-like flaws concentrate stress; the tolerable flaw size decreases as applied stress increases for an otherwise fixed toughness and geometry. Very high nominal tensile strength can coexist with low fracture resistance under the relevant constraints. A safe component design therefore needs credible inspection limits, realistic flaws and appropriate fracture mechanics. The formula in this book for mode-I stress intensity is useful for learning but does not replace valid standardized toughness testing.

Repeated load and sustained load represent different risk pathways. Fatigue damage accumulates through cycles, often at surfaces or notches, while creep can occur under a sustained stress when diffusion or molecular relaxation is active. Both are sensitive to environment, microstructure, processing, and test history. A rapid tensile curve does not certify long-term service. In particular, a plastic under constant room-temperature stress may lose dimensional accuracy over months despite never approaching its instantaneous tensile strength.

Interpretation must include the observational window. A fatigue run-out represents survival beyond a specified cycle count and is not a measured failure life. A short creep test may miss a late accelerating regime. A fracture surface can show a mechanism but still not reveal the initiating cause without field history. Strong engineering conclusions are triangulated from mechanics, materials characterization, realistic service loads and uncertainty analysis.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 4.1 Stress, strain and elastic response

#### Mechanism and vocabulary

Engineering stress divides applied force by initial cross-sectional area; engineering strain divides length change by initial gauge length. Young modulus is a slope in the reversible approximately linear regime, not the same quantity as yield or ultimate tensile strength. Poisson ratio records lateral contraction and can vary across material classes and directions.



#### Measurement and evidence

Use a strain gauge or extensometer appropriate for the gauge length; measure initial dimensions and loading rate. Identify the strain range used to fit modulus, remove fixture compliance where needed and inspect hysteresis during loading–unloading. Report units explicitly: pascals for stress and dimensionless ratio for strain.



#### Engineering use and tradeoffs

A long slender rod and a short stout rod of identical material have different axial extension under the same force. Component stiffness depends on both modulus and geometry, so a catalog number alone does not predict deflection.



#### Scope and common failure of reasoning

Do not measure Young modulus from the post-yield region, or infer a bulk property from crosshead displacement without accounting for machine compliance.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **stress, strain and elastic response**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 4.2 Yielding and tensile strength

#### Mechanism and vocabulary

Metals often exhibit plastic flow through dislocation motion; polymers and ceramics exhibit different deformation and failure mechanisms. Yield stress depends on how yield is defined, on loading rate and often on temperature. The ultimate engineering tensile strength corresponds to the maximum engineering stress, not necessarily the true local stress at fracture.



#### Measurement and evidence

Plot the full force-extension record and mark elastic region, offset-yield convention, maximum force and failure. Record specimen geometry and orientation; compare repeat specimens and inspect fracture surfaces to identify necking, cleavage or interfacial failure.



#### Engineering use and tradeoffs

A sheet forming operation requires sufficient ductility and work hardening to distribute strain, while a bolt needs an adequate proof load and resistance to preload loss. The same nominal yield strength may conceal a large difference in strain-hardening behavior.



#### Scope and common failure of reasoning

One monotonic tensile test does not establish fatigue life, impact toughness, corrosion resistance or behavior after welding.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **yielding and tensile strength**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 4.3 Fracture and stress intensity

#### Mechanism and vocabulary

A crack concentrates stress near its tip. For a suitable linear-elastic geometry, mode-I stress intensity can be written K_I = Y sigma sqrt(pi a), with a shape correction factor Y. Fracture occurs when driving force meets a critical toughness under conditions where the chosen fracture framework applies.



#### Measurement and evidence

Measure crack length and specimen geometry accurately. Fracture toughness testing requires appropriate thickness, crack preparation and validity criteria; a numerical K estimate from a simple teaching formula is not a qualification result. Compare failure load across otherwise equivalent specimens with different initial flaw sizes.



#### Engineering use and tradeoffs

A high-strength alloy used in a large pressure vessel may become intolerant of a defect that a lower-strength, tougher alloy could survive. Inspection intervals and acceptable flaw sizes therefore belong in materials design.



#### Scope and common failure of reasoning

Do not apply small-scale-yielding linear-elastic fracture mechanics blindly to highly ductile materials, short cracks or complex multiaxial loading.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **fracture and stress intensity**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 4.4 Fatigue and cyclic loading

#### Mechanism and vocabulary

Repeated stress can initiate and grow cracks at amplitudes below a monotonic tensile strength. Mean stress, surface condition, loading frequency, environment, residual stress and stress concentrations influence fatigue behavior. S–N curves and crack-growth descriptions answer different questions and may need different experiments.



#### Measurement and evidence

Describe waveform, load ratio, frequency, specimen finish and run-out rule. Treat censored run-out results as distinct from failures. Measure or document initiation sites rather than merely plotting life against a single scalar. Compare polished and notched samples to reveal the effect of geometry.



#### Engineering use and tradeoffs

Rotating shafts, aircraft joints and prosthetic components experience repeated loading. A surface finish change or corrosion pit can overwhelm an apparent improvement in bulk strength, so prevention often requires attention to manufacturing details.



#### Scope and common failure of reasoning

An endurance limit is not universal for all alloys or environments. Extrapolating a short laboratory test directly to decades of field reliability is unsound.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **fatigue and cyclic loading**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 4.5 Creep and time-dependent response

#### Mechanism and vocabulary

At sufficiently high homologous temperature, deformation can accumulate under a sustained load through mechanisms including dislocation climb, grain-boundary sliding and diffusion. Polymers can also creep at ordinary temperatures because their molecular relaxation times are relevant. Strain versus time may show primary, near-steady and accelerating regimes, but not every test exhibits all three clearly.



#### Measurement and evidence

Specify temperature, stress, atmosphere and thermal equilibrium before loading. Measure deformation continuously and consider oxidation, stress redistribution and grip effects. Compare specimens at multiple conditions to assess whether a proposed activation energy or stress exponent describes the data.



#### Engineering use and tradeoffs

Turbine blades, solder joints and polymer fixtures must resist gradual distortion. A high initial stiffness does not guarantee that a precise gap or preload will survive a prolonged exposure.



#### Scope and common failure of reasoning

Simple steady creep laws are fit models for regimes, not substitutes for long-term rupture data. Distinguish creep strain from thermal expansion and instrument drift.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **creep and time-dependent response**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Small cracked bracket assessment

### Research question and hypotheses

Given a bracket with an identified surface flaw, estimate an idealized mode-I stress scale and compare it with a separate elastic-deflection calculation. State why neither numerical result establishes service approval.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Design a specimen protocol to compare as-made and surface-finished coupons, including orientation, geometry, load rate and at least three independent repeats. Explain how notches and corrosion should enter the testing plan.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

A supplier offers a higher-strength grade without any toughness data. Prepare a decision memo explaining why the strength gain cannot justify a direct substitution and what evidence is needed.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 4.1 — Elastic service deflection

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **elastic rod extension** using Axial force (kN) = 8; Length (m) = 0.8; Area (mm²) = 100; Modulus (GPa) = 70. The starting values are synthetic and describe no commercial product.

**Model.** `ΔL = FL/(AE)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute F=8, L=0.8, A=100, E=70 into the stated relation. The reproducibly evaluated result is **0.914286 mm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Axial linear-elastic uniform rod; excludes buckling and joints.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 4.2 — Pre-existing crack screen

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **crack-limited stress** using Toughness (MPa√m) = 38; Shape factor = 1.1; Crack length (mm) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `σ_c = K_IC / (Y√(πa))`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute K=38, Y=1.1, a=2 into the stated relation. The reproducibly evaluated result is **435.814 MPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Linear-elastic mode-I illustration, not a certified tolerance.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 4.3 — Tie rod stiffness requirement

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **elastic rod extension** using Axial force (kN) = 10; Length (m) = 0.8; Area (mm²) = 100; Modulus (GPa) = 70. The starting values are synthetic and describe no commercial product.

**Model.** `ΔL = FL/(AE)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute F=10, L=0.8, A=100, E=70 into the stated relation. The reproducibly evaluated result is **1.14286 mm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Axial linear-elastic uniform rod; excludes buckling and joints.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 4.4 — Inspection flaw sensitivity

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **crack-limited stress** using Toughness (MPa√m) = 44; Shape factor = 1.1; Crack length (mm) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `σ_c = K_IC / (Y√(πa))`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute K=44, Y=1.1, a=2 into the stated relation. The reproducibly evaluated result is **504.627 MPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Linear-elastic mode-I illustration, not a certified tolerance.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 4.5 — Deformation vs toughness decision

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **elastic rod extension** using Axial force (kN) = 12; Length (m) = 0.8; Area (mm²) = 100; Modulus (GPa) = 70. The starting values are synthetic and describe no commercial product.

**Model.** `ΔL = FL/(AE)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute F=12, L=0.8, A=100, E=70 into the stated relation. The reproducibly evaluated result is **1.37143 mm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Axial linear-elastic uniform rod; excludes buckling and joints.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_6 -->

<!-- INTERACTIVE_MODEL_7 -->

## Concept synthesis and oral examination

Discuss how **stress, strain and elastic response** can be connected to **creep and time-dependent response** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
