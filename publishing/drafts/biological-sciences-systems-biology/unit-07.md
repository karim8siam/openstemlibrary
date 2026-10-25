# Unit 7: Data-informed inference and predictive validation

**Scope and intended claim.** Students will estimate parameters honestly and test models beyond their calibration setting. The unit emphasizes measurement equations, uncertainties, identifiability, sensitivity, dimensionless groups and held-out experiments. Its most important epistemic boundary is that a flexible model can fit data accurately without yielding trustworthy extrapolations

## Unit foundations

Model calibration is an inverse problem: rather than calculating output from known parameters, it seeks parameters compatible with observed output. The choice of an error model influences the answer. Counting measurements may need a discrete likelihood, fluorescence readings can need background and heteroscedastic noise, and time series often contain serial dependence. A least-squares optimizer can locate a minimum even if its assumptions are scientifically inappropriate or the model is structurally incapable of resolving the unknown parameters.

Identifiability must be separated from optimizer convergence. For a constant synthesis and first-order decay process, the steady-state concentration identifies a ratio of two rates, not the rates separately. Repeating the same steady-state observation with less measurement noise narrows uncertainty in that ratio but does not resolve the missing direction. Carefully timed transients or an independent rate measurement may do so. Profile likelihoods, posterior diagnostics and algebraic reasoning expose such problems more reliably than one point estimate.

Sensitivity analysis is also conditional on definition and setting. A derivative at one parameter value does not establish global importance across a broad uncertainty range. Normalized sensitivities can be compared across units when properly defined, but correlated parameters and nonlinear interactions still matter. Dimensionless groups often reveal which combinations govern a system and where a reduced approximation might work. The aim is to understand what the predictions depend on rather than to rank every unknown with false precision.

Validating a model requires a genuinely new prediction. Randomly partitioning neighboring frames from the same time series can leak information into evaluation. Holding out a new perturbation, dose regime or biological condition is often more discriminating. No single statistical score certifies mechanism; evidence comes from predictive discrepancies, alternate models, residual diagnostics, and the ability to articulate what observation would refute the proposed explanation.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: nonlinear aggregation discrepancy, feature standard score, decay-rate estimate, local normalized elasticity approximation, steady birth–death rate ratio. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 7.1 — Data types, scaling and batch effects

**Learning goal.** Explain the mechanism or formal representation behind data types, scaling and batch effects, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: estimate parameters honestly and test models beyond their calibration setting.

### Core idea and biological meaning

Systems models integrate counts, intensities, concentrations, rates and categorical annotations. Transformations can equalize numerical scales without making measurements biologically commensurate. Batch effects can mimic or erase cross-omic associations if experimental design is confounded.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine transcriptomics and proteomics measured in separate batches. A combined latent component might capture processing date rather than coordinated regulation.

**Model construction.** Write the parameter set, measurement noise assumptions, calibration data and genuinely held-out prediction target. Record whether alternative parameters or model structures can produce similar fitted outputs. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Standardizing each feature to unit variance does not remove systematic technical differences or justify comparing measurement error across modalities.

**Targeted improvement.** Preserve raw values and units, record batch metadata and use controls or replicated overlap samples to estimate technical effects.

**Definition versus mechanism.** A descriptive quantity becomes mechanistic only when an explicit mapping connects it to events that generate the observations. Ask which extra assumptions make that mapping possible, whether those assumptions can be checked, and how a second representation could lead to a conflicting explanation. A second model is informative not because it contains more equations, but because it exposes which conclusion depends on a choice the first model hid.

### Worked synthetic numerical case — Nonlinear aggregation discrepancy

The input values are invented solely for instruction: `a = 1`, `b = 3`. Apply `(a*a+b*b)/2-((a+b)/2)**2` and obtain **1 squared units**. A nonlinear transformation of mean state differs from the mean of individual transforms. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a flexible model can fit data accurately without yielding trustworthy extrapolations

### Concept transfer and practice problems

**Transfer setting.** Connect these concerns to combining microscopy time courses with sequencing-based measurements.

1. **Inference design.** How would a balanced batch design differ from trying to correct perfectly confounded biological groups after data collection? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(a*a+b*b)/2-((a+b)/2)**2` from the fictional inputs. *Answer:* **1 squared units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 7.2 — Inverse problems and parameter fitting

**Learning goal.** Explain the mechanism or formal representation behind inverse problems and parameter fitting, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: estimate parameters honestly and test models beyond their calibration setting.

### Core idea and biological meaning

Parameter estimation asks which parameter values produce model outputs compatible with observations. Calibration requires a likelihood or loss function, explicit observation noise and parameter bounds grounded in meaning. A small residual is not enough to show that the model mechanism is identified.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Fit a first-order decay model to a few synthetic concentration measurements with uncertain time origin. Compare separate fits for decay rate and initial concentration against a joint fit.

**Model construction.** Write the parameter set, measurement noise assumptions, calibration data and genuinely held-out prediction target. Record whether alternative parameters or model structures can produce similar fitted outputs. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Optimizers can trade parameter values to obtain similar traces; local minima, sloppy directions and measurement offsets complicate interpretation.

**Targeted improvement.** Inspect residual patterns, confidence or profile intervals, multi-start fits and predictive behavior under an unused perturbation.

**Measurement and calibration.** Examine how the observed variable is constructed from the underlying biological state. A sensor may have background, nonlinearity, delay and a detection threshold; mathematical fitting should not treat these as biological responses. A useful validation set includes measurements outside the narrow conditions used to choose the observation mapping.

### Worked synthetic numerical case — Feature standard score

The input values are invented solely for instruction: `observed = 15`, `center = 10`, `scale = 2`. Apply `(observed-center)/scale` and obtain **2.5 standard deviations**. Standardization does not remove batch confounding. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a flexible model can fit data accurately without yielding trustworthy extrapolations

### Concept transfer and practice problems

**Transfer setting.** Compare kinetic fitting with estimating transition rates in a cell-state model from time-lapse data.

1. **Inference design.** Which additional sampling time most efficiently separates unknown initial state from unknown decay rate? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(observed-center)/scale` from the fictional inputs. *Answer:* **2.5 standard deviations**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 7.3 — Sensitivity analysis and dimensionless groups

**Learning goal.** Explain the mechanism or formal representation behind sensitivity analysis and dimensionless groups, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: estimate parameters honestly and test models beyond their calibration setting.

### Core idea and biological meaning

Sensitivity measures how a model output changes as a parameter changes. Local derivatives, normalized elasticities and global uncertainty analyses answer different questions. Nondimensionalization reveals combinations of parameters controlling behavior and can expose timescale separation.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Change a degradation constant around a nominal value, then compare output sensitivity at early and late times. A parameter influential at one time may matter little at another.

**Model construction.** Write the parameter set, measurement noise assumptions, calibration data and genuinely held-out prediction target. Record whether alternative parameters or model structures can produce similar fitted outputs. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A rank ordering from one nominal parameter set may reverse elsewhere; correlations among uncertain parameters also change influence estimates.

**Targeted improvement.** Report sensitivity definition, baseline point, perturbation range and output metric; confirm finite differences converge as step size decreases.

**Time ordering.** Identify which quantities cause changes and which respond later. Cross-sectional associations can be compatible with several temporal mechanisms, so draw at least two causal timelines before trusting the preferred account. An intervention at a carefully selected time can separate lagged effects that a steady-state comparison cannot resolve.

### Worked synthetic numerical case — Decay-rate estimate

The input values are invented solely for instruction: `start = 20`, `end = 10`, `elapsed = 5`. Apply `log(start/end)/elapsed` and obtain **0.1386294 per minute**. This estimate assumes first-order decay and a known baseline. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a flexible model can fit data accurately without yielding trustworthy extrapolations

### Concept transfer and practice problems

**Transfer setting.** Use the same logic to prioritize uncertain diffusivities in a tissue signaling model.

1. **Inference design.** What does a dimensionless ratio of production to degradation reveal that raw constants do not? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `log(start/end)/elapsed` from the fictional inputs. *Answer:* **0.1386294 per minute**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 7.4 — Structural versus practical identifiability

**Learning goal.** Explain the mechanism or formal representation behind structural versus practical identifiability, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: estimate parameters honestly and test models beyond their calibration setting.

### Core idea and biological meaning

Structural identifiability concerns uniqueness under ideal measurements; practical identifiability concerns whether finite noisy data constrain those theoretically unique quantities. Distinct parameter pairs may produce identical steady-state ratios but different transients.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

For a birth–death system, a steady-state level can constrain synthesis rate divided by degradation rate, but not both rates separately. Add a transient shutdown experiment in a purely conceptual design.

**Model construction.** Write the parameter set, measurement noise assumptions, calibration data and genuinely held-out prediction target. Record whether alternative parameters or model structures can produce similar fitted outputs. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Narrow optimizer output is not evidence of narrow uncertainty if constraints or priors determined the answer rather than observations.

**Targeted improvement.** Use algebraic parameter combinations, profile likelihoods or posterior diagnostics; document which data features identify each quantity.

**Conservation and resource limits.** Check which species, energy carriers or shared components are conserved or supplied by the environment. Balance equations should be obeyed before calibrating unknown parameters; otherwise an optimizer may compensate for a missing reaction. A conservation residual can be a more decisive model-quality diagnostic than a small discrepancy in the plotted outcome.

### Worked synthetic numerical case — Local normalized elasticity approximation

The input values are invented solely for instruction: `output2 = 4.4`, `output1 = 4`, `input2 = 1.1`, `input1 = 1`. Apply `(output2/output1-1)/(input2/input1-1)` and obtain **1 dimensionless**. Finite-difference estimates depend on the chosen perturbation range. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a flexible model can fit data accurately without yielding trustworthy extrapolations

### Concept transfer and practice problems

**Transfer setting.** Transfer the argument to receptor binding where equilibrium occupancy alone may constrain only a ratio of kinetic rates.

1. **Inference design.** Why does adding more replicas at the same steady state not necessarily identify two parameters separately? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(output2/output1-1)/(input2/input1-1)` from the fictional inputs. *Answer:* **1 dimensionless**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 7.5 — Model comparison and predictive validation

**Learning goal.** Explain the mechanism or formal representation behind model comparison and predictive validation, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: estimate parameters honestly and test models beyond their calibration setting.

### Core idea and biological meaning

Competing models should be evaluated on predictive targets relevant to the question, not only on training fit. Information criteria, cross-validation and held-out perturbations have different assumptions. A complex model is not favored merely because it has a smaller raw residual.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Fit a one-state decay and a two-state delayed model to the same training trace, then compare predictions after a new stimulation protocol.

**Model construction.** Write the parameter set, measurement noise assumptions, calibration data and genuinely held-out prediction target. Record whether alternative parameters or model structures can produce similar fitted outputs. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Splitting adjacent time points at random can leak temporal information; a held-out biological condition is often a stronger test of transfer.

**Targeted improvement.** State the comparison metric, held-out setting and uncertainty interval before fitting; retain biological plausibility checks alongside numerical scores.

**Nonlinearity and thresholds.** Compare the behavior of the model around a nominal input with its behavior at the edges of the intended input range. Saturation, cooperativity and alternative attractors can make a local approximation unreliable. Testing both increasing and decreasing interventions can reveal memory or threshold behavior invisible to a one-directional sweep.

### Worked synthetic numerical case — Steady birth–death rate ratio

The input values are invented solely for instruction: `birth = 24`, `decay = 8`. Apply `birth/decay` and obtain **3 molecule-equivalent units**. Steady abundance alone identifies a ratio rather than each rate. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a flexible model can fit data accurately without yielding trustworthy extrapolations

### Concept transfer and practice problems

**Transfer setting.** Apply model discrimination to alternative mechanisms of drug tolerance without mistaking prediction for causal explanation.

1. **Inference design.** If two models fit equally well, which perturbation would maximize disagreement between their predictions? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `birth/decay` from the fictional inputs. *Answer:* **3 molecule-equivalent units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: Discriminate two plausible kinetic hypotheses

**Scenario and deliverable.** Fit exponential decay and an alternative two-stage response to synthetic measurements, then hold out a second pulse protocol to test predictions. Include residual checks and parameter-profile discussion.

**Classroom data and assumptions.** Synthetic observations at minutes 0,2,4,6 are 19.6,14.5,10.5,8.0 in arbitrary units. Those values include invented observation error. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Show why a lower training error can coexist with worse held-out prediction; identify at least one structurally unidentifiable parameter combination. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Fitted exponential signal** and **Saturating sensitivity**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
