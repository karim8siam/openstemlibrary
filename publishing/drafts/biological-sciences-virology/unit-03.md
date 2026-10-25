# Unit 03 — Viral genetics, evolution and phylogenetic inference

> **OpenSTEM Book 14, Virology.** Undergraduate editorial draft. Every numerical example and modeled curve uses fictional input. Expert review and publication approval pending. Do not treat these pages as laboratory protocols, clinical tools or instructions for manipulating viruses.

## Learning objectives

Viral genetic change spans mutation, stochastic sampling, selection and distinct mechanisms of genomic exchange. A sequence does not record its entire causal history. Models in this unit use fictitious letters, anonymous types and abstract frequency values, never real viral sequences, so the emphasis remains on inference rather than engineering.

The five conceptual themes are **mutation and substitution; selection versus drift; genomic history; sampling bias; evolutionary evidence**. A reader completing this unit should be able to explain each of its five topics, compare at least two rival causes of a given observation, reproduce five quantitative answers, and critique a synthetic research design. Scientific maturity requires distinguishing the scale at which a fact has been measured from the scale at which an explanation is being proposed. If an observation describes nucleic-acid fragments, do not call it an infection count. If an outcome describes an immune-related marker, do not call it proven protection without validation.

## Foundations for evidence-based reasoning

Virology spans structural, cellular, ecological and clinical observations. A claim supported at one level may be unjustified at another. Check whether a measured signal is a proxy, a rate or a true outcome. Sampling time, location, group composition and denominators can change interpretation even when the plotted shape looks identical.

This unit uses models as tools for exploring assumptions. One parameter may be an arbitrary scale, while another represents a mathematical saturation point. Neither value should be mistaken for a calibrated property of a real virus. When interacting with a chart, first predict a direction, then alter one control, then explain the change in terms of the formula. Repeat with the second control and look for a limiting case. Observe how even a simple model can be illuminating for reasoning yet unsuitable for operational decisions. Reading the explicit warnings attached to each model is part of the exercise.

## Responsible research boundary

The descriptions are conceptual and pedagogical. No experiments requiring access to infectious material, clinical specimens, animals or specialized biosecurity facilities are needed or permitted by the lesson plan. Real research requires institution-specific ethical review, biosafety training and oversight. The synthetic case studies are not data collected from people, hospitals, laboratories or the environment. For work with real published material, cite the original source, verify context and licensing, and avoid reproducing identifiable records. Health, agricultural and public safety decisions should follow qualified professional guidance, not simplified student exercises.

## Topic 3.1 — Mutation, replication errors and diversity

### Mechanism and explanatory scope

Viral populations may accumulate sequence variation through replication-associated error, editing and selection. Mutation supplies some raw diversity, while selection and chance govern whether a variant becomes frequent. Error rates, realized substitution rates and observed consensus changes are different quantities measured over different denominators and timescales.

For **mutation and substitution**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A high observed variant frequency does not identify when a mutation originated or prove it improves fitness. Sampling depth, contamination, sequencing error, host factors and stochastic loss can make rare variants appear or disappear.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **variant labels, antigenic change and scientific communication** and state one observation that would differentiate the explanations.

### Measurement and controls

Calculate a fictional expected count of mutation events using a small abstract genome length and toy copying-error probability. Then explain why this expected value is not the observed number of viable new variants in a biological population.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

No exercises identify alterations that increase transmissibility, tissue range or immune escape. The calculations illustrate probability and uncertainty only.

Connect the topic to **selection, drift and population bottlenecks** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 3.1

**Question.** An abstract 800-symbol sequence is copied with error probability 0.002 per position. What is the expected number of errors?

**Invented inputs:** `L=800`, `p=0.002`. **Assumed relation:** `L*p`. **Answer:** **1.6 events per copy**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **mutation, replication errors and diversity** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **selection, drift and population bottlenecks** while identifying one uncertain link.

## Topic 3.2 — Selection, drift and population bottlenecks

### Mechanism and explanatory scope

Natural selection changes frequencies when heritable alternatives have different reproductive success in a given environment. Genetic drift changes frequencies through finite-population sampling, and transmission bottlenecks can sharply reduce standing diversity. Real sequences reflect a mixture of historical processes.

For **selection versus drift**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A variant increasing in a dataset does not itself prove selection: sampling a different subpopulation, founder effects or stochastic transmission can produce the same pattern. Selection estimates need an explicit comparison group and assumptions about population structure.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **mutation, replication errors and diversity** and state one observation that would differentiate the explanations.

### Measurement and controls

Use an abstract two-type frequency recurrence and a simulated random sampling step. Contrast deterministic change and Monte Carlo variation in a classroom toy example without supplying any biological genotype or variant identity.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

A simplified fitness parameter is context dependent and must not be interpreted as a measured real-world growth advantage. Within-host processes and between-host spread can impose different filters.

Connect the topic to **recombination and segmented-genome reassortment** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 3.2

**Question.** A type increases from frequency 0.2 to 0.3. What is its percentage-point change?

**Invented inputs:** `a=0.2`, `b=0.3`. **Assumed relation:** `100*(b-a)`. **Answer:** **10 percentage points**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **selection, drift and population bottlenecks** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **recombination and segmented-genome reassortment** while identifying one uncertain link.

## Topic 3.3 — Recombination and segmented-genome reassortment

### Mechanism and explanatory scope

Recombination and reassortment are distinct sources of genome-level novelty. Recombination involves genetic exchange within a nucleic acid molecule or related products; reassortment involves different combinations of whole segments when compatible segmented genomes contribute material. Both concepts demand appropriate mechanistic qualifications.

For **genomic history**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A mosaic-like sequence pattern can result from technical assembly artifacts, convergent evolution or mixed sampling. A cluster of sequences does not prove a particular molecular exchange event occurred.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **selection, drift and population bottlenecks** and state one observation that would differentiate the explanations.

### Measurement and controls

Compare abstract colored genome blocks with colored whole segments. State what observations would differentiate a cross-over hypothesis from a segment-level exchange hypothesis and what sequencing errors could falsely favor one.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

The exercise is representational only. It does not provide instructions for combining, engineering or rescuing infectious viral genomes.

Connect the topic to **phylogenetics and molecular-clock uncertainty** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 3.3

**Question.** In a fabricated 6-block comparison, 2 are classified as segment exchanges. What fraction is that?

**Invented inputs:** `a=2`, `n=6`. **Assumed relation:** `a/n`. **Answer:** **0.333333 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **recombination and segmented-genome reassortment** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **phylogenetics and molecular-clock uncertainty** while identifying one uncertain link.

## Topic 3.4 — Phylogenetics and molecular-clock uncertainty

### Mechanism and explanatory scope

Phylogenetic trees are conditional historical hypotheses inferred from aligned sequence data and a model of evolution. Branch length can represent substitutions or time depending on the analysis. The placement of a sample may change with reference selection, missing sites, rate heterogeneity and sampling design.

For **sampling bias**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Close placement in a tree does not by itself establish direct transmission, the direction of transmission or a particular exposure event. A root choice can substantially alter narrative interpretations, and sample date is not equivalent to infection date.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **recombination and segmented-genome reassortment** and state one observation that would differentiate the explanations.

### Measurement and controls

Evaluate an artificial pairwise distance matrix and compare two possible branching sketches. Annotate which decisions depend on alignment assumptions, the clock model and the availability of unsampled intermediate lineages.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Do not use simplified phylogenetic exercises to claim traceable source attribution for real people or communities. Such conclusions require carefully justified evidence and privacy safeguards.

Connect the topic to **variant labels, antigenic change and scientific communication** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 3.4

**Question.** If 19 of 500 abstract symbols differ, what is the simple observed mismatch fraction?

**Invented inputs:** `d=19`, `n=500`. **Assumed relation:** `d/n`. **Answer:** **0.038 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **phylogenetics and molecular-clock uncertainty** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **variant labels, antigenic change and scientific communication** while identifying one uncertain link.

## Topic 3.5 — Variant labels, antigenic change and scientific communication

### Mechanism and explanatory scope

The word variant may refer to a nucleotide difference, a consensus genome lineage, a protein alteration or a surveillance category. Antigenic differences are biological properties requiring relevant immunological evidence, not automatic consequences of genetic differences. Communication should preserve both definitions and uncertainty.

For **evolutionary evidence**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Media narratives often collapse sequence divergence, antibody recognition, clinical severity and epidemiological spread into a single claim. These measures can move independently, and historical comparisons are particularly vulnerable to changing ascertainment.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **phylogenetics and molecular-clock uncertainty** and state one observation that would differentiate the explanations.

### Measurement and controls

Create a mock evidence table separating genotype, binding measurement, neutralization measurement, case detection and clinical outcome. State how assay design and population immunity complicate comparisons over time.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Avoid inferring that a genetic difference confers a dangerous phenotype. The chapter gives no guidance for selecting or designing variants with altered host impact.

Connect the topic to **mutation, replication errors and diversity** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 3.5

**Question.** A simulated classification has 42 consistent labels among 50. What percent meet the declared label rule?

**Invented inputs:** `k=42`, `n=50`. **Assumed relation:** `100*k/n`. **Answer:** **84 %**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **variant labels, antigenic change and scientific communication** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **mutation, replication errors and diversity** while identifying one uncertain link.

## Integrated synthetic research investigation: A changing frequency in an anonymous population

### Scientific question and competing models

This investigation tests how much can be inferred from limited numerical evidence. The first explanation is that **selection produces a directional change**. The rival explanation is that **founder effects with uneven samples produce the same observed change**. Each is formulated to account for a possible upward trend without supplying any actual biological or epidemiological measurements. The goal is not to make the plots resemble authentic virus experiments; it is to learn why similar-looking data can support different causal stories and how a discriminating observation improves a research plan.

The comparison must keep the outcome definition constant. Make a causal diagram with source, intermediate step, observed proxy and background variables. Place an unmeasured factor near the arrow it might influence, rather than listing confounders without indicating their pathway. A credible alternative explanation must be capable of producing a plausible observed difference. State what information would be required to refute each explanation rather than merely to generate an additional matching curve.

### Data and transparent assumptions

| Stage | Series A (synthetic index) | Series B (synthetic index) |
|--:|--:|--:|
| 0 | 13.38 | 14.70 |
| 1 | 16.85 | 16.64 |
| 2 | 20.91 | 18.69 |
| 3 | 25.40 | 20.81 |
| 4 | 30.25 | 22.98 |
| 5 | 35.39 | 25.20 |

These are **fabricated dimensionless teaching indices**, not real assay outputs, infection counts, cases, experimental animals or clinical data. No uncertainty bands are supplied because there are no biological replicates. The table does not support p-values, confidence intervals or causal claims. Between stage zero and stage five, series A changes from **13.38** to **35.39**; the difference is **22.01 index units**. Series B changes from **14.7** to **25.2**, a difference of **10.50 index units**. These arithmetic descriptions are valid within the constructed table only.

A simple endpoint ratio, B over A, equals **0.712** if they are defined on comparable scales. A different normalization might change that ratio dramatically without changing the underlying plotted order. Plot both series with the invented stage index on the horizontal axis. It is incorrect to label the index in hours or days because the exercise deliberately supplies no physical time units. Try plotting the percent change from baseline instead, and explain why percent changes can exaggerate differences when the baseline is small.

### Study design without pathogen experimentation

The most important planned independent measurement is: **compare same-frame sampling over several times**. The leading confound is **missing populations**. State how the independent measurement would behave under the two hypotheses and whether the proposed design could still produce the same answer under different mechanisms. Use only synthetic data, publicly documented nonidentifiable aggregate reports and pencil-and-paper reasoning. No live virus, infectious specimen, virus propagation, sequence engineering or physical containment procedure is authorized or required for this educational investigation.

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

The central lesson is that **mutation, replication errors and diversity**, **selection, drift and population bottlenecks**, **recombination and segmented-genome reassortment**, **phylogenetics and molecular-clock uncertainty** and **variant labels, antigenic change and scientific communication** answer related but not identical questions. Combine them into an evidence map. In the first column, write what the object or process is. In the second, specify a directly observable variable. In the third, state what the observation fails to establish. In the fourth, propose a separate measurement or comparison that could discriminate two competing explanations. The ability to name what evidence does *not* support is as central to science as correctly calculating a number.

### A worked critical-reading pattern

Start with a fictional headline claiming that a sample's measured index has doubled. Ask what the index measures and what unit was used. The number may describe a genome proxy, an assay output, a host marker or a reporting count. None is automatically a measure of an individual's contagiousness. Next, check whether the denominator is the same in the two periods. If collection criteria, instrument sensitivity, target population or data-processing rules have changed, the ratio may not compare like with like. Finally, decide whether alternative explanations predict different observable outcomes, and whether those outcomes were measured. You should be able to criticize the inference without asserting that the opposite explanation is necessarily true.

Build a two-stage evidence table: direct observations first, assumptions second. Note how a negative control or changed denominator could overturn a simple interpretation. Then decide which measurement would genuinely distinguish the candidate explanations.

### Open-book examination problems

**Essay A — causal chain.** Choose the topic **mutation, replication errors and diversity** and write a diagram of five plausible links from observation to explanation. For every link, distinguish an observation from a proposed cause. Show where **recombination and segmented-genome reassortment** might supply a competing explanation. Write a 200-word note on which inference is least supported. An appropriate answer can include 'insufficient evidence' when the source cannot distinguish alternatives.

**Essay B — dimensions and denominators.** Compare the five numeric cases in this unit. Identify which quantities are percentages, unitless proportions, indices, rates or expectations. Explain why a probability cannot exceed one, while an expected number of events may exceed one. Show an extreme-value test for one formula and state why the result need not reflect any measured system.

**Essay C — measurement design.** Using **variant labels, antigenic change and scientific communication**, choose a hypothetical data source and a misleading interpretation that could arise from changing its sampling frame. Specify a control, a sample unit, a reporting window and one independently measured corroborating variable. Make the design noninfectious, computational and ethically appropriate. Explain what a negative result would mean and why repeated technical observations might not establish reproducibility across biological systems.

**Essay D — communicating uncertainty.** Write two abstracts for the same invented table. The first should contain only direct numerical claims. The second may offer a possible mechanism but must label it as a hypothesis and describe its strongest competitor. Identify any phrase in the second abstract that could be mistaken for causal proof and revise it. This exercise values precise communication over confident-sounding conclusions.

### Self-assessment checklist

- I can distinguish presence, structure, biological activity, population dynamics and clinical outcome.
- I can describe two plausible mechanisms for one invented pattern without assuming either is true.
- I have correctly stated the denominator and units for each numeric answer.
- I know which results are algebraic consequences of assumptions and which would require evidence.
- I can identify where a synthetic model ends and where valid real-world inference would need to begin.
- I can connect all five topics without implying every association is causal.

Complete the capstone investigation before referring to the interactive model sliders. A smooth curve that looks biological should be treated as a hypothesis generator, not as evidence. Keep a record of uncertain conclusions; the final unit revisits the same discipline in community and environmental virology.
