# Unit 6: Multiscale integration: molecule to tissue

**Scope and intended claim.** Students will connect rapid molecular interactions with slower changes in cells and tissues. The unit emphasizes temporal ordering, phenotype mapping, population composition, spatial transport and nonlinear aggregation. Its most important epistemic boundary is that bulk measurements can combine state composition changes with changes within individual cells

## Unit foundations

A molecular interaction produces a phenotype only after many intervening steps. Rapid kinase activation can influence a transcription factor, whose targets alter protein abundance, which in turn changes a cellular decision and sometimes a tissue-level pattern. The timescales and measurement processes are heterogeneous. A protein reporter sampled after a delayed maturation step can record a very different profile from the initiating signaling pulse. Equal stimulus area does not guarantee equal phenotypic response when thresholds or nonlinear feedback are present.

Heterogeneous samples create a specific interpretive trap. If a bulk measurement increases, individual cells may express more of the measured molecule, or the fraction of high-expression cells may simply have increased. Those explanations require different biological accounts and different interventions. Single-cell experiments can help, but dropout, batch structure, destructive sampling and incomplete lineage information prevent them from being automatic solutions to every mixture problem.

Spatial systems require additional bookkeeping. Diffusion or transport moves material between local compartments while reactions create and consume it. A boundary source and molecular degradation can establish a stable gradient without any self-organizing instability. Reaction–diffusion systems with coupled activators and inhibitors can produce spontaneous patterns in certain parameter regimes, but a photographed stripe is not sufficient evidence of that mechanism. Geometry and boundary conditions must accompany the equations.

Coarse graining is itself a scientific assumption. For nonlinear response functions, evaluating a function at the mean individual input generally differs from averaging the individual outputs. Agent-based models, population ODEs and continuum PDEs therefore serve different observational scales. This unit asks what remains valid after aggregation and what evidence could justify a more detailed model.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: expected leap event count, pulse dose area, expected two-state expression, bulk mixture mean, spatial decay length. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 6.1 — Signaling-to-transcription integration

**Learning goal.** Explain the mechanism or formal representation behind signaling-to-transcription integration, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: connect rapid molecular interactions with slower changes in cells and tissues.

### Core idea and biological meaning

Rapid signaling activity can control slow gene-expression programs through transcription factors, chromatin state and feedback. The time-integrated input may matter more than peak amplitude, but that must be tested for each regulatory mechanism.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Deliver short high-amplitude and long low-amplitude synthetic input pulses with equal integrated dose. Compare predicted transcript and protein responses using a reporter model with degradation.

**Model construction.** Locate the map from molecular signal to cell outcome or from individual-cell output to tissue-level measurement. Mark which quantities are averaged, which are transported and where nonlinear functions are applied. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Sampling only the final protein abundance can conceal distinct signaling histories and delay processes.

**Targeted improvement.** Record phosphorylation and transcript trajectories, fit a staged model and evaluate whether it predicts a new pulse duration.

**Heterogeneity and aggregation.** State whether the comparison concerns individual trajectories, population means, or the fraction of cells crossing a threshold. Nonlinear averaging changes outputs, and observed between-cell variation may mix model noise with differences in cell condition. Report a distribution or subgroup analysis when averages suppress the behavior central to the biological question.

### Worked synthetic numerical case — Expected leap event count

The input values are invented solely for instruction: `propensity = 2`, `tau = 0.1`. Apply `propensity*tau` and obtain **0.2 events**. A tau-leap must not violate availability constraints or nonnegativity. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of bulk measurements can combine state composition changes with changes within individual cells

### Concept transfer and practice problems

**Transfer setting.** Apply the analysis to environmental stress responses where short pulses activate protective gene programs.

1. **Inference design.** What timing of a second pulse would expose memory in the signaling-to-transcription interface? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `propensity*tau` from the fictional inputs. *Answer:* **0.2 events**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 6.2 — From genes to cell phenotype

**Learning goal.** Explain the mechanism or formal representation behind from genes to cell phenotype, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: connect rapid molecular interactions with slower changes in cells and tissues.

### Core idea and biological meaning

Molecular network outputs such as transcript counts must be connected cautiously to cellular decisions such as migration, division or differentiation. Translation, protein turnover, cell-cycle phase and nutrient availability can alter the relation between expression and behavior.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Two hypothetical cells express the same proliferation marker but differ in available energy. A phenotype model that ignores nutrient state predicts identical division behavior; a coupled model may not.

**Model construction.** Locate the map from molecular signal to cell outcome or from individual-cell output to tissue-level measurement. Mark which quantities are averaged, which are transported and where nonlinear functions are applied. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Inferring cell function directly from one molecular marker is vulnerable to context effects and selection bias across cell states.

**Targeted improvement.** Integrate expression with time-lapse phenotypes or orthogonal functional measurements; calibrate decision thresholds against held-out observations.

**Counterfactual perturbations.** A causal hypothesis earns explanatory value when it predicts what happens under a distinct intervention. Compare an intervention targeting the suggested mechanism with a rival intervention that preserves one observed association. When both interventions have indistinguishable predicted outcomes, the study must be redesigned rather than declaring a winner.

### Worked synthetic numerical case — Pulse dose area

The input values are invented solely for instruction: `signal = 4`, `duration = 3`. Apply `signal*duration` and obtain **12 signal·minute**. Equal integrated doses need not give equal signaling outcomes. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of bulk measurements can combine state composition changes with changes within individual cells

### Concept transfer and practice problems

**Transfer setting.** Extend the reasoning to immune-cell activation, where marker expression and functional response are not synonymous.

1. **Inference design.** Could a molecular perturbation change transcript levels without affecting phenotype because of buffering in the protein network? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `signal*duration` from the fictional inputs. *Answer:* **12 signal·minute**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 6.3 — Cell population heterogeneity

**Learning goal.** Explain the mechanism or formal representation behind cell population heterogeneity, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: connect rapid molecular interactions with slower changes in cells and tissues.

### Core idea and biological meaning

A tissue sample can contain multiple cell states with different dynamics. Bulk averages mix within-state responses with changes in state proportions. Single-cell data add resolution but also technical sparsity, batch effects and destructive sampling limitations.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Consider two cell subpopulations with expression values of 2 and 10 units. A change in their proportions alters the bulk mean even when neither subpopulation changes its expression.

**Model construction.** Locate the map from molecular signal to cell outcome or from individual-cell output to tissue-level measurement. Mark which quantities are averaged, which are transported and where nonlinear functions are applied. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Apparent time-series regulation in a bulk sample may reflect composition shifts rather than cell-intrinsic transcriptional change.

**Targeted improvement.** Estimate cell-state proportions and within-state expression separately; compare with independently observed counts or lineage measurements.

**Statistical and structural uncertainty.** Distinguish uncertain observations from uncertain rate constants, competing equations and unknown system boundaries. More precise data reduce only some forms of uncertainty; a model can remain underidentified after thousands of observations. Report assumptions and parameter equivalence classes when a single numerical point estimate would overstate the available information.

### Worked synthetic numerical case — Expected two-state expression

The input values are invented solely for instruction: `fractionA = 0.25`, `levelA = 10`, `levelB = 2`. Apply `fractionA*levelA+(1-fractionA)*levelB` and obtain **4 expression units**. A state-mixture mean contains composition and within-state values. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of bulk measurements can combine state composition changes with changes within individual cells

### Concept transfer and practice problems

**Transfer setting.** Map this distinction to microbiome metatranscriptomic studies in which abundance and regulation are intertwined.

1. **Inference design.** What evidence can distinguish differentiation of existing cells from selective survival of a pre-existing state? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `fractionA*levelA+(1-fractionA)*levelB` from the fictional inputs. *Answer:* **4 expression units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 6.4 — Spatial patterning and reaction–diffusion

**Learning goal.** Explain the mechanism or formal representation behind spatial patterning and reaction–diffusion, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: connect rapid molecular interactions with slower changes in cells and tissues.

### Core idea and biological meaning

Diffusion couples local kinetics across tissue space. Reaction–diffusion equations can generate spatial gradients and patterns, but the emergence of a pattern depends on boundary conditions, diffusion coefficients, growth and geometry. Turing-type instability is one mechanism, not a universal explanation for stripes or spots.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Place a hypothetical signaling molecule at one edge of a one-dimensional tissue and compare steady gradients under weak and strong degradation. Observe how characteristic decay length changes.

**Model construction.** Locate the map from molecular signal to cell outcome or from individual-cell output to tissue-level measurement. Mark which quantities are averaged, which are transported and where nonlinear functions are applied. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A spatial pattern may result from preexisting tissue geometry or localized sources rather than spontaneous instability in an initially uniform system.

**Targeted improvement.** Record spatial coordinates and boundary conditions, test pattern predictions under altered geometry and quantify spatial residuals.

**Computation and reproducibility.** Record the algorithm, input table, parameter initialization, numerical tolerances, random seed where relevant and comparison benchmark. Verify at least one limiting case analytically before interpreting a complex result. Reproducing the same incorrect answer faithfully is a computational achievement, not scientific validation.

### Worked synthetic numerical case — Bulk mixture mean

The input values are invented solely for instruction: `frac_high = 0.3`, `high = 10`, `low = 2`. Apply `frac_high*high+(1-frac_high)*low` and obtain **4.4 expression units**. The bulk mean changes with cell proportions even without regulation in either state. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of bulk measurements can combine state composition changes with changes within individual cells

### Concept transfer and practice problems

**Transfer setting.** Compare morphogen gradients in embryos with spatial signaling in organized cell cultures.

1. **Inference design.** What perturbation could distinguish source-driven gradients from self-organized reaction–diffusion patterning? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `frac_high*high+(1-frac_high)*low` from the fictional inputs. *Answer:* **4.4 expression units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 6.5 — Multiscale linking and coarse graining

**Learning goal.** Explain the mechanism or formal representation behind multiscale linking and coarse graining, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: connect rapid molecular interactions with slower changes in cells and tissues.

### Core idea and biological meaning

Linking molecules to cells and tissues requires choices about aggregation, exchange of information and scale separation. A population-level rate often emerges from many individual behaviors and need not equal a single-cell rate evaluated at the population mean.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare a collection of cells with heterogeneous receptor occupancy to a single average cell. If activation is nonlinear, the mean activation of individuals differs from activation calculated at mean occupancy.

**Model construction.** Locate the map from molecular signal to cell outcome or from individual-cell output to tissue-level measurement. Mark which quantities are averaged, which are transported and where nonlinear functions are applied. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Averaging before applying nonlinear functions can erase rare, biologically consequential responses.

**Targeted improvement.** Specify how individual states map to population observables and benchmark coarse-grained predictions against a representative detailed simulation.

**Transfer and scope.** Specify which context was represented by the training or thought experiment and which different context the learner wants to predict. Biological interactions can be present yet quantitatively altered by another cell type, nutrient condition or spatial organization. Explicit scope restrictions increase usefulness by preventing the model from being applied where its decisive assumptions fail.

### Worked synthetic numerical case — Spatial decay length

The input values are invented solely for instruction: `diffusivity = 4`, `degradation = 0.25`. Apply `sqrt(diffusivity/degradation)` and obtain **4 distance units**. This ideal length applies to a simple linear one-dimensional reaction–diffusion case. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of bulk measurements can combine state composition changes with changes within individual cells

### Concept transfer and practice problems

**Transfer setting.** Apply the logic to immune infiltration of tissues and quorum-like microbial interactions.

1. **Inference design.** When is an agent-based representation necessary to capture contact-dependent interactions that an averaged ODE cannot? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `sqrt(diffusivity/degradation)` from the fictional inputs. *Answer:* **4 distance units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: From molecular pulse to mixed tissue

**Scenario and deliverable.** Combine a simple response-to-pulse model with two hypothetical cell types and a one-dimensional concentration gradient. Compare single-cell outputs with a bulk aggregate.

**Classroom data and assumptions.** Fictional cell groups contain 70 and 30 cells; source concentration decreases across five positions by a chosen educational profile. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Separate changes in mixture composition from changes within groups; evaluate whether spatial source placement can explain the predicted pattern. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Mixture-average reporter** and **Diffusion length scale**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
