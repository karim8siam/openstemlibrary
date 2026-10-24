# Unit 2: Unit and integration testing

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 2.1 Isolation

### Core reasoning and definitions

Isolation defines the boundary at which a test controls state and collaborators. A unit test may replace a slow network client with a fake, but should still execute the logic it claims to verify rather than mocking every meaningful decision. Isolation improves speed, repeatability, and fault localization at the cost of realism. A database mock cannot prove SQL constraint behavior; a local service with a real database can test it at higher cost. Different boundaries answer different questions. The design begins by identifying the component's contract and the observations a caller can legitimately make. Hide irrelevant nondeterminism such as clocks and random values behind explicitly injected interfaces, while keeping pure transformations directly testable. Do not confuse “one function per test” with isolation: global state, environment variables, caches, files, and asynchronous workers can couple tests even if no application object is shared.

### Original investigative exercise

Test a certificate-expiry decision with an injected clock fixed at the exact expiry instant. Verify the contract's inclusive or exclusive boundary rather than allowing the machine wall clock to change the answer. Next replace only the notification transport with a capturing fake and assert one intended message with the proper recipient. Keep the eligibility decision real. Then add an integration test using the real queue adapter to confirm serialization and retry semantics. Run tests in reverse order and in parallel to detect shared global state. Document which collaborator is simulated and which is genuine for each evidence claim.

### Limits and counterexamples

A test that replaces the policy checker with a stub returning `true` has not verified the policy checker. The use of mocks cannot compensate for failing to exercise the behavior of interest.


### Deep dive: test doubles as measurement instruments

Test doubles are often classified as dummies, stubs, spies, mocks, and fakes, but these names are less important than the epistemic role of the substitute. A dummy exists only to satisfy an interface; it should not influence the outcome. A stub returns prescribed values to drive a path through the unit. A spy records interactions for a later assertion. A mock embeds expectations about calls, usually making a failure when interactions differ. A fake has useful behavior, such as a small in-memory repository. Any one of these can make a test deterministic while reducing realism. Write down what the substitute is allowed to prove and what it hides. A fake database that lacks unique constraints cannot establish correct concurrent reservation behavior, regardless of how many tests pass.

Consider an invoice service with dependencies on a tax calculator, payment provider, invoice repository, and message broker. The tax calculator is a pure function of a tax rule and item prices; unit tests should probably exercise it directly. The provider adapter communicates over HTTP and benefits from contract fixtures representing its documented responses. The invoice repository depends on transaction isolation and uniqueness constraints that must be tested using the target database engine. The broker can be represented by a spy for orchestration assertions, but ordering and delivery semantics require integration checks. If every dependency is mocked, the service may merely be tested for calling methods in an anticipated order, not for producing the right business result.

Build a fault matrix with five rows: successful provider response, client authentication rejection, duplicate event delivery, temporary timeout, and malformed provider payload. For each row, specify expected retry policy, persistence mutation, outward response, and log behavior. A timeout is not the same as a confirmed rollback: the remote provider may have committed before the response was lost. A permanent authentication rejection normally requires intervention instead of rapid retry. Duplicate events should be idempotently acknowledged without repeating ledger movement. A malformed payload must not lead to a partially trusted object in storage. These are externally meaningful contracts that can be enforced with test doubles and later checked against a provider sandbox.

Use fixtures carefully. One team might create a “validInvoice” function returning a mutable object shared by every test. If the refund test changes its status to Reversed, the settlement test that runs later can fail unexpectedly. Prefer factories returning a fresh value or immutable snapshots. A database transaction per test can ease cleanup, but that wrapper itself may hide behaviors involving independent transactions. Concurrency tests need multiple connections and a deliberate interleaving, not one connection inside a global test transaction. Failing to separate these tests can create false confidence about isolation.

A useful isolated experiment forces a crash after a commit and before a provider acknowledgment. On replay, the event identifier is already present; the handler should not create a second settlement but may need to resend an acknowledgment. Now force a crash before commit. Replay should perform the settlement once. The two windows can share the same external symptom, a missing acknowledgment, but have different correct recovery paths. A spy recording the number of attempted notifications cannot on its own establish durable exactly-once accounting. Observe committed ledger rows and outbox entries after controlled faults.

Testing libraries frequently encourage interaction snapshots. For example, asserting `repository.save` was called once with particular arguments can pass even if the repository silently discards the write. An integration test that queries persisted state catches the problem. The opposite risk also exists: a black-box test that sees a correct final state may not discover that the service emitted a duplicate external message as a harmful side effect. Choose assertions according to the risk: state conservation, callback count, protocol schema, durable side effects, and rejection behavior each reveal different faults. Keep sensitive identifiers synthetic.

Evaluate maintainability as part of evidence quality. A suite that fails whenever a harmless internal helper is renamed wastes engineering time and can encourage broad assertion deletion. Prefer semantic assertions at stable boundaries and reserve implementation-specific call checks for genuinely required behavior, such as refusing to contact a provider after credential rejection. Record the purpose of each test double so future engineers know when an API change requires updating the fake and when it indicates a real contract regression. The strongest testing architecture does not maximize mocking or eliminate it: it pairs deliberate control with independent reality checks.


### Unit synthesis: choosing realistic versus controllable collaborators

For a new software component, list all external dependencies and mark whether their correctness is inside or outside the test's chosen boundary. Substitute a deterministic fake when a unit test needs to trigger an error path reliably, but verify the fake's protocol against the actual dependency at a separate level. A fixture that returns success in every case cannot support a claim about authorization failures, duplicate events or timeout handling. An in-memory repository is not a valid oracle for transaction locking unless it actually reproduces those semantics. Compare two contrasting failure scenarios: a process crashes before committing its ledger and it crashes after committing but before acknowledgement. Both can appear as a timeout to the sender, yet idempotent recovery must distinguish durable state. The practical learning outcome is the ability to write a failure matrix and to name which real components must participate in verifying each claim. Isolated and integrated tests are complementary rather than competitors.

## 2.2 Fixtures

### Core reasoning and definitions

Fixtures create known initial conditions and allow tests to leave an environment clean. A fixture can include synthetic users, database rows, temporary files, fixed configuration, clock values, or a prebuilt object graph. Good fixtures are minimal, explicit, and named by the behavior they enable rather than by a giant universal dataset. State leakage can turn test ordering into an accidental dependency. Unique namespaces, transactional rollbacks where appropriate, temporary-directory isolation, and cleanup in finally blocks reduce contamination. Database snapshots offer a fast reset mechanism but can hide migration errors if refreshed from an outdated schema. Test data should avoid real customer secrets. Generated values require deterministic seeds when reproducibility matters; random names alone do not guarantee isolation if shared external resources persist across executions. Fixture teardown failures are themselves test failures requiring diagnosis.

### Original investigative exercise

Create a library database fixture with two catalog items, one borrower and one active loan. Execute a return operation, assert both the API result and the loan-status transition, then roll back or destroy the fixture. Repeat in a fresh environment and confirm no identifier collision. Add a deliberately failing assertion after data insertion; teardown should still restore the initial state. Test a retry path where the application writes to storage and fails before database commit, because transaction rollback may not remove a separately created object. Capture the cleanup evidence explicitly instead of assuming database and object store share atomic transactions.

### Limits and counterexamples

A fixture loaded with hundreds of unrelated entities makes a passing test hard to interpret. It also permits unintended queries to appear successful because some record happens to match an unsafe default.


### Applied laboratory: isolating a payment-ledger integration

An educational payment service has a checkout API, an invoice store, a ledger writer, and an external provider adapter. An apparent unit-test convenience is to replace every dependency with a mock returning success. That can prove that the controller calls expected collaborators, but it does not establish that the service generates correct ledger entries or handles real provider responses. Define the boundary of the unit under test before choosing a replacement. If the target is the tax calculation, external communication is irrelevant and a pure deterministic function may need no mock. If the target is invoice settlement, the database transaction and idempotency mapping are the central behavior, and mocking them away destroys valuable evidence.

Specify a small ledger vocabulary. Every settled invoice references a unique provider event identifier, has a nonnegative total in minor currency units, and produces balanced entries under the accounting model. For a simplified two-account ledger, record a debit of 12,500 cents and a credit of 12,500 cents so that the signed sum is zero. Avoid floating-point equality tests such as comparing 125.00 to the result of repeated decimal addition. Use integer minor units or a decimal type with explicit rounding policy. When the provider resends the same event, processing should be idempotent. However, two distinct events with the same invoice identifier must follow the business rule: an attempted double settlement might be rejected, while a refund is a new transaction with its own type and reference. A mock returning one generic success object cannot verify this distinction.

Create three categories of fixtures. Pure fixtures supply immutable invoice objects and expected totals. Database fixtures supply transactionally seeded rows, including a conflicting uniqueness constraint, and clean up even after a test throws. Provider fixtures use captured, anonymized protocol examples that respect version and signature-validation semantics; never embed production API credentials. Use a controllable fake provider to return a success payload, transient timeout, malformed message, duplicate delivery, and permanent client error. These doubles are useful only if the real adapter contract is tested separately against a maintained contract fixture. The fake must not represent behavior that the provider would never send.

Consider retries. The service receives a settlement event, writes an outbox record, and attempts a downstream notification. If notification fails after commit, a retry must not generate a second ledger entry. Model the order of effects: validating signature, authorizing state transition, committing ledger and outbox atomically, acknowledging receipt, and asynchronously delivering notifications. Inject an exception after the ledger write but before the outbound acknowledgment. On replay, query the ledger for one committed transaction and check that the outstanding outbox message can still be retried. The test oracle has two dimensions: money is not duplicated and notification progress is recoverable. A suite asserting only that an exception is raised would miss both.

Test data contamination often appears as hidden fixture coupling. A test that sets the global exchange rate to a particular value may cause a later tax test to fail depending on execution order. Execute the suite in a randomized order and in two isolated workers; compare failing-test sets and inspect globally mutable state. An independent in-memory database per test can help, but it may not reproduce production locking, collation, or transaction semantics. Run a smaller integration suite on the same database family as production. A tradeoff emerges: isolation improves repeatability while realistic components expose interaction faults. A mature suite uses both, with deliberate responsibilities and separate failure interpretation.

When designing assertions, identify whether they concern calls, state, or protocol. A call-count assertion such as `sendOnce` is suitable for verifying a specific orchestrator policy but can be brittle during refactoring. A state assertion that a ledger remains balanced is resilient to many internal changes. A protocol assertion that an unauthorized webhook yields a rejection and no persistent mutation guards the public boundary. Prefer the narrowest assertion that directly expresses a required property; include other observables where the failure mode demands them. A test double is not a miniature replacement for production reality: it is a controlled instrument whose purpose and limitations must be documented.


## 2.3 Interface Tests

### Core reasoning and definitions

Interface tests focus on compatibility between independently developed components. The interface may be a function signature, an HTTP schema, a database message format, or an event contract. At a request boundary, test required and optional fields, version negotiation, error encoding, idempotency, authorization expectations, and the handling of unknown fields. Consumer-driven contracts describe assumptions a caller actually depends upon; provider verification ensures those expectations hold for a deployed provider version. An interface test cannot replace an integration test for stateful semantics, but it can expose breaking renames before deploying multiple services. Serialization can introduce subtle defects in decimal precision, timestamps, time-zone handling, Unicode normalization, null versus missing fields, and very large identifiers. Test the wire representation rather than only in-memory objects.

### Original investigative exercise

Define a user profile response with `id`, `displayName`, and optional `avatarUrl`. Check that omitting an optional field is accepted by the client and that changing `id` from a string to a number is rejected if the agreed contract requires a string. Test 401 and 404 error payloads, including the absence of private user information. Add a compatibility test for one old consumer version when the provider adds a field. Treat order of JSON object properties as irrelevant, but preserve order for arrays where the contract specifies it. Pin each side's schema version and run validation on actual encoded messages.

### Limits and counterexamples

A fake service coded by copying the client assumptions can pass even if the real provider behaves differently. Periodically exercise the published provider and version policy before claiming compatibility.

### How to interpret the interactive model: fixture contamination

The fixture risk simulator asks what happens to a batch when contamination events are modeled as independent Bernoulli trials. If each of twenty tests has a ten-percent chance of mutating shared state, the hypothetical probability of a clean batch is 0.9^20, approximately 12.16 percent. At risk zero the clean probability is one; at risk fifty percent it becomes tiny. The independence assumption often fails: one leaked global object can contaminate several later tests at once, while a reset fixture can make contamination mutually exclusive. The model therefore does not predict a real team's flaky suite without evidence. Use it to motivate setup and teardown discipline, immutable fixture factories, process isolation, and randomized-order experiments. Inspect whether a contaminated state actually causes an observable assertion failure; the two events should not be conflated.

## 2.4 Dependency Handling

### Core reasoning and definitions

Dependency handling is about observing failure at collaboration boundaries without making a suite depend on uncontrolled external systems. A production service may contact databases, caches, clocks, object storage, third-party APIs, and message brokers. Every dependency can be unavailable, slow, return malformed data, or respond ambiguously after partially completing work. Tests should reflect the declared failure semantics: bounded retries for retryable operations, deadlines, cancellation, fallback where safe, and explicit errors where fallback would mislead. Simulators and fakes are valuable for forcing rare failures deterministically, but must implement meaningful parts of the real protocol. A test double that never models timeout, duplicate delivery, or ordering will overlook precisely the problems that motivate dependency testing. Maintain separate adapter contract tests against a real implementation.

### Original investigative exercise

For an asynchronous email job, configure a fake transport to time out on attempt one, return a transient error on attempt two, and succeed on attempt three. Assert a maximum of three attempts, bounded delays under an injected clock, and one final job status. Then simulate a permanent 400-type rejection: the worker should not retry it indefinitely. For an enrollment API, distinguish a transport timeout before the database operation from a lost acknowledgement after commit; idempotency behavior must cover the second case. Measure whether cancellation actually terminates in-flight work or only stops waiting in the caller.

### Limits and counterexamples

Replacing every network failure with immediate success makes a suite fast but silent about resilience. Conversely, tests against live external services can be flaky, costly, and ethically inappropriate when they create real messages or charges.

### How to interpret the interactive model: retry probability

A request can fail because of a transient network condition or because its operation is permanently forbidden. This simulation represents three independent attempts with an identical per-attempt success probability. If each attempt succeeds with probability 70 percent, all three fail with probability 0.3 cubed, so success by the third attempt is 97.3 percent. It makes no claim that retries are safe: an operation may have committed before the response was lost. Without an idempotency key, repeating payment or enrollment requests can create duplicate effects. Correlated outages invalidate the independent-trial formula, and unbounded retries create overload when service is struggling. When experimenting, compare the reported probability against manual multiplication and discuss which failure classes are retryable, which require human intervention, and which require querying a durable operation identifier before another attempt.

## Fully worked questions

### Worked problem 2.1: Isolation

A ledger settlement posts a debit of 12,500 cents and a matching credit. A worker crashes after committing but before acknowledging the provider event. Design the replay test and expected ledger balance.

**Define the property and assumptions.** Seed an unpaid invoice and a provider event identifier E. The handler's transaction must insert the event idempotency record and paired ledger entries together. Define invariant sum(signed ledger entries for E)=0 and at most one settlement transaction for E.

**Compute or execute the reasoning.** Deliver E once, arrange a crash immediately after commit, then resend E. The initial committed state contains +12,500 and -12,500 cents, yielding a signed total of zero. After replay there must still be one accepted event identifier and exactly the original balanced posting, not duplicate entries totalling twice the amount.

**Interpret the conclusion and limitations.** A fake adapter can supply the duplicate message, but an integration test must use the actual uniqueness constraint and transaction manager. Check that downstream notifications are retried through the outbox without repeating money movement. If acknowledgment had been issued before commit, a different crash window might lose the settlement entirely.

### Worked problem 2.2: Fixtures

A suite of 20 tests shares mutable global state; assume each independently contaminates the state with probability 0.02. What is the chance that at least one contamination occurs? What changes if the events are correlated?

**Define the property and assumptions.** Model each contamination event as a Bernoulli trial only for this mathematical exercise. Under independence, the probability of a clean run is the product of twenty clean-test probabilities: (1-0.02)^20.

**Compute or execute the reasoning.** The clean probability is 0.98^20, approximately 0.667608. The complement gives P(at least one contaminated event) = 1-0.98^20, approximately 0.332392 or 33.24 percent. This result concerns at least one contamination event, not the proportion of suites that visibly fail; some contamination may not activate an assertion.

**Interpret the conclusion and limitations.** Shared globals often cause dependence, invalidating the power rule. Instead of using this idealized number as a production forecast, isolate fixtures, randomize order, track mutation points, and rerun the suite across separate processes. Instrumentation should distinguish contamination from confirmed test failure.

### Worked problem 2.3: Interface Tests

An API may return success, timeout, or a permanent authentication error. Draft three consumer contract tests that a hand-written fake cannot safely replace.

**Define the property and assumptions.** Specify the provider's externally documented status codes, response schema, retry headers, and authentication semantics for one pinned API version. Select a successful request with a synthetic token, a transient timeout, and a request with deliberately invalid credentials.

**Compute or execute the reasoning.** For success, validate field names and types against a captured provider-compliant fixture. For timeout, assert the consumer does not assume the remote action was rolled back; a retry must use the documented idempotency key. For invalid credentials, assert no retry storm and an actionable rejection path without leaking the token to logs.

**Interpret the conclusion and limitations.** Run the same consumer expectations against a maintained provider sandbox or the official contract suite when available. A fake that always returns the expected schema merely demonstrates that the code works with the fake. Revisit the contract when the provider version changes; redact tokens and personal data from evidence.

