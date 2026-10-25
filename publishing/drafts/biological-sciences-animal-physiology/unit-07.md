# Unit 07 — Hormones, reproduction and immune coordination

> **Animal Physiology — OpenSTEM Book 11.** Long-range communication and defense as parts of an integrated physiological control system. All numerical case values in this book are **synthetic teaching data**, not measurements, clinical advice or husbandry recommendations. This editorial draft has not received independent peer review.

## What the unit asks you to explain

Physiology is a quantitative study of how living structures accomplish work and keep conditions within tolerable ranges. This unit examines hormones, reproduction and immune coordination while connecting molecular mechanisms to whole-organism outcomes. The goal is not only to identify a named structure or pathway, but to predict the direction of change, the time needed for a response, and the observation that would distinguish a proposed mechanism from an alternative. Learners should keep conservation of matter or energy in view whenever they write an equation.

By the end of this unit, you should be able to (i) explain its five linked topics in physical and biological terms; (ii) calculate and interpret five dimensioned toy examples; (iii) decide which measurements distinguish input, state and output; (iv) identify failure modes of the models; and (v) design an ethical comparison while naming confounding factors. Prerequisites are first-year biology, elementary chemistry, algebra, and an ability to read plots. Differential equations are discussed conceptually where useful but are not assumed.


## Working distinctions

signal secretion versus tissue sensitivity; pulsatile hormones and delays; allocation to reproduction; immune cost and specificity; organ-system integration. A useful unit-wide habit is to separate direct measurements from inferred flows, clearly stating physical units and time windows.


## Integrated systems lens — Hormones coordinate competing goals across timescales

Endocrine systems link distant tissues through circulating signals, but concentrations alone rarely specify downstream function. A receptor can be abundant and insensitive, or scarce and strongly coupled; a tissue may degrade hormone locally. Negative feedback can maintain an output even while secretion of an upstream hormone changes substantially. Therefore measuring an endocrine axis requires time points, relevant receptor states and a definition of the target physiological output.

Hormones occur in pulses and rhythms because feedback networks contain delays, thresholds and interacting oscillators. A sample every few hours may completely miss pulses lasting minutes. Conversely very frequent sampling may disturb an animal and change the secretion profile that investigators hope to measure. Noninvasive matrices, automated sampling where justified and a priori temporal models can improve inference while reducing burden.

Stress responses combine fast autonomic adjustments with slower endocrine and metabolic effects. A short sympathetic redistribution can help deliver oxygen to active tissues, while glucocorticoids influence longer-scale fuel handling and behavior. These pathways also contribute to ordinary daily homeostasis. A high level relative to a chosen reference could reflect time of day, activity, handling or a natural reproductive stage rather than a single pathological condition.

Reproductive investment brings resource allocation into physiology. Producing gametes, incubating offspring or secreting milk can require materials and energy that are unavailable for other functions. However trade-offs are conditional, not arithmetic guarantees. An individual with high nutrient intake may sustain immune and reproductive outputs together, while another facing scarcity cannot. Observational studies should model common causes such as age, food, temperature and season before attributing one outcome to another.

Innate immune reactions may generate fever by shifting thermoregulatory control and by changing metabolic demands. Fever differs conceptually from heatstroke or simple environmental heating because its origin includes a change in regulated target. Despite this conceptual distinction, both high temperature states can affect water balance and tissue metabolism. Classroom models should avoid suggesting specific treatment decisions for people or animals.

A rigorous comparative endocrine study pre-registers the primary outcome when appropriate, measures baseline variation and recognizes species-specific biology. For example reproductive cycles of birds, mammals, amphibians and invertebrates do not share every anatomical or endocrine step. A common framework of signaling, targets, feedback and resource allocation is valuable precisely because it allows differences rather than erasing them.

## Five linked physiological topics

### 7.1 — Hormone signaling, receptors and feedback axes

#### Biological mechanism and scope

Endocrine cells release signals into body fluids, often operating with neural control. A hormone affects cells expressing suitable receptors, and the outcome depends on receptor abundance, intracellular coupling and prior exposure. Peptide and steroid hormones differ in common transport and receptor mechanisms, but both exhibit feedback, metabolism and tissue-specific action.

#### Comparisons, exceptions and organism-level interpretation

Circulating hormone concentration reflects secretion and clearance, not necessarily target-tissue activity. Pulses can carry information different from a constant average concentration; downregulation can change sensitivity during sustained exposure. Negative feedback along a hormone axis stabilizes outputs yet also creates oscillations when delays and amplification are large.

#### Observation, experiment and causal alternatives

Sample a fictional hormone profile at frequent intervals to show why one blood measurement can miss pulsatility. In real research, align sampling with circadian phase, handling stress and assay cross-reactivity. A correlation between plasma hormone and behavior does not identify the direction of causation.

#### Appropriate limits of the model

Endocrine diagrams indicate plausible directions of influence but must be tested with receptor perturbation and tissue measurements before asserting a mechanism.


#### Mechanism-to-evidence test

A reported change in **hormone signaling, receptors and feedback axes** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 31 — estimate, interpret, challenge

**Problem:** In a hypothetical first-order clearance model, hormone concentration is initially 80 pg/mL and the half-life is 30 min. With secretion switched off, calculate concentration after 90 min.

**Method:** `initial concentration × 2^(−time/half-life)`. Substituting the given teaching values yields **10 pg/mL**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Three half-lives reduce a pure exponentially decaying concentration to one eighth. **Limits:** Real hormone signals may continue to be secreted and distributed between compartments. These are synthetic numbers, not measured organism values.


### 7.2 — Stress responses and glucocorticoid physiology

#### Biological mechanism and scope

A threatening or energetically demanding event recruits neural, endocrine and behavioral processes. Sympathetic activation can redistribute circulation rapidly, while glucocorticoid signaling changes metabolism and gene expression on multiple timescales. These responses are context dependent: transient mobilization of fuel can be adaptive, whereas prolonged elevation may impose costs.

#### Comparisons, exceptions and organism-level interpretation

An animal's apparent stress level cannot be read from one hormone concentration in isolation. Sampling itself can alter the measurement, hormone receptors differ between tissues, and normal daily variation may exceed a modest experimental response. Stress mediators also support routine physiology, so treating them as purely harmful is misleading.

#### Observation, experiment and causal alternatives

Compare a standardized challenge with carefully time-matched controls and noninvasive behavioral observations. Measure both the initial response and recovery, while reducing unnecessary handling. If a treated animal shows lower circulating glucocorticoid, ask whether it reflects reduced secretion, greater clearance or altered feedback.

#### Appropriate limits of the model

The ethically appropriate goal is to study mechanisms while minimizing animal burden, not to maximize a stress response.


#### Mechanism-to-evidence test

A reported change in **stress responses and glucocorticoid physiology** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 32 — estimate, interpret, challenge

**Problem:** A fictitious glucocorticoid time series at minutes 0,20,40,60 has concentrations 10,30,50,20 units. Approximate total area under concentration–time curve by trapezoids.

**Method:** `sum over intervals of (C1+C2)/2 × time step`. Substituting the given teaching values yields **1900 unit·min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Area accounts for both concentration and time and should be compared only across matching windows. **Limits:** Baseline-subtracted exposure would differ; assay units and interpolation assumptions must be reported. These are synthetic numbers, not measured organism values.


### 7.3 — Reproductive endocrine cycles and gamete production

#### Biological mechanism and scope

Animal reproductive function depends on environmental cues, nutritional status and internal endocrine rhythms. Hypothalamic and pituitary signals influence gonadal steroid production and gametogenesis in many vertebrates, but cycle patterns differ widely among taxa. Spermatogenesis and oogenesis require coordinated cellular development and support from surrounding tissues.

#### Comparisons, exceptions and organism-level interpretation

An ovulatory cycle, estrous cycle and seasonal breeding schedule are not interchangeable. Photoperiod, temperature and social environment can modify reproductive timing, especially in seasonal species. Hormone concentrations may rise before a reproductive event rather than being caused by it; temporal ordering must be established from repeated samples.

#### Observation, experiment and causal alternatives

Use a time-series visualization of fictional gonadal hormone pulses with stated sampling resolution. In a comparative study, define reproductive stage independently of the hormone being tested to avoid circular classification. Interpret null results with attention to delayed responses and individual variation.

#### Appropriate limits of the model

Endocrine control integrates timing and resources, and different species should not be forced into the template of a single mammalian menstrual cycle.


#### Mechanism-to-evidence test

A reported change in **reproductive endocrine cycles and gamete production** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 33 — estimate, interpret, challenge

**Problem:** A simulated reproductive hormone trace contains 8 secretory pulses during a 4-hour window. Calculate observed pulse frequency.

**Method:** `pulse count / observation duration`. Substituting the given teaching values yields **2 pulses/hour**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A longer observation period helps distinguish regular oscillation from random event clustering. **Limits:** Pulse identification requires a stated detection threshold and sufficiently frequent sampling. These are synthetic numbers, not measured organism values.


### 7.4 — Pregnancy, development and maternal resource allocation

#### Biological mechanism and scope

In internally developing vertebrates, maternal physiology may be altered to support growth and exchange with offspring. Gas and nutrient transfer depends on membrane architecture, blood flow, gradients and metabolic demand. Different reproductive strategies—including egg laying, placentation and live birth without mammalian placentation—solve similar delivery problems using distinct structures.

#### Comparisons, exceptions and organism-level interpretation

A high maternal metabolic rate is not equivalent to a known fetal nutrient supply. Tissue allocation, transfer efficiency and heat dissipation matter. In lactating mammals, secretion of milk requires substrate delivery, epithelial transport, endocrine signaling and behavioral coordination; production changes with offspring demand and maternal diet.

#### Observation, experiment and causal alternatives

Build a fictional daily energy budget separating maternal maintenance, gestational tissue growth and export to offspring. State whether figures refer to ingested energy or assimilated energy. Compare strategies without assigning moral or evolutionary superiority to a particular reproductive mode.

#### Appropriate limits of the model

Physiological trade-offs are conditional on ecology and life history, not immutable predictions for individuals.


#### Mechanism-to-evidence test

A reported change in **pregnancy, development and maternal resource allocation** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 34 — estimate, interpret, challenge

**Problem:** A fictional maternal budget allocates an additional 2.5 MJ each day for 12 days to tissue growth and offspring support. Estimate cumulative additional energy.

**Method:** `extra energy per day × duration`. Substituting the given teaching values yields **30 MJ**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Cumulative demand is not necessarily equal to additional ingested energy if stored fuels contribute. **Limits:** Rates and duration are artificial; this is not gestation or lactation guidance for any species. These are synthetic numbers, not measured organism values.


### 7.5 — Innate defense, inflammation and fever

#### Biological mechanism and scope

Physical barriers and innate immune sensing detect damage and conserved microbial features. Local mediators can alter blood flow, vascular permeability, leukocyte recruitment and behavior. Adaptive immune memory adds specificity in vertebrate groups with the corresponding cellular machinery. These responses interact with temperature, metabolism and endocrine stress systems.

#### Comparisons, exceptions and organism-level interpretation

Inflammation is protective in some settings and injurious in others; its outcome depends on timing, location and control. Fever is a regulated increase in temperature target mediated by signaling pathways, distinct from uncontrolled overheating. Defense carries an energetic cost and can compete with growth or reproduction when resources are limited.

#### Observation, experiment and causal alternatives

Track temperature, food intake, activity and selected immune markers around a benign, ethically approved observational event. Without controls, a temperature increase could be attributed incorrectly to exercise, ambient warmth or inflammation. An immune marker in blood may not represent local tissue protection.

#### Appropriate limits of the model

A simulation of fever illustrates feedback logic and does not determine when medical intervention is appropriate.


#### Mechanism-to-evidence test

A reported change in **innate defense, inflammation and fever** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 35 — estimate, interpret, challenge

**Problem:** A hypothetical regulated body temperature rises by 1.3°C over 40 min during a modeled fever-onset phase. Calculate average rate of change.

**Method:** `temperature difference / time`. Substituting the given teaching values yields **0.0325 °C/min**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A slope describes a measured response but not its causal trigger. **Limits:** Temperature can change nonlinearly and depends on the recording site and ambient environment. These are synthetic numbers, not measured organism values.


## Integrative investigation — Breeding season, infection and resource conflict

**Setting.** A seasonal breeder approaches reproductive activity while food availability is variable and pathogen exposure changes with migration. Endocrine signaling coordinates reproductive tissues with environmental cues, while immune activation can raise metabolic demands and alter behavior. Observing fewer breeding attempts after infection does not prove a hormone directly suppresses reproduction.

**Design.** Design a field study using noninvasive repeated observations and independently validated indicators of reproductive stage. Record food supply, ambient temperature and body condition as possible shared causes. Avoid experimental infection as an educational exercise; the scientific logic can be explored with archived datasets or observational comparisons.

**Evidence and alternatives.** Hormone dynamics are pulsatile, so a single sample may place individuals in different apparent categories merely because it catches different phases. Immune markers reflect different layers of defense, and the relevant outcome may be local tissue condition rather than a blood concentration.

**Interpretation and transfer.** Develop a directed causal graph with photoperiod, energetic condition, stress mediator, immune activity and reproductive output. Identify two plausible confounding paths and one measurement that would help distinguish each. Explain why evidence for a trade-off in a population need not establish a deterministic response in every individual. Integrative physiology asks how competing priorities are coordinated, not whether one body system is always more important than another.

**Reproducibility checklist.** Declare the independent biological replicate and the direct measurement. Preselect a primary outcome, control environmental changes, and calibrate instruments. Preserve original data and computation steps rather than reporting rounded results alone. Compare the specific competing predictions before interpreting statistical significance. Respect animal welfare by using approved, appropriately noninvasive or existing datasets for educational comparisons.


## Retrieval practice — explain rather than memorize

1. For **Hormone signaling, receptors and feedback axes**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

2. For **Stress responses and glucocorticoid physiology**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

3. For **Reproductive endocrine cycles and gamete production**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

4. For **Pregnancy, development and maternal resource allocation**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

5. For **Innate defense, inflammation and fever**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

**Self-check:** A defensible answer distinguishes direct observation from inference, names a unit or timescale, and explains at least one way its proposed explanation could be wrong. Recalculate all five worked cases without reading the answers.

## Working glossary and distinctions

The entries below state operational differences that matter when planning an experiment. Learn each term through a concrete measurement rather than memorizing a label in isolation.


**Endocrine signaling.** Communication through released molecules carried in body fluids to responsive target tissues with suitable receptors.


**Hormone clearance.** Processes removing or transforming a circulating hormone, influencing measured concentration independently of secretion.


**Pulse frequency.** Number of detectable secretory events per time under a stated sampling and event-detection method.


**Receptor downregulation.** Reduced receptor availability or signaling responsiveness after certain exposure histories, changing tissue sensitivity.


**Hypothalamic–pituitary axis.** A layered regulatory network coordinating neural cues, endocrine secretion and peripheral target-organ feedback.


**Glucocorticoid.** A class of steroid signals affecting metabolism, immune activity and stress-related adaptation, with normal physiological roles.


**Catecholamine.** A chemical messenger class including epinephrine and norepinephrine with important autonomic and endocrine functions.


**Photoperiodism.** Use of day-length information as a seasonal timing cue for physiological events such as reproduction.


**Gametogenesis.** Formation of reproductive cells with coordinated meiotic and developmental processes.


**Maternal allocation.** Energy and nutrient resources directed to parental maintenance versus offspring support over a defined reproductive interval.


**Lactation.** Milk production and secretion in mammals, involving gland differentiation, substrate supply and neuroendocrine control.


**Innate immunity.** Protective functions involving barriers, pattern sensing and rapid cellular or molecular responses.


**Adaptive immunity.** Specific, memory-capable immune responses mediated by antigen-responsive lymphocytes in organisms with such machinery.


**Inflammation.** Coordinated tissue response to infection or injury that can protect and repair but may also cause damage.


**Fever.** Regulated change in temperature target during an immune response, distinct from passive temperature increase due to heat exposure.


## Unit 7 synthesis

Return to the five worked numerical cases and ask what controls each result, which changes are compensatory rather than primary, and how the model would fail when another organ system changes. Connect signal secretion versus tissue sensitivity with immune cost and specificity and state a falsifiable prediction across the two levels of organization.
