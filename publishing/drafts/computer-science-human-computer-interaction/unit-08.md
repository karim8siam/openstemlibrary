# Human–Computer Interaction — Unit 8: Socio-technical design

> Original editorial teaching draft. All datasets and model coefficients are illustrative. Not academically reviewed or production-approved.

## 8.1 Privacy, consent, and information flows

#### Privacy is about flows and power
Privacy in interface design concerns how information is collected, inferred, shared, retained, and used, and whether people can understand and influence those flows. A consent banner is not a complete privacy strategy. A service may display a clear notice while collecting unnecessary location data, retaining records indefinitely, or making deletion difficult. Privacy decisions are embedded in architecture, business incentives, organizational policy, and interface defaults. A person may understand an individual setting but still lack meaningful choice if declining prevents access to an essential service. Evaluating privacy therefore requires examining the whole task and its institutional context.

A student portal provides a concrete example. It needs a student identifier, enrollment status, and perhaps contact details to deliver course services. It may not need continuous device location or detailed behavioral tracking. Start with a data inventory: what is collected, for which purpose, by whom, for how long, and under what access conditions. Distinguish information required to deliver the requested service from optional analytics or marketing. A purpose statement should be specific enough to test. 'Improve your experience' is too broad to explain why precise location is collected during a textbook download.

#### Consent as an interaction
A meaningful choice uses understandable language, balanced options, and a clear account of consequences. An interface that makes 'Accept all' prominent while burying rejection in several screens can manipulate behavior. Consent should not be inferred from a user failing to notice a small checkbox. When a choice is optional, the service should explain what happens if it is declined and allow changes later when feasible. Withdrawal may not erase all previously lawful processing or records that must be retained for legitimate obligations; such constraints should be explained accurately rather than hidden behind a misleading 'delete everything' promise. Legal obligations vary by jurisdiction and require qualified review.

Permission requests should appear in context. Asking for microphone access when a student opens a text chapter is confusing; asking when they initiate voice input makes the purpose understandable. Requesting access only when needed also reduces accidental data collection. If the user denies permission, the application should recover gracefully and provide a non-microphone path when the task permits. Avoid repeated nagging prompts that punish a legitimate refusal. Record which features actually depend on the permission, and ensure the interface's description matches the software's behavior.

#### Data minimization and defaults
Data minimization reduces both exposure and maintenance burden. If aggregate counts suffice to evaluate whether a chapter is being read, collecting identifiable event trails may be unnecessary. Retention periods should reflect operational needs rather than indefinite convenience. Defaults matter because many users never open advanced settings. A privacy-protective default can reduce accidental sharing, but it must still allow users to make informed choices when collaboration requires disclosure. The interface should reveal the audience for shared content before posting, especially when a workspace includes teachers, students, and administrators with different privileges.

A sharing dialog might say 'Visible to everyone' without defining who everyone is. Does it mean the current class, the entire university, or anyone with a link? Replace vague labels with explicit audiences and preview the resulting permissions. After sharing, show how to revoke access. Access control is not only a security implementation detail; it is a user-understanding problem. A user who cannot predict the audience of an action cannot exercise meaningful control over information disclosure.

#### Evaluating privacy experience
Privacy testing should include realistic decisions rather than simply asking whether participants value privacy. Ask someone to submit an assignment without optional analytics, inspect who can see their profile, withdraw a permission, and locate a data-export control. Observe whether the interface supports these tasks without deception or hidden prerequisites. Quantitative metrics such as permission acceptance rate are ambiguous: a higher rate could reflect better explanation, stronger pressure, or changed defaults. Interpret behavior alongside comprehension and autonomy. A successful privacy design allows a person to make a choice aligned with their goals and understand its likely consequences.

## 8.2 Persuasive design and user autonomy

#### Influence is not inherently beneficial
Interfaces influence behavior through defaults, ordering, framing, feedback, reminders, and rewards. Persuasive design intentionally uses these mechanisms to encourage action. A learning platform may remind students to practice regularly; a public-health service may encourage appointment attendance. Influence becomes problematic when it exploits attention, conceals alternatives, or prioritizes business metrics over the user's considered interests. A feature can increase clicks while reducing welfare. Design evaluation must distinguish the organization's target behavior from the user's legitimate goals and ability to decline.

A progress indicator can help learners understand remaining work, but it can also pressure them into meaningless activity. A streak counter may encourage daily study; it may also punish someone who needs rest or has unreliable internet. The same mechanism can have different consequences for different people. Ask whether the intervention supports a user-endorsed goal, whether the person can stop it, and whether the system explains the reward honestly. Avoid inventing artificial urgency or presenting optional actions as mandatory. When the system uses behavioral nudges, make the underlying choices visible and reversible where possible.

#### Defaults and choice architecture
Defaults reduce effort, which is helpful when a common safe choice exists. Yet they can steer people toward a decision they would not otherwise make. Consider a newsletter checkbox on a scholarship form. If it is preselected, enrollment may rise because some users overlook it. That metric does not prove genuine interest. A more informative evaluation measures whether users understood the choice and whether they remain satisfied afterward. For sensitive or optional data sharing, defaulting to a restrictive setting may better preserve autonomy. The correct choice depends on the service, applicable rules, and the costs of an unintended outcome.

Choice architecture includes the language and effort required to accept or decline. 'Continue' and 'Maybe later' may sound neutral, but their placement, contrast, and repetition can create pressure. A cancellation path that requires more steps than enrollment may be a dark pattern even if cancellation remains technically possible. Compare the effort and clarity of alternative paths. The interface should not disguise a purchase as a routine navigation action or bury material terms behind ambiguous labels. Ethical persuasion can make a beneficial option understandable without sabotaging other legitimate choices.

#### Measuring outcomes beyond engagement
Suppose a study reminder increases daily logins but decreases completion of substantive lessons because students spend more time responding to notifications. A dashboard focused only on logins would misclassify the change as success. Define outcomes aligned with user benefit: completed practice, retained knowledge, error reduction, voluntary continuation, and satisfaction. Include guardrails for interruption burden, stress, accidental purchases, and opt-outs. A reminder experiment should specify its hypothesis and stopping conditions before launch, especially when users are minors or subject to institutional authority.

A simple illustrative model might compute total interruption minutes as notifications multiplied by average recovery time. This is a bookkeeping model, not a psychological prediction. Recovery time depends on the task and person, and notifications may differ in importance. Use the model to make assumptions explicit and to compare scenarios, then gather actual data before claiming benefit. Report uncertainty and subgroup differences when the data support them. A design that helps frequent users but harms people with accessibility needs requires reconsideration, not just an average engagement figure.

#### Ethical review of persuasive systems
A practical review asks who benefits, who bears costs, whether the user understands the mechanism, whether alternatives are equally reachable, and whether the intervention can be disabled. Consider a hypothetical learning app that sends increasingly urgent messages after missed study sessions. It may improve attendance for some users, but it can also create anxiety or expose private educational activity on a shared device. Offer notification controls, respect quiet periods, and avoid messages that imply moral failure. Persuasive design is defensible when it supports informed agency and proportionate goals. It is not justified solely because an experiment finds a higher conversion rate.

## 8.3 Collaborative systems and coordination

#### Collaboration changes the unit of design
A single-user interface can often treat actions as a linear sequence: open, edit, save, close. Collaborative systems must account for several people acting with different information, permissions, and expectations. A shared document may receive concurrent edits; a laboratory group may divide responsibilities; a teacher may review work while students continue revising. The interface should make ownership, current state, and consequences understandable across participants. Fast synchronization is useful, but it does not resolve every social conflict. A technically consistent shared document can still leave collaborators uncertain about whose decision is final.

Awareness cues help people coordinate. Showing that another person is editing a section can prevent accidental interference, while an activity history can explain unexpected changes. Too many cues can create distraction or surveillance concerns. The design must decide what awareness is needed for the task and who is entitled to see it. For example, a group project may benefit from seeing that a teammate is currently editing the conclusion, but it may not need a permanent log of every pause and cursor movement. Minimize data while preserving enough information for accountability and recovery.

#### Concurrency and conflict
When two users edit the same value, the system needs a conflict policy. Last-write-wins is simple but can silently discard earlier work. Locking prevents simultaneous modification but can block progress if a lock is abandoned. Merge-based approaches can preserve many independent changes, yet semantic conflicts remain: two paragraphs may both be retained while contradicting each other. An interface should surface unresolved conflicts instead of implying that every automated merge is correct. The right approach depends on the artifact, consequence of errors, and collaboration style.

Consider a shared experiment log. One student changes the measured voltage while another corrects the unit. A naïve last-write-wins implementation may keep only one change. A field-level merge may preserve both but still require checking whether the numeric value matches the unit. The interface can show a change history, highlight concurrent edits, and request confirmation for high-consequence modifications. In educational contexts, retaining an audit trail can support learning and accountability, but retention and access must be proportional to the purpose. The system should not turn every collaborative mistake into permanent surveillance.

#### Roles, permissions, and social norms
Roles such as owner, editor, commenter, and viewer provide a starting point for access control. They are not substitutes for explaining what actions each role can perform. A student who can comment but not edit should understand why an edit control is unavailable and how to request access. Permission changes should be visible to affected users when appropriate. Avoid granting broad access by default merely because it simplifies onboarding. A group can be open to contribution while protecting sensitive grades, private feedback, or unpublished research data.

Social norms also shape success. A shared workspace can include etiquette for claiming tasks, reviewing changes, and resolving disagreements. The interface can support these norms with assignment status, review requests, and structured comments. But it should not impose a rigid workflow that ignores how teams actually operate. Observe real collaborative sessions to identify whether problems come from software, unclear responsibilities, or institutional incentives. A button cannot repair every social disagreement, though clear state and history can make disagreements easier to resolve.

#### Evaluation of group outcomes
Evaluate collaborative systems at the group level as well as the individual level. One person's rapid task completion may come at the cost of another person's confusion or lost work. Measure shared artifact quality, conflict frequency, time to resolution, participation balance, and ability to recover from mistakes. A simulated concurrency model can demonstrate why overlapping edits create more possible conflict pairs as the number of collaborators grows, but it does not predict how often real people collide. The model should be described as combinatorial opportunity, not observed behavior. Pair quantitative logs with interviews and artifact review to understand whether coordination is actually improving.

## 8.4 Design ethics, accountability, and responsible evaluation

#### Ethical questions begin before deployment
Design ethics concerns the consequences of products and the processes used to create them. A technically functional interface can still be harmful if it misleads users, exposes private information, excludes legitimate participants, or makes errors difficult to correct. Ethical review should begin when defining the problem and success metrics, not after implementation. Ask whose problem is being solved, whose behavior is being optimized, and who lacks influence over the design. The organization commissioning the interface may not be the person bearing its costs. This distinction is especially important in education, employment, healthcare, and public services.

An academic monitoring dashboard illustrates competing interests. Administrators may want detailed engagement analytics; students may want privacy and freedom to study at different times. A graph of login frequency can be useful for troubleshooting access problems, but it may become an unfair proxy for motivation or ability. A student with unstable internet may appear disengaged despite completing offline work. Before using such metrics in consequential decisions, examine construct validity, measurement bias, and possible harms. Provide mechanisms for correction and appeal when an automated inference affects a person's opportunities.

#### Accountability through decision records
Responsible teams document assumptions, stakeholders, alternatives, known limitations, and reasons for significant design decisions. A decision record should be short enough to maintain but detailed enough to explain why a choice was made. For example, a team might record that an application requires identity verification because of a specific service obligation, identify less intrusive alternatives considered, and specify how users can recover from a failed verification. Without a record, later teams may treat an accidental design constraint as an unavoidable rule. Documentation also helps reviewers distinguish intentional tradeoffs from neglected risks.

Ethical review needs escalation paths. A developer who discovers that a consent control does not match actual data collection should know how to report the issue and who can stop deployment. A research participant who experiences distress should be able to withdraw and obtain support according to the study protocol. A user who is harmed by an automated decision needs a meaningful route to human review where appropriate. Accountability is not achieved by publishing a generic ethics statement. It requires roles, authority, evidence, and the willingness to change a system when the evidence is inconvenient.

#### Fairness and measurement limitations
Fairness cannot be reduced to one universal numerical score. Different definitions of equitable treatment can conflict, and the relevant definition depends on the service and harm. In an educational recommendation system, equal click-through rates may conceal differences in learning opportunity. An interface translated into multiple languages may still disadvantage people who lack stable connectivity. Evaluate whether groups can access comparable opportunities and complete critical tasks, but avoid treating small, noisy subgroup differences as definitive proof of bias or fairness. Where data are sparse, qualitative investigation and precautionary design changes may be more appropriate than overstated statistics.

An ethical evaluation should examine who was excluded from testing. Participants with disabilities, older devices, or limited literacy may be absent because recruitment was convenient, not because the service has no such users. Report these gaps explicitly. When collecting sensitive attributes for fairness analysis, establish a lawful purpose, consent or another appropriate basis, and strong access controls. Data collection itself can create harm. The goal is to improve decisions while respecting the people represented in the evidence, not to accumulate the largest possible dataset.

#### Safety, reversibility, and graceful failure
Consequences should shape interaction safeguards. A typo in a draft note is easily corrected; an accidental financial transfer or deletion of an irreplaceable record is not. High-consequence actions may require explicit confirmation, clear summaries, transaction records, and recovery procedures. Excessive confirmation can also create habituation, so use it selectively. A reliable interface distinguishes reversible and irreversible actions and communicates what will happen before commitment. Error messages should support recovery without revealing sensitive internal details or blaming the user.

Consider an online exam submission. The system should communicate whether answers are saved, when the submission becomes final, and what happens if connectivity fails. It should not silently submit because a countdown animation ended unless that rule is clearly established. If the service experiences an outage, it should preserve evidence needed to resolve disputes while minimizing unnecessary personal data. A responsible design anticipates failure as part of normal operation and makes institutional remedies understandable. Trust grows when users can predict consequences and seek correction, not when every screen looks polished.

#### Integrating ethics into the lifecycle
A practical lifecycle includes stakeholder mapping, harm scenarios, design alternatives, usability and accessibility tests, privacy review, launch criteria, incident monitoring, and periodic reassessment. Each stage should produce evidence proportionate to the risk. A classroom demonstration may need a simple checklist; a system that controls access to essential services requires more formal review. After deployment, monitor complaints and negative outcomes alongside business metrics. Make it possible to roll back harmful changes and to notify affected users when appropriate. Ethical design is not a promise that harm can be eliminated. It is a disciplined commitment to identify foreseeable harms, limit them, and remain accountable when reality differs from the plan.

## Worked problems

### Calculate a retention-footprint scenario

An educational analytics system records 600 event records each day at a steady illustrative rate. Compare retaining 30 days versus 365 days, assuming no deletion exceptions or compression. Compute the record counts and percentage reduction. Explain why fewer records do not alone prove privacy compliance.

- **Compute each footprint:** Thirty days yields 600×30=18,000 event records. Three hundred sixty-five days yields 600×365=219,000 records.

- **Compute the relative reduction:** The difference is 201,000 records. Relative to the 365-day baseline, the reduction is 201,000/219,000≈0.917808 or 91.78%.

- **Explain the limits:** Retention is only one factor. Collection purpose, data sensitivity, access, consent or another appropriate basis, security, and legal obligations still require assessment.

**Answer:** 18,000 versus 219,000 records, a 91.78% reduction relative to the longer-retention scenario.

### Estimate interruption time without pretending to predict behavior

A constructed planning model assigns 25 seconds of context-recovery time to every nonurgent reminder. Compare eight reminders with two reminders during a study session. Calculate modeled interruption totals and the difference. State why the assumption must be tested.

- **State the bookkeeping assumption:** Assume exactly 25 seconds of recovery for each reminder, with no overlap and no variation across reminders.

- **Calculate both scenarios:** Eight reminders produce 8×25=200 seconds, or 3 minutes 20 seconds. Two reminders produce 2×25=50 seconds.

- **Compare and qualify:** The modeled difference is 150 seconds, or 2 minutes 30 seconds. Actual recovery costs depend on task difficulty, user, timing, and whether reminders are relevant.

**Answer:** 200 seconds versus 50 seconds; a modeled difference of 150 seconds. No empirical productivity effect has been established.

### Count potential collaboration pairs

Six students are allowed to edit a shared laboratory report. How many distinct unordered pairs of students could potentially make conflicting edits? Compute the count and explain why it is not an estimate of actual conflicts.

- **Identify the combinatorial unit:** Each potential pair contains two distinct students, and order does not matter. Counting A–B and B–A separately would double count.

- **Calculate combinations:** The number is C(6,2)=6×5/2=15 unordered pairs.

- **Distinguish opportunity from frequency:** Fifteen is a count of possible pairings, not simultaneous edits, observed collisions, or semantic disagreements. Actual conflicts depend on editing patterns and the system’s merge policy.

**Answer:** 15 distinct potential student pairs; no claim about actual conflict rate follows.

## Interactive models

The following isolated toy models are for numerical exploration, not measured human performance.

## Sources and review limits

- NIST Privacy Framework: https://www.nist.gov/privacy-framework

- W3C WAI accessibility evaluation: https://www.w3.org/WAI/test-evaluate/

- ACM Code of Ethics: https://www.acm.org/code-of-ethics

No real participants were recruited. Academic review, external originality screening, and production integration remain outstanding.
