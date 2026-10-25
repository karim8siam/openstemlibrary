# Unit 01 — Homeostasis, transport and physiological scaling

> **Animal Physiology — OpenSTEM Book 11.** From local membrane processes to whole-animal regulated variables: why constancy is an active achievement. All numerical case values in this book are **synthetic teaching data**, not measurements, clinical advice or husbandry recommendations. This editorial draft has not received independent peer review.

## What the unit asks you to explain

Physiology is a quantitative study of how living structures accomplish work and keep conditions within tolerable ranges. This unit examines homeostasis, transport and physiological scaling while connecting molecular mechanisms to whole-organism outcomes. The goal is not only to identify a named structure or pathway, but to predict the direction of change, the time needed for a response, and the observation that would distinguish a proposed mechanism from an alternative. Learners should keep conservation of matter or energy in view whenever they write an equation.

By the end of this unit, you should be able to (i) explain its five linked topics in physical and biological terms; (ii) calculate and interpret five dimensioned toy examples; (iii) decide which measurements distinguish input, state and output; (iv) identify failure modes of the models; and (v) design an ethical comparison while naming confounding factors. Prerequisites are first-year biology, elementary chemistry, algebra, and an ability to read plots. Differential equations are discussed conceptually where useful but are not assumed.


## Working distinctions

regulated variable versus measured proxy; transport rate versus stored amount; timescale and physical size; feedback versus feedforward action; tissue specificity and comparative caution. A useful unit-wide habit is to separate direct measurements from inferred flows, clearly stating physical units and time windows.


## Integrated systems lens — Failure of a regulator is most visible under load

Physiological experiments become informative when the investigator distinguishes a target variable from the motor mechanisms that help stabilize it. If plasma osmolarity stays nearly unchanged, one possibility is strong renal control; another is that food and water inputs barely varied. The same concentration can also occur through a large water increase accompanied by a proportional solute increase. Thus a concentration observation has to be paired with a volume estimate and transport information. In practice, rigorous studies describe what was measured, where it was measured and over what interval.

Consider two animals placed in the same mild environmental disturbance. The first exhibits a small immediate deviation and rapid recovery; the second exhibits a larger deviation but returns to baseline faster. One cannot decide which has better homeostasis from a single endpoint. Plot controlled-variable error against time, then compare peak error, time to peak, integral of absolute error and final state. These are different performance criteria and need not rank the animals identically. Control also consumes energy and material; a response with a low error might be costly or unsustainable.

A system may compensate in ways that conceal a weakened organ. Imagine an epithelial defect that increases sodium leakage. Greater pump activity might maintain concentration while increasing oxygen consumption and ATP demand. The expected symptom appears only if the capacity to compensate is exceeded. For this reason physiology distinguishes resting state from reserve capacity: the maximum additional transport, flow or work that the system can achieve when challenged. Measurement under a tolerated load can reveal that reserve without exposing animals to harmful conditions.

Surface-area and volume arguments explain why small and large animals cannot exchange substances through the same geometry without modification. For a simple geometric body, area scales as length squared while volume scales as length cubed. If all dimensions double, area grows fourfold but volume eightfold. Yet the actual organism has folded epithelia, ventilatory movement and circulatory distribution. Therefore an area-to-volume ratio is a useful starting constraint but not a complete mechanism explaining observed metabolic scaling exponents.

An informative physiological model separates four layers: an environmental input, a transport law, a compartment state, and a controller modifying the transport coefficients. It is easy to write a plausible differential equation for one layer and then mistakenly treat its output as a prediction for the entire animal. For example an exponential recovery curve describes what happens if the restoring influence scales with error and the gain stays fixed. If there are thresholds, saturation, hormone delay or state-dependent transporters, recovery will differ. Model residuals indicate which assumptions should be reconsidered.

Ethically meaningful comparisons avoid asking animals to withstand extremes merely to make differences obvious. Naturalistic changes, archived measurements, organ-on-chip methods and observational time series can answer many questions. In an introductory course, synthetic examples provide arithmetic practice while explicitly separating the teaching numbers from factual biological ranges. Scientific conclusions depend on appropriate evidence, not the visual attractiveness of a fitted curve.

## Five linked physiological topics

### 1.1 — Controlled variables and negative feedback

#### Biological mechanism and scope

The internal environment of an animal is dynamic, not literally constant. Extracellular ion concentration, temperature, blood volume and acid-base state change when an animal eats, moves or encounters a heat wave. A regulated quantity remains within tolerable limits because sensors detect deviations, integrators compare current conditions with an operating range, and effectors change transport or production rates. A control loop can overshoot or oscillate if delays are long.

#### Comparisons, exceptions and organism-level interpretation

Do not mistake a single normal reading for successful regulation: a damaged system may still appear normal until a load is imposed. A rise in plasma solute concentration can trigger thirst and renal conservation of water, yet these responses have different onset times. A set point is better treated as a physiological operating target that may shift with circadian timing, fever or acclimation, not as a universal immutable number.

#### Observation, experiment and causal alternatives

Measure a controlled variable during a standardized perturbation and recovery rather than reporting a baseline alone. Compare animals receiving the same water challenge with differences in renal concentrating capacity. Monitor time-lag, amplitude and recovery slope. A saline infusion is not a neutral treatment: it changes both solute and volume, which must be analyzed separately.

#### Appropriate limits of the model

A feedback loop corrects an error after it arises whereas feedforward anticipates a predictable disturbance. Anticipatory increases in ventilation during movement do not prove that arterial blood gas error is absent; both forms of control often cooperate.


#### Mechanism-to-evidence test

A reported change in **controlled variables and negative feedback** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 01 — estimate, interpret, challenge

**Problem:** After a mild controlled disturbance, the measured variable is 105 units and the operating target is 95 units. Find the signed control error.

**Method:** `measured − target`. Substituting the given teaching values yields **10 units**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A positive error means the sensed quantity is above its target; corrective output need not be proportional to this error when control saturates. **Limits:** Do not infer physiological safety from the magnitude of an arbitrary-scale error. The sign convention is defined here, not universal. These are synthetic numbers, not measured organism values.


### 1.2 — Diffusion, gradients and transport resistance

#### Biological mechanism and scope

Biological diffusion is a probabilistic movement caused by random molecular collisions. A net flux emerges when concentrations differ; its direction is from higher toward lower chemical potential, which for ions also includes an electrical component. Flux rises with available area and driving gradient but declines as a barrier becomes thicker. A membrane channel differs from a pump because channels dissipate electrochemical gradients whereas pumps can maintain them using energy.

#### Comparisons, exceptions and organism-level interpretation

Thin respiratory epithelia favor fast gas exchange but are prone to injury and water loss. Enlarged surface area accelerates uptake yet increases exposure to toxins. Tight junctions restrict paracellular routes, and carriers saturate because transport proteins have finite cycling rates. A tissue can therefore display both near-linear passive permeability at low solute levels and saturable carrier-mediated uptake for a different substance.

#### Observation, experiment and causal alternatives

In a tracer experiment, independently estimate surface area, membrane thickness and external concentration. If treatment increases apparent clearance, it might alter blood flow rather than epithelial permeability. Follow the time course of the gradient; a flux recorded in the first second cannot be extrapolated unchanged after two minutes if the donor compartment is depleted.

#### Appropriate limits of the model

Fick's diffusion relation describes a steady-state idealization. It does not say every molecule moves along the net gradient or that oxygen movement is independent of dissolved solubility and local blood flow.


#### Mechanism-to-evidence test

A reported change in **diffusion, gradients and transport resistance** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 02 — estimate, interpret, challenge

**Problem:** A membrane model has D = 1.0×10⁻⁹ m²/s, area = 0.020 m², concentration difference = 2 mol/m³ and thickness = 1.0×10⁻⁵ m. Estimate steady diffusive molar flow.

**Method:** `D × area × gradient / thickness`. Substituting the given teaching values yields **4e-06 mol/s**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Doubling available area doubles this idealized flux if all other conditions remain unchanged. **Limits:** The relation assumes a constant effective diffusion coefficient and concentration difference across a homogeneous barrier. These are synthetic numbers, not measured organism values.


### 1.3 — Cell membranes and osmotic water movement

#### Biological mechanism and scope

Water crosses many biological membranes through lipid and aquaporin pathways. Osmosis reflects differences in effective particle concentration across barriers whose permeability to different solutes matters. A cell placed in concentrated impermeant solute tends to lose water, but an equally concentrated permeant solute may equilibrate and produce a very different volume response. Osmolarity and tonicity answer distinct questions.

#### Comparisons, exceptions and organism-level interpretation

Vertebrate cells lack a rigid cell wall and can swell or shrink rapidly. Regulatory volume increase and decrease use ion channels, exchangers and organic osmolytes to restore volume over minutes or hours. Abrupt water shifts may alter tissue function before slower transport adaptation becomes effective. Water balance must therefore be studied with both quantity and timescale in mind.

#### Observation, experiment and causal alternatives

Compare isolated cells exposed to sucrose and urea solutions with matched nominal osmolarity. Quantify radius changes while checking that the imaging medium does not disrupt membrane integrity. A cell-volume response supports a claim about effective osmotic particles under the assay conditions, not a definitive claim about whole-animal renal function.

#### Appropriate limits of the model

The equation for osmotic pressure is useful at dilute ideal concentrations. It should not be used to equate all solutions of the same total molar concentration with identical cell swelling.


#### Mechanism-to-evidence test

A reported change in **cell membranes and osmotic water movement** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 03 — estimate, interpret, challenge

**Problem:** For a hypothetical dilute ideal nonelectrolyte solution, osmolar solute concentration is 0.100 mol/L at 310 K. Use R = 8.314 J/(mol·K) to estimate ideal osmotic pressure in kilopascals.

**Method:** `C(mol/m³) × R × T / 1000`. Substituting the given teaching values yields **257.73 kPa**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Multiplying molar concentration by 1000 converts mol/L to mol/m³ before using SI pressure units. **Limits:** Membrane permeability and nonideal particle behavior determine whether this becomes an effective transmembrane pressure. These are synthetic numbers, not measured organism values.


### 1.4 — Epithelia and compartment balances

#### Biological mechanism and scope

Transporting epithelia maintain compartment differences by arranging channels and ATP-consuming pumps asymmetrically on apical and basolateral surfaces. A sodium gradient created by the basolateral sodium–potassium ATPase can indirectly drive nutrient uptake or ion secretion at the luminal membrane. Tight junction permeability determines whether movement between cells supports or undermines the transcellular route.

#### Comparisons, exceptions and organism-level interpretation

Mass balance separates what enters a compartment, what leaves it, and what accumulates. Concentration alone can change because of dilution even when solute quantity is stable. A blood constituent may fall after fluid infusion without any increase in its clearance. Likewise an organ may move a solute efficiently without causing high plasma concentration if delivery and removal adapt together.

#### Observation, experiment and causal alternatives

Use an epithelial chamber and record short-circuit current together with tracer flux. A rise in current implies a net movement of charge under clamped conditions but does not identify a particular ion without inhibitors, selectivity measurements and controls. Distinguish basal transport from the response to a hormone or secretagogue.

#### Appropriate limits of the model

A polarized sheet is not a bag of isolated cells. Geometry, barrier integrity, blood-side delivery and luminal flow jointly determine its physiological performance.


#### Mechanism-to-evidence test

A reported change in **epithelia and compartment balances** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 04 — estimate, interpret, challenge

**Problem:** A teaching fluid compartment receives 12 mg of a solute per minute and loses 9 mg/min. What is its immediate net accumulation rate?

**Method:** `input rate − output rate`. Substituting the given teaching values yields **3 mg/min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Over two minutes a constant 3 mg/min imbalance would add 6 mg, if no other routes change. **Limits:** Concentration can still decrease if compartment water volume expands faster than solute amount. These are synthetic numbers, not measured organism values.


### 1.5 — Metabolic scaling and size constraints

#### Biological mechanism and scope

Whole-animal function depends on dimensions. Volume grows faster than external area as a geometrically similar organism becomes larger, so distances for delivery, cooling and support do not scale trivially. Metabolic rate often follows a power relation with body mass across broad sets of species, but the fitted exponent depends on taxa, temperature, measurement conditions and analysis method.

#### Comparisons, exceptions and organism-level interpretation

Small mammals frequently show higher mass-specific resting energy use than large mammals. That observation does not mean a small animal has greater total energy consumption than a large one. A comparison of basking reptiles and mammals at different temperatures confounds body mass with physiology and environmental conditions. Scaling exponents should be estimated, not imposed on all groups as laws.

#### Observation, experiment and causal alternatives

Plot logarithm of metabolic rate against logarithm of body mass for an adequately sampled dataset and fit a slope with uncertainty. Exclude nonindependent repeated measures or model them properly. Check residuals against taxonomic group and ambient temperature; otherwise a neat straight line may hide biologically meaningful structure.

#### Appropriate limits of the model

An exponent is an empirical summary, not an explanation of the causes of energy use. Geometry, behavior, organ composition and ecology are candidate mechanisms that require separate tests.


#### Mechanism-to-evidence test

A reported change in **metabolic scaling and size constraints** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 05 — estimate, interpret, challenge

**Problem:** Compare two hypothetical animals with body masses in a ratio of 2:1. If total resting metabolic rate scales with mass to the power 0.75 under matched conditions, what is the predicted total-rate ratio?

**Method:** `(mass ratio)^0.75`. Substituting the given teaching values yields **1.6818 fold**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** The smaller animal has a higher rate per unit mass under this assumed exponent even though its total rate is lower. **Limits:** The assumed exponent is illustrative, not a fixed law across species or environmental conditions. These are synthetic numbers, not measured organism values.


## Integrative investigation — An estuarine fish meets a sudden salinity change

**Setting.** An estuary can change its salinity after heavy rain, tides or changes in river inflow. Imagine following a euryhaline fish through a gradual, controlled salinity transition. The animal's gill epithelia, drinking behavior, kidney output and stress signaling need not adapt simultaneously. The central problem is not simply whether fish survive; it is the schedule by which solute fluxes return toward balance while avoiding large cell-volume disturbances.

**Design.** Compare a slowly adjusted tank with an appropriately acclimated control under approved husbandry conditions. Record water conductivity, oxygen, temperature and food intake, and favor noninvasive measures. From an educational perspective, estimate net ion balance using intake and excretion routes before interpreting any molecular markers. Treat abrupt transfers and severe salinity challenges as excluded, because they are unnecessary for answering the learning question.

**Evidence and alternatives.** A laboratory could measure gill transporter transcripts, but increased transcription is not equal to increased net flux. Protein localization, epithelial surface area and transporter turnover may change independently. An isolated gill preparation can test flux direction, but losing circulating signals and intact ventilation may produce different results from measurements in the whole animal.

**Interpretation and transfer.** Construct a four-time-point table that separates external salinity, body-fluid osmolarity, water intake and urinary output. For each interval determine whether a deviation arises from external delivery, epithelial permeability or active transport. Propose an observation that would distinguish a slow hormonal response from an immediate physical osmotic effect. The learning outcome is a causal balance argument: environmental disturbance → tissue flux → compartment storage → behavioral and endocrine compensation. A matched final osmolarity does not prove every intermediate tissue experienced a harmless transition.

**Reproducibility checklist.** Declare the independent biological replicate and the direct measurement. Preselect a primary outcome, control environmental changes, and calibrate instruments. Preserve original data and computation steps rather than reporting rounded results alone. Compare the specific competing predictions before interpreting statistical significance. Respect animal welfare by using approved, appropriately noninvasive or existing datasets for educational comparisons.


## Retrieval practice — explain rather than memorize

1. For **Controlled variables and negative feedback**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

2. For **Diffusion, gradients and transport resistance**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

3. For **Cell membranes and osmotic water movement**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

4. For **Epithelia and compartment balances**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

5. For **Metabolic scaling and size constraints**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

**Self-check:** A defensible answer distinguishes direct observation from inference, names a unit or timescale, and explains at least one way its proposed explanation could be wrong. Recalculate all five worked cases without reading the answers.

## Working glossary and distinctions

The entries below state operational differences that matter when planning an experiment. Learn each term through a concrete measurement rather than memorizing a label in isolation.


**Homeostasis.** Maintenance of regulated internal conditions by coordinated processes; it permits fluctuations and shifts in target ranges rather than enforcing exact constancy.


**Controlled variable.** A physiological quantity monitored and influenced by a regulatory network, such as osmolarity; a convenient proxy may not equal the variable itself.


**Set point.** An operating target used in a control model; real biological targets can vary with developmental stage, circadian phase and behavioral state.


**Negative feedback.** A loop in which the response reduces the original disturbance or error, though excessive time delay can make the response oscillatory.


**Feedforward control.** Anticipatory action triggered by a predictive signal before the regulated variable itself has deviated markedly.


**Flux.** Quantity passing through a boundary per unit area per unit time when expressed as flux density, or total quantity per time when integrated over area.


**Fick diffusion relation.** An approximate relationship connecting transport rate to diffusion coefficient, area, concentration difference and barrier thickness under specified assumptions.


**Tonicity.** The tendency of a solution to change cell volume through effectively impermeant solutes; not synonymous with total measured osmolarity.


**Aquaporin.** A membrane protein that can provide a route for water movement in a variety of cells and epithelia.


**Polarized epithelium.** A tissue with distinct apical and basolateral transport machinery, allowing net directed transfer across a barrier.


**Mass balance.** A conservation statement that storage changes equal all inflows minus all outflows over a defined interval.


**Allometry.** A quantitative description of how one trait changes with body size, often fitted to a power law with taxon-dependent uncertainty.


**Clearance versus flux.** Clearance is an equivalent volume of fluid processed per time, whereas flux describes material transfer and needs concentration to relate them.


**Steady state.** A condition in which a measured amount or concentration changes negligibly over the interval of interest, even if nonzero transport is ongoing.


**Perturbation experiment.** A planned change in an input used to reveal regulation; interpretation requires matched controls and measurements of recovery over time.


## Unit 1 synthesis

Return to the five worked numerical cases and ask what controls each result, which changes are compensatory rather than primary, and how the model would fail when another organ system changes. Connect regulated variable versus measured proxy with feedback versus feedforward action and state a falsifiable prediction across the two levels of organization.
