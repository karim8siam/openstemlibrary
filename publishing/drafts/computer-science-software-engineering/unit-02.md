# Software Engineering — Unit 2: System design

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for system design.

## 2.1 Architectural Styles

**Architectural Styles: conceptual explanation**

Architectural styles distribute responsibilities across components. A layered monolith has different deployment and communication tradeoffs from independently deployed services; smaller services can incur latency and operational coordination costs. Choose architecture from evidence about deployment, scale and team capability, not fashion.

### Engineering depth and worked reasoning

Architectural style determines the primary boundaries along which a system is changed and operated. A layered monolith, microservices, event-driven pipeline, and client-server application are not quality grades; each enables certain tradeoffs. Begin with business capabilities, critical invariants, transaction boundaries, and deployment constraints. A small university portal can benefit from one deployable application and a relational database because a distributed service architecture adds networking, versioning, observability, and failure coordination that may not buy useful independence.

Use quality-attribute scenarios to choose architecture. A scenario identifies stimulus source, environment, artifact, expected response, and measurable response target. For example, during peak registration, an instructor upload of fifty records must remain idempotent even when requests are retried. Derive component boundaries from these requirements. Separating the user-facing request handler from asynchronous notification delivery may protect consistency without introducing five independently deployed services.

In a poorly scoped microservice migration, each request to display an attendance record traverses identity, enrollment, timetable, attendance, and notification services. This creates extra tail latency and multiple points of failure; a shared database would further undermine service ownership. The remedy is not necessarily more caching. Consider data ownership, aggregation, retry budgets, and whether the proposed split solves a concrete organizational or scaling problem.

Draw two candidate deployments: one modular monolith and one event-driven decomposition. Trace authentication, a submitted correction, data persistence, and event publication. Count synchronous dependencies on the critical path and specify what the user sees when an email system is unavailable. Record a migration trigger that could justify the more complex design, such as independent release frequency or a demonstrated workload bottleneck rather than fashion.

### Investigation: choose boundaries by failure analysis
Compare a modular monolith with four services for a small lab scheduling platform. Draw the complete booking path with all synchronous calls. Assign hypothetical independent availability of 0.999 to each remote dependency and compute a naive all-required path probability for two and four dependencies; explicitly label independence and constant-rate assumptions as unrealistic. Consider a dependency that can be removed from the synchronous path by moving notification after a durable database commit. Compare operational complexity, runtime observability, and authorization boundaries, not merely the count of machines. Use simulated outages to reveal which design preserves the booking invariant. An architecture decision should state why the simpler system is adequate now and what measurable change could justify splitting it later.

### Model the transaction before the architecture diagram
Before drawing services, write down what cannot become inconsistent. For laboratory booking, overlapping confirmed allocations for a single device may be forbidden, while notification delivery can be delayed. This immediately suggests stronger consistency for reservation data and weaker coupling for email. A modular deployment with one transactional database may protect the booking invariant with fewer moving parts. Independently deployed services can improve team autonomy only if data ownership and failure handling are clear. Count required remote calls in critical journeys; then ask which of them can fail without changing the authoritative result. Monitor a service boundary by its user impact, not simply its request count. Record whether a proposed split offers a genuine deployment, scaling, or governance benefit. A useful architect can explain why complexity is justified and when it is unnecessary. Distinguish conceptual modules from deployment processes: one application can contain well-defined modules without becoming a single tangled codebase.

## 2.2 Component Interfaces

**Component Interfaces: conceptual explanation**

A component interface specifies inputs, outputs, failures and compatibility rules. A payment API must define whether repeated requests create duplicate charges and how clients recognize retries. Hidden side effects and undocumented ordering dependencies make components hard to replace.

### Engineering depth and worked reasoning

An interface contract defines what one component may assume about another. It includes operation names, input and output schemas, invariants, error classes, authentication scope, latency expectations, and compatibility rules. A function signature alone rarely captures the essential contract. For a `recordAttendance` operation, specify ownership of the submission token, accepted date formats, uniqueness rules, and the difference between a rejected request and an accepted asynchronous operation.

Develop interface contracts from examples first, then formalize them with a machine-readable schema when practical. Distinguish syntax validation from semantic validation: a student identifier can be a valid UUID yet refer to a learner who does not belong to the course. Define whether error responses reveal existence of protected records. Assign responsibility for retries and timeouts explicitly; two automatic retry loops at different layers can create an accidental request storm.

A client interprets HTTP 200 as “attendance was saved,” although the API returned only a queue acknowledgement. Under pressure, the queue fills and messages expire. The interface is technically well-typed but semantically misleading. Replace ambiguous status responses with a job identifier and explicit states, and document how clients confirm completion. Clients must not promise durability on the basis of an intermediate acknowledgement.

Construct a contract for `POST /sessions/{id}/attendance` and `GET /submissions/{token}`. Include at least one authorization failure, one transient service fault, one stale-record conflict, and one safe replay. Write consumer-driven contract tests for a mobile client and a dashboard. Change one field from optional to required and explain which consumers break, how to detect the break before release, and what transitional contract could preserve compatibility.

### Investigation: contract-level fault injection
Build a table of five requests to the attendance API: new authorized submission, exact retry, conflicting retry with the same token but different contents, unauthorized submission, and request made after the session closes. Specify status codes and structured error identifiers in a documented local design; do not imply there is only one universally correct code for every business rule. Mock an upstream timeout after a committed write, then observe whether the caller can retrieve the original outcome. Verify idempotency across application restarts and simultaneous callers rather than only sequential invocations. Document which component owns request identity, how long it must retain records, and whether that duration satisfies the product's retry expectations. A contract is useful when independently developed clients make the same interpretation.

### Define semantic status before serialized status
An API can return a syntactically valid response that is semantically false. Consider a queue acknowledgement presented as confirmation that a student was enrolled. The queue might accept the work but later reject enrollment because the section is full. The response contract must identify the stage reached: request received, request durably queued, reservation pending, reservation committed, or request rejected. Stable identifiers let clients query outcomes safely when a connection drops. Error messages should support recovery without leaking confidential facts about other users. Document idempotency-key scope and expiry as part of the contract because a retry from another device may arrive much later than expected. Authentication establishes caller identity but does not automatically authorize a particular record. Include permission checks in the operation’s semantics and tests. These decisions matter more than whether the API uses REST or a different transport.

## 2.3 Design Patterns

**Design Patterns: conceptual explanation**

Design patterns give names to recurring solutions such as Strategy for interchangeable behaviors or Observer for subscriptions. They are tools rather than default architecture: adding an abstraction without variability can increase cognitive load. Document the specific change the pattern enables.

### Engineering depth and worked reasoning

A design pattern names a recurring solution under particular forces; it is not a reason to introduce an abstraction. Strategy permits several interchangeable algorithms behind one contract, Adapter wraps an incompatible interface, Observer distributes change notifications, and Repository can isolate persistence-oriented decisions. The important questions are what variability actually exists, which coupling the pattern removes, and which new indirection it creates.

Suppose attendance eligibility differs among lectures, field laboratories, and examinations. A strategy interface can separate these policies while retaining a common decision result containing eligibility, explanation, and audit metadata. A large collection of subclass hierarchies may be worse than a simple configuration table if differences are data rather than behavior. Prefer the smallest representation that makes invalid states difficult to express.

A generic event bus added to a five-class program obscures control flow; every operation now requires tracing registration, dispatch order, and error handling. Conversely, embedding email delivery directly inside the attendance transaction couples a nonessential side effect to critical persistence. A narrow after-commit event is justified because it makes the notification failure independent without making basic domain behavior inscrutable.

Implement one domain operation in two designs: direct calls and a strategy or adapter abstraction. Introduce a new policy with a realistic change request and compare how many production lines and tests need modification. Document the extra concepts introduced by the pattern and show a failing case where incorrect dependency direction allows a low-level detail to leak into domain rules.

### Investigation: prove an abstraction earns its cost
Start with a single policy class that determines whether a student can borrow a laboratory instrument. Add a new rule requiring instructor supervision for dangerous equipment and a time window constraint for limited-use devices. Compare three implementations: conditional branches, a policy configuration table, and interchangeable strategy objects. Count the changes necessary for each and inspect whether business rules become easier to test. Define a result object that includes eligible status and a human-readable refusal reason. Inject one rule whose order matters, such as denying borrowed equipment after a safety lockout, and see whether each design makes precedence clear. Keep the simplest implementation whose behavior remains explicit; adding an interface for every branch is not automatically maintainability.

### Choose patterns by the change they enable
Design patterns are valuable when they give a name to a real variation and establish where decisions live. A policy strategy is defensible if multiple eligibility rules evolve independently, but it is not useful merely because the code contains an `if` statement. An adapter is appropriate when an external scheduling system uses incompatible data formats and the domain must not absorb its peculiarities. An observer or event consumer can decouple notification from a booking transaction while introducing asynchronous failure modes that need explicit handling. For each pattern, name the forcing change request, compare the smallest direct implementation, and count the new abstractions created. Prefer test cases that demonstrate replacement of one behavior without unexpected changes elsewhere. If a pattern causes developers to jump through six files to understand a simple rule, it may be imposing more cost than it saves. Abstraction is an engineering tradeoff, not an aesthetic reward.

## 2.4 Tradeoff Analysis

**Tradeoff Analysis: conceptual explanation**

Tradeoff analysis uses measurable constraints, alternatives and decision criteria. Faster asynchronous processing may reduce request latency but complicate consistency and monitoring. A useful architecture decision record states context, considered alternatives, chosen option and consequences, including a trigger for revisiting it.

### Engineering depth and worked reasoning

Architecture decisions are constrained optimizations rather than a search for a universally best diagram. Latency, complexity, consistency, autonomy, availability, cost, and migration effort interact. Recording explicit assumptions helps prevent later teams from treating an old choice as timeless. An architecture decision record should state context, candidate options, decision, rationale, expected consequences, and evidence that would cause reconsideration.

For a student portal expecting unpredictable registration bursts, compare vertical scaling with caching, a work queue, and independent read replicas. Model read and write proportions, burst duration, database connection limits, and operational staffing. Choose a design under defined constraints and validate it with realistic traffic. Avoid converting a synthetic throughput result into a claim of real scalability without measuring latency distribution and correctness at load.

An architect claims that the smallest number of components always means the lowest operational risk. A single module may still concentrate unrelated permissions and create dangerous blast radius; yet too many services multiply operational failure modes. Quality depends on boundaries and operational capabilities, not component count. Tradeoff analysis should expose what gets worse when another attribute improves.

Hold an architecture review in which participants advocate competing designs. Use a weighted decision matrix, but also record hard constraints that cannot be traded off, such as preserving audit evidence or meeting a legal accessibility obligation. Recalculate scores after changing the workload assumption. Show why a ranking can reverse and why decision makers should distrust fine-grained scores when their weights are subjective.

### Investigation: sensitivity of an architecture choice
Construct a decision matrix with three options: a single database application, an application plus asynchronous work queue, and five separately deployed services. Criteria include write consistency, build cost, operational staffing, component autonomy, and latency. State the meaning of every score and justify weight choices. Now change the assumed support capacity from one engineer to a staffed operations team, then increase notification workload while holding booking traffic constant. Recompute the matrix and inspect whether rankings shift. Identify hard constraints that weighted sums should not override, such as correct allocation of exclusive equipment. Finish with uncertainty intervals for any score based only on guesswork. The exercise should reveal why architecture analysis is a documented judgment, not an objective numerical formula.

### Compare alternatives against hard constraints
A weighted decision matrix can structure conversation, but its scores are judgments anchored to specific assumptions. For example, choose between synchronous calls, cached reads, and asynchronous events under a constraint that bookings cannot be double-confirmed. An option that violates the hard invariant is unacceptable even if it scores well on latency and maintenance cost. For the remaining candidates, estimate error recovery, number of required operator skills, release coordination burden, and effect on future features. Change one assumption, such as adding an operations team or expanding from one campus to fifty, and see how the preferred choice changes. Document evidence quality: a measured load test should carry more weight than untested intuition. Decision records should include consequences and a reconsideration trigger. They are not proof that the chosen architecture is optimal; they protect the rationale from being forgotten when conditions shift.

## 2.5 Integrated Engineering Studio: System design

An ecommerce application has catalog, checkout, inventory and payments. Splitting each capability into a separately deployed service creates network communication, version compatibility and failure handling that an in-process module avoids. Estimate which operations require atomicity and identify boundaries where eventual consistency is acceptable. Record a decision between a modular monolith and microservices using operational team size, deployment independence and latency evidence. If checkout calls payment twice after a timeout, an interface contract needs retry semantics rather than just a method signature. A pattern is justified only if it simplifies a real variation point.

### Studio case: architecture for a campus equipment booking service

A research laboratory manages microscopes, thermal cameras, and mechanical test rigs. Some devices require training certification and others can only be used when a supervisor is available. Existing spreadsheets allow double bookings and do not create useful audit trails. A proposed system must accept reservations, enforce conflicts, and send reminders. The first architectural decision is where transactional responsibility lives: if two users request the same exclusive device, only one reservation can become confirmed for the same interval.

A modular monolith with a relational database can enforce the booking invariant in a single transactional boundary. Separate modules can own inventory, authorization, reservations, and notifications without requiring separate deployment units. The notification module may run asynchronously: whether an email server is available should not change the truth of a successfully committed reservation. Define the outbox entry in the same transaction as the reservation if reliable downstream notification matters. A worker can dispatch outbox messages and retry them with a stable event identifier.

Model failure scenarios. Request A and B reach different application instances concurrently; the application-level “check availability” query in both sees an apparently free slot. A unique database rule or serializable transaction is still necessary to prevent a race. The response to the losing request must explain that the slot is no longer available. If a notification worker sends the same event twice, the consumer should either deduplicate or have a harmless idempotent effect. If an identity service is slow, a design relying on a synchronous check at every step needs an explicit timeout and security-preserving failure policy.

Compare this with a microservice design in which inventory, reservations, and scheduling live on separate databases. The system can gain organizational autonomy but may need reservations that remain pending while an asynchronous coordination process confirms capacity. Users now need to understand eventual states. Because the initial institution has a small operations team, this additional complexity may be unjustified. Record the assumption; a later sustained workload or independent team ownership could change the choice.

Create two diagrams and one decision record. The component diagram should show ownership of data and who calls whom. The sequence diagram should trace simultaneous reservations, a database conflict, outbox creation, notification retry, and a cancellation. The decision record must show why the selected design meets critical requirements, which quality attributes are weaker, and what evidence would motivate migration. Verify the scenario with a concurrency test rather than assuming the arrows guarantee correctness.

### Review of architecture evidence
The laboratory booking case has at least three separate claims to test: exclusive reservation allocation, resilience to notification failure, and appropriate protection of private user records. An architecture diagram alone cannot prove any of them. Build a concurrency fixture where two clients try to acquire the same device at the same time. Stop the notifier while preserving database availability and verify that confirmed bookings remain confirmed. Test denial of access by a student from another laboratory. Collect traces showing transaction, outbox event, consumer retry, and eventual notification status. An architecture decision record should identify where each claim is enforced and which component is authoritative. If a load test reveals latency, investigate the bottleneck before assuming the entire design requires microservices. A small safe optimization can outperform a broad redesign in both cost and risk.

# Fully worked questions

## Component coupling: complete graph versus real deployment

A diagram contains six software components. How many undirected component pairs are possible if every distinct pair could communicate? If only five interactions exist in the deployed system, why would treating the potential count as actual coupling be misleading?

**Analyze the assumptions.** The maximum number of unordered distinct pairs in a simple graph is n(n-1)/2. For six components this equals 6 times 5 divided by 2, or 15. This count assumes one possible undirected connection for each pair and no self-edges.

**Develop the result.** The five observed interactions represent a sparse dependency graph. Graph edge count alone still does not capture direction, strength, criticality, synchronous timing, data ownership, or resilience. One synchronous shared database dependency can be more consequential than several optional asynchronous event consumers.

**Check interpretation and failure cases.** Trace which edges participate in the critical booking transaction. Test a failure on a required edge and then on an optional notification edge. Compare how the user-visible outcome changes before deciding which boundary to refactor.

**Answer.** Fifteen potential pairs, five observed interactions. Meaningful coupling must be assessed from real dependency behavior.

## Synchronous dependency availability under simplifying assumptions

A request requires three remote dependencies, each independently available for 99.9 percent of a randomly sampled interval. Under this hypothetical independence assumption, estimate the probability all three are available. Why may production observations differ?

**Analyze the assumptions.** Translate 99.9 percent to probability 0.999. Under independence, the probability of intersection is 0.999 cubed, giving 0.997002999. As a percentage this is approximately 99.7003 percent.

**Develop the result.** This simple calculation assumes simultaneous independent events and an all-required path. Real components may share electricity, a network or identity service, so outages can be correlated. Retries, fallbacks and timeouts also change the relation between dependency availability and user-visible success.

**Check interpretation and failure cases.** Identify a dependency that can be removed from the request path without violating the key booking invariant. For example, persist notification intent with the booking and deliver an email asynchronously after committing the authoritative record.

**Answer.** About 99.7003% under the stated model; measure real request outcomes and common failure causes.

## Contract semantics when a queue acknowledges work

A reservation API returns success immediately after placing a message on a queue. The worker later rejects the reservation because capacity was exhausted. Explain why a client that displays “confirmed reservation” after the first response is incorrect, even when the JSON response schema is valid.

**Analyze the assumptions.** The queue acknowledgement establishes only that work was accepted for processing under the queue’s stated durability contract. It does not establish that reservation invariants were satisfied or that the database committed a confirmed record.

**Develop the result.** Define a response status such as pending and a stable operation identifier. Supply a follow-up read or callback contract with terminal states confirmed and rejected, plus timeouts and retry semantics. Document how long outcome records remain discoverable.

**Check interpretation and failure cases.** Test a delayed worker, a rejected booking, duplicate message delivery, and a worker restart. The user interface must distinguish uncertainty from final success and must not repeatedly allocate capacity when checking outcome status.

**Answer.** Use pending-state semantics and a durable outcome query; “accepted” is not equivalent to “confirmed”.

