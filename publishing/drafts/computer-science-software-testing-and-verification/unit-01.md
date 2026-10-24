# Unit 1: Quality foundations

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 1.1 Specifications

### Core reasoning and definitions

A specification establishes the behavior a system promises at an observable boundary. It can describe input domains, output values, ordering constraints, state transitions, timing limits, data ownership, authorization, or recovery after failure. The useful question is not merely whether a program matches a document, but whether the document states an observable requirement precisely enough to distinguish correct behavior from incorrect behavior. Consider a digital-library borrowing endpoint. A statement such as “loans should be handled quickly” lacks a measurable threshold and an operational context. A stronger contract says an authenticated eligible reader may borrow one available copy; the operation either creates exactly one active loan and returns its identifier or reports a declared rejection without consuming a copy. Invariant preservation matters under simultaneous requests, not only ordinary sequential calls. Preconditions describe what callers must supply, postconditions describe successful results, and invariants constrain every reachable committed state. These ideas allow a test to select a clear initial state, execute a transition, and inspect both response and persisted effects. Specifications are themselves hypotheses about stakeholder intent and deserve review before test implementation.

### Original investigative exercise

For an enrollment service define capacity=2, initially zero enrolled, and requests from three distinct students. A sequential execution should accept two and reject one; a concurrent execution should never commit three confirmed enrollments. Inspect the response and database constraint, not a UI toast alone. Record the assumption that one student cannot hold two active seats. If the product instead allows waiting lists, amend the transition model and expected rejection type. An executable state model can enumerate valid request sequences and compare actual service states with model states. Maintain a table pairing each requirement identifier with negative and positive examples, and flag requirements for which no observable oracle exists.

### Limits and counterexamples

A test saying “status is 200” is not a complete specification: a service might return 200 while changing the wrong student's loan. Similarly, a test derived solely from existing implementation choices may reproduce the same misunderstanding. Ambiguity must be resolved with domain owners, not hidden in fixture values.


### Deep dive: traceability, oracles, and controlled evolution of requirements

Requirements in substantial projects seldom arrive in a stable, complete form. A course-booking service might initially allow one enrollment per learner; a later policy permits auditing without granting credit; another permits a wait-list seat that automatically converts to active when a student leaves. If the test suite encodes the original “only one record per learner” rule, tests may fail for correct new behavior. Conversely, if developers delete those failing tests without building the new state model, the suite loses important invariants. Requirement traceability is the mechanism for recording which behavior an assertion is meant to protect. Each numbered requirement should have a rationale, an observable oracle, the versions in which it applies, and references to tests that exercise it. Distinguish a requirement being exercised from its behavior passing. One failed exercise can satisfy a coverage count while correctly signaling a defect.

Create two sample versions. In version A, a course has capacity two and no wait-list. In version B, the wait-list is enabled with a maximum of five queued requests. The initial state consists of two enrolled learners, zero queued learners, and capacity two. In version A a third valid request is rejected. In version B the third valid request is queued but has not consumed an enrolled seat. A test that asserts all three requests return HTTP 200 would miss a serious error: the third might incorrectly be enrolled above capacity. A better oracle checks response type, durable enrolled count, queue position, and the state transition allowed by the relevant version. Requirement identifiers must distinguish “confirmed enrollment never exceeds capacity” from “wait-list length is bounded” even though one request can exercise both.

An oracle may be independent, redundant, or derived. An independently coded reference model can provide a different implementation of an expected policy. A derived oracle may compare an input transformed under a known metamorphic relation, for example reversing the order of independent registration requests should preserve the total number of confirmed seats, though it need not preserve which learner wins when priority depends on ordering. A redundant oracle may combine a response assertion with direct database inspection and an emitted audit event. Redundancy can catch misleading UI success, but not when all checks call the same flawed service. The more sources share logic and data, the less independent their apparent agreement becomes.

Formalize a contract as a relation between prior state S, request r, and subsequent state S'. For valid successful enrollment, require `enrolled(S') = enrolled(S) + 1`, capacity is not exceeded, and exactly one enrollment belongs to the authenticated learner. For failed enrollment, require that the persisted enrollment count remains unchanged. This relation makes tests explainable and enables model-based generation. It is not enough to take a snapshot of the database: the model must specify which columns can change and which are forbidden. An audit log may legitimately grow even when enrollment fails; a too-broad assertion that the database is identical before and after would reject correct logging.

Test oracles can themselves be faulty. Consider a grading reference that copies the application's boundary constant. If the constant is wrong in both places, the suite consistently endorses incorrect grades. Review reference policies against the independently approved requirements rather than only against code. Reviewers should challenge hard-coded dates, locale conventions, sorting rules, and exceptional cases. For example, “the earliest valid request wins” needs to define whether earliest refers to client clock time, server arrival, or transaction commit. No amount of random load can compensate for an oracle grounded in an ambiguous rule.

An exercise coverage dashboard needs contextual caveats. Imagine 80 of 100 requirements have tests, giving 80 percent exercised coverage, but the remaining 20 include both payment authorization and data-deletion guarantees. The numerator is easy to calculate; the decision to release is not. Use a risk matrix that separates severity, plausibility, and observability. A high-severity invariant might require model checking, concurrency tests, and production monitoring, while a cosmetic label change may require only a browser accessibility check. This allocation does not license neglecting apparently low-priority accessibility failures; the risk model should explicitly represent who is excluded when keyboard operation breaks.

At the end of a review, record changes as testable propositions. Rather than “fixed enrollment,” write “for an authenticated eligible learner and a course with one remaining seat, a successful reserve request results in one committed row and prevents competing transactions from consuming the same seat.” Specify a synthetic seed, setup script, and observation query. The requirement may evolve, but its history and test intent remain auditable. Tests make meaningful claims when the desired system behavior, evidence, and limitations are all visible to someone who did not write the application.


### Unit synthesis: distinguishing the presence of a test from its claim

A testing report should include a sentence describing the exact behavior each test claims to establish. For the reservation example, a test might show that no two concurrently committed successful holds refer to the same copy during one controlled interleaving. It should not be summarized as “concurrency is correct,” because other interleavings, expiry races and database configurations remain outside that experiment. When reviewing requirements, separate the original policy from its implementation, the test oracle from the test input, and an observed pass from a general correctness proof. Requirement versioning matters when product rules evolve: the same recorded output can be correct under one policy and wrong under another. The exercise at the end of this unit is to construct a traceability matrix whose columns include version, requirement statement, expected outcome, oracle mechanism, execution conditions, observed outcome, and unresolved risk. If one cell is unknown, mark it unknown instead of guessing. Students should be able to justify why a test exists without appealing to the implementation's current behavior.

## 1.2 Faults

### Core reasoning and definitions

A fault is a defect in an artifact or internal decision, while a failure is an observable deviation when the fault is executed under activating conditions. An error is an incorrect internal state that may or may not propagate to a failure. A latent sorting defect might remain unnoticed when numbers are positive and distinct but produce incorrect results on equal keys. Not every incident follows a single fault-to-failure chain: deployment changes, data inconsistency, races, and external dependency states can interact. Distinguish a test failure signal from a confirmed product defect; a stale fixture or incorrect assertion can also make a test fail. Fault models organize expected vulnerabilities such as off-by-one conditions, incorrect comparison operators, lost updates, null dereferences, truncation, and mismatched encodings. The model informs which inputs and states are valuable, but a catalog of common faults is not proof that all others are absent.

### Original investigative exercise

Inject a controlled comparison bug into a grading rule: pass when score is greater than 50 rather than at least 50. Values 49,50,51 demonstrate the decision boundary; scores 10 and 90 alone probably will not. Record the defect, triggering condition, internal state, and expected external failure as distinct observations. For a race, synchronize two requests for the final seat using a barrier; a sequential test can never reproduce the same interleaving. To confirm an observed failure, replay with captured sanitized inputs, pinned code, deterministic clock, and controlled dependencies. Minimize the counterexample until the essential trigger remains.

### Limits and counterexamples

A failed test caused by a mocked database returning an impossible result should not be assigned to the production service. Conversely, a green suite does not establish the absence of defects: it may simply lack activation conditions for the remaining faults.


### Applied laboratory: specifying a digital library reservation service

A university digital library provides a revealing setting for the difference between feature descriptions and testable contracts. An administrator creates a title, adds physical copies, and allows readers to request a temporary reservation. Each copy has a stable identifier. The naive story says that clicking Reserve should show a success message. That is insufficient because two readers could reserve the same copy, the interface could show success without committing a transaction, or the same person could reserve multiple copies despite an eligibility rule. Begin with a state model rather than with web-browser automation. Define a `Copy` entity with states Available, Held, Loaned, and Withdrawn. Define a `Reservation` with a reader identifier, copy identifier, creation time, expiry time, and an independently generated reservation token. Write down the legal transitions: Available to Held on successful reservation, Held to Loaned on pickup, Held to Available on expiry, and any state to Withdrawn only under a permitted administrative operation. Readers cannot transition directly from Available to Loaned if policy requires a hold record. A transition diagram makes illegal events discussable before code exists.

A safety invariant is that each copy has at most one active hold or loan. A second invariant is that a reader with an expired account cannot gain a new hold. A third is conservation: for every title, the number of available, held, loaned, and withdrawn copies sums to the recorded inventory count, provided no administrative add or removal occurs. These invariants cover more than visible messages; they constrain committed database rows. When the reservation endpoint returns a token, the database must contain a corresponding active reservation bound to the authenticated reader. A test oracle should examine that persisted relationship, not merely a success response. If a request is rejected, it must not silently decrement available inventory. To avoid the test itself creating the defect, use separate queries to observe the state and avoid sharing the same business function that implemented the mutation.

Construct a deterministic test fixture with one title, two copies, an eligible reader, an ineligible reader, and a controllable clock. Freeze the clock to an arbitrary instant such as 09:00 and configure a hold period of exactly 15 minutes. At 09:14:59 the hold remains active; at the specified expiry boundary, its state changes according to the explicitly agreed inclusive or exclusive rule. A reviewer must decide whether an expiry exactly equal to now counts as expired. The test cannot invent this policy silently. Use transactional cleanup so a failed assertion does not leave state for the next test. Test repeat submission with the same idempotency key; the second attempt should return the same reservation instead of allocating another copy. Repeat with a different key and confirm that the user's per-title limit is applied. Test authentication separately: a fabricated reader identifier in a JSON body must not override the verified principal bound to the request.

Now exercise concurrency. Start with one available copy and schedule two requests to pass validation before either transaction commits. A correctly isolated reservation transaction must permit at most one successful transition to Held. Record both responses and inspect committed rows. This is a stronger observation than measuring a small probability of collision under ad hoc parallel load. If the implementation performs a read, then an unconditional update, the test can trigger a lost update. A conditional update with a row-version predicate, or a transaction with suitable locking, can preserve the invariant. This does not prove every deployment configuration correct: transaction isolation, replica routing, and retry behavior matter. State the database engine and isolation assumptions in the test evidence.

Distinguish contract-level tests from implementation-specific tests. A contract test may assert that an expired hold is not returned as active and that another reader can eventually reserve its copy. It should not ordinarily assert the private method name that schedules expiry. A storage-unit test may legitimately inspect an SQL row lock or optimistic version. Neither substitutes for a student testing accessibility of the Reserve action: the control should have an accessible name, keyboard focus, and useful failure messaging. A good test plan uses several kinds of evidence at their appropriate boundaries rather than claiming one end-to-end assertion proves everything.

Finally prepare a requirements matrix. For each invariant and transition, list the minimal successful path, the relevant denied path, an edge condition, and the observable state used as oracle. Mark unknown policies as questions. Two teams can execute the same test suite and reach opposite judgments when they silently assume different semantics for expiry or replacement stock. The quality of a specification is therefore visible in whether independent testers can reach the same expected outcome without reading the implementation.


## 1.3 Test Oracles

### Core reasoning and definitions

A test oracle decides whether an observed result is acceptable. For arithmetic functions the oracle may be independently derived mathematics; for a parser it may be a standard, reference implementation, or round-trip law; for a user journey it may be an agreed business rule and persisted state. A reliable oracle must be independent enough that implementation and expected value do not share the same bug. Snapshot tests can reveal unintended changes, but accepting every snapshot update merely transfers trust to the current implementation. Some behaviors have no single known exact answer. Metamorphic relations can test relationships instead: permuting inputs to an order-insensitive sum should not change the total, and increasing a permitted credit limit should not reduce the set of accepted amounts if all other conditions stay fixed. Partial oracles and human review remain necessary for visual usability and requirements that express judgment rather than arithmetic truth.

### Original investigative exercise

Suppose a discount function applies 10% to eligible prices. For a 120-unit price, independent arithmetic gives 108 units after discount. Derive the oracle outside the function under test and compare exact decimal cents rather than loosely using a floating-point threshold. Add a property: for nonnegative valid prices, the discounted amount cannot exceed the original. Then test an ineligible customer to ensure unchanged amount. On disagreement, distinguish a flawed oracle from a flawed implementation by checking the written rule and an independent manual calculation. Store the rule version alongside the test so that intended policy changes are not silently treated as regressions.

### Limits and counterexamples

It is circular to compute expected output by calling the same helper the production function uses. A visual golden-image match is also incomplete if accessible names, keyboard focus, or hidden state are wrong despite identical pixels.

### How to interpret the interactive model: requirement coverage

The requirement coverage slider records how many of a hypothetical set of one hundred equally counted requirements have at least one executed check. It does not measure the fraction that passed, or the strength of any oracle. Move the slider from 60 to 100 and observe that uncovered requirements fall from forty to zero. Nothing in this arithmetic prevents all one hundred checks from asserting the wrong expected result. For a real project, define requirement identity and traceability before treating an exercised count as meaningful. Split compliance, safety, and usability requirements rather than averaging them without context. At the lower boundary zero, there is no exercised coverage; at the upper boundary one hundred, it is possible to have nominal complete exercise coverage while having untested combinations, concurrency races, and invalid requirements. Use the tool to understand the numerator and denominator, not to calculate release readiness.

## 1.4 Coverage Criteria

### Core reasoning and definitions

Coverage is a measurement of the items exercised by a test suite under a defined model. Statement coverage counts executed statements; branch coverage concerns decision outcomes; condition coverage asks which Boolean subconditions received each truth value. Modified condition/decision coverage (MC/DC) provides stronger evidence that individual conditions can independently affect an outcome under its stated definition. Requirements coverage tracks evidence against agreed features, which code coverage alone cannot substitute. A high percentage tells how much measured structure was visited, not whether assertions were correct or the specification complete. A test may execute a branch but fail to detect a wrong result because it checks only that no exception occurred. Conversely, a compact property test can reveal a defect without maximizing structural coverage. In multi-module systems, coverage aggregation must preserve file identity, exclude generated artifacts consciously, and distinguish unit from integration instrumentation.

### Original investigative exercise

Analyze authorization condition `active AND (owner OR admin)`. Construct inputs where active varies while ownership and administration are controlled, then cases where owner and admin separately determine the result. Record statement, branch, and condition coverage in separate columns. Verify that the authorization oracle rejects a suspended administrator if policy requires active status. Run the suite with a deliberately inverted owner check to see whether an assertion fails, not merely whether a branch counter increments. When collecting coverage from subprocesses and browser bundles, avoid treating missing instrumentation as zero tests; mark gaps rather than asserting complete coverage.

### Limits and counterexamples

An apparently perfect 100% statement score may coexist with an unchecked arithmetic result or a missed concurrency interleaving. Coverage reporting should state precisely its denominator, instrumented build, and excluded components.

### How to interpret the interactive model: oracle precision

This model fixes eighty true-positive alerts and varies the number of false-positive alerts. Precision is TP divided by TP plus FP. With twenty false positives, the result is 80/(80+20)=80 percent; with eighty false positives, it falls to fifty percent. Precision alone cannot describe how many faults were missed, because false negatives are not included in this model. If a student interprets higher precision as universally better detection, introduce a recall tradeoff: increasing the detector threshold may hide more real defects. The slider does not model underlying prevalence changes or costs of false alerts. For deployment decisions, report a confusion matrix with independently adjudicated ground truth, appropriate confidence intervals, and a threshold selected for the harm profile of the actual service. A checking tool that flags every legitimate user can have high recall but harmful operational consequences.

## Fully worked questions

### Worked problem 1.1: Specifications

A catalog has 48 independently named requirements; executable checks exercise 36 of them, and six exercised requirements fail their oracles. Compute structural exercise coverage and the count of exercised requirements whose checks pass. Explain whether this proves the other 12 requirements are correct.

**Define the property and assumptions.** Define coverage as the number of distinct named requirements exercised divided by the total requirements, not the number of executed assertions. Here the denominator is 48 and the numerator is 36. Distinguish exercised from satisfied requirements because a check can reveal a failure while still exercising the requirement.

**Compute or execute the reasoning.** The coverage is 36/48 = 0.75 = 75 percent. If six distinct exercised requirements demonstrably fail and the remaining checked requirements pass, then 30 exercised requirements have passing checks. That yields 30/48 = 62.5 percent of named requirements with recorded passes, conditional on each requirement having a meaningful oracle.

**Interpret the conclusion and limitations.** Twelve requirements are not exercised, and a passing check is still weaker than a proof of general correctness. Inspect weighting and dependencies: a safety-critical reservation invariant should not be treated as interchangeable with a decorative wording requirement. Report the failing six and missing twelve separately; do not combine them into one reassuring number.

### Worked problem 1.2: Faults

Two readers attempt to reserve the sole available copy at exactly the same time. Specify the invariant, one deterministic race schedule, and a valid final outcome. Why does a fast green UI check fail as an oracle?

**Define the property and assumptions.** Let H be the set of active holds for copy c. The invariant is |H| <= 1. Initialize the store with one Available copy and no active holds; freeze unrelated background expiry so only the intended concurrency determines the result. A reservation success must atomically bind a reader and hold token to the copy.

**Compute or execute the reasoning.** Arrange a barrier so both transactions read the initial availability before either writes. Then let one attempt the conditional update first and the other observe the conflict. A valid committed result has exactly one active hold and at most one successful reservation response. The losing request should return a conflict or a documented alternative, not a second successful hold.

**Interpret the conclusion and limitations.** A green UI state may be optimistic, cached, or emitted before commit; it cannot establish the persistent invariant. Observe committed rows through an independent query, match each success token to the correct authenticated reader, and repeat against the production database's transaction isolation. A test that only happens to pass under light load has not ruled out the race.

### Worked problem 1.3: Test Oracles

An anomaly detector flags 40 genuinely faulty and 20 healthy requests. It misses 10 faulty requests. Calculate precision and recall, then choose which metric matters more for an automated account suspension system.

**Define the property and assumptions.** Classify outcomes using ground truth independent of the detector. True positives are 40, false positives are 20, and false negatives are 10. Precision asks what fraction of flagged requests were faulty; recall asks what fraction of all genuinely faulty requests were detected.

**Compute or execute the reasoning.** Precision = TP/(TP+FP) = 40/60 = 2/3, approximately 66.67 percent. Recall = TP/(TP+FN) = 40/50 = 80 percent. These are different: improving recall can create more false positive suspensions, and raising the threshold may trade some recall for higher precision.

**Interpret the conclusion and limitations.** For automatic suspension, false positives can deny legitimate users service, so a high-precision operating point plus manual review may be appropriate. The final threshold depends on cost and prevalence, not one universal rule. Validate detector labels with independent evidence, test data drift, and record acceptable false-positive rates explicitly.

