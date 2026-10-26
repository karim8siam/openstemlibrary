# Unit 6: Metamorphism and Mountain Building

## Orientation: a geologist's problem

What can mineral transformations tell us about burial, heat, and exhumation? This unit approaches the problem through testable claims: identify the material or process, distinguish directly observed features from reconstructed events, specify what could make the interpretation wrong, and explain the scale at which a result should be used. These are different intellectual tasks. Good observations do not automatically supply an explanation; a plausible explanation is not an adequate substitute for a measurement plan. Physical geology connects descriptive geology, quantitative reasoning, and the history of the Earth, but it depends on maintaining these distinctions.

**Unit case:** A mountain transect crosses slate, schist, gneiss, plutons, and thrust sheets. Determine which clues indicate metamorphic grade and which indicate later deformation. Work with this as a fictional teaching scenario, not an actual measured field site. Write a preliminary hypothesis, an alternative hypothesis, a list of discriminating observations, and a decision about whether the existing information justifies a firm conclusion. A reader who begins with a favorite explanation should be able to describe the evidence that would lead them to abandon it.

### Learning goals and scientific habits

A successful student will be able to define the terminology in context, describe a plausible chain of processes, examine evidence at multiple scales, calculate an interpretable quantity, state assumptions, and propose measurements that could reject an incorrect explanation. Students should not memorize a list of isolated labels and confuse them for field competence. Field notebooks should preserve sketches, orientation, dimensions, date, coordinate reference systems, and uncertainty where relevant. The analytical workflow should preserve formulas, dimensional checks, and whether numbers are hypothetical examples or observed data.

The unit includes five concept lessons, five solved calculations, a data investigation, and two interactive teaching models. The model sliders expose a specific assumption and recalculate a quantity; they are intentionally simple. They do not constitute validated scientific forecasts, hazard assessments, or mineral exploration services. A model can be internally mathematically correct while being inappropriate for the intended site, because representativeness and boundary conditions are separate requirements.

### Unit-level synthesis map

Start with a measurable description and ask what conservation laws, boundary conditions, geometry, and timescales should connect it to a process. Compare the predicted trace of the process against observations. When a proposed cause is not unique, write down the alternative that best challenges it. Create a decision threshold tied to the intended use: conceptual understanding, preliminary screening, field campaign design, or certified professional work. A textbook exercise may be solved with the information given, whereas a real-world project may need more evidence before a number is safe to use. The most informative result is sometimes the identification of an unknown that changes the answer.

## Lesson 26: Metamorphic grade and mineral assemblages

### Geological concept

Metamorphism changes mineralogy and texture largely without complete melting, responding to pressure, temperature, bulk composition, and fluid chemistry. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Mineral reactions may create index assemblages, but equilibrium depends on reaction progress and availability of constituents. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Thin-section mineral associations, compositional zoning, and phase-equilibrium reasoning constrain relative grade. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A dark schist contains small garnet porphyroblasts along one traverse but not another.

**Competing explanations:** Different bulk rock chemistry could produce the mineral contrast without a simple change in metamorphic temperature.

**Discriminating investigation:** Compare protolith composition and associated chlorite, biotite or staurolite, and map repeated assemblages before drawing an isograd.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A single index mineral may be absent because bulk composition is unsuitable rather than because the rock never reached a given temperature. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Use assemblages and textural relationships, not isolated mineral names, to interpret pressure–temperature conditions. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 26

**Fictional input data:** Estimate lithostatic pressure at 12 km using 2700 kg/m³ and 9.81 m/s². Express MPa.

**Given:** rho=2700, g=9.81, z=12. Use consistent units and define relevant geometry.

**Steps:** Evaluate `rho*g*z*1000/1e6` with the values above; the result is **317.844 MPa**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Uniform density and gravity with depth. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why is garnet presence less decisive without knowledge of the rock's original composition? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 27: Metamorphic textures and deformation

### Geological concept

Foliation, lineation, porphyroblasts, and recrystallized grains preserve aspects of stress, growth, and deformation history. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Aligned platy minerals can develop during directed stress, whereas annealing may reduce lattice strain and produce equant grains. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Microscopic inclusion trails, cleavage intersections, and overgrown fabrics offer relative timing evidence. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Thin quartz-rich ribbons bend around larger porphyroblasts in a foliated rock.

**Competing explanations:** The ribbons may reflect deformation before, during or after mineral growth; their geometry must be interpreted relative to inclusion trails and matrix fabric.

**Discriminating investigation:** Document overgrowth edges and cross-cutting microstructures; avoid assigning one fabric to a single event without relative timing evidence.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

A mineral inclusion trail may be rotated after growth; two fabrics need not form at the same episode. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Present a sequence of fabric-forming events and clearly state any ambiguity between deformation and mineral growth. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 27

**Fictional input data:** A mineral grain diameter increases from 0.20 mm to 0.50 mm. Compute proportional linear growth.

**Given:** d1=0.2, d2=0.5. Use consistent units and define relevant geometry.

**Steps:** Evaluate `(d2-d1)/d1*100` with the values above; the result is **150 %**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Not an area or volume growth percentage. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can a porphyroblast contain an earlier fabric while the surrounding matrix shows a later one? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 28: Pressure–temperature paths and fluids

### Geological concept

Burial, heating, cooling, and exhumation trace paths through pressure–temperature space rather than a single peak condition. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Fluids transport heat and chemical constituents; reaction zones and veins can record open-system behavior. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Mineral zoning, thermobarometry, fluid inclusions, and isotopic analysis may constrain segments of a P–T history. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** High-pressure mineral inclusions occur within grains surrounded by lower-pressure assemblages.

**Competing explanations:** The inclusions may preserve a deeper stage of metamorphism even though the present matrix re-equilibrated during exhumation.

**Discriminating investigation:** Analyze compositional zoning, reaction rims and fluid pathways; test whether later minerals indicate a valid retrograde sequence instead of contamination.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Thermobarometers rely on calibration and phase-equilibrium assumptions and should not be presented as direct temperature sensors. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Estimate a pressure gradient with explicit density assumptions and compare it against independent petrologic evidence. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 28

**Fictional input data:** Temperatures along a hypothetical metamorphic path rise by 210°C over 7 km depth. Estimate gradient.

**Given:** DT=210, z=7. Use consistent units and define relevant geometry.

**Steps:** Evaluate `DT/z` with the values above; the result is **30 °C/km**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Depth and temperature increments do not prove steady state. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why might a metamorphic rock retain high-pressure minerals after exhumation to the surface? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 29: Regional metamorphism and orogenic belts

### Geological concept

Collisions and subduction can thicken, heat, deform, and later exhume crust, often creating regional metamorphic gradients. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Convergent tectonics builds mountain belts through shortening, thrust stacking, magmatism, and isostatic responses. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Mapped isograds, structural cross sections, metamorphic ages, and thermochronology integrate a belt's history. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** A regional transect shows thrust faults, changing metamorphic grade, and an exposed granite body.

**Competing explanations:** A collision history is plausible, but a single synchronous mountain-building event is not required to produce the whole assemblage.

**Discriminating investigation:** Compare mineral growth and intrusion ages with fault kinematics and distinguish magmatic from tectonic heating in the reconstruction.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

The highest present elevation does not always coincide with highest ancient burial or metamorphic grade. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Test a proposed mountain-building model against both surface geology and subsurface geophysical constraints. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 29

**Fictional input data:** A rock is exhumed 12 km in 6 million years. Estimate average exhumation rate.

**Given:** z=12, t=6. Use consistent units and define relevant geometry.

**Steps:** Evaluate `z*1e6/(t*1e6)` with the values above; the result is **2 mm/yr**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Path length simplified as vertical and rate constant. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. How can rocks from deep crust reach the surface without the whole region remaining at peak elevation? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Lesson 30: Mountain-belt history and exhumation

### Geological concept

Exhumation is the movement of a rock toward Earth's surface relative to its overburden, not simply uplift of a landform. Distinguish an observed feature from an inferred history. Identify the material, physical scale, and duration at issue. A useful explanation should predict an additional observation that was not already used to construct the hypothesis.

### Physical and chemical mechanisms

Erosion, faulting, and buoyant adjustment can reveal deep rocks; cooling ages can constrain timescales but not all motion components alone. Sketch the necessary starting conditions, pathway, and geological record. Ask whether transport, phase change, reaction, or deformation is involved and whether later processes could modify the predicted evidence.

### Evidence and analysis

Unconformities, detrital provenance, fault kinematics, cooling histories, and thermochronometric transects help reconstruct paths. Record sample provenance, measurement scale, instrument or descriptive method, and uncertainty. Where an observation can support more than one process, look for independent evidence that can discriminate between alternatives.

### Field notebook — a hypothetical example

**Setting:** Low-temperature cooling ages become systematically younger toward one fault-bounded valley.

**Competing explanations:** The pattern could imply differential exhumation, spatial temperature variation, or changes in the temperature sensitivity of the dating system.

**Discriminating investigation:** Combine multiple closure-temperature systems and structural offsets rather than converting an age gradient directly to vertical erosion rate.

Imagine presenting this evidence to a skeptical colleague. Specify three possible outcomes of the proposed test: supporting one explanation, favoring the alternative, or leaving the question unresolved. State any assumption about exposure, sample alteration, or instrument behavior.

### Limits of the interpretation

Elevation, surface uplift, rock uplift, and exhumation differ and must not be used as interchangeable measurements. The observed pattern need not determine a unique history; spatial coverage and the timing of later alteration affect confidence. Name a competing history in the field report and make clear whether its rejection depends on evidence that is actually available.

Distinguish rock displacement from erosional removal when developing a mass-balance history of a mountain range. Distinguish a classroom inference from an applied decision with health, safety, environmental, or financial consequences. Professional site assessment requires appropriate standards and qualified personnel; the models here are learning aids.

### Worked problem 30

**Fictional input data:** A fold-and-thrust belt shortens from 120 km to 93 km. Compute shortening percentage relative to original width.

**Given:** L0=120, L1=93. Use consistent units and define relevant geometry.

**Steps:** Evaluate `(L0-L1)/L0*100` with the values above; the result is **22.5 %**. Independent numeric verification inputs are supplied in `WORKED-CASES.json`.

**Interpretation:** Plane strain and restored original geometry assumed. This is not a measured quantity from a real exposure or site. Ask how the result changes under a different geological assumption.

### Practice

1. Why can a mountain belt lose elevation while rocks deep beneath it are exhumed rapidly? State a process, an observable test, and a rival interpretation.
2. Recalculate the worked problem after changing one input by 10%; state the unit and why the changed value matters.
3. Build a four-column evidence matrix: direct observations, proposed events, alternative events, and unresolved measurements.
4. Identify which practical decision would require an additional field measurement and explain why.

**Knowledge check:** Explain which inference this lesson supports, which it does not, and the single most valuable next observation.

## Integrated investigation 6: Metamorphism and Mountain Building — constructing and testing an explanation

**Scenario and provenance.** A mountain transect crosses slate, schist, gneiss, plutons, and thrust sheets. Determine which clues indicate metamorphic grade and which indicate later deformation. Every numerical value in the accompanying `datasets/unit-06.csv` is fictional. The table illustrates a possible data structure and does not represent real geological measurements, monitoring instruments, mapped hazards, mineral reserves, or any named community. The first task is to decide what the data can actually answer rather than to impose a preferred scientific story on the columns.

### Research question and rival models

Formulate a research question anchored to the unit's central themes: Metamorphic grade and mineral assemblages; Metamorphic textures and deformation; Pressure–temperature paths and fluids; Regional metamorphism and orogenic belts; Mountain-belt history and exhumation. Write a primary hypothesis that would explain the relationship between the first two recorded variables. Write a rival hypothesis that predicts either a weaker relationship or a different response if a third variable is controlled. For each hypothesis, identify one observation that would strongly support it and another that would challenge it. Avoid conflating association with causation; both curves may be generated by a shared, unmeasured process. Use the correct vocabulary for the kind of age, rock property, or geologic event that the variable is intended to represent.

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

## Unit 6 synthesis, transfer, and examination workshop

The five lessons in this unit—Metamorphic grade and mineral assemblages, Metamorphic textures and deformation, Pressure–temperature paths and fluids, Regional metamorphism and orogenic belts, Mountain-belt history and exhumation—should be understood as connected components of one scientific argument rather than isolated vocabulary. The first connects observations to an initial classification; the second or third develops a physical mechanism; and the later examples test whether that mechanism has explanatory and predictive power. Construct a one-page concept diagram showing these links. Each connecting arrow must be labeled with a physical reason, a measurement, or a conditional hypothesis. Do not connect two claims simply because they are both common geology terms.

**Transfer problem.** Imagine a new fictional site in which only half of the observations described in the unit are available and the remaining measurements would require costly fieldwork. State one conservative interpretation that the evidence supports, and one attractive interpretation that is still unwarranted. Rank three additional data-collection activities by expected usefulness, not by apparent technical sophistication. Define how an unfavorable result would change the interpretation. The point is to practice the economics of information: expensive observations are valuable only when they can alter a real decision.

**Examination problem.** Choose two solved numerical examples from the unit, change one input in each, and recompute the result with clearly displayed units. Describe the limiting behavior as the input approaches zero or becomes large, and assess whether the original formula remains physically appropriate there. Connect the calculation to a field observation that could be made with commonly available instructional equipment or public datasets. Distinguish an exact mathematical solution from a geologically validated model; mathematical consistency is necessary for a model but cannot establish its empirical applicability.

**Oral defense.** A reviewer challenges your interpretation using a contradictory field observation. Your response should not be to dismiss the observation or to invent undocumented special circumstances. Explain how you would confirm its provenance, whether it violates a necessary model prediction, and what other evidence could settle the disagreement. State one inference that would remain valid even if your preferred mechanism turned out to be wrong. That is the kind of robust knowledge that can survive revision when new evidence is collected.
