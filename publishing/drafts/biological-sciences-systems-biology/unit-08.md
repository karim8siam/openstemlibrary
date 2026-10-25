# Unit 8: Applications, reproducibility and responsible use

**Scope and intended claim.** Students will examine interventions, engineering decisions, provenance and fairness. The unit emphasizes synthetic gene circuits, context-dependent disease networks, perturbation analysis and model exchange standards. Its most important epistemic boundary is that a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

## Unit foundations

Systems applications make the consequences of model choices visible. Synthetic gene circuits appear modular on diagrams yet compete with host resources and show leakage, saturation and cellular variability. A circuit that works at one operating point can change behavior with growth rate or copy number. Disease networks likewise combine heterogeneous evidence and can suggest counterfactual interventions, but associations and graph metrics do not authorize treatment choices. Computational feasibility must remain separate from claims of clinical or engineering effectiveness.

A useful perturbation study compares the same intervention under several plausible model structures and parameter sets. Changing one reaction rate can leave a steady state unchanged while altering transient recovery, noise or susceptibility to a second perturbation. Predictions robust across parameter uncertainty are generally stronger than a beautiful nominal curve. Conversely, disagreement between plausible models is informative: it points to an experiment that may distinguish them.

Reproducible computation needs more than a screenshot or code fragment. A shareable system records units, equations, species, parameters, initial states, events, solver settings, software version and simulation tasks. SBML captures many computational model structures, SED-ML describes simulation experiments, and COMBINE archives can package associated artifacts. Interoperability does not verify the biology: a perfectly reproducible wrong model remains wrong.

Model deployment carries ethical duties. An optimized numerical objective can encode missing perspectives, unrepresentative populations or unacceptable tradeoffs. A decision-maker needs the intended use, validity domain, uncertainty, known blind spots, accountability and conditions for withholding use. This final unit integrates modeling skills with a reproducibility checklist and a decision memo that makes boundaries clear.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: mean absolute prediction error, leaky and-gate response, mixture of intervention responses, relative perturbation reduction, group-weighted decision loss. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 8.1 — Synthetic gene circuits

**Learning goal.** Explain the mechanism or formal representation behind synthetic gene circuits, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: examine interventions, engineering decisions, provenance and fairness.

### Core idea and biological meaning

Engineered gene networks can implement switches, pulses and logic-like behaviors, but cellular context, host burden and molecular noise alter idealized circuit diagrams. Robust design requires quantitative characterization under conditions different from those used for construction.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare an ideal AND-gate truth table with a promoter showing leaky expression and saturation. A design that behaves logically at extremes may be ambiguous at intermediate inputs.

**Model construction.** Name the modeled intervention, its domain of use, uncertainties, missing groups and necessary independent verification. Make the distinction between simulation feasibility and approved real-world action explicit. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** An impressive average response can conceal unstable single-cell states or resource competition that changes as circuit copy number varies.

**Targeted improvement.** Define input/output measurement units and threshold criteria, assess variability and test a range of operating conditions rather than a single demonstration.

**Heterogeneity and aggregation.** State whether the comparison concerns individual trajectories, population means, or the fraction of cells crossing a threshold. Nonlinear averaging changes outputs, and observed between-cell variation may mix model noise with differences in cell condition. Report a distribution or subgroup analysis when averages suppress the behavior central to the biological question.

### Worked synthetic numerical case — Mean absolute prediction error

The input values are invented solely for instruction: `p1 = 5`, `p2 = 6`, `p3 = 7`, `y1 = 4`, `y2 = 7`, `y3 = 7`. Apply `(abs(p1-y1)+abs(p2-y2)+abs(p3-y3))/3` and obtain **0.6666667 units**. Compare errors only against held-out observations when claiming predictive validation. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

### Concept transfer and practice problems

**Transfer setting.** Translate these issues to biosensors whose output must remain interpretable across environmental variation.

1. **Inference design.** Which failure modes appear when two synthetic modules share the same limited regulator pool? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(abs(p1-y1)+abs(p2-y2)+abs(p3-y3))/3` from the fictional inputs. *Answer:* **0.6666667 units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 8.2 — Disease network interpretation

**Learning goal.** Explain the mechanism or formal representation behind disease network interpretation, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: examine interventions, engineering decisions, provenance and fairness.

### Core idea and biological meaning

A disease-associated network summarizes possible relationships among genetic changes, signaling and phenotypes. Association, inferred regulation and causal mechanism must be distinguished; patient heterogeneity and compensatory pathways can make a single network score misleading.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine two simulated cell states responding differently to inhibition of a shared signaling node because an alternative pathway is active in only one state.

**Model construction.** Name the modeled intervention, its domain of use, uncertainties, missing groups and necessary independent verification. Make the distinction between simulation feasibility and approved real-world action explicit. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A high-centrality node is not necessarily a safe or effective intervention target; context, toxicity and adaptive response are outside simple graph metrics.

**Targeted improvement.** Use perturbation-response evidence, quantify state heterogeneity and examine counterfactual predictions with uncertainty before ranking a mechanism.

**Counterfactual perturbations.** A causal hypothesis earns explanatory value when it predicts what happens under a distinct intervention. Compare an intervention targeting the suggested mechanism with a rival intervention that preserves one observed association. When both interventions have indistinguishable predicted outcomes, the study must be redesigned rather than declaring a winner.

### Worked synthetic numerical case — Leaky AND-gate response

The input values are invented solely for instruction: `leak = 0.05`, `gain = 1`, `pA = 0.8`, `pB = 0.9`. Apply `leak+gain*pA*pB` and obtain **0.77 relative output**. A nonzero leak complicates binary truth-table thresholds. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

### Concept transfer and practice problems

**Transfer setting.** Consider neurodegenerative and inflammatory conditions where multiple tissue compartments may contribute to the measured signature.

1. **Inference design.** Which independent observation would falsify an attractive network explanation of treatment response? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `leak+gain*pA*pB` from the fictional inputs. *Answer:* **0.77 relative output**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 8.3 — Perturbation analysis and control

**Learning goal.** Explain the mechanism or formal representation behind perturbation analysis and control, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: examine interventions, engineering decisions, provenance and fairness.

### Core idea and biological meaning

In-silico knockouts, parameter shifts and control inputs probe models, not real organisms. A perturbation may change steady output, recovery time or variability differently; robust control requires considering constraints and uncertainty rather than a single nominal trajectory.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Suppress an upstream activator by a fixed fraction in a two-pathway model and compare outcome when a compensating branch is weak versus strong.

**Model construction.** Name the modeled intervention, its domain of use, uncertainties, missing groups and necessary independent verification. Make the distinction between simulation feasibility and approved real-world action explicit. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A modeled knockout can predict no effect because the model omitted an interaction, not because the gene is redundant in the organism.

**Targeted improvement.** State perturbation type, magnitude, duration and uncertainty, then compare model scenarios with independent experimental readouts wherever appropriate.

**Statistical and structural uncertainty.** Distinguish uncertain observations from uncertain rate constants, competing equations and unknown system boundaries. More precise data reduce only some forms of uncertainty; a model can remain underidentified after thousands of observations. Report assumptions and parameter equivalence classes when a single numerical point estimate would overstate the available information.

### Worked synthetic numerical case — Mixture of intervention responses

The input values are invented solely for instruction: `fraction1 = 0.7`, `effect1 = 0.2`, `effect2 = 0.8`. Apply `fraction1*effect1+(1-fraction1)*effect2` and obtain **0.38 average response**. Averages hide differences between states and treatment contexts. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

### Concept transfer and practice problems

**Transfer setting.** Connect perturbation studies to systems-level experiments that seek mechanism rather than only better prediction.

1. **Inference design.** When would a brief pulse reveal network vulnerabilities that a permanent deletion cannot? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `fraction1*effect1+(1-fraction1)*effect2` from the fictional inputs. *Answer:* **0.38 average response**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 8.4 — Reproducible computational models

**Learning goal.** Explain the mechanism or formal representation behind reproducible computational models, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: examine interventions, engineering decisions, provenance and fairness.

### Core idea and biological meaning

A reusable model includes equations, unit declarations, initial values, parameters, solver settings, software versions, simulation tasks, evidence sources and licensing conditions. SBML, SED-ML and COMBINE archives facilitate exchange but do not make an incorrect model true.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine a published oscillator plot lacking the input schedule and solver tolerances. Reconstructing its equations alone cannot guarantee the same reported result.

**Model construction.** Name the modeled intervention, its domain of use, uncertainties, missing groups and necessary independent verification. Make the distinction between simulation feasibility and approved real-world action explicit. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Hidden parameter defaults and undocumented preprocessing choices can silently change model output across software environments.

**Targeted improvement.** Package machine-readable model definitions with simulation instructions, tests, provenance and a known reference plot; verify import/export in two independent tools if possible.

**Computation and reproducibility.** Record the algorithm, input table, parameter initialization, numerical tolerances, random seed where relevant and comparison benchmark. Verify at least one limiting case analytically before interpreting a complex result. Reproducing the same incorrect answer faithfully is a computational achievement, not scientific validation.

### Worked synthetic numerical case — Relative perturbation reduction

The input values are invented solely for instruction: `baseline = 10`, `after = 7`. Apply `(baseline-after)/baseline` and obtain **0.3 fraction**. A nominal reduction is not evidence for a specific causal mechanism. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

### Concept transfer and practice problems

**Transfer setting.** Apply model provenance principles to clinical or environmental models where outdated assumptions carry practical consequences.

1. **Inference design.** What reproducibility claim can be made if an archived simulation runs but conflicts with held-out biological observations? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(baseline-after)/baseline` from the fictional inputs. *Answer:* **0.3 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 8.5 — Model ethics and decision limits

**Learning goal.** Explain the mechanism or formal representation behind model ethics and decision limits, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: examine interventions, engineering decisions, provenance and fairness.

### Core idea and biological meaning

Systems models can influence resource allocation, biomedical hypotheses and environmental interventions. Decisions require attention to uncertainty, population representation, harms from model misuse and the boundary between simulation and validated evidence. No convenient computational result substitutes for ethical review or domain expertise.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare a simplified intervention recommendation based on one average response with one that reports response ranges across heterogeneous simulated groups.

**Model construction.** Name the modeled intervention, its domain of use, uncertainties, missing groups and necessary independent verification. Make the distinction between simulation feasibility and approved real-world action explicit. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Optimizing one numerical objective can hide distributional harms and encode contested value judgments inside ostensibly technical assumptions.

**Targeted improvement.** Identify stakeholders, intended use, exclusion criteria, uncertainty disclosure and conditions that would prohibit deployment before connecting predictions to action.

**Transfer and scope.** Specify which context was represented by the training or thought experiment and which different context the learner wants to predict. Biological interactions can be present yet quantitatively altered by another cell type, nutrient condition or spatial organization. Explicit scope restrictions increase usefulness by preventing the model from being applied where its decisive assumptions fail.

### Worked synthetic numerical case — Group-weighted decision loss

The input values are invented solely for instruction: `weight = 0.4`, `loss1 = 8`, `loss2 = 2`. Apply `weight*loss1+(1-weight)*loss2` and obtain **4.4 loss units**. The weighting encodes a value judgment and does not describe all possible harms. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a plausible simulation is never sufficient on its own to authorize biomedical or environmental action

### Concept transfer and practice problems

**Transfer setting.** Carry the same discipline into ecological conservation models where displaced harms may affect communities not represented by the modeled region.

1. **Inference design.** Which omitted variable could turn a biologically plausible prediction into a socially or clinically unsafe decision? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `weight*loss1+(1-weight)*loss2` from the fictional inputs. *Answer:* **4.4 loss units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: A reproducible model and limitations dossier

**Scenario and deliverable.** Package an equation set, all numerical inputs, simulation task description, plotted benchmark, provenance notes and a plain-language decision limitation. The model remains explicitly synthetic.

**Classroom data and assumptions.** An imaginary engineering team considers two interventions with model-predicted relative effects 0.12 and 0.18 but uncertainty ranges that overlap. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Present alternative explanations, the smallest relevant validation experiment and one circumstance where using this model to make a decision would be inappropriate. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Synthetic circuit leakage** and **Population-average response**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
