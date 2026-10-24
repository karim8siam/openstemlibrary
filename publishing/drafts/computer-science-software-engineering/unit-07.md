# Software Engineering — Unit 7: Project delivery

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for project delivery.

## 7.1 Estimation

**Estimation: conceptual explanation**

Estimation is an uncertain forecast conditioned on scope, skills, integration work and unknowns. A range with explicit assumptions is more useful than a precise point estimate with no evidence. Historical throughput and reference-class comparison can calibrate forecasts, but new technology may invalidate old rates.

### Engineering depth and worked reasoning

Software estimation is reasoning under uncertainty rather than predicting one precise number. Separate effort, elapsed duration, and calendar commitments. A task requiring twelve engineer-hours may take several days because review, dependencies, and environment access are not instantaneous. Decompose the outcome into testable work, estimate with reference classes or observed throughput where available, and present ranges with confidence assumptions.

Three-point estimates distinguish optimistic, most-likely, and pessimistic durations. The PERT-style weighted mean (a+4m+b)/6 is a planning heuristic, not a guarantee that project durations follow a particular distribution. For multiple dependent tasks, a critical path determines which delays affect completion. Explicit buffers for integration, review, and unpredictable discovery prevent a single neat arithmetic estimate from masquerading as a reliable schedule.

A project manager adds individual task estimates and promises the sum as a release date. Several tasks require the same database reviewer and deployment window, so resource constraints and queueing extend delivery. A different team parallelizes tasks but increases interface rework. Estimates should state dependency assumptions, available capacity, and the cost of scope changes.

Estimate a four-feature portal release with best, likely, and worst durations for requirements, implementation, review, migration, and rollout. Draw dependencies and calculate a critical path. Add a plausible interruption and show which tasks have slack. Report a delivery interval with named assumptions and a discovery checkpoint, then contrast that with a misleading single-date commitment.

### Investigation: ranges, dependencies, and promises
Estimate a student scheduler release using three-point durations for requirements, logic, interface, review, and rollout. State dependencies explicitly. A task can have a modest engineering effort yet long elapsed time because authorization and procurement approvals occur sequentially. Compute a weighted expectation as an illustrative tool, and then perturb the most uncertain stage. Report which stage governs the critical path, what can run concurrently, and which external milestone could invalidate the forecast. Discuss why adding all individual expected durations often overestimates parallel work yet underestimates shared-resource delays. Conclude with a range and checkpoint, not an unsupported precise launch date.

### Separate distributions from point estimates
Estimating a feature as “eight days” hides uncertainty about requirements, reviews, competing assignments, and external approvals. A three-point estimate expresses a range of plausible effort or duration under conditions, but it is only as good as the assumptions. Use observed work history when available, especially cycle-time distributions for similar outcomes. Identify resource dependencies before summing task estimates: two activities that both require the sole database reviewer are not truly parallel. Communicate forecast updates when scope changes instead of treating the original number as a promise. Estimation quality improves when actual outcomes are compared with forecasts and the reasons for error are documented. Precision of a spreadsheet is not accuracy of the underlying judgment.

## 7.2 Risk Management

**Risk Management: conceptual explanation**

Risk management identifies events, likelihood, impact, detection and mitigation ownership. A low-probability database migration failure can justify rehearsal if its impact is severe. Risks should be revisited as evidence changes; a static checklist prepared at kickoff is not active risk management.

### Engineering depth and worked reasoning

Risk management identifies events that may derail outcomes and chooses controls before they occur. A risk statement specifies cause, event, consequence, owner, and signals. Probability–impact matrices are useful for discussion but often conceal uncertain numbers. Complement them with concrete exposure analyses, failure-mode exercises, pre-mortems, and operational experiments.

Keep a living risk register with triggers and mitigation status. For a campus service, likely categories include privacy leakage, data corruption, peak-load failure, supply-chain compromise, loss of maintainer access, and unsuitable user workflows. Distinguish preventive controls from detective controls and recovery capabilities. Prioritize irreversible harm and low-probability high-consequence events, not just average expected cost.

An application uses one database backup and the team calls data-loss risk “mitigated.” Nobody has restored the backup into a clean environment. Encryption, retention, and backups may all be configured correctly yet recovery may exceed the operational tolerance. Require scheduled restoration drills and evidence of recovery time and integrity.

Conduct a pre-mortem imagining the product failed during registration week. Generate at least eight plausible causes, grouped by technical, human, institutional, and external dependencies. For each, list leading indicators, a preventive test, an incident response, and a named owner. Review the register after an exercise reveals a risk previously treated as negligible.

### Investigation: pre-mortem and response evidence
Imagine a booking service fails at the beginning of a semester. Generate failure modes spanning overloaded database, corrupted times, inappropriate privileges, missing hardware inventory, email provider outage, and a misunderstood policy. Rank severity, uncertainty, and detectability separately; do not treat a low estimated probability as proof of safety. For each high-consequence failure, identify early indicators, preventive tests, operational containment, and who can declare recovery complete. Perform a table-top exercise for a corrupted room assignment that students have already received. The procedure must consider communication and correction of records as well as restoring service health.

### Risk controls should be tested operationally
A risk register is useful only if owners know what to do when signals appear. For data loss, backups are preventive or recovery resources, but a tested restore demonstrates whether recovery actually works. For unauthorized exposure, an audit log is detective evidence, not an access control. For a dependency outage, retries may improve transient availability but may amplify load if every client retries simultaneously. State each risk as a cause, event, and consequence; connect it to prevention, detection, containment, and recovery. Conduct a pre-mortem to discover failure modes before release, then rehearse a few with deliberate fault injection. Record the outcome and revise the design when the exercise contradicts expectations. Treat high-impact irreversible consequences differently from ordinary cosmetic inconvenience.

## 7.3 Releases

**Releases: conceptual explanation**

A release bundles a selected software artifact with configuration, schema transitions and operational instructions. Feature flags can decouple deployment from user exposure, but flag interactions create their own complexity. Version numbers alone are not a rollback strategy.

### Engineering depth and worked reasoning

A release is a controlled change in the experience of users and operators. Version numbers communicate compatibility policy, but the policy must be defined for the product. A changelog should identify added, changed, fixed, deprecated, and security-relevant behavior without exposing exploit instructions. A release decision weighs test evidence, migration readiness, support capacity, and reversibility.

Separate packaging from activation. Feature flags can hide incomplete functions, but they also introduce configuration combinations that need tests and eventual cleanup. Canary releases expose a small fraction of appropriate traffic to new behavior while monitoring meaningful metrics. A rollout can be gradual for stateless code and still require careful sequencing for schema or data migrations.

A deployment dashboard shows low error rates, so an organization declares a successful release. Yet the release silently delays confirmation emails by forty minutes, breaking a registration deadline. Observability must cover the user outcome and downstream effects, not only HTTP status codes. Define error budgets and guardrails tied to critical workflows.

Write a release checklist for a new booking cancellation policy. Include contract tests, database compatibility, security review, support briefing, monitoring, and rollback. Select a canary population that does not expose vulnerable users to extra risk. Create one failure signal that should automatically pause rollout and another that requires human judgment.

### Investigation: canary metrics connected to outcomes
A release introduces an automatic schedule confirmation. Choose canary metrics that detect incorrect bookings and delayed confirmations, not only server uptime. Explain why a canary of two internal staff accounts may be inappropriate if the failure affects student authorization rules. Build criteria for promotion, pause, and rollback, with owners and thresholds stated as project assumptions. Simulate an HTTP success rate of 99.9 percent while the notification queue grows for an hour. Decide whether release should continue and why. Record compatibility of the deployed artifact with current database schema and the necessary support communication if the feature is withdrawn.

### Release readiness is a claim with evidence
Before enabling a feature, determine what observable change users will experience and how the team will recognize failure. A canary is meaningful only if its population and metrics can expose the targeted defect. A low error rate might coexist with incorrect reservations, inaccessible forms, or delayed email. Use quality guardrails tied to domain invariants and include a rapid stop procedure. Feature flags allow activation control but add state combinations that must be tested and eventually removed. Document which user-facing changes require support training and what data migrations are irreversible. An application rollback does not automatically reverse a database update or undo a notification already sent. Release decisions should explicitly recognize those limits and describe compensation or forward repair where reversal is impossible.

## 7.4 Deployment Planning

**Deployment Planning: conceptual explanation**

Deployment planning includes environments, secrets, observability, backups and recovery steps. A rolling release can preserve availability only if old and new versions can coexist. Rollback must consider irreversible data changes as well as reverting application code.

### Engineering depth and worked reasoning

Deployment planning accounts for environment, data, network, secrets, people, and rollback. Infrastructure as code can reduce configuration drift but still requires review and access controls. Separate immutable artifacts from environment-specific settings. A deployment plan should state what changes, what must remain available, what evidence is checked before and after activation, and who can stop the process.

Plan zero-downtime deployment around compatibility, not marketing terminology. With rolling application instances, old and new versions can execute simultaneously; migrations must accommodate both until the rollout completes. Prepare database backups, tested restoration, and appropriate data repair procedures. If a rollback cannot undo a data migration safely, explain the forward-fix contingency explicitly.

A team deploys code that expects a new column before applying the migration. Some pods crash on startup; healthy instances receive all traffic and overload. A readiness probe can prevent crashes from serving requests, but the underlying sequencing mistake remains. An expand-before-switch release would avoid the cross-version mismatch.

Design a deployment plan for a Cloudflare-hosted static frontend and a separately hosted API. Distinguish the atomicity of static asset publication from the rollout of API and database changes. Verify cache invalidation behavior, versioned asset references, CORS policy, API compatibility, rollback timing, and user-visible fallback messages. State explicitly what the static host cannot roll back in an external database.

### Investigation: rehearsal of a rolling migration
Model three instances of an API server rolling from version A to B while database schema expands. Version A must remain functional during the rollout; version B should not require dropping a field that A still reads. Sequence add column, dual-compatible application rollout, backfill, validation, and eventual cleanup. Inject one failing instance and verify that readiness checks remove it from traffic. Include a secret rotation and an external provider timeout as separate scenarios. Write down which operations are reversible in minutes and which require a data-restoration plan. The release checklist should prove that staff know how to respond, not simply that checkboxes were checked.

### Deployment and data are separate lifecycles
Static frontend files may be replaced atomically on a hosting platform, but APIs, caches, and databases usually evolve on different schedules. Ensure the old frontend remains compatible with the new API during partial rollouts and that the old backend can still read expanded schema during fallback. Avoid deploying a schema-destructive migration in the same uncontrolled operation as application code. Model configuration drift and secrets as operational risks. A readiness check prevents an unhealthy instance from receiving traffic, while a liveness check determines whether it should be restarted; neither proves business correctness. After deployment, run smoke tests of important journeys and monitor state transitions and delayed work. Record the exact artifact version, deployment decision, and conditions that justify rollback or a forward fix.

## 7.5 Integrated Engineering Studio: Project delivery

A team estimates a six-week release with a new payment provider and schema migration. Write a risk register with trigger, exposure, mitigation owner and fallback. For example, an external approval that arrives late could block all paid checkout testing; a sandbox integration and optional launch mode may reduce exposure. Use optimistic, most-likely and pessimistic estimates as assumptions, not guarantees. On release day, identify rollback conditions and verify that old application code tolerates newly written data. A rollback to previous binaries cannot undo all data side effects.

### Studio case: estimating and deploying an online examination scheduler

An examination office needs software that allocates rooms, prevents student conflicts, sends notices, and publishes accessible schedules. A manager proposes a firm release date by adding several single-number estimates. Begin by decomposing deliverables and distinguishing calendar waiting time from engineering effort. A critical path may include receiving the definitive room inventory and obtaining security approval; two engineers coding in parallel cannot eliminate those external dependencies.

Use hypothetical three-point estimates for four activities. Requirements validation takes 3, 5, or 9 days; scheduling logic 5, 8, or 15; interface and accessibility checks 4, 7, or 12; migration and rehearsal 2, 4, or 10. PERT-style weighted means are 5.33, 8.67, 7.33, and 4.67 days respectively. Their sum, 26 days, is not a release promise: some work overlaps, some depends on staff calendars, and variation is not captured by simply summing means. Draw dependency edges and assess available reviewers before setting a range.

Write a risk register. An inaccurate room inventory produces conflicting assignments; an inaccessible timetable excludes some students; a stale cached view displays the wrong examination date; notifications may not arrive; an API rate limit can block publication. Each risk gets a trigger, owner, prevention, detection, recovery, and evidence of rehearsal. Prioritize risks that could affect student attendance even if their estimated probability is low.

Release in stages. Publish a read-only schedule to a pilot audience, verify conflicts against the authoritative database, collect accessibility feedback, and compare what the website displays with export files. Use feature activation gates where appropriate and retain the ability to roll back code without losing valid changes to examination records. A database migration must remain compatible with old and new application instances throughout deployment. Avoid claiming that static-site rollback can also revert a separate server-side data change.

Inject a failure fifteen minutes before a deadline. The external notification service is unavailable while scheduling data remains correct. The user interface should report verified schedule publication without falsely claiming notification delivery. Decide whether to delay release, offer alternate access, or escalate to manual procedures. Record the recovery decision and test it in a rehearsal; an untested checklist is not operational evidence.

### Review of delivery assumptions
Return to the examination scheduler forecast after a room-inventory review slips by three days. Recompute the dependency path rather than merely adding three days to every task. Some interface work may proceed on a mock dataset; final allocation testing cannot proceed without approved room constraints. Distinguish schedule risk from correctness risk when deciding whether to release a pilot. A canary can show whether the scheduling output matches authoritative institutional records, but it cannot discover a policy that was never elicited. Document the people authorized to suspend publication and the fallback way students will obtain verified exam dates. The release decision should state how known risks were mitigated, which remain, and why users will not be misled by partial availability.

# Fully worked questions

## PERT expected duration is not a deadline

A work package has optimistic duration 3 days, most-likely 5 days and pessimistic 9 days. Apply the PERT weighted-mean heuristic. Why does the result not guarantee completion by that date?

**Analyze the assumptions.** Substitute a=3, m=5, b=9 into (a+4m+b)/6. The numerator is 3+20+9=32, so the weighted mean is 32/6 = 5.333 days.

**Develop the result.** A heuristic expectation is not a percentile or contractual promise. Real work duration depends on uncertain scope, shared resources, external approvals, and dependencies. The shape assumed by a simple PERT model may not match observations.

**Check interpretation and failure cases.** Report a planning range and identify dependencies. Revisit the estimate after discovery changes the work definition or a resource becomes unavailable. Avoid silently converting a single activity mean into a whole-project finish date.

**Answer.** PERT heuristic mean ≈ 5.33 days; project delivery needs dependency and uncertainty analysis.

## Critical path and parallel work

Activity A takes four days. Then activities B and C take seven and three days in parallel, respectively. Activity D takes two days and requires both B and C. Calculate the nominal shortest elapsed duration under unlimited resources and no delays.

**Analyze the assumptions.** A must finish before either B or C begins. Their parallel phase is controlled by the longer duration: max(7,3)=7 days. D follows both branches and requires two days.

**Develop the result.** The planned elapsed duration is 4 + 7 + 2 = 13 days. The critical path is A–B–D with total thirteen days. The A–C–D path lasts nine days and therefore has four days of nominal slack.

**Check interpretation and failure cases.** If both B and C require the same single reviewer, they may not run fully in parallel. An unexpected approval dependency or changed task size also alters the critical path; the thirteen-day result is conditional.

**Answer.** Nominal minimum = 13 days; critical path A–B–D, assuming independent parallel resources.

## Deployment claim versus downstream confirmation

An examination scheduling website returns HTTP 200 for a newly published timetable, but email notifications are delayed for forty minutes. Explain why the release may be unacceptable despite healthy HTTP metrics.

**Analyze the assumptions.** The HTTP status proves that requests reached the web service successfully under its endpoint contract. It says nothing by itself about the latency, durability, or successful delivery of downstream messages.

**Develop the result.** Define operational measures tied to user outcomes: confirmed schedule version, queue backlog, age of oldest notification, and whether students can retrieve the correct schedule through an alternate channel.

**Check interpretation and failure cases.** Run a canary with alerts on delayed notification delivery. If the deadline makes email timeliness critical, pause rollout or use an approved fallback. The decision must be grounded in business and safety requirements, not a green uptime indicator.

**Answer.** End-to-end correctness requires downstream outcome checks; HTTP success alone cannot authorize promotion.

