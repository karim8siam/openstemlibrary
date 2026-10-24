# Software Engineering — Unit 1: Requirements

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for requirements.

## 1.1 Stakeholders

**Stakeholders: conceptual explanation**

Stakeholder analysis identifies parties who fund, operate, maintain, regulate or are affected by a system. A school attendance application may have teachers, students, administrators, guardians and privacy officers with conflicting priorities. Treating only the purchaser as the stakeholder misses safety and usability requirements.

### Engineering depth and worked reasoning

A requirements stakeholder is someone who supplies information, makes a decision, operates a workflow, bears its consequences, or can stop deployment. Separate these roles instead of putting every name into an undifferentiated spreadsheet. A registration clerk supplies operational observations; a registrar authorizes policy; a student experiences erroneous records; an identity administrator maintains authentication; a regulator may constrain retention. A stakeholder map should record each party’s goals, influence, access to evidence, and likely conflicts. Interviews are not votes: a convenient request from a powerful manager is not automatically more legitimate than a safety concern from a less influential user.

For a campus attendance service, conduct task observation before proposing screens. Ask an instructor to record thirty students in a room with intermittent connectivity. Watch for corrections, late arrivals, shared devices, and mistaken identities. Interview students separately because they may not criticize the application in front of staff. Draw a power–interest grid, but add a harm dimension so people with little formal power and high exposure are not ignored. Document the evidence behind each requirement, its date, and its owner.

A sponsor proposes publishing all absences on a public noticeboard to encourage punctuality. Teachers consider the page convenient, but students could face unjustified consequences when a mobile device is offline. The engineering response is not merely to attach a privacy warning. Identify the personal data, define the authorized audience, determine the contestation path, and test whether the underlying absence record is reliable enough for any publication. Reject or revise requirements whose foreseeable harm cannot be justified.

Construct a stakeholder register for an education platform with ten users from at least four roles. Include an accessibility stakeholder, an operator who handles outages, and an affected person who cannot authorize a purchase. For each goal, write an observable success criterion and one conflict with another goal. Simulate a requirements workshop: have two parties reject an initial proposal, resolve the conflict in writing, and record unresolved decisions rather than disguising them as consensus.

### Investigation: stakeholder evidence and accountable decisions
Set up a fictional interview archive with five items: a sponsor email requesting a management dashboard; a teacher report about poor Wi-Fi; a student complaint about wrongful absences; a privacy officer's retention concern; and a support technician's description of outage recovery. Extract needs separately from proposed solutions. Do not automatically convert “make a dashboard” into a requirement; record the underlying decision the dashboard is intended to support. Build a responsibility matrix for the recorded attendance decision, correction approval, and deletion requests. Compare whose views were sought with who will bear the outcome. Identify one absent stakeholder and propose how to obtain evidence without creating coercion. The final artifact is a decision log with unresolved questions, not invented unanimity. Reviewers should be able to trace every prioritized requirement to original evidence and a responsible human owner.

### Distinguish authority, expertise, and impact
A stakeholder register should not merge people merely because they work at the same organization. An instructor who uses a workflow every day is an operational expert; the registrar may authorize policy but know little about interface friction; the network administrator can explain connectivity limitations; a student can describe the consequences of a false absence. If a system serves several campuses, do not assume one interviewee represents all of them. Plan sampling across classes, device constraints, accessibility needs, and institutional roles. Prioritize stakeholder engagement using a combination of influence, degree of exposure, ability to supply evidence, and possible harm. Affected groups that cannot authorize spending still deserve attention. After an interview, differentiate an observed problem from a desired feature, a binding policy, and an unverified assumption. A statement such as “our students are all online” is a hypothesis until attendance patterns and offline cases are examined. Keep a record of disagreements because unresolved value conflicts may later become product defects.

## 1.2 Use Cases

**Use Cases: conceptual explanation**

A use case describes a goal and a sequence of actor–system interactions, including alternate and failure paths. “Teacher records attendance” should specify authorization, duplicate submissions and offline operation rather than simply saying “tap submit.” A use case is not a UI mockup or a complete technical specification.

### Engineering depth and worked reasoning

A use case describes an actor’s goal and the system’s externally observable responses, not an implementation recipe for buttons. Record preconditions, trigger, normal flow, alternative flows, failure handling, and postconditions. A use-case specification should remain intelligible if the user interface changes from a mobile app to a kiosk. Separate business rules from screen navigation: a student may not submit attendance for another person regardless of where the submission button appears.

Write the main success scenario for recording attendance: authenticated instructor chooses course and class session, supplies a set of student identifiers, receives validation feedback, and commits one logically atomic submission. Alternatives include the class being closed, a duplicate submission identifier, no network access, and a revoked instructor assignment. The system must preserve exactly which records were accepted and give safe recovery guidance. Treat a retry after timeout as an ordinary branch of the use case rather than an edge case to handle later.

A vague use case says that a guardian “views student progress.” That phrase hides authorization questions: Which learner? Under what relationship? Are disciplinary notes included? Does access expire automatically? A use case that merely assumes an authenticated guardian can view any record enables a horizontal authorization flaw. Reframe it around a verified guardian–learner relationship, specify its lifecycle, and describe the observable response when a relationship is withdrawn.

Create a use-case set for an online laboratory-booking platform. Include reserve equipment, cancel reservation, authorize supervision, and report an unsafe device. At least one alternative flow must contain a partial failure after another system has accepted a request. Draw the boundary separating user activity from internal processing. Test completeness by asking whether a user could accomplish the stated goal through the documented paths without inventing extra steps.

### Investigation: precise goal paths and interrupted workflows
Describe the booking of a university telescope as an actor-goal interaction. Specify initial state, prerequisites for access, validation checks, and what constitutes a committed booking. Introduce a network timeout after the server commits a reservation. A user retries from a different device; the request needs a stable key so the second submission returns the first booking rather than allocating another time slot. Next remove the user's authorization between initial request and retry. Determine whether the same response remains appropriate; distinguish revealing a historic result from authorizing a new operation. Write a failure branch for closed maintenance windows and an offline path that never falsely implies confirmed server state. Test whether a newcomer could implement the intended semantics using only the scenario, without asking the author what “successful” means.

### Use-case completeness is testable
Build a path inventory rather than declaring one idealized scenario complete. For each use case, identify normal success, caller cancellation, invalid request, authorization denial, duplicate request, dependent-service timeout, and partially completed work. Not every path needs a separate screen; all need an intelligible and safe outcome. A use case is externally focused, so it should not prescribe a particular framework or database table unless a technical constraint itself affects a user goal. Distinguish “retry” from “new operation,” and record what a participant can observe when the outcome is uncertain. In education workflows, time-sensitive deadlines make this distinction especially important: an applicant should not have to guess whether a submission was received. When using use cases for acceptance testing, map each branch to an oracle—an authoritative way of deciding correctness. A claim that “the user receives a confirmation” is incomplete if confirmation could be displayed before durable persistence. Use a state transition or an explicit outcome query to remove this ambiguity.

## 1.3 Acceptance Criteria

**Acceptance Criteria: conceptual explanation**

Acceptance criteria translate a requirement into observable behavior that a reviewer can test. A well-formed criterion names an initial condition, action and expected outcome; “the app should be fast” is too ambiguous without a measured workload and threshold. Negative cases matter alongside the happy path.

### Engineering depth and worked reasoning

Acceptance criteria translate a claim about useful behavior into evidence that can be checked. A criterion must specify context, stimulus, observable result, and important boundary conditions. Consider “attendance entry is fast”: speed for whom, how many learners, what network, and which percentile? Replace it with a measured criterion such as saving thirty locally cached entries within two seconds on a stated reference device, while separately specifying synchronization correctness. Quantitative thresholds in an example are design assumptions, not universal industry standards.

Use Given–When–Then wording when it clarifies the observable behavior, but do not mistake a syntax pattern for an adequate specification. Given an already committed submission token, when an instructor retries the same payload, then no additional attendance record is created and the original result is returned. Specify what happens if the token is reused with different data. Add negative cases for unauthorized access and unacceptable input, plus nonfunctional criteria for availability, accessibility, recovery, and operability.

Two requirements may each pass an isolated test while violating the intended product. For instance, a background synchronizer can meet its delay budget and a user interface can display success immediately; together they may incorrectly imply that the server persisted data. Distinguish “saved on device,” “queued for synchronization,” and “confirmed by server.” A correct criterion must require the interface to reveal the current persistence state and prevent silent loss on logout.

For a sample payment confirmation flow, draft twelve acceptance criteria: three happy path, three idempotency and concurrency, two security, two usability/accessibility, and two recoverability. Label which can be automated and which require observation with people. For every criterion, identify the authoritative source of expected behavior, the fixture needed, the oracle, and the person authorized to accept it. Describe a case where all automated checks pass yet the business goal still fails.

### Investigation: oracles and measurable constraints
A proposed criterion reads: “the system handles fifty students quickly.” A test cannot evaluate this phrase because “quickly,” equipment capability, transaction boundary, and user-perceived success are undefined. Specify a reference device, test network profile, number of submissions, endpoint behavior, success threshold, and percentile. Add separate correctness assertions: no missing records, no duplicates after retry, and clear indication of outstanding synchronization. Create cases for an exactly full class, one extra invalid identifier, an already-finished session, and a simultaneous conflict. Treat any chosen latency limit as a project-specific decision requiring stakeholder acceptance. Write down which criteria can be checked without people and which require human evaluation. A useful acceptance suite produces reproducible evidence rather than merely attractive screenshots.

### Acceptance testing must challenge assumptions
Write observable criteria for an ordinary request, a deliberately invalid request, and a concurrent or interrupted request. Give each criterion an actor, precondition, trigger, visible and durable result, and evidence requirement. Distinguish a threshold for experience, such as a completion-time target, from a correctness invariant, such as never allocating a unique device twice. A performance target is meaningful only when a workload, device, data volume, network condition, and percentile are specified. In contrast, many safety and authorization conditions must hold regardless of typical load. In an acceptance review, invite someone to deliberately produce a counterexample. If they can create a scenario where a requirement passes syntactically yet harms the user, the criterion should be revised. Use negative testing to challenge assumptions about identity, state ownership, and recovery. A carefully selected invalid request often reveals more about the contract than ten additional happy-path examples.

## 1.4 Requirements Validation

**Requirements Validation: conceptual explanation**

Requirements validation checks whether the recorded requirements describe the actual stakeholder need; verification checks whether an artifact conforms to its specification. Walkthroughs, prototypes and executable tests can expose contradictions before implementation. A requirements document can be internally consistent yet still specify the wrong product.

### Engineering depth and worked reasoning

Requirements validation asks whether the proposed system solves the right problem; verification asks whether an implementation satisfies its specification. Both are essential, and neither follows automatically from the other. A traceability matrix links stakeholder needs to requirements, design decisions, tests, and operational metrics. A traceability link is useful only if a change can be followed in both directions: from an outage incident to an affected requirement and from a requirement to evidence of its implementation.

Review prototypes with representative users before treating a backlog as settled. Walk through concrete scenarios and ask participants to perform a task without an engineer interpreting every label. Use a decision log when users disagree. Inspect completeness, consistency, feasibility, ambiguity, testability, safety, and dependencies. A requirement “all attendance data is accurate” is infeasible as an absolute promise; a useful replacement specifies reconciliation controls, correction rights, auditability, and error-reporting procedures.

Suppose a team implements a presence dashboard, every unit test passes, and managers approve a demonstration. Only afterward do instructors reveal that some students attend simultaneously scheduled field labs outside the classroom. The underlying domain model is wrong. The proper fix may be to add authorized alternate attendance evidence and exceptions, not to optimize the existing check-in algorithm. Validation failed before coding started, so code coverage cannot rescue the feature.

Prepare a review packet containing stakeholder concerns, an event timeline, a draft workflow, and a small clickable prototype. Ask three readers to identify missing paths and contradictory rules. Triage each finding as an erroneous requirement, uncertain policy, unclear interface, or implementation fault. Record what evidence would close it. Finish with an explicit sign-off boundary: who accepted the requirements, what remained outside scope, and which assumptions must be revisited after deployment.

### Investigation: tracing a high-impact change
The institution changes its attendance policy to allow supervised remote lab participation. Start at stakeholder goal and follow it through requirements, state model, API representation, audit event, display text, reports, tests, and support instructions. Mark each artifact requiring revision. Simulate a missed trace link: the report generator still treats remote participation as an absence even when the student profile shows present. Design a cross-component assertion that would expose that inconsistency. Conduct a review in which a policy owner signs off the meaning of new states and operations confirms monitoring readiness. Track requirements whose evidence remains incomplete. The result should demonstrate the difference between testing one implementation successfully and validating that the institution now makes correct decisions.

### Validation is distinct from implementation approval
Stakeholders may approve a polished demonstration simply because it matches what they previously asked for. A useful validation session therefore begins with observed tasks and representative situations rather than a sales presentation of finished screens. Ask participants to show their own process before interpreting the system's terminology for them. Test unfamiliar examples, including remote sessions, interrupted connectivity, disputed records, and delegated authority. Document whether disagreement concerns policy, user experience, terminology, or technical feasibility. The result of validation is not an unrestricted signature; it is evidence tied to scope and stated assumptions. If those assumptions change, the acceptance decision may need to be revisited. Track changes through the domain model and operational rules rather than only the user interface. A validated feature can still contain coding bugs, and a thoroughly tested implementation can still be the wrong feature. These are separate engineering risks.

## 1.5 Integrated Engineering Studio: Requirements

A university wants an attendance platform. The sponsor asks for a dashboard, students want a way to contest errors, instructors need fast bulk entry, and the privacy officer requires bounded data retention. Write a use case for “record class attendance” with success, duplicate-request, offline, and unauthorized-user paths. An acceptance criterion might state that replaying the same submission ID does not create another attendance record. Validate the criterion with stakeholders before calling it a requirement. Explain why a technically correct implementation of the sponsor's original dashboard request could still harm students if absence is assigned automatically after an outage.

### Studio case: disputed attendance records after a network outage

A university plans to replace signed attendance sheets with a mobile service. The sponsor frames success as fewer hours spent transcribing paper records, but a student union representative asks how false absences can be contested. A senior instructor points out that student groups sometimes attend remote fieldwork on approved schedules. The operations team reports frequent Wi-Fi interruptions in two lecture halls. Each observation changes what “record attendance” must mean: the product is a system of evidence and authorized decisions, not merely an attractive check-in form.

Begin by enumerating events. A session is scheduled, students are enrolled, an authorized instructor records an observation, and the system either confirms persistence or queues the observation for later synchronization. A student can contest a decision, which an authorized reviewer can correct while preserving the previous record and reason. A department officer can export aggregated reports, but cannot infer private corrections from a shared dashboard. These are separate use cases with different permissions and data-retention implications. Translate them into testable requirements with unique identifiers: R-01 concerns authorized recording; R-02 concerns idempotent replay; R-03 concerns the difference between local and remote confirmation; R-04 concerns contestation; R-05 concerns audit provenance.

Write the traceability links. R-02 maps to an API idempotency token, a database uniqueness constraint, and an integration test that sends identical requests twice. R-03 maps to explicit user-interface states and a mobile reconnection test. R-04 maps to a correction workflow, notification rules, and a human usability test involving a fictional disputed absence. R-05 maps to immutable history entries or equivalent protected audit records, plus an access test. The team should not infer that a traceability matrix proves each decision correct: it proves that evidence can be located.

Now inject three changes. First, a course runs simultaneously in two rooms; requirements must define how an instructor selects the intended session. Second, a guardian asks to view another adult student’s attendance; authentication alone does not establish authorization. Third, a school administrator insists on publishing all absence records. Stop the simulated project and ask which evidence, approval, and privacy review would be required before accepting that change. Record alternative designs, including a student-controlled private correction portal. A careful requirements process makes these conflicts visible while changing them is still cheap.

The result of this studio is not a single ideal requirements document. Deliver a set of actor-goal pairs, complete success and failure paths, executable acceptance conditions, documented tradeoffs, and a list of facts still unknown. Explicit unknowns are valuable: an unsupported promise about accuracy or uptime would be worse than a decision to validate the data through a limited pilot.

### Review of evidence completeness
For the attendance case, demand an evidence packet that contains both positive and negative examples. A passing test for a correctly authorized online class does not establish correct handling of remote study, contestation, or disconnection. Trace a concrete student complaint backward through the displayed record, API request, instructor authority, and original requirement. If the system cannot reconstruct why an absence was assigned, its audit model is inadequate even if the count of attendance records is correct. The recommended next experiment is a pilot with representative instructors and students, especially those affected by weak connectivity. Measure disagreement between observed attendance and recorded decisions while preserving privacy; do not interpret a small pilot as a global accuracy guarantee. Identify the staff member with authority to resolve disputed cases and keep the learner informed of status changes.

# Fully worked questions

## Requirement traceability coverage under partial verification

A project records twenty distinct acceptance criteria, of which fourteen have passing implementation evidence and six are still unresolved. Compute evidence coverage. Should the project be declared acceptable? Describe a traceability strategy for a correction workflow that is not among the verified criteria.

**Analyze the assumptions.** Define the denominator as all criteria in the agreed scope, including unverified ones. The measured evidence coverage is 14 / 20 times 100 = 70 percent. This is a descriptive count; it does not weight criteria by impact and does not represent correctness of what the stakeholders originally requested.

**Develop the result.** Follow the correction workflow from a student need, through a requirement identifier, authorization rules, audit-history data design, API behavior, user interface, and automated and human tests. A missing link is a genuine quality gap even if a nearby module has numerous passing unit tests.

**Check interpretation and failure cases.** Inspect the six unresolved criteria for severity. If any governs security, wrongful absence, or data loss, a release decision needs containment or explicit deferral with a justified risk decision. Seventy percent evidence coverage is not a general acceptability threshold.

**Answer.** Coverage = 70%. Acceptance requires requirements validation and a risk-based release decision, not a percentage alone.

## Idempotent replay under an interrupted submission

An instructor submits attendance using token T and the server commits records for thirty students. The network then fails before the response reaches the instructor. The instructor retries token T with the same payload and later retries T with different attendance values. What should the system do and why?

**Analyze the assumptions.** Treat persistence as separate from response delivery. The first request already changed authoritative state despite the caller not observing success. Repeating the same operation without an idempotency rule could insert another set of records or send duplicate events.

**Develop the result.** Associate T with the normalized request and stored outcome inside a durable scope. When T appears again with the same request, return the prior outcome without repeating effects. If T is reused with a different normalized request, signal a conflict rather than silently treating one payload as authoritative.

**Check interpretation and failure cases.** Specify token scope, expiry, concurrent insert behavior and interaction with authorization. The service still needs an audit trail and access checks; possession of a token should not grant cross-course permission. Test retries across process restarts, not only sequential calls in memory.

**Answer.** Exact replay returns the recorded outcome without new writes; conflicting replay is rejected and investigated.

## Validation failure concealed by successful functional tests

An attendance dashboard correctly displays the data stored in its database, and every automated test passes. Later the institution discovers that remote field-lab sessions were never modeled, so authorized participation appears as absence. Explain which quality activities failed and propose one test for each.

**Analyze the assumptions.** Functional verification established that the display agreed with its specified storage representation. That does not establish that the specification represented all legitimate attendance situations. The defect is a domain and requirements failure rather than necessarily a rendering bug.

**Develop the result.** Requirements elicitation should include field-lab instructors and affected students. Validation should walk through a remote-participation scenario with those participants. A model test should verify a distinct authorized participation state and the rules for converting it to reporting categories.

**Check interpretation and failure cases.** An end-to-end acceptance test should create a legitimate field-lab attendance event, persist it, and verify that user display and aggregate export do not classify it as unexplained absence. Preserve an audit trail for corrected historical entries.

**Answer.** Passing code tests cannot compensate for a false model of the user activity; validate the requirement and then verify the corrected implementation.

