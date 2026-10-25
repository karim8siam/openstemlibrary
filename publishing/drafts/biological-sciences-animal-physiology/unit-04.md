# Unit 04 — Circulation, breathing and gas exchange

> **Animal Physiology — OpenSTEM Book 11.** Circulation moves materials through vascular resistance, while respiratory surfaces exchange gases across physical gradients. All numerical case values in this book are **synthetic teaching data**, not measurements, clinical advice or husbandry recommendations. This editorial draft has not received independent peer review.

## What the unit asks you to explain

Physiology is a quantitative study of how living structures accomplish work and keep conditions within tolerable ranges. This unit examines circulation, breathing and gas exchange while connecting molecular mechanisms to whole-organism outcomes. The goal is not only to identify a named structure or pathway, but to predict the direction of change, the time needed for a response, and the observation that would distinguish a proposed mechanism from an alternative. Learners should keep conservation of matter or energy in view whenever they write an equation.

By the end of this unit, you should be able to (i) explain its five linked topics in physical and biological terms; (ii) calculate and interpret five dimensioned toy examples; (iii) decide which measurements distinguish input, state and output; (iv) identify failure modes of the models; and (v) design an ethical comparison while naming confounding factors. Prerequisites are first-year biology, elementary chemistry, algebra, and an ability to read plots. Differential equations are discussed conceptually where useful but are not assumed.


## Working distinctions

convective versus diffusive transport; ventilation versus perfusion; content versus partial pressure; closed and open circulations; flow distribution and reserve. A useful unit-wide habit is to separate direct measurements from inferred flows, clearly stating physical units and time windows.


## Integrated systems lens — Cardiorespiratory transport is a chain, not a single organ

Respiratory and circulatory performance is best described by a series of connected driving forces and resistances. Fresh respiratory medium must reach an exchange surface; gases cross the tissue barrier; circulatory fluid transports bound and dissolved oxygen; capillary delivery distributes that oxygen; and cells must consume it. A change at one step can alter gradients elsewhere, so the same arterial oxygen concentration may accompany very different organ oxygen supply. Independent measures of flow and oxygen content are essential.

The identity cardiac output = heart rate × stroke volume is exact by definition for matching averaged intervals, but it provides no causal law by itself. When heart rate rises, diastolic filling may shorten; contractility and venous return can adjust; and the output response can differ across conditions. Similarly flow = pressure difference / resistance is a useful circuit approximation, but resistance is influenced by vessel radius, tissue compression and autoregulatory tone. These derived identities should be paired with experiments that test their components.

Gas partial pressure and oxygen content are different kinds of measurement. A low partial pressure reduces diffusive driving force, whereas oxygen content includes the large contribution of respiratory pigment. Two blood samples at the same saturation may carry different amounts of oxygen if pigment concentration differs. Moreover tissue extraction depends on blood transit time, diffusion geometry and local metabolic demand. This is why a simple oxygen saturation reading cannot replace a full oxygen-delivery analysis.

Countercurrent exchange is a strategy for sustaining a gradient along a surface; it is not a mysterious mechanism that creates oxygen. Water leaving a fish gill has a lower dissolved oxygen content when gas has crossed into the blood. The driving gradient can remain favorable along a countercurrent arrangement because the fluids travel in opposite directions. In co-current geometry, the two streams tend to approach a common state along the exchanger. Real performance also depends on rates and membrane properties, so directional flow does not determine efficiency alone.

Ventilation–perfusion heterogeneity means different regions may exchange different amounts of gas even while the total ventilation and perfusion appear acceptable. A region with ventilation but very little perfusion contributes less useful oxygen transfer, and an inadequately ventilated perfused region can lower outflow oxygen content. Mixing blood from these regions gives a nonlinear whole-organ outcome because saturation is nonlinear with partial pressure.

Comparative respiratory work should not rank taxa by imagined technological progress. Mammalian tidal lungs, avian flow-through systems, fish gills and insect tracheal systems fit different constraints and phylogenetic histories. Some deliver oxygen directly to tissues, while others rely on circulation for most bulk transport. Appropriate comparison reports ambient medium, body size, mass-specific demand and ecological performance before drawing a mechanistic conclusion.

## Five linked physiological topics

### 4.1 — Heart chambers, stroke volume and cardiac output

#### Biological mechanism and scope

In closed vertebrate circulations, repeated contraction creates a pressure gradient that drives blood flow. Cardiac output equals the volume ejected per beat multiplied by beats per unit time. Filling, contractility, afterload and autonomic input modify stroke volume and rate; the same output may therefore be achieved with different combinations of rate and volume.

#### Comparisons, exceptions and organism-level interpretation

Single and double circulations differ in whether blood passes through one or two principal pump circuits before returning to the body. Fish gills favor one architecture, while birds and mammals support high systemic pressure with separate pulmonary flow. Across animals, one should compare pressures and vascular resistance in ecological context rather than rank hearts as simply advanced or primitive.

#### Observation, experiment and causal alternatives

Use echocardiographic estimates of end-diastolic and end-systolic volumes and separately measured heart rate in an educational dataset. Examine how uncertainty in volume measurement propagates to output. A fast heart does not guarantee high output when shortened filling time reduces stroke volume.

#### Appropriate limits of the model

An output estimate is a mean over a defined interval; pulsatile instantaneous flow and organ-specific perfusion need additional measurements.


#### Mechanism-to-evidence test

A reported change in **heart chambers, stroke volume and cardiac output** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 16 — estimate, interpret, challenge

**Problem:** A model heart ejects 65 mL per beat at 72 beats/min. Calculate cardiac output in liters per minute.

**Method:** `stroke volume × beats per minute / 1000`. Substituting the given teaching values yields **4.68 L/min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Stroke volume and heart rate can compensate for one another within physical and physiological limits. **Limits:** This is a fictional vertebrate teaching case, not a species-specific normal range. These are synthetic numbers, not measured organism values.


### 4.2 — Pressure gradients and vascular resistance

#### Biological mechanism and scope

Flow through a vessel reflects the pressure difference divided by hydraulic resistance under a lumped steady-state representation. Resistance rises strongly as radius narrows for ideal laminar flow in a rigid circular tube, but real vessels are distensible, branching and subject to blood viscosity changes. Arterioles are major adjustable resistance elements in many vertebrate tissues.

#### Comparisons, exceptions and organism-level interpretation

A large pressure drop across an organ may coexist with a low or high flow depending on its vascular state. Parallel organ beds redistribute cardiac output, while series segments add resistance. Regulation of vascular tone interacts with local metabolic signals, nerves and hormones; pressure alone cannot reveal a tissue's oxygen supply.

#### Observation, experiment and causal alternatives

Compare a model arteriole's predicted flow after a measured radius change while holding gradient and viscosity fixed. Then relax one assumption at a time. Do not apply the fourth-power law to an entire living microvascular network without validation; non-Newtonian blood properties and branching alter the relation.

#### Appropriate limits of the model

Blood pressure is a force-per-area quantity and differs from flow, which is volume-per-time. Keeping those units distinct prevents a common physiological misconception.


#### Mechanism-to-evidence test

A reported change in **pressure gradients and vascular resistance** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 17 — estimate, interpret, challenge

**Problem:** A rigid ideal cylindrical vessel reduces radius from r to 0.5r while pressure gradient, length and viscosity remain fixed. Find the new flow fraction under Poiseuille's relation.

**Method:** `(new radius / old radius)^4`. Substituting the given teaching values yields **0.0625 fraction**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A twofold radius reduction produces a sixteenfold ideal resistance increase. **Limits:** Real vessels and branching networks depart from rigid-tube laminar-flow assumptions. These are synthetic numbers, not measured organism values.


### 4.3 — Ventilation, airway mechanics and respiratory work

#### Biological mechanism and scope

Air enters lungs when the pressure at the respiratory surface falls below atmospheric pressure, generated by respiratory muscle action and elastic recoil. Minute ventilation is tidal volume multiplied by breathing frequency, but alveolar ventilation subtracts dead-space volume from each breath. Rapid shallow breathing can have high total minute ventilation while accomplishing little fresh gas delivery to exchanging regions.

#### Comparisons, exceptions and organism-level interpretation

Compliance describes volume change per pressure change. Resistance depends on airway geometry and flow regime. Obstructed airways, stiff lungs and fatigued respiratory muscles create different mechanical problems even if measured ventilation falls in all three. Aquatic animals pumping dense water over gills face a different transport cost and ventilation geometry.

#### Observation, experiment and causal alternatives

Simulate changing tidal volume and breathing rate, reporting alveolar ventilation with an explicit dead-space assumption. In a real experiment calibrate volume sensors and identify whether dead space is anatomical or apparatus related. Avoid predicting oxygenation from ventilation alone without considering blood perfusion and gas partial pressures.

#### Appropriate limits of the model

A ventilation equation is a bookkeeping relation and does not specify how evenly air distributes among exchanging units.


#### Mechanism-to-evidence test

A reported change in **ventilation, airway mechanics and respiratory work** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 18 — estimate, interpret, challenge

**Problem:** Tidal volume is 0.50 L, anatomical dead space 0.15 L, and breathing frequency 12/min. Estimate alveolar ventilation.

**Method:** `(tidal volume − dead space) × frequency`. Substituting the given teaching values yields **4.2 L/min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Increasing frequency without adequate tidal volume may raise total minute ventilation more than alveolar ventilation. **Limits:** Dead space is a simplification and does not establish gas-exchange efficiency by itself. These are synthetic numbers, not measured organism values.


### 4.4 — Oxygen transport, hemoglobin and tissue extraction

#### Biological mechanism and scope

Oxygen moves down partial-pressure gradients from exchange surface to blood and tissues. Much vertebrate blood oxygen content is carried bound to respiratory pigments; oxygen partial pressure and oxygen content are not identical. Hemoglobin binding is cooperative over much of its range, creating a sigmoidal relation that facilitates loading and unloading in different conditions.

#### Comparisons, exceptions and organism-level interpretation

Temperature, pH and carbon dioxide can shift affinity, changing how readily oxygen is unloaded at tissues. Species and developmental stages differ in pigment properties. A measured arterial saturation alone does not establish that delivery is sufficient: cardiac output, hemoglobin concentration and capillary distribution determine how much oxygen reaches an active organ.

#### Observation, experiment and causal alternatives

Calculate a simplified oxygen delivery estimate from blood flow and concentration difference in an explicitly fictional mammal example. If extraction rises while delivery falls, identify whether the tissue may be compensating for restricted flow. An affinity-shift demonstration does not diagnose a disorder and should never be used as an individual clinical calculator.

#### Appropriate limits of the model

The oxygen dissociation curve is a property of binding under defined conditions, not a universal one-parameter curve shared by all animals.


#### Mechanism-to-evidence test

A reported change in **oxygen transport, hemoglobin and tissue extraction** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 19 — estimate, interpret, challenge

**Problem:** A simplified animal has systemic blood flow 5 L/min, arterial oxygen content 200 mL O₂/L and mixed venous content 150 mL O₂/L. Estimate systemic oxygen consumption by the Fick principle.

**Method:** `blood flow × (arterial − venous O₂ content)`. Substituting the given teaching values yields **250 mL O₂/min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A reduction in either delivery or extraction can alter realized oxygen consumption. **Limits:** The measurements must refer to consistent physiological states and true content, not partial pressure. These are synthetic numbers, not measured organism values.


### 4.5 — Gills, countercurrent exchange and ventilation–perfusion matching

#### Biological mechanism and scope

Many fish gills arrange blood flow opposite to water flow, maintaining oxygen partial-pressure differences along much of an exchange lamella. Countercurrent architecture can outperform a co-current exchanger under similar ideal conditions. In lungs, ventilation–perfusion matching affects arterial gas levels because air delivery without blood flow and blood flow without adequate ventilation are both inefficient.

#### Comparisons, exceptions and organism-level interpretation

Countercurrent efficiency depends on flow rates, membrane conductance, oxygen solubility and transit time. Hypoxic water, temperature change and high swimming demand can alter gill performance. Air-breathing birds use flow-through lung architecture with crosscurrent exchange features rather than a mammalian tidal-alveolar pattern.

#### Observation, experiment and causal alternatives

Build a two-stream temperature or dissolved-gas analogue and compare exchange under reversed versus parallel flow while controlling inlet concentrations. A temperature demonstration captures transport geometry but does not fully reproduce oxygen binding in blood. For lung scenarios calculate ventilation–perfusion ratio only after defining each region's ventilation and perfusion.

#### Appropriate limits of the model

Architecture sets useful possibilities, but effective gas transport is a coupled outcome of ventilation, exchange conductance and circulation.


#### Mechanism-to-evidence test

A reported change in **gills, countercurrent exchange and ventilation–perfusion matching** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 20 — estimate, interpret, challenge

**Problem:** A modeled lung region receives 4 L/min of fresh air and 5 L/min of pulmonary blood flow. Compute the ventilation-to-perfusion ratio.

**Method:** `alveolar ventilation / perfusion`. Substituting the given teaching values yields **0.8 dimensionless**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Both numerator and denominator are flow rates, making their ratio dimensionless. **Limits:** Equal ratios in different regions do not imply equal absolute oxygen transport. These are synthetic numbers, not measured organism values.


## Integrative investigation — A hypoxic exercise test in two respiratory designs

**Setting.** A bird and a mammal respond to increased locomotor demand at lower inspired oxygen partial pressure. A comparative thought experiment can reveal why ventilation, diffusion architecture, blood flow and hemoglobin affinity must be analyzed jointly rather than separately.

**Design.** Define species, body mass, exercise intensity and environmental pressure precisely before collecting variables. Measure oxygen consumption, breathing pattern and blood oxygen content when possible with validated minimally intrusive protocols. An increase in ventilation is an active response and cannot be taken as proof of equivalent gas exchange effectiveness.

**Evidence and alternatives.** A hypothetical animal might retain high arterial saturation while reducing total oxygen delivery due to low cardiac output. Conversely a modest saturation may still coexist with adequate delivery if blood flow and hemoglobin content are high. Such possibilities explain why content, partial pressure and transport rate occupy different columns in the same analysis.

**Interpretation and transfer.** Construct a two-by-two table contrasting high and low ventilation with high and low perfusion. Determine which cases are limited by fresh gas delivery versus blood delivery under stated toy assumptions. Compare a countercurrent gill model with the pulmonary case to identify which transport geometry, rather than which evolutionary ranking, is being tested. The causal lesson is a chain of resistances: environment to exchange surface, across the surface, to blood and to working mitochondria. Improving one step may not raise system output when another step is limiting.

**Reproducibility checklist.** Declare the independent biological replicate and the direct measurement. Preselect a primary outcome, control environmental changes, and calibrate instruments. Preserve original data and computation steps rather than reporting rounded results alone. Compare the specific competing predictions before interpreting statistical significance. Respect animal welfare by using approved, appropriately noninvasive or existing datasets for educational comparisons.


## Retrieval practice — explain rather than memorize

1. For **Heart chambers, stroke volume and cardiac output**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

2. For **Pressure gradients and vascular resistance**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

3. For **Ventilation, airway mechanics and respiratory work**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

4. For **Oxygen transport, hemoglobin and tissue extraction**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

5. For **Gills, countercurrent exchange and ventilation–perfusion matching**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

**Self-check:** A defensible answer distinguishes direct observation from inference, names a unit or timescale, and explains at least one way its proposed explanation could be wrong. Recalculate all five worked cases without reading the answers.

## Working glossary and distinctions

The entries below state operational differences that matter when planning an experiment. Learn each term through a concrete measurement rather than memorizing a label in isolation.


**Cardiac output.** Volume of blood pumped per time, calculated as stroke volume multiplied by heart rate under defined beat averaging.


**Stroke volume.** Blood volume ejected by a heart chamber per contraction, affected by filling, contractility and opposing pressure.


**Afterload.** The mechanical load opposing ejection from a pumping chamber, which is not fully summarized by a single pressure reading.


**Perfusion.** Delivery of fluid through a tissue's vascular network, distinct from the diffusion of substances across vessel walls.


**Vascular resistance.** Pressure difference divided by volume flow under a specified steady-flow approximation.


**Poiseuille relation.** A laminar-flow equation for a rigid round tube that predicts very strong radius sensitivity under highly idealized conditions.


**Compliance.** Change in volume for a change in pressure, describing elastic behavior in vessels, lungs or other compartments.


**Dead space.** The fraction of ventilation that does not directly exchange respiratory gases with perfused exchange surfaces under the chosen definition.


**Alveolar ventilation.** Fresh-air flow reaching respiratory exchanging regions, estimated using tidal volume minus dead space in a simple model.


**Ventilation–perfusion ratio.** The local rate of fresh gas supply relative to blood flow, useful for diagnosing mechanistic mismatch in simplified respiratory models.


**Partial pressure.** A gas's contribution to total pressure, influencing exchange driving forces but not identical to total gas content in blood.


**Hemoglobin saturation.** Fraction of pigment oxygen-binding capacity occupied; depends on ligand pressure and the biochemical binding environment.


**Oxygen content.** Total amount of oxygen in a volume of blood, including bound and dissolved oxygen, not equal to partial pressure alone.


**Countercurrent exchange.** Oppositely directed flow that can maintain favorable gradients along an exchange surface under suitable conditions.


**Fick principle.** A conservation relation estimating substance uptake from flow rate times inflow–outflow content difference.


## Unit 4 synthesis

Return to the five worked numerical cases and ask what controls each result, which changes are compensatory rather than primary, and how the model would fail when another organ system changes. Connect convective versus diffusive transport with closed and open circulations and state a falsifiable prediction across the two levels of organization.
