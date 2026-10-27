# Unit 7: Electrical, thermal, magnetic and optical responses

> **Guiding question:** How can structure and defects be connected to transport or field response without overclaiming a simplified model?

## Conceptual overview

Functional response changes when a temperature gradient, electric field, magnetic field or light interacts with matter. These apparently different properties share an underlying theme: charge, energy and momentum must travel or be stored through a structure. Carriers interact with defects, phonons, interfaces and boundaries. The measurable response is usually specific to temperature, frequency, orientation and the size scale of the experiment.

Thermal conductivity measures transport of heat, while heat capacity measures stored thermal energy per temperature change. A thick insulator can allow little heat flow even if a small specimen eventually equilibrates thermally. An electronic heat spreader may have high bulk conductivity yet suffer high interface resistance. Whenever a simple calculation seems too favorable, draw the full thermal or electrical resistance network before making a device-level claim.

Electrical conductivity reflects mobile carriers, but a single measured conductivity cannot determine their density and mobility separately. Four-terminal testing reduces lead/contact contributions; Hall measurements add information that must be interpreted according to carrier type and geometry. Optical absorption has a similar inverse problem: scattering, reflection and absorption can alter apparent signal, so measurements should record the instrument geometry and substrate.

Magnetic hysteresis introduces memory: response depends partly on field history. This is useful in permanent magnets and harmful where energy loss must be minimized. Photonic structures may intentionally exploit wavelength-selective interference; defects or rough surfaces can also scatter light undesirably. A design statement should connect the physical mechanism, required frequency or wavelength, operating conditions and measurement uncertainty, rather than treating a handbook property as a universal constant.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 7.1 Heat capacity and thermal expansion

#### Mechanism and vocabulary

Heat capacity quantifies energy required for a temperature rise under specified thermodynamic conditions; thermal expansion reflects temperature-dependent interatomic spacing and structure. These properties influence thermal shock, joining and dimensional stability. A small coefficient of expansion does not guarantee negligible stress if temperatures are strongly nonuniform.



#### Measurement and evidence

Record sample mass, heating rate, temperature interval and calibration when using calorimetry or dilatometry. Compare heating and cooling cycles to identify transformations or hysteresis. Account for anisotropic expansion in textured or composite parts.



#### Engineering use and tradeoffs

A sensor housing bonded to a silicon chip should minimize differential expansion to protect joints. A furnace lining may need low expansion and high fracture resistance, not merely high maximum temperature tolerance.



#### Scope and common failure of reasoning

Do not conflate heat capacity with thermal conductivity: a material can store substantial heat while transmitting it slowly.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **heat capacity and thermal expansion**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 7.2 Conduction and interface resistance

#### Mechanism and vocabulary

Fourier conduction describes heat flux in relation to a temperature gradient for an appropriate continuum and conductivity tensor. Effective thermal resistance includes layers, contact resistance and possible convection or radiation at boundaries. Conductivity depends on temperature, composition, microstructure and direction.



#### Measurement and evidence

Measure specimen thickness, area and boundary temperatures; allow a steady state when using a steady apparatus. Check for parasitic heat loss and thermal contact quality. A guarded hot-plate test and a laser-flash diffusivity experiment measure different quantities before any conversion.



#### Engineering use and tradeoffs

Electronics cooling may fail because a thin thermal-interface layer has poor contact even when the substrate is highly conductive. Insulation design must consider moisture uptake and aging, which can change effective conductivity.



#### Scope and common failure of reasoning

A one-dimensional steady formula is not accurate when lateral losses, heat generation, temperature-dependent conductivity or transient effects dominate.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **conduction and interface resistance**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 7.3 Charge carriers and resistivity

#### Mechanism and vocabulary

Electrical conductivity depends on mobile carrier populations and how quickly they drift under a field. Metals, semiconductors and ionic solids conduct by different carriers and scattering mechanisms. Conductivity can change with temperature in opposite ways across different regimes and materials.



#### Measurement and evidence

Measure a current–voltage curve over a range where heating and electrochemical reactions are controlled. Use four-terminal geometry when contact resistance dominates two-terminal results. Report whether conductivity was inferred from a thin film, bulk sample or porous composite.



#### Engineering use and tradeoffs

Copper wires favor low resistive loss, while transparent conductive oxides seek a compromise between optical transmission and current spreading. Corrosion or surface films at a connector can increase resistance despite good bulk conductivity.



#### Scope and common failure of reasoning

Do not infer carrier density and mobility separately from conductivity alone; their product is constrained but multiple combinations can produce the same measured value.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **charge carriers and resistivity**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 7.4 Magnetic response and hysteresis

#### Mechanism and vocabulary

Magnetic behavior includes diamagnetic, paramagnetic, ferromagnetic, ferrimagnetic and antiferromagnetic responses. Domain structure, anisotropy and pinning affect hysteresis. A soft magnetic core needs low hysteretic loss for some applications, while permanent magnets seek resistance to demagnetization.



#### Measurement and evidence

Acquire a full field-sweep loop under controlled temperature and geometry. Correct for sample shape and background contributions where possible. Report coercive field, remanence and saturation protocol rather than quoting one magnetic number without context.



#### Engineering use and tradeoffs

Power transformer cores use low-loss magnetic materials; an electric motor magnet requires suitable remanence and thermal stability. Thin-film sensor applications can reward sensitivity that would be undesirable for a high-field structural magnetic component.



#### Scope and common failure of reasoning

A textbook ideal loop is not a quantitative energy-loss estimate without measurement conditions, frequency and sample volume.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **magnetic response and hysteresis**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 7.5 Light interaction and photonic materials

#### Mechanism and vocabulary

Light absorption, reflection, scattering and emission depend on electronic states, vibrational modes, geometry and defects. An optical bandgap can influence wavelength selectivity, but device performance depends on excitons, carrier collection, surfaces and contacts. Microstructure also influences haze and color through scattering.



#### Measurement and evidence

Measure transmission and reflection with appropriate wavelength calibration, reference substrates and sample thickness. Determine whether an apparent absorption edge could be affected by surface roughness or scattering. Report spectral ranges and integration methods when comparing optical figures of merit.



#### Engineering use and tradeoffs

A window coating may need both visible transparency and infrared control; a photodetector requires sensitivity, noise control and stable packaging. Neither is adequately assessed from one visible photograph.



#### Scope and common failure of reasoning

Do not equate optical transparency with electrical insulation or infer a device efficiency directly from its absorption spectrum.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **light interaction and photonic materials**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Thermal management stack

### Research question and hypotheses

Estimate steady conduction resistance for an insulating pad and then include a conceptual contact resistance. Explain which measured temperature gradients would indicate the pad, interface or boundary condition is dominant.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Select a measurement chain: thermal conductivity or diffusivity test, interface characterization, geometry control and actual device thermal trial. For an electrical conductor, compare two- and four-terminal testing to reveal contact effects.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

A device hot spot remains high after a high-conductivity material is substituted. Produce at least two plausible explanations and a targeted test to avoid another unproductive material change.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 7.1 — Electronics heat-spreader thickness

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **layer thermal resistance** using Thickness (mm) = 8.1; Conductivity (W/m/K) = 2; Area (cm²) = 50. The starting values are synthetic and describe no commercial product.

**Model.** `R_th = L/(kA)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute L=8.1, k=2, A=50 into the stated relation. The reproducibly evaluated result is **0.81 K/W**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Steady one-dimensional conduction; omits contact and losses.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 7.2 — Carrier concentration scenario

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **charge-carrier resistivity** using Carrier density (×10²⁸ m⁻³) = 0.93; Mobility (×10⁻³ m²/Vs) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `ρ = 1/(nqμ)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute n=0.93, mu=2 into the stated relation. The reproducibly evaluated result is **3.35565e-07 Ω·m**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **One carrier type; neglects contacts and field effects.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 7.3 — Insulation layer comparison

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **layer thermal resistance** using Thickness (mm) = 10; Conductivity (W/m/K) = 2; Area (cm²) = 50. The starting values are synthetic and describe no commercial product.

**Model.** `R_th = L/(kA)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute L=10, k=2, A=50 into the stated relation. The reproducibly evaluated result is **1 K/W**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Steady one-dimensional conduction; omits contact and losses.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 7.4 — Contact material resistivity

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **charge-carrier resistivity** using Carrier density (×10²⁸ m⁻³) = 1.08; Mobility (×10⁻³ m²/Vs) = 2. The starting values are synthetic and describe no commercial product.

**Model.** `ρ = 1/(nqμ)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute n=1.08, mu=2 into the stated relation. The reproducibly evaluated result is **2.88959e-07 Ω·m**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **One carrier type; neglects contacts and field effects.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 7.5 — Packaging thermal bottleneck

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **layer thermal resistance** using Thickness (mm) = 11.7; Conductivity (W/m/K) = 2; Area (cm²) = 50. The starting values are synthetic and describe no commercial product.

**Model.** `R_th = L/(kA)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute L=11.7, k=2, A=50 into the stated relation. The reproducibly evaluated result is **1.17 K/W**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Steady one-dimensional conduction; omits contact and losses.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_12 -->

<!-- INTERACTIVE_MODEL_13 -->

## Concept synthesis and oral examination

Discuss how **heat capacity and thermal expansion** can be connected to **light interaction and photonic materials** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
