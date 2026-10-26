# Unit 5: Plate Tectonics, Earthquakes, and Deformation

## Orientation: a geologist's problem

How do motions of lithospheric plates generate faults, seismic waves, and mountains? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A schematic margin contains earthquake hypocenters, fault traces, paleomagnetic bands, and a topographic trench. Multiple lines of evidence are required before assigning boundary type. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 21: Plate motion: evidence and measurements

### Geological concept

Plate tectonics integrates seafloor spreading, subduction, transform motion, magnetism, earthquakes, and global kinematics. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Rigid plates move on a deformable mantle over time; local faults, distributed strain, and microplates complicate simple boundaries. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Marine magnetic anomaly patterns, earthquake distributions, bathymetry, GNSS velocity fields, and ocean-crust ages provide independent constraints. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** GPS stations on opposite sides of a mapped boundary diverge by centimeters over several years.

**Competing explanations:** The signal may indicate plate separation, local elastic deformation, groundwater-related subsidence, or reference-frame error.

**Discriminating investigation:** Use more stations and repeat processing in a consistent reference frame; compare geodetic direction with geological rates averaged over much longer time intervals.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

An instantaneous geodetic rate and a million-year mean spreading rate need not be equal. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Evaluate whether plate-motion estimates have consistent reference frames, timescales, and uncertainty definitions. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 21

**Fictional input data:** A plate moves at 4.2 cm/yr for 3 million years. Estimate displacement in kilometers.

**Given:** r=4.2, t=3. Use consistent units and define relevant geometry.

**Steps:** Evaluate `r*t*0.01*1e6/1000` with the values above; the result is **126 km**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Constant motion rate assumed. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can symmetric magnetic stripes support seafloor spreading even without seeing the crust form directly? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 22: Divergent and transform boundaries

### Geological concept

Extension generates new lithosphere at spreading centers, whereas transform motion accommodates lateral displacement without broadly creating or consuming plate area. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Partial melting beneath ridges relates to decompression; transform faults focus shear motion and earthquake hazard across offset ridge segments. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Ridge morphology, shallow earthquake mechanisms, magnetic stripes, and oceanic crustal structures identify boundary processes. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A seafloor map shows two spreading-ridge segments offset across a linear valley.

**Competing explanations:** Only part of the valley may represent an active transform; extensions beyond the ridges may be fossil fracture zones.

**Discriminating investigation:** Compare earthquake locations, focal mechanisms, magnetic stripe offsets and crustal age patterns rather than drawing one continuous active fault.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Not all transform fault segments remain active for their entire mapped length, and ridges may be asymmetric. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Separate boundary geometry from fault slip sense when annotating a tectonic map. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 22

**Fictional input data:** An oceanic crust band lies 120 km from the spreading center and is 6 Ma old. Estimate one-sided spreading speed in cm/yr.

**Given:** d=120, t=6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `d*1e5/(t*1e6)` with the values above; the result is **2 cm/yr**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** The distance is horizontal and ridge location is fixed. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can magnetic lineations and bathymetric offsets jointly distinguish ridge segments from transform faults? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 23: Convergence, subduction, and arcs

### Geological concept

Subduction returns dense lithosphere into the mantle and is associated with trenches, inclined seismic zones, arcs, and accretionary complexes. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Water-bearing material released from the slab affects mantle-wedge melting; compressional deformation may shorten overriding-plate crust. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Earthquake hypocenter depths, geochemistry, trench geometry, and arc locations constrain subduction architecture. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Intermediate-depth earthquakes line up beneath a volcanic arc.

**Competing explanations:** Their pattern can outline a descending slab, but scattered hypocenters and geometric projection can distort apparent slab angle.

**Discriminating investigation:** Inspect three-dimensional hypocenter uncertainty, trench position, and focal mechanisms before comparing depth-distance trends to a simplified planar model.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Trench depth by itself does not specify slab age or full convergence budget; flat slabs and complex geometries exist. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Compare multiple plausible plate geometries before inferring a direct correlation between distance inland and source depth. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 23

**Fictional input data:** A seismic slab is approximated as planar and dips 35°. How deep is it 90 km horizontally inland from a trench?

**Given:** x=90, theta=35. Use consistent units and define relevant geometry.

**Steps:** Evaluate `x*math.tan(math.radians(theta))` with the values above; the result is **63.01868 km**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Flat-Earth planar slab geometry only. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why are some earthquakes deep beneath arcs while transform earthquakes are usually shallow? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 24: Earthquake physics and wave records

### Geological concept

Earthquakes result from sudden fault slip and elastic stress release; seismic waves record source, path, and site effects. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

P and S body waves travel through the Earth with different speeds; surface waves and reflections can amplify or modify ground motion. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Arrival times, focal mechanisms, source spectra, geodetic offsets, and aftershock patterns constrain events. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A distant station records a clear P arrival followed by a later, stronger wave group.

**Competing explanations:** Possible phases include S waves, reflections, surface waves or site-amplified arrivals; a single timing offset is not a unique source solution.

**Discriminating investigation:** Use several stations, realistic velocity profiles and phase polarity to determine whether the chosen picks are comparable across the network.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Magnitude is not intensity, and neither alone predicts site-specific damage or the probability of a future earthquake. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Use a deliberately simplified travel-time model to understand location, then identify what realistic velocity heterogeneity changes. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 24

**Fictional input data:** A first-arrival P wave crosses 240 km at 6 km/s. Compute arrival time.

**Given:** d=240, v=6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `d/v` with the values above; the result is **40 s**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** The wave follows a straight homogeneous path. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why can two places equally distant from the same earthquake experience different ground shaking? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 25: Faults, folds, and crustal strain

### Geological concept

Faults localize brittle displacement while folds and ductile fabrics accommodate deformation over spatially and thermally varied conditions. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Differential stress, temperature, pressure, fluid effects, rock type, and strain rate influence deformation style. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Fault slickensides, displaced markers, fold hinges, cleavage, and shear-sense indicators can reveal movement history. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A displaced limestone layer is visible on both sides of a steep planar surface.

**Competing explanations:** Apparent offset on a single photograph need not equal the true slip vector, because exposure orientation affects projected separation.

**Discriminating investigation:** Measure bedding, fault plane and slickenside orientations; seek additional three-dimensional markers before assigning net displacement.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A fault surface's present attitude does not automatically equal its orientation at the time of motion because later rotation occurs. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Restore the geometry of markers before estimating displacement or regional shortening. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 25

**Fictional input data:** A hypothetical compressive force of 2.4 MN acts over 1.2 m². Estimate stress in MPa.

**Given:** F=2.4, A=1.2. Use consistent units and define relevant geometry.

**Steps:** Evaluate `F/A` with the values above; the result is **2 MPa**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Force perpendicular to a planar area. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How could you distinguish reverse-fault repetition of strata from a normal stratigraphic repetition caused by folding? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 5: Plate Tectonics, Earthquakes, and Deformation — constructing and testing an explanation

**Scenario and provenance.** A schematic margin contains earthquake hypocenters, fault traces, paleomagnetic bands, and a topographic trench. Multiple lines of evidence are required before assigning boundary type. Every numerical value in the accompanying `datasets/unit-05.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: Plate motion: evidence and measurements; Divergent and transform boundaries; Convergence, subduction, and arcs; Earthquake physics and wave records; Faults, folds, and crustal strain. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

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

## Unit 5 synthesis, transfer, and examination workshop

The five lessons in this unit—Plate motion: evidence and measurements, Divergent and transform boundaries, Convergence, subduction, and arcs, Earthquake physics and wave records, Faults, folds, and crustal strain—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
