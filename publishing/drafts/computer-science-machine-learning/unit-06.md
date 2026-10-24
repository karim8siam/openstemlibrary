# Unit 6: Sequential decision learning

*Editorial draft; not approved for live publication.*

## Bandits
### Bandits

### Bandits separate exploration from reward collection
A multi-armed bandit chooses among actions with initially unknown reward distributions. Unlike a full Markov decision process, the classical stationary bandit assumes an action produces a reward without changing an evolving state that drives future rewards. The learner must balance exploiting the currently most promising option with exploring uncertain options. Always choosing the arm with the highest sample mean can lock into a poor option after unlucky early rewards. Always exploring uniformly wastes opportunities once one option is clearly superior.

An epsilon-greedy strategy chooses a random action with probability epsilon and the current best empirical action otherwise. Its simplicity makes it a useful baseline, but fixed epsilon continues random exploration even after ample evidence has accumulated. Upper-confidence strategies add uncertainty bonuses, while Thompson sampling draws action-value hypotheses from posterior distributions and selects the action best under the sampled world. Their guarantees depend on reward assumptions, stationarity, independence and correct implementation. A claimed regret bound without identifying the model class can mislead.

Define cumulative regret relative to the oracle arm with highest expected reward: E[Regret(T)]=T mu_star-E[sum_{t=1}^T r_t]. In an environment where arm A pays Bernoulli mean .6 and arm B pays .4, choosing B incurs .2 expected regret that round. If a ten-round experiment chooses B four times, the expected regret conditional on those choices is .8, although realized rewards can fluctuate and may temporarily favor B. Report aggregate performance over many seeded simulations; one lucky run does not establish an algorithm is superior.

### Practical guardrails
A promotional experiment may want to optimize purchases, but an algorithm that explores aggressive discounts can change the customer's future behavior or create unequal exposure. Specify budget, eligibility and safety constraints before exploration. For a toy simulator, draw Bernoulli rewards from fixed seed streams, compare epsilon-greedy, UCB and uniform exploration, and plot regret with confidence bands. Then switch the reward probabilities halfway through the run to demonstrate why a stationary learner can become stale. The shift changes the problem class; algorithms may need discounting or change detection.

### Regret bounds do not remove policy constraints
Many classical bandit regret bounds are asymptotic or depend on bounded rewards, independent draws and stationarity. In a small real deployment, constants and transient behavior can dominate the asymptotic expression. An algorithm that explores enough to achieve sublinear long-run regret may still violate a short-term budget or safety rule. Model cumulative spend and constrained actions alongside regret. For an advertising experiment, the responsible comparator may be the best policy within budget and eligibility constraints rather than the unconstrained best expected reward arm. Test whether the model's exploration probability causes unacceptable short-run losses. Report distribution of outcomes across seeds, not just mean regret. A low average can coexist with a small fraction of costly runs that an operator cannot tolerate.

## Markov Decision Processes
### Markov Decision Processes

### Markov decision processes model consequence and delay
A finite Markov decision process is defined by states S, actions A, transition probabilities P(s'|s,a), rewards r(s,a,s') and a discount factor gamma where appropriate. The Markov assumption says the next-state distribution depends on the current state and action rather than all previous history. Whether a proposed state is sufficient is an empirical and modeling question. Inventory position alone may not be Markov if supplier lead times or outstanding orders are omitted.

A policy pi(a|s) chooses actions in states. For a discounted infinite-horizon objective, V^pi(s)=E_pi[sum_{t=0}^infty gamma^t r_t |s_0=s]. The Bellman expectation equation expresses this value in terms of one reward plus gamma times the next state's value. The optimality equation replaces averaging over prescribed actions with maximizing over available actions. Value iteration repeatedly applies this Bellman optimality operator; under standard finite, bounded-reward and gamma<1 assumptions it is a contraction in the sup norm.

The discount factor changes preferences, not merely numerical stability. In a simplified decision, earning 8 immediately versus 10 one step later favors the delayed option when 10 gamma>8, or gamma>.8. However, if the future reward arrives only with probability .7, expected delayed value is 7 gamma, so it cannot beat 8 for gamma≤1 without other benefits. Expected utility under the assumed model is not a real-world safety guarantee: tail risk, time limits and constraint violations may matter separately.

### Transition audit
For a two-state machine model with state Healthy or Faulty, write each action's transition probabilities as a row summing to one. Specify whether repairs reset the condition, whether failures can occur immediately after repair, and what monitoring costs. Check all nonnegative probabilities and exact normalization before running value iteration. Compare decisions when the failure penalty doubles. A simulation that merely plots V without showing the transition assumptions cannot explain why its policy changed.

### Value iteration termination and residual bounds
Under a finite discounted MDP with gamma<1, the Bellman optimality operator is a contraction. An implementation can monitor the maximum change between successive value estimates, but a small update difference is not automatically identical to a desired policy-value accuracy unless the relationship and discount factor are considered. With gamma close to one, a given Bellman residual permits a larger value error than with a smaller gamma. Specify the stop tolerance and any associated bound; do not simply terminate after an arbitrary ten iterations. Validate a two-state toy MDP by direct algebra and compare the iterative result. Every transition row must be a valid probability distribution and illegal actions must be excluded or handled explicitly. A solver can converge perfectly to the wrong answer if the transition table itself encodes the wrong environment.

## Reinforcement Learning
### Reinforcement Learning

### Reinforcement learning estimates action values from experience
Reinforcement learning becomes relevant when transition dynamics or rewards are not fully known and an agent learns through interaction or logged experience. In tabular Q-learning, the update is Q(s,a) <- Q(s,a)+alpha[r+gamma max_a' Q(s',a')-Q(s,a)] for nonterminal transitions. This is an off-policy temporal-difference target because the next-state action comes from a greedy maximization even when behavior chose a different action. SARSA instead uses the actual next behavior action, which can lead to more cautious behavior under exploratory policies.

In finite tabular settings, convergence results require conditions such as sufficient state-action visitation and suitable diminishing step sizes. With function approximation, bootstrapped targets and off-policy data, training may become unstable. Replay buffers and target networks are practical techniques in some deep Q-learning systems, but they do not universally guarantee convergence. Policy-gradient methods optimize parameterized stochastic policies using estimates of expected return gradients; actor-critic methods learn both a policy and a value-like baseline.

The objective must be evaluated with real operational constraints. Training a warehouse robot by trial and error in the physical building could damage equipment; use simulation, offline data or a safeguarded exploration regime. Simulators omit friction, unmodeled humans and sensor faults, creating a sim-to-real gap. Reward shaping may accelerate learning but can unintentionally change the optimal policy unless conditions such as potential-based shaping are met.

### One update calculation
Suppose Q(s,a)=2, observed reward r=3, next-state maximum Q=4, gamma=.9 and alpha=.1. The target is 3+.9×4=6.6; temporal-difference error is 4.6 and updated Q=2+.1×4.6=2.46. If the transition is terminal, the bootstrap term should vanish and the target becomes 3. Plot the update for alpha values and test the terminal branch separately. The arithmetic verifies an implementation step, not the quality of a learned policy.

### Q-learning terminal transitions and replay artifacts
A terminal transition has no bootstrap continuation in the standard episodic Q-learning update. Accidentally using a Q value from a reset state can inflate estimated returns and alter learned behavior. Store an explicit terminal flag with each logged transition, and distinguish genuine termination from a time-limit truncation if the task's objective continues beyond that truncation. Replay sampling can overweight common states and underrepresent rare safety events. Prioritized replay changes the sampling distribution and may require importance corrections. Neither a larger replay buffer nor more network parameters guarantees better value estimates. For a tabular test environment, enumerate all legal state-action pairs and compare learned Q values against a dynamic-programming reference as training proceeds. Check convergence under several seeds and exploration schedules rather than inspecting one visually smooth reward curve.

## Exploration
### Exploration

### Exploration and off-policy evaluation have hidden assumptions
An agent collecting data with a behavior policy b(a|s) does not automatically have enough evidence to evaluate another policy pi. If the behavior never chooses an action that the candidate policy might choose in a state, the corresponding outcome cannot be learned from logged data without additional modeling assumptions. This is the support or positivity problem. Importance sampling weights trajectories by likelihood ratios between target and behavior policies, but weights can explode over long horizons and create high variance.

Safe exploration may impose hard constraints: a medical recommendation learner cannot knowingly assign hazardous actions just to estimate their outcomes. Conservative policy improvement and constrained reinforcement learning attempt to control risk while learning, but valid guarantees depend on correct uncertainty estimates and environment assumptions. Offline reinforcement learning must distinguish counterfactual estimates from outcomes actually observed under the logging policy.

Exploration should be quantified in terms of what was unknown before collection and how uncertainty is reduced. A random action can be expensive and uninformative if it visits irrelevant states. Conversely, overconfident exploitation can prevent discovery of rare failure regimes. Measure state-action coverage, effective importance-sampling sample size and conservative lower bounds when possible. Reports should show the behavior policy version and propensity logging, otherwise off-policy conclusions may be irreproducible.

### Policy evaluation laboratory
Suppose the logging system chooses action A with probability .8 and B with .2, while a proposed target policy chooses them .5 each. For a logged B action the one-step importance ratio is .5/.2=2.5; for A it is .5/.8=.625. A few B samples can dominate a weighted estimate. Calculate the effective sample size (sum w)^2/sum w² and compare it with the raw number of observations. Repeat after incorrectly setting the behavior propensity of B to zero and explain why the target policy no longer has empirical support.

### Why importance weights can explode
For a sequence of actions a_1...a_T, ordinary trajectory importance sampling multiplies ratios pi(a_t|s_t)/b(a_t|s_t). Even moderate ratios accumulate dramatically. If a ratio equals two at each of ten steps, the trajectory weight reaches 1024. A small number of such trajectories can dominate the estimate. Weighted importance sampling normalizes the weights and may reduce variance while introducing finite-sample bias. Per-decision methods can sometimes improve efficiency by stopping the product at relevant times. Report effective sample size, weight quantiles and whether critical actions lack behavior support. Off-policy evaluation of a dangerous action cannot be made safe merely by clever weighting when no comparable historical outcomes exist. In such cases, models and domain assumptions must be treated as unverified extrapolation, and an expert-controlled experiment may be the only defensible way to collect evidence.

## Integrated technical investigations and review
# Integrated investigation for Sequential decision learning

### Bellman errors, approximation, and unstable bootstrapping
Temporal-difference learning updates an estimate toward a target that uses other estimates. In tabular Q-learning, this bootstrap structure can be effective because the finite state-action table is revisited repeatedly under suitable assumptions. With a deep network, the same parameters may influence both the current estimate and the target, causing moving-target instability. A target network freezes one copy of parameters for several updates in some algorithms. Replay buffers reduce correlations between adjacent experiences, but the replay distribution can also overrepresent obsolete states or historical policies.

Value overestimation may arise when a maximum over noisy action estimates favors accidentally high errors. Double-estimator approaches aim to separate selecting an action from evaluating its value, reducing one source of bias. They do not resolve reward misspecification or an unrealistic simulator. For every advanced method, keep a tabular or dynamic-programming baseline on a small exactly solvable environment. An agent that cannot solve the two-state case reliably has little basis for a claim of real-world autonomy.

### Credit assignment and delayed consequence
A reward can arrive long after the action that caused it. Discounted value functions propagate information through time, but sparse rewards can make learning inefficient. Reward shaping adds intermediate signals, while demonstration or model-based planning can guide exploration. Yet a shaped reward may create unintended goals: an agent rewarded for approaching a package might oscillate near the package rather than complete delivery if completion reward is mishandled. Check policy behavior under adversarial cases, not only average return.

The distinction between model error and policy error is critical. A planned trajectory may be optimal in the simulator but dangerous in reality if the transition model omits pedestrian behavior. Conversely, a robust policy may seem conservative on the simulated metric because it optimizes worst-case constraints. Report coverage of simulated conditions, not just number of training episodes. Domain randomization tests sensitivity to plausible variation but cannot cover unknown unknowns.

### Reward design with physical units
Suppose maintenance action costs 20 dollars and failure causes expected loss of 400 dollars. A policy that chooses repair based on estimated failure probability p might compare repair cost with expected unmitigated loss p×400 under simplifying assumptions. The naive break-even threshold is p>.05, but this ignores repair effectiveness, future maintenance cost, horizon length and uncertain failure severity. A full MDP models how repairs change future transition probabilities and discounted costs. Forbidding repairs due to budget or scheduling may require constrained optimization instead of a large penalty folded into reward.

A reward combining dollars, downtime minutes and safety incidents needs explicit conversion choices or a multi-objective report. Calling all rewards dimensionless and summing them is a mathematical convenience, not an escape from value judgments. Sensitivity analysis should vary the coefficients and show where the preferred policy changes. The effect of human oversight and legal obligations remains outside a simple numerical reward model.

### Safe offline evaluation as an identification problem
Logged interventions reflect the behavior policy and its own incentives. If operators never choose a risky action, there is no direct empirical evidence of its consequences in the log. A learned world model may extrapolate, but that is a modeling assumption, not observational proof. Importance sampling requires positivity and correctly logged action probabilities; doubly robust estimators rely on either a reliable behavior model or outcome model under particular formulations, not on magic cancellation of every bias.

Weight normalization can control variance at the expense of introducing bias. Long-horizon trajectory weights multiply conditional ratios, which can make a handful of rare trajectories dominate an estimate. Report effective sample size and confidence intervals. For policies controlling medical treatment, industrial machinery or transport, offline scores alone are insufficient evidence of safe deployment. Controlled pilots and domain-specific safety checks are necessary.

### Nonstationarity and contextual bandits
A contextual bandit uses observed context x to choose an action and gets partial feedback for the chosen option. When a content platform changes the items it displays, the logging policy shapes the observed dataset: unshown items receive no click labels from that impression. Standard supervised training on clicked and unclicked displayed items can be biased toward what the previous policy chose. Propensity-aware estimation can help under adequate support and logging accuracy, but the method must respect user consent and platform policy.

Nonstationarity complicates exploration. A promotion that worked last month may fail this month because competitors change prices or user preferences shift. Sliding windows or discounting old data can help adaptation, while reducing the effective sample size. Compare policies under both stationary and changing synthetic rewards, and quantify cumulative regret separately. A stationary bandit benchmark should not be used as proof of adaptation to a strategic opponent.

### Learning under a safety envelope
Specify forbidden state-action combinations independently of the reward optimizer. A robot that must not open its door while moving should enforce that rule in a verified safety layer rather than rely on a large negative reward when the rule is broken. A shield can filter proposed actions and replace invalid ones with safe alternatives; its own assumptions and fallback correctness require testing. Learning within such a constrained environment may reduce exploration freedom, which is an acceptable cost when safety matters. Describe the guarantee narrowly: a classroom invariant over finite states does not certify physical machinery under sensor failure.

### Separating reward learning from policy evaluation
A reinforcement learner may fail because it received insufficient exploration, because its value-function approximation is inaccurate, because the reward specification was misguided, or because the simulator was wrong. These root causes require different interventions. More training episodes cannot fix a reward that favors undesirable behavior, and a better neural architecture cannot validate an impossible transition model. Use an exactly solvable toy environment to check algorithms before moving to complex simulators. Compare learned values and policies with a dynamic-programming reference; then vary one assumption such as transition stochasticity or reward delay at a time. Store episode trajectories and random seeds so an unexpectedly successful run can be examined rather than merely celebrated. For real-world systems, document which actions remain prohibited independently of learned reward. Good sequential learning combines mathematical objectives, empirical coverage, verified safety constraints and operational oversight.

### Worked question: Bandit expected regret
Arm A has mean reward 0.6 and B has mean reward 0.4. In ten rounds an agent chooses the inferior arm B four times. Compute expected regret relative to always choosing A.

**Model the question**
Each B selection sacrifices .6-.4=.2 reward in expectation. Choosing A contributes zero expected regret under the stationary two-arm comparison.

**Calculate or derive**
Four selections of B contribute 4×.2=.8 expected cumulative regret. The other six selections of A contribute zero, so expected regret is .8.

**Check assumptions and boundaries**
Realized regret on a particular stochastic reward sequence can be negative or differ substantially because reward outcomes fluctuate. Expected regret here conditions on the stated choices and fixed arm means; if probabilities change, the oracle definition must change too.

**Answer:** Expected cumulative regret is 0.8 reward units.

### Worked question: One-step Q-learning update
Given Q(s,a)=2, reward r=3, next-state max Q=4, discount gamma=.9 and step size alpha=.1, find the nonterminal tabular Q-learning update.

**Model the question**
Write target r+gamma maxQ=3+.9×4=6.6. The temporal-difference error is target minus current Q, or 4.6.

**Calculate or derive**
Apply update Q_new=Q_old+alpha×TD_error =2+.1×4.6=2.46. The update moves only ten percent of the way toward the one-step bootstrap target.

**Check assumptions and boundaries**
For a terminal next state, maxQ term should be omitted; then target would be 3 and Q_new=2.1. Confusing terminal and nonterminal transitions can materially bias learned values. This computation does not establish convergence.

**Answer:** The updated Q(s,a) is 2.46.

### Worked question: Off-policy importance ratios
Behavior policy chooses A with probability .8 and B with probability .2, while target policy chooses both with probability .5. Compute one-step importance ratios for logged A and B actions.

**Model the question**
Importance ratio for action a is pi(a|s)/b(a|s) when b(a|s)>0. Both behavior action probabilities are nonzero, so ratios are defined.

**Calculate or derive**
For A the ratio is .5/.8=.625; for B it is .5/.2=2.5. B actions receive much larger weight because the target would choose them more often than the behavior did.

**Check assumptions and boundaries**
If b(B|s)=0 and pi(B|s)>.0, the necessary support is absent and importance weighting cannot recover B outcomes from the logged data. In sequential settings, trajectory weights multiply ratios and can become extremely variable.

**Answer:** Ratios: A=0.625; B=2.5.
