# Unit 2: Crystal structures and structural determination

> **Guiding question:** What does periodic atomic order reveal, and what remains hidden without a measurement of defects and texture?

## Conceptual overview

Periodic order is powerful because it restricts which atomic arrangements can repeat through space. The shortest description often uses lattice vectors and a basis, but the easiest cell to draw is not always primitive. An FCC conventional cubic cell has four net lattice points, not the visually tempting eight corner atoms plus six whole face atoms. Each corner belongs to eight adjacent cells and each face atom to two. BCC has two net lattice points per conventional cubic cell. These counting rules are not decorations; they enter theoretical-density calculations and predictions about diffraction.

A crystal can be geometrically ordered and still contain point, line and planar defects. The Bravais lattice describes ideal translational symmetry, while the specimen contains grain orientations and interfaces. That distinction explains why a powder and a single crystal of the same chemical phase can give radically different diffraction images. Powder patterns average over many orientations; single-crystal diffraction retains angular information. Textured sheet lies between these extremes and can produce biased intensity distributions.

Indices are useful only if the frame of reference is unambiguous. Interplanar-spacing equations depend on lattice geometry; the cubic expression is simpler because of the metric symmetry. Miller indices describe geometric plane families, not chemical formulas. When reading a diffraction scan, remember that instruments conventionally report two-theta; the angle in the sine term of Bragg's law is theta. A factor-of-two mistake can produce a physically impossible spacing while giving an apparently plausible number.

Crystallinity has gradations. An amorphous silica glass possesses local coordination and meaningful near-neighbor distances. Polymers frequently combine ordered lamellar regions and more mobile amorphous regions. Grain-size broadening, microstrain, small coherent domain size and instrument resolution can each broaden a diffraction feature. A responsible report separates direct observations—peak position, width, intensity—from inferred models and their assumptions. Structure determination becomes strongest when complementary measurements point to the same explanation.

## Learning outcomes

After completing this unit, a student should be able to state the relevant physical mechanisms, define the operational measurement and its units, solve an idealized numerical problem with a unit check, identify competing explanations for a trend, evaluate one manufacturing tradeoff and write an evidence-based decision memo. The outcomes should be judged through worked calculations and a specific observation plan, not just by the ability to repeat terminology.

## Five core lessons

### 2.1 Unit cells and atomic packing

#### Mechanism and vocabulary

Crystalline solids exhibit translational order described with lattice vectors and a basis of atoms. A primitive cell reproduces a lattice with translation; a conventional cubic cell may be larger but expresses symmetry conveniently. FCC, BCC and HCP structures have different nearest-neighbor environments. Packing factor is a geometric descriptor, not a complete predictor of engineering performance.



#### Measurement and evidence

Build physical or digital sphere models and count fractional atomic contributions at cell corners, faces and body positions. For a monoatomic FCC conventional cell, the atom count is four. Verify that the selected cell geometry agrees with the radius-contact relation before calculating theoretical density.



#### Engineering use and tradeoffs

An alloy can change lattice parameter as composition varies; an interstitial solute can distort the host. Such differences shift diffraction peaks, but the peak shift alone may also reflect residual stress or temperature. State which explanation a measurement can discriminate.



#### Scope and common failure of reasoning

Do not confuse a lattice with an alloy phase, or assume all metals have the same close-packed structure. FCC and HCP share a high hard-sphere packing fraction but differ in symmetry.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **unit cells and atomic packing**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 2.2 Directions, planes and anisotropy

#### Mechanism and vocabulary

Crystallographic directions are denoted with bracket indices, while plane families use a different notation. In a cubic lattice, the spacing of planes with indices hkl scales as a divided by the square root of h squared plus k squared plus l squared. The symmetry of the crystal constrains how elastic, optical and transport properties vary with direction.



#### Measurement and evidence

Use a lattice sketch to draw an intercept plane, convert fractional intercepts to integer Miller indices and check the orientation by tracing parallel planes. For textured rolled sheet, compare longitudinal and transverse tests; an isotropic assumption should be checked rather than inherited.



#### Engineering use and tradeoffs

Sheet metal forming may expose directional ductility, whereas single-crystal turbine components exploit carefully controlled orientation. Processing can orient grains so that a polycrystal develops macroscopic anisotropy even when its grains each obey the same crystal symmetry.



#### Scope and common failure of reasoning

The cubic interplanar-spacing formula cannot be used unchanged for hexagonal or other noncubic cells. Also distinguish a direction [hkl] from a plane (hkl).



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **directions, planes and anisotropy**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 2.3 X-ray diffraction and Bragg condition

#### Mechanism and vocabulary

X-ray diffraction arises from interference among scattered waves, not from a photographic image of individual atoms. The familiar relation n lambda equals 2d sin theta predicts directions of constructive interference from equally spaced planes. Peak positions give structural information; peak widths and intensities also depend on instrumentation, crystallite size, strain, preferred orientation and scattering factors.



#### Measurement and evidence

Collect a calibration standard before a specimen; report radiation wavelength, two-theta range, step size and instrumental broadening. Convert observed two-theta into theta before solving the Bragg equation. Identify plausible phase assignments using multiple reflections rather than one attractive match.



#### Engineering use and tradeoffs

Powder diffraction is powerful for phase identification in a metal, ceramic or battery material, but a minor phase may be concealed by peak overlap or detection limits. A broad amorphous feature should not be forced into a crystalline indexing scheme.



#### Scope and common failure of reasoning

A strong peak does not prove abundant phase fraction without accounting for structure factors and preferred orientation. The simple Scherrer estimate is not a unique measurement of grain size.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **x-ray diffraction and bragg condition**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 2.4 Reciprocal space and orientation maps

#### Mechanism and vocabulary

Reciprocal-space vectors encode plane spacing and direction in a way useful for diffraction. The Ewald sphere provides a geometric view of scattering conditions. Polycrystals produce rings or ensembles of reflections, while a single crystal gives a more discrete pattern. Texture maps show preferred orientation and can connect manufacturing routes with anisotropic response.



#### Measurement and evidence

Compare a single-crystal pattern, a randomly oriented powder pattern and a textured sample. Keep detector geometry explicit and avoid interpreting a missing spot as a missing atomic species. Orientation mapping by electron backscatter diffraction requires careful polishing and appropriate indexing confidence.



#### Engineering use and tradeoffs

During sheet rolling, grains rotate and sometimes recrystallize. Texture data can help explain earing during deep drawing, but one must also measure strain paths and geometry. The diffraction pattern is evidence about orientation, not a full constitutive model.



#### Scope and common failure of reasoning

Reciprocal-lattice vectors are mathematical descriptors; do not draw them as literal rods inside the crystal. Instrument geometry must be included before comparing angles.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **reciprocal space and orientation maps**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

### 2.5 Glasses and partial order

#### Mechanism and vocabulary

Amorphous does not mean completely random. Glasses preserve short-range bonding preferences without the long-range translational periodicity of a crystal. Polymers may contain both ordered lamellae and amorphous regions, and many engineering ceramics contain glassy grain boundaries. Structural descriptors depend on the correlation length of the measurement.



#### Measurement and evidence

Compare sharp diffraction features with broad diffuse scattering, and explain why both may appear in a semicrystalline polymer. Use calorimetry to look for a glass transition; distinguish that kinetic transition from a first-order melting peak. Examine thermal history because rapid cooling can retain nonequilibrium structure.



#### Engineering use and tradeoffs

A transparent glass can be chemically resistant and dimensionally stable yet prone to brittle fracture. A partially crystalline polymer may show improved stiffness but lower transparency. Processing chooses a distribution of structures rather than just a label crystalline or amorphous.



#### Scope and common failure of reasoning

A lack of strong diffraction peaks is not proof that a specimen has zero crystallinity; finite detection sensitivity and very small coherent domains matter.



#### Questions for independent study

1. Define the most important structural or mechanistic quantity in **glasses and partial order**. How does it differ from a directly measured instrument output?
2. Starting from the scenario above, specify an experimental control and one possible misleading correlation. Which observation would discriminate the two explanations?
3. Explain what would change if the component had a different processing history, orientation, size or temperature. Identify at least one property that might worsen.
4. Write a decision criterion using units and a justified safety constraint. What missing information would prevent a valid pass/fail decision?

## Unit investigation: Structure assignment from synthetic diffraction

### Research question and hypotheses

Generate a hypothetical powder scan with two candidate phase families; compare peak positions under a cubic assumption and ask which additional reflections distinguish the phases. Separately inspect whether thermal strain could shift the peaks.

**Hypothesis A:** A controlled difference in material structure or processing changes an operational performance measure. **Alternative B:** The apparent change is primarily caused by specimen geometry, environmental conditions, measurement artifact or selection. Write a mechanism-based prediction for both hypotheses before processing observations. Where the synthetic dataset can discriminate neither explanation, make the limitation explicit instead of claiming statistical significance.

### Method and controls

Define at least three repeat specimens per condition for a classroom pilot, while noting that a serious reliability claim typically needs a much more extensive sample plan. Record composition or material grade, supplier lot, thermal and forming history, orientation, dimensions, specimen condition, instrument calibration, loading or temperature protocol and environmental exposure. Randomize run order where a warming instrument or operator drift might bias comparison. For microstructure, define the number of fields, scale bars and segmentation approach before examining the most attractive image. For electrical, mechanical or thermal tests, list geometry assumptions in advance.

Where hazard is possible, this investigation is a paper or computer study until appropriate training, supervision and facilities are available. Do not perform uncontrolled high-temperature treatment, powered fracture experiments, chemical corrosion exposures, or work with airborne powders. The goal is to learn a defensible analytical workflow, not to reproduce industrial hazards.

### Numerical analysis plan

Build physical models of BCC and FCC cells and explain atomic sharing. Calculate one interplanar spacing and compare it with the interactive Bragg-angle model. Keep lattice labels separate from phase identification.

Before fitting a complex model, check conservation and units. Calculate the appropriate quantity using the simpler chapter formula and vary one parameter. Present a short table distinguishing synthetic input, calculated output, direct observation, assumption and proposed external validation. If measurements are available, plot the raw data rather than only a fitted line. Use uncertainty bars or plausible ranges where repeated measurements support them. Record residual patterns: systematic curvature is a warning that a linearized approximation is incomplete, not an invitation to report a misleadingly precise slope.

### Case-based challenge

A broad shoulder appears where the analyst expects a weak second phase. Write three plausible explanations and choose an independent method that tests each, rather than automatically claiming a discovery.

### Deliverables and grading rubric

Submit a one-page specification; a diagram connecting processing, structure, property and performance; a reproducible dataset and calculation; a one-page evidence table distinguishing observation, interpretation and confounder; and a decision memo with limitations and a targeted next experiment. Award equal credit to defensible negative results and positive results. Grade the scientific chain and transparency, not whether the student chose a fashionable material. A strong submission explains at least one way its preferred conclusion might fail and proposes a practical falsification test.

## Five solved numerical cases

#### Worked case 2.1 — Cubic structure worksheet

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **cubic lattice spacing** using Lattice parameter (nm) = 0.324; Miller h = 1; Miller k = 1; Miller l = 1. The starting values are synthetic and describe no commercial product.

**Model.** `d_hkl = a / √(h²+k²+l²)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute a=0.324, h=1, k=1, l=1 into the stated relation. The reproducibly evaluated result is **0.187061 nm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Change one material property independently of geometry before extending the result to a component. For this case, **Cubic metric only; (0,0,0) is not a valid plane.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 2.2 — Texture-aware diffraction

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **first-order bragg angle** using Wavelength (nm) = 0.1432; Spacing (nm) = 0.25. The starting values are synthetic and describe no commercial product.

**Model.** `θ = arcsin(λ/(2d))`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute lam=0.1432, d=0.25 into the stated relation. The reproducibly evaluated result is **16.6426 degrees θ**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Compare the calculated trend with a physical limiting case, especially near the edge of the permitted input range. For this case, **Reports θ, whereas diffractometers usually report 2θ.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 2.3 — Phase identification scan

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **cubic lattice spacing** using Lattice parameter (nm) = 0.4; Miller h = 1; Miller k = 1; Miller l = 1. The starting values are synthetic and describe no commercial product.

**Model.** `d_hkl = a / √(h²+k²+l²)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute a=0.4, h=1, k=1, l=1 into the stated relation. The reproducibly evaluated result is **0.23094 nm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Do not interpret more printed digits as more reliable knowledge: the synthetic inputs contain uncertainty. For this case, **Cubic metric only; (0,0,0) is not a valid plane.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 2.4 — Interplanar spacing check

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **first-order bragg angle** using Wavelength (nm) = 0.1663; Spacing (nm) = 0.25. The starting values are synthetic and describe no commercial product.

**Model.** `θ = arcsin(λ/(2d))`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute lam=0.1663, d=0.25 into the stated relation. The reproducibly evaluated result is **19.4267 degrees θ**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Explain the direction of change and whether the adjustment would create a new manufacturing or service penalty. For this case, **Reports θ, whereas diffractometers usually report 2θ.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

#### Worked case 2.5 — Detector peak interpretation

**Question.** Under a hypothetical, precisely defined teaching condition, estimate **cubic lattice spacing** using Lattice parameter (nm) = 0.468; Miller h = 1; Miller k = 1; Miller l = 1. The starting values are synthetic and describe no commercial product.

**Model.** `d_hkl = a / √(h²+k²+l²)`. Input values refer to the units stated in the question; the corresponding calculator contains the needed unit conversions.

**Calculation.** Substitute a=0.468, h=1, k=1, l=1 into the stated relation. The reproducibly evaluated result is **0.2702 nm**. If the formula has a square root or an exponential, check that its argument is dimensionally appropriate before substituting numbers. Verify the result's order of magnitude, not just its decimal digits.

**Interpretation.** Translate the result into a testable requirement and identify at least one omitted failure mechanism. For this case, **Cubic metric only; (0,0,0) is not a valid plane.** Hence the numerical result is an illustration of model behavior, not an acceptance limit or safety certificate. Propose an instrument or controlled experiment that could show whether the model is sufficiently accurate for the proposed application.

**Sensitivity question.** Change the first input by roughly ten percent while holding the others constant. Predict whether the answer rises or falls, recalculate using the model and explain any nonlinear response. Then discuss whether those quantities could realistically vary independently in a manufactured component. State the missing data necessary to proceed from classroom arithmetic to component design.

## Guided model experiments

The two calculators below are simplified pedagogical models. Begin at the default parameters and write a physical prediction for the effect of changing the first variable. Move the slider to both ends; then change a second variable and test whether the sensitivity remains similar. Consult the printed equations and applicability limits before interpreting an output. No calculated value is a verified design allowable.

<!-- INTERACTIVE_MODEL_2 -->

<!-- INTERACTIVE_MODEL_3 -->

## Concept synthesis and oral examination

Discuss how **unit cells and atomic packing** can be connected to **glasses and partial order** through a measurable, falsifiable process–structure–property chain. Give a direct observation and a competing explanation for each link. Compare a specimen-level property with a real component constraint, and identify a mechanism that is not represented by the current calculator. Ask what practical evidence is needed before substituting a new material into an existing design. Explain how uncertainty, traceability, cost and service environment alter the decision even if the idealized calculated value appears better. End by explaining one situation in which *not selecting a new material* is the scientifically justified result because the cost and risk of verification exceed the demonstrated benefit.
