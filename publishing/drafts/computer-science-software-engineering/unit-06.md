# Software Engineering — Unit 6: Maintenance

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for maintenance.

## 6.1 Refactoring

**Refactoring: conceptual explanation**

Refactoring changes internal structure while intending to preserve externally observable behavior. Characterization tests help establish current behavior, especially when documentation is weak. If the specification is changing at the same time, separate functional changes from structural edits to make regressions easier to detect.

### Engineering depth and worked reasoning

Refactoring changes the internal organization of code while aiming to preserve externally observable behavior. The most valuable refactorings reduce cognitive load, duplication of domain rules, and unsafe dependencies. Before editing, identify contracts and invariants; create characterization tests where behavior is undocumented. Small reversible steps make it easier to detect an accidental semantic change.

Distinguish deliberate duplication from accidental duplication. Two modules can contain similar code yet represent independent policies with different future evolution; forcing them into one abstraction may increase coupling. Conversely, duplicating an authorization predicate in six endpoints creates a real consistency risk. Extract shared logic only after identifying a stable common concept and appropriate owner.

A team “cleans up” a legacy date parser and silently changes its interpretation of daylight-saving transitions. All unit tests use midday values, so the regression escapes. A safe refactor adds characterization tests for time zones, nonexistent civil times, and ambiguous timestamps before changing implementation. Document any intentional behavior change separately from the structural refactoring.

Refactor a large enrollment controller containing validation, authorization, persistence, and notification. Introduce explicit boundaries one at a time. For each step, state what behavior must remain unchanged, which characterization test protects it, and which measure of complexity improves. Show a proposed abstraction that should be rejected because it hides an important business rule.

### Investigation: build characterization tests first
A legacy timekeeping module converts local class times into stored timestamps. It appears duplicated across three files, inviting extraction into one helper. Before changing it, capture sample behavior around timezone offsets, midnight, leap day, and ambiguous daylight-saving times. Decide whether the existing results are intended rules or defects needing explicit product approval. Refactor one call site at a time, verify behavior against the characterization suite, and show how the simplified dependency structure makes errors easier to localize. Identify one near-duplicate function that should remain separate because its business meaning differs. This distinction is central to safe maintenance.

### Characterization tests define a safe boundary
A legacy function may behave strangely for an invalid timestamp because earlier callers relied on that interpretation. Before refactoring, record observed outcomes and determine which are intentional compatibility obligations. Maintain separate tests for deliberate corrections so reviewers understand when behavior is expected to change. Extract one stable responsibility at a time and keep the public contract visible. Excessive abstraction can hide business differences; two functions with similar syntax need not be the same concept if one governs billing and the other governs course credit. The goal is a codebase in which changes have predictable effects, not one with the fewest lines. Use representative edge cases and operational traces to check that the new structure preserves required behavior under normal and exceptional conditions.

## 6.2 Technical Debt

**Technical Debt: conceptual explanation**

Technical debt is a metaphor for future cost caused by tradeoffs in design or implementation. Not all deliberate shortcuts are mistakes: a short-lived prototype may rationally avoid generality. Debt becomes dangerous when interest appears as repeated defects, long lead times or inability to change safely.

### Engineering depth and worked reasoning

Technical debt is a metaphor for future change cost created by design or implementation choices. It can be intentional, with a documented reason and repayment trigger, or accidental, through short-term fixes that become permanent. Not every imperfect abstraction is debt worth paying immediately. Evaluate debt using expected change frequency, risk, and the cost of continuing with the current structure.

Build a debt register linking each item to its operational effect, such as release delays, defect recurrence, fragility, or security exposure. Estimate remediation in bounded increments and compare it against demonstrable opportunity cost. A high-severity authentication flaw is not merely debt to schedule for later; it may demand urgent risk reduction. Avoid using debt language to justify rewriting code that is stable and rarely modified.

A team proposes replacing a mature monolith because onboarding takes several weeks. The difficulty may come from missing environment scripts and documentation, not monolithic deployment. A low-cost onboarding guide and module boundary cleanup should be tested before a costly service rewrite. The best debt investment targets an identified bottleneck rather than aesthetic dissatisfaction.

Rank five hypothetical debt items: untested billing logic, outdated build scripts, duplicated UI styling, an unsupported cryptographic dependency, and slow integration tests. Define impact, likelihood, remediation estimate, and uncertainty for each. Propose an incremental plan that keeps delivery functioning. Record which indicators would show debt was actually reduced rather than merely relabeled.

### Investigation: quantify a real debt tradeoff
Create a debt register for a small web service: thirty-minute setup, fragile integration fixtures, repeated authorization checks, an outdated export format, and unclear deployment ownership. Estimate implementation cost and expected future change frequency using ranges, not pretend precision. Rank the items by operational exposure and unblockable delivery work. Run an experiment that reduces test setup from thirty to ten minutes, and calculate the effect if a team executes the fixture twenty times per week; include the original investment needed. Compare the measurable gain against a costly proposal to rewrite the application. An effective technical-debt decision has evidence that the burden exists and a check that repayment helped.

### Debt accounting needs a causal model
Engineering teams sometimes use “technical debt” as a synonym for anything they dislike in code. A defensible debt item explains how a design choice increases expected future cost or risk. Measure that effect with incidents, onboarding delay, change lead time, or failure frequency. An ugly but stable utility may not deserve immediate replacement; a duplicated authorization rule that repeatedly causes defects probably does. Compare small remediation experiments with large rewrites and account for migration risk. Track the effort saved after repayment instead of presuming every refactor yields a benefit. Debt decisions should include uncertainty: a team may reasonably accept temporary duplication while domain understanding matures. Write down the repayment trigger and make the compromise discoverable to future maintainers.

## 6.3 Compatibility

**Compatibility: conceptual explanation**

Compatibility includes API schemas, persisted data, clients and deployment processes. A database column cannot always be removed simply because new code no longer reads it; older instances or jobs may remain active. Expand–migrate–contract is one approach to staged changes.

### Engineering depth and worked reasoning

Compatibility is a relationship among producers, consumers, data, and time. Backward compatibility means new providers continue supporting old consumers under a stated contract; forward compatibility means older components tolerate certain newer inputs. Database schemas, network protocols, mobile applications, exported files, and stored data each have independent compatibility lifecycles. “Same JSON shape” is not enough when meaning changes.

Use expand–migrate–contract for persistent schema changes. First add a compatible representation, then deploy writers and readers that understand both forms, backfill data with checkpoints, measure adoption, and finally remove the old form after the supported window closes. For mobile clients that cannot be forced to upgrade immediately, maintain explicit deprecation and sunset policies.

A new API returns milliseconds where a previous client expects seconds, but both values are JSON numbers. No schema validation catches the semantic break, and timeouts become dramatically wrong. Unit labels, examples, versioned contracts, and consumer tests are necessary. Similar hazards arise with currency minor units, null semantics, and integer identifier precision.

Plan migration from a string-valued enrollment status to a structured enum with explanatory reason codes. List every producer and consumer, including batch exports. Describe feature flags, migration ordering, validation metrics, and rollback. Test a client two versions behind the server. Explain how to handle records created during the migration window without losing audit history.

### Investigation: mixed-version evolution
Design a schema migration where a product moves from `status: string` to `status: {code, reason}`. Phase one adds the new representation, phase two backfills and verifies, and phase three removes the obsolete field after supported clients have updated. Simulate an old client that writes only the string during phase two. Define how the canonical state is maintained and how conflicts are detected. Add records whose historic status is genuinely unknown and must not be silently mapped to “inactive.” Write rollback limits: some data transformations are not reversible by simply redeploying old code. Produce tests for clients at old, intermediate, and new versions.

### Long-lived clients create migration windows
Web pages can often be updated quickly, but installed mobile apps, partner integrations, and exported files may live for months or years. A provider changing its contract must understand which consumers remain supported. Use an expansion window to add a new representation, let clients migrate with observed usage, and contract the old form only after verifying readiness. Watch for semantic changes that schemas cannot flag, including identifier interpretation, units, defaults, and authorization meaning. A rollback can restore application code while leaving newer data in the database; include this mismatch in the plan. If a historic field contains unknown or contradictory values, preserve those distinctions through migration rather than fabricating certainty. Backward compatibility is an ongoing operational commitment, not a one-time version-number rule.

## 6.4 Legacy Modernization

**Legacy Modernization: conceptual explanation**

Legacy modernization should begin with business boundaries and measurable risks rather than a blanket rewrite. Replacing a working system can expose undocumented behavior and long migration periods. Incremental extraction, observability and reversible releases often contain risk better than a single cutover.

### Engineering depth and worked reasoning

Legacy modernization starts with understanding why the existing system survives. Valuable behavior may be undocumented, encoded in batch jobs, staff routines, or historical data. A rewrite that reproduces visible screens can still lose critical business rules. Characterization tests, traffic analysis, schema inspection, and interviews uncover behavior before technical transformation begins.

The strangler approach moves one capability at a time behind a stable boundary. Identify a narrow business seam, route a controlled subset of traffic through the new implementation, reconcile results, and expand only after monitoring proves the invariants still hold. Use anti-corruption adapters when an old data model conflicts with a new domain model. Avoid dual writes without a reliable consistency strategy.

A school migrates historic attendance records into a new system and discards “unknown” status because the new interface offers only present or absent. Historical uncertainty is converted into false certainty. The problem cannot be solved by adding database indices; the data semantics must be preserved with explicit unknown states and provenance.

Create a migration plan for an old desktop registration system with nightly CSV exports and manual reconciliations. Inventory critical workflows and hidden integrations, identify data ownership, establish reconciliation thresholds, and stage a read-only pilot. Design the rollback path, staff training, and record-retention policy. Include a stop condition that prevents cutover if measured data mismatch exceeds tolerance.

### Investigation: reconcile legacy exports
A registrar's nightly CSV contains identifiers, status codes, course dates, and manually corrected exceptions. Create a five-row sample that includes a duplicate, a missing identifier, a discontinued status code, and a correction after initial export. Define import behavior for each row before coding. Maintain provenance so the original value can be audited without accidentally reapplying a duplicate. Calculate reconciliation totals and explain why equal row counts do not prove data integrity. Plan a staged cutover with read-only comparison and a safe abort condition. Document the staff workflow that created “mysterious” historic values; the modernization may need to preserve valid institutional knowledge rather than discard it.

### Modernization depends on the business history
Legacy systems often encode exceptions that no longer appear in current requirements documents. An old enrollment export may include unofficial correction codes because staff worked around a policy gap. Deleting them could change records used for scholarships or compliance. Modernization begins with business and data archaeology: inspect documents, interview experienced operators, sample real records lawfully, and characterize hidden workflows. Choose a narrow capability to replace first and compare outcomes against the original under representative use. Reconciliation must examine semantic quality, not just row counts. Keep an abort condition for mismatches and test recovery from a partially completed migration. A clean new architecture is valuable only if it preserves or deliberately improves the institution’s actual obligations.

## 6.5 Integrated Engineering Studio: Maintenance

A decades-old billing program returns correct invoice totals but contains undocumented exception handling. Rewriting it as new services risks losing special cases. Start with characterization tests drawn from actual invoices and determine which behavioral quirks are legally required versus historical bugs. Introduce an interface that allows a replacement implementation to run in shadow mode without charging customers twice. Measure error differences, operational cost and rollback safety. Treat technical debt as a tradeoff with observable consequences, not as justification for rewriting every old function.

### Studio case: modernizing an enrollment database without losing history

A university’s legacy enrollment service stores an enrollment status as free text: `active`, `deferred`, `temporarily suspended`, and several historical abbreviations. A new application wants a two-valued active/inactive flag. Compressing the old categories would simplify its code but destroy important distinctions. Before replacement, inventory who consumes exported CSV files, which reports depend on status dates, and what staff do when they find contradictory records.

Characterize the current behavior with representative examples: an active enrollment that was temporarily suspended, a course withdrawal that can be reversed, a student returning after approved leave, and a historical record whose source is incomplete. Add tests that preserve each outcome before refactoring. Separate status as a domain concept from its database representation. The new model might use explicit lifecycle states and a reason code, with unknown preserved where uncertainty genuinely exists.

Plan an expand–migrate–contract path. Add structured columns without removing the original field; deploy readers tolerant of both forms; write new changes to a canonical representation while maintaining an audited compatibility projection; backfill old rows in bounded batches; reconcile aggregate counts and selected examples; then disable old writes after all consumers have migrated. Avoid unconstrained dual writes because partial failures can cause diverging truth. Track backfill checkpoints and isolate records that require human interpretation.

Suppose a nightly report still expects the old string field and silently treats unrecognized values as inactive. A schema migration can pass database tests while violating a financial-aid reporting rule. Consumer contract tests and stakeholder sign-off are required. Now imagine an unexpected error appears after fifty percent of the backfill: a rollback must specify what data was changed, whether it is reversible, and how new writes during migration are handled. A backup existing somewhere does not prove the recovery plan will work.

The modernization decision should also account for technical debt. A full rewrite may be tempting, but an adapter that preserves the old contract while gradually replacing internal rules may reduce risk. Evaluate the real bottleneck using incident frequency, change lead time, onboarding difficulty, and measurable data discrepancies. Conclude with a plan for deprecating the legacy export, a tested data reconciliation report, and a record of decisions that cannot be automated safely.

### Review of migration semantics
Compare five historical enrollment examples in the original and converted systems. Include a suspended student whose status later reverted, an unidentified code, a row corrected manually, a record referenced by an old export, and a student with two independent enrollments. For every example, verify not only row preservation but also report meaning and authorized visibility. A safe cutover needs an abort threshold for mismatches, a clear owner for semantic exceptions, and a recovery plan that is tested rather than assumed. After migration, monitor which old clients still send deprecated fields. Remove compatibility paths only after evidence shows that supported integrations no longer require them. The true outcome is preservation or deliberate correction of institutional meaning, not successful execution of a migration script.

# Fully worked questions

## Technical-debt repayment as an investment

A test environment takes thirty minutes to prepare, and engineers prepare it twenty times per week. A scripted setup reduces preparation to ten minutes. Calculate weekly time saved and explain what must be considered before claiming positive return on investment.

**Analyze the assumptions.** Time reduction per preparation is 30 minus 10 = 20 minutes. Across twenty runs this is 400 minutes, or 6 hours and 40 minutes per week. This is an engineering-time estimate, not an automatically realized cash saving.

**Develop the result.** Measure the initial implementation and maintenance effort of the script, its failure rate, and whether it truly replaces the old preparation steps. A thirty-hour investment has a naive simple payback of 30 / (20/3) = 4.5 weeks before maintenance costs.

**Check interpretation and failure cases.** Track observed setup times and lost time due to failures after rollout. Value may include reduced mistakes and faster onboarding, but such effects must be evidenced separately.

**Answer.** Potential saving = 6 h 40 min/week; naive 30-hour payback ≈ 4.5 weeks excluding maintenance.

## Historical unknown values in a migration

A legacy enrollment database contains statuses active, inactive, and unknown. The new interface allows only active or inactive. What is wrong with mapping unknown to inactive, and how can a migration preserve usable records?

**Analyze the assumptions.** Unknown represents missing or ambiguous evidence, not necessarily nonparticipation. Mapping it to inactive creates a false statement and may change financial or academic eligibility decisions.

**Develop the result.** Keep a distinct unknown state or attach a provenance flag, original value, and resolution status. Identify which records require manual review and prevent conversion code from silently assigning meaning.

**Check interpretation and failure cases.** Run reconciliation across a sample of historical records and the reports relying on them. A migration can have the same number of rows before and after while still losing critical semantic distinctions.

**Answer.** Preserve unknown and provenance until authorized domain experts can resolve it.

## Compatibility of a two-stage deployment

A mobile client running the previous release writes a string status during a migration, while the new server expects a structured object. Design a transition that avoids data loss when the old client cannot immediately update.

**Analyze the assumptions.** During an expansion period, the server accepts both supported representations and normalizes them into a canonical internal state with explicit rules. Changes written by old clients must remain visible to new readers.

**Develop the result.** Use tests for simultaneous clients and a backfill with checkpoints. Track whether writes arrive in the old format, and publish a deprecation policy linked to real support obligations.

**Check interpretation and failure cases.** If both formats conflict, reject or resolve according to a documented policy rather than selecting one arbitrarily. Contract the old interface only after observed usage is low enough and customers have been notified.

**Answer.** A staged compatibility layer preserves supported old clients while migration evidence accumulates.

