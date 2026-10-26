# Unit 8: Geologic Mapping, Water, Hazards, and Resources

## Orientation: a geologist's problem

How do geologists combine maps, models, and uncertainty for practical decisions? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A fictional community needs a preliminary site appraisal for water supply and slope stability using sparse boreholes, a mapped fault, and variable aquifer properties. Distinguish screening from engineering certification. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 36: Reading geologic maps and cross sections

### Geological concept

A geologic map projects observed and interpreted rock units, contacts, faults, and structural measurements onto a topographic framework. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Strike and dip describe plane orientation; map traces depend on topography and geometry, so apparent outcrop widths differ from true stratigraphic thickness. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Field stations, contact traces, stereographic measurements, and drill logs constrain subsurface interpretations. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A limestone contact curves around a valley and its apparent width changes across slopes.

**Competing explanations:** A horizontal map trace may reflect topography and true bedding dip together, not a change in the bed's actual thickness.

**Discriminating investigation:** Measure strike and dip at multiple points and construct an alternative cross section to test whether a fault or fold is required.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Contacts between stations are interpolations; a precise line on a map should not imply unrealistically precise subsurface location. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Construct at least two cross sections consistent with available evidence and flag where interpretations diverge. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 36

**Fictional input data:** An exposed planar bed spans 15 m horizontally on level ground and dips 30°. Find its thickness if width is perpendicular to strike.

**Given:** w=15, a=30. Use consistent units and define relevant geometry.

**Steps:** Evaluate `w*math.sin(math.radians(a))` with the values above; the result is **7.5 m**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Planar bed, horizontal ground, width perpendicular to strike. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can two subsurface cross sections honor the same surface outcrops yet predict different borehole sequences? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 37: Groundwater flow and aquifers

### Geological concept

Water resides and moves through connected pores and fractures; hydraulic head integrates elevation and pressure contributions. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Darcy's law relates volumetric flow to hydraulic conductivity, hydraulic gradient, and cross-sectional area under its assumptions. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Water levels in monitoring wells, pumping tests, tracer tests, and geological logs constrain flow paths and heterogeneity. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Two wells at different elevations have identical depth-to-water measurements.

**Competing explanations:** Their actual hydraulic heads can differ because the datum and land-surface elevations differ; water depth below ground is not hydraulic head.

**Discriminating investigation:** Survey well reference elevations, measure levels synchronously, and test heterogeneity before interpreting flow direction from well depth alone.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

High porosity does not guarantee high permeability, and a single well test cannot characterize all scales or directional effects. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Calculate hypothetical flow from measured head differences, then assess consequences of uncertain conductivity. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 37

**Fictional input data:** Hydraulic conductivity is 2×10⁻⁴ m/s, head gradient 0.02 and area 18 m². Estimate Darcy discharge.

**Given:** K=2.000e-04, i=0.02, A=18. Use consistent units and define relevant geometry.

**Steps:** Evaluate `K*i*A` with the values above; the result is **7.200e-05 m³/s**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Saturated flow and homogeneous medium. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why could clay store much water yet transmit it far more slowly than coarse sand? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 38: Earth hazards and risk communication

### Geological concept

Hazard describes potentially damaging processes, exposure describes what lies in their path, and vulnerability affects consequences. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Earthquakes, volcanic eruptions, floods, landslides, and subsidence differ in triggers, frequencies, and predictability. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Scenario maps, historical catalogs, instrumentation, field evidence, and engineering assessments serve different levels of decision support. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A settlement sits near a mapped fault but the available data include no current building assessment.

**Competing explanations:** Fault proximity indicates possible exposure to a process, not the vulnerability of particular structures or the probability of damage at a specified time.

**Discriminating investigation:** Combine authoritative hazard maps with engineering investigations and transparent probability language; never imply the classroom map certifies property-level safety.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A regional hazard layer must not be represented as an individual-building safety clearance or a near-term event prediction. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Explain probabilities, mapping resolution, and uncertainty plainly when communicating a screening result to a non-specialist. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 38

**Fictional input data:** An annual hypothetical exceedance chance is 2%. Estimate probability of at least one exceedance in 20 independent years.

**Given:** p=0.02, n=20. Use consistent units and define relevant geometry.

**Steps:** Evaluate `100*(1-(1-p)**n)` with the values above; the result is **33.2392 %**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Independent constant annual probability, not a local forecast. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why can a high-hazard uninhabited place have lower risk than a moderate-hazard dense settlement? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 39: Earth resources and responsible extraction

### Geological concept

Geologic resources include water, aggregates, metals, industrial minerals, and energy-bearing materials with distinct formation processes and environmental costs. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Exploration combines geologic models with drilling and analytical testing; a mineral occurrence becomes a reserve only under qualified economic and technical criteria. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Geochemical assays, mapping, resource modeling, hydrologic monitoring, and impact baselines support phased evaluation. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** An assay from one hand sample shows an unusually high copper concentration.

**Competing explanations:** A localized vein, contaminated sample, or genuinely promising occurrence could all yield the value; none proves an economically recoverable reserve.

**Discriminating investigation:** Use documented chain of custody, systematic sampling, QA/QC and qualified resource evaluation before any economic statement.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

An assay result, a mapped deposit, a resource estimate, and a proven reserve are not equivalent claims. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Make a decision table that includes resource quality, uncertainty, extraction impacts, rehabilitation duties, and local governance. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 39

**Fictional input data:** A simplified ore body contains 1.5 million tonnes of rock at 0.6% metal mass grade. Estimate contained metal.

**Given:** M=1,500,000, g=0.6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `M*g/100` with the values above; the result is **9000 tonnes**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Not a reserve or economically recoverable production amount. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. What evidence would be needed before a promising rock sample could support a credible production claim? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 40: Evidence-driven site appraisal

### Geological concept

Practical geology integrates uncertain subsurface models with decisions about water, land use, excavation, and infrastructure. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Boreholes sample tiny volumes; geophysics interpolates bulk properties; monitoring records changes; iterative models improve as evidence accumulates. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Geotechnical logs, groundwater levels, geomorphic mapping, faults, and repeat surveys provide convergent or conflicting constraints. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Two boreholes show conflicting aquifer thickness despite being close together.

**Competing explanations:** A channel fill, fault juxtaposition, depositional lens or drilling-log interpretation difference could explain the discrepancy.

**Discriminating investigation:** Review logs, correlate independent markers, add a third strategically placed measurement, and quantify yield uncertainty before advising water-supply investment.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Desk-based evaluations cannot replace licensed site investigations and engineering design where safety-critical decisions are involved. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Present a clear go/no-go/collect-more-data recommendation with explicit assumptions and consequences of error. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 40

**Fictional input data:** Two hypothetical boreholes indicate a groundwater level of 18 m and 14 m over 400 m separation. Estimate magnitude of hydraulic gradient.

**Given:** h1=18, h2=14, L=400. Use consistent units and define relevant geometry.

**Steps:** Evaluate `abs(h1-h2)/L` with the values above; the result is **0.01 dimensionless**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Assumes hydraulic head measurements in common datum and one-dimensional flow. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How should a community decision change when two equally plausible groundwater models give different long-term yields? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 8: Geologic Mapping, Water, Hazards, and Resources — constructing and testing an explanation

**Scenario and provenance.** A fictional community needs a preliminary site appraisal for water supply and slope stability using sparse boreholes, a mapped fault, and variable aquifer properties. Distinguish screening from engineering certification. Every numerical value in the accompanying `datasets/unit-08.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: Reading geologic maps and cross sections; Groundwater flow and aquifers; Earth hazards and risk communication; Earth resources and responsible extraction; Evidence-driven site appraisal. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

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

## Unit 8 synthesis, transfer, and examination workshop

The five lessons in this unit—Reading geologic maps and cross sections, Groundwater flow and aquifers, Earth hazards and risk communication, Earth resources and responsible extraction, Evidence-driven site appraisal—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
