# Unit 5: Thermodynamics, phases and heat treatment

> **Guiding question:** How do energy, composition and processing time determine which phases appear and how they evolve?

## Conceptual overview

A phase diagram is an equilibrium map, not a time machine. It tells us what arrangement minimizes the relevant thermodynamic potential for an idealized bulk composition and pressure after sufficient equilibration. Real industrial parts are cooled in finite time, and transformation paths may stop in metastable states. A quenched steel can contain martensite that is absent from an equilibrium diagram; a polymer may retain a morphology set by its thermal history. Kinetics supplies the missing time dimension.

The lever rule is a mass balance written graphically. It gives phase fractions from tie-line compositions within a specified two-phase field, provided the composition basis is consistent. It does not tell you whether crystals are needles, plates or spheres, nor does it predict their distribution or size. Two specimens can contain nearly equal phase fractions but have different toughness because one contains coarse particles at boundaries and the other has finely dispersed precipitates. Microstructure requires more than the list of phases.

Nucleation and growth compete through energy and mobility. A thermodynamic driving force favors the new phase, but creating an interface costs energy. More nucleation events can produce a finer transformation product if growth has limited time; fewer nuclei and long growth periods can yield coarse structures. Heterogeneous nucleation frequently occurs at existing interfaces, yet this does not guarantee a uniform final product. Impurities, temperature gradients and fluid flow in a melt complicate the process.

Thermal schedules should be tested rather than copied across components. A narrow plate and a thick forging cool at different rates even when the furnace controller executes the same program. Precipitation hardening can generate a peak followed by overaging; a beneficial hardness condition may be poor for fatigue, corrosion or dimensional stability. Design experiments must include the final acceptance function, not just the easiest intermediate measurement.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 5.1 Free energy and phase stability

#### Mechanism and vocabulary

At fixed temperature and pressure, the Gibbs free energy helps describe equilibrium among phases and reactions. A composition can favor one set of phases at high temperature and another at low temperature. Kinetics determines whether the system reaches the equilibrium state within the available time. A metastable structure can persist despite a thermodynamic driving force to transform.



#### Measurement and evidence

Use calorimetry, diffraction and microscopy to identify transformation temperatures and phase fractions. State the equilibration route and cooling rate. Compare a slowly cooled specimen with a rapidly quenched one, and distinguish observed retained phases from an equilibrium prediction.



#### Engineering use and tradeoffs

Heat treating an alloy is a competition among nucleation, diffusion, mechanical constraints and energy changes. A part may be deliberately kept metastable to obtain high strength, then aged under controlled conditions to tune precipitation.



#### Scope and common failure of reasoning

Do not claim a phase diagram predicts cooling microstructure uniquely. It gives equilibrium relationships; time-dependent transformations require kinetic information.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **free energy and phase stability**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 5.2 Binary phase diagrams and the lever rule

#### Mechanism and vocabulary

A binary equilibrium phase diagram maps stable phase regions versus composition and temperature at specified pressure. In a two-phase field, a tie line provides phase compositions and the lever rule gives bulk phase fractions by mass when composition coordinates are mass fractions. The rule follows directly from conservation of solute.



#### Measurement and evidence

Locate alloy composition and temperature, identify the two relevant solvus or liquidus intersections, then calculate fractions using mass balance. Check that fractions lie between zero and one and sum to unity. Inspect whether the reported diagram uses atomic or mass percent.



#### Engineering use and tradeoffs

Casting engineers use phase relationships to anticipate segregation and solidification ranges. Battery and ceramic researchers use different phase equilibria to avoid reactive interfaces. The same graphical skill applies, but the governing components and phases change.



#### Scope and common failure of reasoning

Do not apply a binary lever rule to a multiphase or multicomponent region without appropriate constraints; also do not mistake a phase fraction for a grain fraction observed on an arbitrary micrograph.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **binary phase diagrams and the lever rule**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 5.3 Nucleation and growth

#### Mechanism and vocabulary

A transformation often begins by forming nuclei that face a competition between bulk free-energy benefit and interfacial energy cost. Heterogeneous surfaces lower effective barriers; growth then needs transport and interface motion. The number of nuclei and their growth histories shape the final grain or precipitate size distribution.



#### Measurement and evidence

Use thermal analysis to detect a transformation, interrupted quenching to capture stages and microscopy to quantify particle size. Vary cooling rate and hold time independently where possible. Test whether observed particle densities change with sample cleanliness or existing interfaces.



#### Engineering use and tradeoffs

Finer solidification structures can improve some properties while also creating microsegregation or shrinkage defects. Controlled inoculation can promote nucleation, but success still depends on heat extraction and liquid flow.



#### Scope and common failure of reasoning

Classical nucleation theory idealizes particle geometry and interfacial energies; it should not be treated as an exact count of nuclei in a real multicomponent melt.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **nucleation and growth**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 5.4 Transformation-time maps

#### Mechanism and vocabulary

Time–temperature–transformation diagrams describe the evolution of selected transformations during isothermal holding, while continuous-cooling-transformation diagrams describe specific cooling paths. These maps are specific to alloy composition and prior processing. Quench severity, specimen thickness and latent heat can make the center of a component follow a different thermal path from its surface.



#### Measurement and evidence

Compare temperature histories measured with thermocouples against the intended thermal program. Characterize resulting phases by hardness and microscopy. For steel, distinguish pearlite, bainite and martensite by formation mechanisms and morphology rather than identifying all hard structures as martensite.



#### Engineering use and tradeoffs

An industrial heat treatment must achieve consistent properties across part thickness without excessive distortion or cracking. A process designed from a thin laboratory sample may fail on a large forging because temperature changes more slowly inside.



#### Scope and common failure of reasoning

An isothermal diagram is not a universal conversion chart for arbitrary cooling rates. Avoid extrapolation between alloys without experimental support.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **transformation-time maps**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 5.5 Age hardening and microstructural design

#### Mechanism and vocabulary

A supersaturated solid solution may decompose during aging into fine solute-rich precipitates. Particle size, spacing, coherency and volume fraction influence dislocation interactions. Peak hardness occurs when obstacles are effective; overaging can reduce strength as particles coarsen or change character.



#### Measurement and evidence

Create an aging series at fixed temperature, measuring hardness and at least one microstructural indicator at each interval. Compare several temperatures to separate rapid kinetics from final state. Preserve quench-to-aging delays when they affect natural aging.



#### Engineering use and tradeoffs

Aluminum heat-treatable alloys and some superalloys use engineered precipitation pathways. Strength improvement must be evaluated together with corrosion behavior, toughness and manufacturing steps such as welding.



#### Scope and common failure of reasoning

A hardness peak does not prove the optimum condition for all service properties. Thermal exposure in use may continue the aging process.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **age hardening and microstructural design**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Binary-alloy aging sequence

### Research question and hypotheses

At a selected composition and temperature, apply a consistent mass balance for two phase compositions, then discuss why the phase fraction does not specify particle size. Show which transformation-time records a manufacturing team should collect.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Sketch a thermal path through solution treatment, quenching and aging. Label where equilibrium assumptions fail and where diffusion and nucleation rates matter. Use the Arrhenius model to compare temperatures without interpreting its synthetic constants as real.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

Two batches show equal hardness but different fatigue performance. Propose a microstructure-based explanation involving precipitate distribution or boundary chemistry, and design a discriminating test.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 5.1 — Two-phase alloy fractions

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **lever-rule alpha fraction** using Alpha composition (mass %) = 8; Bulk composition (mass %) = 40; Beta composition (mass %) = 80. The starting values are synthetic and describe no commercial product.

**Model.** `fα = (Cβ − C₀)/(Cβ − Cα)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ca=8, C0=40, Cb=80 into the stated relation. The reproducibly evaluated result is **0.555556 fraction**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Valid only when Cα < C₀ < Cβ in a binary two-phase field.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 5.2 — Aging rate sensitivity

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **arrhenius rate coefficient** using Prefactor (1/s) = 93000; Activation energy (kJ/mol) = 60; Temperature (K) = 650. The starting values are synthetic and describe no commercial product.

**Model.** `k = A exp(−Q/RT)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute A=93000, Q=60, T=650 into the stated relation. The reproducibly evaluated result is **1.40255 s⁻¹**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Idealized single-process kinetic fit; parameters not universal.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 5.3 — Composition change screening

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **lever-rule alpha fraction** using Alpha composition (mass %) = 10; Bulk composition (mass %) = 40; Beta composition (mass %) = 80. The starting values are synthetic and describe no commercial product.

**Model.** `fα = (Cβ − C₀)/(Cβ − Cα)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ca=10, C0=40, Cb=80 into the stated relation. The reproducibly evaluated result is **0.571429 fraction**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Valid only when Cα < C₀ < Cβ in a binary two-phase field.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 5.4 — Reaction-time window

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **arrhenius rate coefficient** using Prefactor (1/s) = 108000; Activation energy (kJ/mol) = 60; Temperature (K) = 650. The starting values are synthetic and describe no commercial product.

**Model.** `k = A exp(−Q/RT)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute A=108000, Q=60, T=650 into the stated relation. The reproducibly evaluated result is **1.62877 s⁻¹**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Idealized single-process kinetic fit; parameters not universal.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 5.5 — Heat-treatment comparison

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **lever-rule alpha fraction** using Alpha composition (mass %) = 12; Bulk composition (mass %) = 40; Beta composition (mass %) = 80. The starting values are synthetic and describe no commercial product.

**Model.** `fα = (Cβ − C₀)/(Cβ − Cα)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ca=12, C0=40, Cb=80 into the stated relation. The reproducibly evaluated result is **0.588235 fraction**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Valid only when Cα < C₀ < Cβ in a binary two-phase field.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_8 -->

<!-- INTERACTIVE_MODEL_9 -->

## Concept synthesis and oral examination

Discuss how **free energy and phase stability** can be connected to **age hardening and microstructural design** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
