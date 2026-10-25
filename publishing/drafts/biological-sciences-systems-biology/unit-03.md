# Unit 3: Dynamical systems, feedback and stability

**Scope and intended claim.** Students will derive trajectories from reactions and distinguish transient from asymptotic behavior. The unit emphasizes ODE state derivatives, nonlinear rate laws, feedback delay, stable fixed points and persistent cycles. Its most important epistemic boundary is that the shape of one time series cannot identify a unique underlying circuit

## Unit foundations

Rate equations translate mechanistic assumptions into time-dependent predictions. In a reaction such as A converting to B, the conversion rate determines how rapidly A changes and how rapidly B appears; with no other reactions, their sum remains constant. Conservation statements are often more reliable first tests of implementation than visual inspection of a trajectory. A simulation that violates a known conserved total has a structural or numerical problem even if its curve looks smooth.

Feedback terminology describes the sign of the loop, not an automatic dynamic outcome. Negative feedback may reduce steady-state sensitivity, accelerate recovery or generate oscillations if sufficient delay is present. Positive feedback may enhance gain; only particular nonlinearities and parameter regions produce several locally stable equilibria. Likewise a damped transient can show repeated peaks without being a persistent limit cycle. One must examine long-duration behavior, stability and sensitivity to initial conditions.

The local Jacobian connects changes in state variables to changes in rates near an equilibrium. Negative real parts of its eigenvalues imply local asymptotic stability for a standard smooth continuous-time ODE, but cannot rule out a different attractor elsewhere. A stability calculation also depends on the model equation and parameter point. Empirical prediction needs observation-aware tests: sparse sampling may miss short pulses or alias faster oscillations into deceptively slow patterns.

This unit repeatedly distinguishes a mathematically correct derivation from a validated biological mechanism. An accurate solution of a simplified ODE proves properties of that ODE, not that the living system follows it. The strongest conclusions come when several plausible models make different predictions for an experiment that can actually be observed.

## Mathematical practice across the five lessons

Start with a toy example small enough to solve or check analytically. Define whether the variables are dimensionless, molecular counts, concentrations, rates or graphical quantities. When a mathematical property such as convergence or an optimum is asserted, write down the assumptions making that statement true. Compare at least two parameter regimes or alternative models rather than treating one attractive image as sufficient evidence. A plausible-looking simulation should be followed by a limiting-case calculation, a units audit and an explicit statement about which parts are fictional.

The worked cases associated with this unit are deliberately distinct: first-order half life, closed-loop sensitivity factor, hill occupancy analogy, toy angular frequency to period, return time of a stable mode. Each calculation isolates one quantitative relationship. The point is not to make every biological process reducible to arithmetic; it is to show where simple algebra can detect an impossible explanation and where additional experimental information would be needed to determine a physical parameter. Check at least one result both manually and with an independent computational implementation.

## Five detailed lessons

## Lesson 3.1 — Mass action and reaction kinetics

**Learning goal.** Explain the mechanism or formal representation behind mass action and reaction kinetics, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: derive trajectories from reactions and distinguish transient from asymptotic behavior.

### Core idea and biological meaning

Mass action links reaction rates to reactant amounts under well-mixed idealized conditions. It enables transparent differential equations but may fail when transport, spatial heterogeneity or crowding matters. Reaction stoichiometry fixes concentration changes, whereas rate constants and initial states determine trajectories.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Model A converting to B with rate kA and compare early-time loss of A across two initial concentrations. For a reversible reaction add a reverse flux and locate the equilibrium ratio.

**Model construction.** Write the direction of every process, determine whether a conserved sum exists, and distinguish the early transient from the eventual state. If no equilibrium is expected, define the observation window and the cause of sustained variation. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A first-order fit to a pooled assay does not establish that the microscopic mechanism is first order across all concentrations or compartments.

**Targeted improvement.** Write each reaction explicitly, derive rate terms from it, confirm units and check that any closed-system total remains constant numerically.

**Definition versus mechanism.** A descriptive quantity becomes mechanistic only when an explicit mapping connects it to events that generate the observations. Ask which extra assumptions make that mapping possible, whether those assumptions can be checked, and how a second representation could lead to a conflicting explanation. A second model is informative not because it contains more equations, but because it exposes which conclusion depends on a choice the first model hid.

### Worked synthetic numerical case — First-order half life

The input values are invented solely for instruction: `k = 0.14`. Apply `log(2)/k` and obtain **4.951051 minutes**. Constant first-order decay and no additional source are assumed. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of the shape of one time series cannot identify a unique underlying circuit

### Concept transfer and practice problems

**Transfer setting.** Generalize to receptor turnover or mRNA decay, remembering that rate laws must match the measurement scale.

1. **Inference design.** How can a constant background synthesis term mask apparent first-order decay in sparse measurements? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `log(2)/k` from the fictional inputs. *Answer:* **4.951051 minutes**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 3.2 — Negative feedback and adaptation

**Learning goal.** Explain the mechanism or formal representation behind negative feedback and adaptation, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: derive trajectories from reactions and distinguish transient from asymptotic behavior.

### Core idea and biological meaning

Negative feedback can suppress disturbances, speed recovery or create overshoot, but the outcome depends on loop gain and delays. Adaptation is return toward a baseline after a sustained input, not merely a smaller peak. Incoherent feedforward control is another route to transient responses.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Compare a regulated species that induces its own inhibitor with an otherwise identical open-loop species after an input step. Examine peak, steady state and recovery after signal withdrawal.

**Model construction.** Write the direction of every process, determine whether a conserved sum exists, and distinguish the early transient from the eventual state. If no equilibrium is expected, define the observation window and the cause of sustained variation. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A smaller peak can result from lower input rather than feedback; adaptation also may fail at saturation or under slow inhibitor kinetics.

**Targeted improvement.** Use matched input and initial conditions, track both regulated species and inhibitor, then vary a single feedback-strength parameter while retaining mass balance.

**Measurement and calibration.** Examine how the observed variable is constructed from the underlying biological state. A sensor may have background, nonlinearity, delay and a detection threshold; mathematical fitting should not treat these as biological responses. A useful validation set includes measurements outside the narrow conditions used to choose the observation mapping.

### Worked synthetic numerical case — Closed-loop sensitivity factor

The input values are invented solely for instruction: `gain = 3`. Apply `1/(1+gain)` and obtain **0.25 fraction**. This static negative-feedback analogy omits delays and nonlinear saturation. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of the shape of one time series cannot identify a unique underlying circuit

### Concept transfer and practice problems

**Transfer setting.** Extend the reasoning to homeostatic hormone regulation and bacterial chemotaxis without assuming either has identical molecular architecture.

1. **Inference design.** What measurements distinguish feedback-induced adaptation from progressive receptor exhaustion? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `1/(1+gain)` from the fictional inputs. *Answer:* **0.25 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 3.3 — Positive feedback and bistability

**Learning goal.** Explain the mechanism or formal representation behind positive feedback and bistability, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: derive trajectories from reactions and distinguish transient from asymptotic behavior.

### Core idea and biological meaning

Positive feedback can support memory and hysteresis when nonlinear response is strong enough. A steep input–output curve alone is not evidence of multiple stable states; initial-condition dependence and switching thresholds must be demonstrated.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Analyze a cooperative self-activating protein and track steady-state output as stimulus increases and decreases. Compare possible low and high expression states under the same stimulus.

**Model construction.** Write the direction of every process, determine whether a conserved sum exists, and distinguish the early transient from the eventual state. If no equilibrium is expected, define the observation window and the cause of sustained variation. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A noisy population average can look bimodal because of cell heterogeneity even if every individual cell has a single stable attractor.

**Targeted improvement.** Test different initial conditions, perturbations in both directions and return paths; use a stability argument rather than only plotting a single trajectory.

**Time ordering.** Identify which quantities cause changes and which respond later. Cross-sectional associations can be compatible with several temporal mechanisms, so draw at least two causal timelines before trusting the preferred account. An intervention at a carefully selected time can separate lagged effects that a steady-state comparison cannot resolve.

### Worked synthetic numerical case — Hill occupancy analogy

The input values are invented solely for instruction: `x = 5`, `h = 3`, `K = 4`. Apply `x**h/(K**h+x**h)` and obtain **0.6613757 fraction**. Cooperativity can create a steep curve without proving hysteresis. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of the shape of one time series cannot identify a unique underlying circuit

### Concept transfer and practice problems

**Transfer setting.** Apply the idea to differentiation decisions where lineage commitment may involve coupled feedback rather than a single isolated loop.

1. **Inference design.** How would transiently lowering an activator reveal a genuine switch with memory? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `x**h/(K**h+x**h)` from the fictional inputs. *Answer:* **0.6613757 fraction**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 3.4 — Oscillations, delays and phase

**Learning goal.** Explain the mechanism or formal representation behind oscillations, delays and phase, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: derive trajectories from reactions and distinguish transient from asymptotic behavior.

### Core idea and biological meaning

Sustained rhythms require a mechanism continually regenerating variation. Delayed negative feedback, coupled activator–repressor circuits and cell-cycle models can oscillate in some parameter regimes, but a transient overshoot is not a limit cycle. Sampling interval and observation length strongly influence apparent periodicity.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Simulate a simple delayed-repression analogy and inspect peaks under long observation. Change the sampling interval and show how aliasing can transform a high-frequency cycle into an apparently slower one.

**Model construction.** Write the direction of every process, determine whether a conserved sum exists, and distinguish the early transient from the eventual state. If no equilibrium is expected, define the observation window and the cause of sustained variation. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A spectral peak in a short noisy series is not proof of an endogenous oscillator; external forcing and measurement drift can produce peaks.

**Targeted improvement.** Compare unforced and forced traces, quantify phase consistency across cycles and inspect whether amplitude persists after initial conditions are forgotten.

**Conservation and resource limits.** Check which species, energy carriers or shared components are conserved or supplied by the environment. Balance equations should be obeyed before calibrating unknown parameters; otherwise an optimizer may compensate for a missing reaction. A conservation residual can be a more decisive model-quality diagnostic than a small discrepancy in the plotted outcome.

### Worked synthetic numerical case — Toy angular frequency to period

The input values are invented solely for instruction: `omega = 2`. Apply `2*pi/omega` and obtain **3.141593 time units**. Mathematically oscillatory frequency does not prove a real biological oscillator. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of the shape of one time series cannot identify a unique underlying circuit

### Concept transfer and practice problems

**Transfer setting.** Consider synchronized cell populations, where aggregate rhythms can vanish because individual oscillators drift out of phase.

1. **Inference design.** What control can separate circadian entrainment by a daily cue from an autonomous cellular clock? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `2*pi/omega` from the fictional inputs. *Answer:* **3.141593 time units**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Lesson 3.5 — Stability, equilibria and perturbations

**Learning goal.** Explain the mechanism or formal representation behind stability, equilibria and perturbations, identify its observable outputs, and name a perturbation that could refute the preferred explanation. This contributes to the unit objective: derive trajectories from reactions and distinguish transient from asymptotic behavior.

### Core idea and biological meaning

Equilibria are states at which model derivatives vanish; stability concerns what happens after a small displacement. Jacobian eigenvalues describe local behavior for differentiable ODEs, but local stability does not imply global safety or absence of large excursions.

To turn this principle into an analysis, specify the **estimand or desired prediction** before choosing equations or graph statistics. Is the target a steady concentration, a response trajectory, a flux range, an event probability, or a tissue-level average? These outputs answer different biological questions. Record the intended validation comparison before seeing model output.

### Fictional biological example

Study a two-variable feedback model with a stable fixed point. Perturb each variable separately and compare recovery trajectories; a slow eigenmode can dominate late-time behavior.

**Model construction.** Write the direction of every process, determine whether a conserved sum exists, and distinguish the early transient from the eventual state. If no equilibrium is expected, define the observation window and the cause of sustained variation. State which quantities were inserted by assumption and which hypothetical measurements could constrain them. Compare its output with a plausible alternative explanation.

### Assumptions and competing explanations

**Topic-specific risk.** A numerically converged simulation can appear stable because the timestep is too large to resolve an instability or because a trajectory never enters a competing basin.

**Targeted improvement.** Check fixed-point residuals, integration tolerance and local linearization; test multiple initial conditions when nonlinear effects are plausible.

**Nonlinearity and thresholds.** Compare the behavior of the model around a nominal input with its behavior at the edges of the intended input range. Saturation, cooperativity and alternative attractors can make a local approximation unreliable. Testing both increasing and decreasing interventions can reveal memory or threshold behavior invisible to a one-directional sweep.

### Worked synthetic numerical case — Return time of a stable mode

The input values are invented solely for instruction: `eigen_real = -0.5`. Apply `1/abs(eigen_real)` and obtain **2 minutes**. The one-mode approximation is local near a stable equilibrium. Check the result with units and a rough order-of-magnitude estimate, then vary one input and predict which way the answer moves before doing arithmetic. A mathematically correct result is a claim about the stated formula; biological validity requires an independent comparison with meaningful measurements.

### Interpretation, failure diagnosis and model comparison

For this example, explicitly separate **structural uncertainty** (which interactions exist), **parameter uncertainty** (the numbers attached to an assumed structure) and **observation uncertainty** (how real signals would be recorded). An excellent fit cannot by itself settle which mechanism generated an observation.

Use the targeted improvement above to construct two competing predictions: one from the preferred account and one from a model where its vulnerable assumption is relaxed. Name the readout and conditions under which the explanations disagree. If they remain observationally equivalent, seek a different data type. Return to the question of the shape of one time series cannot identify a unique underlying circuit

### Concept transfer and practice problems

**Transfer setting.** Relate these ideas to ecosystem tipping points and cell fate transitions without claiming a single shared cause.

1. **Inference design.** Can a system recover from small disturbances but switch permanently after a sufficiently large shock? *Guidance:* make the readout and intervention explicit, and identify an alternative cause of the same observed change.
2. **Recalculation.** Reproduce `1/abs(eigen_real)` from the fictional inputs. *Answer:* **2 minutes**. Describe the assumption necessary for interpreting that number.
3. **Model discrimination.** Describe a less detailed and a more detailed representation of this system. What measurable difference would justify the more detailed model? *Guidance:* detail is warranted when it improves falsifiable predictions, not when it merely adds entities.
4. **Stress testing.** Name one variable that could change with time or cell context although the original example kept it fixed. Outline a repeat measurement that would reveal the problem. *Guidance:* think about feedback, conservation, hidden mixtures, time delays and measurement artifacts.

## Integrated synthetic investigation: A feedback module under alternate inputs

**Scenario and deliverable.** Specify a two-state activator–inhibitor model and compare step, ramp and pulse inputs using a shared initial condition. Report transient amplitude, time-to-peak and steady behavior where the latter exists.

**Classroom data and assumptions.** The invented pulse lasts 3 minutes, the monitored response is sampled every 0.5 minutes, and a control series is sampled every 5 minutes. The numbers are invented; no external study or real patient data are implied. Before writing a model, create an explicit table of variable names, units, sampling intervals, boundaries and what could be observed independently. Mark any rate constant not inferred from these data as an assumption or sensitivity-analysis input, not an estimate.

**Implementation.** Draft the smallest system that can answer the investigation. If a network is used, keep evidence and edge types with the graph; if a differential equation is used, record its initial condition and units; if a simulation is random, preserve the seed and summarize distributions. Document the exact quantity compared with the fictional measurements. Avoid modifying a large set of free parameters until the first plausible curve appears. Instead, report at least two scientific hypotheses with predicted points of disagreement.

**Stress test.** Explain how the coarse observation interval could miss a transient or alias a periodic response. Include local conservation or positivity checks. Identify which claim survives when an uncertain parameter is varied, and which claim depends on a narrow condition. Propose an independently measurable perturbation that would distinguish your preferred mechanism from at least one alternative. A model that is highly accurate only for the supplied invented numbers is still not externally validated.

**Submission checklist.** Include (a) a one-paragraph biological question; (b) a boundary diagram or reaction list; (c) units and formulas; (d) at least one hand calculation; (e) one reproducible table or plot; (f) a falsifying observation; (g) two limitations; (h) a concise conclusion that states the simulation result without overstating its biological significance.

**Instructor rubric.** Award 25% for mechanistic clarity and appropriate scope, 20% for transparent equations/units, 20% for correct numerical work and reproducibility, 20% for competing explanations and tests, and 15% for responsible interpretation. A polished plot does not compensate for an invalid conservation relation or a claim of measurement where there was only simulation.

## Interactive teaching models

Two offline manipulable models accompany this unit: **First-order clearance** and **Idealized feedback attenuation**. Their equations are documented in `MODELS.json` and displayed beneath each control in the HTML reader. Vary one slider, describe the change and explain why the curve is a mathematical illustration rather than a measurement-based prediction. In particular, compare the default value to values at the edges of the slider; note which model assumptions would require reconsideration outside this idealized domain.

## Unit-level review and deeper synthesis

A complete systems explanation combines representations, a correct mathematical operation, an observable and uncertainty in the connection between them. Start a critique by listing all numbers that came from observation and all numbers inserted to make the demonstration run. Treat those lists differently. A fitted model should not be evaluated solely by how precisely it reproduces the observations that determined its parameters. A diagram derived from correlations should not be narrated as proven regulation. A simulation derived from exact event rules should not be called experimental replication.

The most transferable skill is the ability to identify what would change a conclusion. Examine a missing component, an alternate input schedule, a different scale of aggregation and a parameter range the original demonstration did not include. One of those variations may leave the answer almost unchanged, supporting a narrow form of robustness. Another may reverse the answer, revealing an assumption that deserves emphasis. A responsible report describes both outcomes without converting uncertainty into false confidence.

### Recommended independent study

Return to the five lesson problems and attempt them without viewing their guides. For one lesson, annotate a peer-reviewed system model from a source you can lawfully access: identify the state variables, model assumptions, measurement system, code availability, a numerical property that can be checked, and a biologically distinct experiment that was not included in the calibration. Do not copy a published model into this educational manuscript without respecting its license and attribution conditions.
