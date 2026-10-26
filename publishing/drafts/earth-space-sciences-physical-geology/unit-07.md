# Unit 7: Weathering and Surface Processes

## Orientation: a geologist's problem

How does the surface translate gravity, climate, and water into landforms? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A catchment has steep headwaters, a meandering downstream reach, a variable rainfall record, and disturbed slopes. Evaluate sediment movement without assuming a single flood predicts all future events. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 31: Physical and chemical weathering

### Geological concept

Water, temperature changes, biological agents, and chemical reactions disintegrate or alter rock exposed near the surface. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Fracturing increases reactive surface area; oxidation, hydrolysis, dissolution, and carbonation can change mineral and solute budgets. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Saprolite, mineral alteration profiles, dissolved loads, fractures, and regolith thickness constrain weathering pathways. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A granite boulder breaks into angular fragments while feldspar grains become cloudy.

**Competing explanations:** Mechanical fracture increases exposed surface while hydrolysis can produce secondary clays, allowing coupled physical and chemical changes.

**Discriminating investigation:** Measure mineral changes, solution chemistry and rind development at multiple sites; climate, residence time and transport may confound any weathering-rate inference.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A thick soil profile does not necessarily imply faster current weathering; landform stability and erosion also control thickness. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Use a simple mass-balance model to separate chemical loss, particulate export, and deposition. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 31

**Fictional input data:** A soil-weathering column initially contains 950 kg of rock minerals and now 770 kg. Compute fractional mineral loss.

**Given:** m0=950, m1=770. Use consistent units and define relevant geometry.

**Steps:** Evaluate `(m0-m1)/m0*100` with the values above; the result is **18.94737 %**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Loss excludes new additions and material export errors. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How could identical bedrock develop contrasting soils under different climate and drainage conditions? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 32: Slope stability and mass movement

### Geological concept

Gravity drives downslope movement when forces resisting shear become insufficient for a particular failure geometry. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Slope angle, material strength, pore pressure, discontinuities, vegetation, and loading influence susceptibility and triggering. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Scarps, tension cracks, displaced blocks, colluvium, pore-pressure logs, and rainfall history document different stages of movement. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A hillside has fresh tension cracks after weeks of rain and an older debris apron below.

**Competing explanations:** Pore-pressure changes may help explain decreased shear resistance, yet old scarps do not prove imminent failure or a particular triggering threshold.

**Discriminating investigation:** Obtain professional assessment with groundwater and geometry data; a single educational stability formula must not determine evacuation or construction safety.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A high susceptibility map is not a deterministic short-term forecast; many slopes with similar characteristics have different histories. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Treat numerical stability estimates as screening tools, not engineering designs or individual property safety certifications. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 32

**Fictional input data:** A 500-kg block lies on a 22° ideal plane. Find downslope gravitational force component.

**Given:** m=500, g=9.81, a=22. Use consistent units and define relevant geometry.

**Steps:** Evaluate `m*g*math.sin(math.radians(a))` with the values above; the result is **1837.44534 N**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Friction, cohesion, pore pressure, and dynamics omitted. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How could prolonged rainfall reduce stability without visibly increasing the slope angle? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 33: Rivers and sediment budgets

### Geological concept

A river network transports water, solutes, and sediment from uplands toward depositional sinks and responds to changing discharge and base level. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Channel form emerges from interactions among slope, sediment caliber, vegetation, flow regime, and bed resistance. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Channel cross sections, rating curves, suspended-load samples, terraces, and floodplain deposits reveal different process timescales. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Suspended sediment concentration peaks before the largest stream discharge during a storm.

**Competing explanations:** A hysteresis loop could reflect available sediment near the channel, shifting source areas or delayed transport from hillslopes.

**Discriminating investigation:** Sample several storm stages, report measurement uncertainty and grain size, and avoid extrapolating one event to annual sediment yield.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

One flow observation cannot define a reliable long-term sediment budget, and discharge alone does not predict transport for all grain sizes. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Estimate a hypothetical stream discharge and identify where channel geometry or velocity uncertainty matters most. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 33

**Fictional input data:** A rectangular stream is 6 m wide and 1.5 m deep with mean velocity 0.8 m/s. Estimate water discharge.

**Given:** w=6, d=1.5, v=0.8. Use consistent units and define relevant geometry.

**Steps:** Evaluate `w*d*v` with the values above; the result is **7.2 m³/s**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Rectangular cross section and uniform mean velocity. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why might a river carry more sediment during the rising limb than the falling limb of the same flood? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 34: Glaciers and cold-region landscapes

### Geological concept

Glacial ice deforms and slides under stress while accumulating snow in some zones and losing mass in others. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Ice movement can erode bedrock, entrain sediment, and build moraines; meltwater redistributes sediment and alters depositional patterns. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Striations, till fabrics, erratic boulders, valley profiles, and dated moraines constrain former glaciation. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Ridges of unsorted sediment form arcs downvalley from a mountain basin.

**Competing explanations:** Terminal moraines are plausible, but debris-flow lobes and inherited landforms can create similar shapes.

**Discriminating investigation:** Look for till characteristics, erratic provenance, striated bedrock and independent chronology to establish that ice deposited the ridges.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A U-shaped valley alone is insufficient to date an ice advance or determine climatic cause. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Combine landforms, chronology, and climate proxies before reconstructing a glacial sequence. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 34

**Fictional input data:** A glacier receives 1.6 m water equivalent accumulation and loses 1.9 m in ablation during a year. Find surface mass balance.

**Given:** A=1.6, B=1.9. Use consistent units and define relevant geometry.

**Steps:** Evaluate `A-B` with the values above; the result is **-0.3 m water eq/yr**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** No lateral mass redistribution included. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can a moraine remain preserved long after the glacier that deposited it disappears? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 35: Coasts, beaches, and sea-level change

### Geological concept

Waves, tides, storms, sediment supply, and relative sea level shape shorelines and redistribute material along and across the coast. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Wave refraction and longshore transport shift sediment; changes in land elevation alter relative sea level independently of global ocean change. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Beach profiles, barrier stratigraphy, tide gauges, terraces, and sediment tracers reveal trends on different timescales. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A sandy beach narrows after several storms but partly recovers in calmer months.

**Competing explanations:** Seasonal cross-shore exchange can explain change without requiring a sustained negative sediment budget.

**Discriminating investigation:** Compare matched beach profiles over years, measure alongshore inputs and outputs, and separate relative sea-level change from seasonal wave forcing.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Short-term beach erosion does not by itself establish long-term shoreline retreat; seasonal variability can be substantial. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Develop a sediment-budget table before recommending interventions that may starve adjacent coasts. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 35

**Fictional input data:** A coast receives 18,000 m³/yr of littoral sediment and exports 25,000 m³/yr. Calculate net annual storage change.

**Given:** In=18,000, Out=25,000. Use consistent units and define relevant geometry.

**Steps:** Evaluate `In-Out` with the values above; the result is **-7000 m³/yr**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** No additional cross-shore fluxes. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why can a seawall reduce erosion at one location yet increase beach loss nearby? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 7: Weathering and Surface Processes — constructing and testing an explanation

**Scenario and provenance.** A catchment has steep headwaters, a meandering downstream reach, a variable rainfall record, and disturbed slopes. Evaluate sediment movement without assuming a single flood predicts all future events. Every numerical value in the accompanying `datasets/unit-07.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: Physical and chemical weathering; Slope stability and mass movement; Rivers and sediment budgets; Glaciers and cold-region landscapes; Coasts, beaches, and sea-level change. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

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

## Unit 7 synthesis, transfer, and examination workshop

The five lessons in this unit—Physical and chemical weathering, Slope stability and mass movement, Rivers and sediment budgets, Glaciers and cold-region landscapes, Coasts, beaches, and sea-level change—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
