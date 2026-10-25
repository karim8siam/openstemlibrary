# Unit 1: System representations and mathematical boundaries

**Scope and intended claim.** Students will build a traceable bridge from a biological question to a model representation. The unit emphasizes molecule counts versus concentrations, measured outputs versus hidden states, inputs versus feedback. Its most important epistemic boundary is that a model may fit the intended training observation while failing under a new intervention

## Unit foundations

Systems biology begins by deciding what to leave outside a mathematical description. A living cell does not possess a fixed border between the internally controlled and the externally imposed: oxygen availability, receptor ligands, the local tissue matrix and neighboring cells all become relevant under different experiments. If a ligand is a constant model input, a simulated cell may consume an unlimited supply. If the ligand is a state of a finite extracellular pool, binding and uptake deplete it. Both idealizations can be scientifically useful; the choice depends on the experiment and the claim.

Representations should begin with biological entities and observations, not with software. A list of state variables needs names, dimensions, initial values and a specification of whether these values are directly measured. For a one-compartment model of a transcript and protein, synthesis rates might have units of concentration per time and decay constants inverse time. Fluorescent intensity is then an output of an observation equation with background and maturation effects; it is not identical to protein concentration. Working with mixed units without an explicit conversion is a modeling error, not a harmless notation choice.

A reasonable modeling hierarchy moves from causal sketches to simple algebra or logical rules and only then to dynamic and stochastic representations where the question warrants it. The hierarchy need not be traversed in only one direction: a large ODE system can be reduced after sensitivity studies reveal that only a few combinations of variables affect the measured output. Model reduction creates a falsifiable approximation. It does not license ignoring fast variables that affect transient decisions, nor does it prove that the reduced components are biologically unimportant.

A testable boundary statement names an intended input, time horizon, spatial region and perturbation range. The same model may predict the direction of a short-term response and fail to predict the longer-term steady state. Unit 1 trains readers to document such limits explicitly so subsequent simulations, graphs and fitted parameters have a transparent scientific meaning.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: exposure area, background-corrected reporter, boolean state count, timescale separation ratio, share of conserved regulator. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 1.1 — Systems thinking and intervention boundaries

**Learning goal.** Explain the mechanism or formal representation behind systems thinking and intervention boundaries, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: build a traceable bridge from a biological question to a model representation.

### Core idea and biological meaning

A system model specifies interacting components, a defined environment, and a purpose for prediction. Its boundary is a scientific choice: extracellular ligand can be an input for a cell model but a state variable for an endocrine model. Boundaries determine which conservation laws and perturbations can be interpreted.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Consider a signaling module receiving pulses of an external cue while receptors and downstream enzymes change over time. Treat the ligand concentration as fixed in one model and depleted by binding in another; ask when predictions diverge.

**Model construction.** Translate the lesson into variables with units, initial values, known/unknown status, and an observation rule. Add a column for the scale at which the variable is meaningful, such as molecules per cell or concentration averaged over a tissue. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A boundary that suppresses feedback from the studied system to its environment can make intervention predictions look stable even when depletion changes the exposure.

**Targeted improvement.** First draw an influence diagram, then write a table stating which molecules are tracked, which are external inputs, and which processes cross the boundary.

**Definition versus mechanism.** A descriptive quantity becomes mechanistic only when an explicit mapping connects it to events that generate the observations. Ask which extra assumptions make that mapping possible, whether those assumptions can be checked, and how a second representation could lead to a conflicting explanation. A second model is informative not because it contains more equations, but because it exposes which conclusion depends on a choice the first model hid.

### Worked synthetic numerical case — Exposure area

The input values are invented solely for instruction: `amplitude = 3`, `duration = 4`. Apply `amplitude*duration` and obtain **12 nM·min**. Area of a rectangular stimulus is not necessarily equal to downstream activation area. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a model may fit the intended training observation while failing under a new intervention

### Concept transfer and practice problems

**Transfer setting.** Transfer the analysis from hormone signaling to nutrient-limited microbial growth, where external supply and internal uptake cannot always be treated independently.

1. **Inference design.** Would a short pulse or a long constant exposure expose the mistaken boundary more strongly? Explain what must be measured outside the cell. *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `amplitude*duration` from the fictional inputs. *Answer:* **12 nM·min**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 1.2 — Variables, units and observables

**Learning goal.** Explain the mechanism or formal representation behind variables, units and observables, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: build a traceable bridge from a biological question to a model representation.

### Core idea and biological meaning

State variables describe the evolving quantities of a model, parameters specify relationships, and observables map internal states to measurements. Protein concentration, molecule counts and fluorescence intensity are not interchangeable. A measurement equation can carry background, nonlinear response and detection limits.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Build an idealized gene-expression model with messenger RNA and protein states but only a fluorescent reporter readout. Two trajectories for protein concentration can produce similar observed intensities if maturation or background differs.

**Model construction.** Translate the lesson into variables with units, initial values, known/unknown status, and an observation rule. Add a column for the scale at which the variable is meaningful, such as molecules per cell or concentration averaged over a tissue. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A parameter estimate is not automatically a molecular concentration: arbitrary fluorescence units and unmeasured calibration factors may render absolute scale unidentifiable.

**Targeted improvement.** Specify every variable in a data dictionary with unit, sampling time, origin and expected measurement transform; include negative controls and a calibration scenario.

**Measurement and calibration.** Examine how the observed variable is constructed from the underlying biological state. A sensor may have background, nonlinearity, delay and a detection threshold; mathematical fitting should not treat these as biological responses. A useful validation set includes measurements outside the narrow conditions used to choose the observation mapping.

### Worked synthetic numerical case — Background-corrected reporter

The input values are invented solely for instruction: `signal = 850`, `background = 120`, `slope = 2.5`. Apply `(signal-background)/slope` and obtain **292 relative concentration units**. A valid calibration slope and background model are prerequisites. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a model may fit the intended training observation while failing under a new intervention

### Concept transfer and practice problems

**Transfer setting.** Compare a fluorescence reporter with an electrical readout of ion channel activity; both are indirect windows onto hidden biological states.

1. **Inference design.** How does adding one independent protein quantification measurement constrain otherwise equivalent state trajectories? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(signal-background)/slope` from the fictional inputs. *Answer:* **292 relative concentration units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 1.3 — Assumptions and model hierarchy

**Learning goal.** Explain the mechanism or formal representation behind assumptions and model hierarchy, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: build a traceable bridge from a biological question to a model representation.

### Core idea and biological meaning

A conceptual network, a Boolean model, ordinary differential equations and a spatial stochastic model answer different questions. Greater mathematical detail is not always greater validity. A useful hierarchy begins with the smallest representation capable of discriminating competing explanations.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Evaluate a two-gene switch with an ON/OFF abstraction before introducing continuous production and degradation rates. The discrete representation may identify a feedback motif without fixing its switching time.

**Model construction.** Translate the lesson into variables with units, initial values, known/unknown status, and an observation rule. Add a column for the scale at which the variable is meaningful, such as molecules per cell or concentration averaged over a tissue. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Adding unknown kinetic constants can increase the range of plausible behaviors instead of reducing uncertainty. Complexity is warranted only when observations or decisions require it.

**Targeted improvement.** Define the intended prediction first, such as steady-state sign, response time or event probability; choose a representation consistent with available temporal and spatial resolution.

**Time ordering.** Identify which quantities cause changes and which respond later. Cross-sectional associations can be compatible with several temporal mechanisms, so draw at least two causal timelines before trusting the preferred account. An intervention at a carefully selected time can separate lagged effects that a steady-state comparison cannot resolve.

### Worked synthetic numerical case — Boolean state count

The input values are invented solely for instruction: `nodes = 5`. Apply `2**nodes` and obtain **32 possible configurations**. Not all logical configurations are necessarily dynamically reachable. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a model may fit the intended training observation while failing under a new intervention

### Concept transfer and practice problems

**Transfer setting.** Apply the same hierarchy to immune-cell activation: categorical cell states may suffice for a population survey but not for rapid receptor phosphorylation.

1. **Inference design.** What new experimental observations justify replacing a Boolean update rule with differential equations? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `2**nodes` from the fictional inputs. *Answer:* **32 possible configurations**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 1.4 — Timescales and model reduction

**Learning goal.** Explain the mechanism or formal representation behind timescales and model reduction, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: build a traceable bridge from a biological question to a model representation.

### Core idea and biological meaning

Fast binding, medium-speed signaling and slow protein synthesis may be separated approximately, but not by assertion alone. Quasi-steady-state reduction replaces a rapidly relaxing variable by an algebraic relation, while careless elimination can destroy transient memory or introduce incorrect feedback.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine a receptor complex that equilibrates in seconds and a transcription factor that turns over in hours. Compare full and reduced trajectories after a brief ligand pulse and after a slow ramp.

**Model construction.** Translate the lesson into variables with units, initial values, known/unknown status, and an observation rule. Add a column for the scale at which the variable is meaningful, such as molecules per cell or concentration averaged over a tissue. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A variable can be fast under one experimental condition and slow near saturation or a critical transition, so a single reduction may not work everywhere.

**Targeted improvement.** Examine dimensionless timescale ratios, compare full and reduced simulations against a held-out perturbation and report an error measure, not just an attractive fit.

**Conservation and resource limits.** Check which species, energy carriers or shared components are conserved or supplied by the environment. Balance equations should be obeyed before calibrating unknown parameters; otherwise an optimizer may compensate for a missing reaction. A conservation residual can be a more decisive model-quality diagnostic than a small discrepancy in the plotted outcome.

### Worked synthetic numerical case — Timescale separation ratio

The input values are invented solely for instruction: `slow = 600`, `fast = 15`. Apply `slow/fast` and obtain **40 dimensionless**. A ratio of forty suggests but does not prove a successful fast-variable reduction. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a model may fit the intended training observation while failing under a new intervention

### Concept transfer and practice problems

**Transfer setting.** Relate timescale separation to enzyme intermediates in metabolic models and fast diffusion in tissue signaling models.

1. **Inference design.** Which feature of the pulse response would reveal that the removed variable stores biologically relevant memory? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `slow/fast` from the fictional inputs. *Answer:* **40 dimensionless**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 1.5 — Modularity, coupling and identifiability

**Learning goal.** Explain the mechanism or formal representation behind modularity, coupling and identifiability, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: build a traceable bridge from a biological question to a model representation.

### Core idea and biological meaning

Biological subsystems are often modeled as modules, but shared metabolites, sequestration, retroactivity and resource competition couple them. Modular descriptions simplify reasoning only when interfaces and conserved resources are stated. Structural identifiability asks whether ideal measurements could determine parameters uniquely.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Two promoter circuits compete for a finite transcription factor pool. An isolated-module prediction gives high expression for both; a coupled model predicts competition as target abundance changes.

**Model construction.** Translate the lesson into variables with units, initial values, known/unknown status, and an observation rule. Add a column for the scale at which the variable is meaningful, such as molecules per cell or concentration averaged over a tissue. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Fitting modules separately can conceal correlation among parameters that compensate for the same unobserved resource constraint.

**Targeted improvement.** Compare isolated and coupled predictions using one targeted perturbation and profile likelihood or algebraic reasoning to detect nonunique parameters.

**Nonlinearity and thresholds.** Compare the behavior of the model around a nominal input with its behavior at the edges of the intended input range. Saturation, cooperativity and alternative attractors can make a local approximation unreliable. Testing both increasing and decreasing interventions can reveal memory or threshold behavior invisible to a one-directional sweep.

### Worked synthetic numerical case — Share of conserved regulator

The input values are invented solely for instruction: `bound = 80`, `free = 120`. Apply `bound/(bound+free)` and obtain **0.4 fraction**. A competing module alters available free regulator without a direct edge. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a model may fit the intended training observation while failing under a new intervention

### Concept transfer and practice problems

**Transfer setting.** Translate the idea to metabolic pathway engineering where enzyme expression competes for cellular energy, ribosomes and precursor pools.

1. **Inference design.** Can increased binding-site number decrease output from an unrelated branch without any direct regulatory edge? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `bound/(bound+free)` from the fictional inputs. *Answer:* **0.4 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: The receptor-pulse boundary audit

**Scenario and deliverable.** Two idealized cellular modules receive an extracellular cue while a shared receptor pool is limited. Students submit two boundary diagrams, variable/unit dictionaries, one conservation ledger and an argument identifying which pulse experiments might separate the models.

**Classroom data and assumptions.** A fictional exposure series consists of times [0,1,2,3,4,5] min and normalized signals [0,0.37,0.62,0.75,0.70,0.49]; both arrays are invented. The reference total ligand amount is 60 arbitrary units, with 12 units measured in the bound pool at one point. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Describe a quantity that would not be conserved because material enters or leaves the chosen boundary. Distinguish measurement noise from a genuine missing state; state which added observation you would prioritize. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Finite boundary response** and **Reporter background**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
