# Unit 02 — Neural, sensory and information processing

> **Animal Physiology — OpenSTEM Book 11.** How excitable membranes encode signals and nervous systems transform information into behavior. All numerical case values in this book are **synthetic teaching data**, not measurements, clinical advice or husbandry recommendations. This editorial draft has not received independent peer review.

## What the unit asks you to explain

Physiology is a quantitative study of how living structures accomplish work and keep conditions within tolerable ranges. This unit examines neural, sensory and information processing while connecting molecular mechanisms to whole-organism outcomes. The goal is not only to identify a named structure or pathway, but to predict the direction of change, the time needed for a response, and the observation that would distinguish a proposed mechanism from an alternative. Learners should keep conservation of matter or energy in view whenever they write an equation.

By the end of this unit, you should be able to (i) explain its five linked topics in physical and biological terms; (ii) calculate and interpret five dimensioned toy examples; (iii) decide which measurements distinguish input, state and output; (iv) identify failure modes of the models; and (v) design an ethical comparison while naming confounding factors. Prerequisites are first-year biology, elementary chemistry, algebra, and an ability to read plots. Differential equations are discussed conceptually where useful but are not assumed.


## Working distinctions

electrical driving forces; spike timing rather than strength; signal conversion and noise; circuit integration; adaptation and inference. A useful unit-wide habit is to separate direct measurements from inferred flows, clearly stating physical units and time windows.


## Integrated systems lens — Information becomes action through physical bottlenecks

The membrane potential provides a compact observable, but it is not a single-cause variable. If membrane voltage becomes more positive after pharmacological treatment, at least three mechanisms might explain the change: reduced potassium conductance, increased inward sodium or calcium conductance, or changes in ionic concentration. A recording of voltage alone cannot discriminate these mechanisms. Measuring current–voltage relationships or specific ionic reversal potentials adds crucial constraints. Even there, experimental series resistance and space-clamp limitations affect interpretation.

Propagation and synaptic transmission occupy different locations in the signaling chain. In a myelinated axon, insulation and node spacing influence propagation; at a chemical synapse, vesicle release and receptor kinetics influence transfer. If a behavioral response is delayed, the causal change could occur anywhere from stimulus transduction to muscle shortening. Multipoint timing and targeted perturbation are therefore often more useful than a single response-time average. In a field animal, noninvasive sensing may provide partial but ethically preferable information.

Electrophysiological units deserve care. Membrane potential is volts or millivolts; membrane current is amperes; resistance is ohms and conductance is siemens. Capacitance stores charge and shapes the rate of voltage change. The elementary relation I = C dV/dt shows that the same input current produces different voltage slopes when capacitance changes. Because channels alter membrane conductance during the response, the full dynamics are not just an RC circuit; nonetheless that elementary relation explains why time matters for summation.

Sensory systems solve a dynamic-range problem. A transducer sensitive enough to detect minute changes might saturate under a strong stimulus, while a receptor optimized for strong signals might miss weak inputs. Adaptation can shift operating range, and populations of receptors with different sensitivities can encode larger ranges than one receptor alone. A psychophysical threshold is also influenced by decision criteria, attention and noise. It is consequently unwise to declare that a receptor has failed merely because a subject did not respond to one stimulus.

Motor control is closed-loop during most natural movement. Sensory feedback provides information about unexpected loads and posture, while central commands prepare anticipated movements. When feedback is delayed or noisy, prediction becomes valuable. Experiments that perturb a limb at different phases of walking can reveal phase-dependent reflex gains. The same spinal connection may strengthen, weaken or change sign with task state, undermining overly rigid circuit diagrams.

When evaluating mechanism, select the earliest predicted observation unique to one competing hypothesis. For a slower action potential, conduction latency should change before muscular force develops; for impaired force generation, neural timing may remain normal. This temporal-order principle does not eliminate confounding but makes it harder to tell a purely descriptive story. Include electrode controls, temperature measurement, blinding where possible and an explicit unit of biological replication.

## Five linked physiological topics

### 2.1 — Resting membrane potential and ion selectivity

#### Biological mechanism and scope

A resting neuron contains unequal concentrations of sodium, potassium, chloride and other ions on its two sides. Its membrane voltage reflects relative permeability as well as ion gradients. Potassium leak often dominates the resting state in many neurons, but an exact Nernst equilibrium for potassium should not be mistaken for the actual voltage of a living neuron with multiple conductive ions and electrogenic pumps.

#### Comparisons, exceptions and organism-level interpretation

Ion channel opening changes conductance and can shift voltage toward the equilibrium potential for that ion. Hyperpolarization is not synonymous with inhibition: a hyperpolarizing current can interact with timing and intrinsic channels to facilitate rebound firing in some cells. Similarly chloride currents depend on chloride gradients and can be depolarizing in particular developmental contexts.

#### Observation, experiment and causal alternatives

Record membrane potential with a suitable intracellular technique while changing extracellular potassium in controlled increments. Compare the observed slope with a simple Nernst prediction, but remember junction potentials, changing conductances and cell health. Interpret deviations as clues to multiple-ion permeability rather than automatic measurement mistakes.

#### Appropriate limits of the model

Nernst calculations assume a membrane selectively permeable to the selected ion at electrochemical equilibrium. They cannot predict spike shape or cellular excitability on their own.


#### Mechanism-to-evidence test

A reported change in **resting membrane potential and ion selectivity** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 06 — estimate, interpret, challenge

**Problem:** For a cell near 37°C with potassium concentration outside = 5 mM and inside = 140 mM, approximate the potassium equilibrium potential using 61.5 log₁₀(out/in) mV.

**Method:** `61.5 × log10(outside / inside)`. Substituting the given teaching values yields **-89 mV**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** The result is negative because the outward potassium concentration gradient favors positively charged ion efflux at zero voltage. **Limits:** Actual resting potential also depends on other ions and conductances. These are synthetic numbers, not measured organism values.


### 2.2 — Action potentials, refractory periods and conduction

#### Biological mechanism and scope

Many axons generate action potentials when inward voltage-gated current outweighs opposing currents past a dynamic threshold. Rapid depolarization is followed by inactivation and repolarizing conductances. The spike propagates because current from one active patch changes the next patch's voltage. Myelination permits current to travel under insulated segments and regenerate at nodes, improving speed and energetic efficiency within structural limits.

#### Comparisons, exceptions and organism-level interpretation

Spike amplitude is not a code for stimulus strength in the way an analog microphone output is. Neural information is often encoded in firing rate, temporal pattern and recruited populations. High firing frequency eventually becomes limited by refractory recovery, ion accumulation and metabolic demand. Loss of myelin can impair conduction despite apparently intact transmitter release at a terminal.

#### Observation, experiment and causal alternatives

Stimulate a nerve at two sites and compare latency at a fixed recording position to estimate conduction speed. Control for temperature, electrode geometry and stimulus artifact. Compound action potentials mix fibers of different sizes, so the first onset gives a property of the fastest detected fibers, not the average speed of all fibers.

#### Appropriate limits of the model

Refractory intervals emerge from channel state and membrane conditions; a single textbook number should not be applied to every species, axon and temperature.


#### Mechanism-to-evidence test

A reported change in **action potentials, refractory periods and conduction** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 07 — estimate, interpret, challenge

**Problem:** A compound nerve response travels an extra 0.12 m and appears 3 ms later. What is the estimated speed of the earliest detectable component?

**Method:** `distance / delay`. Substituting the given teaching values yields **40 m/s**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** The extra-distance method avoids confusing stimulus-to-electrode latency with conduction time alone. **Limits:** Fiber recruitment and signal threshold can change the identified onset. These are synthetic numbers, not measured organism values.


### 2.3 — Synapses and postsynaptic integration

#### Biological mechanism and scope

A chemical synapse translates presynaptic electrical activity into calcium-dependent transmitter release and postsynaptic receptor signaling. Vesicles release transmitter in probabilistic quanta, and postsynaptic receptors may produce rapid ionotropic currents or slower metabotropic changes. Temporal summation depends on membrane time constant, while spatial summation depends on dendritic location and local conductances.

#### Comparisons, exceptions and organism-level interpretation

An excitatory transmitter does not guarantee an action potential. Inhibition can reduce firing by hyperpolarizing the membrane, increasing conductance and shunting nearby excitation, or changing intracellular signaling. Plasticity may change presynaptic release probability, receptor number or intrinsic excitability. The same postsynaptic voltage change can therefore arise from several mechanisms.

#### Observation, experiment and causal alternatives

Apply paired pulses and record postsynaptic currents, then compare responses under receptor blockade. Paired-pulse ratios are informative but do not uniquely identify presynaptic release mechanisms without additional measurements. Use miniature events and quantal analysis carefully because detection thresholds bias the inferred distribution.

#### Appropriate limits of the model

Network behavior follows connectivity and cell states, not a simple arithmetic sum of isolated synapse amplitudes.


#### Mechanism-to-evidence test

A reported change in **synapses and postsynaptic integration** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 08 — estimate, interpret, challenge

**Problem:** Use a deliberately linear membrane toy model with baseline −67 mV, three +3 mV inputs and two −2 mV inputs. Estimate net membrane voltage.

**Method:** `baseline + excitatory contributions − inhibitory contributions`. Substituting the given teaching values yields **-62 mV**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** The approximation gives a conceptual picture of summation near rest. **Limits:** True synaptic integration is nonlinear and depends on conductance, location and reversal potentials. These are synthetic numbers, not measured organism values.


### 2.4 — Sensory receptors and adaptation

#### Biological mechanism and scope

Sensory receptors convert physical or chemical energy into graded changes in membrane current. Mechanoreceptors, photoreceptors and chemoreceptors use different proteins and anatomical arrangements, yet all must balance sensitivity with dynamic range. A constant stimulus may produce a large initial response and smaller sustained firing as receptors and circuits adapt.

#### Comparisons, exceptions and organism-level interpretation

Adaptation is not failure: it can emphasize changes in the environment while sacrificing an accurate representation of constant intensity. Some receptors adapt rapidly and signal onset or movement; others retain tonic information. The response of a sensory nerve may also be changed by attention, feedback, stimulus history or mechanical properties of the receptor organ.

#### Observation, experiment and causal alternatives

Measure the response to step stimuli of several magnitudes, reporting both transient and steady components. Randomize stimulus order to prevent drift or desensitization from confounding intensity effects. A logistic dose–response curve is a phenomenological summary; receptor binding alone does not establish neural perception.

#### Appropriate limits of the model

A detection threshold depends on signal-to-noise criteria, the behavioral task and downstream processing as well as receptor biochemistry.


#### Mechanism-to-evidence test

A reported change in **sensory receptors and adaptation** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 09 — estimate, interpret, challenge

**Problem:** In a classroom receptor model, a response probability is p = 1/(1+e^(−(S−5))), with S = 6 in dimensionless stimulus units. Calculate p.

**Method:** `1 / (1 + exp(−(S−5)))`. Substituting the given teaching values yields **0.73106 probability**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** At the model's midpoint, S = 5, the calculated response probability would be 0.5. **Limits:** A modeled behavioral response probability is not identical to an individual receptor's firing rate. These are synthetic numbers, not measured organism values.


### 2.5 — Reflex circuits, central patterning and motor commands

#### Biological mechanism and scope

A spinal reflex links afferent activity to motor output through circuits that can operate without deliberate conscious control. Stretch-sensitive afferents influence spinal motor neurons and interneurons, providing rapid stabilization. Walking and swimming additionally recruit rhythm-generating networks that interact with proprioceptive feedback and descending commands.

#### Comparisons, exceptions and organism-level interpretation

A short-latency response does not prove a circuit is fixed or purely feedforward. Task demands, posture, presynaptic inhibition and neuromodulators can change reflex gain. Identical limb movements may arise from different combinations of sensory feedback and central commands. A reflex recorded under anesthesia is not necessarily a faithful representation of awake locomotion.

#### Observation, experiment and causal alternatives

Record muscle electromyography and joint movement before and after a controlled tendon displacement. Manipulate background muscle activation rather than comparing uncontrolled trials. Evaluate latency, gain and aftereffects; then ask whether the perturbation altered receptor activation, spinal integration or muscle mechanics.

#### Appropriate limits of the model

Motor output is a property of the coupled neural-musculoskeletal system. A circuit diagram without its load and sensory environment is incomplete.


#### Mechanism-to-evidence test

A reported change in **reflex circuits, central patterning and motor commands** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 10 — estimate, interpret, challenge

**Problem:** A reflex signal travels 0.45 m to the spinal cord at 45 m/s, then 0.60 m back at 50 m/s, with 8 ms of circuit delay. Estimate overall latency.

**Method:** `afferent distance/speed + efferent distance/speed + delay`. Substituting the given teaching values yields **30 ms**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** The calculated latency sums separate conduction and central-processing intervals. **Limits:** Neuromuscular transmission, electromechanical delay and real anatomy add additional delays. These are synthetic numbers, not measured organism values.


## Integrative investigation — Signal timing in a predator-avoidance reflex

**Setting.** A small vertebrate encounters a rapidly moving shadow and changes posture before initiating locomotion. The sensory organ must transduce a visual or mechanical signal, neurons conduct action potentials, spinal or brainstem circuits transform information, and muscles generate force against the animal's inertia. These stages occur at different delays, so response timing is more informative than one final movement distance.

**Design.** Use video frame timing with voluntary natural behavior, keeping illumination and substrate constant. Identify the first detectable sensory event, motor electrical activity, movement initiation and escape trajectory. The total latency should be decomposed into recognition, conduction, synaptic, excitation–contraction and biomechanical components rather than allocated entirely to neural conduction.

**Evidence and alternatives.** If a treatment delays the escape by 15 ms, a slower axon is only one explanation. Vision could be impaired, circuit threshold altered, the muscle cooler or the animal less motivated. Compare response amplitudes and latencies, and repeat across stimulus intensities to distinguish sensory detectability from motor execution.

**Interpretation and transfer.** Build a timing diagram with candidate minimum and maximum delays. Use the nerve-conduction calculation in the unit as one constraint, not an exact prediction. Specify what control reveals whether temperature altered membrane conduction, muscular shortening or both. Discuss why repeated startling would create adaptation and ethical concerns. The important distinction is between information flow and mechanics: identifying the earliest changed component provides a stronger inference than interpreting final escape performance alone.

**Reproducibility checklist.** Declare the independent biological replicate and the direct measurement. Preselect a primary outcome, control environmental changes, and calibrate instruments. Preserve original data and computation steps rather than reporting rounded results alone. Compare the specific competing predictions before interpreting statistical significance. Respect animal welfare by using approved, appropriately noninvasive or existing datasets for educational comparisons.


## Retrieval practice — explain rather than memorize

1. For **Resting membrane potential and ion selectivity**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

2. For **Action potentials, refractory periods and conduction**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

3. For **Synapses and postsynaptic integration**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

4. For **Sensory receptors and adaptation**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

5. For **Reflex circuits, central patterning and motor commands**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

**Self-check:** A defensible answer distinguishes direct observation from inference, names a unit or timescale, and explains at least one way its proposed explanation could be wrong. Recalculate all five worked cases without reading the answers.

## Working glossary and distinctions

The entries below state operational differences that matter when planning an experiment. Learn each term through a concrete measurement rather than memorizing a label in isolation.


**Electrochemical gradient.** The combined concentration and electrical driving force on an ion; a concentration gradient alone is insufficient to determine direction.


**Equilibrium potential.** The voltage at which electrical and chemical forces on a given ion balance, assuming the appropriate temperature and concentrations.


**Conductance.** A measure of how readily ionic current crosses a membrane; multiple channel populations can contribute to effective membrane conductance.


**Action potential.** A regenerative electrical event produced by excitable membrane currents; information is often carried in event timing and recruitment.


**Refractory period.** An interval of altered capacity to generate another spike because channel state and membrane conditions have not fully recovered.


**Saltatory conduction.** Propagation in myelinated axons in which electrical current travels between regenerating nodes of Ranvier; the process is not literal jumping.


**Synaptic cleft.** The narrow extracellular space across which released transmitter molecules travel to affect postsynaptic receptor proteins.


**Temporal summation.** Interaction of inputs arriving close in time, influenced by membrane time constant and active membrane conductances.


**Spatial summation.** Combination of signals arising at different cell locations, with dendritic geometry and conductance shaping their effective weight.


**Shunting inhibition.** Reduction of voltage response when added conductance diverts membrane current, sometimes with little resting voltage change.


**Proprioception.** Sensing the state and movement of limbs and body segments using receptors in muscles, joints and associated tissues.


**Receptor potential.** A graded electrical response to a stimulus that may subsequently affect spike generation or transmitter release.


**Adaptation.** A change in sensitivity or response during sustained or repeated stimulation, arising at receptor or circuit levels.


**Reflex gain.** The magnitude of an evoked motor response relative to a defined stimulus measure, dependent on physiological and behavioral context.


**Central pattern generator.** A neural network capable of producing rhythmic motor-related activity, ordinarily modified by sensory input and descending commands.


## Unit 2 synthesis

Return to the five worked numerical cases and ask what controls each result, which changes are compensatory rather than primary, and how the model would fail when another organ system changes. Connect electrical driving forces with circuit integration and state a falsifiable prediction across the two levels of organization.
