# Unit 4: Metabolic systems and constrained flux

**Scope and intended claim.** Students will enforce material balance and distinguish feasible solutions from measured flux. The unit emphasizes stoichiometry, steady-state feasibility, optimization objectives and sensitivity to exchange bounds. Its most important epistemic boundary is that a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

## Unit foundations

Metabolic systems illustrate the distinction between dynamics and feasibility particularly clearly. A stoichiometric matrix collects the reactants and products of a reaction list. Multiplying it by a flux vector yields the net rates of accumulation for metabolites. Under a steady-state approximation for internal metabolite pools, the matrix product is zero. This does not mean that uptake, conversion and secretion cease. It means that internal production and consumption are balanced during the interval of interest.

Constraint-based reconstruction adds upper and lower bounds for each reaction. A linear program can then find a feasible solution that maximizes an objective such as biomass synthesis or metabolite output. Because multiple solutions often exist, flux balance analysis should not be described as measurement of the true intracellular flux state. Solvers do exactly what their constraints and objective demand, even when the selected objective has poor biological justification for a resting, stressed or differentiated cell.

The most scientifically informative exercise is frequently not finding one optimum but changing a bound or objective and identifying which conclusions survive. Flux variability analysis reveals reaction-by-reaction ranges compatible with the chosen objective threshold. Dual sensitivity quantities such as shadow prices are local properties of the optimized mathematical problem. They may indicate that relaxing an uptake bound increases the objective for a small change, yet that relationship may break after the limiting resource shifts.

Pathway throughput is also not fully controlled by a single universally rate-limiting enzyme. Distributed control, metabolite accumulation and feedback can produce a different response to enzyme abundance than expected from a cartoon chain. Readers will therefore compare feasible flux patterns with specific, independently measurable quantities and acknowledge alternate pathways rather than presenting solver outputs as observed biochemical truth.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: internal flux-balance residual, available product after competing branch, joint carbon-oxygen limit, finite-difference local shadow estimate, flux range across alternate solutions. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 4.1 — Stoichiometric matrices and mass balance

**Learning goal.** Explain the mechanism or formal representation behind stoichiometric matrices and mass balance, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: enforce material balance and distinguish feasible solutions from measured flux.

### Core idea and biological meaning

The stoichiometric matrix S encodes metabolite consumption and production for each reaction. For internal steady state the flux vector v satisfies Sv = 0, subject to uptake and reaction bounds. This relation is a conservation constraint, not an assertion that cells have stopped metabolizing.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Write a three-reaction toy pathway with an intermediate metabolite. Use input, conversion and product export fluxes to see why internal production must equal internal consumption at steady state.

**Model construction.** Define internal versus exchange metabolites, write mass-balance constraints, note direction bounds and state the objective. A predicted flux should be tied to the assumption under which it is feasible or optimal. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Omitting a cofactor, exchange flux or compartment can create false cycles and unsupported high yields even when Sv = 0 in the incomplete reconstruction.

**Targeted improvement.** Inspect reaction balance, matrix dimensions and exchange conventions before solving; audit the solution for biologically unsupported flux loops.

**Heterogeneity and aggregation.** State whether the comparison concerns individual trajectories, population means, or the fraction of cells crossing a threshold. Nonlinear averaging changes outputs, and observed between-cell variation may mix model noise with differences in cell condition. Report a distribution or subgroup analysis when averages suppress the behavior central to the biological question.

### Worked synthetic numerical case — Internal flux-balance residual

The input values are invented solely for instruction: `input_flux = 7`, `output_flux = 7`. Apply `input_flux-output_flux` and obtain **0 flux units**. A zero residual is necessary for this toy intermediate at steady state. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

### Concept transfer and practice problems

**Transfer setting.** Map the same mass-balance concept to signaling complexes where conservation of a shared protein limits activation.

1. **Inference design.** Why might allowing reverse flow through an irreversible transport step change predicted product yield? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `input_flux-output_flux` from the fictional inputs. *Answer:* **0 flux units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 4.2 — Flux balance optimization

**Learning goal.** Explain the mechanism or formal representation behind flux balance optimization, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: enforce material balance and distinguish feasible solutions from measured flux.

### Core idea and biological meaning

Flux balance analysis commonly selects a feasible flux vector optimizing an assumed objective under linear constraints. It does not measure the unique intracellular flux state; multiple alternative optima can satisfy the same constraints. Biomass maximization is a context-dependent modeling objective, not a universal cellular law.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

In a toy branch pathway, allocate limited substrate between product and biomass. Change the objective from biomass production to desired metabolite export and examine how the optimal allocation changes.

**Model construction.** Define internal versus exchange metabolites, write mass-balance constraints, note direction bounds and state the objective. A predicted flux should be tied to the assumption under which it is feasible or optimal. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Reporting one optimal vector without objective, units, uptake bounds or alternate optima can mislead students into treating optimization results as direct observations.

**Targeted improvement.** Compare objective choices, check solver status, run feasible range analysis and seek extracellular flux data that constrain ambiguous predictions.

**Counterfactual perturbations.** A causal hypothesis earns explanatory value when it predicts what happens under a distinct intervention. Compare an intervention targeting the suggested mechanism with a rival intervention that preserves one observed association. When both interventions have indistinguishable predicted outcomes, the study must be redesigned rather than declaring a winner.

### Worked synthetic numerical case — Available product after competing branch

The input values are invented solely for instruction: `import_flux = 6`, `biomass_flux = 2`. Apply `import_flux-biomass_flux` and obtain **4 flux units**. Routing could differ when other reactions or cofactors matter. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

### Concept transfer and practice problems

**Transfer setting.** Compare resource allocation in microbial production with metabolic tradeoffs in rapidly dividing mammalian cells.

1. **Inference design.** When would a cell under stress fail to approximate a growth-maximizing solution? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `import_flux-biomass_flux` from the fictional inputs. *Answer:* **4 flux units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 4.3 — Limiting nutrients and shadow prices

**Learning goal.** Explain the mechanism or formal representation behind limiting nutrients and shadow prices, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: enforce material balance and distinguish feasible solutions from measured flux.

### Core idea and biological meaning

Exchange bounds express environmental limits. In linear programming a shadow price describes local improvement in an objective as a constraint is relaxed, within the sensitivity range of the current optimum. It is not a physical energy price or a universal biological benefit.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Model biomass limited by both carbon and oxygen; increase carbon supply alone, then oxygen supply alone. Record which change affects maximal growth under each condition.

**Model construction.** Define internal versus exchange metabolites, write mass-balance constraints, note direction bounds and state the objective. A predicted flux should be tied to the assumption under which it is feasible or optimal. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Shadow prices change when a different constraint becomes active; extrapolating a local derivative across large environmental changes gives unjustified predictions.

**Targeted improvement.** Identify active constraints and make a finite-difference sensitivity plot over small and large bound changes.

**Statistical and structural uncertainty.** Distinguish uncertain observations from uncertain rate constants, competing equations and unknown system boundaries. More precise data reduce only some forms of uncertainty; a model can remain underidentified after thousands of observations. Report assumptions and parameter equivalence classes when a single numerical point estimate would overstate the available information.

### Worked synthetic numerical case — Joint carbon-oxygen limit

The input values are invented solely for instruction: `carbon = 8`, `oxygen = 3`. Apply `min(carbon/2,oxygen)` and obtain **3 growth units**. The limiting rule is a fictional linear resource requirement. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

### Concept transfer and practice problems

**Transfer setting.** Translate nutrient limitation to phototrophic cultures where light supply can constrain biomass alongside fixed-carbon availability.

1. **Inference design.** What observation indicates the system is no longer carbon-limited even though carbon uptake remains high? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `min(carbon/2,oxygen)` from the fictional inputs. *Answer:* **3 growth units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 4.4 — Flux variability and alternate pathways

**Learning goal.** Explain the mechanism or formal representation behind flux variability and alternate pathways, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: enforce material balance and distinguish feasible solutions from measured flux.

### Core idea and biological meaning

A network may permit a range of reaction fluxes while preserving the same optimal objective. Flux variability analysis bounds each reaction while maintaining an objective requirement, and parsimonious criteria introduce additional preferences rather than empirical facts.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare two parallel pathways making the same product from the same precursor. A solver can send all flux through either branch without changing net product formation.

**Model construction.** Define internal versus exchange metabolites, write mass-balance constraints, note direction bounds and state the objective. A predicted flux should be tied to the assumption under which it is feasible or optimal. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** An internally consistent path should not be reported as evidence that the organism uses that path; alternative pathways need isotope tracing or selective perturbations.

**Targeted improvement.** Calculate alternative feasible ranges, annotate optional reactions and prioritize measurements that constrain branch usage.

**Computation and reproducibility.** Record the algorithm, input table, parameter initialization, numerical tolerances, random seed where relevant and comparison benchmark. Verify at least one limiting case analytically before interpreting a complex result. Reproducing the same incorrect answer faithfully is a computational achievement, not scientific validation.

### Worked synthetic numerical case — Finite-difference local shadow estimate

The input values are invented solely for instruction: `objective2 = 9`, `objective1 = 7`, `bound2 = 5`, `bound1 = 4`. Apply `(objective2-objective1)/(bound2-bound1)` and obtain **2 objective/bound**. The slope is local to the assumed optimization structure. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

### Concept transfer and practice problems

**Transfer setting.** Use this logic to interpret redundancy in microbial metabolic models and unexpected compensation after a gene perturbation.

1. **Inference design.** How can an identical extracellular uptake rate hide dramatically different intracellular routing? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `(objective2-objective1)/(bound2-bound1)` from the fictional inputs. *Answer:* **2 objective/bound**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 4.5 — Metabolic control and elasticities

**Learning goal.** Explain the mechanism or formal representation behind metabolic control and elasticities, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: enforce material balance and distinguish feasible solutions from measured flux.

### Core idea and biological meaning

Metabolic control analysis distributes control over steady-state fluxes and concentrations across system components. Flux control is usually shared rather than owned by one rate-limiting enzyme. An elasticity describes local sensitivity of one reaction rate to a metabolite under specified conditions.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Imagine two serial enzymes with substrate accumulation between them. Increasing the first enzyme may raise the intermediate without changing final flux if the second step remains restrictive.

**Model construction.** Define internal versus exchange metabolites, write mass-balance constraints, note direction bounds and state the objective. A predicted flux should be tied to the assumption under which it is feasible or optimal. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A large enzyme concentration change cannot be interpreted from a single elasticity when the entire pathway adjusts through metabolite pools and feedback.

**Targeted improvement.** Measure baseline and perturbed flux, include intermediate concentrations and define the perturbation range in which local coefficients remain meaningful.

**Transfer and scope.** Specify which context was represented by the training or thought experiment and which different context the learner wants to predict. Biological interactions can be present yet quantitatively altered by another cell type, nutrient condition or spatial organization. Explicit scope restrictions increase usefulness by preventing the model from being applied where its decisive assumptions fail.

### Worked synthetic numerical case — Flux range across alternate solutions

The input values are invented solely for instruction: `maxflux = 8`, `minflux = 2`. Apply `maxflux-minflux` and obtain **6 flux units**. A wide feasible range warns against claiming a unique intracellular rate. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of a solver produces an answer to its encoded assumptions, not an observation of intracellular pathways

### Concept transfer and practice problems

**Transfer setting.** Examine drug-target reasoning where inhibiting one enzyme redistributes control to other parts of the pathway.

1. **Inference design.** Why might doubling enzyme abundance yield only a small increase in pathway throughput? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `maxflux-minflux` from the fictional inputs. *Answer:* **6 flux units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: A resource-limited metabolic branching problem

**Scenario and deliverable.** Reconstruct a toy pathway with precursor import, two product branches and biomass synthesis. Express an internal steady state as S v=0, then compare objectives and uptake limits.

**Classroom data and assumptions.** Fictional feed availability is 10 flux units with a biomass branch capped at 6; no actual metabolism is represented. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Report a feasible flux solution, a competing feasible solution and the evidence that would distinguish them. Check mass balance and feasibility before claiming optimality. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Nutrient-limited capacity** and **Alternate-pathway allocation**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
