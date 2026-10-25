# Unit 05 — Cell movement, adhesion and morphogenesis

> **Book 10 — Developmental Biology.** How migration, proliferation, death and mechanics cooperate to change tissue shape.

## Learning outcomes and prerequisites

By the end of this unit, explain the central mechanisms without confusing a measured marker with a complete cell fate. Interpret a worked numerical example with appropriate units, design a control to separate two alternative causes, and identify the species, tissue and developmental stage to which the evidence applies. Prerequisites include basic cell biology, genetics, gene expression, membrane signaling and elementary mathematical modeling. Calculus and statistical reasoning strengthen the advanced exercises, but each quantitative example includes the numerical relationship used.

## Conceptual orientation

Embryonic shapes arise from collective cell decisions and material constraints. Adhesion changes who remains in contact; contractility changes forces across those contacts; proliferation adds volume; apoptosis removes cells; and migration or intercalation redistributes neighbors. These contributions can compensate for each other. A final tissue length is thus an outcome of several processes, not a direct measurement of any single one. The practical solution is to acquire movies and quantitative geometry alongside molecular readouts.
The path of a moving cell illustrates the measurement problem. Speed is traveled path divided by elapsed time. Net displacement is the straight-line separation of initial and final positions. Directional persistence, often approximated as displacement divided by path length, distinguishes purposeful travel from wandering. Two cells could move the same cumulative distance and arrive at very different final destinations. Three-dimensional movement needs appropriately spaced z-stacks; otherwise a cell can disappear from a focal plane and falsely be interpreted as a dead or stalled cell.
A mechanical experiment also demands care. When laser ablation cuts an epithelial junction, local recoil is affected by preexisting stress but also by viscosity and architecture. Recoil is therefore an informative proxy under an assumed material model, not a calibrated tensile-force measurement by itself. Similar caution applies to cell sorting: changing cadherin expression can alter adhesion, cell signaling and contractility simultaneously. To infer cause, investigators pair spatial perturbations with complementary measurements and explicit alternatives. Our simulated curves keep assumptions visible and never substitute for direct mechanical calibration.

## Five linked studies

### 5.1 Cell migration and collective guidance

#### Mechanism and biological context

Migrating cells polarize, generate traction and respond to chemical, mechanical or contact-based cues. Some developmental movements involve single cells; others rely on coordinated multicellular sheets or streams. Net displacement, instantaneous speed and directional persistence quantify different aspects of movement.

**Core question:** For **cell migration and collective guidance**, which intermediate molecular, cellular or mechanical event should precede the described phenotype? Distinguish identity changes from changes in cell number or position.

#### Comparative case and specific predictions

Cells with the same average speed can reach a target at different rates when directional persistence differs. Neighbor exchange within an epithelium can lengthen tissue without large migration of the whole cell sheet.

Identify the stage, the variable actually manipulated, and a proximal measurement that must change before the terminal outcome. A later difference arising only after tissue loss may be secondary rather than a direct specification defect.

#### Experimental intervention and measurement

Track centroid trajectories and neighbor contacts in time-lapse imaging. Calculate displacement, traveled path, speed and persistence for each cell.

Use a stage-matched control, report surviving specimens and define independent biological replicates. Combine an early readout with a later structural or lineage endpoint; report segmentation and fluorescence artifacts when relevant.

#### Worked numerical example 5.1

**Problem.** A migrating cell travels 420 micrometers in a 35-minute movie. Calculate mean path speed.

**Calculation.** Evaluate `420/35` = **12 micrometers per minute**. This is a worked teaching calculation using hypothetical inputs. Ratios, percentages and percentage-point differences are different quantities; verify dimensions and the chosen denominator before interpreting the number.

**Caution.** Path speed does not tell whether the cell moved toward a target. This arithmetic does not establish causality or sampling uncertainty.

#### Alternative explanations and scope

A two-dimensional tracking plane underestimates out-of-plane motion. Tracking errors and cell divisions can create artificial path discontinuities.

Make the next experiment discriminating: choose a readout whose predicted time course or spatial location differs across the two most plausible mechanisms. Explicitly restrict any conclusion to the measured species and stage.

#### Practice and transfer

1. Draw a diagram linking the proposed cause, intermediate response and phenotype in **cell migration and collective guidance**.
2. Specify a control and a measurement that distinguishes competing explanations.
3. Change one problem input by 10%, recompute and interpret the resulting unit.

### 5.2 Cell adhesion and tissue sorting

#### Mechanism and biological context

Cadherin-mediated adhesion, cortical tension and contact-dependent signaling help cells organize into layers and compartments. Differential adhesion can contribute to sorting, but active contractility, polarity and motility must also be considered. Tissue segregation cannot always be reduced to stickiness alone.

**Core question:** For **cell adhesion and tissue sorting**, which intermediate molecular, cellular or mechanical event should precede the described phenotype? Distinguish identity changes from changes in cell number or position.

#### Comparative case and specific predictions

Mixed aggregates of two labeled cell populations may segregate; changing cadherin expression may change the final configuration or the rate of sorting.

Identify the stage, the variable actually manipulated, and a proximal measurement that must change before the terminal outcome. A later difference arising only after tissue loss may be secondary rather than a direct specification defect.

#### Experimental intervention and measurement

Compare aggregate geometry, contact angles, cell motility and tension-sensitive measurements before and after perturbation.

Use a stage-matched control, report surviving specimens and define independent biological replicates. Combine an early readout with a later structural or lineage endpoint; report segmentation and fluorescence artifacts when relevant.

#### Worked numerical example 5.2

**Problem.** After mixing, 68 of 85 labeled cells reside in homotypic neighborhoods. Compute the homotypic-neighbor percentage.

**Calculation.** Evaluate `100*68/85` = **80 percent**. This is a worked teaching calculation using hypothetical inputs. Ratios, percentages and percentage-point differences are different quantities; verify dimensions and the chosen denominator before interpreting the number.

**Caution.** The metric depends on neighborhood definition and cell density. This arithmetic does not establish causality or sampling uncertainty.

#### Alternative explanations and scope

A static final image may not distinguish differential adhesion from active migration. Overexpression can induce nonphysiological receptor levels.

Make the next experiment discriminating: choose a readout whose predicted time course or spatial location differs across the two most plausible mechanisms. Explicitly restrict any conclusion to the measured species and stage.

#### Practice and transfer

1. Draw a diagram linking the proposed cause, intermediate response and phenotype in **cell adhesion and tissue sorting**.
2. Specify a control and a measurement that distinguishes competing explanations.
3. Change one problem input by 10%, recompute and interpret the resulting unit.

### 5.3 Oriented divisions and anisotropic growth

#### Mechanism and biological context

Spindle orientation and spatial regulation of proliferation affect tissue shape. Dividing cells may contribute to growth along a particular axis or exchange neighbors without large global size changes. Mechanical feedback can align mitotic orientation with tissue stress, although this relationship is not universal.

**Core question:** For **oriented divisions and anisotropic growth**, which intermediate molecular, cellular or mechanical event should precede the described phenotype? Distinguish identity changes from changes in cell number or position.

#### Comparative case and specific predictions

Two epithelia with equal total divisions may form different shapes if division planes and intercalations are distributed differently.

Identify the stage, the variable actually manipulated, and a proximal measurement that must change before the terminal outcome. A later difference arising only after tissue loss may be secondary rather than a direct specification defect.

#### Experimental intervention and measurement

Track mitotic spindle angles, tissue strain and lineages in three-dimensional images. Control for stage and cell-cycle effects.

Use a stage-matched control, report surviving specimens and define independent biological replicates. Combine an early readout with a later structural or lineage endpoint; report segmentation and fluorescence artifacts when relevant.

#### Worked numerical example 5.3

**Problem.** In an epithelium, 45 mitoses occur and 12 apoptotic events occur over an imaging period. Estimate net cell-event balance.

**Calculation.** Evaluate `45-12` = **33 net cell events**. This is a worked teaching calculation using hypothetical inputs. Ratios, percentages and percentage-point differences are different quantities; verify dimensions and the chosen denominator before interpreting the number.

**Caution.** Immigration, delamination and nonuniform cell-cycle timing also change counts. This arithmetic does not establish causality or sampling uncertainty.

#### Alternative explanations and scope

Counts of mitoses are not a direct measure of net growth, because apoptosis, cell extrusion and changes in volume also matter.

Make the next experiment discriminating: choose a readout whose predicted time course or spatial location differs across the two most plausible mechanisms. Explicitly restrict any conclusion to the measured species and stage.

#### Practice and transfer

1. Draw a diagram linking the proposed cause, intermediate response and phenotype in **oriented divisions and anisotropic growth**.
2. Specify a control and a measurement that distinguishes competing explanations.
3. Change one problem input by 10%, recompute and interpret the resulting unit.

### 5.4 Programmed cell death and sculpting

#### Mechanism and biological context

Apoptosis removes cells in a regulated manner and can shape structures, refine connections and eliminate transient tissues. Local differences in proliferation and apoptosis determine net population change. Morphological loss does not always imply apoptosis; cell migration and tissue remodeling can yield similar appearances.

**Core question:** For **programmed cell death and sculpting**, which intermediate molecular, cellular or mechanical event should precede the described phenotype? Distinguish identity changes from changes in cell number or position.

#### Comparative case and specific predictions

Interdigital tissue remodeling illustrates the coordination of cell death and digit separation in particular tetrapods; mechanisms and extent vary among species.

Identify the stage, the variable actually manipulated, and a proximal measurement that must change before the terminal outcome. A later difference arising only after tissue loss may be secondary rather than a direct specification defect.

#### Experimental intervention and measurement

Score cell-death markers and live cell trajectories in the same time series while separately tracking proliferation and tissue volume.

Use a stage-matched control, report surviving specimens and define independent biological replicates. Combine an early readout with a later structural or lineage endpoint; report segmentation and fluorescence artifacts when relevant.

#### Worked numerical example 5.4

**Problem.** A patterned interdigital area declines from 3.4 square millimeters to 2.3 square millimeters. Find proportional area loss.

**Calculation.** Evaluate `100*(3.4-2.3)/3.4` = **32.3529 percent**. This is a worked teaching calculation using hypothetical inputs. Ratios, percentages and percentage-point differences are different quantities; verify dimensions and the chosen denominator before interpreting the number.

**Caution.** Area loss is not a direct count of apoptotic cells. This arithmetic does not establish causality or sampling uncertainty.

#### Alternative explanations and scope

One apoptosis marker may detect stress or late-stage damage without uniquely establishing its cause. Blocking apoptosis can cause compensatory tissue responses.

Make the next experiment discriminating: choose a readout whose predicted time course or spatial location differs across the two most plausible mechanisms. Explicitly restrict any conclusion to the measured species and stage.

#### Practice and transfer

1. Draw a diagram linking the proposed cause, intermediate response and phenotype in **programmed cell death and sculpting**.
2. Specify a control and a measurement that distinguishes competing explanations.
3. Change one problem input by 10%, recompute and interpret the resulting unit.

### 5.5 Mechanical forces and morphogenesis

#### Mechanism and biological context

Epithelial folding, constriction, elongation and buckling depend on active cellular forces and passive material properties. Actomyosin networks generate contractility while extracellular matrix and neighboring tissues provide resistance. Mechanical stresses can also alter signaling and gene expression, producing mechanochemical feedback.

**Core question:** For **mechanical forces and morphogenesis**, which intermediate molecular, cellular or mechanical event should precede the described phenotype? Distinguish identity changes from changes in cell number or position.

#### Comparative case and specific predictions

Reducing apical contractility can flatten a furrow even when positional gene expression is initially intact. Increasing tissue stiffness may change fold geometry without altering signaling source.

Identify the stage, the variable actually manipulated, and a proximal measurement that must change before the terminal outcome. A later difference arising only after tissue loss may be secondary rather than a direct specification defect.

#### Experimental intervention and measurement

Use live shape measurements, local laser ablation where appropriate, and perturbations of myosin activity. Compare shape trajectories to force-model predictions.

Use a stage-matched control, report surviving specimens and define independent biological replicates. Combine an early readout with a later structural or lineage endpoint; report segmentation and fluorescence artifacts when relevant.

#### Worked numerical example 5.5

**Problem.** A curved sheet's width changes by 18 micrometers from a 120 micrometer baseline. Calculate engineering strain.

**Calculation.** Evaluate `18/120` = **0.15 unitless**. This is a worked teaching calculation using hypothetical inputs. Ratios, percentages and percentage-point differences are different quantities; verify dimensions and the chosen denominator before interpreting the number.

**Caution.** Strain calculated from width does not identify active or passive force sources. This arithmetic does not establish causality or sampling uncertainty.

#### Alternative explanations and scope

Laser recoil is an indirect indicator that depends on viscosity and geometry. A fitted physical model is not proof of one specific molecular force generator.

Make the next experiment discriminating: choose a readout whose predicted time course or spatial location differs across the two most plausible mechanisms. Explicitly restrict any conclusion to the measured species and stage.

#### Practice and transfer

1. Draw a diagram linking the proposed cause, intermediate response and phenotype in **mechanical forces and morphogenesis**.
2. Specify a control and a measurement that distinguishes competing explanations.
3. Change one problem input by 10%, recompute and interpret the resulting unit.

## Integrated investigation 5 — Cell movement, adhesion and morphogenesis

### Scientific question and candidate mechanisms

**Research question:** Can cell trajectory data distinguish directed migration from rapid random movement?

This investigation uses **synthetic data and conceptual experiments only**. The reader is not asked to conduct embryo manipulation, genetic intervention or laboratory work without suitable supervision, approvals and resources. The goal is to practice framing measurable alternatives. Begin by proposing at least two causal routes that could lead to a superficially similar pattern. For example, a change in a final anatomical marker could be caused by altered identity acquisition, altered cell survival, migration to a new location, changes in proliferation, differential reporter expression or delayed development. Choose alternatives that predict a measurably different temporal sequence rather than vague claims that “many factors” might matter.

### Variables, units and sampling design

The primary observables are **Stepwise displacement vectors, cumulative path, net displacement, neighbor exchanges**. Define an exact operational rule for each variable: what observation counts as positive, what unit it is measured in, and when the observation is made. State the inclusion and exclusion criteria for embryos or cultures before inspection of outcomes. Do not switch the denominator from all embryos to only surviving embryos without displaying both. If the observation is a proportion, give its numerator and denominator; if it is fluorescence intensity, include a calibration or background-subtraction plan. Biological replication should be described in terms of independently treated specimens or batches; additional fields of view support precision of measurement but may not supply independent interventions.

**Perturbation strategy:** Analyze simulated traces with matched path lengths but different directional persistence

In a real study, stage-match intervention groups and check instrument stability. Treat interventions that also alter tissue survival, stiffness or position as potential multiple-pathway manipulations. For a pilot design, use more than one readout and include an appropriate blank, sham or untreated comparison. Keep a full record of staging criteria, conditions, imaging settings and the analysis version that produced each figure.

### Reproducible procedure

Download the [synthetic dataset for Unit 5](datasets/lab-05.csv) to practice the suggested analysis. Every row is invented for teaching, not a laboratory measurement.

1. Construct trajectories with equal traveled lengths but different turning angles.
2. Compute path length, net displacement and persistence, checking micrometer per minute units.
3. Downsample the same tracks to test whether sampling frequency biases the estimated metrics.
4. Create a tidy dataset with one row per independent specimen per recorded stage; if measurements are nested, use a separate linked table for individual cells. Record missing observations explicitly rather than coding them as zeros.
5. Graph each specimen trajectory and the group-level summary with units on both axes. Where the model is deterministic, show the assumed equation and parameters instead of drawing a misleading empirical confidence ribbon around invented data.
6. Perform a sensitivity analysis: vary one uncertain parameter or threshold, recalculate the headline result and report whether the conclusion is robust to plausible measurement choices.

### Example interpretation and competing explanations

A visibly different experimental curve is not sufficient to identify the molecular or mechanical cause of the change. Specifically, **Projection into two dimensions and mistaken cell identity can alter tracks and inflate speed**. Build a claim-evidence-alternative table in which every claim is paired with its measurement, an independent verification, and one rival mechanism. Ask whether that rival mechanism could fit the data without violating any observation. If it can, add a new observation or intervention whose expected outcomes differ. This is especially important for developmental systems where stage, tissue position and cell composition change simultaneously.

When reporting a fitted model, give the equation, parameter units and the range over which it was applied. A fitted curve can be useful for interpolation but may mislead when extrapolated to a different species, stage or organ. All provided teaching-model curves are phenomenological unless otherwise stated; their numerical parameters were chosen to illustrate reasoning, not derived from a biological dataset. Resist reporting highly precise outputs when the input values are hypothetical or approximate. A sensible result paragraph describes the direction and possible magnitude of change while making its inferential limits explicit.

### Deliverables and review questions

**Required deliverable:** Plot tracks, calculate speed and persistence, and specify required imaging cadence.

Write a one-page experimental plan with a prespecified outcome, a data dictionary, a valid replicate definition, a proposed graph and two plausible confounders. Provide a concise result paragraph using the synthetic table or teaching simulation, but do not claim that a real organism has been experimentally tested. Explain which inference would still require a direct biological experiment. A reader should be able to reproduce the arithmetic and disagree constructively about the interpretation by referring to the same data and assumptions.

## Unit 5 synthesis and peer-review checklist

In **cell movement, adhesion and morphogenesis**, the progression from **cell migration and collective guidance** to **mechanical forces and morphogenesis** should not be read as an inflexible sequence of independent modules. Developmental systems contain feedback: early fate decisions alter later cell contacts, while movement, growth and environmental context can reshape the signaling landscape that originally produced those fates. An explanatory account must therefore connect a chosen observation to its time-resolved predecessors. If the proposed explanation is purely genetic, ask what spatial information is missing. If it is purely mechanical, ask how forces became localized in the first place. If it is purely observational, specify the manipulation that could distinguish causation from correlation.

Trajectories and strains establish how shapes change; they do not independently reveal the stresses that produced the motion. Mechanical perturbations must be matched to stage, geometry and tissue integrity. A model parameter such as effective stiffness is often inferred rather than measured; its precision should not be exaggerated.

**Audit the unit's quantitative work:** for each of the five examples, list the formula, raw hypothetical inputs, result, units and a measurement that could change the answer. Compare absolute difference, relative change and dimensionless ratios without treating them as synonyms. The models are useful if they clarify assumptions and yield testable predictions, not because their outputs appear precise. Biological extrapolation requires stage-specific, species-specific validation, while statistical inference requires appropriate replicate-level data. Avoid the appearance of evidence by clearly labeling synthetic values at every step.

**Challenge assignment:** Prepare two mutually competing explanations for a hypothetical phenotype in this unit. Outline one imaging or perturbation experiment capable of distinguishing them, describe how many independent specimens would be needed and how that number should be justified by a pilot or power analysis, and name one plausible failure mode in image segmentation or lineage identification. Present a figure legend that could accompany the experiment without overstating its conclusions. Conclude with the exact observation that would cause you to revise your preferred mechanism.

## Check your understanding

- What is the earliest developmental event measured directly in the strongest argument in this unit, and what later outcome does it predict?
- Which comparison relies on a chosen model rather than a directly observed mechanism, and how would you test that model?
- What additional evidence is necessary to translate a result from the featured model species to a different species or human developmental context?
- How could altered sample selection, incomplete survival reporting or incorrect replication change the interpretation of the numerical examples?
