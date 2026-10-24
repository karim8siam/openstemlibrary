# Unit 7: Distributed web architecture

## 7.1 Background Jobs

Background jobs separate work that must happen later from the immediate response path. Sending a certificate email, generating a PDF report, or recomputing a recommendation index may not need to block the student who triggered it. A web handler can validate the request, commit durable intent, and return a job identifier or status resource. A worker then performs the task, possibly after retries. This improves perceived responsiveness, but it introduces new states: queued, running, succeeded, failed, cancelled, and potentially unknown after a crash. The UI needs to communicate those states accurately.

A queue is not a guarantee that work executes exactly once. A worker might complete an external effect, crash before acknowledging the message, and receive the same job again. Idempotent job design associates a stable operation identifier with a durable outcome, so retrying does not create a duplicate invoice or certificate. Some effects cannot be undone easily, such as an email already delivered; for these, distinguish at-least-once attempt semantics from business-level deduplication and communicate uncertainty when necessary. Poison jobs require dead-letter handling or manual inspection instead of infinite hot-loop retries.

Job payload design influences security and reliability. Pass immutable identifiers and necessary version information instead of copying full sensitive database records into a queue without retention controls. Revalidate permissions and current resource state where the effect requires current authority. A staff member could lose export rights between scheduling and execution. Timeouts and leases prevent stuck workers from holding work indefinitely, but a lease expiration can allow overlapping attempts. Operations must tolerate that overlap or use effective coordination. Job cancellation may be best effort once an external side effect has begun.

Capacity planning starts with arrival rate, service time, worker concurrency, and backlog. If 30 reports arrive per minute and each worker completes one every ten seconds, one worker handles roughly six per minute; five workers only match average arrival, leaving little safety margin for bursts or retries. Monitoring queue age often reveals user pain more directly than queue length alone. Background processing improves scalability only when it is designed with persistence, operational visibility, and explicit failure semantics.

### Applied design, experiment, and interpretation

**Case analysis: transcript export queue.** Exporting five years of academic records can take several minutes. The request handler validates authority, writes a durable job record, and returns a job URL instead of blocking until completion. A worker processes the request under a constrained service account, storing the result in a private object with a short-lived access mechanism. When the requester loses permission before execution, the job should be cancelled or denied according to documented policy. A retry must not generate conflicting duplicate exports with unnecessarily long retention.

**Research exercise.** Measure queue arrival and service rates, then simulate a burst of one hundred exports. Record maximum queue age and worker utilization under failure retries. Kill a worker after writing the output but before acknowledgement; verify idempotent completion or safe artifact replacement. Ensure that logs and job payloads do not expose the exported records.

## 7.2 Messaging

Messaging lets services communicate through events or commands without requiring a synchronous HTTP call for every consequence. A message broker can buffer work, provide routing, and decouple producers from consumers. An event describes something that has happened, such as AssignmentSubmitted; a command requests an action, such as GenerateCertificate. Mixing those meanings makes ownership confusing. Events can have multiple interested consumers, while commands usually have a designated handler. The distinction is conceptual; the delivery guarantees depend on the broker and the application protocol.

At-least-once delivery is common, so duplicate handling is essential. A message needs a stable identifier, versioned schema, creation time, and sufficient context to process it safely. A consumer should make state changes conditional on whether the event has already been applied, ideally atomically with its own records. A producer writing to a database and a broker in two unrelated calls can create a gap: it may commit the data but fail to publish the event. The transactional outbox pattern records pending publication in the same database transaction as the domain change, then relays it asynchronously. This reduces loss but still requires duplicate-safe consumers.

Ordering is often partial, not global. Messages about the same student may need sequential processing, but achieving a single total order across all activity can impose heavy constraints. Partition keys, per-aggregate sequence numbers, and conflict-aware consumers can maintain necessary order without assuming a universal timeline. Schema evolution adds another concern: older consumers may still process messages after a producer adds new fields. Prefer additive changes and compatibility tests; changing the meaning of an existing field is usually more dangerous than adding a new optional one.

Operationally, monitor consumer lag, retry rates, poison-message counts, and effects on downstream services. A burst of enrollment events can overload a slow email provider even when the broker is healthy. Bounded concurrency and backoff prevent runaway retries. Sensitive payloads need access controls and retention limits because queues and dead-letter stores can become secondary copies of private information. Messaging is most useful when it clarifies ownership of domain effects and makes asynchronous failures manageable, not when it is adopted simply because a 'microservices architecture' sounds modern.

### Applied design, experiment, and interpretation

**Case analysis: attendance events and notifications.** A course application emits AttendanceMarked events consumed by analytics and notification services. The producer cannot assume that the two consumers run at the same speed. Store a stable event identifier and aggregate version, keep an outbox associated with the attendance transaction, and make each consumer duplicate tolerant. A late event should not overwrite a more recent attendance correction unless the consumer understands ordering. Notifications that have already been sent cannot be unsent, so a correction may require an additional event rather than a destructive rewrite of history.

**Research exercise.** Deliver the same event twice, reorder two updates, and drop an acknowledgement. Verify final analytical totals and notification behavior against an explicit policy. Check schema compatibility when a new optional attendance reason is added. Simulate a dead-letter queue and document what human intervention would resolve rather than infinitely retrying a permanently invalid event.

## 7.3 Realtime Updates

Realtime updates communicate server-side changes to an already open browser without requiring users to reload the page repeatedly. Polling makes periodic HTTP requests; long polling holds a request until an event or timeout; Server-Sent Events stream server-to-client updates over HTTP; WebSockets establish a bidirectional channel. The right choice depends on who needs to send information, expected message frequency, intermediary support, and recovery behavior. A course notification feed may work well with Server-Sent Events, while a collaborative whiteboard may need bidirectional low-latency messaging.

A realtime stream is not automatically a durable log. If a student loses connectivity on a bus, events may be missed unless the protocol supports replay or the client can fetch an authoritative snapshot. Design an event cursor or revision number and a reconnection strategy. The browser should reconcile streamed hints with server state rather than assuming that every event is exactly once and in perfect order. If a grade changes, the stream might tell the client to fetch the updated grade; the server still enforces authorization on that read. Never broadcast private data to everyone on the same connection channel merely because subscriptions are convenient.

Backpressure matters when producers outpace consumers. A fast simulation might emit hundreds of updates per second while a low-powered phone can render only a fraction. Coalesce intermediate states, bound buffers, and prioritize the latest useful snapshot where history is not essential. For an exam countdown, broadcasting every second from the server can be wasteful; sending a trusted deadline and reconciling against server time at key moments may be more efficient. Clock skew must still be handled, and the server remains the authority for submission deadlines.

Test reconnection, duplicated messages, out-of-order arrival, stale authorization, and page visibility transitions. Mobile browsers suspend background tabs and may close network connections unexpectedly. A design that succeeds only on an uninterrupted desktop connection is not reliable realtime software. Realtime features should degrade gracefully to refreshable state when the transport is blocked. Document whether the UI represents a confirmed authoritative update or merely an optimistic local estimate.

### Applied design, experiment, and interpretation

**Case analysis: live laboratory measurements.** Sensors stream temperature readings at twenty updates per second into a dashboard. If each browser renders every event while backgrounded, a slow device may accumulate a large queue and freeze after returning. The client can coalesce readings for display, while keeping authoritative historical samples on the server. A reconnect should request a snapshot or resume from a validated cursor. Alerts for dangerous values require clear delivery guarantees and should not rely only on an ephemeral browser WebSocket.

**Research exercise.** Disconnect the network for thirty seconds, reconnect, and compare the recovered plot with the server's recorded history. Inject out-of-order sequence numbers. Measure queue and memory growth under a producer rate higher than rendering capacity. Confirm that one student's private experiment data cannot appear in another student's subscription even if channel identifiers are guessable.

## 7.4 Scaling

Scaling a web service means maintaining desired latency and correctness as demand and data grow. Vertical scaling gives a process more resources; horizontal scaling adds instances and distributes work. A load balancer can spread requests, but stateless service instances only remain interchangeable if user state is held in a suitable shared system or encoded under an appropriate security design. In-memory sessions tied to one process can fail when subsequent requests reach another instance. Sticky sessions may temporarily mask that design, but they complicate failover and uneven load.

The bottleneck is often not the web server. Increasing application replicas can multiply database connections and overwhelm a shared database. A pool has a finite capacity; if every instance maintains fifty connections and twenty instances start, a small database may receive a thousand connections before doing useful work. Queueing and bounded concurrency can protect the database. Read replicas can offload suitable queries, but replication lag affects the freshness of results. Sharding distributes data across stores at the cost of cross-shard operations and more complex resharding. These costs should be justified by measured need.

A practical growth scenario is a university exam platform receiving fifty times normal traffic in the minute before a deadline. Caching stable question text can reduce read pressure, while submissions need durable authenticated writes. Pre-warming capacity, load testing, and isolating expensive analytics from the submission path can matter more than an elaborate distributed architecture. A queue may absorb post-submission processing, but it cannot replace acknowledgement of a durable answer when deadlines are strict. Define what counts as accepted before claiming that the system scaled correctly.

Evaluate scaling with throughput, p95 latency, errors, resource saturation, and cost per successful operation. Run controlled tests with realistic traffic mix and data sizes; a trivial health endpoint can scale differently from a transaction requiring indexes and locks. A cache hit rate under a warm synthetic test may not represent a deployment with cold keys. Scale only the bottleneck that evidence identifies, and preserve failure isolation and observability during the change. Scalability is the ability to maintain service quality under growth, not simply the number of containers visible in a dashboard.

### Applied design, experiment, and interpretation

**Case analysis: exam traffic at the deadline.** A university exam normally sees 100 requests per second but peaks at 5,000 near submission time. Adding fifty frontend instances may overwhelm a database that supports only a few hundred active connections. Use bounded connection pools and load-test actual submission transactions. Serve static instructions and assets from caches, but acknowledge a submitted answer only after durable acceptance. Expensive grading jobs can be queued after submission while preserving the deadline record. Emergency overload behavior must be defined before an exam begins.

**Research exercise.** Use a representative traffic mix of reads, autosaves, and final submissions. Report accepted writes, p95 response time, lock waits, errors, and recovery time after the burst. Compare scaling the frontend alone with reducing database work per submission. Verify that clients retrying after timeout do not create duplicate finalized attempts.

### Integrated laboratory: reliable asynchronous certificate generation

A university issues completion certificates after grading. The synchronous user action should record successful course completion and return an acknowledgement; generating a PDF, signing it, storing the artifact, and emailing a link can happen asynchronously. Define a durable status model that includes pending, processing, succeeded, and failed. The user-facing dashboard must not say 'certificate issued' until the durable artifact exists and is accessible under the intended authorization policy. A background worker should be able to resume work after a crash without silently losing requests.

Construct an outbox sequence. In one database transaction, save completion and a pending CertificateRequested event. A relay publishes the event, and a consumer generates the artifact. Because messages can be delivered more than once, use an idempotency key derived from the completion attempt and certificate version. A second attempt should return or verify the same outcome rather than creating two independently valid certificates. Define how a corrected grade produces a new certificate version and what happens to older public verification links. Distinguish an attempted email from a confirmed artifact creation.

Model capacity. Suppose 180 certificates arrive over one minute, while one worker can create three per second. One worker matches average arrival only under ideal conditions, without retry cost or bursts. Estimate the backlog under a worker outage and choose a concurrency limit that respects the PDF service and storage. Queue age is a particularly useful user-facing health measure. Add a dead-letter path for malformed certificate requests and provide an operator workflow that does not bypass authorization. Retrying forever at high speed merely amplifies a broken dependency.

Introduce real-time progress carefully. A browser may subscribe to Server-Sent Events for status changes, but loss of connectivity must not imply loss of the job. On reconnection, it should fetch the authoritative state, possibly using a revision cursor. Coalesce noisy progress events rather than flooding the client. Ensure subscriptions are authorized for the relevant student. A realtime stream is a delivery convenience; the database record is the persistent truth for completed certificates.

Finish with failure injection. Crash a worker before generation, after writing the artifact but before acknowledgement, and after publishing a success event but before marking the local record. Check idempotency and eventual convergence in each case. Measure duplicate delivery and out-of-order event handling. Write a short operations plan for monitoring backlog, failures, privacy, and storage retention. The result should be a dependable workflow justified by tests rather than by a claim that adding a message queue automatically makes software scalable.

### Synthesis: asynchronous work requires a durable definition of success

A queue, event stream, or realtime channel changes the timing of a workflow but does not erase its responsibilities. Jobs may retry; messages may duplicate or reorder; browser connections may drop; new web replicas may contend for the same database. The application must identify what is committed, what is merely requested, and what information can be reconstructed after failure. A student's certificate should not disappear because an email provider was unavailable, and duplicate completion events should not create multiple conflicting certificates. These are domain guarantees implemented through storage, idempotency, and carefully chosen communication patterns.

Compare three forms of state. An authoritative database record persists the outcome of a course completion. A message tells a worker that some consequence needs attention, possibly more than once. A realtime UI event informs the student's open tab that it may refresh its view. Treating all three as interchangeable causes lost effects and misleading displays. In a load test, watch both response latency and queue age; moving expensive work behind a broker can make requests faster while letting a backlog grow unnoticed. Scaling the web tier alone may increase pressure on a shared database. Reliability comes from measured capacity, failure isolation, and recoverable state transitions, not from the number of technologies in the architecture.

## Worked questions

### Calculate certificate queue capacity

A university receives 180 certificate generation jobs in one minute. One worker completes 3 jobs per second under an ideal fixed-time model. What is the average service capacity and what happens after a 20-second worker outage?

**Convert the rates.** Three jobs per second equals 180 per minute. Therefore, one worker exactly matches the stated average arrival rate when it runs continuously without retries, setup delays, or variance. Equality of average rates gives no capacity headroom for bursts or outages.

**Compute lost capacity.** A twenty-second outage removes capacity for 20 × 3 = 60 jobs. If arrivals continue at the same average rate, roughly sixty jobs accumulate. When the worker resumes at exactly the arrival rate, it cannot reduce the backlog, because new arrivals consume all of its nominal service capacity.

**Propose a recovery strategy.** To clear the backlog, the system needs temporary additional service capacity, reduced arrivals, or a longer completion horizon. Monitor queue age and failure retries, not merely the worker process's health. Make the generator idempotent and persist job state so a crash cannot permanently lose the certificates.

### Explain messaging duplicates

A database commits CourseCompleted, publishes an event, and a worker generates a certificate. The worker crashes after generation but before acknowledging the event. How can the system avoid generating duplicates on retry?

**Locate the uncertainty.** The broker may redeliver an unacknowledged message because it cannot know whether the external effect completed. The worker may already have written a certificate artifact. This is a normal consequence of at-least-once processing and cannot be fixed by assuming that each message arrives exactly once.

**Choose idempotency identity.** Associate a stable operation key with the course completion attempt and certificate version. On retry, the generator checks durable evidence of an existing successful result and returns or verifies it rather than creating a conflicting second certificate. This check and write must be coordinated under a concurrency-safe storage policy.

**Complete the failure path.** Use an outbox to reduce the risk of committing completion but losing the publication request. Track processing outcomes, retry bounded transient errors, and dead-letter permanent failures. An email may already have been sent even if acknowledgement fails, so distinguish notification attempts from the durable certificate record.

### Recover a realtime dashboard

A browser loses its live laboratory stream for 30 seconds while the server continues receiving readings. Explain why reconnecting to a WebSocket alone may not restore the full history.

**Distinguish live from durable data.** A WebSocket transports messages over an active connection. Once disconnected, an ordinary ephemeral stream does not necessarily retain the missing updates. Even if the connection reopens, previously emitted events may be gone or out of order. The browser needs a contract for authoritative state restoration.

**Specify resynchronization.** Maintain sequence identifiers or timestamps suitable for a durable cursor, and after reconnection fetch a current snapshot or replay missing history from a server-side store. Authenticate access to the stream and the history endpoint. Deduplicate by event identity and resolve ordering according to the model's documented guarantees.

**Handle rendering capacity.** If sensors send twenty updates per second and the browser can render five, coalesce intermediate visual updates while retaining necessary historical information on the server. Test background-tab suspension, connectivity loss, stale permissions, and rapid reconnections. Realtime communication is useful only when its recovery semantics match the educational task.

