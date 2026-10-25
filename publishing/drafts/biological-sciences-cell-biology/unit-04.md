# Unit 4: Cell signaling

## Introduction

A signaling pathway maps a transient external or internal cue into a measurable response. Receptor occupation, messenger concentration, kinase state, gene expression, and final cell behavior are different quantities connected by regulated processes. The same occupied receptor fraction may evoke different outputs because of amplification, spare receptors, feedback, and adaptation. This unit uses equilibrium occupancy models, nonlinear transfer functions, and simplified dynamical systems to clarify those distinctions. The equations are deliberately minimal. Their primary purpose is to make a testable prediction and reveal when the observed data require another component, not to reconstruct all molecular states from one curve.



## 4.1 Receptors

### Central mechanism and vocabulary

Cells detect extracellular ligands through receptors that convert binding into altered intracellular behavior. Receptor occupancy depends on free ligand concentration and binding affinity, but signaling output depends also on receptor abundance, clustering, trafficking, and downstream amplification. A simple one-site equilibrium binding model yields an occupied fraction L/(Kd+L); that fraction is not automatically the fraction of maximum transcription or calcium response. Some receptors act through ion channels, G proteins, kinase domains, or regulated proteolysis. Ligand identity matters because antagonists, partial agonists, and biased ligands may stabilize different conformational outcomes.

### Why this mechanism matters

The central issue in **receptors** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Cells detect extracellular ligands through receptors that convert binding into altered intracellular behavior. Description and mechanism are not equivalent.

Consider a thought experiment involving **receptors**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms. For this topic, examine the meaning of the upstream perturbation and downstream state variable; ask which additional time point, reference marker, or independent assay would break the ambiguity. This is especially important because measurement-induced disturbance can make population averages deceptively stable even when individuals change substantially.

### Mechanism from molecular to cellular scale

A mechanism for receptors should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Ligand identity matters because antagonists, partial agonists, and biased ligands may stabilize different conformational outcomes.

### Experimental evidence and its interpretation

Quantify fluorescent ligand binding across a concentration series after nonspecific-background subtraction. In parallel, measure a downstream reporter, keeping time after stimulation constant. Compare the apparent EC50 for the reporter with the binding Kd to detect amplification or spare-receptor behavior.

**Write the causal chain.** Begin with a prespecified comparison that changes one primary factor and holds other plausible causes as constant as practicable. For receptors, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on receptors, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for receptors.

### Competing explanations, limitations, and quality controls

Fluorescence intensity can be affected by ligand internalization and receptor recycling. The Hill coefficient from a fitted response should not be presented as direct proof of molecular binding-site number.

A persuasive conclusion about receptors has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in receptors after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A receptor binds a ligand with a measured dissociation constant near 10 nM, yet a transcriptional reporter reaches half-maximal output below 1 nM. That difference does not automatically imply a bad binding assay. Amplification and receptor reserve can allow substantial downstream response when only a subset of surface receptors are occupied. An experiment measures surface receptor number, fluorescent ligand occupancy, and reporter induction at matched time points. If the receptor internalizes, the free surface pool changes during measurement, and a simple equilibrium binding equation may not apply. A competitive antagonist can shift the curve but may also have ligand-independent effects. The most rigorous interpretation compares binding and function as related but nonidentical outputs and explicitly tests whether the observed response is reversible after ligand washout.


## 4.2 Second messengers

### Central mechanism and vocabulary

Many signaling pathways generate diffusible intracellular intermediates, including cyclic AMP, calcium ions, diacylglycerol, and inositol phosphates. A signal may start as receptor activation and become a spatially and temporally restricted wave of messenger activity. Calcium responses depend on stores, channels, buffers, extrusion, and sensor kinetics; a transient peak can be larger even when integrated exposure is lower. Feedback and scaffold proteins help direct a shared messenger toward particular outputs. Signal termination is an essential feature: phosphodiesterases degrade cAMP, phosphatases reverse phosphorylation, and pumps restore ionic gradients.

### Why this mechanism matters

The central issue in **second messengers** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Many signaling pathways generate diffusible intracellular intermediates, including cyclic AMP, calcium ions, diacylglycerol, and inositol phosphates. Description and mechanism are not equivalent.

Consider a thought experiment involving **second messengers**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for second messengers should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Signal termination is an essential feature: phosphodiesterases degrade cAMP, phosphatases reverse phosphorylation, and pumps restore ionic gradients.

### Experimental evidence and its interpretation

Image a calibrated calcium reporter at adequate temporal sampling after a controlled agonist pulse. Compare peak, time-to-peak, and area under the response curve, not just one arbitrary time point. Use a nonresponsive control and correct for reporter bleaching; make an explicit model for rise and clearance.

For second messengers, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on second messengers, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for second messengers.

### Competing explanations, limitations, and quality controls

A fluorescent calcium indicator buffers calcium to some degree and its intensity may saturate. Observed oscillations can be created or hidden by acquisition and segmentation choices. Messenger concentration alone does not reveal which downstream effector was activated.

A persuasive conclusion about second messengers has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in second messengers after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A cell's calcium reporter produces a sharp spike after a short ligand pulse followed by a slower decline. Two drug conditions show identical peak brightness but different durations. Choosing peak intensity as the sole outcome would conceal a potentially large difference in time-integrated calcium exposure. The experiment therefore measures baseline, rise time, full-width at half-maximum, and area under a calibrated fluorescence-versus-time curve. The reporter itself can bind calcium and thereby change buffering. Confocal imaging may also miss a brief spike if frames are too far apart. Simultaneously imaging a nuclear effector could determine whether the sustained signal correlates with pathway activation, but the effector response may include delays and nonlinear thresholds. A rate-equation model for influx and extrusion gives a useful first approximation; the case asks students to reject an interpretation unsupported by temporal sampling.


## 4.3 Signal integration

### Central mechanism and vocabulary

Multiple receptors may converge on shared kinases, transcription factors, or metabolic responses. Integration may resemble a logical AND gate, a weighted sum, threshold crossing, or a history-dependent state change depending on circuit structure. Crosstalk occurs because components are shared, compete, inhibit one another, or change each other's expression. Temporal order can matter as much as final concentration: a priming pulse may alter response to a later stimulus. A cell population can show a smooth average even when individual cells are switching between distinct states.

### Why this mechanism matters

The central issue in **signal integration** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Multiple receptors may converge on shared kinases, transcription factors, or metabolic responses. Description and mechanism are not equivalent.

Consider a thought experiment involving **signal integration**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for signal integration should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: A cell population can show a smooth average even when individual cells are switching between distinct states.

### Experimental evidence and its interpretation

Apply a two-factor design crossing low and high levels of two ligands and inspect whether the combination is additive, synergistic, or antagonistic on a specified response scale. Record single-cell distributions where possible. Include repeated-pulse experiments to test whether cell history changes the apparent integration rule.

For signal integration, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on signal integration, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for signal integration.

### Competing explanations, limitations, and quality controls

Statistical interaction depends on the chosen response scale; multiplication on one scale may appear additive on another. Do not infer direct protein–protein contact from a shared change in transcription.

A persuasive conclusion about signal integration has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in signal integration after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

Two growth factors each raise a kinase reporter by 20 arbitrary units, but the combination raises it by 70. The difference from the simple additive expectation of 40 suggests interaction on that reported scale. Before describing synergy as a fundamental molecular fact, inspect the baseline and maximal dynamic range of the reporter, as well as whether either stimulus changed receptor expression. An experiment crosses several doses rather than only two binary conditions and compares single-cell response distributions. Some cells may respond only to factor A and others only to factor B; a smooth population average can create the false impression that every cell integrates both signals. Sequential pulses can test memory: A followed by B might differ from B followed by A. The conclusion should name the measured scale, pulse timing, and cellular heterogeneity rather than treating the word synergy as a mechanism in itself.


## 4.4 Feedback

### Central mechanism and vocabulary

Negative feedback can restore a signal toward baseline, reduce sustained gain, and sometimes create oscillations when delays and nonlinearities are important. Positive feedback can amplify a perturbation and create switch-like or bistable outcomes under suitable conditions. Feedback requires a directed causal loop: a correlated increase in two markers does not establish feedback. A system's steady state follows from balancing production, activation, degradation, and inhibition, while transient trajectories reveal parameters that steady-state measurements cannot distinguish.

### Why this mechanism matters

The central issue in **feedback** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Negative feedback can restore a signal toward baseline, reduce sustained gain, and sometimes create oscillations when delays and nonlinearities are important. Description and mechanism are not equivalent.

Consider a thought experiment involving **feedback**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for feedback should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: A system's steady state follows from balancing production, activation, degradation, and inhibition, while transient trajectories reveal parameters that steady-state measurements cannot distinguish.

### Experimental evidence and its interpretation

Stimulate cells with an input step and record the response over time, then selectively disrupt a suspected feedback component. Compare the early peak, late steady level, and recovery after washout. Fit a minimal differential-equation model and check residuals and parameter uncertainty rather than declaring one mechanism proven by visual curve similarity.

For feedback, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on feedback, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for feedback.

### Competing explanations, limitations, and quality controls

A stable response does not prove negative feedback; constitutive degradation can also generate stabilization. High-gain feedback models can hide spatial effects, stochastic events, and molecular delays.

A persuasive conclusion about feedback has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in feedback after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

After a ligand step, a reporter rises to a peak and then returns toward baseline despite continued ligand presence. Negative feedback is one plausible explanation, but receptor desensitization, ligand depletion, and reporter bleaching can produce similar trajectories. The investigator temporarily reduces the abundance of a candidate phosphatase and asks whether the adaptation time changes while the early rising slope stays comparable. A delayed feedback loop might generate overshoot; a fast degradation pathway can also generate a transient without feedback. Fit the shortest plausible dynamical model and compare its prediction under a second input waveform, such as two pulses separated by a recovery interval. Parameters that reproduce one trace may be unidentifiable without multiple perturbations. Students should explain why perturbing a feedback component and testing timing is stronger evidence than merely observing a peak.


## Fully worked problems

### CB-U4-P1: Receptor binding fraction

**Question:** A one-site receptor has Kd=8 nM and free ligand concentration L=24 nM. Calculate equilibrium occupancy; is this necessarily 75% of maximal signaling?

- 1. Use θ=L/(Kd+L) under the single noncooperative equilibrium assumption.
- 2. Substitute θ=24/(8+24) = 24/32.
- 3. Therefore θ=0.75, or 75% bound.
- 4. Occupancy and downstream functional response can differ due to amplification, receptor trafficking, reserve receptors, and feedback.
- 5. An independent reporter concentration-response curve is needed before claiming 75% maximal signaling.

**Verified final result:** 75% receptor occupancy

### CB-U4-P2: Hill-response threshold

**Question:** For a simplified cooperative reporter y=L^n/(K^n+L^n), let n=2, K=5 arbitrary units and L=10. Compute output.

- 1. Calculate L²=100 and K²=25.
- 2. Substitute y=100/(25+100).
- 3. Hence y=0.8, or 80% of modeled maximum.
- 4. At L=K, the expression yields 0.5 regardless of positive n.
- 5. A fitted Hill exponent does not by itself reveal the number of molecular binding sites.

**Verified final result:** 80% of maximum model output

### CB-U4-P3: Feedback steady state

**Question:** At steady state an idealized feedback variable x follows input/(1+kx)=x, with input=6 and k=2. Solve the physically meaningful nonnegative root.

- 1. Multiply through: 6=x+2x², or 2x²+x−6=0.
- 2. Factor the equation as (2x−3)(x+2)=0.
- 3. Its roots are x=1.5 and x=−2.
- 4. Reject the negative root for a nonnegative concentration-like variable.
- 5. The steady-state relation does not establish how fast x approaches equilibrium or whether omitted delays destabilize dynamics.

**Verified final result:** x=1.5



## Integrative study: receptor binding through adaptation

A ligand binds a surface receptor, stimulates an intracellular calcium transient, and eventually changes gene expression. Different groups measure different stages and announce contradictory dose–response curves. A binding group reports half-maximal receptor occupancy around one concentration, whereas a transcription group reports half-maximal output at a lower concentration. This discrepancy need not represent bad measurements. Downstream amplification, receptor reserve, temporal integration, and negative feedback can shift the functional response relative to equilibrium occupancy. Begin by arranging each data set according to what was physically detected, how long after stimulation it was acquired, and what units were used.

Design an experiment with at least five ligand concentrations, a vehicle condition, and repeated time points. A fluorescent ligand can provide a surface-binding proxy, but the experiment must separate bound from unbound ligand and account for internalization. For calcium dynamics, record a time series with a calibrated indicator and report baseline, peak, duration, and area. A transcriptional reporter measured hours later may reflect integration of signaling history rather than any one calcium concentration. If fluorescence reporters use different normalization baselines, comparing their numerical half-maximal doses without checking dynamic ranges can be misleading. A dose–response plot must label whether it refers to occupancy, intracellular messenger signal, or gene output.

Next, include a paired-stimulus condition to examine integration. Deliver ligand A followed by B, then reverse the order while controlling the interval. If output depends on order, a memory or adaptation mechanism might be operating, but receptor downregulation and ligand stability are rival explanations. Quantifying the single-cell distributions can show whether a population average represents universal moderate responses or mixed high and low responders. Negative feedback becomes a stronger causal explanation if selective perturbation of a candidate loop element changes adaptation timing and the model predicts responses to an untested input waveform.

Use two simplified equations as contrasting models: occupancy θ=L/(Kd+L) describes one equilibrium property, while a feedback relation such as dx/dt=u/(1+kx)−x describes one dynamical response. The equations operate on different levels of organization and have different assumptions. Neither reconstructs the complete receptor-to-gene network. The capstone asks students to annotate every curve with its observable, time coordinate, normalization rule and plausible confounding mechanism. The final claim should avoid equating a Hill slope with receptor stoichiometry or equating a temporary decrease in reporter intensity with full restoration of pre-stimulus function.

## Unit synthesis and interpretation

A signaling-analysis capstone compares three curves with the same x-axis of ligand concentration: receptor occupancy, calcium peak, and reporter-gene induction. Even if each rises with ligand concentration, their half-maximal levels can differ. Ask whether the calcium curve is sampled at the same time for every concentration and whether reporter induction is normalized to baseline or maximal expression. If a receptor is rapidly internalized, a binding measurement collected late may underestimate early occupancy. If a feedback element is inhibited, a transient peak may grow even if equilibrium binding stays unchanged. Students should predict the response to a short ligand pulse followed by washout, state the time resolution needed, and separate a direct receptor property from system-level adaptive behavior. Such a comparison teaches why a signaling pathway is not interchangeable with one ligand-binding equation.

## Interactive model specifications

### Single-site receptor occupancy

**Question tested by the model:** how does a ligand concentration relate to one-site receptor occupancy? For equilibrium independent binding, occupancy is 100L/(Kd+L) percent. At ligand 24 nM and Kd=8 nM, the predicted bound fraction is 75%. At L=Kd, it is exactly 50%. Raising Kd while holding ligand constant decreases occupancy because the interaction is less strongly favored in this idealized relation. Receptor occupancy is not a direct measurement of downstream transcription, ion-channel response, or cell fate; signal amplification, receptor turnover, and feedback can separate those outcomes.

### Negative-feedback steady state

**Question tested by the model:** how does an inhibitory feedback term temper an input-response curve? The educational balance equation is dx/dt=u/(1+kx)−x, producing a nonnegative steady state x=[sqrt(1+4ku)−1]/(2k) for k>0, and x=u when k=0. At input u=6 and gain k=2, the steady value is x=1.5 rather than 6. Dragging feedback gain toward zero shows the recovery of the uninhibited relation. This steady-state formula cannot predict oscillations or time-to-settlement, because delays and transient kinetics were intentionally omitted.

