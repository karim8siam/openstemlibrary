# Unit 06 — Growth regulators and environmental signaling

> **OpenSTEM Biological Sciences / Book 12: Plant Physiology.** This is an original **unreviewed undergraduate study manuscript**. All example values, comparison series and computational results are synthetic teaching illustrations, not published experimental observations, crop management advice or independently validated predictions.

## Learning scope and conceptual foundations

Chemical signals and photoreceptors coordinate development with resources, light direction, mechanical conditions and seasonal timing. An understanding of basic biological chemistry, membrane transport, gas exchange and high-school algebra will help. The emphasis in this unit is on the **causal chain** connecting an environmental or developmental input to a cellular mechanism, the resulting physiological rate and the observable performance of an entire plant. A well-formed explanation has all four pieces. Naming a hormone or an enzyme without explaining how its action changes matter or energy flows does not answer a physiological question.

The five topics below relate to the following fundamental distinctions: **hormone concentration versus sensitivity; signal crosstalk and response location; light perception and transcription; directional growth and mechanical sensing; temporal and tissue context**. They are best learned as tools for deciding what to measure and how to interpret measurements. Many leaf measurements report a concentration, whereas the biological question concerns a flow or accumulation rate. Many comparative studies manipulate fertilizer, light, temperature or watering yet change several physiological inputs at once. A useful experimental diagram therefore shows where the treatment enters, what process it should alter, and what separate processes could mimic its observed consequence.

By the end of this unit a learner should be able to explain all five processes using cell or tissue mechanisms; independently reproduce five worked calculations with correct physical units; interpret the study's simulated dataset without treating it as real evidence; and propose a discriminating control for a competing hypothesis. Additional practice asks for counterexamples, not just definitions. In living plants a mechanism can be plausible and still fail to explain a particular experiment because organ age, water status, whole-plant resource availability or the time of day changes its operating state.

## Measurement before mechanism

A reproducible plant-physiology experiment begins with specimen identity, developmental stage, time of measurement, environmental history and a declared biological replicate. For gas exchange or transpiration specify area basis and temperature. For solutes specify concentration versus total amount, fresh mass versus dry mass and intracellular compartment where known. For time series decide whether independent plants were destructively harvested or repeated measurements came from the same individual. Neither a spectacular photograph nor a perfectly smooth fitted curve establishes a causal mechanism by itself.

There are three useful levels of uncertainty. **Instrument uncertainty** concerns calibration and resolution; **sampling uncertainty** concerns variation among independently grown plants or plots; and **model uncertainty** concerns assumptions used to turn readings into rates or parameters. These should not be merged into one vague caveat. Synthetic datasets in this unit demonstrate analytical reasoning but cannot estimate real-world uncertainty. In appropriate classroom experiments, use benign and authorized materials, avoid harmful chemical handling and follow the institution's biological and greenhouse safety policies.


## Topic 6.1 — Auxin gradients and directional growth

### Mechanistic explanation

Auxin biosynthesis, polar transport and cellular perception help organize tissue pattern and growth. Directional auxin distribution can lead to unequal expansion across an organ, contributing to bending during phototropism and gravitropism. Response depends on cell type and developmental stage; the same signal can support extension in one location and inhibition in another.

### Coupled constraints and functional trade-offs

A bend toward unilateral light is not proof that all tissues simply have more auxin on their shaded side at the measurement time. Photoreceptor activation, transporter relocation and wall properties interact dynamically. In roots, geometry and sensitivity differ from shoot responses, so applying a shoot rule directly to a root can reverse the prediction.

### How evidence would be collected

Grow seedlings in reproducible directional light, record curvature time courses and test a transporter mutant with complemented controls. Image reporter distributions while independently measuring elongation on both sides. A transient gradient should be sampled before its downstream deformation obscures cause and effect.

### Scope, assumptions and what must not be inferred

Exogenous auxin treatments can alter many tissues and uptake kinetics. A reporter measures a signaling proxy rather than absolute auxin concentration unless independently calibrated.

### Diagnostic distinction

In **auxin gradients and directional growth**, the central distinction is **hormone concentration versus sensitivity**. Specify the treatment, one tissue-level mediator, and a direct measurement that could distinguish the proposed mechanism from an alternative involving **signal crosstalk and response location**. A time course and appropriate control are stronger evidence than a single endpoint.

### Worked quantitative case 6.1

**Question.** A hypocotyl bends 24° over 3 hours under directional light. Estimate mean angular rate.

**Relation.** `rate = angle/duration`. Evaluate the supplied hypothetical quantities in consistent units. The calculated value is **8 degrees h−1**. Reconstruct the arithmetic independently and specify whether it estimates a flux, concentration, coefficient or fraction. A correct numerical answer without units and domain assumptions is incomplete.

**Interpretation.** Directional development involves unequal tissue extension. **Model boundary.** Angular speed is not a direct auxin concentration reading. This is a synthetic calculation, not a measured field value. Replace one positive input with a value 20% greater, recompute, and ask whether an intact plant could instead respond through feedback that changes other inputs. When a model assumes constant conditions, a measurement during a rapid transient can deviate even if the mechanism is scientifically reasonable.

### Test your explanation

Propose a control for the measurement described above. Explain how plant age or environment could change the predicted response, and identify a result that would falsify your favored mechanism. Distinguish a directly measured quantity from one inferred through the equation.


## Topic 6.2 — Abscisic acid and water-stress responses

### Mechanistic explanation

Abscisic acid signaling contributes to stomatal regulation, seed dormancy and acclimation to some stresses. Guard-cell ion channels and osmotic changes alter turgor to change pore aperture, while ABA-dependent transcription can modify longer-term responses. Signaling is modulated by biosynthesis, transport, receptors and degradation.

### Coupled constraints and functional trade-offs

A high ABA concentration need not produce stronger closure if guard-cell sensitivity changes or another environmental input dominates. Some stomatal responses to hydraulic shifts can precede slower hormonal changes. ABA should not be treated as a universal drought-on switch that always improves yield.

### How evidence would be collected

Under matched light and leaf temperature, follow ABA proxies, stomatal conductance and water potential during gradual soil drying. Compare a signaling-impaired genotype with appropriate background controls and rewatering. Separate early hydraulic timing from later transcriptional changes.

### Scope, assumptions and what must not be inferred

Hormone application dose in a dish does not correspond automatically to endogenous compartment concentration. Tissue transport and signal sensitivity matter.

### Diagnostic distinction

In **abscisic acid and water-stress responses**, the central distinction is **signal crosstalk and response location**. Specify the treatment, one tissue-level mediator, and a direct measurement that could distinguish the proposed mechanism from an alternative involving **light perception and transcription**. A time course and appropriate control are stronger evidence than a single endpoint.

### Worked quantitative case 6.2

**Question.** A guard-cell aperture proxy falls from 6.5 to 3.9 µm after ABA treatment. Find percent decrease.

**Relation.** `change = (initial−final)/initial×100`. Evaluate the supplied hypothetical quantities in consistent units. The calculated value is **40 %**. Reconstruct the arithmetic independently and specify whether it estimates a flux, concentration, coefficient or fraction. A correct numerical answer without units and domain assumptions is incomplete.

**Interpretation.** Aperture changes require context to predict whole-leaf conductance. **Model boundary.** Pore density and cuticular water loss remain unknown. This is a synthetic calculation, not a measured field value. Replace one positive input with a value 20% greater, recompute, and ask whether an intact plant could instead respond through feedback that changes other inputs. When a model assumes constant conditions, a measurement during a rapid transient can deviate even if the mechanism is scientifically reasonable.

### Test your explanation

Propose a control for the measurement described above. Explain how plant age or environment could change the predicted response, and identify a result that would falsify your favored mechanism. Distinguish a directly measured quantity from one inferred through the equation.


## Topic 6.3 — Gibberellins, cytokinins, ethylene and crosstalk

### Mechanistic explanation

Gibberellins can promote certain growth transitions and mobilization processes, cytokinins influence cell proliferation and developmental choices, and ethylene is a gas involved in diverse developmental and stress responses. These descriptions are roles, not exclusive functions. Molecular signaling networks incorporate biosynthesis, perception and shared regulatory targets.

### Coupled constraints and functional trade-offs

One developmental phenotype may arise from altered synthesis, altered transport or altered downstream responsiveness. Ethylene exposure can inhibit elongation in some seedlings yet promote other processes in different tissues. A simple one-hormone–one-outcome chart obscures such context and can lead to incorrect predictions for crop handling.

### How evidence would be collected

Apply controlled pulses or use genetic perturbations while monitoring more than one hormone-responsive marker and measuring tissue growth. Ensure environmental treatments do not themselves change gas exchange or water status. Use time-resolved observations to separate primary transcriptional effects from secondary growth changes.

### Scope, assumptions and what must not be inferred

Cross-talk means correlations between hormone abundance and phenotype are not enough. A mechanistic test must locate where a particular signal enters a broader network.

### Diagnostic distinction

In **gibberellins, cytokinins, ethylene and crosstalk**, the central distinction is **light perception and transcription**. Specify the treatment, one tissue-level mediator, and a direct measurement that could distinguish the proposed mechanism from an alternative involving **directional growth and mechanical sensing**. A time course and appropriate control are stronger evidence than a single endpoint.

### Worked quantitative case 6.3

**Question.** A stem elongates 4.8 mm with control and 7.2 mm with treatment in one day. Find relative enhancement.

**Relation.** `enhancement=(treatment−control)/control×100`. Evaluate the supplied hypothetical quantities in consistent units. The calculated value is **50 %**. Reconstruct the arithmetic independently and specify whether it estimates a flux, concentration, coefficient or fraction. A correct numerical answer without units and domain assumptions is incomplete.

**Interpretation.** Growth changes can result from multiple hormone pathways. **Model boundary.** Fresh mass and extension are not the same thing. This is a synthetic calculation, not a measured field value. Replace one positive input with a value 20% greater, recompute, and ask whether an intact plant could instead respond through feedback that changes other inputs. When a model assumes constant conditions, a measurement during a rapid transient can deviate even if the mechanism is scientifically reasonable.

### Test your explanation

Propose a control for the measurement described above. Explain how plant age or environment could change the predicted response, and identify a result that would falsify your favored mechanism. Distinguish a directly measured quantity from one inferred through the equation.


## Topic 6.4 — Phytochrome, cryptochrome and shade signaling

### Mechanistic explanation

Plants perceive qualities of light as well as total photon availability. Phytochromes respond to red and far-red signals, cryptochromes and phototropins to blue-light regimes, and signaling networks influence germination, de-etiolation and neighbor responses. The ratio of light wavelengths reaching a leaf can provide information about surrounding vegetation.

### Coupled constraints and functional trade-offs

Shade avoidance can increase elongation while reducing structural robustness or reproductive allocation under some conditions. A low red-to-far-red ratio is not equivalent to low total light, and plants can respond differently when irradiance, temperature and spectral composition vary independently.

### How evidence would be collected

Use controlled spectral treatments with measured photon flux and comparable temperatures. Record hypocotyl length, leaf angle and photosynthetic capacity, and test a receptor-deficient line where feasible. Distinguish developmental plasticity from changes caused simply by lower assimilate production.

### Scope, assumptions and what must not be inferred

An action spectrum is not an identity certificate for a single receptor; multiple photoreceptors can share wavelength regions and interact.

### Diagnostic distinction

In **phytochrome, cryptochrome and shade signaling**, the central distinction is **directional growth and mechanical sensing**. Specify the treatment, one tissue-level mediator, and a direct measurement that could distinguish the proposed mechanism from an alternative involving **temporal and tissue context**. A time course and appropriate control are stronger evidence than a single endpoint.

### Worked quantitative case 6.4

**Question.** Leaf area increases from 16 to 19.2 cm2 after spectral treatment. Find relative change.

**Relation.** `relative change=(new−old)/old×100`. Evaluate the supplied hypothetical quantities in consistent units. The calculated value is **20 %**. Reconstruct the arithmetic independently and specify whether it estimates a flux, concentration, coefficient or fraction. A correct numerical answer without units and domain assumptions is incomplete.

**Interpretation.** Spectral responses can alter shape rather than net carbon gain. **Model boundary.** Replicate variation and total light integral are omitted. This is a synthetic calculation, not a measured field value. Replace one positive input with a value 20% greater, recompute, and ask whether an intact plant could instead respond through feedback that changes other inputs. When a model assumes constant conditions, a measurement during a rapid transient can deviate even if the mechanism is scientifically reasonable.

### Test your explanation

Propose a control for the measurement described above. Explain how plant age or environment could change the predicted response, and identify a result that would falsify your favored mechanism. Distinguish a directly measured quantity from one inferred through the equation.


## Topic 6.5 — Gravitropism, mechanosensing and growth rhythms

### Mechanistic explanation

Roots and shoots can detect reorientation relative to gravity through specialized perception and signaling pathways, leading to differential growth. Mechanical stimuli such as touch, wind and bending also influence wall properties and development. Circadian timing can regulate growth and responsiveness even when external conditions appear constant.

### Coupled constraints and functional trade-offs

A vertically growing stem is not solely a product of gravitropism: light direction, contact and intrinsic growth patterns interact. Repeated shaking may reduce extension yet increase support investment, complicating a simple growth-rate comparison. A delayed response after rotating an organ can reflect signaling and tissue-growth time constants.

### How evidence would be collected

Rotate a standardized set of seedlings under nondirectional or controlled directional light and record curvature every few minutes. Compare intact specimens with age-matched controls and document handling contact. If rhythms are suspected, repeat the same protocol at several circadian phases.

### Scope, assumptions and what must not be inferred

Curvature is a geometric output, not direct proof of the gravity-sensing molecule. A proposed intermediate should be assayed or genetically tested separately.

### Diagnostic distinction

In **gravitropism, mechanosensing and growth rhythms**, the central distinction is **temporal and tissue context**. Specify the treatment, one tissue-level mediator, and a direct measurement that could distinguish the proposed mechanism from an alternative involving **hormone concentration versus sensitivity**. A time course and appropriate control are stronger evidence than a single endpoint.

### Worked quantitative case 6.5

**Question.** Curvature is 9° at 20 min and 33° at 80 min after reorientation. Estimate mean angular rate across interval.

**Relation.** `rate=Δangle/Δtime`. Evaluate the supplied hypothetical quantities in consistent units. The calculated value is **0.4 degrees min−1**. Reconstruct the arithmetic independently and specify whether it estimates a flux, concentration, coefficient or fraction. A correct numerical answer without units and domain assumptions is incomplete.

**Interpretation.** A time-resolved phenotype helps identify lag and sensitivity. **Model boundary.** A mean does not reveal transient peaks or circadian effects. This is a synthetic calculation, not a measured field value. Replace one positive input with a value 20% greater, recompute, and ask whether an intact plant could instead respond through feedback that changes other inputs. When a model assumes constant conditions, a measurement during a rapid transient can deviate even if the mechanism is scientifically reasonable.

### Test your explanation

Propose a control for the measurement described above. Explain how plant age or environment could change the predicted response, and identify a result that would falsify your favored mechanism. Distinguish a directly measured quantity from one inferred through the equation.


## Integrative investigation — Testing directional growth and signaling timing

### Biological puzzle and mechanistic alternatives

**Primary question:** Does curvature begin after asymmetrical cell elongation and auxin-response reporter redistribution? Different physiological mechanisms can produce the same apparent trend in a leaf measurement or growth endpoint. The role of a good experiment is to make those explanations diverge under an observation that can actually be collected. The case below is **hypothetical**: none of the tabulated values come from published research, field trials or experiments performed for this book. They exist only to exercise design, plotting, arithmetic and interpretation.

Two competing accounts are: **Hypothesis A:** Perception changes auxin-related signaling before unequal expansion. **Hypothesis B:** Directional bending can be explained by a rapid mechanical effect without signaling delay. Neither is assumed correct merely because it sounds familiar. Before collecting data, specify which mediator each requires, where the mediator would change and what difference in timing or environmental dependence would distinguish them. If both hypotheses make the same prediction for the primary outcome, adding sample size will not solve the identification problem; a better intervention or second observable is needed.

### Proposed experimental design

Expose matched seedlings to unilateral blue light; image both flanks every ten minutes and compare control, photoreceptor-impaired and complemented backgrounds. Choose independent plants or plots as biological replicates, rather than treating multiple leaves from one plant as fully independent individuals. Randomize positions within the available growth space and rotate placements only if rotation itself will not change the intended light treatment. Document watering, temperature, developmental stage and the time of sampling, because plant physiology exhibits strong diel and developmental variation. Repeat technical instrument readings to estimate precision but analyze them as nested observations within a plant where appropriate.

**Most concerning confound:** Changing light geometry can alter temperature and growth rate; imaging light may activate the receptor. A rigorous design should either hold this variable stable, measure it independently or include it as an explicit factor. Predeclare the primary endpoint and sample interval. Add a negative control for the manipulation, an untreated baseline and a positive control when one can be implemented safely and ethically. Technical success means the planned exposure and measurement occurred; it does not automatically mean the biological hypothesis was supported.

### Synthetic data to analyze

Axes: **Minutes after illumination** and **Curvature (degrees)**. For clarity the table uses serial index values 0–4, corresponding to five ordered levels or time points selected for this teaching example. Values are illustrative and carry no real-world standard errors. Treatment A and B are not empirical groups.

| Minutes after illumination (index) | Treatment A | Treatment B |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 2 | 0 |
| 2 | 7 | 2 |
| 3 | 15 | 5 |
| 4 | 25 | 9 |

The endpoint change for series A is **25** in the stated outcome scale, and for series B is **9**. Because we have no independent replication, there is no valid standard error, confidence interval, statistical test or effect-size claim about a population. Plot both series on shared axes, explain what is and is not comparable, and reconstruct one contrast by hand. A difference between these five-number curves is a mathematical observation about **constructed numbers**, not evidence for either biological hypothesis.

### Interpretation, checks and follow-up

Temporal precedence is necessary but not sufficient evidence; a genetic perturbation plus rescue adds a more discriminating causal test. Compare patterns in at least three ways: absolute change, proportional change against the initial state, and the shape of the progression. Determine whether a lag, plateau or recovery segment is present. Ask what unmeasured variable could generate a similar pattern and what instrumentation would make it observable. Where the data describe a concentration or a fraction, do not call its slope a transport flux until a volume, area, residence time or mass-balance assumption has been supplied.

For an undergraduate replication assignment, prepare an analysis plan with a clear naming convention for raw measurements and calibration records. Preserve negative readings, missing samples and handling deviations rather than silently dropping them. Create a version-controlled script or spreadsheet with equations, units and plots, and keep an untouched raw-data copy. Estimate power and replication requirements only when realistic preliminary variance estimates exist; this table provides none. A scientifically useful final report should give the causal reasoning, the alternative mechanism, and limitations with the same prominence as the resulting graph.

### Five decisions for the lab notebook

1. Define the independent sampling unit and explain why extra sensor readings cannot substitute for new plants or plots.
2. Select a measurable process variable from **hormone concentration versus sensitivity** and explain why it is more mechanistic than the visual appearance of an organ.
3. Identify which part of **Changing light geometry can alter temperature and growth rate; imaging light may activate the receptor.** can be standardized and which requires measurement as a covariate.
4. Describe the plot and model comparison that would genuinely differentiate the two stated hypotheses under a larger, replicated dataset.
5. Write a cautious conclusion that states exactly what would be learned if the new experiment agrees with series A, or if instead it agrees with series B. Never call the synthetic sequence published evidence.


## Unit-level synthesis: following a cause through the entire plant

Physiological accounts become more reliable when processes are linked without silently changing scale. In this unit the chain spans **Auxin gradients and directional growth**, **Abscisic acid and water-stress responses**, **Gibberellins, cytokinins, ethylene and crosstalk**, **Phytochrome, cryptochrome and shade signaling**, and **Gravitropism, mechanosensing and growth rhythms**. These five labels identify related mechanisms, but they do not establish which one limits performance in any particular specimen. Draw them as an interacting network rather than a rigid left-to-right progression. A local cellular process can determine a whole-plant response only if material transport, signaling or mechanical continuity connects the two. Conversely, a change in an organ’s environment can alter cellular behavior through feedback, even if the molecular machinery itself is unchanged.

Consider a thought experiment with two healthy plants that show equal final biomass after a seven-day treatment. The first maintained relatively stable daily assimilation but spent more carbon on defense or repair; the second experienced a severe early decline followed by compensatory growth. Their identical endpoint conceals opposite physiological trajectories and potentially different resource reserves. Sampling only the last day cannot distinguish them. For the five topics above, choose one early mediator and one later integrative variable whose trajectories would separate these alternatives. Include time and physical units in the predictions. Do not equate relative rate with absolute amount: a small organ can have a high rate per area but a small total flux.

Now change the experimental setting from a controlled growth cabinet to a variable outdoor canopy. Differences in illumination, boundary-layer conductance, root-zone moisture, developmental stage and nutrient supply arise over centimeters and hours. A fitted response in a single leaf may therefore be unsuitable for prediction of plant performance under the field regime. A better transferable model makes the limiting assumptions visible, specifies the range of conditions it is calibrated for and tests whether the relation survives at least one new condition. The chapter's simplified equations are tools for understanding direction and scale, not calibrated growth-management systems.

Finally create a mass and energy ledger. Identify water, carbon, mineral ions, ATP or reductant relevant to this unit. For each, record where it is supplied, where it is transformed, where it is stored and where it leaves the defined plant compartment. A balance that does not close should prompt a search for a missing flow or measurement error; it should not be forced to close by arbitrarily changing a measured term. Ask a partner to challenge one causal link and one numerical assumption. The strongest answer will describe what data could prove your account incomplete.

### End-of-unit oral defense

Explain a plausible experiment in which **auxin gradients and directional growth** changes before **gravitropism, mechanosensing and growth rhythms**; then propose a second experiment in which the apparent order reverses because another condition becomes limiting. Explain what result would distinguish a direct mechanism from a feedback effect. Choose one of the worked calculations, double-check its dimensions and identify whether it estimates a state variable, a rate, a fraction or a phenomenological coefficient. Use at least two possible mechanisms for a common symptom such as slow growth, lower gas exchange or color change; give one measurement that discriminates them. End by stating a meaningful boundary to the generalization: species, tissue age, temperature range, developmental phase or assay method.



## Unit reference navigation

The reference list at the reader index provides textbook and review starting points. Review each primary claim against the original literature before presenting this manuscript as an accredited or peer-reviewed textbook. Next unit: Reproductive physiology and senescence.
