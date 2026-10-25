# Unit 02 — Viral information flow and the logic of infection

> **OpenSTEM Book 14, Virology.** Undergraduate editorial draft. Every numerical example and modeled curve uses fictional input. Expert review and publication approval pending. Do not treat these pages as laboratory protocols, clinical tools or instructions for manipulating viruses.

## Learning objectives

Molecular virology is a sequence of logical dependencies, not a single universal recipe. Attachment can occur without entry; entry without productive genome expression; translation without successful assembly; assembly without an infectious particle. Follow the information from viral genome to messenger RNA to components while maintaining explicit limits on what an assay observes.

The five conceptual themes are **binding versus functionality; information flow; host-cell resource constraints; life-cycle bottlenecks; assay denominators**. A reader completing this unit should be able to explain each of its five topics, compare at least two rival causes of a given observation, reproduce five quantitative answers, and critique a synthetic research design. Scientific maturity requires distinguishing the scale at which a fact has been measured from the scale at which an explanation is being proposed. If an observation describes nucleic-acid fragments, do not call it an infection count. If an outcome describes an immune-related marker, do not call it proven protection without validation.

## Foundations for evidence-based reasoning

Virology spans structural, cellular, ecological and clinical observations. A claim supported at one level may be unjustified at another. Check whether a measured signal is a proxy, a rate or a true outcome. Sampling time, location, group composition and denominators can change interpretation even when the plotted shape looks identical.

This unit uses models as tools for exploring assumptions. One parameter may be an arbitrary scale, while another represents a mathematical saturation point. Neither value should be mistaken for a calibrated property of a real virus. When interacting with a chart, first predict a direction, then alter one control, then explain the change in terms of the formula. Repeat with the second control and look for a limiting case. Observe how even a simple model can be illuminating for reasoning yet unsuitable for operational decisions. Reading the explicit warnings attached to each model is part of the exercise.

## Responsible research boundary

The descriptions are conceptual and pedagogical. No experiments requiring access to infectious material, clinical specimens, animals or specialized biosecurity facilities are needed or permitted by the lesson plan. Real research requires institution-specific ethical review, biosafety training and oversight. The synthetic case studies are not data collected from people, hospitals, laboratories or the environment. For work with real published material, cite the original source, verify context and licensing, and avoid reproducing identifiable records. Health, agricultural and public safety decisions should follow qualified professional guidance, not simplified student exercises.

## Topic 2.1 — Attachment and recognition at the cell surface

### Mechanism and explanatory scope

Entry often begins with multiple molecular interactions involving a viral component and host-associated molecules; co-receptors, glycans or environmental factors can influence attachment. Molecular binding, internalization and productive infection are logically separate milestones. Local concentration and receptor abundance also affect a measured binding signal.

For **binding versus functionality**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A high binding signal may originate from nonspecific electrostatic association, aggregate particles, assay saturation or abundant receptor expression. It cannot prove that the downstream steps required for viral reproduction have taken place.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **assembly, release and particle-to-infectivity ratios** and state one observation that would differentiate the explanations.

### Measurement and controls

Analyze a synthetic ligand-occupancy curve and identify a control that distinguishes specific binding from background adsorption. Explain why an apparent affinity from a complex cell surface is not necessarily a purified protein binding constant.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Do not use receptor-binding equations to predict human infection risk from a novel sequence or construct. They are teaching approximations that exclude immunity, tissue anatomy and downstream intracellular restrictions.

Connect the topic to **entry routes and uncoating** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 2.1

**Question.** In an idealized occupancy model with ligand concentration L=3 and K=7, what is L/(K+L)?

**Invented inputs:** `L=3`, `K=7`. **Assumed relation:** `L/(K+L)`. **Answer:** **0.3 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **attachment and recognition at the cell surface** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **entry routes and uncoating** while identifying one uncertain link.

## Topic 2.2 — Entry routes and uncoating

### Mechanism and explanatory scope

Different virus groups deliver their nucleic acids into cellular compartments through distinct entry and uncoating pathways. Membranes, vesicular trafficking and capsid remodeling can matter, but mechanistic details are group-specific. The critical analytical question is when the genome becomes available to the correct molecular machinery.

For **information flow**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Seeing internalized fluorescent signal does not distinguish intact particle uptake from released dye, and an endosomal image does not prove that the genome reached an active replication compartment. Time-resolved spatial evidence improves interpretation but still may not establish functionality.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **attachment and recognition at the cell surface** and state one observation that would differentiate the explanations.

### Measurement and controls

Given a fictional series of fluorescence locations, distinguish surface-associated, vesicular and cytosolic or nuclear signals. Specify a noninfectious particle mimic as a conceptual control and explain its limitations compared with a real biological process.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

The chapter addresses conceptual cell biology, not step-by-step delivery methods, particle construction, or infection optimization. Entry routes vary even within broad groups and cell contexts.

Connect the topic to **from viral genomes to messenger rna** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 2.2

**Question.** A synthetic internalization proxy drops from 90 to 54 units. What is the proportional decrease?

**Invented inputs:** `a=90`, `b=54`. **Assumed relation:** `(a-b)/a`. **Answer:** **0.4 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **entry routes and uncoating** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **from viral genomes to messenger rna** while identifying one uncertain link.

## Topic 2.3 — From viral genomes to messenger RNA

### Mechanism and explanatory scope

Every genome strategy must ultimately provide messages a host ribosome can translate, but the enzymatic route differs. DNA-genome viruses, positive-sense RNA viruses, negative-sense RNA viruses and reverse-transcribing viruses face different initial information constraints. Regulation of expression can be temporally organized.

For **host-cell resource constraints**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

Positive-sense RNA should not be equated with unlimited direct translation, and double-stranded DNA should not be assumed to depend exclusively on a host nucleus. These are general patterns with significant mechanistic exceptions.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **entry routes and uncoating** and state one observation that would differentiate the explanations.

### Measurement and controls

Use a safe abstract flowchart to compare the steps between an input genome and translated protein. For each route, label which transformation is logically needed without specifying viral sequences, vectors or laboratory expression systems.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Information-flow diagrams ignore subcellular localization, host shutoff, RNA processing and immune recognition. Do not confuse the route to messenger RNA with the complete life cycle.

Connect the topic to **replication regulation and host resource constraints** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 2.3

**Question.** In an abstract information-flow chart, 24 out of 32 input units reach the message stage. What is the represented conversion fraction?

**Invented inputs:** `m=24`, `i=32`. **Assumed relation:** `m/i`. **Answer:** **0.75 fraction**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **from viral genomes to messenger rna** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **replication regulation and host resource constraints** while identifying one uncertain link.

## Topic 2.4 — Replication regulation and host resource constraints

### Mechanism and explanatory scope

Viral nucleic-acid copying requires substrates, catalytic activities, suitable compartments and host resources. Even when a virus encodes key enzymes, translation and metabolic support are provided by the host. Regulatory timing can influence the balance between genome copying and structural component accumulation.

For **life-cycle bottlenecks**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

More genomic copies do not always yield more assembled infectious particles. A replication-associated assay can measure intracellular fragments, defective genomes or material from nonproductive events. A bottleneck elsewhere in the life cycle can dominate final output.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **from viral genomes to messenger rna** and state one observation that would differentiate the explanations.

### Measurement and controls

Interpret a theoretical resource-limited production curve. Compare a model in which more template raises output with a model in which host translation becomes limiting, and identify what independent measurement would distinguish them.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

The exercises omit parameters that could optimize real viral production. They are illustrative systems questions rather than experimentally calibrated growth conditions.

Connect the topic to **assembly, release and particle-to-infectivity ratios** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 2.4

**Question.** Toy output follows Y=20x/(4+x). What is Y at x=6?

**Invented inputs:** `v=20`, `x=6`, `k=4`. **Assumed relation:** `v*x/(k+x)`. **Answer:** **12 arb. units**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **replication regulation and host resource constraints** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **assembly, release and particle-to-infectivity ratios** while identifying one uncertain link.

## Topic 2.5 — Assembly, release and particle-to-infectivity ratios

### Mechanism and explanatory scope

Viral components must be organized into particles, with maturation and release differing across virus groups. Some particles are incomplete or otherwise noninfectious. The ratio between a molecular signal and infectious units depends on the assay and sample context, not just on a fixed species property.

For **assay denominators**, identify the unit of observation, the relevant timescale, and the step for which evidence is missing. A structural observation cannot alone prove a clinical or population-level effect.

### Competing explanations

A measured increase in particle-associated nucleic acid could occur while functional infectivity is constant or declining. Conversely, a functional readout may change because of target-cell conditions rather than particle abundance.

Compare a biological change with a shifted sampling frame or instrument response. Connect the topic to **replication regulation and host resource constraints** and state one observation that would differentiate the explanations.

### Measurement and controls

Given synthetic genome-copy and functional-index columns, calculate a ratio and discuss how detection thresholds or assay saturation alter interpretation. Use dimensionally correct labels and avoid interpreting the ratio as a universal conversion factor.

Declare the outcome, unit, denominator, window and negative control. Technical repeats are not independent biological replicates; no fictional curve supplies a confidence interval or causal proof.

### Limitations and connections

Not every viral system has a meaningful singular particle-to-infectivity ratio. Functional measurements require specialized facilities and trained professionals and are not procedures taught here.

Connect the topic to **attachment and recognition at the cell surface** on an evidence ladder from molecules to populations. Name the missing assumption before moving between scales, and keep clinical or biosafety decisions outside this teaching model.

### Worked quantitative case 2.5

**Question.** A mock dataset reports 240 genome-index units and 12 function-index units. What is the ratio?

**Invented inputs:** `g=240`, `f=12`. **Assumed relation:** `g/f`. **Answer:** **20 index ratio**. Work through the substitution without confusing a percentage with a unitless fraction. State the denominator, and check whether any rate also needs a time unit. A direct ratio answers the arithmetic question but cannot, by itself, establish infectiousness, clinical disease or transmission.

**What might break the inference?** Identify whether a changed sampling frame, a poorly calibrated measurement or an invalid modeling assumption could change the result. Alter the first numerical input by ten percent, keeping other values fixed, and independently recompute the output. Explain whether its response is proportional or nonlinear. All values here are fictional; no measurements or biological replicates were collected.

### Apply the idea

1. Define the central term in **assembly, release and particle-to-infectivity ratios** and name one tempting but unsupported inference.
2. State two explanations of the same imaginary observation and propose a distinguishing, safe, noninfectious analysis.
3. Recalculate the numerical case with correctly labeled units and discuss a limiting case.
4. Create a three-column evidence ledger: direct observations, inferred mechanism and absent evidence.
5. Explain how this topic connects to **attachment and recognition at the cell surface** while identifying one uncertain link.

## Integrated synthetic research investigation: A bottleneck in an abstract viral life-cycle diagram

### Scientific question and competing models

This investigation tests how much can be inferred from limited numerical evidence. The first explanation is that **an upstream index increases while the downstream index flattens**. The rival explanation is that **host-resource limitation explains the plateau**. Each is formulated to account for a possible upward trend without supplying any actual biological or epidemiological measurements. The goal is not to make the plots resemble authentic virus experiments; it is to learn why similar-looking data can support different causal stories and how a discriminating observation improves a research plan.

The comparison must keep the outcome definition constant. Make a causal diagram with source, intermediate step, observed proxy and background variables. Place an unmeasured factor near the arrow it might influence, rather than listing confounders without indicating their pathway. A credible alternative explanation must be capable of producing a plausible observed difference. State what information would be required to refute each explanation rather than merely to generate an additional matching curve.

### Data and transparent assumptions

| Stage | Series A (synthetic index) | Series B (synthetic index) |
|--:|--:|--:|
| 0 | 12.25 | 13.60 |
| 1 | 15.54 | 15.43 |
| 2 | 19.39 | 17.36 |
| 3 | 23.64 | 19.35 |
| 4 | 28.23 | 21.40 |
| 5 | 33.11 | 23.48 |

These are **fabricated dimensionless teaching indices**, not real assay outputs, infection counts, cases, experimental animals or clinical data. No uncertainty bands are supplied because there are no biological replicates. The table does not support p-values, confidence intervals or causal claims. Between stage zero and stage five, series A changes from **12.25** to **33.11**; the difference is **20.86 index units**. Series B changes from **13.6** to **23.48**, a difference of **9.88 index units**. These arithmetic descriptions are valid within the constructed table only.

A simple endpoint ratio, B over A, equals **0.709** if they are defined on comparable scales. A different normalization might change that ratio dramatically without changing the underlying plotted order. Plot both series with the invented stage index on the horizontal axis. It is incorrect to label the index in hours or days because the exercise deliberately supplies no physical time units. Try plotting the percent change from baseline instead, and explain why percent changes can exaggerate differences when the baseline is small.

### Study design without pathogen experimentation

The most important planned independent measurement is: **assay saturation also explains the plateau**. The leading confound is **normalization and dynamic range**. State how the independent measurement would behave under the two hypotheses and whether the proposed design could still produce the same answer under different mechanisms. Use only synthetic data, publicly documented nonidentifiable aggregate reports and pencil-and-paper reasoning. No live virus, infectious specimen, virus propagation, sequence engineering or physical containment procedure is authorized or required for this educational investigation.

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

The central lesson is that **attachment and recognition at the cell surface**, **entry routes and uncoating**, **from viral genomes to messenger rna**, **replication regulation and host resource constraints** and **assembly, release and particle-to-infectivity ratios** answer related but not identical questions. Combine them into an evidence map. In the first column, write what the object or process is. In the second, specify a directly observable variable. In the third, state what the observation fails to establish. In the fourth, propose a separate measurement or comparison that could discriminate two competing explanations. The ability to name what evidence does *not* support is as central to science as correctly calculating a number.

### A worked critical-reading pattern

Start with a fictional headline claiming that a sample's measured index has doubled. Ask what the index measures and what unit was used. The number may describe a genome proxy, an assay output, a host marker or a reporting count. None is automatically a measure of an individual's contagiousness. Next, check whether the denominator is the same in the two periods. If collection criteria, instrument sensitivity, target population or data-processing rules have changed, the ratio may not compare like with like. Finally, decide whether alternative explanations predict different observable outcomes, and whether those outcomes were measured. You should be able to criticize the inference without asserting that the opposite explanation is necessarily true.

Build a two-stage evidence table: direct observations first, assumptions second. Note how a negative control or changed denominator could overturn a simple interpretation. Then decide which measurement would genuinely distinguish the candidate explanations.

### Open-book examination problems

**Essay A — causal chain.** Choose the topic **attachment and recognition at the cell surface** and write a diagram of five plausible links from observation to explanation. For every link, distinguish an observation from a proposed cause. Show where **from viral genomes to messenger rna** might supply a competing explanation. Write a 200-word note on which inference is least supported. An appropriate answer can include 'insufficient evidence' when the source cannot distinguish alternatives.

**Essay B — dimensions and denominators.** Compare the five numeric cases in this unit. Identify which quantities are percentages, unitless proportions, indices, rates or expectations. Explain why a probability cannot exceed one, while an expected number of events may exceed one. Show an extreme-value test for one formula and state why the result need not reflect any measured system.

**Essay C — measurement design.** Using **assembly, release and particle-to-infectivity ratios**, choose a hypothetical data source and a misleading interpretation that could arise from changing its sampling frame. Specify a control, a sample unit, a reporting window and one independently measured corroborating variable. Make the design noninfectious, computational and ethically appropriate. Explain what a negative result would mean and why repeated technical observations might not establish reproducibility across biological systems.

**Essay D — communicating uncertainty.** Write two abstracts for the same invented table. The first should contain only direct numerical claims. The second may offer a possible mechanism but must label it as a hypothesis and describe its strongest competitor. Identify any phrase in the second abstract that could be mistaken for causal proof and revise it. This exercise values precise communication over confident-sounding conclusions.

### Self-assessment checklist

- I can distinguish presence, structure, biological activity, population dynamics and clinical outcome.
- I can describe two plausible mechanisms for one invented pattern without assuming either is true.
- I have correctly stated the denominator and units for each numeric answer.
- I know which results are algebraic consequences of assumptions and which would require evidence.
- I can identify where a synthetic model ends and where valid real-world inference would need to begin.
- I can connect all five topics without implying every association is causal.

Complete the capstone investigation before referring to the interactive model sliders. A smooth curve that looks biological should be treated as a hypothesis generator, not as evidence. Keep a record of uncertain conclusions; the final unit revisits the same discipline in community and environmental virology.
