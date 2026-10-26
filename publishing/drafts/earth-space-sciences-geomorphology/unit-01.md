# Unit 1 — Landscape systems, scale and quantitative evidence

## Guiding scientific question

How can a landscape be described before its history is inferred?

## Unit perspective

A landscape is an evolving boundary between solid Earth, atmosphere, water, ice and living organisms. Landforms are recognizable patterns in surface geometry, but a recognizable shape does not, by itself, identify a unique process. A smooth convex hill may reflect soil creep over bedrock, weathering gradients or a inherited glacial surface. A steep river valley may reflect rapid incision, a change in rock resistance or a transient response to a downstream disturbance. Geomorphology therefore combines morphometry with sediment description, process measurements and independent chronological constraints. Students must learn to distinguish surface form, process, rate and age. The four are related but cannot be exchanged without justification. In this unit we first build the observational vocabulary: elevation, relief, slope, curvature, drainage divide, catchment, base level and scale. We then examine what is actually represented by a topographic map or digital elevation model (DEM). Elevation products are measurements or algorithms with vertical accuracy, cell size, acquisition dates and sometimes vegetation biases. One pixel is not one independent geological observation. Repeated surveys can reveal change, but require stable registration and explicit error propagation. Once these foundations are secure, rates can be expressed over relevant timescales without silently equating a short storm response to a million-year erosion average.

### Learning outcomes and scale discipline

By the end of this unit, students should be able to describe at least five independent landform or sediment observations, demonstrate one dimensionally consistent quantitative calculation, design a comparative measurement, and distinguish an interpretation from the observations used to support it. Practice viewing the same landform in a map, a section and a material description. Keep an explicit column for phenomena that are absent, unobserved or only assumed. At the finest scale, a few grain contacts may govern transport; at larger scales, inherited valley geometry and event histories control the response. Switching scale is legitimate only after specifying which variables remain meaningful. At the start of the field exercise, make a drawing of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet; list which parts would be measured directly and which reconstructed from other evidence.

The unit's measurement choices should include elevation benchmarks, raster resolution and field coordinate reference; the strongest report also checks independent spot heights and terrain gradients. Even a carefully derived rate does not establish its formative mechanism unless the sedimentary or stratigraphic evidence agrees. Interpret changes in the context of the process and observation interval, and use at least two sources of independent evidence. Most useful scientific uncertainties are not just numerical instrument errors: researchers must also consider incorrect boundaries, missing events, biased sample sites, mistaken ages and incomplete constitutive laws.

## Five topic lessons and worked investigations

## Lesson 1.1 — Slope, elevation and local relief

### Process mechanism and scale

Slope is vertical change divided by horizontal distance, whereas local relief compares extremes within a declared search window. Both depend on grid scale and slope is not an intrinsic constant of a landform. Draw a control volume showing forcing, material transfers and storage. Name the scale and timescale of the proposed process; landform shape alone does not reveal either.

### Observable evidence

Contour spacing, surveyed benchmarks, DEM aspect and curvature reveal whether a ridge is broad or sharply dissected. Record elevation benchmarks, raster resolution and field coordinate reference. In the diagram of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet, label measured features separately from inferred histories. Provide survey dates, scale and a detection threshold.

### Alternatives and field tests

A steep pixel at a vegetation boundary can be a lidar-ground-classification error rather than a cliff. Compute relief with two window sizes; survey three spot heights and repeat after coarsening the raster. Consider a spurious channel produced by raster flow filling. Identify one independently measurable outcome that would distinguish the two interpretations, and one negative result that would undermine the leading explanation.

### Worked quantitative example — Topographic slope

**Given.** A measured rise of 45 m along 1,500 m of horizontal ground distance. **Calculation:** 100 × rise / horizontal distance. **Result:** **3 %**. Work through the units before using the output to discuss Earth-surface history. If the horizontal distance is doubled at the same rise, the percent grade is halved. A profile sampled on an inclined map grid must still use true horizontal distance. A correct result from an incorrect conceptual model is not evidence that the process operated. State which measured variable would need independent verification. If the answer is a rate, indicate the averaging interval; if it is a geometric ratio, identify the scale and measurement direction; if it is a budget, give the boundary and the sign convention.

### Research procedure and critical interpretation

Document terrain registration; independently check depression treatment. Assess sensitivity to changing window size and verify dated markers. Record each raw observation, units, uncertainty and assumptions before model fitting.

Raster noise and smoothing can destroy sharp channels; relief statistics do not reveal the formative process. Always give units, horizontal datum, vertical datum and resolution with terrain metrics. A high-resolution shape map without ages and a dated deposit without spatial coverage offer different constraints. Explain how they could be combined for slope, elevation and local relief without overclaiming a process history. Identify one further test.

### Problems with answer guidance

**Problem 1.** Recalculate the worked case after changing an input by 20% and show units. **Problem 2.** Contrast two possible landform origins using a specific field test. **Answer guidance:** correct units, explicit physical assumptions and a genuinely distinguishing observation are essential.

## Lesson 1.2 — Drainage basins and divides

### Process mechanism and scale

A watershed consists of all points whose surface runoff joins an outlet under the flow-routing assumptions used. Divides can shift through capture or human drainage modification. Draw a control volume showing forcing, material transfers and storage. Name the scale and timescale of the proposed process; landform shape alone does not reveal either.

### Observable evidence

Ridge morphology, channel heads, road culverts and mapped flow lines constrain the divide. Record elevation benchmarks, raster resolution and field coordinate reference. In the diagram of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet, label measured features separately from inferred histories. Provide survey dates, scale and a detection threshold.

### Alternatives and field tests

A DEM sink may represent a true depression or a data artifact requiring hydrologic correction. Route flow before and after a carefully logged sink correction; check predicted crossings at roads. Consider a spurious channel produced by raster flow filling. Identify one independently measurable outcome that would distinguish the two interpretations, and one negative result that would undermine the leading explanation.

### Worked quantitative example — Watershed area

**Given.** 210 mapped raster cells, each 25 m by 25 m. **Calculation:** 210 × 25 × 25. **Result:** **131,250 m²**. Work through the units before using the output to discuss Earth-surface history. If pixel width doubles while the count remains constant, mapped area increases by a factor of four. A DEM boundary may exclude engineered drainage diversions. A correct result from an incorrect conceptual model is not evidence that the process operated. State which measured variable would need independent verification. If the answer is a rate, indicate the averaging interval; if it is a geometric ratio, identify the scale and measurement direction; if it is a budget, give the boundary and the sign convention.

### Research procedure and critical interpretation

Document terrain registration; independently check depression treatment. Assess sensitivity to changing window size and verify dated markers. Record each raw observation, units, uncertainty and assumptions before model fitting.

Subsurface flow in karst may cross topographic divides and urban drains can bypass surface networks. Validate basin area against observed drainage infrastructure and topography. A high-resolution shape map without ages and a dated deposit without spatial coverage offer different constraints. Explain how they could be combined for drainage basins and divides without overclaiming a process history. Identify one further test.

### Problems with answer guidance

**Problem 1.** Recalculate the worked case after changing an input by 20% and show units. **Problem 2.** Contrast two possible landform origins using a specific field test. **Answer guidance:** correct units, explicit physical assumptions and a genuinely distinguishing observation are essential.

## Lesson 1.3 — Long profiles and base level

### Process mechanism and scale

A river long profile records elevation against channel distance; slope breaks can reflect lithology, tectonics, sediment input or changing downstream boundary conditions. Draw a control volume showing forcing, material transfers and storage. Name the scale and timescale of the proposed process; landform shape alone does not reveal either.

### Observable evidence

Bedrock knickpoints, tributary junctions, strath terraces and mapped formations offer independent constraints. Record elevation benchmarks, raster resolution and field coordinate reference. In the diagram of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet, label measured features separately from inferred histories. Provide survey dates, scale and a detection threshold.

### Alternatives and field tests

A dam-related backwater step can imitate a natural grade adjustment. Project the profile above and below the break, map lithologic contacts and compare with an undammed tributary. Consider a spurious channel produced by raster flow filling. Identify one independently measurable outcome that would distinguish the two interpretations, and one negative result that would undermine the leading explanation.

### Worked quantitative example — Long-profile gradient

**Given.** 250 m of channel elevation loss over 12 km channel length. **Calculation:** 250 / 12. **Result:** **20.83333 m/km**. Work through the units before using the output to discuss Earth-surface history. Compare a 6 km reach having the same elevation drop: the reported gradient doubles. Channel distance differs from straight-line valley distance. A correct result from an incorrect conceptual model is not evidence that the process operated. State which measured variable would need independent verification. If the answer is a rate, indicate the averaging interval; if it is a geometric ratio, identify the scale and measurement direction; if it is a budget, give the boundary and the sign convention.

### Research procedure and critical interpretation

Document terrain registration; independently check depression treatment. Assess sensitivity to changing window size and verify dated markers. Record each raw observation, units, uncertainty and assumptions before model fitting.

A single profile is a snapshot; migration speed and forcing time cannot be read from shape alone. Require a second independent line of evidence before assigning a knickpoint to uplift. A high-resolution shape map without ages and a dated deposit without spatial coverage offer different constraints. Explain how they could be combined for long profiles and base level without overclaiming a process history. Identify one further test.

### Problems with answer guidance

**Problem 1.** Recalculate the worked case after changing an input by 20% and show units. **Problem 2.** Contrast two possible landform origins using a specific field test. **Answer guidance:** correct units, explicit physical assumptions and a genuinely distinguishing observation are essential.

## Lesson 1.4 — Topographic maps and digital elevation models

### Process mechanism and scale

Raster terrain grids interpolate samples; cell size, canopy penetration, interpolation and coordinate transforms affect derived slope and curvature. Draw a control volume showing forcing, material transfers and storage. Name the scale and timescale of the proposed process; landform shape alone does not reveal either.

### Observable evidence

Survey control points and repeat overlapping terrain swaths quantify spatial error and systematic offsets. Record elevation benchmarks, raster resolution and field coordinate reference. In the diagram of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet, label measured features separately from inferred histories. Provide survey dates, scale and a detection threshold.

### Alternatives and field tests

Elevated canopy returns may produce a false convex hill rather than genuine ground relief. Cross-section at a forest edge and compare ground-classified lidar to independent GPS benchmarks. Consider a spurious channel produced by raster flow filling. Identify one independently measurable outcome that would distinguish the two interpretations, and one negative result that would undermine the leading explanation.

### Worked quantitative example — Combined survey uncertainty

**Given.** Two independent vertical difference errors of 0.30 and 0.40 m. **Calculation:** sqrt(0.30² + 0.40²). **Result:** **0.5 m**. Work through the units before using the output to discuss Earth-surface history. A correlated offset cannot be removed by this independent-error expression. An error bound is not direct evidence of real change. A correct result from an incorrect conceptual model is not evidence that the process operated. State which measured variable would need independent verification. If the answer is a rate, indicate the averaging interval; if it is a geometric ratio, identify the scale and measurement direction; if it is a budget, give the boundary and the sign convention.

### Research procedure and critical interpretation

Document terrain registration; independently check depression treatment. Assess sensitivity to changing window size and verify dated markers. Record each raw observation, units, uncertainty and assumptions before model fitting.

Differencing two grids without coregistration can show apparent erosion over stationary terrain. Propagate measurement error before describing terrain change as real. A high-resolution shape map without ages and a dated deposit without spatial coverage offer different constraints. Explain how they could be combined for topographic maps and digital elevation models without overclaiming a process history. Identify one further test.

### Problems with answer guidance

**Problem 1.** Recalculate the worked case after changing an input by 20% and show units. **Problem 2.** Contrast two possible landform origins using a specific field test. **Answer guidance:** correct units, explicit physical assumptions and a genuinely distinguishing observation are essential.

## Lesson 1.5 — Dating surfaces and denudation rates

### Process mechanism and scale

Surface age estimates use materials tied to landform formation, while denudation is lowering of a surface averaged over a declared duration. Different clocks sample different processes. Draw a control volume showing forcing, material transfers and storage. Name the scale and timescale of the proposed process; landform shape alone does not reveal either.

### Observable evidence

Buried organic layers, tephra markers, luminescence samples and cosmogenic exposure histories may constrain chronology. Record elevation benchmarks, raster resolution and field coordinate reference. In the diagram of a ridge-line transect, two drainage paths, contour intersections and a catchment outlet, label measured features separately from inferred histories. Provide survey dates, scale and a detection threshold.

### Alternatives and field tests

An inherited boulder exposure age may predate deposition of the moraine on which it now sits. Compare stratigraphic position and replicate samples; test how inheritance and erosion bias the result. Consider a spurious channel produced by raster flow filling. Identify one independently measurable outcome that would distinguish the two interpretations, and one negative result that would undermine the leading explanation.

### Worked quantitative example — Long-term denudation

**Given.** 24 m of surface lowering averaged over 2 million years. **Calculation:** 24 / 2 × 0.001. **Result:** **0.012 mm/yr**. Work through the units before using the output to discuss Earth-surface history. Reducing the time interval by half doubles the inferred average rate. Event-scale rates can be much larger than geologic averages. A correct result from an incorrect conceptual model is not evidence that the process operated. State which measured variable would need independent verification. If the answer is a rate, indicate the averaging interval; if it is a geometric ratio, identify the scale and measurement direction; if it is a budget, give the boundary and the sign convention.

### Research procedure and critical interpretation

Document terrain registration; independently check depression treatment. Assess sensitivity to changing window size and verify dated markers. Record each raw observation, units, uncertainty and assumptions before model fitting.

Age uncertainty and episodic disturbance prevent treating a dated clast as a universal landscape timestamp. Convert lowering per time into consistent units with the averaging interval written out. A high-resolution shape map without ages and a dated deposit without spatial coverage offer different constraints. Explain how they could be combined for dating surfaces and denudation rates without overclaiming a process history. Identify one further test.

### Problems with answer guidance

**Problem 1.** Recalculate the worked case after changing an input by 20% and show units. **Problem 2.** Contrast two possible landform origins using a specific field test. **Answer guidance:** correct units, explicit physical assumptions and a genuinely distinguishing observation are essential.

## Integrated field-and-model capstone — Topography as a fallible dataset

Given an invented 25 m grid, digitize the ridge and outlet. Show how filling a single erroneous sink changes drainage area. Compare mean slope after resampling to 50 m and after applying a filter. Pair each topographic result with its acquisition assumption. Draft an evidence ledger indicating which inferred landforms remain ambiguous and name field observations that would change your confidence.

### Protocol and evidence allocation

Write a project proposal that names the study question, a defined sampling region, hypotheses H1 and H2 and three observations that could discriminate them. Build an input table with at least twelve synthetic measurements; record a unit, identifier, uncertainty class and data source for every row. Design one transect, one temporal repeat survey and one test using a different kind of evidence. State how the field team would avoid confirmation bias: preregister predicted outcomes, assign a second mapper to identify landforms independently and blind the initial data processing to the favored model. Any unmeasured quantity must be marked as an assumption. Base the arithmetic on the numerical cases in the unit, but do not present the invented data as actual measurements.

In the analysis, start with a mass or elevation balance rather than a purely visual explanation. If the balance does not close, label the residual and list processes that may lie outside the boundary, including sediment stored in a channel, transport at an unmonitored exit and error in estimated density or surface area. Separate interpretation of rate from reconstruction of age and chronology. An apparently consistent average rate can conceal long inactive periods punctuated by large storms, landslides or channel switching. Explore a parameter range wide enough to expose this sensitivity. Explain what observation would tell you whether the residual is an actual physical loss or a measurement artifact.

### Reporting template and peer review

The final report should contain: a title that describes an inquiry rather than a conclusion; data source and acquisition notes; a map or section with scale; a table of raw observations; a short derivation with units; alternative interpretations; uncertainty and detection limits; and an honest conclusion identifying what the exercise cannot show. A peer reviewer should trace one plotted value back to an original input without assistance. Report uncertainty in both physical data and causal attribution. Describe how sampling locations could bias the result, and identify one independent validation datum that was not used when choosing the model. Treat a good fit as a starting point for further testing, not proof of a unique historical trajectory.

### Assessment prompts and rubric

**Interpretation.** Provide two competing process histories consistent with the invented evidence, predict one differentiating field measurement, and identify which uncertainties could reverse the preferred interpretation. **Quantitative reasoning.** Recompute the selected unit case in SI units, vary two inputs independently, and interpret signs, magnitudes and nonlinearities. **Evidence ethics.** Identify all fabricated datasets and explain why they must never be described as real hazard, glacial or coastal monitoring records. **Review standard.** Full credit requires correct units, reproducible methods, a mass or geometry balance, explicit chronology limits and an alternative interpretation; numerical correctness alone is insufficient.

## Unit synthesis

Return to the guiding question: **How can a landscape be described before its history is inferred?** Make a process diagram contrasting an observable pattern with a process that could produce it. Now add a second process capable of leaving a similar pattern. Underline measurements that would distinguish the two. Ask whether the lesson's calculations predict the type of change measured by those instruments or only provide a scale for discussing it. The emphasis throughout geomorphology is not on naming spectacular landforms but on reconstructing defensible histories, with uncertainties, from repeatable measurements and physical consistency.
