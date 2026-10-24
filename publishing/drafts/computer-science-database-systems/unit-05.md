# Database Systems — Unit 5: Transactions

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 5.1 Atomicity

**Core model — Atomicity**

Atomicity means a transaction's state changes are all-or-nothing, even if execution fails. Transaction boundaries should enclose a coherent business invariant.

**Original worked illustration**

Transferring 50 between accounts requires debiting one and crediting the other within one transaction; committing only one side violates the invariant.

**Boundary conditions and checks**

Atomicity does not by itself establish isolation from concurrent transactions or durability across physical failure.

### Domain model and precise assumptions

Atomicity means that a transaction's changes become visible as one committed outcome, or are abandoned without a partial committed effect. It does not mean the transaction executes instantly, that external messages can be rolled back, or that application logic cannot fail after a commit. In a transfer between two internal account balances, deducting an amount from one account and adding it to the other must be enclosed in one transaction, along with an invariant check that forbids an invalid negative balance when the business rules require it. If the first UPDATE commits before the second executes, a crash can leave a permanent imbalance. The unit of work must reflect the domain's smallest consistent operation.

### Worked field scenario

Suppose account A has 140 units, account B has 60 units, and a transfer moves 35 units. Correct final balances are 105 and 95, with total 200 preserved. Within one database transaction, updating A then B and committing yields this result. If the second update fails, a rollback returns both to the initial values. This toy example does not establish how a payment moves between independent financial institutions: an external network request and a local SQL transaction are not one atomic transaction unless a special coordination protocol is involved. An application normally uses event and reconciliation patterns for external side effects.

### Counterexample and limits

Savepoints allow a portion of a larger transaction's work to be undone, but their exact behavior depends on the engine. A retry of an entire transaction after a timeout must be safe against duplicate effects. An idempotency key stored with a uniqueness constraint can protect operations against repeated client requests, provided the key is checked in the same effective transaction as the operation. A retry system should distinguish definitely rolled-back work from a commit whose acknowledgment was lost. “I saw an error” does not always imply “the database did not commit.”

### Investigation and self-check

Design a transfer endpoint using a durable request ID, validated positive amount and two account records. Trace the normal path, insufficient-funds failure, constraint rejection and connection loss after COMMIT was sent. Specify how the client can look up the request's outcome before retrying. Do not put a third-party HTTP payment call in the middle of a local transaction and assume the remote system will roll back.

### Engineering verification

Run a failure-injection test after each statement and before acknowledging success. Reconnect and verify the sum of balances and the uniqueness of the transfer ID. Ensure the application does not swallow a partial error and incorrectly send an acknowledgment while the transaction is still open.

## 5.2 Isolation

**Core model — Isolation**

Isolation governs which effects concurrent transactions can observe. Serializability matches some serial order, while common weaker levels permit additional anomalies.

**Original worked illustration**

Two transactions each reading total reserved seats and then inserting a reservation can violate capacity under snapshot isolation if their writes do not conflict directly.

**Boundary conditions and checks**

Database product labels for isolation levels do not always match identical implementation details; reproduce anomalies before assuming safety.

### Domain model and precise assumptions

Isolation controls which concurrent changes a transaction may observe and which anomalies the system prevents. Common teaching anomalies include dirty reads, nonrepeatable reads, phantoms, lost updates and write skew. SQL-standard isolation-level names describe broad guarantees, but actual implementations vary. For example, PostgreSQL uses multiversion concurrency control, and its Repeatable Read has stronger properties than a minimal SQL-standard description in some respects. A developer must document the chosen engine and version. A snapshot is a logical visibility rule, not a lock on every row seen by a query.

### Worked field scenario

Consider two doctors who may go off duty only if another doctor remains on duty. Both transactions read the same snapshot showing doctors A and B on duty. T1 sets A off duty and T2 sets B off duty, writing different rows. Under snapshot-isolation behavior that allows both commits, each saw a valid precondition yet the committed result violates the cross-row invariant. That is write skew, not a classic lost update on the same row. A serializable mode that detects the conflict may abort one transaction; the application must handle serialization retries, and the predicate must be represented correctly.

### Counterexample and limits

Read Committed may provide a fresh snapshot per statement and can show different values in successive statements. Repeatable Read often fixes a transaction snapshot, but guarantees are engine-specific. Serializable execution is intended to give results equivalent to some serial ordering, not to prevent every wait or abort. A proper workload design includes short transactions, bounded retries and an awareness that locks, contention and deadlocks can reduce throughput.

### Investigation and self-check

Create two connections and a schedule table with columns time, T1 action, T2 action and visible values. Demonstrate a nonrepeatable read in an implementation that permits it. Then construct the on-call doctors example and compare the possible outcomes under two isolation modes in your chosen engine. Explain why merely wrapping each UPDATE in a transaction does not automatically protect a multi-row invariant.

### Engineering verification

Test isolation with true concurrent sessions; a single sequential test never establishes the guarantee. Read authoritative documentation for the exact database version. Record serialization errors and retry outcomes without assuming that a failed transaction can safely resume at an arbitrary intermediate statement.

## 5.3 Concurrency Control

**Core model — Concurrency Control**

Concurrency control coordinates locks, timestamps or multiversion snapshots. Two-phase locking can enforce conflict-serializable schedules when implemented correctly.

**Original worked illustration**

If T1 holds an exclusive lock on row A, a conflicting T2 update waits until lock release or abort rather than overwriting blindly.

**Boundary conditions and checks**

Predicate and range anomalies need more than row-level locks; phantom protection depends on locking protocol and access paths.

### Domain model and precise assumptions

Concurrency control coordinates operations that may conflict while keeping useful parallelism. Two-phase locking acquires locks and avoids releasing them until an appropriate phase, making some schedules conflict-serializable when the protocol is followed. Multiversion systems keep several visible versions to reduce read/write interference. Optimistic control validates that the data read has not changed before accepting an update. The right approach depends on contention, the scope of the invariant and acceptable conflict retries. A mutex in one application process cannot protect the database from another process that bypasses it.

### Worked field scenario

Suppose a ticket inventory row has remaining=1. Two clients each read 1 and then write 0. Both can claim success without a protected predicate. An atomic conditional update `UPDATE ticket_inventory SET remaining=remaining-1 WHERE id=? AND remaining>0` followed by checking the affected-row count can protect a single-row stock constraint in engines with appropriate atomic statement semantics. For multi-row seat allocation or coordinated resource pools, the invariant may require explicit row locks, serializable mode or a carefully designed ledger. Lock scope and update order should be documented.

### Counterexample and limits

Optimistic version checking stores a monotonically increasing version number and writes only if the expected version still matches. A rejected update may be a normal concurrent edit rather than a system failure. Pessimistic locking reduces retries but can lead to waits and deadlocks. The cost model includes contention duration, lock granularity, validation overhead and time spent holding connections. There is no universally fastest concurrency protocol.

### Investigation and self-check

Design a two-client experiment for a shared counter using plain read-then-write, conditional SQL update and version-column compare-and-swap. For each, list the permitted final counters after two successful acknowledgments. Explain when a retry must re-read current state rather than blindly resubmit a stale calculation. Extend the scenario from one ticket row to a two-seat booking spanning distinct records.

### Engineering verification

Measure successful operations, aborted transactions, retry attempts and lock waits. A throughput test with zero contention is insufficient; include a hot-key workload. Verify that error paths release locks and close or return connections to the pool.

## 5.4 Deadlocks

**Core model — Deadlocks**

A transaction deadlock occurs when transactions wait cyclically for resources held by each other. Detection and victim abort are common recovery strategies.

**Original worked illustration**

T1 locks A then requests B while T2 locks B then requests A: each waits on the other's lock and neither progresses.

**Boundary conditions and checks**

Timeout is a heuristic, not proof of deadlock; imposing a consistent lock order can prevent this pattern.

### Domain model and precise assumptions

A deadlock occurs when transactions form a cycle of waiting dependencies that cannot be resolved by waiting alone. A simple case: T1 holds a lock on row A and requests B while T2 holds B and requests A. Neither can proceed. Deadlock detection may build or approximate a wait-for graph and choose one transaction as a victim; some systems use timeouts or prevention rules. Deadlock is distinct from slow but eventually progressing lock contention. The victim transaction must be rolled back appropriately and retried only when its operation is safe to retry.

### Worked field scenario

Imagine an account transfer routine that locks the source account first and destination second. Concurrent transfers A→B and B→A can acquire locks in opposite orders and deadlock. A conventional mitigation is to lock account IDs in a global order, smallest ID first, independent of transfer direction. This reduces one important class of cycle but does not guarantee that every system-level deadlock is impossible: indexes, triggers, foreign-key checks and other resources may introduce additional dependencies.

### Counterexample and limits

Timeouts limit waiting but also abort transactions that might have completed with more patience. Shorter transactions reduce the time locks are held; moving user prompts and slow network calls outside a transaction can prevent avoidable contention. Deadlock avoidance schemes differ from detection-and-recovery. In a textbook wait-for graph, nodes represent transactions and a directed edge T1→T2 means T1 waits for a resource held by T2. A cycle is a sufficient deadlock signal in the simple exclusive-lock model, while richer lock modes and resources require careful interpretation.

### Investigation and self-check

Trace a schedule where T1 locks A, T2 locks B, T1 requests B and T2 requests A. Draw the graph and name both edges. Break the cycle by rolling back T2 and show how T1 may continue. Repeat under deterministic lock ordering and identify which wait can still occur without forming that original cycle. Describe why a blanket retry with zero backoff may increase contention.

### Engineering verification

Keep transaction log entries containing statement durations, lock-wait events and deadlock detector output where supported. A deadlock count alone cannot identify the query responsible. Keep application retries bounded and use jitter when many clients could otherwise retry simultaneously.

### Integrated unit case study

**Unit case study: simultaneous appointment reservation.**

A clinic appointment application has a row for each available slot and must prevent selling a slot twice. Initially `Slot(slot_id,available)` holds (S9,true). Two clients A and B both request S9. A broken implementation performs `SELECT available`, then, in a later statement, `UPDATE Slot SET available=false`. If the operations interleave, both clients can see true and both can send confirmation messages. The final row value false does not reveal that two confirmations were issued. This demonstrates that checking only the final database state is insufficient; the acknowledgment history is part of the correctness contract.

A safer single-row technique is a conditional update that changes the available state only if it still equals true and checks that exactly one row was modified. In a database supporting atomic statement evaluation, only one competing client should report success for the same slot. Add an Appointment record with a unique slot reference inside the same transaction. If booking has more complex rules, such as forbidding overlapping clinician intervals, the invariant spans rows and may require a stronger locking or constraint strategy.

Now introduce payment. Processing a card payment before securing the slot can charge a client for an unavailable appointment. Holding a database lock while waiting on a slow payment gateway can block unrelated appointments. A more robust workflow reserves temporarily under a durable expiry policy, requests payment using a unique idempotency key, confirms only after observing success and releases or compensates on failure. The reservation's expiry and payment callbacks must be safe under retries and out-of-order events. A reservation that expires during a remote confirmation needs an explicit reconciliation policy.

Construct a two-session schedule with T1 and T2 both reading the initial slot. Trace the outcome using an unprotected read–modify–write sequence, a row-locking transaction and a conditional update. Discuss transaction isolation: a row-level atomic conditional update is not evidence that arbitrary cross-row predicates are safe at Read Committed. Document the chosen engine's actual behavior and deadlock retry rules.

**Testing plan.** Send 100 concurrent requests for a single slot with distinct request IDs. Assert exactly one confirmed appointment; reject or waitlist the others without double-billing. Kill one worker after committing but before responding and retry its request ID. Verify that it retrieves the same result rather than creating another booking. Log acquisition times, timeouts, retries and rejected operations separately, so contention does not masquerade as a mysterious application failure.

### Extended executable laboratory

**Extended laboratory: transaction schedule testing.**

Start a disposable database with a single inventory row `(ticket_id='T1',remaining=1)`. Construct two separate connections, A and B, and explicitly control the scheduling of reads and writes. In an unsafe application, both connections read remaining=1. A decides to sell a ticket; B makes the same decision. If both write remaining=0 and announce success without an atomic claim, two tickets may be “sold” despite the row displaying zero. The database's final count is insufficient as a test oracle: the number of success acknowledgments must also be recorded.

Replace the unsafe sequence with a conditional decrement that affects a row only while `remaining>0`. Under appropriate statement-level atomicity, exactly one client can change the row from 1 to 0. The other observes an affected-row count of zero, and the application must not send a success response. Test retries with a stable client request ID and a unique record of completed claims. A timeout after the server's commit is an ambiguous outcome, not permission to submit the same sale under a new ID. This distinction helps keep database correctness and user-facing correctness aligned.

Next test deadlocks with two account rows A and B. In connection 1 lock A before B; in connection 2 lock B before A, if the selected engine provides a supported row-locking operation. Trace the wait-for graph and recovery. Introduce a consistent ID ordering policy and rerun. State what this policy prevents and what it cannot promise about triggers or other locked resources.

For isolation, model an on-call rota where two doctors each may leave duty only if another remains. Have T1 read that B is on call and T2 read that A is on call, then write disjoint rows. An isolation level allowing both commits can violate the “at least one doctor” invariant. Compare the observed behavior to documentation for the actual DBMS rather than assigning the same behavior to all products. The lab report must contain the schedule, chosen isolation level, success/failure outcomes and evidence that any necessary application retry is safe.

### Connections and deeper pitfalls

**Further investigation: locks are not a substitute for a contract.** A team might lock a row representing a course while checking capacity, which can serialize enrollments for that course. That design can work, but the lock's existence is not visible to a future developer who adds a different code path that inserts enrollments without taking the same lock. The invariant should also be protected by a schema mechanism or a narrowly defined transaction API wherever practical. Test every writer, including administration imports and background jobs, not just the user-facing endpoint.

Long-running transactions create performance and operational risks. A transaction held open while waiting for a student to solve a CAPTCHA or for a payment gateway to return can retain locks, old row versions and connection resources. Prefer short units of database work connected by durable workflow states. A reservation with explicit expiry is different from holding a SQL lock for five minutes; the former survives process restarts and can be inspected or released by a reconciliation worker. Expiry handling must still be race-safe with late payment confirmation.

A correct retry strategy distinguishes conflicts from validation failures. A serialization failure may justify retrying a complete transaction a bounded number of times using freshly read data. A uniqueness conflict on a known request ID should usually return the existing outcome. A negative balance constraint means the user's requested operation is invalid, not something to retry indefinitely. Every repeated attempt increases workload and can magnify an outage if backoff and timeouts are ignored.

## Three worked questions

### Problem 1: Atomicity: worked verification
A transfer of 50 debits account A but credit to B fails before commit. What should atomicity ensure?

**Set up the model and conditions**
Both updates belong to the same transaction representing the transfer.

**Carry out the calculation or proof**
If the transaction cannot complete, rollback removes its partial state change.

**State the result and its scope**
Neither account balance should reflect the transfer after rollback.

**Detailed reasoning and validation.** If A begins with 120 and B with 80, a transfer of 50 should commit balances 70 and 130, preserving a total of 200. If the credit to B fails before commit, both changes must roll back to 120 and 80 under the assumed atomic transaction. It would violate the requirement to leave A at 70 and B at 80. This does not establish safety for external payment gateways, which do not automatically join the SQL transaction. When the client loses its connection after issuing COMMIT, it may be uncertain whether the commit succeeded; query a durable transfer ID before retrying so that an acknowledged or ambiguously acknowledged operation is not duplicated.

**Answer:** Neither account balance should reflect the transfer after rollback.

### Problem 2: Isolation: worked verification
Two transactions read seat count 9 with maximum 10 and both insert one reservation. What anomaly might occur?

**Set up the model and conditions**
Each transaction sees count 9 and independently decides one new reservation is allowed.

**Carry out the calculation or proof**
Both may commit disjoint inserts under an insufficient isolation policy.

**State the result and its scope**
Final count can become 11, violating the cross-row capacity invariant.

**Detailed reasoning and validation.** Both clients see nine existing reservations and conclude that inserting one would reach capacity ten. Because each inserts a different row, a snapshot-based system that permits write skew may accept both commits, leaving eleven reservations. The invariant is not “each transaction inserts at most one”; it is “there are at most ten committed reservations across the offering.” A protected capacity counter updated conditionally, an appropriate serialization rule or an engine-specific exclusion/capacity protocol can enforce the shared limit. Test with concurrent connections and count successful acknowledgments. The fact that no single database row was overwritten does not mean isolation preserved the business rule.

**Answer:** Final count can become 11, violating the cross-row capacity invariant.

### Problem 3: Concurrency Control: worked verification
T1 locks row A then waits for B, while T2 locks B then waits for A. Draw the wait cycle.

**Set up the model and conditions**
T1 waits on a resource held by T2, so create edge T1→T2.

**Carry out the calculation or proof**
T2 waits on a resource held by T1, so create edge T2→T1.

**State the result and its scope**
The cycle indicates deadlock in this single-instance lock model.

**Detailed reasoning and validation.** In a wait-for graph, T1 has an edge to T2 because T1 needs a lock currently held by T2. T2 has an edge to T1 for the symmetric reason. The cycle T1→T2→T1 means neither can make progress in the simple non-preemptive exclusive-lock model. A deadlock detector can break the cycle by aborting one victim transaction and releasing its locks; the surviving transaction may then proceed. Ordering all account locks by ascending account ID avoids this direct two-lock cycle, though other resources can still cause deadlocks. A safe retry restarts the entire aborted business transaction using current data and respects an idempotency key if external effects are involved.

**Answer:** The cycle indicates deadlock in this single-instance lock model.
