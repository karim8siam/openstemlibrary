# Unit 2: Magma Generation, Composition, and Storage

## Central question

**How do composition and thermal history alter volcanic materials and eruption potential?**

**Synthetic scenario.** A hypothetical magma storage zone receives basaltic recharge while cooling, crystallizing and interacting with crustal rocks; students evaluate ambiguous geochemical trends. This is an imagined classroom landscape; no measured eruption or real safety recommendation is implied.

## Concepts and study approach

The unit brings together **partial melting, crystallization, viscosity, magma mixing and subsurface storage**. Physical processes can be reconstructed from deposits, rock composition, geodetic observations or measured signals, but different materials survive and different instruments observe different parts of the system. The same observable feature may arise from distinct combinations of source conditions and later changes. The aim is to identify the evidence most capable of separating interpretations, not merely to attach a name to the most striking landform. The included case measurements and graphs were designed solely for teaching.

**Problem framing.** A hypothetical magma storage zone receives basaltic recharge while cooling, crystallizing and interacting with crustal rocks; students evaluate ambiguous geochemical trends. Imagine that students must present a short technical brief. Before making a numerical model, determine the time span, which observations are independent, and which boundaries are directly mapped rather than estimated. Data may have unequal completeness and calibration. Distinguish an interpretation based on direct field material from one inferred from numerical fitting or a remote sensor. Where the evidence allows more than one answer, explain what added observation would be valuable.

### Lesson 2.1: Partial melting and phase equilibria

**Learning objective.** Explain the physical reasoning behind partial melting and phase equilibria, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** A source rock can yield melt over a temperature and pressure interval; the fraction and chemical composition of melt vary with mineral assemblage, volatile content and melting path. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Read simplified solidus-liquidus diagrams and distinguish equilibrium from fractional extraction of melts. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** A linear melt-fraction model between solidus and liquidus is a classroom approximation, not a universal petrological law. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Mechanisms and competing explanations

A causal model should connect source conditions, transport, transformation and the observable product. The central mechanism is: A source rock can yield melt over a temperature and pressure interval; the fraction and chemical composition of melt vary with mineral assemblage, volatile content and melting path. This description predicts particular textures or signals, yet alternate processes might also produce parts of the same pattern. Use **A linear melt-fraction model between solidus and liquidus is a classroom approximation, not a universal petrological law.** as a test of an attractive but inadequate story. Set out two hypotheses with predictions that diverge at a practical sampling location. Retain the less dramatic hypothesis in the record until some observation actually rules it out; familiarity is not a substitute for comparison.

#### Contradictions worth testing

A scientific explanation is strengthened when it survives serious attempts at falsification. Here, a specific danger is: A linear melt-fraction model between solidus and liquidus is a classroom approximation, not a universal petrological law. Write the interpretation that a skeptical colleague would advance from the same field notebook. Then identify what the two explanations predict differently in rock fabric, chemistry, geophysical time series or deposit distribution. Record the proposed test before examining the answer so it cannot be adjusted after the fact. Where more than one hypothesis survives, report that ambiguity instead of choosing the version that tells the most coherent story.

#### Communication protocol

Write a technical paragraph and a public-facing paragraph using exactly the same evidence. In the public version, preserve uncertainty and cite the relevant observatory rather than presenting a student result as advice. Keep hazard, risk, exposure, vulnerability and uncertainty as separate concepts. The meaning of a forecast depends on the time window and the outcome that is counted. Apply it specifically to **partial melting and phase equilibria** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 2.1: Illustrative fraction melted between solidus and liquidus.** Input = 980 degrees Celsius; the specified relation is `Math.max(0,Math.min(1,(x-950)/350))` with `x` equal to that input. Substitution yields **0.0857143 melt fraction**. Assumptions and interpretation: Linear interpolation is a teaching approximation, not a real multi-phase melt model. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Explain why two parental melts with equal total melt fraction can have distinct chemical compositions. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 2.2: Major elements and volcanic rock names

**Learning objective.** Explain the physical reasoning behind major elements and volcanic rock names, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Basalt, andesite, dacite and rhyolite are useful labels for volcanic materials; formal classification uses accepted chemical or mineralogical conventions with attention to alteration. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Calculate oxide totals in normalized teaching analyses and identify immobile-element data that may be needed when alkalis have moved. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** A single silica percentage does not establish eruption style or complete the formal nomenclature of every volcanic rock. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Measurements and evidence quality

Implement the following discipline-specific measurement plan: Calculate oxide totals in normalized teaching analyses and identify immobile-element data that may be needed when alkalis have moved. Make sampling and calibration explicit. If an instrument observes several correlated points, avoid reporting them as fully independent replications. Carry the raw data and a record of exclusions into the final analysis. If a signal is close to the detection limit, show an interval or a qualified statement rather than an extra decimal place. Ask whether the same observational conclusion would emerge if the most uncertain record were removed or processed using another defensible method.

#### Worked quantitative reasoning

The numerical exercise uses fictional inputs and one declared equation, so it can be recalculated without external data. First determine the measured quantity, units, reference level and temporal averaging interval. Change the model input by a modest fraction and check whether the response is linear, nonlinear or bounded. Be careful not to infer that a good calculator result validates the underlying physics. For **major elements and volcanic rock names**, numbers support an explanation only when the chosen equation applies to the process, not merely because the units can be made to cancel.

#### Competing hypothesis protocol

Begin with three columns: observable feature, explanation A, explanation B. For each column decide whether an observation is expected, merely compatible or contradictory. The exercise should not put a weight of one on every observation: multiple measurements from the same camera, sample or process can be correlated. Where the evidence is ambiguous, propose a new measurement rather than manufacturing a definitive choice. Apply it specifically to **major elements and volcanic rock names** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 2.2: Fixed-composition illustrative melt viscosity.** Input = 1030.5 degrees Celsius; the specified relation is `1e5*Math.exp(150000/8.314*(1/(x+273.15)-1/1473.15))` with `x` equal to that input. Substitution yields **491537 dynamic viscosity (Pa s)**. Assumptions and interpretation: Arrhenius example only; crystals, shear rate, gases and composition held fixed. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Compare two synthetic analyses and document which classification is secure and which requires new measurements. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 2.3: Crystallization and differentiation

**Learning objective.** Explain the physical reasoning behind crystallization and differentiation, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** As minerals crystallize, the remaining melt may change composition; assimilation, recharge and mixing can produce similar chemical trends that require additional constraints. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Compare hypothetical mineral fractionation paths, crystal textures and compatible-element concentration patterns. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** An apparent differentiation array may combine separate magma batches rather than trace one closed-system liquid line of descent. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Physical scale and boundary conditions in practice

Physical interpretation changes with scale. A hand specimen, a ten-metre outcrop, a volcanic edifice and a satellite pixel do not offer interchangeable constraints on **crystallization and differentiation**. State the spatial support of each observation and the time averaging implicit in the selected method. Compare the variables held fixed in the worked exercise with the quantities that vary naturally. If your calculation assumes a homogeneous material or a steady flow, explain which observations could reveal heterogeneity, a discontinuity, or a shift in regime.

#### Designing an investigation in practice

An actionable class exercise is: Design paired petrography and trace-element tests to evaluate mixing versus fractional crystallization. Describe two observations that support the preferred inference and one that would substantially weaken it. Provide a sketch or table with a data dictionary and include both an expected result and a plausible unexpected result. Distinguish data gathered at the same site from independently sampled sites. Even if the teaching exercise is entirely desk-based, include metadata on coordinate systems, measurement precision, instrument or image source, and whether values are synthetic.

#### Mapping protocol

Provide a legend for directly mapped material, interpolated boundaries, inaccessible terrain, and the uncertain direction of transport. Label profiles with a consistent distance scale. When converting between a map and cross-section, note that topographic exaggeration alters the visual impression of slope and thickness. Any real-world hazard map would need expert validation not attempted here. Apply it specifically to **crystallization and differentiation** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 2.3: Illustrative fraction melted between solidus and liquidus.** Input = 1110 degrees Celsius; the specified relation is `Math.max(0,Math.min(1,(x-950)/350))` with `x` equal to that input. Substitution yields **0.457143 melt fraction**. Assumptions and interpretation: Linear interpolation is a teaching approximation, not a real multi-phase melt model. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Design paired petrography and trace-element tests to evaluate mixing versus fractional crystallization. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 2.4: Temperature, silica structure, and viscosity

**Learning objective.** Explain the physical reasoning behind temperature, silica structure, and viscosity, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Melt viscosity varies strongly with temperature, composition, dissolved volatiles and crystals; viscosity is not measured by a rock name alone. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Explore a temperature-sensitive viscosity law and consider shear rate, crystal fraction and changing water content as missing variables. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** An Arrhenius-form teaching calculation does not directly describe non-Newtonian crystal-rich magma or volatile-driven foaming. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Contradictions worth testing

A scientific explanation is strengthened when it survives serious attempts at falsification. Here, a specific danger is: An Arrhenius-form teaching calculation does not directly describe non-Newtonian crystal-rich magma or volatile-driven foaming. Write the interpretation that a skeptical colleague would advance from the same field notebook. Then identify what the two explanations predict differently in rock fabric, chemistry, geophysical time series or deposit distribution. Record the proposed test before examining the answer so it cannot be adjusted after the fact. Where more than one hypothesis survives, report that ambiguity instead of choosing the version that tells the most coherent story.

#### Interpretation, uncertainty, and safe limits

When presenting a result, separate the observation, the calculation and the implication in three sentences. An output that matches a conceptual model does not necessarily predict a real eruptive event. In this topic, **An Arrhenius-form teaching calculation does not directly describe non-Newtonian crystal-rich magma or volatile-driven foaming.** remains an important constraint even when the exercise appears numerically neat. Volcanic hazards affect communities and field researchers; classroom values must never become evacuation zones, thresholds, aircraft routing or claims of safety. The scientific report should end by naming what would have to be independently observed before any consequential application.

#### Time-series protocol

State acquisition times, the local-to-UTC conversion, instrument uptime, rate of sampling and any changes to detection limits. Calculate the effect of one missing observation on a simple mean, then compare this change with any claimed physical trend. Multiple channels may indicate the same phenomenon and should not automatically be interpreted as independent evidence. Apply it specifically to **temperature, silica structure, and viscosity** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 2.4: Fixed-composition illustrative melt viscosity.** Input = 1147.5 degrees Celsius; the specified relation is `1e5*Math.exp(150000/8.314*(1/(x+273.15)-1/1473.15))` with `x` equal to that input. Substitution yields **157238 dynamic viscosity (Pa s)**. Assumptions and interpretation: Arrhenius example only; crystals, shear rate, gases and composition held fixed. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** State the temperature range and measurements required before comparing two samples quantitatively. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

### Lesson 2.5: Reservoirs, dikes and magma mushes

**Learning objective.** Explain the physical reasoning behind reservoirs, dikes and magma mushes, design a suitable observation, evaluate a counterexample, and distinguish classroom arithmetic from an empirical volcanic conclusion.

**Scientific foundation.** Volcanic feeding systems may contain interconnected storage zones, crystal-rich mushes and transient dikes rather than one large permanently molten chamber. The issue is not resolved by knowing a label alone: observations may be indirect, sampled at different scales or altered after the event. A defensible explanation specifies the process, its boundary conditions and a plausible competing mechanism.

**Evidence and method.** Use petrological zoning, earthquake locations, deformation and geochemical recharge signatures as partly independent constraints. Define the instrument or mapping method, the measured physical quantity, the sampling interval and the possible biases. State what could be directly checked by another observer, without requiring them to accept your interpretation first.

**Common interpretive trap.** Ground inflation can result from multiple sources, including hydrothermal changes; interpreting every uplift as magma volume is unjustified. The corresponding methodological safeguard is to compare observations that should differ between explanations. A failure to collect discriminating data is a limitation, not proof that the working mechanism is right.

#### Establishing what is observed

Treat the starting point as an observation rather than a conclusion. For **Reservoirs, dikes and magma mushes**, describe the feature recorded in a map, sample, time series or laboratory log. A photograph should include scale and orientation, and a quantitative record should state units and detection limits. The next step is to ask whether **Use petrological zoning, earthquake locations, deformation and geochemical recharge signatures as partly independent constraints.** is directly measured or reconstructed. Where reconstruction is involved, name the underlying assumption instead of hiding it within a figure caption. A later researcher must be able to reverse that assumption without recreating the entire field campaign.

#### Worked quantitative reasoning

The numerical exercise uses fictional inputs and one declared equation, so it can be recalculated without external data. First determine the measured quantity, units, reference level and temporal averaging interval. Change the model input by a modest fraction and check whether the response is linear, nonlinear or bounded. Be careful not to infer that a good calculator result validates the underlying physics. For **reservoirs, dikes and magma mushes**, numbers support an explanation only when the chosen equation applies to the process, not merely because the units can be made to cancel.

#### Rock and material protocol

Describe texture and components before giving the sample a genetic name. Keep field identification separate from laboratory classification. Distinguish fresh juvenile material, older lithic fragments and secondary alteration where relevant. A classification statement should say what observations are decisive and what additional analysis would be needed to settle ambiguity. Apply it specifically to **reservoirs, dikes and magma mushes** using the supplied scenario. An effective report should make the observer’s original question visible and keep all artificial data marked as invented.

#### Checked numerical exercise

**Worked case 2.5: Illustrative fraction melted between solidus and liquidus.** Input = 1240 degrees Celsius; the specified relation is `Math.max(0,Math.min(1,(x-950)/350))` with `x` equal to that input. Substitution yields **0.828571 melt fraction**. Assumptions and interpretation: Linear interpolation is a teaching approximation, not a real multi-phase melt model. Recompute from the given numbers and state why additional digits would not increase physical reliability.

#### Research task and assessment

**Investigation.** Propose two storage geometries consistent with a fictional uplift and gas anomaly. Before starting, list the available evidence, feasible controls and at least one alternative explanation. Your product should include a labeled diagram, a small table, a calculation when appropriate, and a short uncertainty paragraph.

**Interpretation check.** Identify the most consequential uncertainty in your conclusion.

## Integrated research studio: Unit 2

**Scenario.** A hypothetical magma storage zone receives basaltic recharge while cooling, crystallizing and interacting with crustal rocks; students evaluate ambiguous geochemical trends. Assemble an evidence ledger with a row for each observation, its provenance, its measured units, and an explicit distinction between original observation and interpreted process. Add a third column for alternative hypotheses. Decide which items could be affected by the same source of error or sampling gap before computing averages, rates or correlations. A synthetic observation should be documented as such both in the file name and in any figure legend, because a decontextualized number can appear real after it is copied into another report.

**Research sequence.** First define a narrowly stated question. Second draw the relevant physical geometry or time axis. Third identify process variables that could be measured independently. Fourth check dimensional consistency of a simple model. Fifth create two alternative explanations and an observation capable of distinguishing them. Sixth record an uncertainty or sensitivity check. Seventh communicate the conclusion in a short paragraph aimed at technically informed readers and in another paragraph suited to nonspecialists, preserving the uncertainty in both.

**Practical assessment.** Use the explicitly synthetic CSV file for this unit to construct a two-panel visualization: one panel shows the fictional input series, and the other shows the result of a transparently specified numerical transformation. Add labeled axes and units; do not connect samples with a line if the observation units are unrelated. Explain whether outliers represent legitimate processes, data errors or unknowns. Describe how results change if the least complete rows are excluded, and archive the transformation steps.

**Scope and responsibility.** The educational concepts here do not generate official volcano warnings, physical access permissions or operational models of lava inundation, ash dispersal or lahar travel. Where a problem resembles an applied hazard calculation, the student must state why it lacks sufficient measurements for public-safety use. Official observatories and civil authorities are responsible for operational interpretations and decisions. For reproducible research, preserve the original dataset, all transformations, software environment information and the model assumptions.

## Simulation review

This unit's two browser models are **Illustrative fraction melted between solidus and liquidus** and **Fixed-composition illustrative melt viscosity**. Change each slider near its low, middle and high settings. Observe whether the numerical result rises, falls, saturates or changes rapidly. Explain which assumption produces that shape. The plotted curve is a property of its stated function, not an observation of a volcanic system.

