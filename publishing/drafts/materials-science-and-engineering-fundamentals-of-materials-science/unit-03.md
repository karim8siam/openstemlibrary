# Unit 3: Defects, diffusion and microstructural evolution

> **Guiding question:** Why can a small population of defects have a large influence on transport, strength and stability?

## Conceptual overview

Defects are central to materials performance because perfect crystals are conceptual reference systems, not manufacturing outcomes. The entropic advantage of multiple configurations creates finite thermal populations of point defects; however, the defect populations frozen into real specimens can be governed by fast cooling or irradiation instead. A diffusion path that is irrelevant at one temperature may dominate at another, and diffusion along grain boundaries can proceed much faster than transport through a perfect lattice.

Plasticity reveals why dislocations matter. Moving one dislocation through a crystal allows a portion of the material to slip without shearing every bond across a full plane simultaneously. This concept does not imply that easy slip is always desirable: structures that obstruct motion often strengthen alloys. Work hardening adds dislocations, fine precipitates impede motion and grain boundaries disrupt its transfer. Each strengthening mechanism has costs. Cold work can reduce formability; precipitation can overage; boundary strengthening can increase high-temperature diffusion or embrittlement sensitivity.

The temperature and time dimensions must be kept together. The familiar diffusion estimate proportional to the square root of D times t contains a temperature-sensitive coefficient. Increasing temperature may be more effective than multiplying time by the same numerical factor, but higher temperature can grow grains, drive chemical reactions and raise energy cost. The ideal thermal recipe must be tested against all affected microstructural features. A favorable carbon depth profile is of little use if a gear tooth becomes excessively distorted during quenching.

Characterization must be chosen to distinguish causes. If hardness rises after rolling, quantify whether changes follow dislocation density, phase fraction or grain refinement. If a diffusion profile broadens, first rule out instrument convolution and sample-preparation smearing. If microscopy suggests recrystallization, accompany the image with hardness, orientation or other independent measures. A causal explanation is useful only if it predicts observations that a competing explanation would not.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 3.1 Point defects and concentrations

#### Mechanism and vocabulary

Vacancies, interstitials and substitutional solutes disturb perfect periodic order. Equilibrium vacancy concentration generally increases with temperature because configuration entropy competes with the energy cost of forming a vacancy. Real materials may retain nonequilibrium defect populations after quenching, irradiation, plastic deformation or growth.



#### Measurement and evidence

Measure composition independently from site occupancy. Use resistivity, positron methods or diffusion experiments when appropriate to test defect-related hypotheses; never infer one precise vacancy concentration solely from a nominal alloy designation. Control temperature and hold time, because equilibrium assumptions may require time that the process does not provide.



#### Engineering use and tradeoffs

Vacancies enable many substitutional diffusion events and can influence sintering. Doping controls charge carriers in semiconductors but dopants can also form complexes or segregate. The same defect may be beneficial in one device and harmful in another.



#### Scope and common failure of reasoning

A vacancy-concentration Arrhenius expression is schematic unless the formation free energy, site count and relevant charge states are defined. Surface and grain-boundary defects complicate bulk estimates.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **point defects and concentrations**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 3.2 Dislocations and plastic flow

#### Mechanism and vocabulary

A dislocation is a line defect whose motion allows slip at stresses much lower than the ideal shear strength of a perfect crystal. Edge and screw character describe limiting geometries; most real segments are mixed. Dislocation density, obstacles and available slip systems influence yield behavior and strain hardening.



#### Measurement and evidence

Draw a Burgers circuit and describe how its closure failure identifies a dislocation. Compare cold-worked with annealed specimens via hardness, tensile measurements and microscopy. Report test orientation and strain rate. Look for evidence of recovery or recrystallization after heating.



#### Engineering use and tradeoffs

Cold-rolling strengthens many alloys by introducing obstacles to dislocation motion but also reduces ductility. Annealing can restore formability, so rolling and heat treatment must be designed as a sequence rather than independent operations.



#### Scope and common failure of reasoning

High hardness does not uniquely measure dislocation density. Precipitates, grain boundaries, residual stress and local chemistry may also raise measured hardness.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **dislocations and plastic flow**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 3.3 Grain boundaries and strengthening

#### Mechanism and vocabulary

Grain boundaries disrupt lattice continuity and often impede slip transfer. Hall–Petch scaling expresses a useful approximate increase of yield stress as inverse square root of grain size over a limited regime. Boundaries can also accelerate diffusion, provide nucleation sites and become vulnerable to segregation or corrosion.



#### Measurement and evidence

Measure a meaningful grain-size distribution rather than a single field average. Document whether size is area-equivalent diameter, intercept length or another quantity. Prepare tensile coupons from comparable processing routes to separate grain-size effects from precipitation or work hardening.



#### Engineering use and tradeoffs

Fine grains often help room-temperature yield strength, while large grains or directional microstructures may improve high-temperature creep resistance. A design that optimizes one property can therefore worsen another.



#### Scope and common failure of reasoning

Hall–Petch is an empirical relation that should not be extrapolated without validation to nanocrystalline sizes, radically different materials or extreme temperatures.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **grain boundaries and strengthening**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 3.4 Diffusion and concentration gradients

#### Mechanism and vocabulary

Diffusion is net mass transport driven by a chemical-potential gradient; Fick laws provide a useful form when concentration and activity can be related simply. The diffusion coefficient is temperature-dependent and mechanism-dependent. Grain-boundary diffusion can dominate over bulk diffusion at certain temperatures and time scales.



#### Measurement and evidence

For a diffusion couple, polish across the bonded interface and measure composition versus distance at known times and temperatures. Plot concentration profiles, report spatial resolution and use more than one duration to test a square-root-of-time scaling. Distinguish tracer diffusion from interdiffusion.



#### Engineering use and tradeoffs

Carburization and semiconductor doping depend on concentration gradients and thermal budgets. Deep cases or broad junctions require longer exposure or higher diffusion coefficients, but temperature can induce unwanted grain growth and reactions.



#### Scope and common failure of reasoning

The square-root diffusion-length estimate assumes idealized constant diffusion coefficient and geometry. A moving reaction front, changing boundary concentration or multicomponent effects needs a different model.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **diffusion and concentration gradients**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 3.5 Recovery, recrystallization and coarsening

#### Mechanism and vocabulary

Stored deformation energy can drive microstructural change during heating. Recovery rearranges defects without entirely replacing grains; recrystallization creates new comparatively strain-free grains; subsequent grain growth reduces boundary area. Particle pinning and solute drag can limit boundary migration.



#### Measurement and evidence

Track hardness, diffraction peak width and microstructure across a heat-treatment matrix. Record ramp rates, soak times, atmosphere and specimen thickness because furnace set temperature is not always specimen temperature. A time series reveals whether changes are progressive or abrupt.



#### Engineering use and tradeoffs

A forming process might require intermediate annealing to avoid cracking. In a turbine component, however, excessive coarsening can alter creep resistance or anisotropy. The ideal schedule depends on both manufacturing and service conditions.



#### Scope and common failure of reasoning

Heating does not invariably soften every alloy; precipitation hardening may compete with recovery, and some materials undergo embrittling phase changes.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **recovery, recrystallization and coarsening**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Microstructure after cold work and annealing

### Research question and hypotheses

Plan a matrix with two deformation levels, two hold temperatures and three time intervals. Specify how hardness, orientation and grain size will be measured. Predict which hypotheses could yield similar hardness but different microstructures.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Use the diffusion-length and Hall–Petch models to show that a faster diffusional process and a stronger grain-size contribution need not move in the same direction. Describe limits of applying both formulas at once.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

A production part becomes softer after heat treatment even though some precipitates appear. Offer a dislocation-recovery hypothesis and an overaging hypothesis; identify the experiment that separates their contributions.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 3.1 — Carburized case-depth estimate

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **diffusion length** using Diffusivity (×10⁻¹⁴ m²/s) = 4.05; Time (h) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `ℓ = √(2Dt)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute D=4.05, t=2 into the stated relation. The reproducibly evaluated result is **24.1495 µm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **One-dimensional ideal scaling for constant diffusivity.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 3.2 — Grain refinement sensitivity

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **hall–petch stress** using Base stress (MPa) = 110; Coefficient (MPa√m) = 0.35; Grain size (µm) = 20. The starting values are synthetic and describe no commercial product.

**Model.** `σ_y = σ₀ + k/√d`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute s0=110, k=0.35, d=20 into the stated relation. The reproducibly evaluated result is **188.262 MPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Empirical finite-regime relation; micron input converted to meters.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 3.3 — Heat-treatment diffusion budget

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **diffusion length** using Diffusivity (×10⁻¹⁴ m²/s) = 5; Time (h) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `ℓ = √(2Dt)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute D=5, t=2 into the stated relation. The reproducibly evaluated result is **26.8328 µm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **One-dimensional ideal scaling for constant diffusivity.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 3.4 — Strengthening tradeoff analysis

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **hall–petch stress** using Base stress (MPa) = 130; Coefficient (MPa√m) = 0.35; Grain size (µm) = 20. The starting values are synthetic and describe no commercial product.

**Model.** `σ_y = σ₀ + k/√d`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute s0=130, k=0.35, d=20 into the stated relation. The reproducibly evaluated result is **208.262 MPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Empirical finite-regime relation; micron input converted to meters.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 3.5 — Surface treatment timing

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **diffusion length** using Diffusivity (×10⁻¹⁴ m²/s) = 5.85; Time (h) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `ℓ = √(2Dt)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute D=5.85, t=2 into the stated relation. The reproducibly evaluated result is **29.0241 µm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **One-dimensional ideal scaling for constant diffusivity.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_4 -->

<!-- INTERACTIVE_MODEL_5 -->

## Concept synthesis and oral examination

Discuss how **point defects and concentrations** can be connected to **recovery, recrystallization and coarsening** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
