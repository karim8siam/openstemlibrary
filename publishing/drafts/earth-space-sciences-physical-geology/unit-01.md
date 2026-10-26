# Unit 1: Earth as an Investigated System

## Orientation: a geologist's problem

How can indirect measurements constrain a planet that cannot be sampled at most depths? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A research team interprets three hypothetical crustal columns from density, seismic speed, and heat-flow observations. The task is to avoid overfitting: several internal structures can produce similar surface signals. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 1: What geology can and cannot infer

### Geological concept

Geology reconstructs events from rocks, landforms, structures, and measurements; interpretations depend on the quality and spatial scale of surviving evidence. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Observations become geological explanations by linking process, predicted traces, and alternative histories; a narrative that fits one outcrop may fail when tested across a region. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

An outcrop notebook, mapped contact, rock texture, and mineral assemblage are different kinds of evidence; each can constrain some hypotheses while leaving others open. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A roadcut reveals two contacts and three lithologies across fifty meters.

**Competing explanations:** A darker zone might represent an intrusive margin, an altered fault gouge, or younger sediment filling a channel; merely describing color cannot decide among them.

**Discriminating investigation:** Trace the geometry beyond the face, examine clasts and fabrics under magnification, and look for baked host material or displaced markers before naming the contact.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Unexposed contacts, erosion, alteration, human disturbance, and sampling bias make apparently straightforward stories underdetermined. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Choose a research question with predictions that field descriptions or laboratory analysis could falsify; record uncertainty separately from observation. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 1

**Fictional input data:** A field traverse measures 12 cm on a 1:25,000 map. Convert map length to ground distance in kilometers.

**Given:** L=12, S=25,000. Use consistent units and define relevant geometry.

**Steps:** Evaluate `L*S/100000` with the values above; the result is **3 km**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Straight horizontal map distance, no terrain correction. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How would two observers distinguish a measured bedding attitude from an inference about the regional tectonic history? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 2: Earth's layers and physical properties

### Geological concept

The crust, mantle, outer core, and inner core are distinguished through material behavior and seismic observations, not simply by depth labels. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Elastic wave speed changes with density, rigidity, temperature, composition, and phase; liquid outer-core behavior explains the absence of transmitted direct shear waves. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Travel-time curves, normal modes, gravity, moment of inertia, and laboratory mineral physics are jointly informative about deep Earth. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Seismic travel times show arrivals delayed along one station profile.

**Competing explanations:** A hot lower crust, compositional differences, or a thick sedimentary basin can all lower apparent wave speed; timing alone is not a direct temperature map.

**Discriminating investigation:** Compare ray coverage, converted phases, gravity data, and nearby known structures; assess whether velocity variations remain after correcting station elevation and near-surface layers.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A change in wave speed is not a direct photograph of a rock type; several combinations of composition and temperature may reproduce it. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Compare independent measurements before asserting an interior property, and separate seismic boundaries from chemical classifications. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 2

**Fictional input data:** A P wave crosses 720 km of uniform material at 6 km/s. Estimate direct-path travel time.

**Given:** d=720, v=6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `d/v` with the values above; the result is **120 s**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Uniform speed and straight path are simplified. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why is a mantle mineral identification less secure when based only on a single seismic velocity anomaly? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 3: Earth's heat and energy budget

### Geological concept

Solar radiation drives most surface weather and climate processes while radiogenic heat and residual planetary heat contribute to the internal geothermal budget. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Thermal gradients vary with conductivity, heat production, groundwater flow, and tectonic regime; heat flux is related to the gradient through Fourier's law. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Borehole temperatures, heat-flow measurements, bathymetric age patterns, and volcanic belts constrain energy transport. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Two temperature logs taken one month apart differ near the water table.

**Competing explanations:** Conduction, groundwater advection, drilling disturbance, and seasonal temperature propagation have different spatial and temporal signatures.

**Discriminating investigation:** Repeat the profile after equilibration; pair temperature with conductivity and piezometric observations before deriving a crustal heat-flow estimate.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A steep temperature gradient need not indicate an approaching magma chamber; shallow groundwater and conductivity contrasts can modify readings. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Estimate an order-of-magnitude conductive flux with reported assumptions, then assess which measurement would dominate uncertainty. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 3

**Fictional input data:** A conductive geothermal gradient is 28 K/km and thermal conductivity is 2.7 W/(m K). Estimate heat-flux magnitude.

**Given:** k=2.7, G=28. Use consistent units and define relevant geometry.

**Steps:** Evaluate `k*G/1000` with the values above; the result is **0.0756 W/m²**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** One-dimensional steady heat conduction. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How could two wells with identical heat flux yield different measured temperature gradients? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 4: The rock cycle as process network

### Geological concept

Rocks are temporarily stabilized records that can be melted, crystallized, eroded, deposited, buried, metamorphosed, uplifted, and recycled. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

The pathways are branching rather than a single obligatory circle: any given rock may undergo repeated alteration or deformation without passing every named stage. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Cross-cutting veins, rounded clasts, mineral reaction rims, unconformities, and xenoliths document different transitions between rock states. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A sandstone contains quartz clasts, chlorite-rich fragments, and rounded pebbles.

**Competing explanations:** Its constituents could derive from multiple source terrains; a single apparent rock-cycle pathway is not adequate to explain the mixture.

**Discriminating investigation:** Count clast types in several beds, compare paleocurrent indicators, and test whether heavy minerals indicate a metamorphic source rather than only igneous bedrock.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A single thin section cannot usually determine the complete history of a rock; later overprinting may erase earlier features. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Interpret a rock history as an ordered set of testable events rather than a fixed diagram with a predetermined starting point. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 4

**Fictional input data:** An outcrop zone covers 1.5 km² and loses 2 cm of material. Estimate removed volume.

**Given:** A=1.5, d=2. Use consistent units and define relevant geometry.

**Steps:** Evaluate `A*1e6*d/100` with the values above; the result is **30,000 m³**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Uniform lowering is invented for teaching. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Which features would indicate that a sandstone formed from erosion of an older metamorphic rock? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 5: Observational methods and geologic scales

### Geological concept

Geologic problems range from atomic lattices and thin sections to satellite observations and hundred-million-year plate reconstructions. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Field mapping records location and geometry; microscopy reveals texture; geochronology constrains age; remote sensing samples broad patterns with limited penetration. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Repeated bearings, stratigraphic logs, thin sections, analytical blanks, and spatially referenced maps provide complementary constraints. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A satellite image shows a linear ridge that seems to connect two discontinuous outcrops.

**Competing explanations:** The ridge may mark a resistant bed, a fault zone, a volcanic dike, or a human-altered boundary; spatial alignment is not enough.

**Discriminating investigation:** Visit the gaps, log GPS uncertainty, compare topographic shadows and drainage deflections, and explicitly mark unverified stretches as inferred rather than observed contacts.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Instrument precision, map resolution, sampling extent, and representativeness are different qualities and should not be combined into one vague accuracy label. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Design a multi-scale observation plan in which each measurement answers a question that the other instruments cannot directly answer. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 5

**Fictional input data:** Thirty stations are collected across 15 km². Compute mapped station density.

**Given:** n=30, A=15. Use consistent units and define relevant geometry.

**Steps:** Evaluate `n/A` with the values above; the result is **2 stations/km²**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Station spatial clustering is ignored. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. What is lost when a one-meter fracture is averaged into a one-kilometer geologic map pixel? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 1: Earth as an Investigated System — constructing and testing an explanation

**Scenario and provenance.** A research team interprets three hypothetical crustal columns from density, seismic speed, and heat-flow observations. The task is to avoid overfitting: several internal structures can produce similar surface signals. Every numerical value in the accompanying `datasets/unit-01.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: What geology can and cannot infer; Earth's layers and physical properties; Earth's heat and energy budget; The rock cycle as process network; Observational methods and geologic scales. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

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

## Unit 1 synthesis, transfer, and examination workshop

The five lessons in this unit—What geology can and cannot infer, Earth's layers and physical properties, Earth's heat and energy budget, The rock cycle as process network, Observational methods and geologic scales—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
