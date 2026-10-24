# Database Systems — Unit 7: Distributed databases

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 7.1 Replication

**Core model — Replication**

Replication maintains multiple copies to improve availability, read scaling or resilience. Synchronous and asynchronous replication trade acknowledgement latency against possible lag.

**Original worked illustration**

If a leader acknowledges a write before a follower receives it, reading the follower immediately can return the previous value.

**Boundary conditions and checks**

Replication alone is not backup: deletion or corruption may propagate to every replica.

### Domain model and precise assumptions

Replication keeps multiple copies or representations of data available on different nodes, but it introduces questions about ordering, lag, failure and acknowledgment semantics. Primary–replica arrangements route writes through a primary and distribute reads to followers, while multi-leader designs have to confront conflicting concurrent writes. A replicated copy is not necessarily current. A read from a lagging follower may return an old balance or missing recently created record even though the primary acknowledged a successful write. Durability and availability improve only under specified failure assumptions and protocols.

### Worked field scenario

Suppose a primary commits enrollment E at 10:00:00 and its replica applies the change at 10:00:03. A user directed immediately to the replica at 10:00:01 may not see E. This is a read-after-write consistency problem, not necessarily a lost commit. Solutions include reading through the primary for a bounded period, waiting for a replication position, session routing or using a system that offers stronger read guarantees. The choice must consider latency, failover, replica load and the application requirement. It would be unsafe for a confirmation page to claim enrollment was never created simply because a stale replica lacked it.

### Counterexample and limits

Synchronous replication can wait for acknowledgments from other nodes before reporting success, but “synchronous” is not a magic guarantee of zero data loss under every disaster. Some protocols wait for reception, others for durable persistence or application. Asynchronous replication reduces normal write latency but can leave a divergence window after failover. Replication also faithfully propagates accidental deletes; it is not a replacement for historical backup or point-in-time restore.

### Investigation and self-check

Design a student registration service with a primary and two followers. State exactly which reads can tolerate a few seconds of lag and which need immediately consistent results. Draw a timeline of commit, replication and failover. Explain how the system handles a client whose write was acknowledged but whose next read is routed to a stale node. Propose a test that delays one replica and verifies the expected UI behavior.

### Engineering verification

Monitor replica delay, replication slot or log retention, follower replay errors and promotion procedures. Conduct failover rehearsals with concurrent writes. A health check that only pings TCP connectivity is not evidence that a node is current or able to serve the required consistency level.

## 7.2 Partitioning

**Core model — Partitioning**

Partitioning shards records across storage or nodes by key, range or hash. A good partition key balances load while supporting important queries.

**Original worked illustration**

Hashing user_id across four shards spreads uniformly distributed IDs approximately evenly; a query by exact user_id can route to one shard.

**Boundary conditions and checks**

A very popular key remains hot even under hashing; range scans can cross many shards and cause fan-out costs.

### Domain model and precise assumptions

Partitioning divides a logical data set into regions to reduce per-node storage and processing or to manage lifecycle policies. Range partitioning groups records by ordered values such as event date; hash partitioning distributes identifiers according to a deterministic hash; list partitioning groups declared categories. In a single database, partitions can be physical tables managed by one engine. In a distributed system, shards may live on different nodes with routing and rebalancing. These are related but distinct mechanisms. A partition key should reflect actual query patterns, growth and operational constraints.

### Worked field scenario

Consider an events table recording timestamp, student_id and event_type. Monthly range partitions can make retention and date-restricted queries easier if the engine can prune irrelevant months. A query lacking the date predicate may still scan many partitions. If events are also routed to shards by student ID, a report aggregating every student across all shards must communicate and merge partial results. A poor hash key, such as a small number of departments with uneven activity, creates hot shards despite multiple servers.

### Counterexample and limits

Changing the partition count or mapping requires migration and coordination; consistent hashing can reduce movement for some designs but does not eliminate rebalancing complexity. Cross-partition uniqueness and foreign keys may have engine-specific restrictions. Global secondary indexes can be expensive. Time-based partitioning also needs a policy for late-arriving data and clock corrections. The simplest partition strategy that meets measurable scale and maintenance needs is generally safer than speculative sharding.

### Investigation and self-check

Route student IDs 1 through 12 to three shards using `student_id mod 3` and tabulate where each goes. Increase to four shards and compute which IDs move under naïve modulo; explain why this is disruptive for a large data set. Next partition an event log by month and show which partitions a query for one week should need, assuming proper query predicates and engine pruning.

### Engineering verification

Record per-partition row counts, hot keys, scan counts and rebalance time. A “balanced” total row count can hide a hot partition receiving most writes. Require a rollback plan for routing changes, because the mapping itself becomes critical application state.

## 7.3 Distributed Transactions

**Core model — Distributed Transactions**

Distributed transactions must coordinate updates across participants. Two-phase commit can achieve atomic decisions but introduces blocking risks when coordinators fail.

**Original worked illustration**

A cross-shard transfer requires both debiting shard A and crediting shard B; a prepared participant should not unilaterally commit before the global decision.

**Boundary conditions and checks**

Two-phase commit is not a consensus protocol and does not solve availability under arbitrary network partitions by itself.

### Domain model and precise assumptions

A distributed transaction attempts to coordinate one logical operation across independently failing participants. Two-phase commit first asks participants to prepare, then communicates a commit or abort decision. It can produce atomic outcomes under specified assumptions, but may block when the coordinator fails and participants retain prepared state. It is not a universal reliability solution for arbitrary HTTP services. Modern workflows sometimes choose sagas: a chain of local transactions with compensating steps. Compensation is a new business action, not a literal reversal of time or guaranteed undo of an external effect.

### Worked field scenario

Suppose a reservation spans a room database and a payment service. A coordinator can make promises about two transactional databases that support a compatible protocol, but a card processor's payment API usually cannot be enlisted in the same SQL transaction. A practical saga may create a pending reservation, request payment using an idempotency key, confirm on success, and release the reservation on failure. A refund is not the same thing as the original payment never happening: fees, settlement delays and customer notifications may already exist.

### Counterexample and limits

Distributed consistency also depends on message delivery. A message may be delivered more than once after retries, so handlers should tolerate duplicates with durable IDs. The transactional outbox pattern stores the business change and an outgoing message record atomically in one database, then asynchronously publishes the message. Consumers still need deduplication or idempotent processing. This reduces a common gap where a database commit succeeds but an attempted message send fails.

### Investigation and self-check

Draw the states PENDING, PAID, CONFIRMED and CANCELLED for a booking saga. Label which transitions are local SQL commits and which depend on an external acknowledgment. Introduce a lost acknowledgment after payment succeeded and state how an idempotency key and status lookup prevent a second charge. Contrast this with the prepared/commit phases of two-phase commit and identify the blocking failure mode.

### Engineering verification

Test retries, duplicate messages, reordered callbacks and coordinator loss. Do not claim “exactly once” end-to-end processing without defining which event or effect is counted and the atomic boundary protecting it. Reconcile externally visible outcomes with internal state after fault injection.

## 7.4 Consistency Models

**Core model — Consistency Models**

Consistency models specify what order and freshness clients can rely on. Linearizability appears as if operations take effect atomically within real-time boundaries.

**Original worked illustration**

If a write completes before a read begins, a linearizable register must return that write or a later value, not an older one.

**Boundary conditions and checks**

Eventual consistency alone does not bound staleness. Product terms such as strong consistency need a precise formal interpretation.

### Domain model and precise assumptions

Consistency models describe what values reads may return relative to writes under concurrency and failures. Linearizability treats each completed operation as if it occurred at one instant between its call and response; serializability concerns transaction histories equivalent to some serial execution order. These are not the same property. Eventual consistency means replicas converge when updates stop and propagation succeeds, but by itself does not bound convergence time or guarantee session read-after-write behavior. A system can offer causal consistency, monotonic reads or bounded staleness according to its protocol. Statements like “distributed databases are eventually consistent” are much too broad.

### Worked field scenario

A replicated inventory service may display an outdated product count for a short period yet require every accepted purchase to obey a global stock invariant. That combination forces an architectural decision: writes to stock may need a single authoritative partition or coordination, while catalog descriptions may tolerate replica lag. Quorum arithmetic is often summarized as R+W>N for N replicas, but overlapping quorum sets alone do not guarantee linearizability. Version ordering, conflict resolution, membership changes and reads overlapping writes matter.

### Counterexample and limits

The CAP theorem concerns consistency and availability during network partitions under a particular formal model, not a slogan that engineers can choose exactly two of three vague virtues at all times. A system may reduce availability for operations requiring a consistent decision during a partition while continuing to serve cached read-only pages. Real design also involves latency, durability, recovery and application semantics. Describe the user-visible contract rather than branding the whole product with one consistency label.

### Investigation and self-check

For five replicas, test read quorum R=3 and write quorum W=3; show that any such sets intersect because 3+3>5. Then consider R=2, W=3, where equality does not ensure a common node. Explain why even an intersecting read may encounter old or concurrent versions without correct version-selection rules. Design separate consistency requirements for payment confirmation and a public article view counter.

### Engineering verification

Document guarantees with executable tests: write then read through a new session, concurrent writers, node isolation and replica recovery. Identify the specific interface and scope of each guarantee. Treat ambiguous “strong consistency” marketing claims as incomplete engineering requirements.

### Integrated unit case study

**Unit case study: global course registration with replica lag.**

A distributed registration service has one write primary and two regional followers. Students in different regions read the catalog from the nearest follower; the primary accepts enrollment writes. Suppose student S12 receives a successful enrollment confirmation, but the next page load is routed to a follower that is two seconds behind. The follower reports no matching enrollment. The application could accidentally tell the student to enroll again, creating a duplicate or frightening the user. Define a read-after-write strategy: temporarily route that student's confirmation and immediate status requests to the primary, wait for a replay position, or use a database feature with an explicit consistency guarantee. The acceptable choice depends on latency and availability requirements.

Now distribute write data into shards by student_id modulo three. If students 1–12 are evenly distributed, each shard receives four students. But the same count does not mean equal work: students from one institution may all take a heavily promoted exam at the same time, creating a hot shard. A domain-based partition may localize most queries but makes cross-domain reporting and rebalancing harder. Hash sharding can distribute steady-state volume more evenly in some workloads, but adding another shard under simple modulo remaps many keys. Routing metadata and migration rules become part of the system's correctness boundary.

Introduce a payment service for registration fees. Payment is external to the enrollment database, so a local SQL BEGIN does not roll the card network backward. Design a saga with a reservation hold, a payment intent carrying an idempotency key, a durable confirmation event and compensating release/refund paths. A delayed callback should be recognized as belonging to the original request, not treated as a new registration. Track reconciliation states and distinguish confirmed payment from merely submitted payment intent.

For a five-replica replicated record, quorum values R=3 and W=3 satisfy R+W>5; thus any fixed-size read and write quorums overlap. But that arithmetic alone does not guarantee that a read selects the latest version, that clocks are comparable or that write conflicts are resolved safely. A protocol must specify version ordering and membership changes. In a network partition, some operations may be unavailable if preserving a particular consistency guarantee is mandatory.

**Verification plan.** Delay one follower, partition another, and send concurrent enrollment requests. Assert database uniqueness for the business enrollment key, document which reads may be stale and measure how long stale reads persist. Run a safe promotion exercise and check that every acknowledged registration remains accounted for under the advertised durability promise. Keep backups because replication does not protect against accidental deletion replicated to every follower.

### Extended executable laboratory

**Extended laboratory: consistency under replica and network failure.**

Begin with a leader and two followers in a modeled replication system. The leader commits student enrollment E with revision 15, follower A has applied revision 15 and follower B remains at revision 14. Route a user to B immediately after the leader acknowledged the write. The follower may omit E; this is permitted under an asynchronous lag contract but violates an application promise of immediate read-after-write visibility. Choose a remedy such as primary read routing for recently written session data or waiting for a follower replay position. Define a timeout and an honest user message when the condition cannot be met.

Now model a replicated key with N=5 replicas. Enumerate read quorums of size 3 and write quorums of size 3; every pair overlaps. For R=2 and W=3, disjoint subsets can exist because their sizes sum to five, so overlap is not guaranteed. Explicitly distinguish this combinatorial property from complete linearizability: an overlapping node must also participate in a correct version and conflict-resolution protocol. Ask what happens if two clients write concurrently or membership is reconfigured during the operation.

Next route user identifiers 1–12 to three shards by modulo and count four IDs in each. Add a fourth shard and show the remapping. Distinguish key-count balance from request load; a few very active users can dominate one shard. Create a synthetic hotspot and compare per-shard throughput rather than claiming the modulo map ensures equal processing work.

Finally add an external payment provider. Duplicate callback delivery, timeout after success, and callback arrival after reservation expiry must all be simulated. Store a stable request identifier and a durable state machine, and reconcile inconsistent states. Two-phase commit is not a generic solution for providers lacking transactional prepare/commit interfaces. The lab report should state which components are modeled, which use actual database connections and which guarantees are only hypothetical until tested on a deployed cluster.

### Connections and deeper pitfalls

**Further investigation: availability and correctness during partial failure.** Network partitions may leave one region reachable by some users and unreachable by others. The application should explicitly classify operations by consistency needs: viewing a public syllabus might tolerate cached data while issuing a unique certificate, allocating a scarce seat or changing a financial balance may need stronger coordination. A single global consistency label is not detailed enough to design user workflows. Identify what the interface promises about read freshness, write acknowledgment and retry behavior.

A follower that responds quickly is not necessarily healthy for a freshness-sensitive task. Health checks should assess replay progress, acceptable lag and role suitability. Promotion of a lagging follower can lose recently acknowledged asynchronous writes under some configurations. A failover plan must specify whether the system prioritizes continuous write availability or avoiding loss of acknowledged state in each scenario. This is an engineering contract, not a matter of using an impressive database brand.

Distributed transactions add the possibility of partially completed external effects. A well-designed saga state machine makes each transition and compensating action visible and retryable, with durable identifiers. If a payment settled while reservation confirmation failed, the system must reconcile and potentially refund; pretending the original operation never occurred would be misleading. Monitor the age of unresolved saga states. “Exactly once” claims should describe a scoped effect, such as one committed enrollment per request ID, rather than an unspecified guarantee over every message and service.

## Three worked questions

### Problem 1: Replication: worked verification
A follower replica lags a leader by one committed write. What can an immediate follower read return?

**Set up the model and conditions**
Asynchronous replication may acknowledge a write before the follower receives it.

**Carry out the calculation or proof**
A read routed to that follower can observe the previous value.

**State the result and its scope**
The read may be stale unless the consistency mechanism prevents this.

**Detailed reasoning and validation.** With asynchronous replication, primary acknowledgment may precede follower replay. If the primary has committed state version v11 while the follower remains at v10, a read from the follower can return v10. That behavior is stale but consistent with the stated asynchronous lag. A session that requires read-after-write can route to the primary, wait for a replay position, or use a protocol with a stronger guarantee. If the user receives a “record missing” error after a successful registration, blindly resubmitting could create duplicates unless the database also enforces an idempotent business key. Monitor the replica's replay progress before advertising a freshness promise.

**Answer:** The read may be stale unless the consistency mechanism prevents this.

### Problem 2: Partitioning: worked verification
For N=5 replicas with read quorum R=3 and write quorum W=3, do quorums necessarily intersect?

**Set up the model and conditions**
Compute R+W=3+3=6.

**Carry out the calculation or proof**
Since 6>5, any read set and write set of these sizes overlap at least one replica.

**State the result and its scope**
Yes, quorums intersect; this alone does not solve stale-version or failure handling.

**Detailed reasoning and validation.** For N=5, R=3 and W=3, the sum of the quorum sizes is six, greater than five. Two subsets of a five-element set with sizes three and three cannot be disjoint, because disjoint subsets would require six distinct nodes. Hence every such pair intersects at least once. The intersection claim is combinatorial; it does not specify which version the shared replica holds, how concurrent writes are ordered, or what happens when membership changes. Correct quorum protocols add version or consensus rules. The exercise demonstrates necessary overlap for one family of designs, not a complete proof of linearizable storage.

**Answer:** Yes, quorums intersect; this alone does not solve stale-version or failure handling.

### Problem 3: Distributed Transactions: worked verification
Explain a blocking risk of two-phase commit when a coordinator fails after participants prepare.

**Set up the model and conditions**
Participants have voted ready and may hold resources awaiting commit/abort decision.

**Carry out the calculation or proof**
If the coordinator's decision is unavailable, they cannot always safely choose one unilaterally.

**State the result and its scope**
Prepared participants may block until a durable decision is recovered.

**Detailed reasoning and validation.** During the prepare phase of two-phase commit, participants may have logged a prepared state and retained locks while awaiting a final decision. If the coordinator fails before its durable commit/abort decision becomes available, those participants cannot simply decide on their own without risking disagreement. They may remain blocked until the coordinator or recovery mechanism resolves the outcome. The approach addresses atomic agreement under stated assumptions but can harm availability during failures. A saga uses local commits and compensating steps instead; compensation does not retroactively erase external effects such as a notification or payment processing fee.

**Answer:** Prepared participants may block until a durable decision is recovered.
