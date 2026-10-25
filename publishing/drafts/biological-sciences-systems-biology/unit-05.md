# Unit 5: Stochastic biology and cellular diversity

**Scope and intended claim.** Students will describe distributions and rare events rather than means alone. The unit emphasizes jump processes, reaction propensities, noisy reporters, promoter switching and approximation methods. Its most important epistemic boundary is that random sampling of a model does not establish that the model is correct

## Unit foundations

When molecule numbers are small, the order and timing of reaction events vary from cell to cell. A deterministic equation may describe an expected tendency while obscuring how many cells reach zero molecules or enter a rare state. A discrete stochastic model specifies possible reaction events, how each event changes the state, and a propensity governing event occurrence. The chemical master equation evolves probabilities of discrete states; an exact stochastic simulation algorithm samples one possible history from the specified model.

Repeated trajectories matter because any single simulation can be atypical. The output of a stochastic teaching model should include a distribution, quantiles or event probabilities computed from many independent draws when uncertainty is central to the question. Simulation seeds make runs reproducible but should not be mistaken for new experimental replications. Comparing different seeds examines numerical variability under the same assumptions; comparing model predictions with independent measurements examines biological validity.

Heterogeneity has additional sources. Two cells may differ in size, enzyme abundance, cell-cycle position or microenvironment even if their reaction mechanisms are otherwise similar. Such extrinsic variation can be correlated across reporters, whereas molecule-level event variability may contribute more independent fluctuations. Measurement artifacts such as reporter maturation and photobleaching complicate decomposition of total variance. Transcript bursting adds another challenge: distinct promoter-switching rates can produce similar snapshot count distributions.

Exact event simulation becomes expensive for high-rate, high-copy-number systems. Tau-leaping and hybrid methods can be justified by a convergence and error analysis, not merely by speed. Students should check nonnegativity, conserved totals and sensitivity to step size, particularly for outputs driven by rare events rather than ensemble means.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: approximate finite flux control, birth–death stationary mean, total event propensity, poisson count coefficient of variation, fano factor of rna counts. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 5.1 — Chemical master equation concepts

**Learning goal.** Explain the mechanism or formal representation behind chemical master equation concepts, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: describe distributions and rare events rather than means alone.

### Core idea and biological meaning

A chemical master equation describes the time evolution of a probability distribution over discrete molecular states. At low copy number, events are random even if each reaction propensity is well defined. Mean behavior can therefore hide broad or asymmetric distributions.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

For a molecule undergoing synthesis and decay, imagine cells that begin with the same molecule count. Later count distributions differ although all cells follow the same kinetic rules.

**Model construction.** Identify discrete events and propensities, a specified initial count and a measurement time. Compare distributions from repeated trials with a deterministic reference rather than comparing only one simulated curve. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A deterministic mean trajectory cannot predict rare-event probabilities or cell-to-cell variability when copies are few or propensities are nonlinear.

**Targeted improvement.** State the discrete state, event channels, propensity and transition change before discussing probability dynamics.

**Definition versus mechanism.** A descriptive quantity becomes mechanistic only when an explicit mapping connects it to events that generate the observations. Ask which extra assumptions make that mapping possible, whether those assumptions can be checked, and how a second representation could lead to a conflicting explanation. A second model is informative not because it contains more equations, but because it exposes which conclusion depends on a choice the first model hid.

### Worked synthetic numerical case — Approximate finite flux control

The input values are invented solely for instruction: `fraction_flux_change = 0.12`, `fraction_enzyme_change = 0.3`. Apply `fraction_flux_change/fraction_enzyme_change` and obtain **0.4 dimensionless**. A finite ratio approximates a local control coefficient only for small changes. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of random sampling of a model does not establish that the model is correct

### Concept transfer and practice problems

**Transfer setting.** Transfer the framework to promoter occupancy where an individual binding event has an outsized impact on transcription.

1. **Inference design.** At what abundance could a continuous approximation become adequate for the specific question being asked? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `fraction_flux_change/fraction_enzyme_change` from the fictional inputs. *Answer:* **0.4 dimensionless**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 5.2 — Gillespie stochastic simulation

**Learning goal.** Explain the mechanism or formal representation behind gillespie stochastic simulation, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: describe distributions and rare events rather than means alone.

### Core idea and biological meaning

The stochastic simulation algorithm samples event waiting times and reaction identities from propensities in a well-mixed Markov jump process. It simulates a specified mathematical model; its random trajectories are not independent experimental validation of real biological dynamics.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare repeated birth–death simulations with identical initial counts and parameters. Report the distribution of molecule counts at a chosen time, not only a representative trace.

**Model construction.** Identify discrete events and propensities, a specified initial count and a measurement time. Compare distributions from repeated trials with a deterministic reference rather than comparing only one simulated curve. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Using one random seed or a handful of paths can conceal uncertainty in estimated quantiles, especially for rare switching events.

**Targeted improvement.** Record seed, reaction definitions, propensity expressions, stopping conditions and number of independent simulation replicates.

**Measurement and calibration.** Examine how the observed variable is constructed from the underlying biological state. A sensor may have background, nonlinearity, delay and a detection threshold; mathematical fitting should not treat these as biological responses. A useful validation set includes measurements outside the narrow conditions used to choose the observation mapping.

### Worked synthetic numerical case — Birth–death stationary mean

The input values are invented solely for instruction: `birth_rate = 6`, `decay_rate = 2`. Apply `birth_rate/decay_rate` and obtain **3 molecules**. Assumes constant birth and independent linear death with stationary conditions. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of random sampling of a model does not establish that the model is correct

### Concept transfer and practice problems

**Transfer setting.** Consider stochastic switching in a gene-regulatory circuit where waiting-time distributions matter more than mean expression.

1. **Inference design.** How does doubling all propensities affect the event timeline when event ratios remain constant? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `birth_rate/decay_rate` from the fictional inputs. *Answer:* **3 molecules**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 5.3 — Intrinsic and extrinsic variability

**Learning goal.** Explain the mechanism or formal representation behind intrinsic and extrinsic variability, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: describe distributions and rare events rather than means alone.

### Core idea and biological meaning

Intrinsic noise arises from probabilistic events within a biochemical network; extrinsic variability includes changes in cell size, resources, environmental state and other factors affecting many reactions. The distinction depends on the chosen model boundary and measurement design.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine two fluorescent reporters controlled by nominally equivalent promoters in the same cell. Shared fluctuations may produce correlated signals while reporter-specific fluctuations add independent variation.

**Model construction.** Identify discrete events and propensities, a specified initial count and a measurement time. Compare distributions from repeated trials with a deterministic reference rather than comparing only one simulated curve. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Reporter differences can reflect unequal maturation or stability rather than purely intrinsic transcriptional randomness.

**Targeted improvement.** Calibrate measurement noise, analyze covariance and compare within-cell with between-cell variance rather than equating all spread with mechanistic noise.

**Time ordering.** Identify which quantities cause changes and which respond later. Cross-sectional associations can be compatible with several temporal mechanisms, so draw at least two causal timelines before trusting the preferred account. An intervention at a carefully selected time can separate lagged effects that a steady-state comparison cannot resolve.

### Worked synthetic numerical case — Total event propensity

The input values are invented solely for instruction: `birth = 3`, `decay = 0.2`, `count = 10`. Apply `birth+decay*count` and obtain **5 events/min**. The next waiting time is exponential with the total propensity. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of random sampling of a model does not establish that the model is correct

### Concept transfer and practice problems

**Transfer setting.** Apply the distinction to single-cell proteomics and growth-rate variability across a clonal culture.

1. **Inference design.** Why might a higher population variance not imply any larger stochasticity at the molecular reaction level? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `birth+decay*count` from the fictional inputs. *Answer:* **5 events/min**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 5.4 — Bursting and promoter switching

**Learning goal.** Explain the mechanism or formal representation behind bursting and promoter switching, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: describe distributions and rare events rather than means alone.

### Core idea and biological meaning

Intermittent promoter activity can yield transcription bursts and overdispersed RNA counts. A two-state promoter model captures switching between transcriptionally active and inactive conditions, but biological transcription involves richer chromatin and regulatory dynamics.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare a constant low-rate transcription model with a promoter that occasionally switches ON and synthesizes several transcripts. Match their average RNA count and inspect how variance differs.

**Model construction.** Identify discrete events and propensities, a specified initial count and a measurement time. Compare distributions from repeated trials with a deterministic reference rather than comparing only one simulated curve. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Inferring a unique burst frequency and size from one snapshot may be impossible because multiple parameter combinations produce similar distributions.

**Targeted improvement.** Analyze both mean and variance across time or complementary reporter measurements, and test identifiability before assigning molecular mechanisms.

**Conservation and resource limits.** Check which species, energy carriers or shared components are conserved or supplied by the environment. Balance equations should be obeyed before calibrating unknown parameters; otherwise an optimizer may compensate for a missing reaction. A conservation residual can be a more decisive model-quality diagnostic than a small discrepancy in the plotted outcome.

### Worked synthetic numerical case — Poisson count coefficient of variation

The input values are invented solely for instruction: `mean_count = 5`. Apply `sqrt(mean_count)/mean_count` and obtain **0.4472136 fraction**. Poisson variability is a model benchmark rather than a universal cellular law. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of random sampling of a model does not establish that the model is correct

### Concept transfer and practice problems

**Transfer setting.** Connect promoter switching to developmental heterogeneity and cell-state transitions.

1. **Inference design.** How could time-resolved RNA labeling distinguish frequent small bursts from rare large ones? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `sqrt(mean_count)/mean_count` from the fictional inputs. *Answer:* **0.4472136 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 5.5 — Simulation approximations and uncertainty

**Learning goal.** Explain the mechanism or formal representation behind simulation approximations and uncertainty, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: describe distributions and rare events rather than means alone.

### Core idea and biological meaning

Tau-leaping, diffusion approximations and hybrid deterministic–stochastic methods trade computational cost for approximation error. Method choice should be guided by copy numbers, stiffness and the output of interest, especially when rare events determine decisions.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Run a hypothetical model with abundant metabolite A and scarce regulatory protein B. Treating both continuously may approximate mean A but miss the probability that B reaches zero.

**Model construction.** Identify discrete events and propensities, a specified initial count and a measurement time. Compare distributions from repeated trials with a deterministic reference rather than comparing only one simulated curve. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A fast simulation that generates negative molecule counts or depends strongly on timestep is not an acceptable shortcut, even if the graph looks smooth.

**Targeted improvement.** Compare small and large step sizes, monitor nonnegativity and conservation, and benchmark a reduced sample against exact event simulation.

**Nonlinearity and thresholds.** Compare the behavior of the model around a nominal input with its behavior at the edges of the intended input range. Saturation, cooperativity and alternative attractors can make a local approximation unreliable. Testing both increasing and decreasing interventions can reveal memory or threshold behavior invisible to a one-directional sweep.

### Worked synthetic numerical case — Fano factor of RNA counts

The input values are invented solely for instruction: `variance = 12`, `mean_count = 4`. Apply `variance/mean_count` and obtain **3 dimensionless**. Values above one can have multiple sources including bursting and extrinsic variation. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of random sampling of a model does not establish that the model is correct

### Concept transfer and practice problems

**Transfer setting.** Transfer the tradeoff to heterogeneous cellular populations where rare resistant states may dominate a later response.

1. **Inference design.** When is a hybrid model superior to either a full exact stochastic model or a fully deterministic approximation? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `variance/mean_count` from the fictional inputs. *Answer:* **3 dimensionless**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: Noise and reporter interpretation

**Scenario and deliverable.** Construct a birth–death reaction set with one stable reporter and one more rapidly degraded reporter. Simulate at least 100 independent trajectories and compare means, variance and the probability of zero molecules.

**Classroom data and assumptions.** Use invented synthesis rate 5 events per min and decay propensity 0.5 events per molecule per min; samples are classroom simulations only. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Assess random-seed sensitivity and explain which conclusions require a measured observation distribution rather than a modeled distribution. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Zero-count probability** and **Count relative variation**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
