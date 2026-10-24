# Unit 1: Intelligent agents

*Editorial draft; not approved for live publication.*

## State Representations
**State Representations: conceptual explanation**

### State design is a hypothesis about what can influence the future
An autonomous agent does not act on reality directly: it acts on an internal description constructed from observations. In a delivery robot, the current floor cell might be encoded as a pair of integers, but a truly useful state also includes orientation, battery charge, carried payload, elevator access, and perhaps an estimate of whether a corridor is occupied. The purpose is not to store everything imaginable. It is to store enough information that two histories assigned the same state really lead to the same relevant future possibilities. This is the Markov property relative to a chosen decision process: after conditioning on the state and action, earlier history should not add predictive information about the next state. The property is an assumption to evaluate, not a slogan attached to any data structure.

Represent the agent as a transition system with state set S, actions A, a transition function T:S×A→S for deterministic environments, and an observation function O. In a stochastic model replace T by a conditional probability T(s'|s,a). If a location consists of 12 rows and 10 columns, four headings and six discretized battery levels, the naive Cartesian representation contains 12×10×4×6=2880 states before carrying status is represented. Adding a Boolean load flag doubles that count. Yet walls make some positions unreachable, and incompatible combinations may never occur. Thus the Cartesian product is an upper bound on syntactic configurations, not a count of reachable states. Breadth-first exploration from the initial state can establish reachability in a finite deterministic abstraction. The corresponding simulation must not imply that counting variables discovers which configurations can occur physically.

An example of state aliasing arises when a cleaning robot stores its location but not whether a floor patch has already been cleaned. Two histories produce identical locations with different work remaining. A policy based only on location cannot always decide whether to revisit. Add a cleaned-cell bitmask or maintain a belief about unobserved cleanliness. A bitmask for 20 cells has 2^20 possible assignments; this is a reason to exploit spatial structure, not a reason to ignore the missing information. In a bounded laboratory, build two trajectories that reach the same encoded location with different target completion. If the controller prescribes the same action where different actions are required, you have found a representational failure.

Continuous variables introduce another tradeoff. Discretizing battery charge into 10% buckets reduces the state count but may hide a critical threshold: at 10.1% and 19.9% battery the robot may have different ability to return home. Test behavior near bin boundaries, and report the quantization scale whenever a simulation displays a state count. Encodings are design choices whose information loss should be measured against the decisions they support.

## Objectives
**Objectives: conceptual explanation**

### Goals, reward functions, utility, and incentives
A goal predicate describes whether a terminal situation is acceptable. A cost function evaluates paths, perhaps combining travel distance, energy expenditure and deadline penalties. A utility function orders consequences, while a reinforcement-learning reward is a numerical feedback signal accumulated through experience. These objects are related, but they are not interchangeable. A path planner that minimizes meters traveled may violate delivery time windows; a robot that receives one unit of reward per movement may deliberately wander; a support assistant optimized for conversation length may avoid resolving a customer's issue. The objective must represent the service outcome rather than an easily manipulated surrogate.

Consider a vehicle-routing agent choosing paths p. Let travel time t(p) be measured in minutes, expected energy e(p) in watt-hours, and lateness ℓ(p) in minutes. A weighted cost C(p)=t(p)+0.02 e(p)+5ℓ(p) is interpretable only after saying that one watt-hour is assigned the equivalent cost of 0.02 minutes and one minute late is assigned five minutes of penalty. Such weights express policy preferences, not physical laws. For a path taking 30 minutes, 100 Wh and zero lateness, C=32. A path taking 27 minutes, 120 Wh and two late minutes has C=39.4, so the first path wins despite being longer. The numerical result follows from the chosen units and coefficients; different organizational priorities could reverse the ranking.

An agent under uncertainty may maximize expected utility E[U(a,X)] over outcomes X, rather than act on average outcome values. Suppose one route arrives on time with probability 0.9 and yields utility 100, but a late outcome yields -200. Its expected utility is 0.9×100+0.1×(-200)=70. A reliable route delivering utility 65 on every run is slightly worse under expected utility, although a risk-averse stakeholder might prefer it. Risk-sensitive objectives can penalize tail losses or impose probability constraints. A technical report should state whether the choice maximizes expected reward, worst-case reward, or a risk-aware criterion.

Reward hacking can be tested adversarially. Define a toy support environment in which an agent earns points each time a user sends a message. The easiest policy may become asking unnecessary questions. The fix is not merely increasing the message reward's coefficient; it is a redesign that ties success to verified issue resolution, appropriate user consent and bounded interaction costs. Even then, success labels can be corrupted. Distinguish the mathematical optimizer's obedience to the supplied objective from the designer's obligation to specify the right objective.

In sequential decisions a discounted return G_t=∑_{k=0}^{∞}γ^k r_{t+k+1} with 0≤γ<1 weights near-term rewards more heavily. Discounting can represent timing preferences or aid mathematical convergence, but may disfavor long-delayed maintenance and safety. Compare policies under several γ values before treating an optimized action as rational.

## Environments
**Environments: conceptual explanation**

### Environment taxonomy and where assumptions break
An agent's environment can be fully or partially observable, deterministic or stochastic, episodic or sequential, stationary or changing, discrete or continuous, and single-agent or multi-agent. These are modeling dimensions, not labels of prestige. A board game is commonly discrete and turn-based; a warehouse robot navigates continuous motion with uncertain perception; a recommender operates in a changing environment where users respond to the recommendations themselves. State which idealization is being used before selecting an algorithm.

A fully observable controller receives the state required for optimal action selection at every step. A partially observable controller receives observations o whose distribution depends on the hidden state. It maintains a belief distribution b_t(s)=P(s_t=s|o_{1:t},a_{1:t-1}). In a small two-room robot problem, suppose the robot believes a target is in room A with probability 0.6 and in room B with probability 0.4. A noisy sensor reports A with sensitivity 0.8 and false-positive probability 0.3. After observing an A report, the posterior probability the target is actually in A is (0.8×0.6)/(0.8×0.6+0.3×0.4)=0.8. The posterior is not certainty; an agent must still account for inspection cost and remaining risk.

A deterministic grid planner can return a valid shortest path under a fixed obstacle map. On a real sidewalk, moving forward may fail because a pedestrian blocks the way, a wheel slips, or the map is outdated. A stochastic transition matrix distributes probability over successor states, allowing the planner to compare expected costs. A robust planner can instead optimize over a set of plausible transition models. These choices have different guarantees. A probability distribution trained on past weather is not a promise about unprecedented storms, and a worst-case planner may become overly conservative if its uncertainty set is unrealistic.

Multi-agent environments create strategic dependence. A ride-hailing allocator changes traffic demand, and competing allocators adapt. A policy evaluated against one frozen opponent is not necessarily optimal against an adapting opponent. Likewise, a customer-support model that changes the information customers provide violates a static-data assumption. When building a simulator, keep an explicit switch between static and changing environments and explain which causal feedback is absent.

An environment audit should enumerate observations, available actions, time steps, hidden variables, failure modes and the source of uncertainty. Students can implement three versions of a navigation game: known deterministic map, stochastic movement, and hidden map requiring sensing. Compare both success rates and action costs under identical initial conditions. The lesson is that an algorithmic result is conditional on the environment class; transferring it requires an argument about preserved assumptions.

## Rationality
**Rationality: conceptual explanation**

### Rational action selection and computational limits
A rational agent chooses actions expected to do best under its information, model, performance measure and computational resources. Rationality is not omniscience and does not require flawless outcomes. A weather-based delivery policy can be rational before a surprise storm and still fail on that trip. Conversely, a lucky random choice is not proof of rationality. Evaluation should ask whether the policy uses the available evidence and objective consistently, rather than whether one outcome looked favorable.

The idealized optimal policy for a fully observable finite-horizon Markov decision process obeys Bellman's recurrence V_t(s)=max_a [r_t(s,a)+∑_{s'}T(s'|s,a)V_{t+1}(s')]. The final-time value is specified by the terminal reward. To compute V_t, enumerate candidate actions, aggregate immediate reward and future value under each successor probability, then choose the maximizing action. In a one-step example, action A yields reward 4 surely; action B yields reward 12 with probability 0.5 and -6 otherwise. The expected immediate reward for B is 0.5×12+0.5×(-6)=3, so A is preferable under expected reward. If B also leads to a valuable state tomorrow, this one-step comparison may change.

Exact dynamic programming can be infeasible because the number of states and actions is huge. A bounded agent may use a heuristic, a learned value approximation, sampled rollouts or a receding-horizon controller. This introduces a difference between theoretical optimality and operational bounded rationality. A useful benchmark records planning time, peak memory, expected objective value and safety constraint violations. Faster decisions are only better when the cost of computation and the stakes of delay justify the lost solution quality.

Policies should be tested under distribution shift. Train a route policy on light traffic, then increase the frequency of delayed intersections while keeping the goals unchanged. The policy's original expected-value guarantee does not automatically apply because the transition probabilities have changed. Distinguish errors from model mismatch, planning approximation, stochastic bad luck and contradictory objectives. Their remedies differ: recalibration, deeper search, more robust constraints and revised goals respectively.

For safety-critical agents, actions may be filtered by a separate guard. The optimizer proposes a movement; a collision-avoidance controller rejects it if a validated sensor-based bound would be violated. Such separation can make failures easier to diagnose, but guard reliability depends on its own assumptions and sensor faults. A 'rational' utility score is never a substitute for testing requirements imposed outside the reward function.

## Integrated Case Study and Model Limitations
**Integrated investigation for Intelligent agents.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Integrated case study: a campus delivery agent
A campus delivery robot must move medical samples between three buildings before a deadline. Define its state as (node, heading, battery-bin, load-flag, delivery-progress) and its actions as move, wait, charge, pick up, and drop off. Transition constraints include passable edges, charge-station locations and battery consumption. Objectives are not simply shortest path: some samples have maximum transit temperatures and strict delivery deadlines. A planning program that finds the geographically shortest path can be operationally invalid.

Start with a small graph with nodes Depot, Clinic, Laboratory and Charger. Edges Depot–Clinic and Clinic–Laboratory each take five minutes and consume ten energy units; Depot–Charger takes two minutes and consumes four energy units; Charger–Laboratory takes eight minutes and consumes 16 units. Starting energy is 18 units, so Depot–Clinic–Laboratory is infeasible without a recharge although its travel time is ten minutes. Record preconditions before scoring paths. If the robot must first pick up a sample at Clinic, Depot–Charger–Laboratory is not a valid alternative either. This illustrates why cost optimization after constraint checking is different from blindly comparing path lengths.

Construct a simulator with separate panels for state-space upper bound and reachable states, and never call the former the latter. Add a policy comparison showing what happens when battery is ignored versus included. For each policy log action, observed state, estimated hidden state, remaining resource and violated constraint if any. Inject three faults: a closed corridor, a delayed elevator and a battery sensor reading with a fixed positive bias. Measure task completion, not animation smoothness. On failure, identify whether the cause lies in the state encoding, transition model, objective or search method.

A responsible deployment design includes a stop command, human escalation, a defined communications-loss policy and retention limits for location data. The robot should not claim a medical safety approval based on simulation tests. The case illustrates a recurring design principle: an agent is a chain of assumptions and controls, and a good academic example explains how each link can fail independently. Student reports should include one counterexample where a simpler representation produces a demonstrably wrong decision.

### Research exercise: discover the right state abstraction
A designer proposing an agent state should be able to argue that the stored variables support every distinction necessary for the decision. Consider an autonomous lift delivering packages among four floors. Its state records floor, direction, door-open flag and remaining capacity. Suppose the service must prioritize passengers who have waited the longest. Two histories can lead to identical stored lift configurations even when one floor has a passenger waiting for two minutes and another for ten. The encoded state does not contain elapsed waiting time, so an action-selection policy based only on that representation cannot always implement the intended priority. Adding per-floor waiting time changes the available decisions, but also enlarges the state and creates privacy and clock-synchronization obligations. The engineering tradeoff is between adequacy and manageable complexity.

One systematic method is to begin with a specification rather than a guess at variables. Write the decision outcomes as properties of future trajectories: every requested pickup is eventually handled subject to feasible capacity, unsafe door openings never happen, and average wait time is minimized subject to a maximum-wait guard. Next choose candidate state variables and attempt to construct pairs of feasible histories that collapse to the same state but require different optimal actions. This is a counterexample search for state sufficiency. A successful counterexample shows the representation is too coarse. Failure to find one in a bounded simulation is not proof that none exists in the unbounded system. State abstraction can also deliberately ignore distinctions that provably do not affect relevant reward or transition probabilities.

### Occupancy, belief and limited sensing
The lift controller might know its own floor and passenger count exactly while only observing hall buttons, not the number or patience of waiting passengers. Model hidden demand with a belief state and test how it evolves when a door opens without anyone boarding. Such an observation could mean the request was cancelled, a person was too slow to board, or a sensor failed. A belief update should retain more than one hypothesis when the observation model allows several explanations. If sensors report 'nobody waiting' with 90% probability when the floor is empty but with 15% probability when someone is present, the controller's posterior depends on the prior and on both likelihoods. An empty-looking floor is not certain evidence of zero demand.

For a useful experiment, create a two-floor abstraction with one outstanding request, two possible passenger-demand states and two actions: travel or wait. Supply a state transition table and a reward table that penalizes energy and excessive waiting. Compute exact one-step action values for each belief by hand, then implement a numerical controller. Verify normalization of every transition row and observation distribution. Next deliberately omit waiting-time history, demonstrate an ambiguous case, and report what extra variable repairs the ambiguity. This is more informative than simply plotting the exponential number of hypothetical state combinations.

### Safety and performance are separate claims
A controller may minimize average waiting time while occasionally commanding a dangerous door state; such an outcome is unacceptable even if its reward total is high. Specify an invariant that doors remain closed during travel. Implement the invariant as a precondition for every movement action and assert it after every transition. Test a faulty action that opens doors during motion and ensure the validator rejects it before the simulation updates the state. An agent with correct average-case decision theory can still have a defective transition engine or unsuitable constraints. Evaluation should therefore report invariant violations separately from reward.

Benchmark two policies across the same demand traces: nearest-request-first and oldest-request-first. Record average wait, maximum wait, energy proxy, number of unfinished requests and policy runtime. Use deterministic pseudo-random seeds so different policies see the same arrivals. Explain that the simulator may omit mechanical acceleration, actual elevator regulations and human unpredictability. These omissions prevent any real safety guarantee. The lesson is how to connect internal representations and objective choices to observations and verifiable consequences, not how to certify lift equipment with classroom code.

### Counterfactual policy evaluation
A final investigation varies one assumption at a time. Increase sensor false negatives while keeping arrival frequency fixed; compare policy choices. Then increase waiting-time penalty while holding the observation model fixed; compare the same traces. If both variables change simultaneously, the source of performance improvement becomes ambiguous. A well-designed report includes assumptions, exact rules, representative traces, confidence intervals where random trials are used, and at least one carefully analyzed failure case. The smallest model that illustrates a real distinction is often more educational than a high-fidelity animation whose correctness cannot be independently checked.

### Independent state-abstraction proof check
A useful formal check compares two proposed encodings: full state s and compressed state z=φ(s). For the compressed representation to preserve a chosen decision process exactly, states mapped to the same z must have compatible rewards and aggregated transition probabilities over equivalence classes for every action. If s1 and s2 map to the same z but taking action a yields different immediate rewards, an optimal compressed policy can be impossible even with perfect search. A classroom example assigns the same location to a loaded and unloaded robot while delivery reward depends on carrying status. The contradiction is structural: no single action value for that compressed location represents both original cases. Students can test pairs exhaustively in a finite toy model and report the first failed condition. That is stronger evidence than plotting a state count or observing several successful trajectories.

### Worked question: Finite agent-state count
A robot can occupy 8 floor cells, face any of 4 directions, carry or not carry a parcel, and have one of 5 discrete battery levels. How many representable states are there, and does that number equal reachable states?

**Model the question**
A state is one tuple (cell, heading, carry flag, battery bin). The question specifies a Cartesian representation, so the multiplication principle applies to each independent field in the encoding.

**Calculate or derive**
Multiply 8×4×2×5=320 possible tuples. This number is a syntactic upper bound; a rule may forbid some combinations, such as a robot in a walled-off cell or a parcel already delivered while carried.

**Check assumptions and boundaries**
A reachability claim requires the initial state and legal action transitions. Enumerating 320 encodings alone cannot establish that all are reachable. Test with a blocked cell, which would remove at least some tuples from the reachable set.

**Answer:** There are 320 representable tuples; reachable-state count cannot be determined from the question alone.

### Worked question: Expected utility versus worst case
An agent can choose A, which yields utility 5 for sure, or B, which yields utility 14 with probability 0.6 and utility -6 otherwise. Which action maximizes expected utility?

**Model the question**
Write expected utility using mutually exclusive outcomes and the supplied probabilities. For A the result is 5 because its sole outcome has probability one.

**Calculate or derive**
For B, EU(B)=0.6×14+0.4×(-6)=8.4-2.4=6. Thus EU(B)>EU(A), and an expected-utility maximizer selects B. The arithmetic uses utility units, not guaranteed currency.

**Check assumptions and boundaries**
B has a worse minimum outcome (-6) than A (5). A maximin decision maker would select A, showing that the decision depends on the criterion, not an arithmetic contradiction.

**Answer:** Expected utility selects B with value 6; a worst-case criterion would select A.

### Worked question: Observation update for a hidden target
A target is in room A with probability 0.7. A sensor reports A with probability 0.8 when the target is in A, and 0.1 when it is in B. Compute P(A|report A).

**Model the question**
Let H mean the target is in A and E mean that the sensor reports A. Priors are P(H)=0.7 and P(not H)=0.3; likelihoods are P(E|H)=0.8 and P(E|not H)=0.1.

**Calculate or derive**
Bayes gives P(H|E)=0.8×0.7/(0.8×0.7+0.1×0.3)=0.56/0.59≈0.94915. The denominator includes both ways the observed signal could occur.

**Check assumptions and boundaries**
The posterior is below one because false positive signals remain possible. Changing the prior to a very low value would reduce the posterior despite identical sensor sensitivity.

**Answer:** P(target in A | report A)≈94.915% under the specified model.
