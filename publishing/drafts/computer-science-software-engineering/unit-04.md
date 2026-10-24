# Software Engineering — Unit 4: Modeling and documentation

*Draft instructional manuscript. Not independently peer reviewed.*

Original engineering case studies, failure analysis, design exercises, and locally testable simulations for modeling and documentation.

## 4.1 Domain Models

**Domain Models: conceptual explanation**

A domain model represents meaningful concepts, associations and invariants. An order is not merely a database row; its lifecycle may forbid shipping before payment authorization. Modeling invariants explicitly helps locate the code that must enforce them under concurrent changes.

### Engineering depth and worked reasoning

A domain model represents the vocabulary and invariants of the problem space rather than mirroring database tables. Entities have identities across time, value objects express interchangeable descriptive values, and aggregates protect consistency rules within a transaction boundary. In an attendance domain, Student, CourseSession, Enrollment, and AttendanceDecision are different concepts. A student can attend several sessions; one session can be corrected; an enrollment can end without erasing all historical decisions.

Write invariant statements that can become executable tests. For example, a recorded decision belongs to an existing scheduled session; the issuing instructor has permission for that session; corrections retain audit provenance; and duplicate request tokens do not create duplicate decisions. Distinguish invariants that must hold immediately from eventual consistency conditions, such as a notification being delivered after a record changes.

A database design stores attendance as a mutable Boolean column in a student row. It cannot represent which class was attended, the time or reason for correction, or contradictory evidence. The issue is not normalization alone: the domain language is wrong. Model attendance as a decision or event attached to a session and authorized actor, with an explicit state transition and history.

Build a minimal domain model for equipment loans. Identify entities, values, commands, and events. Draw aggregate boundaries so that two concurrent reservations cannot both allocate the same exclusive item without detection. Define rules for maintenance lockout, borrower eligibility, and return inspection. Use examples to reveal whether “available” means physically present, administratively cleared, or both.

### Investigation: enforce invariants in concurrency
Model exclusive equipment allocation as a domain invariant: overlapping confirmed reservations for the same device are forbidden. Write an example where two transactions both check availability before either commits, then both attempt allocation. Describe a database-level exclusion constraint or transactional locking mechanism that closes the race, and state the portability limitations of a particular implementation. Compare this with a purely application-level check, which is insufficient when multiple application instances exist. Add an audit record for staff overrides and distinguish a safety lockout from an ordinary booking. The exercise tests whether a domain model survives real concurrency rather than merely looking elegant on a whiteboard.

### Domain boundaries follow independent reasons to change
When creating a domain model, use concrete questions to identify entities and values. Does this object have persistent identity? Can two records share its descriptive attributes but represent different real-world things? Which rules must be true after every successful transaction? A reservation identifier and reservation time interval serve different roles: the identifier persists even if time changes, while the interval may be a value object with comparison rules. If a supervisor revokes permission, which existing reservations remain valid and how is that decision recorded? Define aggregate boundaries around required atomic invariants rather than around visual modules. Excessively large aggregates cause unnecessary lock contention, while excessively small boundaries can make core rules impossible to enforce consistently. A correct model also represents uncertainty explicitly. “Unknown attendance” should not be silently converted into absence merely to make a database column non-null.

## 4.2 Behavioral Models

**Behavioral Models: conceptual explanation**

Behavioral models represent allowed transitions and interactions over time. A state machine can prohibit refunding an uncaptured payment, while a sequence diagram can show retries and asynchronous notifications. Use models to reveal impossible transitions rather than decorate documentation.

### Engineering depth and worked reasoning

Behavioral models describe how systems change state as events occur. A state machine can make invalid transitions explicit; a sequence diagram can reveal synchronous dependencies; an activity model can uncover branches and concurrency. Choose a model for the question at hand rather than producing diagrams for their own sake. For a support ticket, states may include received, triaged, assigned, awaiting customer, resolved, and reopened.

Specify transitions with guards and effects. A laboratory instrument reservation moves from requested to confirmed only when authorization and capacity checks pass. A cancellation after an equipment handover may require a return workflow instead of pretending the reservation never existed. Record timeout behavior and compensating actions for distributed processes. State machines clarify what a retry should do when the state has already advanced.

A team documents only the normal payment sequence and overlooks a timeout after a provider charges the card but before the application receives confirmation. A naive retry could charge again. Model uncertain outcomes, establish idempotency keys, and use reconciliation with the provider before changing customer-facing status. The value of the diagram is exposing ambiguity, not the visual neatness of the arrows.

Draw both a state machine and a message sequence for a research-equipment booking service. Include an authorization rejection, concurrent booking conflict, cancellation, delayed notification, and recovery after a restart. Identify where an event log is authoritative and where a cached view may lag. Explain how the models reveal different classes of errors.

### Investigation: state-machine coverage
Draw states for a submitted grant application: draft, submitted, under review, clarification requested, awarded, declined, and withdrawn. Enumerate transitions and their authorized actors. A request for clarification must preserve original submission time and the history of requested edits. Test invalid transitions: awarding a draft, editing a withdrawn record, and withdrawing after a legally binding acceptance stage. Add a timer event for an unattended clarification request. Create a transition table in which every row has current state, event, guard, side effect, and resulting state. Use the table to generate test cases, then compare its coverage against a screenshot of the normal workflow. The state diagram should make missing error behavior visible.

### Behavioral models reveal time-related failures
Static domain relationships do not reveal all temporal conditions. A state machine makes legal transitions explicit, while a sequence trace shows order, messages, timeouts, and retry responsibilities. Model delayed work as delayed rather than silently assuming eventual success. A pending grant application cannot be called approved because a review message was queued. Use guard conditions to define who may trigger each transition and whether it remains valid after a concurrent change. Timeouts deserve special attention: if a client does not hear a response, the underlying operation might nevertheless have committed. Design retry paths around operation identity and authoritative outcome queries. A useful behavioral test triggers a timeout at the most awkward point, between irreversible effect and response delivery. Make recovery observable to the user instead of hiding inconsistency behind a spinner.

## 4.3 Api Contracts

**Api Contracts: conceptual explanation**

An API contract specifies request schema, response schema, status codes, authentication and versioning. A syntactically valid response may still violate semantics, such as returning stale inventory as confirmed stock. Consumer-driven tests can detect some incompatibilities but need stable assumptions about clients.

### Engineering depth and worked reasoning

An API contract is an agreement across independently changing components. OpenAPI schemas can document request shape, response status, and examples, but cannot by themselves guarantee authorization, business semantics, or temporal ordering. A stable API describes resource identity, error categories, pagination, concurrency control, idempotency, and version evolution. Consumers need explicit guarantees about which changes are compatible.

For a list endpoint, make filtering and pagination deterministic under concurrent inserts; a cursor may be safer than a mutable offset for rapidly changing datasets. Use conditional requests or revision numbers for update conflicts. Treat timestamps as timezone-aware instants and define how local civil times are represented. Standardize machine-readable error identifiers without exposing internal stack traces or confidential identifiers.

A vendor adds a new enum value for a laboratory state, assuming additive changes are always backward compatible. Older clients parse enums exhaustively and crash. Robust consumers should handle unknown values where semantically safe, while providers must publish an evolution policy and test realistic clients. Compatibility is about behavior, not only schema shape.

Design a versioned reservation API and three consumer scenarios: interactive mobile client, offline-capable kiosk, and nightly audit exporter. Specify contracts for conflict, retry, partial batch failure, and permission revocation. Build request/response examples that are valid and invalid. Demonstrate one breaking change and a compatibility strategy supported by tests.

### Investigation: API evolution under mixed clients
A new version of a reservation API changes `startTime` from a local clock string to an ISO timestamp with offset and renames `device` to `equipmentId`. Produce three sample requests and the expected behavior of old mobile clients, new browsers, and an export worker. Design a transitional representation or versioned contract rather than changing server and all clients at once. Include requests that contain both fields with conflicting values and specify how the server responds. Test cursor pagination under an insertion made between page requests. State which errors reveal authorization problems without disclosing whether a confidential reservation exists. The analysis should be about consumer behavior over time, not only JSON validity.

### API stability concerns meaning as well as shape
Compatibility decisions must specify whether clients may ignore unexpected fields, what happens when new enum values appear, and how to interpret missing, null, or empty values. Some consumers can tolerate a new optional field but fail on a new enum because they use exhaustive matching. Dates and durations require explicit units and timezone semantics; two JSON numbers may have identical serialization while representing milliseconds and seconds. Each endpoint should document authorization, pagination, idempotency, concurrency control, and stable error meaning. Contract tests should exercise at least one old supported consumer against a candidate server. Versioning is not a universal substitute for migration: if a database model changes underneath two API versions, both must remain coherent until the support window ends. Rollback planning needs to account for stored data created by the newer version.

## 4.4 Technical Documentation

**Technical Documentation: conceptual explanation**

Technical documentation serves different audiences: an operator needs recovery instructions, a developer needs build steps and an integrator needs protocol contracts. Examples should be executable and checked against actual behavior. A document with perfect formatting but obsolete commands is more dangerous than a short verified guide.

### Engineering depth and worked reasoning

Technical documentation is an operational part of the product, not a decorative afterthought. Different readers require different artifacts: a quick-start explains a successful first task; a reference specifies exact behavior; a tutorial develops mental models; a runbook tells responders how to act under failure; an architecture decision record explains why a costly tradeoff exists. Mixing these genres makes documentation long without making it useful.

Document executable examples alongside the code that implements them. Check commands, paths, data schemas, and error responses in CI wherever possible. Include version ranges, prerequisites, safe sample credentials, and how to remove trial data. Explicitly mark irreversible procedures and their preconditions. Maintain a separate change history for external consumer-visible behavior rather than assuming readers inspect Git commits.

During an outage, a support engineer follows a runbook that says “restart the queue” without specifying its effects. The operation discards unacknowledged messages, causing data loss. A useful runbook identifies observable symptoms, diagnostic commands, safe steps, rollback, escalation, and verification that the original user-facing invariant still holds. Rehearsed operational documentation is a reliability control.

Write a developer quick-start and a production incident runbook for the same application. Ask a new teammate to complete setup without oral explanation and record every missing step. In the runbook, distinguish harmless observation from actions that alter state. Add a “last tested on” record and a scheduled documentation test, then identify which statements must be updated after changing deployment infrastructure.

### Investigation: operational documentation that prevents harm
Write a first-run developer guide for the booking project, including prerequisites, local test data, commands, and the expected successful response. Then write an incident runbook for “confirmed reservation absent from user screen.” Begin with read-only diagnostics and avoid recommending irreversible actions until the failure mode is known. Include a check of database state versus cached views, authorization, and delayed event processing. Specify who can approve data correction. Give a teammate the guide without oral explanation and record every ambiguity. Check that command examples do not contain live credentials and that deleting local trial records cannot affect production. Documentation should demonstrate reproducibility and safe operator behavior.

### Treat documentation as an executable interface
Documentation can fail in the same way as code: stale setup steps make development unreproducible, invalid API examples teach broken contracts, and ambiguous runbooks produce unsafe operator actions. Write examples with explicit versions and verify them in automation where feasible. Distinguish tutorials that develop understanding from references that specify exact options and runbooks that direct incident response. A runbook should begin with observation and safe diagnosis before state-changing commands, and should include a stop condition if the system behaves unexpectedly. For a destructive migration or retention task, identify authorization and recovery prerequisites. Use feedback from a new user who cannot ask the author for help to discover hidden assumptions. Good documentation reduces dependence on individual memory and acts as a real interface between developers, operators, and users.

## 4.5 Integrated Engineering Studio: Modeling and documentation

An order system has states Draft, Authorized, Fulfilled, Cancelled and Refunded. The product manager initially asks for “refund order” as a single button. Model legal transitions: refunding a fulfilled charge requires settlement handling, while canceling an unpaid draft has different semantics. Produce a state table with transition, precondition, side effect and failure response. Derive an API contract that is idempotent under repeated requests. An implementation should reject attempts to fulfill a cancelled order even if a stale client still displays an enabled Fulfill button. Update operator documentation to describe reconciliation after asynchronous payment events.

### Studio case: modeling a research laboratory booking domain

A laboratory currently treats any appointment marked on a shared calendar as a confirmed reservation. However, devices can be unavailable during maintenance, students may lack training, and a supervisor must sometimes approve use. A single Boolean “booked” field cannot preserve these distinctions. Start by interviewing operations staff and write the ubiquitous-language glossary: request, allocation, confirmation, cancellation, handover, return, maintenance lockout, authorization, and capacity.

Define a reservation aggregate with identity, user, equipment, interval, and current status, while a separate inventory model records whether an item is safe to use. Proposed states include requested, awaiting-supervisor, confirmed, active, completed, rejected, and cancelled. Some transitions depend on permission and available equipment; a return cannot be recorded for a device never handed over. A cancellation after the equipment became active should initiate a controlled return process instead of silently erasing audit history. State invariants with unambiguous words before implementing validators.

The API offers `POST /reservations` with a caller-supplied idempotency token. The response distinguishes confirmed from pending approval. A conditional update requires the current reservation revision, so stale clients do not silently overwrite supervisor decisions. The mobile client displays the current state with human-readable alternatives, while an audit exporter sees a stable history. A notification event carries a reservation identifier and revision rather than embedding confidential personal data that every consumer would otherwise receive.

Use two diagrams for different questions. A state machine should reject impossible transitions, including cancellation of completed reservations without a separate correction record. A sequence diagram should show user request, authorization check, database conflict detection, outbox write, and asynchronous email handling. Inject a timeout after the database transaction commits but before the response reaches the client. The client retries with the same idempotency token and should receive the original result. An error status alone is insufficient to establish whether the reservation exists.

Provide machine-readable valid and invalid payload examples. Document what the user can rely on, how clients detect a stale revision, and how errors are explained without leaking another student’s reservation details. A design review should uncover that updating a supervisor approval policy affects domain transitions, API status expectations, user-interface labels, and the operational runbook. Good models reduce ambiguity across all of these representations; they do not replace working tests.

### Review of modeling consistency
Check that the domain, state machine, API, and documentation assign the same meaning to pending and confirmed reservations. If the diagram says confirmation requires a supervisor yet the API returns confirmed immediately, the models contradict one another. Construct an integration test that exercises the authoritative transition after supervisor approval, and verify that the UI changes state only on that event. Review what happens when an email is delayed or a mobile app is offline. A good model preserves meaning across time and components, including recovery from a missed message. Ask the owner to justify which facts must be strongly consistent and which may be eventually visible. These are operational semantics, not aesthetic choices about the names on arrows.

# Fully worked questions

## Concurrent equipment allocation invariant

Two clients each read the last available device and attempt a booking. Under a read-then-write sequence without isolation, both may obtain “available.” Explain the race and how a database-enforced invariant changes the outcome.

**Analyze the assumptions.** The requests interleave: client A reads available, client B reads available, client A writes confirmed, client B writes confirmed. Both reads were individually correct at their times, but the combined result violates exclusive allocation.

**Develop the result.** Use an appropriate database constraint, lock, or serializable transaction to make the critical check and update atomic. The losing transaction should receive an explicit conflict that the application can translate to a safe user message.

**Check interpretation and failure cases.** Test with controlled concurrent transactions, not only sequential simulated users. The exact SQL approach depends on the database; specify interval-overlap semantics and maintenance lockout in the invariant before implementation.

**Answer.** The booking invariant must be enforced at a concurrency-safe authority; two success responses are invalid.

## State transitions and invalid actions

A reservation has states requested, confirmed, active, completed, and cancelled. A student sends a cancellation command while the device is already active. Why should the system not simply set the state to cancelled?

**Analyze the assumptions.** The active state means equipment was handed over and may need physical return, safety inspection, or inventory reconciliation. Switching directly to cancelled would erase an operational obligation and misrepresent the physical state.

**Develop the result.** Specify a transition guard: direct cancellation is allowed only from requested or confirmed states before handover. After activation, a return or early-termination process records how the device was recovered and who accepted it.

**Check interpretation and failure cases.** Add a negative transition test from active to cancelled and a positive test that follows active to completed with return evidence. Record status history so a correction does not silently overwrite the fact that equipment was used.

**Answer.** Reject direct cancellation after handover; require a return workflow with an auditable transition.

## Compatible API evolution beyond JSON validity

An API changes a duration field from seconds to milliseconds without renaming it. Both versions still send a JSON number. Explain the failure and design a migration that permits old and new clients to operate.

**Analyze the assumptions.** A schema validator that only requires a number cannot detect changed units. Old clients interpret a one-minute duration of 60,000 as 60,000 seconds; they may set wildly incorrect timeouts or deadlines.

**Develop the result.** Introduce a new explicitly named field such as durationMs, retain the old durationSeconds temporarily, and document precedence if both are supplied. Alternatively version the endpoint with clearly defined semantics.

**Check interpretation and failure cases.** Write consumer tests for an old client and a new client. Instrument version usage, communicate a deprecation window, and remove old behavior only after supported consumers have migrated. Conversion should be checked at boundaries rather than inferred from magnitude.

**Answer.** Field meaning is part of the contract; changing units silently is breaking even if the serialized type does not change.

