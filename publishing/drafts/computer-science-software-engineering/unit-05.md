# Software Engineering — Unit 5: Quality engineering

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for quality engineering.

## 5.1 Testing Strategies

**Testing Strategies: conceptual explanation**

Testing strategies distribute checks across unit, integration, contract and end-to-end levels. Unit tests localize failures quickly, while end-to-end tests exercise deployments and infrastructure but may be slow or flaky. Coverage percentages count executed lines or branches, not whether assertions detect meaningful faults.

### Engineering depth and worked reasoning

A testing strategy assigns evidence to risks rather than maximizing the number of tests. Unit tests check local rules, integration tests examine boundaries, end-to-end tests evaluate representative journeys, and exploratory testing can reveal misunderstandings that scripted assertions overlook. A test only shows a property under specified conditions; it does not prove the absence of every possible defect. Select tests according to fault likelihood, consequence, and cost of detection.

Apply equivalence classes and boundary analysis to an enrollment service. Test empty and maximum-sized input, duplicate submissions, unauthorized users, concurrent updates, and interrupted transactions. Property-based tests can assert invariants over many generated inputs, such as never allocating more equipment than capacity. Mutation testing can reveal assertions that execute without detecting broken logic.

A team proudly reports ninety-eight percent statement coverage while no test checks whether students can read another student’s records. Coverage is a measure of execution, not of appropriateness. Add authorization properties, negative journeys, and live observability checks. Also identify what automated testing cannot establish, including clarity of language for diverse users and real accessibility with assistive technology.

Construct a risk-to-test matrix with five failure modes: duplicate charge, inaccessible confirmation, unauthorized read, dropped message, and delayed report. Rank them by severity and uncertainty, then choose the cheapest test layer that catches each reliably. Include one chaos or fault-injection experiment and a rollback condition. Explain which failures demand human investigation despite passing automation.

### Investigation: select evidence by failure impact
Make a risk map for a student grant deadline workflow. Assign test levels for required uniqueness, local-time deadline interpretation, accessible upload, malicious file content, protected document storage, and restart recovery. Design one property-based test asserting that a valid idempotency token never creates more than one persisted application under arbitrarily repeated requests. Include a negative authorization test across different applicants. Demonstrate why a unit test for a date-formatting function does not guarantee the whole end-to-end deadline condition. Record one manual usability test and explain which design change it could trigger. Aim for confidence in outcomes rather than a large number of superficially passing tests.

### Use a layered strategy tied to risk
A resilient testing approach starts from what could harm the user, then chooses the most direct evidence of absence of that specific failure under specified conditions. A unit test for permission calculation is useful, but a request-level test can reveal a routing path that bypasses the calculation entirely. Integration tests reveal database races and mismatched schemas that isolated mocks conceal. End-to-end tests verify complete journeys but can be slow and fragile, so use them for high-value outcomes rather than every trivial branch. Exploratory sessions with real users can expose ambiguous terminology and inaccessible interactions. Distinguish test detection coverage from line execution coverage and track tests that fail for irrelevant environmental reasons. A test suite that frequently produces false alarms risks teaching developers to ignore genuine evidence. Reliability of the test infrastructure is part of product quality.

## 5.2 Static Analysis

**Static Analysis: conceptual explanation**

Static analysis reasons about code without executing its intended runtime workflow. Linters catch style and common mistakes; type systems eliminate some classes of invalid operations but cannot prove arbitrary business correctness. Tool findings need severity classification, reproducible examples and responsible owners.

### Engineering depth and worked reasoning

Static analysis examines software without executing its deployed behavior. Compilers catch type and syntax errors; linters enforce conventions; abstract interpretation can reason about data flow; specialized tools flag dangerous patterns and dependencies. Each tool has false positives and false negatives. A useful policy ties checks to clear risk and teaches developers how to address findings without suppressing every warning.

Treat dependency scanners, secret detectors, license checkers, and type systems as different sources of evidence. A vulnerable package notification needs exploitability and exposure assessment, not an automatic claim that every installation is compromised. Record findings with severity, reachability, ownership, remediation plan, and exception expiration. Avoid blocking all builds on low-confidence suggestions while leaving critical authorization code unexamined.

A linter approves a function that concatenates a user-supplied filter into a SQL query because its syntax is valid. A security analyzer may warn, but only parameterized queries and appropriate authorization solve the issue. Conversely, a scanner may flag unreachable test-only code. Tools should inform engineering decisions with precise evidence, not replace them.

Build a static-check pipeline for a small TypeScript or Python project. Include type checking, secret scanning, license inventory, and dependency advisories. Seed one deliberate bug from each category and show which tool detects it. Classify a false positive and document an exception with scope and expiry. Verify that generated artifacts do not accidentally include API keys or student data.

### Investigation: evidence from three analyzer types
Seed a codebase with an accidentally committed mock secret, a variable whose type can be null despite a non-null assumption, and a SQL query constructed by concatenating a user parameter. Choose tools that can detect each error and document what the tools actually report. False positives should be triaged with reproducible evidence rather than suppressed as irritating noise. Create an exception record with an expiration date for one low-risk finding, while refusing to excuse the live secret. Discuss reachability: a vulnerable development-only dependency does not imply the same exploit path as a production dependency exposed to untrusted input.

### Static findings require causal interpretation
A security advisory for a dependency indicates a potential exposure, not proof of an exploitable path in the deployed product. Ask whether the version is present in production, reachable by untrusted input, and protected by other controls. Conversely, a scanner may miss a novel authorization defect because its rules do not understand the business meaning of tenant ownership. Use static checks as fast guardrails for known patterns: compiler errors, obvious secrets, dangerous data flow, vulnerable packages, and inconsistent types. Keep reproducible exceptions with a named owner and expiry to avoid silently losing protection. An ignored critical warning may persist long after the emergency that first justified it. Combine the tool output with targeted review and tests, and document which claims are verified versus inferred from an alert.

## 5.3 Continuous Integration

**Continuous Integration: conceptual explanation**

Continuous integration runs automated checks when changes arrive, giving rapid evidence about build and test regressions. A green pipeline does not guarantee production correctness; environmental differences, missing test cases and unsafe migration scripts can still cause incidents. Release promotion should preserve artifact identity.

### Engineering depth and worked reasoning

Continuous integration provides repeatable evidence about a candidate change; continuous delivery prepares changes for release; deployment automation actually changes a running environment. Distinguish these terms because a passing CI job does not imply that production behavior is healthy. Pin runtime and tool versions, isolate secrets, and retain provenance of built artifacts. Run fast checks early, while expensive end-to-end checks may run in parallel or after initial gates.

Construct a pipeline with dependency resolution, lint and static checks, unit tests, integration fixtures, package creation, vulnerability analysis, staging smoke tests, and a controlled production gate. Prefer building once and promoting the same artifact rather than rebuilding independently in staging and production. Treat database migrations as first-class release steps with compatibility tests and a recovery plan.

An artifact passes tests in CI but fails after deployment because a production-only environment variable is missing. The pipeline proved the wrong configuration. Add environment contract checks that verify required settings without leaking their values, plus synthetic production checks for critical journeys. Investigate failures with logs and telemetry; a green build badge is only a starting point.

Design a pipeline for a web application with a relational database and static frontend. Draw separate paths for pull requests, mainline merges, and production deployment. Identify what triggers each stage, which secrets are required, who may approve an irreversible migration, and what evidence authorizes rollback. Calculate the cost of a flakey check that fails one run in twenty over hundreds of builds.

### Investigation: reproducible release pipeline
Take a basic application with a frontend, service process, database schema, and object store. Build one immutable artifact per commit, run deterministic tests, then promote it to a test environment. Put independent stages in parallel only when failures remain visible. Record dependency versions and checksums so a production incident can be tied to a specific artifact. Simulate a migration that adds a nullable field and later makes it required; verify the safe release ordering. Demonstrate how a staging environment with permissive authorization could hide a production-only fault. Produce a post-deploy smoke test that checks a private resource cannot be read without permission.

### CI evidence is narrower than release evidence
Continuous integration tests one candidate artifact under configured conditions. It does not automatically test production secrets, network rules, background jobs, real load, or interactions with all existing clients. An effective pipeline preserves artifact identity between environments and records what passed: syntax checks, test suites, security policy, contract compatibility, migration smoke tests, and accessibility assertions where automatable. The release pipeline must add a decision about the target environment and post-deployment observation. A database schema can pass automated tests yet fail under historic data patterns unseen in fixtures. Include representative migration rehearsal and a path to stop rollout. Successful release engineering requires both confidence in the built artifact and evidence that the deployed system continues delivering intended outcomes.

## 5.4 Defect Management

**Defect Management: conceptual explanation**

Defect management separates symptoms, reproducible steps, likely root cause, severity and corrective action. Two reports may share one root cause or describe independent faults. Useful post-incident reviews focus on system improvements and verification rather than merely attaching blame to the last person who changed code.

### Engineering depth and worked reasoning

Defect management is the disciplined handling of uncertainty, not merely a count of tickets. A useful defect report includes reproducible steps, expected and observed results, environment, severity, affected users, logs with sensitive fields removed, and supporting evidence. Severity describes impact; priority incorporates timing and business context. A cosmetic issue may be urgent before a public demonstration, while a rare privacy leak remains severe regardless of its frequency.

Triage by impact and confidence. Reproduce the defect or preserve a failing test before changing code; otherwise a fix may target the wrong cause. Use root-cause analysis to ask why existing safeguards did not detect the error. Prevent recurrence through tests, design changes, better requirements, or operational monitoring. Avoid blame-focused analysis that discourages reporting.

A queue retry bug duplicates grade notifications. The immediate patch suppresses duplicate emails, but the underlying message handler remains non-idempotent. If a future feature sends billing events through the same handler, the risk returns. A robust remediation defines event identity, durable processing state, and tests for redelivery and out-of-order messages.

Write a defect report for an enrollment conflict that appears only under simultaneous requests. Include a two-client reproduction script, expected invariant, actual database state, and logs that would distinguish a lost update from a stale cache. Propose an immediate containment action and a long-term correction. Specify how support staff should communicate with people affected by already-corrupted records.

### Investigation: reproduce and correct a race defect
Two clients submit a reservation for the last available seat. In a naive implementation both read “one available” before either updates the count. Capture the initial database state, interleaved operations, observed violation, and expected invariant. Use transaction isolation or atomic update predicates to prevent oversubscription, then replay the exact interleaving. A successful fix must not turn every conflict into a silent success. Include a communication plan for already affected applicants whose records might require manual correction. Record whether the defect stems from specification ambiguity, a code mistake, missing concurrency tests, or all three; a patch without root-cause analysis invites recurrence.

### Manage defects as evidence about a system
A defect report without a reliable reproduction can still be valuable, especially for rare concurrency faults, but it needs enough context to guide investigation. Preserve timestamps, relevant revision identifiers, request correlations, sanitized logs, and state changes. Separate the observed symptom from a proposed explanation: a duplicate record might arise from request replay, eventual-consistency conflict, or an incorrect migration. Test competing hypotheses instead of immediately rewriting the code closest to the visible failure. Record user impact and needed corrections, not only the code patch. A robust post-incident analysis asks why the issue escaped requirements, review, tests, and monitoring; it does not search for an individual to blame. Operational fixes can include rate limits, safe retries, visibility into queue age, or clearer user states in addition to code changes.

## 5.5 Integrated Engineering Studio: Quality engineering

A service is tested using 94 percent line coverage, but users still receive duplicate charges. Coverage says those lines executed, not that the tests checked idempotency under concurrent retries. Add a contract test simulating duplicated payment requests and an integration test with transaction rollback. In CI, pin dependency and build versions, run migration checks, and preserve logs for failing tests. A defect report should record the precise request sequence, expected result and actual ledger entries. Investigate root cause without assuming the person who last edited the payment module introduced the problem.

### Studio case: test strategy and CI for scholarship applications

A student grant portal receives eligibility documents and supporting statements before a strict deadline. A failed submission can have real consequences. The engineering team writes twenty unit tests for file parsing and reports excellent coverage, but no test simulates the application deadline, storage outage, or a reviewer attempting to read another applicant’s file. The number of passing tests is not proportional to the safety of the feature.

Create a failure-mode inventory. Data loss can occur when a request is acknowledged before its upload is durable; duplicate applications can arise from retries; a clock mismatch can reject an on-time request; stale authorization can expose documents; an inaccessible upload widget can block keyboard-only users. For each mode, choose evidence. Unit tests handle extension and size validation, integration tests handle transaction and object-store behavior, security tests handle cross-applicant access, end-to-end tests cover deadline behavior, and usability testing covers actual task completion.

A CI pipeline should run deterministic fast checks on every proposed change. It can then build one artifact, run integration fixtures against a temporary database, perform dependency and secret scanning, and exercise a small set of critical journeys in staging. Promote the same tested artifact to production after a documented release gate. If the database schema changes, verify both old and new client versions during the supported transition. A passing artifact alone does not validate the live configuration or the external storage service.

Seed three deliberate faults. Remove a role check from a download endpoint; the authorization test should fail. Make a retry handler return a new submission identifier after a timeout; the idempotency test should fail. Change local time comparison to naive UTC; a deadline test on a non-UTC date should detect it. For each fault, ask whether line coverage would reveal the problem. Calculate a simple escape scenario to teach probability, but explicitly state that independent detection probabilities across tests are rarely a valid literal description of correlated defects.

Finally rehearse an incident. The external storage service returns success for a metadata operation while rejecting a later upload step. Decide what the user should see, which metrics alert responders, how affected applicants can resubmit, and how the institution records deadline exceptions. The QA deliverable consists of risk-linked evidence, not a badge asserting that the application is bug-free.

### Review of quality assurance evidence
For the grant application portal, the most important tests cover deadline decisions, durable receipt, cross-applicant privacy, and recovery from storage failure. Run a controlled failure after the metadata transaction but before object content is durable. The system must not present an unqualified final submission success if evidence is missing. Use mutation testing to verify that a changed authorization condition causes a meaningful test failure. Examine whether every alert has an actual owner and diagnostic procedure. When a test fails intermittently, preserve logs and isolate environmental variability instead of simply retrying until the pipeline turns green. A trustworthy QA packet states what was actually exercised and the remaining untested risks. Its purpose is to support a reasoned release decision, not to manufacture certainty.

# Fully worked questions

## Toy defect-detection model and its limitations

Assume a single defect independently escapes each of four review or test stages with probability 0.7. Calculate its probability of escaping all four. Explain why the result should not be used as a real-world prediction of project quality.

**Analyze the assumptions.** Under the explicit independence assumption, multiply conditional escape probabilities: 0.7 × 0.7 × 0.7 × 0.7 = 0.2401, or 24.01 percent.

**Develop the result.** Actual tests may share mistaken specifications, fixtures, or code paths. Their outcomes are then correlated. Different defect classes also have different detection probabilities, and severity is not represented in this one-defect model.

**Check interpretation and failure cases.** Improve evidence through independent test strategies and by checking important system invariants, especially privacy, consistency, and fault recovery. Never report 24.01 percent as the measured escape probability of the application.

**Answer.** Toy escape probability = 24.01%; independence and identical rates are illustrative assumptions only.

## Why coverage cannot replace authorization testing

A package reaches ninety-five percent line coverage, but the API has no test checking access across tenant boundaries. Identify the missing quality evidence and propose a small test that could discover a severe defect.

**Analyze the assumptions.** Line coverage only records that statements executed. A test that reads another tenant’s record and asserts the content exists may increase coverage while failing to inspect the correct authorization behavior.

**Develop the result.** Create two tenants with overlapping local identifiers and users authorized only for their own resources. Authenticate as tenant A, request tenant B’s private record through each access path, and assert access is denied without leaking confidential details.

**Check interpretation and failure cases.** Repeat after a cache is warmed by tenant B, because a cache key that omits tenant identity can accidentally return cross-tenant content. Complement automated tests with code review of resource ownership checks.

**Answer.** Authorization invariants require negative tests; high line coverage alone does not establish them.

## Reproducible artifacts and database migration order

A deployment builds a new web artifact expecting an additional database column. Some application instances still run the old version while a rolling update proceeds. Describe a safe migration order and what rollback can and cannot guarantee.

**Analyze the assumptions.** First expand the schema so old application instances remain compatible. Deploy code that can read or write both representations as needed, then backfill in controlled batches and measure data consistency.

**Develop the result.** Only after supported clients and all application instances have migrated should the old field be removed. The production artifact should be the same tested artifact rather than rebuilt independently with changed dependencies.

**Check interpretation and failure cases.** Rolling code back may restore executable behavior but cannot reliably undo a destructive data transformation. A recovery strategy must specify reversible steps, backups tested by restoration, and forward-fix options.

**Answer.** Expand schema before incompatible code; migrate consumers; contract only after validation and a recovery decision.

