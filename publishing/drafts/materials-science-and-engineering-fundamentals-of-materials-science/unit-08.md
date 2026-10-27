# Unit 8: Manufacturing, selection, degradation and sustainability

> **Guiding question:** How should an engineer turn incomplete test data into a justified, maintainable and lower-impact materials decision?

## Conceptual overview

A good materials decision makes the manufacturing sequence part of the specification. The cast, forged, welded, printed or molded state is not incidental: it creates the microstructure that determines measured properties. Additive manufacturing offers geometric freedom but can produce layer-dependent defects and residual stress. Joining adds local thermal and chemical histories. Surface finishes and coatings can improve service life while introducing new interfaces to inspect.

Degradation changes the ranking over time. A corrosion-resistant candidate in dry laboratory air may corrode in a chloride crevice, while an inexpensive polymer may lose strength under ultraviolet exposure or solvent contact. Accelerated tests help compare candidates, but only if they preserve the field failure mechanism. A temperature-accelerated chemical process is not necessarily equivalent to a fatigue-corrosion problem in seasonal outdoor service.

Quantitative screening is useful but demands correctly defined objectives. Specific strength divides a strength measure by density; it does not automatically solve a beam-buckling problem. A material index is derived from constraints and geometry, which means the correct exponent changes with the structural problem. All weighted rankings should be rerun under alternate prices, property bounds, maintenance assumptions and supply scenarios. Hard safety requirements should be filtered out before ranking.

Circular design requires a system view. Material production energy, manufacturing yield, useful life, operational efficiency, repair, recovery and end-of-life treatment affect the net outcome. Data are often incomplete; analysts should show assumptions and sensitivity ranges. A synthetic teaching dataset teaches arithmetic, not a product's verified carbon footprint. The end product of this unit is an auditable recommendation explaining why a material was retained, what could make the decision wrong and which inexpensive test would most efficiently reduce uncertainty.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 8.1 Casting, forming and additive routes

#### Mechanism and vocabulary

Manufacturing history defines microstructure through heat flow, deformation, phase transformation and defect creation. Casting can form complex shapes but may suffer shrinkage and segregation. Forming introduces texture and work hardening. Layerwise additive manufacturing can produce geometry efficiently but may introduce directionality, residual stress and porosity.



#### Measurement and evidence

Compare process records with sample locations inside a component. Use nondestructive testing to screen defects, then destructively characterize selected coupons. Record build direction and scan strategy for additively manufactured samples; record strain and temperature history for rolled or forged components.



#### Engineering use and tradeoffs

A component optimized purely for material mass may require an expensive process with high scrap or poor inspection access. A design-for-manufacture comparison includes tooling, energy, throughput, tolerances and joining options as well as raw material price.



#### Scope and common failure of reasoning

Process-specific properties should not be replaced by generic wrought handbook values. A small coupon from the best region may conceal unacceptable variability.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **casting, forming and additive routes**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 8.2 Joining, coating and interfaces

#### Mechanism and vocabulary

Components are assemblies, and interfaces often determine performance. Welding changes the nearby microstructure through a thermal cycle. Adhesives transmit load through interfaces and can age with environment. Coatings control corrosion, wear or optical behavior but introduce their own adhesion and defect concerns.



#### Measurement and evidence

Document surface preparation, cleaning, cure or welding variables and resulting interface geometry. Inspect cross sections and run appropriate peel, shear or fracture tests. Distinguish a coating pinhole from a bulk-material failure.



#### Engineering use and tradeoffs

A multi-material enclosure might combine a stiff metal shell with a polymer seal. Its field reliability depends on expansion mismatch, galvanic coupling, seal creep and repair procedures rather than merely the best individual material.



#### Scope and common failure of reasoning

A high coupon-level joint strength does not prove durability under moisture, thermal cycling or fatigue. Do not treat adhesive datasheet values as universal design allowables.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **joining, coating and interfaces**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 8.3 Corrosion, oxidation and environmental aging

#### Mechanism and vocabulary

A material may degrade through electrochemical corrosion, high-temperature oxidation, ultraviolet exposure, solvent attack, fatigue–corrosion interaction or other environment-specific processes. The damage rate depends on chemistry, transport, mechanical stress, protective films and local geometry.



#### Measurement and evidence

Establish service chemistry, including chloride, pH, oxygen, humidity and temperature when relevant. Use controlled exposures with appropriate reference coupons and inspect both mass loss and localized attack. A very low average corrosion rate can coexist with dangerous pits or crevice attack.



#### Engineering use and tradeoffs

Marine fasteners, outdoor polymer housings and hot gas paths require different protective strategies. A coating can postpone damage but inspection and maintenance must remain feasible. Material substitution can shift rather than eliminate the dominant failure mode.



#### Scope and common failure of reasoning

Accelerated aging is not automatically an exact clock conversion to real-world lifetime. Changed mechanisms at elevated temperature or concentration can invalidate extrapolation.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **corrosion, oxidation and environmental aging**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 8.4 Material indices and decision matrices

#### Mechanism and vocabulary

Selection begins with function, constraints, objective and free variables. Material indices such as specific stiffness or specific strength can rank candidates only when the relevant structural model and constraints are correctly specified. A decision matrix can organize evidence but numerical weights encode human priorities rather than laws of nature.



#### Measurement and evidence

Start with must-meet constraints such as operating temperature, fatigue life, supply availability and regulatory requirements. Then calculate indices using units consistently and perform sensitivity analysis on uncertain inputs. Mark property data as typical, minimum, tested or estimated.



#### Engineering use and tradeoffs

A lightweight enclosure might favor polymer on mass and cost but fail a flammability constraint. An aerospace part may accept high material cost to save mass if service and certification costs support the decision. Engineering feasibility is not a single-number ranking.



#### Scope and common failure of reasoning

A weighted score can conceal a hard failure. Never let an excellent price score compensate for a safety constraint that a candidate cannot meet.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **material indices and decision matrices**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 8.5 Life cycle, circularity and responsible innovation

#### Mechanism and vocabulary

Environmental impact depends on a product system, not just a material label. Extraction, manufacturing yield, process energy, use-phase performance, maintenance and end-of-life scenarios can all dominate a cradle-to-grave result. Comparative life-cycle assessments require a common functional unit and transparent system boundaries.



#### Measurement and evidence

Build an inventory of masses, energy and replacement intervals with separate data-quality labels. Compare scenarios using the same service function and lifetime. Test sensitivity to recycling assumptions and electricity supply. Note emissions or impacts omitted because evidence is unavailable.



#### Engineering use and tradeoffs

A heavier durable component can sometimes have lower lifetime impact than a lighter one that must be replaced frequently; the opposite can also hold. Circularity requires recoverable design, viable collection and processing routes, not merely nominal technical recyclability.



#### Scope and common failure of reasoning

Do not claim carbon neutrality or sustainability based on a single recycled-content percentage. A synthetic classroom inventory is not an independently reviewed environmental product declaration.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **life cycle, circularity and responsible innovation**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Auditable, lower-impact component decision

### Research question and hypotheses

Define a functional unit, a service-life requirement and a system boundary before comparing candidate materials. Calculate synthetic production emissions and rerun the comparison with replacement intervals and scrap-rate assumptions.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Create a decision matrix that filters hard safety constraints first, then weighs cost, mass, repair and environmental impacts. Show sensitivity to uncertain property data instead of reporting a single false-precision score.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

A supplier advertises a material as carbon neutral using an unspecified factor. Draft an evidence request that separates inventory data, allocation, boundaries, offsets and independent verification.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 8.1 — Cradle-to-gate mass screen

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **embodied carbon screening** using Mass (kg) = 16; Emission factor (kg CO₂e/kg) = 3.5. The starting values are synthetic and describe no commercial product.

**Model.** `G = mass × assumed emission factor`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute m=16, f=3.5 into the stated relation. The reproducibly evaluated result is **56 kg CO₂e**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Synthetic screening; not a verified life-cycle inventory.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 8.2 — Specific-stiffness shortlist

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **stiffness-weight index** using Young modulus (GPa) = 65; Density (kg/m³) = 2700. The starting values are synthetic and describe no commercial product.

**Model.** `M = √E / ρ`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute E=65, r=2700 into the stated relation. The reproducibly evaluated result is **94.4263 index units**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Illustrative for a defined bending-dominated variable-section case only.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 8.3 — Remanufacture material saving

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **embodied carbon screening** using Mass (kg) = 20; Emission factor (kg CO₂e/kg) = 3.5. The starting values are synthetic and describe no commercial product.

**Model.** `G = mass × assumed emission factor`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute m=20, f=3.5 into the stated relation. The reproducibly evaluated result is **70 kg CO₂e**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Synthetic screening; not a verified life-cycle inventory.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 8.4 — Density-driven design alternative

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **stiffness-weight index** using Young modulus (GPa) = 76; Density (kg/m³) = 2700. The starting values are synthetic and describe no commercial product.

**Model.** `M = √E / ρ`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute E=76, r=2700 into the stated relation. The reproducibly evaluated result is **102.104 index units**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Illustrative for a defined bending-dominated variable-section case only.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 8.5 — Replacement cycle sensitivity

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **embodied carbon screening** using Mass (kg) = 23; Emission factor (kg CO₂e/kg) = 3.5. The starting values are synthetic and describe no commercial product.

**Model.** `G = mass × assumed emission factor`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute m=23, f=3.5 into the stated relation. The reproducibly evaluated result is **80.5 kg CO₂e**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Synthetic screening; not a verified life-cycle inventory.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_14 -->

<!-- INTERACTIVE_MODEL_15 -->

## Concept synthesis and oral examination

Discuss how **casting, forming and additive routes** can be connected to **life cycle, circularity and responsible innovation** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
