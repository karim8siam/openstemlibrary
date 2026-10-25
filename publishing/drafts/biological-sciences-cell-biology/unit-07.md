# Unit 7: Cellular stress

## Introduction

Cell stress is a decision-making problem with competing possible outcomes. A cell can repair damage, degrade compromised components, arrest proliferation, adapt its metabolism, enter senescence, or undergo a regulated death program. The same molecular marker may accompany more than one outcome, and a decline in that marker can reflect recovery, selection, or loss of cells. This unit emphasizes experiments with longitudinal tracking, functional recovery, and multiple markers. Mathematical response curves illustrate thresholds and clearance kinetics, but readers must avoid turning an arbitrary normalized signal into a clinical probability or interpreting a simplified half-life as a complete recycling pathway.



## 7.1 Apoptosis

### Central mechanism and vocabulary

Apoptosis is a coordinated regulated cell-death program involving caspase proteases and characteristic changes such as controlled cell fragmentation, with multiple initiation routes. Intrinsic signaling can integrate mitochondrial outer-membrane permeabilization and apoptosome activity; extrinsic pathways can involve death receptors. Executioner caspase activation often produces a switch-like commitment in simplified models, but pathways interact with survival signaling and alternative death processes. Apoptotic bodies can be cleared by phagocytes with limited inflammatory release in appropriate contexts.

### Why this mechanism matters

The central issue in **apoptosis** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Apoptosis is a coordinated regulated cell-death program involving caspase proteases and characteristic changes such as controlled cell fragmentation, with multiple initiation routes. Description and mechanism are not equivalent.

Consider a thought experiment involving **apoptosis**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms. For this topic, examine the meaning of acute marker activity and long-term viable descendants; ask which additional time point, reference marker, or independent assay would break the ambiguity. This is especially important because loss of high-signal cells can make population averages deceptively stable even when individuals change substantially.

### Mechanism from molecular to cellular scale

A mechanism for apoptosis should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Apoptotic bodies can be cleared by phagocytes with limited inflammatory release in appropriate contexts.

### Experimental evidence and its interpretation

Measure caspase activity with a validated reporter alongside morphology and membrane-integrity markers over time. Use an inhibitor or a genetic perturbation and quantify whether cells survive long-term, not merely whether one caspase signal declines. Distinguish apoptosis from necrosis using multiple independent readouts.

**Distinguish stress from fate.** Begin with a prespecified comparison that changes one primary factor and holds other plausible causes as constant as practicable. For apoptosis, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on apoptosis, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for apoptosis.

### Competing explanations, limitations, and quality controls

A single Annexin V or fluorescent caspase readout cannot universally establish death mechanism. Caspase inhibition may divert a cell to another death pathway, and a high-dose insult can bypass regulated dynamics.

A persuasive conclusion about apoptosis has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in apoptosis after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A compound produces a high caspase-reporter signal in a cell population after four hours. The researcher labels the compound an apoptosis inducer and reports the percentage of bright cells as the death fraction. However, reporter cleavage can precede or sometimes occur without immediate loss of cell viability; bright cells can also vanish from later measurements because of detachment. A stronger experiment tracks single-cell reporter trajectories, plasma-membrane integrity, morphology, and long-term survival after washout. A selective genetic perturbation of an initiating pathway helps differentiate routes to caspase activity. The interactive Hill response is deliberately called a normalized stress-response model, not a patient-specific or experimentally calibrated death probability. Students should identify which experimentally measured quantity would justify every word of a claimed biological outcome.


## 7.2 Autophagy

### Central mechanism and vocabulary

Macroautophagy encloses cytoplasmic cargo within double-membrane autophagosomes that subsequently fuse with lysosomes for degradation. It supports quality control and resource recycling and can be selective for damaged mitochondria or aggregates. Counting autophagic vesicles is not the same as measuring autophagic flux: more puncta can reflect increased formation or blocked degradation. Nutrient-sensing systems regulate initiation, but different cell types prioritize different cargoes and signaling branches.

### Why this mechanism matters

The central issue in **autophagy** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Macroautophagy encloses cytoplasmic cargo within double-membrane autophagosomes that subsequently fuse with lysosomes for degradation. Description and mechanism are not equivalent.

Consider a thought experiment involving **autophagy**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for autophagy should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Nutrient-sensing systems regulate initiation, but different cell types prioritize different cargoes and signaling branches.

### Experimental evidence and its interpretation

Measure a tandem pH-sensitive autophagy reporter across time and compare conditions with and without a lysosomal degradation block. Quantify reporter turnover as well as puncta number. Include controls for reporter expression and lysosomal pH; a fluorescent change can reflect acidification rather than actual clearance.

For autophagy, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on autophagy, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for autophagy.

### Competing explanations, limitations, and quality controls

Autophagy can be protective, neutral, or associated with cell death depending on circumstances. The simple exponential-clearance model used in exercises assumes first-order degradation of one well-mixed cargo pool and does not capture vesicle formation and maturation.

A persuasive conclusion about autophagy has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in autophagy after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A fluorescent autophagy marker becomes concentrated into puncta after cells are starved. More puncta could indicate enhanced autophagosome formation or failure to clear those compartments. The laboratory measures cargo degradation over time and compares the response with and without a lysosomal maturation block. A pH-sensitive tandem reporter helps distinguish early structures from acidified later compartments, but fluorophore quenching must be calibrated. In a clearance exercise a constant half-life creates a simple exponential decline; actual autophagic flux includes cargo capture, enclosure, transport, fusion, and enzymatic hydrolysis. Students should draw a compartment diagram and ask which rate change increases a static punctum count while reducing total degradation. The correct interpretation connects flux with inventory, whereas reliance on one bright image can reverse the apparent direction of the process.


## 7.3 Senescence

### Central mechanism and vocabulary

Cellular senescence describes a relatively stable withdrawal from proliferation accompanied by altered metabolism, chromatin, signaling, and often secretory activity. It can arise in response to replicative history, oncogenic stress, or damage. Senescent cells are heterogeneous and should not be defined solely by one enzyme stain or flattened morphology. Tissue effects depend on cell abundance, inflammatory context, and clearance mechanisms. Distinguishing senescence from quiescence requires attention to durability of arrest and molecular state.

### Why this mechanism matters

The central issue in **senescence** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cellular senescence describes a relatively stable withdrawal from proliferation accompanied by altered metabolism, chromatin, signaling, and often secretory activity. Description and mechanism are not equivalent.

Consider a thought experiment involving **senescence**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for senescence should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Distinguishing senescence from quiescence requires attention to durability of arrest and molecular state.

### Experimental evidence and its interpretation

Combine EdU incorporation, cell-cycle entry after release from stress, and a panel of senescence-associated markers. Compare the same lineage at several recovery times and report cell loss. Use a controlled low-stress group because strong insults can kill cells before a stable senescent state can develop.

For senescence, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on senescence, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for senescence.

### Competing explanations, limitations, and quality controls

Senescence-associated beta-galactosidase activity may also increase in other contexts; it is supportive but not definitive. Apparent lack of proliferation in a short movie cannot distinguish slow cycling from permanent arrest.

A persuasive conclusion about senescence has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in senescence after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A culture stopped dividing after an oxidative insult and has elevated lysosomal enzyme staining. The investigator proposes senescence, but quiescence or an unusually slow cell cycle could explain a short-term absence of mitosis. The study therefore removes the stressor, restores mitogenic conditions, and observes whether cells resume cycling over a prespecified interval. Alongside a proliferation assay, investigators check chromatin-associated markers, secreted factors, and morphology in individual cells. If many high-marker cells die during recovery, the surviving population's low proliferation rate cannot be interpreted without accounting for attrition. The distinction between stable arrest, reversible inactivity, and cell death matters because these states have different consequences in development, aging, and disease. A responsible report describes the combination of markers and functional tests used instead of asserting that any one stain uniquely defines senescence.


## 7.4 Repair

### Central mechanism and vocabulary

Cells detect molecular damage and restore function through repair, replacement, removal, and sometimes compensatory remodeling. DNA repair pathways address different lesion classes; proteins can be refolded, degraded, or replaced; membranes can undergo local resealing. A repair signal can be activated without successful repair. Cells weigh repair against cell-cycle arrest, differentiation, and death. The outcome depends on lesion burden, metabolic resources, tissue environment, and time for recovery.

### Why this mechanism matters

The central issue in **repair** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cells detect molecular damage and restore function through repair, replacement, removal, and sometimes compensatory remodeling. Description and mechanism are not equivalent.

Consider a thought experiment involving **repair**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for repair should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: The outcome depends on lesion burden, metabolic resources, tissue environment, and time for recovery.

### Experimental evidence and its interpretation

Induce a precisely timed low-level stress and follow an independent functional endpoint after washout. For DNA damage, quantify lesion-specific markers together with genomic integrity and subsequent divisions; for membrane injury, monitor dye exclusion and survival. Fit clearance kinetics cautiously because marker disappearance may reflect protein turnover rather than lesion elimination.

For repair, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on repair, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for repair.

### Competing explanations, limitations, and quality controls

Repair should not be conflated with tolerance: a cell may survive while retaining a defect. Rapidly returning fluorescence does not alone establish structural restoration, and population averages can hide selective death of the most damaged cells.

A persuasive conclusion about repair has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in repair after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

Following a low-dose genotoxic challenge, fluorescence of a DNA-damage marker rises sharply and then returns to baseline. Successful repair is possible, but marker disappearance might represent dephosphorylation, redistribution, or selective loss of damaged cells. A combined study records cell lineage survival, lesion-specific measurements, and downstream replication competence. The investigator calibrates the marker's dynamic range and compares samples with a repair-deficient positive control. A cell may tolerate damage without restoring the original sequence or structure; conversely, a cell may repair lesions but remain arrested while other stresses persist. Students are asked to write two distinct hypotheses with the same marker time course and propose a measurement that separates them. This exercise highlights the danger of treating molecular signal decay as equivalent to functional restoration.


## Fully worked problems

### CB-U7-P1: Apoptosis-like threshold model

**Question:** Use a Hill-style stress response f=s^4/(K^4+s^4). Find f at s=2K and explain why it is not a literal cell-death probability without calibration.

- 1. Write s=2K, giving s^4=16K^4.
- 2. Substitute f=16K^4/(K^4+16K^4).
- 3. Cancel K^4 to obtain f=16/17.
- 4. Numerically this is approximately 0.9412, or 94.1% of the modeled maximum response.
- 5. A caspase-reporter signal, committed-death fraction, and long-term survival are different biological endpoints.

**Verified final result:** 94.1% of the illustrative maximal response

### CB-U7-P2: Cargo clearance half-life

**Question:** In an idealized first-order intracellular clearance experiment, damaged cargo has half-life 3 h. What fraction remains after 9 h?

- 1. Nine hours is three half-life intervals when the half-life is constant.
- 2. Use C/C0=(1/2)^(t/t1/2).
- 3. Substitute (1/2)^(9/3)=(1/2)^3=1/8.
- 4. The remaining fraction is 0.125, or 12.5%.
- 5. Loss of reporter fluorescence may involve photobleaching or cell division; independent cargo mass measurements distinguish those effects.

**Verified final result:** 12.5% remains

### CB-U7-P3: Marker disappearance versus repair

**Question:** A population has 500 damage-marker-positive cells at t=0 and 200 after treatment. Calculate the percent reduction; identify why this is not a repair-efficiency estimate.

- 1. The absolute change is 500−200=300 marker-positive cells.
- 2. Divide by baseline: 300/500=0.60.
- 3. The marker-positive count fell by 60%.
- 4. But the denominator may have changed if cells died, detached, diluted a label, or divided.
- 5. Repair efficiency needs an independent lesion-specific or functional endpoint, plus viable-cell and recovery counts.

**Verified final result:** 60% reduction in marker-positive count, not necessarily 60% repair



## Integrative study: stress response without assuming a single cell fate

A brief oxidative-stress pulse induces a transient molecular reporter and reduces viable cell counts after 24 hours. Some surviving cells show increased autophagy markers, while a smaller subset no longer re-enters the cell cycle. Does the stress predominantly cause apoptosis, senescence, repair, or adaptation? The correct question recognizes that the population can contain multiple fates with different histories. A bulk reporter curve cannot reveal whether most cells recovered slightly or whether a minority generated a very large signal before dying. Time-resolved single-cell tracking can connect early marker dynamics to later viability, division, and morphology.

For the first stage, choose two independent reporters that distinguish a regulated death program from generic membrane damage. A caspase-based reporter can be useful, but it should be paired with a second endpoint such as membrane integrity, nuclear morphology, or long-term survival. An idealized fourth-order Hill function can illustrate a switch-like response to a normalized stress input, but students must not interpret the output as a calibrated death probability. Dose, exposure duration, and cellular metabolic condition may all change the observed transition. Fit a curve only to the measured quantity and state its unit.

For the second stage, follow turnover of a damaged cytoplasmic cargo. A single exponential with a measured half-life summarizes one effective clearance rate. However, autophagic flux includes sequestration, maturation, delivery to lysosomes, and degradation; a rise in puncta may mean more formation or slower destruction. Introduce a lysosomal block condition and test whether cargo degradation changes. Fluorescence quenching and cell dilution can mimic reporter loss, so an independent mass or immunochemical assay strengthens the conclusion. A cell can also reduce damaged cargo by eliminating the entire cell, which complicates population measurements.

Finally, test arrest reversibility. Cells that fail to divide immediately after stress might be quiescent, senescent, damaged, or dying. Apply recovery conditions and monitor multiple cycles, while recording the cells lost from observation. DNA damage-marker disappearance should be assessed against a functional recovery assay, not accepted as automatic proof of repair. The capstone report should present a branching fate diagram and estimate uncertainties on each fate proportion. It should openly acknowledge that experimental markers overlap and that precise mechanistic classification sometimes remains unresolved despite informative measurements.

## Unit synthesis and interpretation

The stress module closes with a branching outcome table. A cell exposed to damage might restore molecular function, permanently exit the cell cycle, activate a death program, or survive with a persistent defect. A temporary caspase signal is not interchangeable with a committed-death fraction; punctate autophagy marker abundance is not equivalent to total degradation; marker disappearance is not repair efficiency. Challenge students to design a pulse-chase experiment in which damaged cargo declines while viable cell number also declines. They must determine whether fluorescence loss reflects degradation inside surviving cells or disappearance of the most damaged cells. Normalizing to remaining cells changes the denominator and may reverse an apparent effect. Longitudinal fate mapping, viability endpoints, and marker-specific controls are required to distinguish these possibilities. The final report should acknowledge mixed cellular responses rather than inventing a single fate for every member of a heterogeneous population.

## Interactive model specifications

### Normalized stress-response switch

**Question tested by the model:** how sharply can a normalized cellular response rise around a threshold? The output is 100s^4/(K^4+s^4), with stress input s and threshold scale K. At s=2K, the output is 94.1% of the model maximum. The fourth power creates a relatively steep response and makes threshold changes visually interpretable. The percent on the plot is an illustrative reporter response; it is *not* a calibrated probability of apoptosis, caspase activation in a specified experiment, or patient risk. Establish those relationships independently using validated cell-fate measurements.

### First-order cargo clearance

**Question tested by the model:** how does a fixed half-life translate into loss of a tracked cargo pool? The remaining percent is 100×2^(−t/t_half), so three half-lives leave 12.5% of the starting amount. For t=9 h and half-life 3 h, this is the plotted baseline. An increased measured fluorescent signal despite cargo clearance could reflect new cargo production, maturation of reporter fluorescence, or changed imaging conditions. Real autophagy requires formation, trafficking, lysosomal fusion, and degradation steps that are not resolved by this one-pool first-order approximation.

