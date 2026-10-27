# Unit 6: Metals, ceramics, polymers, composites and electronic materials

> **Guiding question:** Which material family is suitable when more than one property and several manufacturing constraints matter?

## Conceptual overview

Materials families provide useful first approximations, but a family is too broad to specify a component. Metals typically offer useful electrical conduction and plasticity, yet alloys span orders of magnitude in corrosion resistance and mechanical response. Ceramics often perform well under heat or wear, but their defect sensitivity is crucial. Polymers may be economical and formable, while their response depends strongly on time and temperature. Composites combine constituents whose geometry and interface performance largely determine anisotropy.

The distinction between intrinsic and effective properties matters. A dense alumina crystal and a porous alumina component will not have the same strength or heat transport. A composite fiber may possess exceptional stiffness, yet the laminate can fail by delamination or compressive microbuckling. A semiconductor wafer can have excellent mobility but poor device yield if contamination and contacts are uncontrolled. In each case, the material of interest is the manufactured structure, not an ideal constituent.

Testing should reflect the actual loading direction. A unidirectional composite is often strong and stiff along the fibers but much less so across them. The ideal longitudinal rule of mixtures assumes equal strain and effective load transfer; it cannot predict transverse or impact failure. Likewise, a polymer evaluated at a slow test speed can perform differently under a short impact, and a ceramic flexural coupon can fail from the condition of its tensile surface.

The engineering choice links material and process. Welding compatibility may rule out a promising metal. A polymer suitable for injection molding may be poorly suited to an adhesive-based repair system. A ceramic can require costly sintering controls and finish machining. The best first decision is a shortlist whose candidates are testable under a clear specification, not a single heroic material name.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 6.1 Engineering metals and alloys

#### Mechanism and vocabulary

Metals combine mobile electronic carriers with a broad range of crystal structures and deformation mechanisms. Alloying and processing change phase fractions, precipitates and grain structure. Steel is not one material: chemistry, heat treatment and product form generate many grades whose performance must be specified.



#### Measurement and evidence

Inspect a mill certificate, product standard and actual process history. Test weld heat-affected zones where joining is central to the application. Correlate microstructure with hardness and tensile data rather than selecting by generic family labels.



#### Engineering use and tradeoffs

A corrosion-resistant stainless steel can be a poor high-temperature choice in a specific chloride atmosphere; an aluminum alloy may save mass but need different joining and surface protection. The choice is application-specific, not a contest between family names.



#### Scope and common failure of reasoning

Do not treat handbook values as guaranteed minima or mix values from different temper conditions.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **engineering metals and alloys**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 6.2 Structural ceramics and glasses

#### Mechanism and vocabulary

Ceramics have bonding and structural arrangements that often produce high hardness and chemical stability, but flaw sensitivity and limited plasticity can dominate structural design. Porosity, grain boundaries and residual stresses introduced by processing can significantly alter strength. Glass is an amorphous subset rather than a synonym for all ceramics.



#### Measurement and evidence

Measure density and porosity, inspect surfaces for machining damage and specify test configuration. Flexural strength results depend on tensile surface condition; small polished coupons can appear stronger than full-scale parts because failure probability grows with stressed volume or surface area.



#### Engineering use and tradeoffs

Ceramic cutting tools tolerate temperature and wear, while glass fibers carry tensile load when their small diameters reduce severe flaws. Large transparent panels require different safety design, protective layers and defect controls.



#### Scope and common failure of reasoning

High hardness is not equivalent to high fracture toughness. Weibull parameters require sufficient valid data and cannot be invented from a few measurements.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **structural ceramics and glasses**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 6.3 Polymers and viscoelasticity

#### Mechanism and vocabulary

Polymer chains gain mobility through molecular rotation and rearrangement, so stiffness and damping depend strongly on temperature and loading time. Thermoplastics, thermosets and elastomers describe different architectures and processing possibilities; degree of crystallinity and additives further diversify behavior.



#### Measurement and evidence

Run a dynamic mechanical analysis or time-dependent tensile experiment over a meaningful temperature range. Control moisture and physical aging when these affect the polymer. Compare tests at different strain rates rather than relying on a single room-temperature stress–strain curve.



#### Engineering use and tradeoffs

A polymer hinge may withstand repeated flexure yet creep under sustained load. Packaging design values impact resistance and barrier properties, whereas an electrical enclosure also requires flammability and dimensional stability evaluations.



#### Scope and common failure of reasoning

Never assume a plastic modulus is constant across temperatures or that recyclability alone proves a favorable lifecycle footprint.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **polymers and viscoelasticity**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 6.4 Fiber composites and interfaces

#### Mechanism and vocabulary

A composite combines constituents whose combined response depends on geometry, orientation, volume fraction and interface integrity. For longitudinal loading of aligned continuous fibers under ideal equal-strain conditions, a rule of mixtures estimates axial modulus; transverse response and failure are more complicated.



#### Measurement and evidence

Specify fiber volume fraction, layup, cure history, void content and test direction. Measure interlaminar response where delamination matters. Compare predictions with coupon data and check if the load case is tension, compression, shear or impact.



#### Engineering use and tradeoffs

Composite airframes and wind-turbine blades can achieve high stiffness per unit mass, but repairability, moisture aging, impact damage and anisotropic failure require careful management. A material attractive in pure axial tension may be unsuitable for a bolted joint.



#### Scope and common failure of reasoning

Do not use the ideal axial rule of mixtures as a universal composite strength predictor. It neglects interface damage, defects and fiber misalignment.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **fiber composites and interfaces**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 6.5 Semiconductors and active materials

#### Mechanism and vocabulary

Semiconductors use electronic band structure and carrier concentrations to control current. Doping can shift the majority-carrier population, while defects, contacts and surfaces strongly influence device behavior. A material with useful electronic properties may still fail as a device because process contamination or interface states are poorly controlled.



#### Measurement and evidence

Distinguish four-point-probe resistivity, Hall measurements and current–voltage tests; they probe related but nonidentical quantities. Report temperature, illumination and contact geometry. Compare an ideal transport model with real contact resistance and recombination.



#### Engineering use and tradeoffs

Silicon, compound semiconductors and emerging thin films serve different niches based on bandgap, mobility, manufacturing maturity and environmental stability. Device selection must include fabrication yield and packaging, not only a calculated bandgap.



#### Scope and common failure of reasoning

The relation conductivity equals charge density times charge and mobility is a simplified transport identity; mixed carriers and field-dependent mobility require more care.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **semiconductors and active materials**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Lightweight composite panel selection

### Research question and hypotheses

Compare a metal, a polymer and a unidirectional laminate for an axial stiffness requirement. Compute an ideal composite axial modulus and identify the failure modes absent from that equation.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Create a procurement specification that includes volume fraction, laminate orientation, porosity, cure history, moisture condition and joining method. Show how missing any one can invalidate a nominal materials-data comparison.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

An impact event leaves barely visible damage in a laminate. Explain why a post-impact tension result and an undamaged coupon property are not equivalent, and plan an inspection pathway.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 6.1 — Composite panel stiffness

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **aligned-fiber axial modulus** using Fiber modulus (GPa) = 190; Matrix modulus (GPa) = 3; Fiber volume fraction = 0.55. The starting values are synthetic and describe no commercial product.

**Model.** `E_parallel = E_f V_f + E_m (1 − V_f)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ef=190, Em=3, vf=0.55 into the stated relation. The reproducibly evaluated result is **105.85 GPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Ideal isostrain aligned continuous fibers only.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 6.2 — Porous ceramic redesign

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **porosity modulus penalty** using Dense modulus (GPa) = 190; Porosity (%) = 12. The starting values are synthetic and describe no commercial product.

**Model.** `E_eff ≈ E₀(1 − φ)²`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute E0=190, p=12 into the stated relation. The reproducibly evaluated result is **147.136 GPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Illustrative empirical scaling, not a material-independent law.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 6.3 — Fiber volume optimization

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **aligned-fiber axial modulus** using Fiber modulus (GPa) = 230; Matrix modulus (GPa) = 3; Fiber volume fraction = 0.55. The starting values are synthetic and describe no commercial product.

**Model.** `E_parallel = E_f V_f + E_m (1 − V_f)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ef=230, Em=3, vf=0.55 into the stated relation. The reproducibly evaluated result is **127.85 GPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Ideal isostrain aligned continuous fibers only.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 6.4 — Powder-processing pore removal

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **porosity modulus penalty** using Dense modulus (GPa) = 220; Porosity (%) = 12. The starting values are synthetic and describe no commercial product.

**Model.** `E_eff ≈ E₀(1 − φ)²`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute E0=220, p=12 into the stated relation. The reproducibly evaluated result is **170.368 GPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Illustrative empirical scaling, not a material-independent law.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 6.5 — Direction-dependent stiffness

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **aligned-fiber axial modulus** using Fiber modulus (GPa) = 270; Matrix modulus (GPa) = 3; Fiber volume fraction = 0.55. The starting values are synthetic and describe no commercial product.

**Model.** `E_parallel = E_f V_f + E_m (1 − V_f)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute Ef=270, Em=3, vf=0.55 into the stated relation. The reproducibly evaluated result is **149.85 GPa**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Ideal isostrain aligned continuous fibers only.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_10 -->

<!-- INTERACTIVE_MODEL_11 -->

## Concept synthesis and oral examination

Discuss how **engineering metals and alloys** can be connected to **semiconductors and active materials** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
