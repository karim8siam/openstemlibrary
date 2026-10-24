# Unit 8: Quality operations

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 8.1 Continuous Testing

### Core reasoning and definitions

Continuous testing integrates focused verification throughout the development and delivery process. Fast deterministic checks typically run on every change, broader integration suites run on protected branches or release candidates, and expensive environment-level tests may run before a production rollout. The order should minimize feedback delay while preserving coverage of high-impact failure modes. Every stage needs explicit inputs, versions, and exit criteria. A test gate cannot replace review of ambiguous requirements, third-party dependency trust, or security-specific analysis. Build artifacts should be tied to source revisions so that passing tests refer to the exact code deployed. Untrusted pull requests must not receive privileged deployment credentials or permission to modify protected artifacts.

### Original investigative exercise

Design a pipeline for a STEM textbook site: parse source data, check educational word counts and duplicate prose, run simulation oracles, render static chapters, test navigation and accessibility interactions, inspect sitemap/canonical consistency, then deploy to staging. Trigger a release approval only after all required checks pass. If a chapter fails a math test, stop the release rather than publishing an older simulation with newer prose. Preserve a report for the exact artifact checksum. On a later issue, operators should identify which source and test versions produced the deployed page.

### Limits and counterexamples

Repeatedly rerunning a failing pipeline until one green run appears can hide intermittent defects. An absent test report should not be interpreted as a successful test.


### Deep dive: release decisions under imperfect evidence

Software quality gates exist because a project cannot exhaustively test every possible state, yet it must make release decisions. The result is an evidence-management problem. A release candidate might pass thousands of unit tests while a critical accessibility path fails, a migration cannot roll back, or a settlement idempotency invariant breaks under one controlled race. Reporting an overall 99.8-percent test pass rate could obscure those consequences. Define gate classes according to risk and criticality before execution, so that a large volume of low-impact green assertions cannot outweigh one known release-blocking defect.

Build a quality dossier for a particular immutable artifact. Record the commit and build artifact digests, dependency lock, runtime environment, schema version, feature flags, test datasets, browser support matrix, and test execution times. Each quality claim should link to an executable test or reviewed formal argument. A status labeled “manual review passed” must identify who actually reviewed what and how; a model-generated comment is not a substitute for an independent expert. Keep source and logs free of credentials and real student data. Reproducibility depends on preserving meaningful configuration as well as code.

Prioritize test families deliberately. Unit tests execute frequently and detect local logic regressions. Contract tests protect agreements between producers and consumers and require version management. Integration tests reveal behavior of real database constraints, network clients, and queue boundaries. Browser tests inspect actual user flows and accessibility interaction. Performance tests use controlled workloads; security testing needs threat-specific methods; formal checks make scoped statements about models. No one family is a universal replacement for another. A smaller set of tests with appropriate independent oracles can be more valuable than an enormous set of checks that share the same flawed assumptions.

A flaky test makes release decisions unreliable. Measure failures with context, not only a failure ratio. Suppose three of fifty runs fail on one build host. That is an observed six-percent frequency, but the failures might all occur during an external outage, invalidating an independent-trial model. Collect test order, seed, timestamps, resource contention, network status, and external dependency versions. If the cause is an arbitrary sleep, use a condition-based bounded wait. If the cause is shared mutable data, isolate fixtures. If the product truly races, keep the failure visible and use a controlled concurrency test to reproduce it. Unlimited reruns are not a repair; they disguise uncertain outcomes.

Mutation testing asks whether assertions can distinguish selected plausible code faults. A score of 16 killed among 20 non-equivalent runnable mutants is 80 percent, with important caveats. A survived mutation affecting authorization can be much more serious than several killed arithmetic changes. An equivalent mutant is not a weakness in the suite because no permitted input distinguishes it; an unbuildable mutation is also not evidence of a meaningful tested behavior. Track these categories separately and review surviving mutants according to risk. Combine mutation results with a coverage gap analysis tied to requirements rather than merely optimizing a percentage.

Deployment itself changes system behavior. A green source build may fail with production environment variables, a different database migration order, stale browser caches, or inconsistent versions across replicas. Deploy an immutable candidate to a staging environment and run smoke tests against the deployed URL. For a canary release, define acceptable changes in error rate, tail latency, duplicate processing, and business invariants before rollout. The baseline should be measured comparably; two healthy requests are not meaningful statistical evidence. A rollback procedure should account for forward-only migrations and data written by the newer code. Test rollback while the impact is contained rather than assuming that a button labeled Roll Back can reverse every change.

At the end, classify the result as approved, rejected, or conditionally accepted with an explicit documented exception. Release blockers are not averaged into a confidence score. A waiver should identify the failure, consequence, mitigation, owner, and review deadline. This style of engineering is more demanding than a dashboard screenshot, but it links verification directly to the outcomes students and operators rely upon.


### Unit synthesis: deciding whether evidence is sufficient to release

A test dashboard aggregates results, but the release decision is not an arithmetic average of green and red checks. A missing authorization test in an otherwise huge suite is still consequential, while a failed noncritical snapshot may be handled through a different documented process. Link high-risk requirements to independent tests, artifact identifiers and explicit approval conditions. Record flaky-test behavior with an execution timeline rather than retrying invisibly until success. Treat mutation scores as evidence that selected assertions can detect selected code changes, not as a probability of catching any defect. Finally inspect the deployed staging artifact as well as the source build: wrong configuration, stale caches and incompatible migrations often appear only after packaging. Students should finish with a release dossier that distinguishes automated checks, manual observations, unresolved limitations, and decisions made by accountable reviewers. When a blocker is waived, the impact and mitigation must be explicit rather than hidden by a nominal passing percentage.

## 8.2 Flaky-Test Diagnosis

### Core reasoning and definitions

Flaky tests produce inconsistent outcomes despite unchanged relevant application behavior, often because tests depend on uncontrolled time, thread scheduling, environment state, asynchronous completion, resource contention, or nondeterministic data. A flaky test is not necessarily a harmless false alarm: some intermittently observed failures indicate real concurrency defects. Rerunning can help estimate frequency but is not a substitute for diagnosis. Look for shared fixtures, random seeds, fixed sleeps, clocks, locator ambiguity, unawaited promises, resource exhaustion, and order dependence. Stabilization usually requires better boundaries and synchronization with meaningful conditions. Quarantining a test may keep a pipeline functioning temporarily, but the missing coverage and owner must remain visible.

### Original investigative exercise

Run a browser test repeatedly under consistent code, recording durations and errors. Suppose it fails in 3 of 50 independent runs; the empirical failure rate is 6 percent for that test under those conditions, not a universal probability. Examine whether the test waits for a particular state transition or sleeps for 500 ms before asserting. Replace the sleep with a bounded wait for a stable observable state and compare results over a new repeated run. Randomize test order and check whether the failure follows one test's leftover storage state. Archive logs and seeds for the smallest failing case.

### Limits and counterexamples

If one failure only appears under genuine simultaneous requests, deleting the test as flaky may remove the only detector for a serious race. Investigate product behavior and harness behavior independently.


### Applied laboratory: building an evidence-driven release pipeline

A course-management service is maintained by several teams who commit changes to APIs, database migrations, frontend forms, and scheduled jobs. A release pipeline that merely runs `npm test` and prints green is not an adequate quality argument. Define gates based on consequences. A parser change needs unit and property tests for malformed inputs; a migration needs schema compatibility and rollback evidence; a user-interface change needs representative browser and accessibility checks; a dependency upgrade needs security and integration verification. Separate checks that must run before every merge from slower checks executed on release candidates. The goal is to direct evidence toward risk rather than treating test quantity as a quality score.

Define the pipeline's provenance. Record the exact commit SHA, dependency-lock hash, compiler and runtime versions, test-runner image, feature flags, database schema version, and seed of property-based or randomized tests. An investigation is reproducible only if another engineer can reconstruct the conditions. Store the raw test result and artifact checksums alongside a concise verdict; screenshots and coverage reports are useful but insufficient without environment and expected-behavior context. Do not upload secrets, private test tokens, or real student records in logs. A hermetic test environment helps, but external API contracts and production-like storage still require separate deliberate checks.

Diagnose intermittent failures instead of hiding them behind unlimited retries. Suppose a UI test fails three times in fifty independent runs. Its observed failure proportion is 3/50 or 6 percent. This empirical number does not establish a universal six-percent probability, because the runs may share infrastructure state and may be correlated. Record when failures occur, their error messages, machine load, timestamps, resource utilization, test order, and relevant network or clock events. Retry can sometimes identify transient nondeterminism but should not turn a failed test into an unquestioned pass. Quarantine a genuinely unstable test only with an owner, issue link, replacement coverage, and a deadline for repair. Otherwise, a persistent quality problem becomes invisible.

Strengthen the suite with mutation testing. Choose code in a domain with clear oracles, such as a function that rejects a request after a seat limit is reached. Mutations might replace an inclusive comparison with an exclusive one, remove the authorization guard, invert a boolean condition, or alter a returned identifier. A mutant is killed only when an appropriately relevant test catches a behavioral difference. Invalid mutants that do not build must be handled separately, and equivalent mutants must not be counted as test weakness. If 16 of 20 known non-equivalent runnable mutants are killed, the mutation score is 80 percent; this is evidence about selected mutations, not a claim that 80 percent of all possible defects are detectable.

Create a release evidence table linking each high-risk requirement to its tests, verification method, observed result, and unaddressed limitations. A financial settlement invariant might require database integration and concurrency tests; a keyboard navigation requirement might require an automated scanner plus manual assistive-device evaluation; a liveness property might require a bounded model and production monitoring. Decide release acceptance before executing the checks. Otherwise, teams can be tempted to reinterpret unexpected failures as acceptable under deadline pressure. Any waiver should record impact, responsible decision-maker, mitigation, and the date it expires.

Treat deployment as a testable change. Build an immutable artifact, run static and dependency checks, deploy to a staging environment using production-like configuration, and perform smoke tests against that specific deployed version. Verify that a rollback does not discard schema changes needed by the previous release. For gradual rollout, select objective health indicators and stop conditions: increased server errors, latency regression, unexpected duplicate jobs, or new accessibility failures. Compare the canary against a suitable baseline with enough observations; one healthy request after deployment proves very little. After full release, keep monitoring linked to the same requirements. Quality operations therefore extend verification across the lifecycle rather than declaring testing finished when a CI dashboard turns green.


## 8.3 Mutation Testing

### Core reasoning and definitions

Mutation testing evaluates a suite by applying controlled small changes to code and observing whether tests detect them. A mutant may invert a comparison, replace an arithmetic operator, remove a return, or alter a condition. A mutant is “killed” when relevant tests fail, “survives” when they do not, or may be equivalent to the original under the intended semantics and therefore impossible to distinguish. The mutation score is the proportion killed among mutants considered non-equivalent; it should be interpreted cautiously when timeouts, unbuildable mutants, and tooling exclusions are involved. Mutation testing probes assertion strength rather than proving completeness. Source-aware selection can target risk-critical modules; indiscriminate mutation of generated or trivial code adds cost without instructional value.

### Original investigative exercise

Apply four mutations to a pass-score rule: change >= to >, invert eligibility, replace return value with a constant, and remove an audit event. Design specific tests that would kill each non-equivalent mutant, including a score exactly at the threshold and a check of stateful audit effects. If two mutants behave identically for every permitted input, mark the equivalence question separately rather than claiming an inadequate suite. Record compilation outcome, mutant identifier, executed tests, and whether the detected difference reflects the specified business behavior.

### Limits and counterexamples

A mutation score of 95 percent can still hide a catastrophic unmodeled requirement. Conversely, low scores in mechanically generated code may not justify treating every surviving mutant as equally important.

### How to interpret the interactive model: flakiness rate

This teaching model holds the number of executed runs at fifty and changes the number observed to fail. With three failures, the empirical proportion is 3/50 = 6 percent; with zero failures it is zero in the observed sample, not proof the underlying failure probability is mathematically zero. If runs are not independent, applying binomial confidence formulas without checking assumptions is misleading. A shared build worker, stale fixture, clock leap or network outage can cause correlated failures. The useful next step is diagnosis: retain execution order, seed, timing, resource utilization and stack traces; reproduce a controlled failing schedule. Unlimited retries that eventually obtain a green run conceal uncertainty rather than improving the test.

## 8.4 Evidence Reporting

### Core reasoning and definitions

Evidence reporting explains what was actually verified, by which procedure, against which version, and with which limitations. An effective report separates requirements, test observations, mathematical oracles, environmental context, and unresolved risks. Every pass should be backed by an executable test, reproducible calculation, review artifact, or inspectable recording—not an optimistic status flag. Failure triage should preserve expected and observed results, minimal inputs, timestamps, software versions, and ownership of next action without leaking private data. Traceability links requirements to evidence and links discovered defects back to the assumptions they challenge. A release claim must state its scope; success of isolated simulation tests cannot be represented as proof that the published browser page works for every student.

### Original investigative exercise

Prepare a release report for eight textbook units. Include measured original prose by unit, actual fully worked question count, simulations and independent oracles, error and accessibility test records, source and output hashes, link/canonical checks, and confirmation that draft chapters are excluded from production. Add “not performed” where review or live deployment tests are missing. A failing abstract-interpretation exercise should block an academic correctness claim even if every UI interaction passes. Preserve historical reports so a later reviewer can reconstruct what changed between checkpoints.

### Limits and counterexamples

An automated script that writes `status:pass` without executing a check is evidence fabrication. Record unknowns and scope limitations openly rather than converting them into success labels.

### How to interpret the interactive model: mutation score

The mutation simulator assumes twenty runnable mutants have already been classified as non-equivalent to the intended program semantics. If tests kill sixteen, the score is 16/20 = 80 percent. At twenty killed, the modeled score reaches one hundred percent for this mutation set only. No implication follows about all faults, unmodeled requirements, or external services. A mutant replacing a required authorization check with unconditional access can be more important than numerous arithmetic mutations. Equivalent mutants cannot be killed by any legitimate input, and unbuildable mutants need separate accounting. Review survived mutations by consequence and translate significant ones into improved assertions. The purpose is to challenge test oracles, not to manufacture a universally meaningful quality percentage.

## Fully worked questions

### Worked problem 8.1: Continuous Testing

A test fails on 3 of 50 runs. Calculate its observed failure frequency. Explain why the result does not justify a universal 6 percent failure probability claim.

**Define the property and assumptions.** Define the empirical failure proportion as failures divided by total observed runs. The observed sample contains three failures and forty-seven passes out of fifty runs.

**Compute or execute the reasoning.** The observed rate is 3/50 = 0.06 = 6 percent. Its uncertainty depends on the sampling process; repeated tests on one machine can be dependent through caches, clocks, shared services, and load. The same failure might be concentrated within one outage rather than drawn from independent identical trials.

**Interpret the conclusion and limitations.** Keep the raw timeline and environment metadata. Diagnose fixed sleeps, data contamination and race conditions before replacing the test with automatic retries. Quarantine requires an owner and replacement coverage so the suite does not silently stop protecting a risky behavior.

### Worked problem 8.2: Flaky-Test Diagnosis

A mutation experiment generates 20 runnable, known non-equivalent mutants. Existing tests kill 16. Compute mutation score and explain what survives might mean.

**Define the property and assumptions.** The denominator includes runnable mutants that are not equivalent to the intended program semantics. For the stated dataset, all 20 belong in the denominator and 16 are killed by failing relevant assertions.

**Compute or execute the reasoning.** The mutation score is 16/20 = 0.80 = 80 percent. Four mutants survive, meaning the current suite does not distinguish them under exercised cases. Inspect whether they affect boundary behavior, authorization, stateful side effects, or an otherwise unused path.

**Interpret the conclusion and limitations.** An eighty-percent score is not an estimate of eighty-percent bug-detection probability. Equivalent, invalid, and timed-out mutants require separate classification. High scores on trivial mutations can coexist with missing stakeholder requirements, so mutation analysis supplements rather than replaces risk-based review.

### Worked problem 8.3: Mutation Testing

A release candidate passes unit tests but fails an accessibility keyboard check and a critical database migration rollback test. Should it ship? Construct the evidence-based decision.

**Define the property and assumptions.** First classify each failure against predefined acceptance criteria. A keyboard path may block students from submitting enrollment; a broken rollback may prevent safe recovery from a production migration. The presence of green unit tests does not cancel failures in independent quality dimensions.

**Compute or execute the reasoning.** If those checks are defined release blockers, the candidate must not ship until corrected or a responsible change-control process explicitly approves mitigations and risks. Fix the keyboard sequence, reproduce it at supported viewport sizes, repair migration compatibility, and rerun both gates on the same immutable build artifact.

**Interpret the conclusion and limitations.** Document failure reproduction, affected versions, test environment, release owners, and rollback evidence. A waiver cannot be inferred from urgency or a high percentage of passing tests. Do not claim a release is safe solely because its CI aggregate displays a mostly green dashboard.

