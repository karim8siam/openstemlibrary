# Unit 05 — Transmission, ecological setting and population dynamics

> **OpenSTEM Book 14, Virology.** Undergraduate editorial draft. Every numerical example and modeled curve uses fictional input. Expert review and publication approval pending. Do not treat these pages as laboratory protocols, clinical tools or instructions for manipulating viruses.

## Learning objectives

Population spread emerges from relationships among contacts, susceptibility, duration and environment. Reproduction numbers and inferred networks are statistical summaries, not immutable genetic traits. Ecological conclusions require denominators, spatial context and careful handling of biases and privacy.

The five conceptual themes are **contact networks; model assumptions; timing and delay; ecological confounding; missing data**. A reader completing this unit should be able to explain each of its five topics, compare at least two rival causes of a given observation, reproduce five quantitative answers, and critique a synthetic research design. Scientific maturity requires distinguishing the scale at which a fact has been measured from the scale at which an explanation is being proposed. If an observation describes nucleic-acid fragments, do not call it an infection count. If an outcome describes an immune-related marker, do not call it proven protection without validation.

## Foundations for evidence-based reasoning

Virology spans structural, cellular, ecological and clinical observations. A claim supported at one level may be unjustified at another. Check whether a measured signal is a proxy, a rate or a true outcome. Sampling time, location, group composition and denominators can change interpretation even when the plotted shape looks identical.

This unit uses models as tools for exploring assumptions. One parameter may be an arbitrary scale, while another represents a mathematical saturation point. Neither value should be mistaken for a calibrated property of a real virus. When interacting with a chart, first predict a direction, then alter one control, then explain the change in terms of the formula. Repeat with the second control and look for a limiting case. Observe how even a simple model can be illuminating for reasoning yet unsuitable for operational decisions. Reading the explicit warnings attached to each model is part of the exercise.

## Responsible research boundary

The descriptions are conceptual and pedagogical. No experiments requiring access to infectious material, clinical specimens, animals or specialized biosecurity facilities are needed or permitted by the lesson plan. Real research requires institution-specific ethical review, biosafety training and oversight. The synthetic case studies are not data collected from people, hospitals, laboratories or the environment. For work with real published material, cite the original source, verify context and licensing, and avoid reproducing identifiable records. Health, agricultural and public safety decisions should follow qualified professional guidance, not simplified student exercises.

## Topic 5.1 — Contact structure and chains of transmission

### Mechanism and explanatory scope

Transmission can be analyzed as a network of opportunities for exposure rather than as a property of a viral genome alone. Frequency and type of contact, infectious period, environmental conditions and susceptibility together shape population-level spread. The observed network is usually an imperfect sample of the underlying social or ecological system.

For **contact networks**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A cluster of temporally close infections does not demonstrate a direct edge between every case. Shared environments and unobserved contacts create alternative paths, and changes in testing behavior can alter apparent clusters.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **environmental transmission, seasonality and context** and state one observation that would differentiate the explanations.

### Measurement and controls

Analyze a small synthetic contact graph using only labeled nodes and edges. Compare a dense subnetwork with a sparse one, and discuss what additional timing evidence would be needed for transmission inference.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Graph edges are educational abstractions rather than accusations or identification of real transmission sources. Personal contact data must be protected.

Connect the topic to **basic and effective reproduction numbers** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 5.1

**Question.** A toy contact rate is 4 contacts/time, transmission probability 0.1/contact and infectious duration 3 time units. What simple expected count results?

**Invented inputs:** `c=4`, `p=0.1`, `d=3`. **Assumed relation:** `c*p*d`. **Answer:** **1.2 expected contacts-to-cases**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **contact structure and chains of transmission** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **basic and effective reproduction numbers** while identifying one uncertain link.

## Topic 5.2 — Basic and effective reproduction numbers

### Mechanism and explanatory scope

The basic reproduction number R0 is a theoretical average of secondary infections in a fully susceptible population without interventions; the effective reproduction number Rt describes transmission in a particular time-dependent context. Both depend on model assumptions and uncertainty, and neither equals individual contagiousness.

For **model assumptions**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A reported Rt below one can be unstable under sparse data or changing ascertainment. Differences among settings should not be treated as intrinsic constants of a virus because behavior, susceptibility and mitigation shape transmission.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **contact structure and chains of transmission** and state one observation that would differentiate the explanations.

### Measurement and controls

Compute simple next-generation expectations from toy contact and transmission probabilities. Contrast an elementary relation Rt approximately equals R0 times susceptible fraction with a scenario where changing contact patterns invalidates the simplification.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

These models provide no real-time forecast or local intervention recommendation. Public-health modeling requires actual surveillance data and qualified interpretation.

Connect the topic to **incubation, infectiousness and observed case timing** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 5.2

**Question.** Using idealized R0=2.8 and susceptible fraction 0.5, what is Rt?

**Invented inputs:** `R0=2.8`, `s=0.5`. **Assumed relation:** `R0*s`. **Answer:** **1.4 expected secondary cases**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **basic and effective reproduction numbers** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **incubation, infectiousness and observed case timing** while identifying one uncertain link.

## Topic 5.3 — Incubation, infectiousness and observed case timing

### Mechanism and explanatory scope

Incubation period, latent period in epidemiological models, generation interval and serial interval are related but different. Symptom onset may occur after, before or not at all relative to periods of infectiousness. Surveillance observations combine biological timing with healthcare-seeking behavior and test reporting delays.

For **timing and delay**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Using symptom onset as a proxy for infection time introduces uncertainty. A test date is a reporting event rather than an exact exposure date, and missing asymptomatic cases distort inferred interval distributions.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **basic and effective reproduction numbers** and state one observation that would differentiate the explanations.

### Measurement and controls

Compare two imaginary symptom timelines and compute intervals only where their endpoints are defined. Use a timeline diagram to label exposure, infectious period, symptom onset, sampling and report date separately.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Avoid making pathogen-specific claims about contagious periods from these toy timelines. Definitions and estimators must match the biological question.

Connect the topic to **reservoirs, vectors and one health interfaces** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 5.3

**Question.** An invented serial interval has onset times 5 and 9 days. What is the difference?

**Invented inputs:** `a=5`, `b=9`. **Assumed relation:** `b-a`. **Answer:** **4 days**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **incubation, infectiousness and observed case timing** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **reservoirs, vectors and one health interfaces** while identifying one uncertain link.

## Topic 5.4 — Reservoirs, vectors and One Health interfaces

### Mechanism and explanatory scope

Some viral transmission systems involve long-term ecological hosts, intermediate environments, arthropod vectors, or multiple host species. One Health considers interactions between human, animal and environmental conditions. A reservoir is an ecological persistence concept, not simply any animal in which viral RNA was detected.

For **ecological confounding**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A wildlife-positive molecular assay can reflect exposure, contamination or transient infection without demonstrating a maintenance reservoir. Host density, seasonality, land use and surveillance effort confound observed patterns.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **incubation, infectiousness and observed case timing** and state one observation that would differentiate the explanations.

### Measurement and controls

Assess a hypothetical regional dataset containing habitat type, sampling effort and positive observations. Standardize detections by samples collected and list additional evidence required for reservoir or vector competence claims.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

This material avoids field capture and virus isolation instructions. Ethical ecological inference requires permits, animal welfare and appropriate public-health infrastructure.

Connect the topic to **environmental transmission, seasonality and context** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 5.4

**Question.** A survey observes 36 positives in 240 samples. What is the observed sampling proportion?

**Invented inputs:** `p=36`, `n=240`. **Assumed relation:** `p/n`. **Answer:** **0.15 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **reservoirs, vectors and one health interfaces** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **environmental transmission, seasonality and context** while identifying one uncertain link.

## Topic 5.5 — Environmental transmission, seasonality and context

### Mechanism and explanatory scope

Environmental persistence and transport can influence exposure via surfaces, droplets, aerosols, water or other routes depending on the virus and setting. Seasonality arises from interactions among behavior, climate, vector ecology and susceptibility, often with strong uncertainty.

For **missing data**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Discovering genetic fragments in environmental samples is not sufficient to prove a viable exposure route. It is easy to confuse detection with infectious risk, especially when data lack sampling denominators or control for environmental degradation.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **reservoirs, vectors and one health interfaces** and state one observation that would differentiate the explanations.

### Measurement and controls

Construct a synthetic seasonality chart with simulated sampling effort. Compare raw counts and sampling-adjusted rates, then specify what mechanistic evidence would differentiate environmental survival from seasonal behavior.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Do not convert abstract environmental detection examples into operational claims about specific sites or disinfection regimens. Context-specific authoritative guidance is required for practice.

Connect the topic to **contact structure and chains of transmission** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 5.5

**Question.** A seasonality example records 90 observations after 300 samples. What percent of samples were positive?

**Invented inputs:** `k=90`, `n=300`. **Assumed relation:** `100*k/n`. **Answer:** **30 %**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **environmental transmission, seasonality and context** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **contact structure and chains of transmission** while identifying one uncertain link.

## Integrated synthetic research investigation: Two contact graphs with identical case totals

### Scientific question and competing models

This investigation tests how much can be inferred from limited numerical evidence. The first explanation is that **more network links cause more transmission opportunities**. The rival explanation is that **altered case ascertainment produces an apparently denser graph**. Each is formulated to account for a possible upward trend without supplying any actual biological or epidemiological measurements. The goal is not to make the plots resemble authentic virus experiments; it is to learn why similar-looking data can support different causal stories and how a discriminating observation improves a research plan.

The comparison must keep the outcome definition constant. Make a causal diagram with source, intermediate step, observed proxy and background variables. Place an unmeasured factor near the arrow it might influence, rather than listing confounders without indicating their pathway. A credible alternative explanation must be capable of producing a plausible observed difference. State what information would be required to refute each explanation rather than merely to generate an additional matching curve.

### Data and transparent assumptions

| Stage | Series A (synthetic index) | Series B (synthetic index) |
|--:|--:|--:|
| 0 | 15.62 | 16.90 |
| 1 | 19.46 | 19.07 |
| 2 | 23.95 | 21.36 |
| 3 | 28.92 | 23.73 |
| 4 | 34.27 | 26.16 |
| 5 | 39.96 | 28.64 |

These are **fabricated dimensionless teaching indices**, not real assay outputs, infection counts, cases, experimental animals or clinical data. No uncertainty bands are supplied because there are no biological replicates. The table does not support p-values, confidence intervals or causal claims. Between stage zero and stage five, series A changes from **15.62** to **39.96**; the difference is **24.34 index units**. Series B changes from **16.9** to **28.64**, a difference of **11.74 index units**. These arithmetic descriptions are valid within the constructed table only.

A simple endpoint ratio, B over A, equals **0.717** if they are defined on comparable scales. A different normalization might change that ratio dramatically without changing the underlying plotted order. Plot both series with the invented stage index on the horizontal axis. It is incorrect to label the index in hours or days because the exercise deliberately supplies no physical time units. Try plotting the percent change from baseline instead, and explain why percent changes can exaggerate differences when the baseline is small.

### Study design without pathogen experimentation

The most important planned independent measurement is: **measure reporting fraction independently**. The leading confound is **unobserved edges**. State how the independent measurement would behave under the two hypotheses and whether the proposed design could still produce the same answer under different mechanisms. Use only synthetic data, publicly documented nonidentifiable aggregate reports and pencil-and-paper reasoning. No live virus, infectious specimen, virus propagation, sequence engineering or physical containment procedure is authorized or required for this educational investigation.

Distinguish technical repeats, independent samples and randomized comparisons. An assay readout can be perfectly repeatable while its causal interpretation remains incorrect. Record denominator, missing observations and any change to the definition of a positive result.

### Interpretation and competing-cause exercise

Evaluate the constructed series using three levels of claims. At the first level, directly report its numerical values. At the second, describe a statistical pattern such as monotonic rise, relative difference or saturation. At the third, discuss whether a particular biological mechanism is responsible, and explicitly state that the invented data cannot decide. A fourth level, practical intervention or policy, needs real outcomes and specialist scrutiny and cannot follow from these pages.

The strongest scientific answer may be that the present design is underdetermined: more than one account fits the observations. When the two rival hypotheses make identical predictions for the chosen outcome, collecting more of the same outcome alone may not resolve the ambiguity. Change the type of observation or the comparison structure. Write a paragraph describing a result that would contradict hypothesis one but be expected under hypothesis two, while refusing to treat the imagined result as if it actually occurred.

### Six-part assignment and grading guide

1. Write a one-sentence research question with a specified outcome and observation window (2 points).
2. Draw a causal diagram with the two competing mechanisms and at least one confound (3 points).
3. Calculate absolute and proportional changes from the synthetic table with correct labels (3 points).
4. Explain how changing the sampling denominator could reverse a simplistic conclusion (3 points).
5. Specify a safer, nonexperimental, computational distinction between the hypotheses (4 points).
6. Write a short reproducibility statement with data provenance, invented status and three limitations (5 points).

Strong submissions separate calculation from explanation, use defensible language, and do not imply that a toy model proves a statement about an actual virus, patient, ecosystem or intervention. Weak submissions introduce unsupported numerical assumptions, hide their denominators or mistake plot smoothness for model validation.

## Unit synthesis: linking five concepts without forcing causality

The central lesson is that **contact structure and chains of transmission**, **basic and effective reproduction numbers**, **incubation, infectiousness and observed case timing**, **reservoirs, vectors and one health interfaces** and **environmental transmission, seasonality and context** answer related but not identical questions. Combine them into an evidence map. In the first column, write what the object or process is. In the second, specify a directly observable variable. In the third, state what the observation fails to establish. In the fourth, propose a separate measurement or comparison that could discriminate two competing explanations. The ability to name what evidence does *not* support is as central to science as correctly calculating a number.

### A worked critical-reading pattern

Start with a fictional headline claiming that a sample's measured index has doubled. Ask what the index measures and what unit was used. The number may describe a genome proxy, an assay output, a host marker or a reporting count. None is automatically a measure of an individual's contagiousness. Next, check whether the denominator is the same in the two periods. If collection criteria, instrument sensitivity, target population or data-processing rules have changed, the ratio may not compare like with like. Finally, decide whether alternative explanations predict different observable outcomes, and whether those outcomes were measured. You should be able to criticize the inference without asserting that the opposite explanation is necessarily true.

Build a two-stage evidence table: direct observations first, assumptions second. Note how a negative control or changed denominator could overturn a simple interpretation. Then decide which measurement would genuinely distinguish the candidate explanations.

### Open-book examination problems

**Essay A — causal chain.** Choose the topic **contact structure and chains of transmission** and write a diagram of five plausible links from observation to explanation. For every link, distinguish an observation from a proposed cause. Show where **incubation, infectiousness and observed case timing** might supply a competing explanation. Write a 200-word note on which inference is least supported. An appropriate answer can include 'insufficient evidence' when the source cannot distinguish alternatives.

**Essay B — dimensions and denominators.** Compare the five numeric cases in this unit. Identify which quantities are percentages, unitless proportions, indices, rates or expectations. Explain why a probability cannot exceed one, while an expected number of events may exceed one. Show an extreme-value test for one formula and state why the result need not reflect any measured system.

**Essay C — measurement design.** Using **environmental transmission, seasonality and context**, choose a hypothetical data source and a misleading interpretation that could arise from changing its sampling frame. Specify a control, a sample unit, a reporting window and one independently measured corroborating variable. Make the design noninfectious, computational and ethically appropriate. Explain what a negative result would mean and why repeated technical observations might not establish reproducibility across biological systems.

**Essay D — communicating uncertainty.** Write two abstracts for the same invented table. The first should contain only direct numerical claims. The second may offer a possible mechanism but must label it as a hypothesis and describe its strongest competitor. Identify any phrase in the second abstract that could be mistaken for causal proof and revise it. This exercise values precise communication over confident-sounding conclusions.

### Self-assessment checklist

- I can distinguish presence, structure, biological activity, population dynamics and clinical outcome.
- I can describe two plausible mechanisms for one invented pattern without assuming either is true.
- I have correctly stated the denominator and units for each numeric answer.
- I know which results are algebraic consequences of assumptions and which would require evidence.
- I can identify where a synthetic model ends and where valid real-world inference would need to begin.
- I can connect all five topics without implying every association is causal.

Complete the capstone investigation before referring to the interactive model sliders. A smooth curve that looks biological should be treated as a hypothesis generator, not as evidence. Keep a record of uncertain conclusions; the final unit revisits the same discipline in community and environmental virology.
