# Unit 2: Networks: structure, evidence and interpretation

**Scope and intended claim.** Students will separate measured biochemical connections from statistical associations. The unit emphasizes directed versus undirected edges, condition-specific interaction evidence, node-level properties versus network-level function. Its most important epistemic boundary is that graph topology is descriptive and must not be equated with causal control

## Unit foundations

Network models encode information at multiple evidence levels. A correlation edge says that two measured features covary under the sampling and preprocessing choices used; it is not equivalent to a direct biochemical reaction. A physical interaction map usually does not specify whether a protein activates or inhibits another protein, while an inferred regulatory arrow may depend on perturbation design and unmeasured confounders. Mixing these edge meanings creates pathways that look mechanistic but cannot be translated into coherent kinetics.

Network statistics answer topological questions only for the graph supplied. Degree counts recorded neighbors; betweenness measures frequency on shortest paths; strongly connected components identify directed cycles. Those mathematical definitions do not by themselves establish an indispensable molecular role. A transporter with few links can be functionally essential, while an extensively connected scaffold may be dispensable under a particular environmental condition. Experimental sampling tends to be concentrated on well-studied proteins, which also affects observed connectivity.

Gene-regulatory motifs illustrate why topology and dynamics must be taught together. A feedforward graph can respond differently depending on its logic gate, thresholds and turnover times. Mutual inhibition can support switching under some nonlinear regimes, but it cannot be labeled bistable without analysis of actual equations. Metabolic graphs add a distinct discipline: reactions must honor stoichiometry, compartments and mass balance. An inferred enzyme annotation is not a measured flux, and a reconstructed reaction route may be infeasible in the real organism.

The integrated network investigation in this unit uses a fictional multi-layer cellular response. It asks students to rank proposed causal mechanisms and then choose new observations that could separate them. Ranking without evidence labels is disallowed: biological networks acquire explanatory power only as their definitions become inspectable.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: directed edge density, independent gate coincidence, steady path remainder, path-length in edges, normalized node degree. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 2.1 — Regulatory network edges and signs

**Learning goal.** Explain the mechanism or formal representation behind regulatory network edges and signs, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: separate measured biochemical connections from statistical associations.

### Core idea and biological meaning

A regulatory edge records a hypothesized influence and often a direction or sign, not necessarily a direct molecular binding event. Correlation networks, perturbation-based networks and biochemical interaction networks encode different evidence. Feedback cycles make network effects context-dependent.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

A transcription factor activates two targets, which appear correlated across cells. Introduce a third factor that changes both targets and compare the inferred graph under observational and targeted perturbation data.

**Model construction.** List each suggested relation and specify whether it is a biochemical stoichiometric reaction, a directly perturbed effect, a binding interaction or a statistical association. Record context: organism, cell type, time and compartment. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A graph with many plausible arrows may fit observations while remaining unable to distinguish direct regulation from common causes.

**Targeted improvement.** Label each edge as measured, inferred or assumed; keep evidence type and confidence with the graph, and test selected edges by independent perturbations.

**Heterogeneity and aggregation.** State whether the comparison concerns individual trajectories, population means, or the fraction of cells crossing a threshold. Nonlinear averaging changes outputs, and observed between-cell variation may mix model noise with differences in cell condition. Report a distribution or subgroup analysis when averages suppress the behavior central to the biological question.

### Worked synthetic numerical case — Directed edge density

The input values are invented solely for instruction: `edges = 6`, `nodes = 4`. Apply `edges/(nodes*(nodes-1))` and obtain **0.5 fraction**. This density excludes self-links and ignores evidence quality. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of graph topology is descriptive and must not be equated with causal control

### Concept transfer and practice problems

**Transfer setting.** Use the same evidence labels when reconstructing transcriptional programs from single-cell expression data.

1. **Inference design.** What experiment can distinguish A→B from a hidden C→A and C→B? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `edges/(nodes*(nodes-1))` from the fictional inputs. *Answer:* **0.5 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 2.2 — Gene-regulatory motifs

**Learning goal.** Explain the mechanism or formal representation behind gene-regulatory motifs, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: separate measured biochemical connections from statistical associations.

### Core idea and biological meaning

Feedforward loops, autoregulation and mutual repression provide recurring regulatory motifs. Motif behavior depends on logic gates, degradation, delays and input duration; a coherent feedforward loop is not inherently a delay filter in every parameter regime.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare an AND-controlled feedforward motif with an OR-controlled one under brief and sustained input pulses; track which target activates and how quickly it decays.

**Model construction.** List each suggested relation and specify whether it is a biochemical stoichiometric reaction, a directly perturbed effect, a binding interaction or a statistical association. Record context: organism, cell type, time and compartment. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Calling a motif a biological timer from graph structure alone mistakes topology for dynamics. Binding strengths, turnover and the readout threshold determine timing.

**Targeted improvement.** Draw the motif, choose explicit logical rules or rate laws, and plot response to both onset and removal of input.

**Counterfactual perturbations.** A causal hypothesis earns explanatory value when it predicts what happens under a distinct intervention. Compare an intervention targeting the suggested mechanism with a rival intervention that preserves one observed association. When both interventions have indistinguishable predicted outcomes, the study must be redesigned rather than declaring a winner.

### Worked synthetic numerical case — Independent gate coincidence

The input values are invented solely for instruction: `pA = 0.8`, `pB = 0.6`. Apply `pA*pB` and obtain **0.48 probability**. Multiplication assumes independent inputs, which biological regulation may violate. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of graph topology is descriptive and must not be equated with causal control

### Concept transfer and practice problems

**Transfer setting.** Examine stimulus filtering in developmental patterning where signal duration influences target-gene response.

1. **Inference design.** Can the same three-node wiring reject a brief ON pulse yet show rapid switching after input removal? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `pA*pB` from the fictional inputs. *Answer:* **0.48 probability**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 2.3 — Metabolic network reconstruction

**Learning goal.** Explain the mechanism or formal representation behind metabolic network reconstruction, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: separate measured biochemical connections from statistical associations.

### Core idea and biological meaning

A metabolic reaction network connects metabolites by stoichiometric transformations; an arrow must respect atom balance, compartment boundaries and direction assumptions. Genome annotation supplies candidates, not proof that an enzyme is active in a chosen environment.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Reconstruct a toy pathway converting an imported carbon source to a product and waste. Ask which reactions must exist for steady production and which transport step closes a missing compartment link.

**Model construction.** List each suggested relation and specify whether it is a biochemical stoichiometric reaction, a directly perturbed effect, a binding interaction or a statistical association. Record context: organism, cell type, time and compartment. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Gap filling can create a mathematically feasible route that is biologically dubious if reaction direction and evidence are ignored.

**Targeted improvement.** Audit every reaction against elemental balance and biological context, then compare predictions against isotope or uptake observations before expanding the network.

**Statistical and structural uncertainty.** Distinguish uncertain observations from uncertain rate constants, competing equations and unknown system boundaries. More precise data reduce only some forms of uncertainty; a model can remain underidentified after thousands of observations. Report assumptions and parameter equivalence classes when a single numerical point estimate would overstate the available information.

### Worked synthetic numerical case — Steady path remainder

The input values are invented solely for instruction: `import_flux = 6`, `waste_flux = 2`. Apply `import_flux-waste_flux` and obtain **4 flux units**. Net routing needs a balanced internal metabolic network. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of graph topology is descriptive and must not be equated with causal control

### Concept transfer and practice problems

**Transfer setting.** Connect the reconstruction problem to microbiome communities where cross-feeding creates reactions that appear only at community level.

1. **Inference design.** What missing transport process could make a valid intracellular sequence infeasible at the organism scale? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `import_flux-waste_flux` from the fictional inputs. *Answer:* **4 flux units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 2.4 — Protein interaction and signaling graphs

**Learning goal.** Explain the mechanism or formal representation behind protein interaction and signaling graphs, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: separate measured biochemical connections from statistical associations.

### Core idea and biological meaning

Physical association, phosphorylation influence and colocalization are distinct relations. A signaling network built by pooling interactions across tissues may contain routes that cannot operate in a single cell state. Direction, context, compartment and confidence need explicit encoding.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Consider a receptor, adaptor and kinase measured in different cellular compartments. A simple undirected interaction graph predicts a route that is impossible if the adaptor is excluded from the relevant compartment.

**Model construction.** List each suggested relation and specify whether it is a biochemical stoichiometric reaction, a directly perturbed effect, a binding interaction or a statistical association. Record context: organism, cell type, time and compartment. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** Network shortest paths can suggest mechanistic explanations that vanish when temporal expression and localization are considered.

**Targeted improvement.** Annotate nodes with abundance and compartment, distinguish direct binding from functional association, and seek time-resolved perturbation evidence.

**Computation and reproducibility.** Record the algorithm, input table, parameter initialization, numerical tolerances, random seed where relevant and comparison benchmark. Verify at least one limiting case analytically before interpreting a complex result. Reproducing the same incorrect answer faithfully is a computational achievement, not scientific validation.

### Worked synthetic numerical case — Path-length in edges

The input values are invented solely for instruction: `edge_count = 3`. Apply `edge_count` and obtain **3 edges**. A short path does not guarantee physical colocalization. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of graph topology is descriptive and must not be equated with causal control

### Concept transfer and practice problems

**Transfer setting.** Compare protein–protein interaction interpretation with ecological species interaction graphs; both require contextual assumptions before claiming mechanism.

1. **Inference design.** How might an apparent two-edge path fail when one partner appears only after the stimulus has ended? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `edge_count` from the fictional inputs. *Answer:* **3 edges**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 2.5 — Topology, centrality and robustness

**Learning goal.** Explain the mechanism or formal representation behind topology, centrality and robustness, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: separate measured biochemical connections from statistical associations.

### Core idea and biological meaning

Degree, betweenness, clustering and path length summarize graph structure but are not direct measures of biological indispensability. Highly connected proteins may be experimentally unimportant in a particular condition, while low-degree nodes may gate an essential pathway.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Rank three candidate nodes in a toy pathway by degree and by whether their deletion disconnects the product from its input. Observe that the rankings can disagree.

**Model construction.** List each suggested relation and specify whether it is a biochemical stoichiometric reaction, a directly perturbed effect, a binding interaction or a statistical association. Record context: organism, cell type, time and compartment. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A global network statistic can be dominated by experimental sampling bias and by edges imported from incompatible biological contexts.

**Targeted improvement.** Report the graph construction method, missing-data assumptions and a function-linked perturbation metric along with each topology statistic.

**Transfer and scope.** Specify which context was represented by the training or thought experiment and which different context the learner wants to predict. Biological interactions can be present yet quantitatively altered by another cell type, nutrient condition or spatial organization. Explicit scope restrictions increase usefulness by preventing the model from being applied where its decisive assumptions fail.

### Worked synthetic numerical case — Normalized node degree

The input values are invented solely for instruction: `neighbors = 5`, `nodes = 12`. Apply `neighbors/(nodes-1)` and obtain **0.4545455 fraction**. High degree is not equivalent to perturbation importance. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of graph topology is descriptive and must not be equated with causal control

### Concept transfer and practice problems

**Transfer setting.** Apply network robustness cautiously to host–microbe interaction maps rather than equating centrality with therapeutic suitability.

1. **Inference design.** Which deletion should receive priority if a low-degree metabolite transporter is the only route into an essential pathway? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `neighbors/(nodes-1)` from the fictional inputs. *Answer:* **0.4545455 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: An evidence-tagged three-layer network

**Scenario and deliverable.** Build a graph containing a regulator layer, a signaling layer and a small metabolic exchange layer. Every edge must carry a type (physical, causal hypothesis, statistical association or stoichiometric relation) and a provenance field.

**Classroom data and assumptions.** The fictional network has 11 nodes, 15 edges and 4 edges with unverified direction. Treat these numbers as an exercise, not an estimate for any organism. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Compare one centrality ranking with a function-linked knockout hypothesis; explain which biological conclusion is not justified by graph topology alone. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **Interaction coverage** and **Cooperative regulatory response**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
