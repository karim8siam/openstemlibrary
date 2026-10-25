# Unit 8: Cell investigation

## Introduction

Reliable cell biology requires measurements whose errors and selection effects are understood. Culture changes the biological context; microscopy creates spatially sampled signals; fractionation trades enrichment against recovery; and single-cell methods uncover heterogeneity while introducing their own capture biases. A powerful study often combines complementary methods: spatial imaging locates a candidate process, a biochemical assay tests function, and single-cell analysis asks which cells participate. An assay result is only as strong as its controls and denominator. This unit helps readers plan experiments, calculate interpretable quantities, and document measurements so that another scientist can reproduce both the procedures and the reasoning.



## 8.1 Culture systems

### Central mechanism and vocabulary

Cell culture places cells in a controllable environment that can reveal mechanisms but also selects for phenotypes adapted to artificial media and surfaces. Primary cultures, immortalized lines, organoids, and co-culture systems differ in lifespan, genetic variability, cellular composition, and physiological fidelity. Media composition, oxygen, substrate stiffness, passage number, and cell density influence behavior. Cultures are biological systems requiring authentication and contamination monitoring rather than interchangeable containers.

### Why this mechanism matters

The central issue in **culture systems** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cell culture places cells in a controllable environment that can reveal mechanisms but also selects for phenotypes adapted to artificial media and surfaces. Description and mechanism are not equivalent.

Consider a thought experiment involving **culture systems**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms. For this topic, examine the meaning of sample handling, eligibility gates, and biological replicate structure; ask which additional time point, reference marker, or independent assay would break the ambiguity. This is especially important because sample-selection effects can make population averages deceptively stable even when individuals change substantially.

### Mechanism from molecular to cellular scale

A mechanism for culture systems should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Cultures are biological systems requiring authentication and contamination monitoring rather than interchangeable containers.

### Experimental evidence and its interpretation

Design a growth assay using authenticated cells at defined initial densities, biological replicates, and recorded passage history. Measure both viable cells and total cells, and compare growth curves to imaging observations. Include a mycoplasma test and document medium lot, incubation conditions, and counting method before judging a treatment effect.

**Verify the assay.** Begin with a prespecified comparison that changes one primary factor and holds other plausible causes as constant as practicable. For culture systems, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on culture systems, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for culture systems.

### Competing explanations, limitations, and quality controls

A tumor-derived cell line may not represent its tissue of origin. High confluence changes metabolism and signaling; a difference between plates can arise from seeding error or edge evaporation rather than biology.

A persuasive conclusion about culture systems has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in culture systems after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A cell culture shows a shorter doubling interval after changing growth medium, yet a parallel viability assay reports no difference in survival. The investigator must check that the initial seeding densities were equal and that the new medium did not affect the measurement chemistry. If direct viable-cell counts agree with the apparent rate change, a growth effect is better supported, but passage-dependent selection could still influence results. Establish biological replicates from independent culture preparations and distinguish technical counting repeats from additional biological samples. Primary cells may senesce while immortalized cells continue to proliferate, so results from one line should not be generalized to all tissues. In the worked exercise a fourfold expansion over 48 hours gives a 24-hour doubling interval only under a constant exponential-rate assumption. The experiment should explicitly identify the time window where that approximation holds.


## 8.2 Imaging

### Central mechanism and vocabulary

Biological imaging maps a physical signal onto spatial or temporal measurements. Widefield fluorescence, confocal microscopy, live-cell reporters, electron microscopy, and label-free methods provide complementary contrast and resolution. A microscope image requires calibration, metadata, and an explanation of specimen preparation. Quantification involves segmentation, background correction, photobleaching assessment, and an explicit rule for selecting cells or regions. When fluorescence intensity is used as a proxy for molecule number, sensor saturation and photophysics constrain the interpretation.

### Why this mechanism matters

The central issue in **imaging** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Biological imaging maps a physical signal onto spatial or temporal measurements. Description and mechanism are not equivalent.

Consider a thought experiment involving **imaging**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for imaging should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: When fluorescence intensity is used as a proxy for molecule number, sensor saturation and photophysics constrain the interpretation.

### Experimental evidence and its interpretation

Perform fluorescence recovery after photobleaching with a defined region of interest, an unbleached reference region, and background subtraction. Fit a recovery curve, calculate half-time, and measure the mobile fraction separately if data permit. Repeat across cells and acquisition sessions rather than treating every time point in one cell as a biological replicate.

For imaging, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on imaging, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for imaging.

### Competing explanations, limitations, and quality controls

A fitted FRAP recovery rate depends on geometry and transport mechanisms, not solely a unique diffusion coefficient. Post-processing cannot restore information never collected, and aggressive image contrast can distort comparisons.

A persuasive conclusion about imaging has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in imaging after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A fluorescent protein recovers after a small circular region is photobleached. A fitted exponential produces a half-recovery time of 20 seconds. It is tempting to translate that one number into a unique molecular diffusion coefficient, but the result also depends on spot geometry, mobile fraction, binding, transport, and image acquisition. The laboratory varies the bleach-region radius and includes an unbleached reference area to correct for acquisition-associated bleaching. At least several independent cells are fitted and the distribution of parameter estimates is reported. If the recovery plateau remains below prebleach intensity, a nonrecovering component or finite observation time may be involved; a single-parameter 100%-recovery model cannot capture the full behavior. Students should explain which model assumptions can be tested by changing bleach geometry and which require a different kind of molecular tracking assay.


## 8.3 Fractionation

### Central mechanism and vocabulary

Cell fractionation separates components according to physical properties such as size, sedimentation rate, and density. Differential centrifugation can enrich nuclei, mitochondria, membranes, or soluble proteins, but enrichment is rarely absolute. Density gradients improve some separations at the cost of yield and time. Interpreting a fraction requires markers for target and contaminating compartments, recovery accounting, and awareness that disruptive lysis can change molecular complexes.

### Why this mechanism matters

The central issue in **fractionation** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cell fractionation separates components according to physical properties such as size, sedimentation rate, and density. Description and mechanism are not equivalent.

Consider a thought experiment involving **fractionation**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for fractionation should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Interpreting a fraction requires markers for target and contaminating compartments, recovery accounting, and awareness that disruptive lysis can change molecular complexes.

### Experimental evidence and its interpretation

Measure compartment-marker abundance in input, pellet, and supernatant after each step. Calculate both enrichment relative to a contaminant and mass recovery across fractions; a pure-looking pellet with tiny yield may not support downstream biochemical conclusions. Include a cytosolic marker to detect unintended organelle rupture.

For fractionation, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on fractionation, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for fractionation.

### Competing explanations, limitations, and quality controls

A protein detected in two fractions may be genuinely dual-localized, physically associated during lysis, or misassigned through contamination. Centrifuge speed should be reported as relative centrifugal force, not RPM alone, because rotor radii differ.

A persuasive conclusion about fractionation has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in fractionation after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A crude mitochondrial pellet contains a strong mitochondrial marker but also detectable ER-associated protein. Reporting that the pellet is purified mitochondria would overstate the evidence. A sequential centrifugation experiment measures concentrations and total recovered volumes for each fraction, then compares marker ratios with the original lysate. Higher target concentration does not automatically mean higher recovery because small pellet volume may contain only a fraction of the initial target. A density gradient can improve enrichment, but can lose fragile components or disrupt associations. A functional respiration assay provides a complementary readout but does not prove that every protein in the pellet is mitochondrial. Students should calculate both percent recovery and enrichment against a contaminant and then state what additional purity marker is needed before interpreting a biochemical interaction as intramitochondrial.


## 8.4 Single-cell methods

### Central mechanism and vocabulary

Single-cell measurements uncover heterogeneity hidden by bulk assays. Flow cytometry measures marker intensities and scatter on many events, whereas single-cell RNA sequencing profiles transcripts from individually captured cells or nuclei. Neither method directly measures every protein or function. Data processing requires quality filters, normalization, batch assessment, and attention to doublets and ambient RNA. Clustering is a computational summary, not proof of discrete natural cell types, and marker genes must be interpreted with tissue context.

### Why this mechanism matters

The central issue in **single-cell methods** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Single-cell measurements uncover heterogeneity hidden by bulk assays. Description and mechanism are not equivalent.

Consider a thought experiment involving **single-cell methods**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for single-cell methods should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Clustering is a computational summary, not proof of discrete natural cell types, and marker genes must be interpreted with tissue context.

### Experimental evidence and its interpretation

Analyze flow-cytometry gates using single-color and unstained controls, and report both fractions and absolute counts when available. For single-cell transcriptomics, inspect reads per cell, mitochondrial-read fraction, doublet estimates, and replicate mixing before assigning labels. Validate selected marker interpretations using an independent spatial or protein-level assay.

For single-cell methods, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on single-cell methods, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for single-cell methods.

### Competing explanations, limitations, and quality controls

Single-cell capture has selection bias: fragile or rare cells can be lost, and dissociation induces stress responses. A compact visualization such as UMAP cannot by itself establish lineage or causality; parameter settings alter apparent separation.

A persuasive conclusion about single-cell methods has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in single-cell methods after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A single-cell clustering plot displays two sharply separated groups, one expressing a signaling marker and the other a metabolic marker. The investigator claims discovery of two novel cell types. Yet dissociation time, batch effects, sequencing depth, and cell-cycle state may create apparent separation. A defensible workflow examines quality-control covariates, donor mixing, doublet detection, and the robustness of clustering across parameter choices. An independent in situ protein or RNA imaging experiment asks whether the proposed groups occupy distinct tissue niches. For flow cytometry, a marker-positive gate should be set from controls and reported with viable singlet denominators. A cluster is a computational summary of measured variation, not automatically a distinct developmental lineage. Students should be able to propose an orthogonal validation step and identify a biological interpretation that would remain unresolved even after a stable cluster is reproduced.


## Fully worked problems

### CB-U8-P1: Specific growth rate

**Question:** A cell culture grows from 1.0×10^5 to 4.0×10^5 viable cells in 48 h under ideal exponential conditions. Estimate its specific growth rate and doubling time.

- 1. Write N(t)=N0 e^(µt), so µ=ln(N/N0)/t.
- 2. Compute ln(4)/48≈1.38629/48=0.02888 h⁻¹.
- 3. Doubling time is ln(2)/µ≈0.69315/0.02888=24 h.
- 4. Check: two doublings in 48 hours give a fourfold change.
- 5. Do not fit a single exponential across lag, saturation, or substantial cell-death phases.

**Verified final result:** µ≈0.0289 h⁻¹; doubling time≈24 h

### CB-U8-P2: FRAP recovery half-time

**Question:** A normalized fluorescence recovery curve follows F(t)=1−exp(−kt), where k=0.035 s⁻¹. Find the half-recovery time.

- 1. Set F(t1/2)=0.5.
- 2. Then exp(−k t1/2)=0.5.
- 3. Taking natural logs gives t1/2=ln(2)/k.
- 4. Calculate 0.69315/0.035≈19.8 seconds.
- 5. The rate does not uniquely determine a diffusion coefficient without specifying geometry and model assumptions.

**Verified final result:** Approximately 19.8 s

### CB-U8-P3: Flow-cytometry gating

**Question:** A single-cell flow experiment acquires 12,000 quality-filtered single-cell events, and a predeclared marker gate contains 3,000 events. Estimate gated fraction and discuss interpretation.

- 1. Use fraction = gated events / total quality-filtered single-cell events.
- 2. Compute 3000/12000=0.25.
- 3. The gated population is 25% of the acquired eligible events.
- 4. Compensation, threshold selection, viability, and doublet exclusion determine which events enter this denominator.
- 5. Without absolute-count beads or a known sampled volume, 25% does not establish the absolute number of marker-positive cells in the source specimen.

**Verified final result:** 25% of quality-filtered events



## Integrative study: designing a reproducible cell-investigation workflow

A collaborating laboratory wants to compare a candidate drug's effect on trafficking in two cell lines. One team proposes measuring vesicle fluorescence, a second prefers subcellular fractionation, and a third proposes single-cell transcript profiling. These assays answer different questions; the purpose of a reproducible study is to join their evidence without confusing readouts. Begin by authenticating cell lines, recording passage number, and documenting culture conditions. Use the same drug batch and prespecified treatment interval across independent experimental days. Randomize plate position where possible to reduce edge effects and include blinded scoring for image-derived outcomes.

Imaging should quantify a declared feature: vesicle count per cell, fraction of reporter within a compartment mask, transit time, or fluorescence recovery. These choices have different denominators and biological interpretations. Calibrate imaging intensity, set segmentation rules from appropriate controls, and do not treat repeated image frames of one cell as independent biological replicates. A fluorescence-recovery experiment must account for the bleached-region geometry, acquisition bleaching, and mobile fraction; the fitted rate is not automatically a unique diffusion constant. A static image may establish localization without revealing flux.

Fractionation supplies complementary biochemical evidence. Differential centrifugation enriches compartments but usually produces mixed fractions. For every pellet and supernatant, measure target-marker abundance, contaminant markers, total protein mass, and recovery. Calculate enrichment and yield independently. A tiny but apparently clean pellet might represent only a small fraction of original target material; a high-yield fraction may be heavily contaminated. If drug treatment changes organelle fragility, the isolation procedure itself can shift measured composition. Use functional assays where available to determine whether the fraction retains the activity required by the hypothesis.

Single-cell methods can reveal whether a mean trafficking phenotype results from all cells or a distinct responder subpopulation. Flow-cytometry gates should follow quality filtering, viability checks, doublet exclusion, and controls for spectral compensation. A single-cell transcriptomics result must account for batch, sequencing depth, cell-cycle state, stress caused by dissociation, and ambient RNA. A clustering map by itself cannot prove a new cell type or a direct drug mechanism. An independent spatial assay can test whether the proposed population exists in its original context. The final integrated report should define each observation, list its principal assumptions, provide biological replicate counts, and show how the three methods constrain rather than duplicate one another.

## Unit synthesis and interpretation

The investigation module ends with a mock preregistration. State the biological hypothesis, primary endpoint, cell-line identity, biological replicate definition, exclusion criteria, and expected major confounders. One group will use time-lapse images, one will enrich organelles by centrifugation, and one will estimate a gated cell fraction from flow cytometry. Their results are related but not automatically numerically comparable. The imaging group must control photobleaching and segmentation; the fractionation group must report both yield and contamination; the flow group must state its gate and eligible-event denominator. When all groups report a statistically significant effect, students should still ask whether the assays measured the same event. A joint mechanism claim is stronger if the three methods predict coherent outcomes under a selective perturbation. If they disagree, the correct response is to investigate the discrepancy, not to discard an inconvenient measurement.

## Interactive model specifications

### FRAP recovery

**Question tested by the model:** how quickly does a normalized fluorescence recovery process approach its plateau? This simplified model uses F(t)=100[1−exp(−kt)] percent after instantaneous bleaching, implying t_half=ln(2)/k. At k=0.035 s⁻¹, half-recovery occurs after about 19.8 seconds. Moving the rate slider changes recovery speed; it does not change the assumed 100% mobile plateau. In an actual FRAP experiment, bleached-region geometry, immobile fraction, reversible binding, image acquisition, and reporter exchange can all affect the observed curve. The rate is not automatically a diffusion coefficient.

### Illustrative gating fraction

**Question tested by the model:** how can a marker threshold change the fraction of eligible cells classified as positive? The illustrative distribution is logistic with unit scale, giving percentage above threshold T as 100/[1+exp(T−µ)] for population location µ. At T=µ the fraction is 50%; raising the threshold reduces the gated fraction without changing any biological specimen. This is not a fit to flow-cytometry measurements. Real gating requires viability and singlet selection, compensation and unstained controls, and declared denominators. A high percentage is not an absolute cell count and can reflect gate choice or acquisition selection rather than a causal treatment effect.

