# Unit 06 — Virological measurements, surveillance and scientific uncertainty

> **OpenSTEM Book 14, Virology.** Undergraduate editorial draft. Every numerical example and modeled curve uses fictional input. Expert review and publication approval pending. Do not treat these pages as laboratory protocols, clinical tools or instructions for manipulating viruses.

## Learning objectives

Measurement is an inference chain: specimen, analytical system, signal, classification and interpretation. Positive observations may reflect a chosen assay target without establishing clinical disease, viability or transmissibility. This unit develops diagnostic numeracy and transparent surveillance reasoning, not clinical test procedures.

The five conceptual themes are **analytic detection; conditional probability; sampling frame; clinical interpretation; data provenance**. A reader completing this unit should be able to explain each of its five topics, compare at least two rival causes of a given observation, reproduce five quantitative answers, and critique a synthetic research design. Scientific maturity requires distinguishing the scale at which a fact has been measured from the scale at which an explanation is being proposed. If an observation describes nucleic-acid fragments, do not call it an infection count. If an outcome describes an immune-related marker, do not call it proven protection without validation.

## Foundations for evidence-based reasoning

Virology spans structural, cellular, ecological and clinical observations. A claim supported at one level may be unjustified at another. Check whether a measured signal is a proxy, a rate or a true outcome. Sampling time, location, group composition and denominators can change interpretation even when the plotted shape looks identical.

This unit uses models as tools for exploring assumptions. One parameter may be an arbitrary scale, while another represents a mathematical saturation point. Neither value should be mistaken for a calibrated property of a real virus. When interacting with a chart, first predict a direction, then alter one control, then explain the change in terms of the formula. Repeat with the second control and look for a limiting case. Observe how even a simple model can be illuminating for reasoning yet unsuitable for operational decisions. Reading the explicit warnings attached to each model is part of the exercise.

## Responsible research boundary

The descriptions are conceptual and pedagogical. No experiments requiring access to infectious material, clinical specimens, animals or specialized biosecurity facilities are needed or permitted by the lesson plan. Real research requires institution-specific ethical review, biosafety training and oversight. The synthetic case studies are not data collected from people, hospitals, laboratories or the environment. For work with real published material, cite the original source, verify context and licensing, and avoid reproducing identifiable records. Health, agricultural and public safety decisions should follow qualified professional guidance, not simplified student exercises.

## Topic 6.1 — Molecular detection and interpretation of signal

### Mechanism and explanatory scope

Nucleic-acid amplification and sequencing can detect fragments of viral genetic material. An analytical positive is defined relative to method, controls, reference targets and thresholds. Molecular positivity should not be equated automatically with contagiousness or the quantity of viable particles.

For **analytic detection**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A low or high cycle-threshold value cannot be interpreted identically across platforms, sample types and protocols. Extraction variation, sample quality and inhibition alter observed values; any approximate doubling rule requires clearly stated idealized assumptions.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **ethics, provenance and biosafety literacy** and state one observation that would differentiate the explanations.

### Measurement and controls

In a purely invented dataset, compare signal intensities and compute differences under a hypothetical perfect-amplification assumption. Discuss how controls and calibration change the claim.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

No laboratory diagnostic protocol, primer design or specimen-handling instructions are supplied. Clinical diagnosis belongs to validated local services and current official guidance.

Connect the topic to **antigen, antibody and functional assay distinctions** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 6.1

**Question.** Under a purely theoretical perfect-doubling model, what signal-fold difference accompanies 3 ideal cycles?

**Invented inputs:** `d=3`. **Assumed relation:** `2**d`. **Answer:** **8 fold**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **molecular detection and interpretation of signal** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **antigen, antibody and functional assay distinctions** while identifying one uncertain link.

## Topic 6.2 — Antigen, antibody and functional assay distinctions

### Mechanism and explanatory scope

Antigen tests aim to detect viral proteins or related components, whereas serological assays assess aspects of a host response. Functional assays ask different questions from binding assays. Each test has a context-specific window in which the targeted signal is likely to be informative.

For **conditional probability**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A negative antigen test at one time cannot rule out all infection histories, while a positive antibody test may indicate previous exposure or vaccination depending on the assay. Sensitivity and specificity are conditional on the case definition and validation population.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **molecular detection and interpretation of signal** and state one observation that would differentiate the explanations.

### Measurement and controls

Create a 2-by-2 contingency table for a hypothetical test with known simulated counts. Compute sensitivity, specificity and predictive values; then examine how prevalence alters the positive predictive value.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Never infer a personal clinical conclusion from the practice data. Test performance should not be transferred between populations or assay designs without evidence.

Connect the topic to **sequencing surveillance and sampling bias** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 6.2

**Question.** A toy study has 72 true positives from 80 reference-positive examples. What is sensitivity?

**Invented inputs:** `tp=72`, `p=80`. **Assumed relation:** `tp/p`. **Answer:** **0.9 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **antigen, antibody and functional assay distinctions** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **sequencing surveillance and sampling bias** while identifying one uncertain link.

## Topic 6.3 — Sequencing surveillance and sampling bias

### Mechanism and explanatory scope

Sequence surveillance describes sampled viral genetic diversity and can reveal changing lineages or patterns. Its inferences depend on where, when and from whom samples were obtained and on quality filtering, metadata and analysis pipeline choices.

For **sampling frame**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A lineage occupying a large fraction of deposited sequences need not occupy the same fraction of infections. Geographic sampling intensity, targeted outbreak investigations and retrospective deposits can bias the denominator.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **antigen, antibody and functional assay distinctions** and state one observation that would differentiate the explanations.

### Measurement and controls

Analyze a fictional two-region table in which one region contributes many more sequences per infection estimate. Reweight the counts to an explicitly declared sampling frame and compare the resulting interpretation.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Do not publish identifiable patient or location metadata without authorization. A sequence database alone does not establish clinical severity or causal transmissibility.

Connect the topic to **uncertainty, false positives and bayesian reasoning** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 6.3

**Question.** A surveillance table has 140 reads with a selected label among 700. What percentage bear the label?

**Invented inputs:** `n=140`, `t=700`. **Assumed relation:** `100*n/t`. **Answer:** **20 %**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **sequencing surveillance and sampling bias** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **uncertainty, false positives and bayesian reasoning** while identifying one uncertain link.

## Topic 6.4 — Uncertainty, false positives and Bayesian reasoning

### Mechanism and explanatory scope

Predictive values combine test characteristics with prior probability or prevalence. Rare outcomes can produce surprising proportions of false positives even when specificity is high. Estimation should distinguish analytical detection, clinical case classification and downstream public-health decisions.

For **clinical interpretation**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Reporting only sensitivity can hide the false-positive burden in low-prevalence populations. Selecting a test cutoff after seeing results exaggerates apparent accuracy unless validated in an independent sample.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **sequencing surveillance and sampling bias** and state one observation that would differentiate the explanations.

### Measurement and controls

Calculate a hypothetical predictive value using Bayes' theorem and cross-check it with an expected-count table for 10,000 imaginary people. Then vary the assumed prevalence and graph the effect while leaving assay performance fixed.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Population-based priors do not determine an individual's clinical probability without relevant context. This book cannot replace medical interpretation or public health guidance.

Connect the topic to **ethics, provenance and biosafety literacy** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 6.4

**Question.** For sensitivity 0.9, specificity 0.95 and prevalence 0.05, what is the toy PPV?

**Invented inputs:** `se=0.9`, `sp=0.95`, `p=0.05`. **Assumed relation:** `se*p/(se*p+(1-sp)*(1-p))`. **Answer:** **0.486486 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **uncertainty, false positives and bayesian reasoning** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **ethics, provenance and biosafety literacy** while identifying one uncertain link.

## Topic 6.5 — Ethics, provenance and biosafety literacy

### Mechanism and explanatory scope

Virological evidence must be traceable to a data source, legal permission, laboratory quality framework and appropriately calibrated interpretation. Preprints, surveillance dashboards and peer-reviewed studies have different review states and potential biases. Biosafety refers to risk assessment, training and containment obligations, not a badge inferred from a method name.

For **data provenance**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

An attractive graph can hide mislabeled units, cherry-picked time windows or restricted patient data. Publishing code and numbers is not enough if the underlying provenance cannot be verified or consent and confidentiality have been violated.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **uncertainty, false positives and bayesian reasoning** and state one observation that would differentiate the explanations.

### Measurement and controls

Create a transparent evidence ledger for a fabricated literature summary: claim, type of source, publication date, limitations, replication state and licensing. Mark which parts are observations and which are interpretations.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

This section does not teach pathogen handling or laboratory containment procedures. Institutional biosafety officers and official standards govern any real research activity.

Connect the topic to **molecular detection and interpretation of signal** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 6.5

**Question.** An evidence ledger checks 29 of 35 entries. What is the checklist completion percentage?

**Invented inputs:** `k=29`, `n=35`. **Assumed relation:** `100*k/n`. **Answer:** **82.8571 %**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **ethics, provenance and biosafety literacy** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **molecular detection and interpretation of signal** while identifying one uncertain link.

## Integrated synthetic research investigation: A surveillance signal with changing case definitions

### Scientific question and competing models

This investigation tests how much can be inferred from limited numerical evidence. The first explanation is that **greater true prevalence explains more test positives**. The rival explanation is that **expanded testing explains the observation**. Each is formulated to account for a possible upward trend without supplying any actual biological or epidemiological measurements. The goal is not to make the plots resemble authentic virus experiments; it is to learn why similar-looking data can support different causal stories and how a discriminating observation improves a research plan.

The comparison must keep the outcome definition constant. Make a causal diagram with source, intermediate step, observed proxy and background variables. Place an unmeasured factor near the arrow it might influence, rather than listing confounders without indicating their pathway. A credible alternative explanation must be capable of producing a plausible observed difference. State what information would be required to refute each explanation rather than merely to generate an additional matching curve.

### Data and transparent assumptions

| Stage | Series A (synthetic index) | Series B (synthetic index) |
|--:|--:|--:|
| 0 | 16.75 | 18.00 |
| 1 | 20.77 | 20.29 |
| 2 | 25.47 | 22.70 |
| 3 | 30.67 | 25.19 |
| 4 | 36.28 | 27.75 |
| 5 | 42.24 | 30.35 |

These are **fabricated dimensionless teaching indices**, not real assay outputs, infection counts, cases, experimental animals or clinical data. No uncertainty bands are supplied because there are no biological replicates. The table does not support p-values, confidence intervals or causal claims. Between stage zero and stage five, series A changes from **16.75** to **42.24**; the difference is **25.49 index units**. Series B changes from **18.0** to **30.35**, a difference of **12.35 index units**. These arithmetic descriptions are valid within the constructed table only.

A simple endpoint ratio, B over A, equals **0.719** if they are defined on comparable scales. A different normalization might change that ratio dramatically without changing the underlying plotted order. Plot both series with the invented stage index on the horizontal axis. It is incorrect to label the index in hours or days because the exercise deliberately supplies no physical time units. Try plotting the percent change from baseline instead, and explain why percent changes can exaggerate differences when the baseline is small.

### Study design without pathogen experimentation

The most important planned independent measurement is: **tabulate positivity and number tested separately**. The leading confound is **changing test population**. State how the independent measurement would behave under the two hypotheses and whether the proposed design could still produce the same answer under different mechanisms. Use only synthetic data, publicly documented nonidentifiable aggregate reports and pencil-and-paper reasoning. No live virus, infectious specimen, virus propagation, sequence engineering or physical containment procedure is authorized or required for this educational investigation.

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

The central lesson is that **molecular detection and interpretation of signal**, **antigen, antibody and functional assay distinctions**, **sequencing surveillance and sampling bias**, **uncertainty, false positives and bayesian reasoning** and **ethics, provenance and biosafety literacy** answer related but not identical questions. Combine them into an evidence map. In the first column, write what the object or process is. In the second, specify a directly observable variable. In the third, state what the observation fails to establish. In the fourth, propose a separate measurement or comparison that could discriminate two competing explanations. The ability to name what evidence does *not* support is as central to science as correctly calculating a number.

### A worked critical-reading pattern

Start with a fictional headline claiming that a sample's measured index has doubled. Ask what the index measures and what unit was used. The number may describe a genome proxy, an assay output, a host marker or a reporting count. None is automatically a measure of an individual's contagiousness. Next, check whether the denominator is the same in the two periods. If collection criteria, instrument sensitivity, target population or data-processing rules have changed, the ratio may not compare like with like. Finally, decide whether alternative explanations predict different observable outcomes, and whether those outcomes were measured. You should be able to criticize the inference without asserting that the opposite explanation is necessarily true.

Build a two-stage evidence table: direct observations first, assumptions second. Note how a negative control or changed denominator could overturn a simple interpretation. Then decide which measurement would genuinely distinguish the candidate explanations.

### Open-book examination problems

**Essay A — causal chain.** Choose the topic **molecular detection and interpretation of signal** and write a diagram of five plausible links from observation to explanation. For every link, distinguish an observation from a proposed cause. Show where **sequencing surveillance and sampling bias** might supply a competing explanation. Write a 200-word note on which inference is least supported. An appropriate answer can include 'insufficient evidence' when the source cannot distinguish alternatives.

**Essay B — dimensions and denominators.** Compare the five numeric cases in this unit. Identify which quantities are percentages, unitless proportions, indices, rates or expectations. Explain why a probability cannot exceed one, while an expected number of events may exceed one. Show an extreme-value test for one formula and state why the result need not reflect any measured system.

**Essay C — measurement design.** Using **ethics, provenance and biosafety literacy**, choose a hypothetical data source and a misleading interpretation that could arise from changing its sampling frame. Specify a control, a sample unit, a reporting window and one independently measured corroborating variable. Make the design noninfectious, computational and ethically appropriate. Explain what a negative result would mean and why repeated technical observations might not establish reproducibility across biological systems.

**Essay D — communicating uncertainty.** Write two abstracts for the same invented table. The first should contain only direct numerical claims. The second may offer a possible mechanism but must label it as a hypothesis and describe its strongest competitor. Identify any phrase in the second abstract that could be mistaken for causal proof and revise it. This exercise values precise communication over confident-sounding conclusions.

### Self-assessment checklist

- I can distinguish presence, structure, biological activity, population dynamics and clinical outcome.
- I can describe two plausible mechanisms for one invented pattern without assuming either is true.
- I have correctly stated the denominator and units for each numeric answer.
- I know which results are algebraic consequences of assumptions and which would require evidence.
- I can identify where a synthetic model ends and where valid real-world inference would need to begin.
- I can connect all five topics without implying every association is causal.

Complete the capstone investigation before referring to the interactive model sliders. A smooth curve that looks biological should be treated as a hypothesis generator, not as evidence. Keep a record of uncertain conclusions; the final unit revisits the same discipline in community and environmental virology.
