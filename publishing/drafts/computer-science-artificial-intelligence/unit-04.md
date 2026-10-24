# Unit 4: Uncertainty

*Editorial draft; not approved for live publication.*

## Bayesian Networks
**Bayesian Networks: conceptual explanation**

### Bayesian networks and conditional independence
A Bayesian network is a directed acyclic graph whose nodes are random variables and whose edges indicate a factorization of their joint probability distribution. For variables X_1,...,X_n in a topological order, P(x_1,...,x_n)=∏_i P(x_i|parents(X_i)). The graph can make conditional-independence assumptions explicit and reduce the number of parameters compared with a full joint table. An edge should not automatically be interpreted as a causal effect: a probabilistic dependency learned from data can reflect confounding or selection bias.

Consider two binary variables Rain and Sprinkler, both influencing WetGrass. A model might specify P(Rain)=0.2, P(Sprinkler)=0.3, and P(WetGrass=true|Rain,Sprinkler) via a four-row conditional probability table. If Rain and Sprinkler are treated as marginally independent, the joint probability of Rain=true and Sprinkler=true is 0.06. If the sprinkler controller turns off when it rains, the independence assumption fails; the model needs an edge, a shared cause, or a joint distribution encoding that policy. The visual graph is a statement about factorization, not just a diagram.

Collider structures are particularly easy to misunderstand. Suppose Skill→Hiring←Connection. Skill and Connection might be independent in the applicant population, but conditioning on Hiring=true can make them statistically dependent among selected hires. Learning from only accepted applicants can therefore produce spurious associations between skills and personal connections. A simple simulator can enumerate a binary population, apply a hiring rule, and compare correlations before and after selection. This is an example of selection bias, not evidence that skill causes connections.

Parameter estimation also requires smoothing and attention to unseen combinations. A conditional frequency table built from a tiny dataset might assign zero probability to a configuration never observed, even if the true probability is positive. Dirichlet smoothing or expert priors can mitigate brittle zeros, but introduce assumptions that must be disclosed. Graph structure learning from observational data may identify only an equivalence class of directed graphs under assumptions, not necessarily a unique causal graph.

For a lab, implement enumeration on a three-node network, check that each conditional probability row sums to one, and compute a query in two ways: explicit joint summation and variable elimination. Test evidence that has tiny or zero probability and do not silently divide by zero. Record graph independence claims, model provenance and a counterexample distribution where an omitted edge causes a materially wrong posterior.

## Probabilistic Inference
**Probabilistic Inference: conceptual explanation**

### Bayes' theorem, inference and base-rate effects
Bayes' theorem updates a prior probability in response to evidence: P(H|E)=P(E|H)P(H)/P(E). For a binary hypothesis H with sensitivity s=P(E+|H) and false-positive rate f=P(E+|¬H), the positive predictive value is sp/(sp+f(1-p)). This formula illustrates why sensitivity alone is not enough to interpret a positive alarm. If p=0.01, s=0.95 and f=0.05, then P(H|E+)=(0.0095)/(0.0095+0.0495)≈0.161. About 16% of positive signals correspond to H under those assumptions despite 95% sensitivity.

The denominator is essential because it normalizes the evidence across mutually exclusive explanations. An alarm may result from a genuine failure or a false trigger. In a hypothetical population of 10,000 cases with a 1% base rate, the expected number of true events is 100; 95 trigger positive. Of 9,900 nonevents, 495 trigger false positives. Thus 95 of 590 positive alerts are true. The count argument independently reproduces the Bayesian fraction and helps detect common denominator errors.

Likelihood ratios provide an alternative form. Posterior odds equal prior odds times the likelihood ratio P(E|H)/P(E|¬H). For the same positive test, the likelihood ratio is 0.95/0.05=19, but the prior odds are 1/99, so the posterior odds are 19/99 and the probability is 19/(19+99)≈0.161. Multiplying a likelihood ratio by a prior probability without converting to odds is incorrect. Similarly, P(E|H) is not P(H|E).

Exact inference in large Bayesian networks can require substantial computation depending on graph structure, especially induced width or treewidth. Variable elimination sums out hidden variables in an order selected to manage intermediate factor size. Approximate inference samples from distributions or uses variational approximations. A convergence plot from one sampling run does not prove correctness; report sample count, effective sample size when appropriate and comparison against exactly enumerable examples.

A responsible alarm system may combine posterior probability with action costs. If investigation costs 10 units and an undetected true event causes 100 units of expected loss, investigating can be rational at a posterior above 0.1 under a simplified decision model. The threshold changes if investigation creates harms or if probabilities are miscalibrated. A Bayesian number is a belief under declared assumptions, not an automatic instruction to act.

## Decision Models
**Decision Models: conceptual explanation**

### Decision theory, value of information and uncertainty-aware choices
Probabilistic inference estimates what might be true; decision theory connects those estimates to actions and consequences. For actions a∈A and states x∈X, expected utility is EU(a)=∑_x P(x|e)U(a,x) in the discrete case. The agent selects the action with maximum expected utility, provided the utility function accurately reflects the decision maker's priorities. A probability forecast alone cannot choose an action without a description of costs and benefits.

Suppose a server component is likely to fail within a week with posterior probability 0.25. Proactive replacement costs $200. An unplanned failure costs $1000 and can be prevented completely by replacement in a toy model. Expected cost without replacement is 0.25×1000=$250, so proactive replacement is preferred by $50. If replacement itself carries a 10% chance of a $500 interruption, add that expected $50 cost, making the simple policies tie. The analysis changes if failure has safety effects or correlated impacts not represented in the model. State the excluded consequences before accepting the numerical conclusion.

The expected value of perfect information is the difference between expected utility after learning the true state and current maximum expected utility. Information cannot hurt an ideal rational optimizer that may ignore it, so this value is nonnegative before acquisition costs, but practical decision makers may be constrained or interpret information incorrectly. A diagnostic test provides imperfect information; its expected value must integrate possible test outcomes and the optimal decision after each outcome. A test costing more than its expected decision benefit should not be purchased under the model.

Distinguish aleatoric variability, such as genuinely random noise, from epistemic uncertainty due to limited knowledge or model uncertainty. More observations might reduce epistemic uncertainty but cannot remove inherent randomness. Predictive intervals in time series can be miscalibrated under structural changes; a controller should assess out-of-distribution conditions rather than always produce a narrow confidence band. A confidence interval for a parameter and a prediction interval for a future observation describe different uncertainties.

For a laboratory, implement a decision table with probabilities summing to one and utilities tagged with units. Verify expected utilities against a hand calculation. Vary the prior, test costs and utility penalties, drawing the boundary where the preferred action changes. Students should explain the boundary algebraically and note when a toy utility calculation is insufficient to authorize a real operational decision.

## Uncertainty Calibration
**Uncertainty Calibration: conceptual explanation**

### Calibration, proper scoring rules and distribution shift
A confidence score is calibrated when, among cases assigned a probability near p, the event occurs with frequency near p under a specified sampling process. Accuracy and calibration are different. A classifier predicting 0.9 for every example and achieving 90% accuracy may be globally calibrated yet unable to distinguish harder from easier cases. Conversely, a high-accuracy classifier may assign 0.99 to mistakes and be dangerously overconfident. Reliability diagrams group predictions into bins and compare average predicted confidence to observed event frequency; finite bins introduce uncertainty and can hide subgroup failures.

The Brier score for binary events is the average squared error (p_i-y_i)^2, with outcomes y_i in {0,1}. It is a proper scoring rule: in expectation the true conditional event probability minimizes the score when the prediction is chosen without other constraints. For probabilities 0.8 and 0.2 with outcomes 1 and 0, the Brier score is [(0.8-1)^2+(0.2-0)^2]/2=0.04. If both outcomes reverse, the score becomes [(0.8-0)^2+(0.2-1)^2]/2=0.64. A proper scoring rule evaluates probability quality, whereas thresholded accuracy discards much of that information.

Expected calibration error, often computed as a weighted sum of absolute gaps between confidence and accuracy across bins, depends on bin design. It is a diagnostic rather than a universally comparable gold-standard statistic. A low global value can conceal severe overconfidence for a small demographic subgroup or a rare high-stakes event. Temperature scaling fits a parameter on held-out data to modify classification probabilities while preserving class ranking under common implementations. It does not correct incorrect underlying causal structure or guarantee calibration after deployment conditions change.

Dataset shift can change P(X), P(Y|X), or label prevalence. Label shift changes the class prior while class-conditional feature distributions may remain stable; covariate shift changes the feature distribution under a stable conditional label relation in an idealized setting. These distinctions inform monitoring and correction techniques. An image classifier calibrated on sunny daytime photographs may produce unreliable confidences on foggy nighttime images. Confidence histograms alone cannot prove that performance remains acceptable because ground-truth labels may be delayed.

Design a calibration lab with a synthetic Bernoulli generator using a fixed seed. Group outputs into probability bins and compute the Brier score, log loss with numerical clipping for finite calculation, and a reliability table. Vary dataset size and show sampling variability without interpreting single-bin noise as a guaranteed pattern. Compare a globally calibrated model with one that is miscalibrated in a rare subgroup to illustrate the importance of slice-based validation.

## Integrated Case Study and Model Limitations
**Integrated investigation for Uncertainty.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Case study: uncertainty in maintenance alerts
A campus energy system monitors cooling units and must decide whether to schedule maintenance. Sensors measure vibration, current and temperature; true failure events are uncommon. A naive classifier reports '90% confidence' because a sensor crosses a threshold, without deriving a conditional probability. A more useful pipeline distinguishes raw measurement, a probabilistic fault model, calibrated posterior risk and an action threshold determined by costs and safety procedures.

Start with a hypothetical fleet of 1,000 units, a 2% weekly failure base rate, 90% sensitivity and 10% false-positive rate. Expected alerts include 18 true positives and 98 false positives, so the positive predictive value is 18/116≈15.5%. Do not claim these are observed operational rates; they are an illustrative assumed population. If the maintenance team can inspect only 30 alerts, ranking cases by calibrated risk may be more useful than applying a fixed yes/no rule, but requires a utility model and suitable oversight.

Add a cheap preliminary sensor and an expensive confirmatory diagnostic. Derive how the confirmatory test changes expected cost under plausible sensitivities and specificities, and account for dependence between test errors. Simply multiplying likelihood ratios is justified only under an appropriate conditional independence assumption. Show a scenario in which two sensors fail together when ambient temperature rises, making naive independent updates overconfident.

For robustness, perturb the event prevalence from 2% to 0.5% and compare posterior probabilities. The number of positives may remain high while the fraction of genuine faults falls. Record threshold sensitivity and whether the chosen intervention respects constraints from the maintenance manual. Neither toy posterior plots nor a model's confidence score substitute for the team's safety protocols.

The exercise concludes with an audit table: assumed priors, conditional likelihoods, posterior calculations, utility values, calibration diagnostics, missing-data behavior, and escalation rules. Every displayed recommendation needs a trace back to these quantities. This is how a probabilistic AI demonstration becomes a teachable analysis instead of an impressive but ungrounded alarm animation.

### Research exercise: derive a complete Bayesian decision pipeline
A probability calculator becomes useful only when its inputs, conditioning events and action consequences are explicit. Imagine a server anomaly monitor using a vibration sensor and a temperature sensor. Define H as 'the component will fail this week,' V as 'vibration alert positive' and T as 'temperature alert positive.' Specify the prior P(H), both sensors' likelihoods conditional on H and not H, and whether V and T can be treated as conditionally independent given H. That last assumption is not automatically plausible: both signals may be driven by ambient heat or a shared electrical fault. If independence fails, multiplying individual likelihood ratios can overstate or understate evidence.

For a numerical baseline, take prior P(H)=0.02, vibration sensitivity 0.8 and vibration false-positive rate 0.1. After vibration positive, posterior failure probability is 0.8×0.02/(0.8×0.02+0.1×0.98)=0.016/0.114≈0.14035. Suppose temperature sensitivity is 0.9 and false-positive rate 0.2. Under conditional independence, the posterior odds after both alerts equal prior odds times likelihood ratios 8 and 4.5. Prior odds are 0.02/0.98≈0.020408; multiplied odds ≈0.734694 yield posterior ≈0.42353. Calculate it independently using the joint likelihoods: numerator 0.02×0.8×0.9=0.0144; alternative 0.98×0.1×0.2=0.0196; posterior 0.0144/0.034≈0.42353. Agreement verifies the arithmetic, not the independence assumption.

### Add an action model
Let replacing a component cost 150 units and an unplanned failure cost 600 units, assuming replacement prevents the modeled failure. After both positive sensors, expected unreplaced failure cost is 0.42353×600≈254.12 units, so repair is preferred in this toy model. After only the vibration alert, expected failure cost is 0.14035×600≈84.21, so no repair is preferred. The implied probability threshold for repair is 150/600=0.25. This simple decision boundary emerges from the costs, not from an arbitrary convention that a posterior above 50% is automatically actionable.

Now add imperfect repair that prevents only 90% of failures. Expected loss after repair is repair cost plus 10% of the failure risk cost under an independence-style simplification: 150+0.1×600p. No repair costs 600p. Solve 150+60p<600p to obtain p>150/540≈0.27778. The threshold rises because repair is no longer guaranteed. If a repair can introduce new faults, further terms are needed. Every new mechanism changes the decision rule and should be visibly documented.

### Calibration experiment under changing prevalence
Suppose the deployed failure prevalence falls from 2% to 0.5% after equipment upgrades while sensor likelihoods remain unchanged. With both positive signals and the conditional-independence assumption, posterior becomes (0.005×0.72)/(0.005×0.72+0.995×0.02)=0.0036/0.0235≈0.15319. A decision rule tuned for the old prevalence may now trigger expensive repairs unnecessarily. This illustrates label shift within the deliberately simplified model. In practice, the likelihoods may also change as equipment ages, so prevalence adjustment alone is not guaranteed to restore calibration.

A reproducible notebook should compare exact posterior calculations with Monte Carlo simulations of at least several sample sizes, using a fixed seed for debugging and multiple seeds for variability. Report binomial sampling noise and never interpret a simulated frequency as an exact probability. Plot posterior over a range of priors and show the repair decision threshold. Test zero and near-zero denominators; if evidence is impossible under every modeled hypothesis, report model failure instead of inventing a posterior. The research conclusion concerns consistency of a declared probability model, not an independently verified maintenance policy.

### Independent probability sanity checks
Every Bayesian result should pass elementary invariants. A posterior lies between zero and one when the evidence probability is positive. Its complement sums to one within numerical precision. If a binary positive signal has equal likelihood under both hypotheses, the posterior equals the prior because the signal provides no discrimination. If the false-positive likelihood approaches zero while the positive-event likelihood stays nonzero, a positive signal should move the posterior toward one for nonzero prior. Conversely, as prevalence approaches zero the positive predictive value also approaches zero for fixed positive false-alarm rate. These limiting cases are powerful tests because they do not depend on an implementation's own formulas. An interactive teaching model should include them alongside one numerical comparison to independently computed references.

### Reliability of posteriors in small datasets
A Bayesian inference model is only as credible as its likelihood estimates and prior. Suppose the positive-signal likelihood under genuine failure is estimated as 9 positives in 10 observed failures. The plug-in sensitivity estimate is 0.9, but ten cases do not justify treating this value as known exactly. A simple beta prior on a Bernoulli sensitivity parameter yields a posterior distribution over sensitivity instead of a single fixed value. With a uniform Beta(1,1) prior and nine positives from ten independent failure cases, the posterior is Beta(10,2), whose mean is 10/12≈0.8333. This posterior mean differs from the raw sample proportion because the prior adds one notional success and one notional failure. Such pseudo-count language is a calculation aid, not evidence of two actual extra observations.

Predictive risk can integrate parameter uncertainty rather than plugging in one estimated sensitivity. For an introductory exercise, draw a sensitivity value from its beta posterior, a false-positive rate from a separately specified posterior and compute the positive predictive value at a chosen prior prevalence. Repeating this calculation produces a distribution of plausible posterior predictions under the hierarchical model. An interval from that distribution does not have the same interpretation as a frequentist confidence interval obtained from repeated samples, and neither automatically accounts for systemic sampling bias. The key teaching point is that finite calibration data make the probability model itself uncertain.

### Worked question: Positive predictive value
A detector has event prior probability 0.01, sensitivity 0.95 and false-positive rate 0.05. Compute the probability of a genuine event after a positive alert.

**Model the question**
Write Bayes for positive alert E+ and true event H: P(H|E+)=P(E+|H)P(H)/[P(E+|H)P(H)+P(E+|not H)P(not H)].

**Calculate or derive**
Substitute: 0.95×0.01/(0.95×0.01+0.05×0.99)=0.0095/0.059≈0.16101695. The prior probability is multiplied by sensitivity to obtain the true-positive joint probability. The nonevent prior is multiplied by the false-alarm rate to obtain the false-positive joint probability; normalization compares these two explanations of the alert.

**Check assumptions and boundaries**
In 10,000 hypothetical trials this corresponds in expectation to 95 true positives and 495 false positives. The 95/(95+495) fraction independently checks the posterior.

**Answer:** Positive predictive value ≈16.10% under the stated assumptions.

### Worked question: Expected value of a maintenance decision
A component fails with probability 0.3 this week. Failure costs $800. Preventive repair now costs $180 and prevents this modeled failure completely. Which action minimizes expected cost?

**Model the question**
Without repair the expected failure cost is the probability of failure multiplied by its financial consequence. With repair the immediate cost is fixed at $180.

**Calculate or derive**
No repair: 0.3×$800=$240 expected cost. Repair: $180. The modeled cost saving from immediate repair is $60.

**Check assumptions and boundaries**
The conclusion assumes repair prevents failure with certainty and has no side effects, costs or capacity constraints beyond $180. Those assumptions should be relaxed before making operational recommendations.

**Answer:** Preventive repair is preferred by $60 expected cost in the toy model.

### Worked question: Brier score verification
A binary forecaster outputs event probabilities 0.8, 0.3 and 0.6 for outcomes 1,0 and 1. Compute the mean Brier score.

**Model the question**
For each observation calculate (p-y)^2. Respect the order of predictions and corresponding binary observed outcomes.

**Calculate or derive**
The errors are (0.8-1)^2=0.04, (0.3-0)^2=0.09, and (0.6-1)^2=0.16. The mean is (0.04+0.09+0.16)/3=0.29/3≈0.0966667. A Brier contribution measures squared difference between the announced probability of the positive event and the observed binary outcome. Summing all contributions and dividing by the number of forecasts computes the mean, so each case receives equal weight.

**Check assumptions and boundaries**
The score ranges from zero to one for binary probabilities; smaller values are better. Three outcomes are too few to establish long-run calibration.

**Answer:** Mean Brier score ≈0.09667.
