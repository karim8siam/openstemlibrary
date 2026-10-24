# Unit 8: Responsible AI systems

*Editorial draft; not approved for live publication.*

## Evaluation
**Evaluation: conceptual explanation**

### Evaluation design for systems with uncertain outputs
Evaluating an AI system begins by defining the claim. A model may perform well on average accuracy but fail on a rare safety-critical condition. An evaluation plan should specify the intended population, input distribution, output contract, baseline, metrics and acceptable failure thresholds before examining results. A dataset chosen after observing model behavior can conceal weaknesses. Distinguish offline benchmark scores from prospective field performance, which may change as users adapt and systems encounter new conditions.

For a binary classifier, a confusion matrix counts true positives, false positives, true negatives and false negatives at a stated threshold. Precision and recall focus on positive predictions and true positives; specificity TN/(TN+FP) focuses on negative cases. In a rare-event setting, a seemingly small false-positive rate can generate more false alarms than true alerts. For example, with prevalence 1%, sensitivity 90% and specificity 95% among 10,000 cases, expected true positives are 90 and expected false positives are 495. Precision is 90/585≈15.4%, not 90%. Always document the prevalence and threshold when presenting precision.

Generative systems require more than one rubric. A summarizer can be fluent but omit critical caveats; a code assistant can produce syntactically valid software with security defects; a science tutor can state the right final answer using an invalid derivation. Human evaluation may assess factuality, completeness, source faithfulness, readability and harmful failure modes separately. Agreement among evaluators should be checked when subjective judgments are used. A single numerical 'quality score' may hide tradeoffs and conceal severe tail failures.

Statistical uncertainty matters when comparing alternatives. Suppose system A answers 82 of 100 questions correctly and system B answers 86. That four-point difference may not be statistically persuasive with only 100 examples, especially if the models were tested on different or correlated tasks. A paired evaluation on exactly the same items makes better use of the comparison and permits a paired uncertainty analysis. Repeatedly testing many candidate changes without controlling selection can overstate apparent progress.

An honest evaluation report includes failure examples and explains data exclusions, labeling disputes and missing ground truth. It distinguishes a fixed benchmark from deployment monitoring and specifies which questions were never tested. In a practical lab, pre-register five edge cases and three failure metrics, then show how a model that wins on average accuracy can still fail acceptance criteria. The objective is evidence sufficient for a bounded claim, not proof that the system is universally safe.

## Robustness
**Robustness: conceptual explanation**

### Robustness, distribution shift and adversarial examples
Robustness concerns whether a system maintains acceptable behavior under changes to input, environment or operating conditions. Ordinary noise robustness tests sensor error and missing fields; distribution-shift tests change population or data collection; adversarial robustness tests manipulation by an agent seeking a particular failure. The three overlap but require different threat models. A model that handles random Gaussian noise may still be vulnerable to carefully chosen perturbations, and a model robust to pixel perturbations may fail when the camera angle changes.

Consider a spam classifier relying heavily on the word 'free'. An attacker can replace the word with visually similar characters, insert spaces or embed the message in an image. Whether this attack works depends on normalization and multimodal handling. A proper security evaluation defines what the attacker can edit, what information they know about the model, how many attempts are allowed and what outcome constitutes success. Reporting a single adversarial success rate without threat-model details makes comparisons unreliable.

A classifier f(x) is locally robust within a set of permitted perturbations if its relevant output property holds for every x' in that set. Exact certification can be difficult for large nonlinear models; randomized smoothing and bound-propagation methods offer particular guarantees under restrictive assumptions. Empirical testing samples attacks but cannot establish robustness against every possible input. A red-team test finding no failures is a result about the attempted attacks, not a mathematical proof of immunity.

Out-of-distribution detection attempts to recognize inputs unlike the training population. Softmax confidence alone can remain high on unfamiliar examples, so thresholding maximum class probability may fail. Evaluate known, shifted and deliberately malformed inputs while reporting false alarms and misses. Systems should be able to abstain or ask for additional information when uncertainty exceeds a defined boundary. Abstention has a cost and must be included in the decision evaluation rather than being treated as free.

For a lab, train a tiny classifier on synthetic points and test rotations, missing features and changes in class prevalence. Show clean-data accuracy and degradation under each perturbation separately. Then introduce a bounded perturbation chosen to maximize loss and compare to random noise of the same magnitude. Document that the toy attack does not establish a universal failure rate for unrelated models, and verify that a defensive preprocessing step does not silently distort legitimate examples.

## Explainability
**Explainability: conceptual explanation**

### Explainability, causal claims and the limits of attribution
An explanation can be a transparent description of how a simple model computes an output, a local approximation of a complex predictor, a feature-attribution score, or a causal account of what would change the outcome. These are not the same. For linear regression with known features, the contribution w_jx_j can be reported relative to a chosen baseline, but correlated variables make causal interpretations precarious. A feature that predicts loan default is not necessarily a legitimate or causal reason to deny credit.

Local surrogate methods fit a simpler model near a particular input. Their faithfulness depends on how the neighborhood is sampled and whether the surrogate reproduces the original model where it matters. A plot can look persuasive while explaining behavior only in an unrealistic synthetic neighborhood. SHAP-style additive attributions apportion a prediction relative to a reference distribution under defined feature coalition assumptions. Correlated inputs and reference choice can change the allocation, and a high attribution is not proof of causation or moral justification.

Counterfactual explanations ask what changes would alter an outcome. For a student admissions predictor, a counterfactual might say that increasing an examination score would change the prediction. But proposed changes must be actionable, legal and feasible; changing birthplace or a protected characteristic is not an appropriate recommendation. A good counterfactual also considers interactions: changing one feature may imply related variables must change. Purely mathematical nearest-neighbor optimization can output impossible people or situations if those constraints are missing.

A useful explanation evaluation checks faithfulness, stability, completeness and user comprehension separately. Faithfulness asks whether the explanation actually tracks model behavior; stability asks whether small irrelevant changes cause wildly different explanations; completeness asks whether key factors are omitted; comprehension asks whether a person can use it. User satisfaction with a polished explanation is not evidence that the explanation is faithful.

In a lab, define a transparent rule-based classifier whose true decision process is known. Produce a feature-importance explanation and an actionable counterfactual, then change an irrelevant feature and test whether the explanation remains stable. Add a redundant correlated feature and observe how attribution methods can distribute credit differently. Explain the correct boundary: a system can be interpretable enough to audit its computation while still relying on biased inputs or an unsuitable decision objective.

## Societal Impacts
**Societal Impacts: conceptual explanation**

### Fairness, privacy, accountability and downstream impacts
AI systems can allocate resources, prioritize cases and shape the information people see. Technical fairness metrics evaluate different properties that may conflict. Demographic parity asks for similar positive-decision rates across groups; equal opportunity compares true-positive rates; equalized odds additionally compares false-positive rates; calibration compares observed outcomes at similar predicted scores. Different base rates and imperfect prediction can make some properties incompatible in general, so there is no one mathematical fairness score that automatically resolves a policy dispute.

A simple illustration involves two groups of 100 applicants each. Suppose Group A has 40 qualified applicants and Group B has 20, under a particular qualification definition. A classifier that approves 30 qualified applicants in A and 15 in B has equal true-positive rates of 75%, but approval-rate parity depends on how many unqualified people are also approved. Equal opportunity alone does not determine demographic parity or false-positive rates. The choice of 'qualified' label itself may reflect historical inequities; using it uncritically can reproduce the very disparity being measured.

Privacy risks include training-data memorization, inference about individuals, leakage through logs, and unauthorized use of sensitive input. Data minimization asks what information the model actually needs. Access controls, deletion policies and purpose restrictions govern handling of records; differential privacy is a mathematical guarantee about how output distributions change when one individual's data is added or removed, under a specified adjacency definition and privacy budget. A system is not differentially private merely because its data are encrypted or identifiers removed.

Accountability requires an owner for failures and a process for correction. Document model version, training-data provenance, intended uses, prohibited uses, monitoring thresholds, appeal options and decision authority. Human review is not meaningful if reviewers lack context, time or the power to override an automated recommendation. Monitoring should detect changes in the input population, error rates and material subgroup harms, subject to lawful and ethical data collection practices.

A classroom project can compare approval-rate parity and true-positive-rate parity on a synthetic dataset and show how thresholds affect them. Avoid presenting one threshold adjustment as universal fairness. Discuss privacy and auditability together: detailed logs aid investigations but may expose sensitive data. The engineering problem is to collect enough justified evidence for accountability while minimizing retention, access and secondary uses.

## Integrated Case Study and Model Limitations
**Integrated investigation for Responsible AI systems.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Case study: evaluating an educational AI tutor
An AI tutor may explain mathematics, ask diagnostic questions and suggest further practice. A narrow benchmark measuring only whether the final answer is correct can miss fabricated proofs, omitted conditions or confusing pedagogy. Define an evaluation rubric with mathematical correctness, step-by-step justification, alignment with the learner's level, clarity about uncertainty and respect for privacy. A wrong intermediate identity followed by a correct final number should not receive full credit for sound reasoning.

Construct a set of 80 original problems spanning algebra, basic probability and mechanics, with separate difficulty groups and reference solutions checked by a second method. Include 10 adversarially phrased questions that contain a false premise, and 10 questions whose wording intentionally omits necessary information. The tutor should correct false premises and ask for missing details rather than hallucinating a unique numerical answer. Report per-category performance, not only an overall score.

For a concrete edge case, ask for the acceleration of a falling object without specifying resistance or a model. A tutor may explain that in an ideal uniform gravitational field near Earth's surface one commonly approximates g≈9.8 m/s² downward, but real drag changes acceleration. A confident claim that every object always falls at exactly the same acceleration in air would fail the rubric. This tests boundary conditions and explanation quality rather than arithmetic alone.

Privacy testing should include messages containing fictitious student records and instructions embedded in retrieved notes telling the tutor to reveal private information. The model should treat source text as task data rather than new authority. Evaluate whether it invents citations, stores unnecessary details or produces a judgment about a student's ability without evidence. A human instructor should be able to inspect and correct lessons that materially affect academic guidance.

The final report should include measured agreement among graders, representative failures, a retest protocol after model updates and explicit limits on deployment claims. A good educational AI system is not defined by the length of its responses or number of available simulations, but by the reliability of its explanations and the learner's ability to use them correctly.

### Research exercise: write an operational assurance case
An AI system should be evaluated against concrete claims, evidence and assumptions. Imagine a campus advising chatbot whose acceptance criteria include correct prerequisite advice, no disclosure of private student records, accessible explanations and escalation to a human for unresolved policy questions. Rather than writing 'the system is trustworthy,' create an assurance table: each row contains one claim, its threat or failure model, a test, an acceptance threshold, evidence location and an owner who can authorize or reject release. This transforms an abstract ethical discussion into an auditable engineering process.

For the correctness claim, curate an independently checked evaluation set with clear answers and contradictory-policy examples. Include cases where course requirements changed between catalog years. The system should state which catalog version it used and avoid presenting historical policy as current policy. For the privacy claim, insert synthetic student records and attempt unauthorized queries across user sessions. Verify that access controls apply before retrieval, not merely that the text generator was instructed to refuse. A model-level refusal is not a substitute for enforcement by the data-access layer.

### Error budget and acceptance decisions
Suppose the system handles 2,000 questions in a pilot study and makes 30 incorrect factual assertions, for observed correctness 98.5%. That number may look high but is insufficient without the distribution of errors. If all 30 errors concern a crucial scholarship deadline, the service may be unacceptable even though average accuracy is strong. Define separate thresholds for critical errors and ordinary wording defects. A zero-tolerance critical category needs particularly careful sampling and may still not be demonstrated to have zero underlying risk by observing no failures in a finite sample.

Paired before-and-after evaluation should avoid moving the goalposts. If a new retrieval system is introduced, retest both versions on the same locked examples, record which items improve and which regress, and inspect representative regressions. A four-point increase in average score accompanied by a new private-data leak is not a net win under a privacy-critical acceptance policy. Use confidence intervals for statistical metrics and avoid claiming a causal effect when changes to the reference data or evaluator were made at the same time.

### Threat-model exercises
List the adversary's capabilities. A malicious user might query private records without authorization, while an attacker controlling an external web page might plant prompt-injection instructions in retrieved material. A developer might accidentally log raw user inputs to an analytics service, creating privacy risk without any malicious prompt. These are three different paths to harm. Their defenses include authenticated data-layer authorization, untrusted-source handling and logging minimization respectively. Testing one defense does not prove the others work.

For a synthetic red-team exercise, construct three attacks against each defined boundary. Measure whether the unauthorized information is returned, whether the attempted attack reaches sensitive tools, and whether alerts or audit records are produced. Include false alarms where legitimate queries are mistakenly blocked. Document the exact synthetic fixtures so tests can be rerun after changes. Do not retain genuine student records in the test dataset merely to make scenarios realistic.

### Human review and appeals
A human-in-the-loop process is only meaningful if a reviewer receives understandable evidence and has actual authority to correct the outcome. If the reviewer merely clicks 'approve' on hundreds of opaque recommendations under unrealistic time pressure, the process may be ceremonial. Design a review screen that displays the source policy, relevant facts, uncertainty and reason for escalation. Give the reviewer a way to mark missing data, correct a fact and request a system-wide fix when similar failures recur.

An appeals process should preserve enough evidence to reconstruct the decision without keeping unnecessary personal information indefinitely. Document retention limits, access controls, deletion workflows and how the record of a model version is associated with the case. Transparency is not the same as publishing sensitive details, and privacy is not the same as deleting all evidence of accountable decisions.

### Release decision from evidence
Build a final scorecard with functional correctness, mathematical solution fidelity, privacy boundary tests, subgroup error analysis, robustness to stale sources, accessibility checks and operational failure handling. Each requirement is evaluated separately. A software team can choose to release only a restricted pilot when the evidence supports a narrow claim, while blocking public deployment until unresolved critical risks are addressed. This approach rejects both artificial optimism and blanket pessimism. The right conclusion is calibrated to the scope of testing.

In academic work, students should explicitly distinguish a tested engineering guarantee from an ethical judgment. A statistical test may establish that two observed error rates differ under assumptions; it does not determine whether that difference is acceptable to affected students. A sound curriculum treats mathematical models as decision aids whose limitations remain visible, and asks learners to justify operational choices with both evidence and articulated values.

### Incident-response rehearsal
A release-ready AI application needs a procedure for discovering and correcting errors. Define severity categories before incidents occur: a typo in an explanatory caption differs from a fabricated safety instruction or unauthorized personal-data disclosure. For each category document who receives the report, what logs can be inspected, whether a model or data source can be disabled, how affected users are notified and how a corrected behavior is regression-tested. Stage a fictional incident in which a course prerequisite changed but the assistant continues using an older policy document. Show the detection trigger, containment, source update and test that prevents recurrence. Treat an absence of reported incidents as insufficient evidence of zero incidents: monitoring coverage and user feedback channels must also be evaluated.

### Documentation as a falsifiable claim
A release note claiming 'the tutor is accurate and safe' is not falsifiable enough to guide testing. Replace it with bounded statements: 'On this frozen set of 120 introductory algebra problems, the tutor's final answers matched verified references on 114 items; three mathematical proof checks were inconclusive; the error rate on future populations has not been established.' A privacy statement should likewise identify which access-control paths were tested and which connected sources were outside scope. Clear claims support correction when new evidence arrives. Broad assurances without scope encourage inappropriate reliance. A student audit should be able to reproduce every numerical assertion from saved fixtures and scripts, while carefully distinguishing measured implementation behavior from expert academic judgment.

### Worked question: Precision under rare positive events
In 10,000 hypothetical examples, 1% truly contain an event. A detector identifies 90% of true events, but falsely flags 5% of nonevents. What is precision?

**Model the question**
There are 100 actual positives and 9,900 negatives. The expected number of true positive flags is 0.9×100=90.

**Calculate or derive**
False-positive flags are 0.05×9900=495. Precision is TP/(TP+FP)=90/(90+495)=90/585≈0.153846. Precision conditions on the set of positive detector outputs, so its denominator must include false alarms as well as genuine detections. The low event prevalence makes the false-alarm contribution relatively large despite a favorable sensitivity.

**Check assumptions and boundaries**
Sensitivity is 90% but precision only about 15.4% because the event is rare. These counts are expectations under the model, not empirical observations.

**Answer:** Precision≈15.38%.

### Worked question: Two fairness criteria
Group A contains 40 qualified people and Group B 20. A model correctly accepts 30 qualified people from A and 15 from B. Compare true-positive rates; can demographic parity be established?

**Model the question**
True-positive rate uses qualified people as the denominator for each group: TPR_A=30/40 and TPR_B=15/20.

**Calculate or derive**
Both are 0.75, so equal opportunity holds for these counts. Demographic parity uses all accepted decisions divided by each group’s total population, which is not provided.

**Check assumptions and boundaries**
Unknown group sizes and false-positive decisions prevent calculating approval rates. Equal opportunity does not entail demographic parity.

**Answer:** Both TPRs are 75%; demographic parity cannot be determined.

### Worked question: Paired model evaluation
On the same 100 examples, model A is correct on 80 and model B on 84. Suppose A-only correct cases are 6 and B-only correct cases are 10. Find agreements and explain how to assess the difference.

**Model the question**
The number of cases where both are correct is 80-6=74; both incorrect is 100-(74+6+10)=10. Check B correctness: 74+10=84.

**Calculate or derive**
Discordant pairs total 16: A-only=6 and B-only=10. A paired statistical comparison such as McNemar’s test examines these discordant cases, not the two raw accuracy estimates as independent samples.

**Check assumptions and boundaries**
The observed difference is four correct predictions, but with only 16 discordant cases it does not justify a confident claim of superior generalization without uncertainty analysis.

**Answer:** Both correct 74; both wrong 10; discordant counts 6 vs 10.


### Case investigation: uncertainty in an automated academic adviser

A course adviser chooses between recommending a prerequisite review session and recommending immediate enrollment. Its prediction score is not automatically a calibrated probability. Imagine one group of one hundred synthetic requests that all receive estimated success probability 0.8, of which only sixty succeed in later verified records. In that bin, observed frequency is 0.6, suggesting overconfidence if the sample is representative and the outcome is measured correctly. A decision maker should not confuse classification accuracy with calibrated uncertainty. If advising students incorrectly has an asymmetric cost, the action rule must account for consequences and an appropriate option to abstain. Analyze performance separately for courses with different prerequisites and for out-of-distribution inquiries. Preserve the student's agency: show the evidence and limitations, and escalate uncertain eligibility decisions rather than presenting them as authoritative facts. Reliability diagrams, held-out evaluation and sensitivity analysis help determine whether the confidence statements are useful; no single small bin proves full calibration across all populations. 
