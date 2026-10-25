# Unit 03 — Muscles, movement and energetic performance

> **Animal Physiology — OpenSTEM Book 11.** Coupling molecular motors, tissue mechanics and ATP supply to useful work. All numerical case values in this book are **synthetic teaching data**, not measurements, clinical advice or husbandry recommendations. This editorial draft has not received independent peer review.

## What the unit asks you to explain

Physiology is a quantitative study of how living structures accomplish work and keep conditions within tolerable ranges. This unit examines muscles, movement and energetic performance while connecting molecular mechanisms to whole-organism outcomes. The goal is not only to identify a named structure or pathway, but to predict the direction of change, the time needed for a response, and the observation that would distinguish a proposed mechanism from an alternative. Learners should keep conservation of matter or energy in view whenever they write an equation.

By the end of this unit, you should be able to (i) explain its five linked topics in physical and biological terms; (ii) calculate and interpret five dimensioned toy examples; (iii) decide which measurements distinguish input, state and output; (iv) identify failure modes of the models; and (v) design an ethical comparison while naming confounding factors. Prerequisites are first-year biology, elementary chemistry, algebra, and an ability to read plots. Differential equations are discussed conceptually where useful but are not assumed.


## Working distinctions

force is not work; motor control and recruitment; mechanical leverage; oxidative and anaerobic ATP supply; time-dependent fatigue. A useful unit-wide habit is to separate direct measurements from inferred flows, clearly stating physical units and time windows.


## Integrated systems lens — Energy, motion and performance are not interchangeable

Muscle converts free energy from ATP hydrolysis into mechanical force, movement and heat. Work requires force acting through displacement; force held without external displacement can still consume metabolic energy, although the external mechanical work is zero. A person pushing against an immovable wall illustrates the distinction, and a hovering animal adds the complication that high muscular power may be spent moving air rather than lifting its center of mass. Any energetic estimate needs a clear mechanical boundary.

The muscle–tendon complex is not a rigid actuator. Muscle fibers, tendon and aponeurosis can change length at different rates, allowing tendon stretch to absorb work and later return some of it. A jumping animal may store energy during landing preparation, while a runner may exploit repeated elastic recoil. Such recycling reduces cost under some conditions, but elastic materials cannot create energy. Losses occur through hysteresis, tissue damping and control effort.

Comparing force across animals requires normalizing by appropriate structural dimensions. Maximum muscle force is related partly to physiological cross-sectional area; length and architecture influence excursion and velocity. A very large muscle can produce substantial force without being particularly strong per unit area. Comparing locomotor speed in body lengths per second answers a different question from meters per second. Both metrics can be informative if the denominator is stated.

Fatigue arises when the task demands outstrip the combined ability of neural commands, membrane excitation and chemical energy systems to sustain output. It cannot be understood solely as depletion of ATP, because living muscle generally defends ATP concentration even as metabolites and calcium handling change. Task history matters: an isometric protocol and a series of maximal sprints produce different perturbations. Temperature and recovery interval can also reverse observed rankings between subjects.

Mechanical power can be negative when an active muscle lengthens while resisting a load, meaning the muscle absorbs external mechanical energy. A simple power calculation that assumes all positive muscle activation produces positive work will fail during downhill movement or landing. Inverse dynamics estimates net joint moments and powers, not the contributions of each muscle or ligament separately. Interpretation therefore requires tendon imaging, activation measures or carefully chosen anatomical models.

Metabolic measurements integrate many tissues. Oxygen uptake during whole-animal exercise includes the energetic demands of heart and breathing muscles as well as locomotor muscles. The rate of oxygen uptake lags rapidly changing work because gas stores, circulation and mitochondrial activation have their own dynamics. A high instantaneous mechanical output can temporarily exceed a contemporaneous oxidative ATP supply because phosphagens and other stores buffer the mismatch. Strong conclusions require synchronized mechanics and metabolism across the full exercise-and-recovery period.

## Five linked physiological topics

### 3.1 — Crossbridge cycling and calcium regulation

#### Biological mechanism and scope

In vertebrate striated muscle, calcium binding to troponin changes thin-filament regulation so actin and myosin can interact. ATP binding favors detachment, hydrolysis primes the motor, and product release couples conformational change to force-producing interactions. Calcium removal by sarcoplasmic reticulum pumps allows relaxation; maintaining ionic gradients also consumes energy.

#### Comparisons, exceptions and organism-level interpretation

ATP is required both for force production cycles and for resetting the machinery. A sustained contraction is not evidence that individual myosin heads remain locked in one state. In cardiac muscle calcium influx helps trigger calcium release, whereas skeletal excitation–contraction coupling uses a different coupling architecture. Smooth muscle uses calmodulin and myosin light-chain phosphorylation rather than troponin regulation.

#### Observation, experiment and causal alternatives

In isolated muscle, measure force during a rapid calcium activation step while varying ATP availability within safe physiological limits for the preparation. Distinguish peak force from rate of force development and relaxation. A fluorescence calcium signal is a proxy that must be calibrated against the force–calcium relationship.

#### Appropriate limits of the model

Textbook crossbridge cartoons are sequences of states, not literal synchronized motions of every motor molecule.


#### Mechanism-to-evidence test

A reported change in **crossbridge cycling and calcium regulation** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 11 — estimate, interpret, challenge

**Problem:** A hypothetical muscle develops 1500 N of force at full activation and reaches 70% of that activation level. Under linear scaling, what active force is estimated?

**Method:** `maximum force × activation fraction`. Substituting the given teaching values yields **1050 N**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** This illustration emphasizes the distinction between capacity and current activation. **Limits:** Single-muscle force does not always vary linearly with neural activation or stimulation rate. These are synthetic numbers, not measured organism values.


### 3.2 — Length–tension, force–velocity and power

#### Biological mechanism and scope

A muscle's active force depends on overlap between thin and thick filaments, while passive elastic elements add force at longer lengths. As a shortening muscle moves faster, it generally produces less force; lengthening contractions can show high force but involve different crossbridge and structural behavior. Mechanical power is the product of force and shortening velocity, not the same as force alone.

#### Comparisons, exceptions and organism-level interpretation

Maximum isometric force occurs at zero shortening velocity, where external mechanical power is zero. Conversely an unloaded muscle can shorten rapidly while doing almost no external work. Tendons can temporarily store and return elastic energy, allowing muscles to operate at favorable velocities while limbs move quickly. Mechanical efficiency includes internal losses and must not be inferred from gross joint work alone.

#### Observation, experiment and causal alternatives

Use an ergometer to obtain multiple force–velocity points and fit a descriptive relation. Report contraction temperature, stimulation history and starting fiber length. A power curve constructed by multiplying noisy fitted force by velocity should include uncertainty and not be interpreted as a universal property of all muscles.

#### Appropriate limits of the model

The Hill force–velocity model is an informative approximation for concentric shortening, not a model of every eccentric or cyclic contraction.


#### Mechanism-to-evidence test

A reported change in **length–tension, force–velocity and power** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 12 — estimate, interpret, challenge

**Problem:** Use the simplified concentric force law F = 120(1−v/1.5)/(1+3v/1.5) N. At v = 0.30 m/s, calculate mechanical power F × v.

**Method:** `force(v) × shortening speed`. Substituting the given teaching values yields **18 W**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** At zero shortening velocity external power is zero even though isometric force may be high. **Limits:** This illustrative curve excludes length dependence, eccentric contractions and fatigue. These are synthetic numbers, not measured organism values.


### 3.3 — Motor units, recruitment and fatigue

#### Biological mechanism and scope

A motor unit includes a motoneuron and the muscle fibers it activates. Force rises through recruitment of additional units and changes in firing rate. Different fibers exhibit distinct shortening speeds, mitochondrial density and resistance to fatigue, but real muscles show distributions rather than binary fast and slow categories.

#### Comparisons, exceptions and organism-level interpretation

Fatigue is a decline in performance capacity arising from interacting central drive, excitation, ion homeostasis, calcium handling, substrate delivery and contractile metabolism. A falling EMG amplitude is not automatically proof that the brain reduced its output, because electrode geometry and membrane action potentials also change. Recovery kinetics help distinguish reversible physiological limitation from structural injury.

#### Observation, experiment and causal alternatives

Repeat fixed-duration contractions with standardized duty cycles and record torque, stimulation response and surface EMG. Contrast voluntary and electrically evoked responses while considering discomfort and participant safety. A protocol that compares subjects only at an identical absolute load disadvantages smaller muscles and may obscure relative capacity.

#### Appropriate limits of the model

Fatigue should be reported with a defined task, temperature and performance metric rather than treated as a single substance that accumulates.


#### Mechanism-to-evidence test

A reported change in **motor units, recruitment and fatigue** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 13 — estimate, interpret, challenge

**Problem:** Measured force declines from 140 N at the beginning of a fixed task to 105 N at its end. Calculate percent decline relative to initial force.

**Method:** `100 × (initial − final) / initial`. Substituting the given teaching values yields **25 %**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** A 25% decline is evidence of task-defined performance fatigue. **Limits:** It does not uniquely locate fatigue in the nervous system, sarcolemma or contractile filaments. These are synthetic numbers, not measured organism values.


### 3.4 — Locomotor biomechanics and elastic recoil

#### Biological mechanism and scope

Limb muscles act through lever arms. Muscle force, joint torque and ground reaction force differ because bones and tendons transform movement and distribute loads. During running, elastic tissues can absorb energy when loaded and return part of it when unloaded. Animals also shift gait, stride frequency and duty factor as speed or terrain changes.

#### Comparisons, exceptions and organism-level interpretation

Long tendons can reduce the energy required for cyclic force production, but they can also raise peak stress or complicate precise positioning. Aquatic swimmers, terrestrial runners and flyers face different fluid and ground reaction forces; a common mechanical accounting framework does not imply identical solutions. Electromyography identifies activation timing but does not directly measure individual muscle force.

#### Observation, experiment and causal alternatives

Film limb motion with synchronized force plates, then estimate joint moments using inverse dynamics. Explain sensitivity to segment mass assumptions and marker placement. To assess tendon elastic storage, combine ultrasound geometry with a force estimate rather than treating any springlike movement as direct evidence of energy recovery.

#### Appropriate limits of the model

The least energetic gait depends on speed, body design and ecological constraints, not just the shortest distance travelled.


#### Mechanism-to-evidence test

A reported change in **locomotor biomechanics and elastic recoil** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 14 — estimate, interpret, challenge

**Problem:** A muscle applies 100 N perpendicular to a moment arm 0.030 m long. Calculate joint torque under static ideal assumptions.

**Method:** `perpendicular force × moment arm`. Substituting the given teaching values yields **3 N·m**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Torque depends on the perpendicular lever arm, not merely bone length. **Limits:** Changing joint angle changes leverage; a single torque value cannot describe an entire movement cycle. These are synthetic numbers, not measured organism values.


### 3.5 — Exercise metabolism and oxygen debt

#### Biological mechanism and scope

ATP demand rises within seconds when contractile activity begins. Stored phosphagens buffer rapid changes; glycolysis can provide ATP at high rates; mitochondrial oxidation supports sustained work when oxygen delivery, substrates and enzyme capacity permit. Lactate is a dynamic metabolite and fuel, not merely a poisonous waste product.

#### Comparisons, exceptions and organism-level interpretation

Oxygen consumption may lag behind mechanical demand at exercise onset because cardiac, respiratory and tissue processes require time to adjust. Recovery oxygen consumption supports many processes including phosphagen restoration, temperature regulation and fuel turnover. It should not be naively equated with the oxygen needed to oxidize all lactate generated during work.

#### Observation, experiment and causal alternatives

Measure oxygen uptake and external mechanical power during stepwise exercise, holding each workload long enough for an interpretable steady state where possible. Use gas analyzer calibration and account for respiratory exchange ratio. A breath-by-breath signal is noisy; avoid labeling every fluctuation a change in mitochondrial capacity.

#### Appropriate limits of the model

Maximum oxygen uptake is a system-level outcome of delivery and utilization, not a standalone assay of one enzyme or organ.


#### Mechanism-to-evidence test

A reported change in **exercise metabolism and oxygen debt** is not automatically a demonstration of the mechanism proposed to explain it. Draw a chain from the experimental input through a cellular or tissue intermediate to the whole-animal outcome. Next, name a competing pathway that could change the same final outcome, and predict a measurement that would distinguish the two explanations. Include when each signal should first appear, rather than measuring only the last endpoint. The relevant body compartment, temperature, developmental stage and experimental disturbance must be stated before generalizing. A simplified equation in this chapter is a transparent conditional calculation; it is not a biological law outside its specified assumptions.


#### Worked case 15 — estimate, interpret, challenge

**Problem:** During a controlled task external useful mechanical output is 80 W while measured total metabolic power is 400 W. Calculate apparent gross efficiency.

**Method:** `100 × output / metabolic input`. Substituting the given teaching values yields **20 %**. Check that the dimensions agree before interpreting the result. Changing a numerator or denominator has a predictable direction only while the other inputs and model assumptions stay fixed.

**Biological meaning:** Distinguish gross efficiency from net efficiency after subtracting resting metabolic expenditure. **Limits:** The estimate depends on accurately measuring and aligning energy flows over the same interval. These are synthetic numbers, not measured organism values.


## Integrative investigation — Running uphill with elastic tendons

**Setting.** Imagine two closely related mammals ascending the same incline at matched speed. One has long distal tendons, while the other relies on a different distribution of muscle and tendon mass. Both must raise their center of mass, but their muscles may follow different shortening velocities and patterns of activation.

**Design.** Measure incline, speed, body mass, ground reaction forces, stride timing and respiratory exchange. Estimate the minimum change in gravitational potential energy per unit time from vertical speed, remembering that this is only part of external mechanical work. Record metabolic expenditure over an interval long enough to avoid confusion with the transient rise at exercise onset.

**Evidence and alternatives.** A tendon may absorb and return energy within each stride without generating net energy. Thus an observed reduction in oxygen consumption cannot simply be equated with elastic energy storage; changes in posture, muscle length and coactivation also affect cost. Ultrasound data can refine estimates of muscle fascicle and tendon length changes.

**Interpretation and transfer.** Prepare a comparative table of estimated joint power, oxygen uptake and tendon stretch. Ask whether equal slope and speed ensure equal total mechanical cost when the animals differ in stride and limb posture. Construct a simple fatigue test that avoids training history as a confounder. The integration exercise emphasizes that anatomy influences energetic economy, while metabolic measurements and mechanical measurements quantify different aspects of the same task.

**Reproducibility checklist.** Declare the independent biological replicate and the direct measurement. Preselect a primary outcome, control environmental changes, and calibrate instruments. Preserve original data and computation steps rather than reporting rounded results alone. Compare the specific competing predictions before interpreting statistical significance. Respect animal welfare by using approved, appropriately noninvasive or existing datasets for educational comparisons.


## Retrieval practice — explain rather than memorize

1. For **Crossbridge cycling and calcium regulation**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

2. For **Length–tension, force–velocity and power**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

3. For **Motor units, recruitment and fatigue**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

4. For **Locomotor biomechanics and elastic recoil**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

5. For **Exercise metabolism and oxygen debt**, identify a controlled variable, a plausible alternative mechanism, and an observation that would separate the two. What would change if the animal or environmental condition changed?

**Self-check:** A defensible answer distinguishes direct observation from inference, names a unit or timescale, and explains at least one way its proposed explanation could be wrong. Recalculate all five worked cases without reading the answers.

## Working glossary and distinctions

The entries below state operational differences that matter when planning an experiment. Learn each term through a concrete measurement rather than memorizing a label in isolation.


**Sarcomere.** A repeating contractile unit in striated muscle whose organized actin and myosin arrangement supports sliding-filament force production.


**Troponin.** A regulatory complex in vertebrate striated muscle that responds to calcium and alters access of myosin to actin.


**Crossbridge.** An interaction between a motor protein head and a filament that can contribute to force and movement.


**Isometric contraction.** A contraction during which muscle–tendon length is held effectively fixed, although internal microscopic elements may still move.


**Concentric contraction.** Active shortening of muscle under a load, often described by an inverse force–velocity relation over a limited range.


**Eccentric contraction.** Active muscle lengthening under load; the force behavior and energy accounting differ from active shortening.


**Active tension.** Force produced by activated contractile machinery, distinguished from passive force developed in elastic tissue.


**Moment arm.** The perpendicular distance from a joint's rotational axis to the line of action of a force.


**Joint torque.** Rotational effect of force about a joint, expressed in newton meters and dependent on leverage.


**Motor unit.** A motor neuron together with the muscle fibers it activates, forming an operational unit of motor recruitment.


**Electromyography.** Recording of muscle-associated electrical signals, useful for timing and recruitment but not a direct reading of force.


**Mechanical power.** Work rate, often calculated as force multiplied by speed when the force and velocity are aligned.


**Elastic recoil.** Return of stored mechanical energy from a previously deformed elastic structure such as a tendon.


**Fatigue.** Task-dependent reduction in capacity to produce force or power, potentially reflecting interacting neural, ionic and metabolic factors.


**Phosphagen buffer.** A rapid energy-transfer system that can temporarily maintain ATP availability while slower metabolic processes adjust.


## Unit 3 synthesis

Return to the five worked numerical cases and ask what controls each result, which changes are compensatory rather than primary, and how the model would fail when another organ system changes. Connect force is not work with oxidative and anaerobic ATP supply and state a falsifiable prediction across the two levels of organization.
