# Unit 02 — Innate recognition, inflammation and complement

> **OpenSTEM Biological Sciences, Book 13: Immunology.** Undergraduate editorial draft; expert review pending. All numerical inputs and investigation records are hypothetical instructional examples. Models are not pathogen predictions, diagnostic tests, patient advice or clinical decision tools.

## Learning objectives and context

Innate defense converts molecular detection into recruitment and effector action. An undergraduate analysis must trace receptor specificity, signal amplification, spatial delivery and checks on self-injury. Broad words such as inflammation hide multiple coupled but separable molecular events.

The five topics in this unit approach a common problem from different levels of explanation. They concern **recognition versus activation; signal amplification; localized recruitment; complement control; resolution mechanisms**. By the end, explain the core mechanism for each topic, identify at least two plausible alternative explanations for a measured signal, reproduce the arithmetic in five cases, and describe what data would actually falsify a claim. Separate the event being *detected* from the downstream consequence inferred from that event. In immunology, an increase in a reporter, a cytokine, a cell percentage or antibody binding often looks persuasive but rarely establishes host protection by itself.

A useful immune-system model declares its spatial scale, the biological unit and the time horizon. A molecule can bind within seconds, a cell may alter transcription over hours, a clone expands across days, and tissue structure or population immunity changes across longer periods. Measured concentrations cannot be substituted for cell numbers, and cell numbers cannot replace measurements of functional killing, pathogen burden or tissue function. Check whether a figure uses proportions of all live cells, proportions within a selected gate, copies per milliliter, fluorescence units or an actual physical rate. The denominator is part of the scientific claim.

## Evidence and responsible interpretation

An immune response depends on anatomical compartment and previous exposure. Blood samples provide valuable, accessible information but can miss tissue-resident populations and localized mediator gradients. Bulk averages hide rare cell populations and interactions. Healthy versus diseased comparisons can confound cause and consequence, while an intervention that changes two pathways at once may not isolate either one. For quantitative work, preserve raw counts, clarify calibration, distinguish independent donors from repeated technical wells, and describe measurement error separately from biological variation.

All activities in this unit are computational, synthetic-data or abstract analysis exercises. Do not culture pathogens, perform human or animal exposure experiments, or attempt clinical assays on personal samples from these pages. Appropriate institutional biosafety and ethics review are prerequisites for any real laboratory research. These pages never prescribe immunization, diagnosis or treatment.


## Topic 2.1 — Pattern-recognition receptors and danger signals

### Biological mechanism

Toll-like, NOD-like, RIG-I-like and other receptors detect distinct molecular contexts such as microbial nucleic acids or cell-wall components. Receptor localization helps avoid inappropriate activation: endosomal nucleic-acid sensors sample a different compartment from cytosolic detectors. Downstream adaptors connect engagement to transcription, inflammasome assembly or antiviral programs.

### Why a plausible explanation can fail

Pathogen-associated molecular patterns and damage-associated signals can overlap in the inflammation they induce. Receptor activation does not reveal whether a detected substance came from a living replicating organism. Some receptors are activated by products of tissue injury in sterile conditions.

To challenge this account, use the related concept **signal amplification** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In a non-pathogen cell-signaling thought experiment, compare an intact ligand with a structurally altered negative control and measure a pathway reporter plus viability. Receptor knockdown helps attribution, but off-target effects and redundant receptors require independent verification.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A reporter increase is not proof of antimicrobial protection. A reporter may reflect pathway induction without production of an active effector molecule, correct localization or effective pathogen control.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 2.1

**Problem.** In a reporter assay, 75 of 300 cells cross a defined activity threshold. Compute fraction activated.

**Hypothetical inputs:** active = 75, n = 300. **Relation:** `active/n*100`. **Answer:** **25 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Cells with signal above a threshold form an assay-specific category. **Scope limit:** A detection threshold can create an artificial binary activation boundary. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **recognition versus activation**: direct observations versus explanatory assumptions. Draw a causal network for **pattern-recognition receptors and danger signals** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 2.2 — Cytokine networks and chemokine gradients

### Biological mechanism

Cytokines create context-dependent instructions for immune cells; chemokines bias movement along spatial or haptotactic gradients through cell-surface receptors. Signaling through receptor-associated kinases and transcription factors changes transcription, survival and metabolism. Receptor abundance, negative feedback and ligand availability shape response strength.

### Why a plausible explanation can fail

A concentration measured in plasma does not describe a gradient in tissue. A chemokine can be abundant but poorly positioned to guide cells, and a cytokine can have different consequences in macrophages, epithelial cells and lymphocytes. Multiple cytokines may synergize or counteract each other.

To challenge this account, use the related concept **localized recruitment** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

In a constructed microfluidic model, measure cell displacement toward a gradient and separately record random motility. Evaluate the chemotactic index rather than using total movement distance as evidence for directional guidance. Check that surfaces do not bind the ligand unevenly.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

Cytokine concentrations cannot be interpreted independently of assay calibration and sampled compartment. A twofold increase in bulk supernatant may arise from twice as many cells rather than doubled release per cell.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 2.2

**Problem.** A mock chemotaxis track advances 18 µm toward a cue across 60 µm total path length. Calculate directional index.

**Hypothetical inputs:** net = 18, track = 60. **Relation:** `net/track`. **Answer:** **0.3 index**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Directional movement is distinguished from random motility. **Scope limit:** This simple index ignores track curvature and gradient field changes. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **signal amplification**: direct observations versus explanatory assumptions. Draw a causal network for **cytokine networks and chemokine gradients** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 2.3 — Neutrophil recruitment and phagocytosis

### Biological mechanism

Neutrophils travel from blood into inflamed tissue through rolling, integrin-mediated adhesion and transendothelial migration. Their receptors detect opsonized particles and activating signals; engulfed material enters compartments containing proteases and reactive chemistry. Phagocytosis is a multistep process involving binding, internalization, maturation and degradation.

### Why a plausible explanation can fail

An increase in neutrophils at a site can mean more recruitment or slower clearance. Strong antimicrobial release can damage neighboring host tissues. Extracellular traps may appear in selected contexts, but the presence of extracellular DNA alone does not establish a functionally protective trap mechanism.

To challenge this account, use the related concept **complement control** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

A safe classroom analysis can use video data from inert fluorescent particles taken up by a nonpathogenic model cell line. Count association and internalization separately using appropriate imaging controls. Record time-to-engulfment distributions rather than relying on a single end-point average.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A fluorescence increase around cells is not equivalent to successful degradation of a pathogen. Dead or extracellular particles, probe bleaching and receptor saturation can distort interpretation.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 2.3

**Problem.** At one time point 45 of 180 internalized inert particles are fully processed. Find processed fraction.

**Hypothetical inputs:** processed = 45, engulfed = 180. **Relation:** `processed/engulfed*100`. **Answer:** **25 %**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** Particle association, uptake and degradation are distinct stages. **Scope limit:** Fluorescence may not directly measure chemical breakdown. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **localized recruitment**: direct observations versus explanatory assumptions. Draw a causal network for **neutrophil recruitment and phagocytosis** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 2.4 — Complement activation and regulatory checkpoints

### Biological mechanism

The classical, lectin and alternative complement routes converge on proteolytic amplification involving C3. Deposited fragments can opsonize surfaces, soluble fragments recruit or activate cells, and downstream assembly can damage certain target membranes. Host-protective regulators inhibit inappropriate deposition or membrane injury on healthy tissues.

### Why a plausible explanation can fail

Complement is not simply a linear cascade that automatically destroys any microbial cell. Susceptibility differs among target surfaces, amplification can be controlled locally, and opsonization may matter more than terminal membrane attack. Deficient regulation can be harmful even when microbial recognition is intact.

To challenge this account, use the related concept **resolution mechanisms** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Given a hypothetical C3-fragment deposition time series, distinguish initial recognition from amplification by measuring slope before and after a regulatory perturbation. Include a blank surface and a control for nonspecific antibody signal. Use complement-depleted controls only as an analytical concept, not a protocol.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A high soluble complement component concentration does not necessarily imply high activation; cleavage products and deposition are different readouts. Avoid equating fluorescence intensities from different antibody probes.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 2.4

**Problem.** Complement-deposition proxy rises from 100 to 250 units over 5 minutes. Calculate average increase rate.

**Hypothetical inputs:** final = 250, initial = 100, minutes = 5. **Relation:** `(final-initial)/minutes`. **Answer:** **30 proxy units/min**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** A slope can summarize an interval but cannot isolate complement pathways. **Scope limit:** Real amplification is non-linear and can saturate. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **complement control**: direct observations versus explanatory assumptions. Draw a causal network for **complement activation and regulatory checkpoints** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Topic 2.5 — Interferons, inflammasomes and resolution

### Biological mechanism

Type I interferons induce antiviral-associated programs in many cell types through receptor signaling and interferon-stimulated genes. Inflammasome pathways can lead to inflammatory cytokine maturation and specialized inflammatory cell death. Resolution recruits inhibitory mediators, clearance of spent cells and tissue repair networks that restore local structure.

### Why a plausible explanation can fail

Antiviral pathway induction can restrict some viruses but also impose metabolic costs and change tissue sensitivity. Inflammasome activation and interferon induction are distinct events; one is not a universal substitute for the other. Long-term signaling can alter differentiation and cause dysfunction.

To challenge this account, use the related concept **recognition versus activation** to propose a different route to the same observation. Which intermediate biological step would make the two hypotheses diverge?

### Designing an informative measurement

Compare three constructed time courses: early interferon-responsive transcription, a later inflammatory mediator, and a tissue-repair marker. Explain what sampling frequency would resolve their apparent ordering. Tissue heterogeneity may make a bulk response appear prolonged even if individual cells respond briefly.

Define a control that separates assay background from biological mechanism. Sample before, during and after the expected response, and identify a second measurement that would corroborate the proposed pathway.

### Boundaries and counterexamples

A transcriptional signature does not prove a clinically useful antiviral effect. A single biomarker cannot diagnose an inflammasome-associated disorder or establish that inflammation has resolved.

Construct a counterexample where the measured signal changes without the proposed mechanism changing. Prioritize one alternative and choose an observation that would refute it.

### Quantitative worked case 2.5

**Problem.** A hypothetical interferon marker declines from 80 to 20 units in 6 h. Assuming pure exponential decay, calculate the apparent half-life.

**Hypothetical inputs:** hours = 6, start = 80, end = 20. **Relation:** `hours/math.log(start/end,2)`. **Answer:** **3 h**. Recompute independently and identify the physical or assay denominator, including the time interval where applicable.

**Interpretation:** The observed factor-of-four decline spans two ideal half-lives. **Scope limit:** Production, receptor uptake and cellular turnover can violate simple exponential decay. These invented inputs offer no independent biological replicates or measured variance. Change an input by 20 percent, repeat the calculation and identify one mechanism that could break the simplified assumption.

### Applying and challenging the concept

Prepare a two-column evidence ledger on **resolution mechanisms**: direct observations versus explanatory assumptions. Draw a causal network for **interferons, inflammasomes and resolution** with one feedback edge. State how a null result could reflect either a false hypothesis or inadequate sampling.


## Integrated computational investigation — Recognition, cytokines and recruitment at different times

### Question and rival explanations

A constructed immune-challenge reporter rises before cell arrival; is receptor engagement sufficient to explain the accumulated cells?

**Mechanistic hypothesis A:** Early recognition drives a chemokine gradient.

**Mechanistic hypothesis B:** Tissue stress changes vascular access independently of the gradient.

The challenge is not to select the explanation that seems familiar. First articulate the different predictions each account makes under a condition that would actually distinguish them. A mechanism might predict an early localized signal, whereas an alternative predicts a later population effect; both can reproduce the same final bulk number. Construct a causal diagram with the stimulus, intermediate state, assay output and at least one unmeasured covariate. Mark which relations are observed and which require assumptions. The invented numbers below are practice material only: no patients, animals, pathogen samples or laboratory measurements generated them.

### Research design

Analyze simulated receptor-reporter traces, chemokine spatial profiles and tracked cell migration in separately normalized assays. Compare directedness and total mobility while varying a cue-gradient factor.

**Principal confound:** Sampling one central tissue spot cannot establish a gradient, and altered cell viability changes apparent recruitment..

A study needs biological units that match the hypothesis. If all measurements come from one culture vessel, 50 images represent subsampling of that vessel, not 50 independent cultures. If hundreds of cells come from one donor, those cells cannot support donor-level generalization without a design that accounts for clustering. Predefine the primary comparison, effect direction, main covariates and quality exclusions. Calibrate instruments or report uncalibrated arbitrary units explicitly, and store the untouched data before plotting or normalization. Use safe computational methods for these classroom tasks; any real specimen acquisition requires proper authorization, ethics and biosafety oversight.

### Constructed series (not research data)

| Stage / sample index | Series A (invented) | Series B (invented) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 4 | 1.2 |
| 2 | 6 | 2.3 |
| 3 | 5 | 4.1 |
| 4 | 3 | 5.2 |

Series A changes by **2** display units across the five stages; series B changes by **4.2**. Its endpoint ratio is **1.733** if the chosen scales are comparable; if the assays do not share a scale, that arithmetic is only a display ratio and has no biological interpretation. Compute each sequence's initial-to-final proportional change separately. Plot the two curves, label axis units or 'arbitrary teaching index', and add no error bars: the dataset supplies no independent replicate variation. Do not invent significance levels, biological confidence intervals or citations to make synthetic observations appear empirical.

### Interpretation and identification

The reporter peaks earlier, but a causal connection requires perturbing the cue and ruling out vascular and motility confounds. The most important next step is to specify a discriminating measurement. A time course is better than a single endpoint when mechanisms have distinct delays, but unobserved confounding remains possible. A targeted perturbation can improve causal identification, provided it does not independently change the outcome through a second mechanism. Some data would make both hypotheses less plausible; identify such a result explicitly. The final answer should distinguish the direction of the constructed numbers, the mechanism proposed to explain them, and the missing evidence needed for a real biological conclusion.

### Structured analysis assignment

1. Write both hypotheses as falsifiable predictions for one named assay and an explicit time window.
2. State whether the sample unit is a donor, animal, organ, culture vessel or cell; explain why technical repetitions cannot silently increase biological sample size.
3. Quantify the endpoint and one interval rate, explaining any limitations due to missing time units.
4. Identify two alternative causes of the same observed trajectory, including the principal confound listed above.
5. Propose a safe, noninfectious follow-up or computational analysis and choose a criterion that would change your preferred explanation.
6. Produce a short reproducibility note giving data schema, graph labels, analysis pseudocode and a statement that all values are fictional.


## Systems synthesis and examination preparation

An immune network changes across compartments and timescales. This unit links **Pattern-recognition receptors and danger signals**, **Cytokine networks and chemokine gradients**, **Neutrophil recruitment and phagocytosis**, **Complement activation and regulatory checkpoints** and **Interferons, inflammasomes and resolution**. Try placing these concepts in a table with columns for recognition, cellular actors, immediate output, delayed outcome, negative regulation and an assay limitation. Some rows will not fit neatly: the same mediator may promote clearance and also exacerbate injury. Treat that apparent contradiction as a clue about concentrations, timing and tissue specificity rather than a reason to ignore the mechanism.

To test integration, imagine two specimens showing the same final reporter value despite different early trajectories. In one, a small number of strongly responding cells drive the signal; in the other, a large number of weakly responding cells produce an equal bulk total. A single bulk assay cannot resolve those explanations. Which of this unit's five mechanisms could generate the two situations, and what independent measurement would discriminate them? For every proposed measurement, identify whether it estimates a concentration, frequency, absolute count, location, phenotype or function. Then articulate the assumption that makes the measurement relevant.

Transfer the explanation from a controlled cell system into an intact tissue. Tissue oxygen, access to antigen, migration routes and regulatory signals could all change the qualitative outcome even if receptor-level biochemistry remains the same. Do not silently treat a monotonic curve as an empirical law valid across species, tissues and developmental stages. If you use the interactive model, name one omitted interaction and describe how including it might shift the curve, introduce a delay, or reverse the predicted comparison. Sensitivity to an assumed parameter is useful for learning but cannot establish that the chosen parameter value matches biology.

### End-of-unit synthesis questions

- Use **pattern-recognition receptors and danger signals** and **interferons, inflammasomes and resolution** in one causal argument and identify where negative feedback could intervene.
- Present a competing hypothesis for a result initially attributed to **neutrophil recruitment and phagocytosis**. What measurement, with units, would favor one explanation?
- Explain how an apparent change in immune-cell frequency might arise with no change in absolute abundance of that population.
- Recompute one quantitative case with different assumptions and report which assumption contributes most to uncertainty.
- Choose a claim that would be dangerous to generalize into patient advice and explain why the available educational model cannot justify it.

**Editorial reminder:** The described scenarios are concept exercises, not real laboratory results. All clinical statements require authoritative evidence and, where applicable, qualified professional interpretation.
