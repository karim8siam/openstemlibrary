# Unit 3: Igneous Processes and Volcanic Landscapes

## Orientation: a geologist's problem

How do melt generation, cooling, and eruption produce recognizable rock records? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A volcanic province has compositionally contrasting lavas, an eroded pluton, and ash beds. Reconstruct the sequence while distinguishing eruption deposits from intrusive contacts. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 11: Sources and generation of magma

### Geological concept

Partial melting depends on temperature, pressure, volatile content, and source composition; mantle and crustal melts need not have the same origins. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Decompression, flux-assisted melting, and heat transfer can each move materials across a solidus without requiring a uniformly molten mantle. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Experimental phase relations, geochemical patterns, volcanic settings, and geophysical observations connect melt formation to tectonic environment. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A chain of basaltic cones lies behind an active-looking deformation zone.

**Competing explanations:** A convergent margin, a rift, and an intraplate hot region have different source and geochemical predictions although all can produce basalt.

**Discriminating investigation:** Compare fault geometry, regional earthquakes, trace-element ratios, and the spatial distribution of vents; do not equate basalt with a unique tectonic boundary.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A volcanic rock's composition reflects multiple processes; source composition cannot be solved uniquely from one oxide percentage. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Use competing petrogenetic models and state which isotope, trace-element, or textural measurement could distinguish them. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 11

**Fictional input data:** An illustrative solidus varies as T=1050+105P, with P in GPa. Estimate temperature at 2 GPa.

**Given:** T0=1050, a=105, P=2. Use consistent units and define relevant geometry.

**Steps:** Evaluate `T0+a*P` with the values above; the result is **1260 °C**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** This classroom line is not a mantle melting calibration. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why can adding water promote mantle melting while lowering pressure can trigger melting without adding heat? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 12: Crystal growth and igneous textures

### Geological concept

Grain size and texture reflect nucleation, growth, cooling history, and volatile evolution rather than a single cooling-rate dial. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Rapid quenching tends to suppress large crystal growth; slow cooling may permit coarser crystals; staged cooling can produce porphyritic texture. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Phenocrysts in fine groundmass, glass, vesicles, flow banding, and interlocking crystals provide process clues. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A volcanic rock contains large plagioclase crystals in a fine dark matrix.

**Competing explanations:** The texture suggests a two-stage crystallization history, but crystal accumulation or late mixing could modify the interpretation.

**Discriminating investigation:** Document zoning and resorption surfaces, compare phenocryst populations across flows, and assess whether the same growth history explains inclusions and host melt.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Crystal size also depends on melt chemistry, nucleation density, and deformation; a texture should not be turned into an exact clock without calibration. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Compare microscopic observations with field relations to distinguish intrusive versus extrusive origins and the possibility of multiple cooling episodes. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 12

**Fictional input data:** Under Newton cooling, a sample at 900°C is exposed to 20°C and k=0.02/min. Estimate temperature after 30 min.

**Given:** Ta=20, T0=900, k=0.02, t=30. Use consistent units and define relevant geometry.

**Steps:** Evaluate `Ta+(T0-Ta)*math.exp(-k*t)` with the values above; the result is **502.95424 °C**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Lumped uniform-temperature approximation. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. What sequence of events can produce large crystals suspended in a fine-grained volcanic groundmass? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 13: Igneous composition and differentiation

### Geological concept

Mafic, intermediate, and felsic categories organize compositional patterns but do not encode every melt source or alteration pathway. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Fractional crystallization changes residual liquid composition; assimilation and magma mixing can produce additional trends beyond simple crystallization. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Mineral proportions, whole-rock chemistry, zoning, enclaves, and isotope patterns help evaluate differentiation models. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Two lavas define a straight trend between different silica values on a composition plot.

**Competing explanations:** Simple mixing may explain the line, whereas a fractionation trend could mimic it over a limited range.

**Discriminating investigation:** Evaluate compatible and incompatible trace elements and mineral assemblages, and check whether a physically reasonable mixing mass balance is possible.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Simple linear mixing is not a universal replacement for thermodynamic crystallization models; concentrations may be altered after emplacement. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Check mass balance before accepting a story that invokes mixing, and consider whether the observed phases can crystallize at the proposed conditions. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 13

**Fictional input data:** A hypothetical basalt-and-rhyolite mixture contains 60% of 50 wt% SiO2 and 40% of 74 wt% SiO2. Find bulk silica percentage.

**Given:** f=0.6, A=50, B=74. Use consistent units and define relevant geometry.

**Steps:** Evaluate `f*A+(1-f)*B` with the values above; the result is **59.6 wt%**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Simple mass-weighted mixing only. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why might a compositional line on an oxide plot result from mixing rather than fractional crystallization? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 14: Intrusive bodies and contact relations

### Geological concept

Dikes, sills, plutons, stocks, and batholiths describe intrusive geometries at different scales or relations to country rock. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Magma entering fractures can cut across layering, whereas concordant sills follow layering; thermal contact effects depend on temperature and wall-rock properties. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Cross-cutting contacts, chilled margins, baked zones, xenoliths, and intrusive fabrics constrain emplacement order and mechanics. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A narrow dike cuts folded shale and is itself transected by a small fault.

**Competing explanations:** The intrusion is younger than the shale folding if the contact relations are correctly interpreted, and the fault is younger than the dike displacement marker.

**Discriminating investigation:** Inspect whether the fracture truly offsets the dike or merely intersects it, and look for chilled margins, xenoliths, and repeated fault-plane slip indicators.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Erosion may remove the original top of a body; a surface exposure rarely reveals the complete three-dimensional shape. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Construct a relative chronology from contact relationships before estimating emplacement depth or uplift magnitude. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 14

**Fictional input data:** A tabular dike is 18 m thick along a 600 m strike length and 300 m depth extent. Estimate geometric volume.

**Given:** t=18, L=600, H=300. Use consistent units and define relevant geometry.

**Steps:** Evaluate `t*L*H` with the values above; the result is **3,240,000 m³**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Rectangular extent is hypothetical. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can a chilled margin and an included host-rock fragment independently support the same intrusion order? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 15: Volcanic deposits and eruption style

### Geological concept

Eruptive behavior responds to melt viscosity, gas exsolution, ascent rate, and interaction with external water or ice. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Effusive lava may build flows and domes; explosive fragmentation produces tephra, surges, and pyroclastic density currents with different transport conditions. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Clast shape, bedding, welding, pumice, lava morphology, and stratigraphic contacts identify processes and depositional environments. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A pumice-rich deposit thins downslope but becomes locally thicker in a valley.

**Competing explanations:** Fallout, pyroclastic currents, and later sediment reworking can create superficially similar thickness trends.

**Discriminating investigation:** Describe grading, welding, erosive basal contacts, and lateral sorting; a hazardous-flow interpretation should not rest solely on the thickness map.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Deposit thickness alone cannot rank eruption danger; topography, recurrence, wind, and sediment remobilization matter. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Map plausible hazard pathways and avoid presenting toy models as real eruption forecasts. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 15

**Fictional input data:** A lava sheet covers 2.4 km² with average thickness 6 m. Estimate bulk lava volume.

**Given:** A=2.4, h=6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `A*1e6*h` with the values above; the result is **14,400,000 m³**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Uniform thickness, no vesicular correction. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why does the same volcano sometimes leave both coherent lava and highly fragmented deposits? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 3: Igneous Processes and Volcanic Landscapes — constructing and testing an explanation

**Scenario and provenance.** A volcanic province has compositionally contrasting lavas, an eroded pluton, and ash beds. Reconstruct the sequence while distinguishing eruption deposits from intrusive contacts. Every numerical value in the accompanying `datasets/unit-03.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: Sources and generation of magma; Crystal growth and igneous textures; Igneous composition and differentiation; Intrusive bodies and contact relations; Volcanic deposits and eruption style. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

### Sampling protocol and provenance

Imagine acquiring these data through a permitted classroom field investigation, laboratory session, or secondary dataset. Define a sampling frame with a spatial or stratigraphic coordinate, then identify how selection would occur. Would samples be clustered along accessible roads, selected at regular intervals, or chosen to represent the full range of rock types? Accessibility sampling may omit the very materials that would falsify a favored explanation. A reliable protocol would document instruments, calibrations, units, replicate measurements, missing values, detection limits, coordinate reference systems, and any preparation that changes the specimen. Here those details are intentionally not actual field records; the data are simulated and should be labeled at every export.

### Quantitative exploration

Read the CSV header and determine which variables can be compared dimensionally. Calculate a mean and a range for at least two numeric columns, and create a scatterplot that retains the original sample identifiers. Check whether the response changes monotonically; do not assume a straight line from a small table. Fit a simple slope only if the units and sample selection make it interpretable. For every fitted coefficient, explain what a one-unit input change would mean physically. Do not report a formal confidence interval unless the sampling assumptions and statistical method justify it. The exercise assesses the quality of inference, not the sophistication of a software package.

### Perturbations and missing evidence

Repeat the analysis after removing the single point with the largest response. Then repeat after treating that point as an authentic observation whose cause is not yet known. Compare how the story changes. Consider a hidden spatial gradient, instrument drift, and an unmeasured material property as alternative explanations for a pattern. If two samples appear contradictory, inspect the provenance first. A geological contradiction may be scientifically valuable: perhaps the rock units are not equivalent, the chronology differs, or a younger event overprinted only part of the area. Construct a follow-up plan that could discriminate these possibilities without inventing field facts.

### Communicating a bounded conclusion

Produce a one-page briefing with a short question, the exact assumptions, a plot, a table of key statistics, and an interpretation expressed at the scale of the data. Include three explicit limitations, such as synthetic provenance, missing spatial coverage, uncertain material properties, or simplified boundary conditions. Recommend exactly one high-value additional observation, and explain why it would be more discriminating than merely collecting many more similar samples. For a safety-related application, state that no design, permit, drilling, construction, or public risk communication should rely on a classroom simulation alone.

### Synthesis and oral defense

Defend your interpretation to a colleague who did not see the raw data. First, explain the mechanism without using the apparent correlation as its sole evidence. Second, show the figure and state what is measured and what is simulated. Third, present the strongest plausible alternative. Fourth, identify whether the proposed model would extrapolate beyond observed conditions, and say why that extrapolation might fail. Finally, explain what observation or model discrepancy would make you revise your conclusion. A complete scientific answer includes both a positive claim and its boundary of applicability.

### Suggested rubric

Allocate 20% to valid definitions and evidence provenance, 20% to dimensional and statistical checks, 20% to competing explanations, 20% to meaningful uncertainty and sensitivity analysis, and 20% to clarity of scientific communication. A high-scoring report need not select the most dramatic explanation. It must display the reasoning necessary for another investigator to reproduce the numerical steps and understand precisely why some questions remain unresolved. This rubric is a proposed instructional aid and can be adjusted for an institution's curriculum.

## Unit 3 synthesis, transfer, and examination workshop

The five lessons in this unit—Sources and generation of magma, Crystal growth and igneous textures, Igneous composition and differentiation, Intrusive bodies and contact relations, Volcanic deposits and eruption style—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
