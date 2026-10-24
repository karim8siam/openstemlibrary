# Software Engineering — Unit 3: Development methods

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for development methods.

## 3.1 Iterative Delivery

**Iterative Delivery: conceptual explanation**

Iterative delivery reduces uncertainty by producing small slices that can be demonstrated and tested. Sprint completion is not equivalent to validated customer value; teams must compare increments against usage or stakeholder feedback. Work in progress and integration risk grow when many features remain unfinished.

### Engineering depth and worked reasoning

Iterative delivery decomposes risk into observable increments rather than merely scheduling work in short calendars. A deliverable should be valuable, demonstrable, and testable end to end. A backlog item “create database tables” may be necessary infrastructure, but it is not the same as a user outcome such as “an instructor can correct a mistaken entry and the learner can see the correction.” Choose vertical slices that cross interfaces, persistence, validation, and deployment.

Estimate cycle time by measuring actual flow from work start to usable completion, including review, test, and release. Work in progress is an economic constraint because unfinished tasks accumulate coordination overhead. A team finishing twelve tickets in a week with ten defects is not necessarily healthier than one finishing eight verified outcomes. Report throughput alongside escaped defects, blocked time, customer use, and recovery performance.

A team commits to a feature because its frontend is ninety percent complete, while authorization rules and data migration remain unresolved. The remaining ten percent may dominate deployment risk. Instead of declaring progress by hours spent, demonstrate an executable narrow slice, record discovered unknowns, and revise scope. Early validation can prevent several weeks of polished work on a concept that users reject.

Plan three iterations for a laboratory reservation product. The first delivers a safe single-device booking flow, the second introduces cancellations and conflict detection, and the third adds asynchronous notifications. For each iteration identify a user-visible result, dependency, acceptance test, release fallback, and the operational signal that would indicate success. Explain which work cannot be split without invalidating the user journey.

### Investigation: flow over feature counting
Take a backlog containing login, profile editor, mentor search, invitations, cancellation, and document upload. Arrange it into end-to-end slices, each with a visible user outcome and one acceptance demonstration. Show a dependency graph rather than a list sorted only by estimated effort. Simulate a two-week iteration during which a third-party identity provider becomes unavailable for one day. Replan without pretending that work already started is complete. Track completion by user-visible behavior, tests, and release availability. Explicitly distinguish throughput in stories from comparable throughput of actual work; unequal ticket sizes make averages misleading. Document the uncertainty around the next iteration using observed data rather than an invented universal velocity multiplier.

### A usable increment crosses every important boundary
A “done” feature is more than a merged component. When a learner edits a profile, the change must be authorized, validated, stored, presented accurately, accessible to supported devices, and supportable during outages. Breaking the work into frontend and backend tickets may help internal scheduling, but a release plan should still organize results around complete user outcomes. Choose a thin vertical slice and make explicit which functionality remains absent. Measure lead time from decision to deployed evidence rather than counting code written. If a feature cannot yet be tested end to end, avoid reporting it as delivered. The economics of iteration come from discovering wrong assumptions early. Showing a narrow real workflow to users can reveal a product mistake before a much larger implementation exists. Iteration should reduce uncertainty while preserving a coherent experience, not simply create activity at predictable dates.

## 3.2 Version Control

**Version Control: conceptual explanation**

Version control records changes as commits with identifiable authorship and histories. A feature branch should be reviewed and integrated while divergence remains manageable; merges do not automatically prove the code is correct. Traceability between a request, a change and a test makes defect investigation easier.

### Engineering depth and worked reasoning

Version control is a record of proposed and accepted changes; it is not a substitute for engineering judgment. A commit should be small enough to review and cohesive enough to restore a meaningful state. Branch policies, protected releases, signed tags where appropriate, reproducible builds, and review discussions make changes traceable. The practical objective is to find, understand, test, and if necessary revert a change without guessing which files belong together.

A good pull request links a problem statement to changed behavior. It should describe implementation choices, tests, migration impact, and operational risk. When a schema change removes a column, prepare clients and backfill data before dropping the field; committing the migration and application in one branch does not mean they can deploy atomically. Consider intermediate compatibility releases and rollback constraints.

A rushed merge replaces an authorization helper used by both the attendance page and the grading page. The new unit tests only cover attendance, so grading silently exposes a cross-course lookup. Branch history tells investigators when the defect arrived but does not establish its cause. Review needs dependency analysis, cross-module tests, and checks around security-sensitive changes.

Simulate concurrent feature branches touching a shared policy. Resolve the merge without discarding either intended behavior, and explain why a conflict-free automatic merge could still be semantically wrong. Create a bisect plan for a regression that appears after several deployments. Record an emergency hotfix procedure that keeps production history and mainline history reconciled rather than creating a permanent fork.

### Investigation: semantic conflict without merge markers
Engineer A adds cancellation to mentor invitations. Engineer B adds an expiration check to another module. Their branches merge cleanly, yet the notification renderer still generates links for cancelled invitations and a cache retains stale invitations. Build a test that asserts a cancelled invitation never grants access, including if it was already cached before cancellation. Write a pull request description that directs reviewers to the invariant and affected modules. Simulate a release tag and a revert, then show that reverting an application commit cannot automatically undo a separately applied data migration. Use Git history to identify which change introduced a defect, but confirm the causal pathway with a failing test.

### A clean history is not an assurance case
Commit history helps engineers locate changes, but it does not prove that a merge is functionally safe. Git understands text and trees, not domain invariants. Two nonconflicting branches can violate an authorization rule together, and a migration can be impossible to roll back even when its application commit is easy to revert. For important changes, link the commit to a requirement, an executable test, an observed effect, and a recovery decision. Commit a database migration separately where deployment sequencing requires compatibility. Use tags or artifact checksums to identify exactly what is deployed. Encourage descriptive commits that explain intent and avoid adding confidential data to messages. Review the expected effect of a cherry-pick or revert across release branches, especially when a fix depends on earlier data changes. Version control is the historical substrate of change control; release correctness requires higher-level evidence.

## 3.3 Review Processes

**Review Processes: conceptual explanation**

Code review can detect logic errors, unclear interfaces and maintainability risks while transferring knowledge. Review effectiveness depends on context and attention, not just approval counts. Very large changes are difficult to inspect; automated checks are useful but cannot replace reasoning about requirements.

### Engineering depth and worked reasoning

Code review is collaborative risk analysis. Reviewers examine whether a change satisfies intent, interacts safely with existing code, and can be maintained by someone other than its author. Style checks can automate spacing, but a reviewer must still ask about transaction boundaries, authorization paths, precision, observability, error handling, and unintended consequences. Review effectiveness depends on psychological safety and bounded, comprehensible changes.

Structure review around a threat or failure hypothesis: “What if the request is replayed?” “What if this function sees an unknown enum?” “What if the upstream API becomes slow?” Then verify claims with local tests or controlled experiments. Require clear ownership for high-risk changes without turning review into a ceremony. Pairing or synchronous explanation may be useful for complex logic; written records preserve why a decision was accepted.

A reviewer requests a caching layer to reduce lines of code in a controller. This advice may actually increase privacy risk if cache keys do not include tenant identity. A useful review comment identifies the specific failure mode and proposes a test, rather than demanding a stylistic preference. Treat disagreements as decisions requiring evidence, not status contests.

Review a proposed patch that caches student profiles by student ID while authorization varies by instructor. Write a threat-focused checklist and a failing test demonstrating a cross-tenant cache leak. Compare the review workload of one two-hundred-line patch against ten dependent twenty-line patches. Decide where atomicity and context should outweigh a rigid change-size metric.

### Investigation: review the security consequences
Review a patch that replaces individual database calls with a shared cache. The cache uses the resource identifier but not the tenant identifier, while resource IDs are only unique inside a tenant. Construct two tenant fixtures with the same resource ID and demonstrate how one tenant could receive another's data. Draft a review comment explaining the exact failure, expected invariant, and test required for correction. Compare a design using compound cache keys with one that checks authorization after cache retrieval. Consider cache invalidation when permissions are revoked, not just when records change. A reviewer should distinguish a convincing test from a plausible argument that cannot be executed under the application’s real permissions.

### Reviews should ask falsifiable questions
Useful review comments identify a specific invariant that the patch might violate. Instead of “this feels complicated,” ask whether the code changes the transaction boundary, exposes another tenant’s data, mishandles retries, or confuses a pending operation with a completed one. Favor small reproducible inputs that would trigger failure. For a multi-tenant cache, warm it using one tenant, then access the same local identifier under another; a leak becomes concrete. Reviewers should distinguish style preferences, maintainability concerns, verified defects, and speculative risks. Authors should respond with evidence or a reasoned alternative, not a ritual acknowledgment. Pair review with automated checks, but do not outsource semantic judgment to a linter. Measure review quality through escaped incidents and learning, not the raw number of comments. A healthy review culture makes a reviewer comfortable asking about assumptions and lets an author disagree without escalating a status conflict.

## 3.4 Team Coordination

**Team Coordination: conceptual explanation**

Team coordination defines ownership, interfaces and escalation paths. A dependency between two teams becomes a delivery risk if neither owns the boundary contract. Shared definitions of done, written decisions and explicit handoffs reduce ambiguity; excessive meetings are not a substitute for clear responsibilities.

### Engineering depth and worked reasoning

Team coordination is an information-flow design problem. Dependencies grow with shared ownership, changing requirements, and unclear decisions. A team should make interfaces explicit and avoid turning one person into a permanent approval bottleneck. Define decision rights: who owns the API, who accepts the business behavior, who can halt a risky release, and who responds when the service fails.

Use lightweight written artifacts that survive personnel changes: decision records, runbooks, issue links, interface examples, and explicit “definition of done” criteria. Track blocked work separately from active progress. Clarify escalation paths when quality, scope, and deadline conflict. A standup meeting cannot repair missing ownership or undefined contracts; it can only expose those problems if people feel safe raising them.

Two engineers separately assume they own idempotency, and both independently deduplicate by different keys. Tests pass in their services, but a retry across the boundary creates duplicate attendance. The failure is partly organizational: ownership of the end-to-end invariant was never assigned. Identify a single accountable owner for the behavior while allowing implementation responsibilities to be distributed.

Write a responsibility matrix for a product team that includes engineering, operations, privacy, product management, accessibility, and support. Trace a change to notification retention from discovery through deployment and customer support. Inject a simulated incident outside office hours and test whether the escalation path identifies a decision maker. Remove coordination rituals that generate activity without improving decisions.

### Investigation: ownership during an outage
A deployment changes the schema for research profiles, and the website starts returning errors. The frontend developer assumes the database team owns the migration; the database engineer assumes the deployment pipeline applies it automatically. Compose a RACI-style responsibility record with one accountable owner for release coordination, plus operational incident roles. Write a timeline from first alert through containment, customer notice, decision to roll forward, and post-incident review. Identify what information should exist in the runbook before the incident. Conduct a simulated handover to a person not involved in the design. If that person cannot identify the latest safe database state, the coordination process needs stronger release artifacts, not more status meetings.

### Coordination is a system of decision rights
A team may attend daily meetings and still be unable to deploy safely because nobody owns the release decision. Clarify responsibility at major boundaries: product acceptance, API compatibility, database migrations, operational monitoring, security escalation, and incident communication. An owner does not need to write all the code; they ensure an invariant has a clear source of authority and evidence. Document decisions at the time they are made, especially temporary compromises and their expiration conditions. Make handovers executable by supplying deployment instructions, current risk registers, and reproducible setup processes. When work blocks, distinguish waiting for external approval from a technical obstacle. Escalation should reach someone empowered to resolve the underlying issue, not merely generate another status report. Coordination is successful when someone unfamiliar with the project can answer what is safe to release and how to respond to failure.

## 3.5 Integrated Engineering Studio: Development methods

A team merges three large feature branches on the day before release and discovers conflicting database schema migrations. An iterative process with short integration intervals would expose compatibility earlier. Establish a definition of done requiring tests, an updated API contract, code review and successful migration rehearsal. Then separate throughput from value: completing five implementation tickets does not prove users can accomplish their goal. Record lead time, defect escape, blocked time and user feedback, while avoiding incentives to subdivide tickets only to improve an arbitrary metric.

### Studio case: iterative delivery of a student research portal

A student research office requests profiles, mentorship invitations, manuscript uploads, project matching, notifications, and usage reports. A single large launch would delay feedback and concentrate risk. Design the first increment around the smallest complete outcome: a student can create a profile with permission controls, and an invited mentor can view it through an authorized link. Later releases can add invitations and collaboration records. This sequence gives real users a useful journey without pretending that building an isolated database schema counts as delivered value.

Plan a six-week example with three two-week iteration boundaries. Treat the dates as assumptions for teaching, not a forecast for any real team. The first iteration includes identity, profile editing, private-by-default storage, and deletion. A second increment adds opt-in mentor discovery and cancellation of invitations. A third adds document submission and review status. Each increment includes tests, operational logs, support instructions, and a release decision. Keep work items small enough to review but preserve the full user outcome from input through durable result.

Two engineers separately change the mentor invitation rule. One creates a link that expires after seven days; another adds invitation cancellation but forgets that expired links may remain in cached pages. Automated merging produces no textual conflict because they edited different files. Behavior nonetheless violates the intended security model. The fix requires semantic review across modules, contract tests, and a clear invariant: only active, nonexpired invitations grant access. Add a test for an invitation that is cancelled moments before link use.

During a review, someone claims the team is “ninety percent complete” because screens are ready. Ask for evidence of accessible keyboard navigation, authorization, profile-deletion handling, and the actual deployment. Report the remaining unknowns and the observed cycle time instead. In a weekly review, decide whether additional features should enter the sprint when two user-facing defects remain unresolved. Capacity arithmetic alone cannot answer this; the risks and cost of a broken release matter.

Deliver a backlog linking each slice to acceptance scenarios, a pull request template describing risks, a decision log for invitation lifecycles, and a definition of done containing tests and monitoring. Evaluate team coordination by running a simulated engineer absence: can someone else understand the code, reproduce the release, and contact the appropriate owner? If not, reducing the number of meetings will not solve the underlying information problem.

### Review of process evidence
The portal team's key release claim is that a real user can complete an end-to-end outcome, not that the backlog has no open tickets. Conduct a demonstration without developer intervention: create a profile, revoke an invitation, verify stale links cannot grant access, and delete the data through the supported procedure. Track defects discovered during the demonstration back to ambiguous contracts or missed tests. Evaluate change lead time alongside rework, support incidents, and any dependency waiting. An iterative plan is working when it produces usable learning and controls risk; frequent releases of unverified code are not automatically a sign of maturity. End the iteration with a concrete decision about the next highest-risk assumption to test rather than simply carrying every unfinished ticket into a new sprint.

# Fully worked questions

## Flow and Little’s law in a stable work system

A hypothetical team completes eight comparably sized tasks every two weeks, and measured average cycle time is one and a half weeks. Assuming a stable system where Little’s law applies, estimate average work in progress and state two reasons the real measurement might differ.

**Analyze the assumptions.** Compute throughput λ = 8/2 = 4 tasks per week. Little’s law is L = λW, with W = 1.5 weeks. Then L = 4 × 1.5 = 6 tasks in progress on average.

**Develop the result.** The system must be measured consistently: same population of tasks, stable flow over the observation window, and the same start/end definitions. A backlog containing large and small items or fluctuating demand can make a short sample unrepresentative.

**Check interpretation and failure cases.** Use the result as a description and capacity signal, not a prescription to keep exactly six tasks open. Examine blocked items, review waiting, and defect rework before concluding that more parallel work will increase throughput.

**Answer.** Average WIP = 6 tasks under the stable-flow assumptions.

## Safe merge versus correct behavior

Feature A adds expiry to mentor invitation links. Feature B adds the ability to revoke an invitation. The changes touch different files, and Git reports a clean merge. Describe how a security defect can still occur and what an effective test would assert.

**Analyze the assumptions.** Textual merge success means no conflicting edits required human resolution. It does not ensure semantic compatibility across the new features. An invitation may be both unexpired and revoked; a consumer that checks only expiry would still grant access.

**Develop the result.** Define a single authorization invariant: access is allowed only if invitation belongs to the resource and viewer, is active, is not revoked, and is before its expiry. Test these properties together, including stale cache and concurrent revocation.

**Check interpretation and failure cases.** Review the places that issue, render, cache, and validate tokens. A contract test across the access boundary is necessary even though each individual branch passed its own unit tests.

**Answer.** A clean merge is not a verified product behavior; integration must check revocation and expiry together.

## Review bottleneck and observed queue time

A patch takes four hours to implement, then waits three days before review and one day for verification. Why would adding a second developer not necessarily reduce the elapsed time? Propose a measurable experiment instead.

**Analyze the assumptions.** Separate touch time from elapsed cycle time. Four hours of coding is only one component of the path. A three-day reviewer queue dominates a small implementation improvement.

**Develop the result.** A second developer may increase the number of submitted patches and worsen the review queue. Investigate available reviewer capacity, change scope, clarity of acceptance tests, and whether automatic checks can run before human review.

**Check interpretation and failure cases.** Trial smaller cohesive reviewable changes and reserve a daily reviewer window. Compare distributions of lead time, escaped defects, and blocked work before and after. Do not optimize only median lead time if the tail becomes unsafe.

**Answer.** Relieve the review constraint using evidence; more developers alone do not eliminate a serial approval bottleneck.

