# Database Systems — Unit 6: Recovery and integrity

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 6.1 Logging

**Core model — Logging**

Write-ahead logging records changes before dirty pages reach stable storage. The WAL rule underpins redo/undo recovery in many systems.

**Original worked illustration**

If a transaction changes page P, its log record must become durable before the modified data page is flushed, so recovery can replay or roll back safely.

**Boundary conditions and checks**

A commit acknowledgment requires the engine's configured durability semantics; unsafe disk caches or relaxed fsync settings can invalidate assumptions.

### Domain model and precise assumptions

Logging records enough information to recover a durable database state after failure. Write-ahead logging requires a relevant log record to reach durable storage before the corresponding changed data page is allowed to reach durable storage. This ordering makes it possible to reconstruct committed changes even when some pages were not flushed at commit. The log is not merely an audit trail for business users; it is a low-level recovery structure recording operations or page changes and transaction boundaries. Its format, record identifiers and durability choices differ among systems. A source log may contain sensitive data, so backup and retention policies matter.

### Worked field scenario

Consider a page P initially containing value 10. A transaction changes the value to 15, and the engine appends a log record describing the update. If the data page is written before the relevant log record is durable, a crash can leave data and log irreconcilable. In a WAL protocol, log durability must precede unsafe data-page flushing. The transaction's commit acknowledgment must also follow the durability policy the service promises; otherwise a client can receive success for work that may disappear after power loss. Different synchronous-commit settings deliberately trade latency against the strength of that promise.

### Counterexample and limits

Some recovery designs combine redo and undo information; other designs use multiversion reconstruction and different mechanisms. Do not reduce all DBMS recovery to a single uniform algorithm. PostgreSQL WAL and SQLite WAL share the idea of logging before later data-file integration but differ greatly in file format and recovery architecture. The data page and log need not be written on the same schedule, and a checkpoint is not equivalent to permanently deleting every older log record.

### Investigation and self-check

Write a toy trace: BEGIN T1, UPDATE P(10→15), COMMIT T1, then a crash before data page P is written. Explain which log evidence allows recovery of 15. Compare with a crash before the commit record is durable and state why recovery behavior depends on the database's commit protocol. Explicitly distinguish the logical final value from the physical ordering of writes.

### Engineering verification

Test crash consistency only with controlled fault injection and a disposable database. Validate checksums or other recovery signals according to the engine. Database backups should include all relevant files and WAL segments for the intended recovery point; copying a hot data directory with ordinary file-copy commands can be unsafe.

## 6.2 Checkpoints

**Core model — Checkpoints**

A checkpoint records a recovery starting position or dirty-page/transaction state, limiting recovery work without guaranteeing every page is immediately clean.

**Original worked illustration**

If all required log records before LSN 100 are durable and the checkpoint tracks remaining dirty pages, recovery may avoid scanning older irrelevant history.

**Boundary conditions and checks**

A checkpoint is not the same as a backup, and its mechanics differ between fuzzy and quiescent checkpoint designs.

### Domain model and precise assumptions

A checkpoint narrows the amount of recovery work by recording a recovery boundary and coordinating dirty-page or log-management state. Its precise meaning depends on the storage engine. A checkpoint need not flush every dirty page to durable storage, and it may be fuzzy, allowing normal changes to continue while checkpoint metadata is produced. Recovery may still need log records from before or after the checkpoint depending on active transactions and page states. In SQLite WAL mode, checkpointing moves committed WAL frames into the main database under its particular protocol. In PostgreSQL, checkpointing and log recycling have different internal mechanics. Do not transfer operational advice uncritically between these systems.

### Worked field scenario

Suppose a system generates 6 MB of recovery log each minute and a complete scan of a log segment takes a fixed amount of time. Halving the interval between safe recovery boundaries may reduce potential replay work but can increase write bursts or flush pressure during normal operation. A toy trade-off measures log growth separately from write amplification and checkpoint duration. It is a mistake to assume recovery time is determined by the checkpoint interval alone: dirty-page volume, checkpoint overlap, storage bandwidth and index rebuilding can also matter.

### Counterexample and limits

Operational systems may perform background checkpoints automatically. Forcing checkpoints too frequently can damage throughput. Long-running snapshots can keep WAL segments or page versions alive beyond the apparent checkpoint and must be considered in retention and backup planning. A monitoring dashboard should distinguish log bytes generated, bytes retained, recovery-lag estimates, checkpoint frequency and checkpoint I/O. Correlated counters are not interchangeable measures.

### Investigation and self-check

Create a checkpoint schedule for a laboratory workload with 30 transactions per minute, each producing two illustrative change records. Predict 60 log records per minute, then describe why those records do not directly translate to a fixed number of database pages. Introduce a long-running reader and ask whether old versions or WAL segments may have to be retained. Compare an automatic policy with an artificial policy that forces a checkpoint after every transaction.

### Engineering verification

Measure checkpoint duration, write latency percentiles and log retention simultaneously. A configuration change that shortens replay but causes extreme online stalls might not improve system availability. Keep recovery point and recovery time objectives distinct when reporting results.

## 6.3 Crash Recovery

**Core model — Crash Recovery**

Crash recovery analyzes persisted logs and data pages to reconstruct a transactionally consistent state. Systems may redo history then undo losers.

**Original worked illustration**

If T1's committed update has a durable log but an old data page remains on disk, redo restores it. If T2 never committed, undo removes its effects as required.

**Boundary conditions and checks**

Recovery claims require testing crashes at different write boundaries and understanding torn writes, checksums and storage guarantees.

### Domain model and precise assumptions

Crash recovery reconstructs a consistent state after unexpected termination using log records, checkpoints and a defined commit protocol. A classic ARIES-style explanation separates analysis, redo and undo passes, but not every engine implements precisely that algorithm. Analysis discovers transaction and dirty-page state, redo repeats relevant updates, and undo reverses uncommitted work under the algorithm's rules. Idempotent redo is essential because recovery itself can be interrupted and restarted. The first question is always which transactions were committed according to durable evidence, not which SQL statements a client happened to send.

### Worked field scenario

Consider T1 committed an insertion and T2 updated another row but did not commit before a crash. The required recovered logical state contains T1's effect and excludes T2's incomplete effect, assuming a durability policy that acknowledged T1 only after the necessary log was persisted. Some pages may already contain portions of both transactions when recovery begins. Recovery logic must reconcile this mixed physical state without interpreting physical presence as proof of commit. The textbook distinction between STEAL/NO-STEAL and FORCE/NO-FORCE describes when uncommitted changes may reach disk and when committed pages must be forced; those policies influence what undo and redo information is needed.

### Counterexample and limits

The recovery window also interacts with replica failover and external side effects. After a crash, a client may not know whether a request committed. A durable idempotency record lets it query the outcome and avoid duplicate logical effects. Restoring from a backup adds another layer: point-in-time recovery requires the backup and the correct retained log history. A backup that opens correctly is not proof that the application schema and required business invariants remain usable.

### Investigation and self-check

Construct a trace with UPDATE records for T1 and T2, a COMMIT for T1, a checkpoint marker and a crash. Classify the transactions as winners or losers for a simplified undo/redo system. Explain why replaying a committed update must not create duplicate payments if recovery is restarted. Build an application-level test with a unique business event ID and show how it detects duplicate replay at the logical layer.

### Engineering verification

Perform restore rehearsals on isolated infrastructure. Check that recovered row counts, referential constraints and representative business workflows pass. Record achieved recovery point and recovery time instead of assuming backup availability guarantees zero data loss or a fixed recovery deadline.

## 6.4 Consistency Constraints

**Core model — Consistency Constraints**

Consistency constraints include uniqueness, foreign keys, checks and procedural business invariants. A transaction preserving declared constraints may still violate undeclared requirements.

**Original worked illustration**

CHECK(quantity>=0) can prevent negative stock per row; preventing overselling across several rows may require a stronger transaction-level rule.

**Boundary conditions and checks**

Application-level validation alone is race-prone if another writer modifies data after the check.

### Domain model and precise assumptions

Integrity constraints must hold across normal writes, maintenance and recovery. A primary key prevents duplicate identifiers in its scope; foreign keys restrict references; business invariants may additionally depend on multiple rows and transactions. A database can pass an internal page checksum yet contain logically invalid business data produced by a flawed application. Conversely, a reported constraint violation after a migration may reflect an invalid import rather than physical corruption. Distinguish physical integrity, relational integrity and domain integrity in incident reports.

### Worked field scenario

Suppose Purchase(order_id,customer_id,total) and LineItem(order_id,quantity,price) exist. An invariant might require the order total to equal the sum of quantity×price of its lines. This is not an ordinary one-row CHECK. If order totals are stored as derived data, the application must maintain them transactionally, use a reliable trigger, or calculate them when needed. If storing both values for performance, a periodic reconciliation query detects divergence but does not prevent transient inconsistency. Monetary rounding and currency rules also require explicit policy; floating point should not silently stand in for exact accounting representation.

### Counterexample and limits

A migration can expose hidden violations when legacy systems allowed orphan references or disabled constraints for bulk loading. Validation needs staged checks, remediations and a rollback plan. Deferred constraints can allow temporary intermediate states inside a transaction but require validity at commit under their documented rules. A design should not assume all engines support every deferrable constraint. Security permissions and administrative bypass paths must also be considered when claiming an invariant is enforced.

### Investigation and self-check

Write integrity tests for absent customers, duplicate order IDs, negative quantity and a mismatch between stored and derived total. Use a transaction to add two line items and update the order total, then deliberately raise an exception between statements. Verify that the final committed state either includes the consistent change or excludes it. Separate the invariant that protects current transactions from an audit that catches legacy defects.

### Engineering verification

Schedule periodic reconciliation without interpreting it as a replacement for safe constraints. Track bad-row counts, failed schema changes and the age of unresolved inconsistencies. Before repairing inconsistent rows, preserve evidence of their origin; silent overwrites can erase the information needed to diagnose recurring defects.

### Integrated unit case study

**Unit case study: failure during a grade update.**

A school system stores Grade(student_id,course_id,score), and a registrar publishes final scores in batches. Consider an update that changes Grade(S17,CS101) from 68 to 74, then writes a corresponding GradeChange event containing actor, reason and timestamp. The domain requirement is that the score and its auditable event commit together. A transaction that updates Grade but crashes before inserting the event should roll back if both changes are within the same atomic boundary. If the event must also be sent to another service, store an outbox record in the same local transaction and publish it asynchronously with retry and deduplication.

At the physical layer, imagine page P contains the Grade row and page Q contains the GradeChange row. The engine has dirtied both in memory and recorded appropriate WAL. A crash can occur after P was written but before Q, or after durable commit but before either page was written. A write-ahead protocol and the engine's recovery logic reconcile such mixed physical states. Never infer transaction commit from observing one changed page in a low-level dump. The relevant durable commit evidence and recovery rules determine whether the transaction survives.

Build a toy log timeline: LSN 10 BEGIN T1, LSN 11 change P, LSN 12 change Q, LSN 13 COMMIT T1. Suppose P and Q remain dirty when the process terminates. A simplified redo recovery can restore both committed effects using the relevant log records. Now remove durable LSN 13 and reconsider: an incomplete transaction must not appear as a committed update under the assumed policy. This trace teaches the conceptual distinction; real engine logs contain much more bookkeeping and may perform physical undo differently.

Next define a backup scenario. A nightly base backup and retained WAL segments can support point-in-time restore, but only if the backup mechanism and segment retention are correct for the engine. Restore to a staging environment, check that the final score matches the chosen recovery point, and verify that GradeChange events agree with Grade rows. An empty error log is not sufficient evidence of a usable restore.

**Operational checks.** Measure write latency during checkpoints, log retention under a long-running reader, and recovery time after a controlled termination. Document whether the client received COMMIT acknowledgment before the fault. A lost acknowledgment is an application ambiguity that should be resolved through a durable operation ID and status lookup rather than blind repeat updates.

### Extended executable laboratory

**Extended laboratory: recoverable changes under fault injection.**

Create two related rows, a Grade and a GradeChange event, updated in one transaction. In the normal case, commit produces the new grade and one corresponding event. Inject an exception after updating Grade but before inserting GradeChange; an explicit rollback should leave both in the old logical state. Inject an exception after both statements but before COMMIT; the transaction should again roll back when aborted. Reconnect after each simulated failure so the test does not accidentally inspect uncommitted values through the same session.

Now reason about physical durability separately. A write-ahead protocol can acknowledge a committed transaction after required log data are durable without forcing every changed table page immediately. A subsequent crash may leave some pages old, some updated. Recovery uses durable log and page information to reconstruct a consistent committed result. Draw a timeline for BEGIN, row update, event insert, COMMIT, page flush and crash. Consider three crash points: before durable commit, after durable commit but before page flush, and after checkpoint. Do not assume checkpoint always means all pages have been flushed; inspect the engine's documented behavior.

Add an application ambiguity test: terminate a client connection just after sending COMMIT, before the client receives a reply. The client cannot infer from silence alone whether the commit succeeded. A durable unique request ID stored within the transaction enables a status lookup. If the ID already exists with a committed result, the retry should return the previous result instead of writing a duplicate event. This mechanism addresses logical duplication and complements, rather than replaces, low-level WAL recovery.

Complete the lab by restoring a backup to a clean database. Verify row counts, foreign keys, representative joins and the correspondence of current grades to GradeChange history. Measure the restore's actual duration and record the recovered timestamp or log position. A recovery plan is not validated by the mere existence of backup files. Use disposable data for fault tests; deliberately killing a real production database is not a safe way to learn recovery mechanics.

### Connections and deeper pitfalls

**Further investigation: recovery assurance as a measurable property.** Recovery point objective is a bound on tolerated data loss, while recovery time objective is a bound on acceptable service restoration delay. They are different dimensions. An application can have fast restart but lose recently acknowledged data if durability settings are weak, or preserve every acknowledged transaction but require a lengthy restore after total storage loss. Define the failure scenario first: process crash, server power loss, corrupted disk, accidental delete or region outage may demand different recovery processes.

Backups should be validated for logical usability. A successful checksum of an archive proves that bytes can be read, not that the right time range and external dependencies were included. Restore the database, execute representative application queries, verify role permissions and confirm expected schema versions. If a logical backup omits large object storage or external file references, the user experience may remain broken despite valid table data. Keep restore documentation synchronized with schema migrations.

When writing a toy WAL simulator, label its assumptions. A counter of `two records per transaction` cannot predict the real WAL volume of an engine whose updates affect pages, indexes and metadata. The simulator is valuable for reasoning about growth under an explicitly chosen record-count model, but it should not be presented as an operational log-sizing calculator. The same principle applies to checkpoint simulations: useful conceptual models are not measurements of a deployment.

## Three worked questions

### Problem 1: Logging: worked verification
A page has an updated value but its WAL record is not durable. Is it safe to flush the page?

**Set up the model and conditions**
The WAL rule requires the describing log record to become durable before the dirty page reaches disk.

**Carry out the calculation or proof**
If flushed first, a crash may leave an unlogged data change that recovery cannot correctly explain.

**State the result and its scope**
No; force the appropriate log record first.

**Detailed reasoning and validation.** Write-ahead means the change-describing log information must reach the required durable medium before a modified data page containing that change is allowed to reach durable storage. If the page is flushed first and the server crashes, recovery may find a changed page without the information required to reconcile its update with commit status. The phrase “write the log first” refers to durability ordering, not just placing a record in an in-memory log buffer. In an implementation with buffered I/O, the relevant flush barrier or durability primitive matters. State the guarantee at the chosen engine's configured synchronous-commit level instead of assuming every cache and drive honors the same promises.

**Answer:** No; force the appropriate log record first.

### Problem 2: Checkpoints: worked verification
A committed update has durable WAL but its data page remains old at crash. What does redo do?

**Set up the model and conditions**
Recovery inspects durable committed log records and page progress information.

**Carry out the calculation or proof**
It reapplies needed logged changes to the data page, using idempotent/log sequence logic.

**State the result and its scope**
Redo restores the committed update if it was not already reflected on disk.

**Detailed reasoning and validation.** A committed transaction can be durable even when its changed page is still only in memory, provided the engine's log protocol has durably recorded the necessary information. After a crash, redo inspects log and page progress to apply updates not already reflected in persistent data pages. Reapplying must be safe across repeated interrupted recovery attempts, often using log-sequence comparisons or an equivalent mechanism. This example is intentionally abstract and does not specify an engine's exact redo algorithm. A restored logical value should match the committed transaction, whereas an uncommitted concurrent update must not be reported as a committed outcome.

**Answer:** Redo restores the committed update if it was not already reflected on disk.

### Problem 3: Crash Recovery: worked verification
Explain why a checkpoint is not a backup.

**Set up the model and conditions**
A checkpoint is recovery metadata and may describe dirty pages or active transactions.

**Carry out the calculation or proof**
It does not create an independent recoverable copy of every required data file.

**State the result and its scope**
A backup needs separate durable data and log retention practices.

**Detailed reasoning and validation.** A checkpoint creates a recovery reference point and can coordinate flushing or log state, but it does not copy the whole database to independent safe storage. If the underlying data drive fails permanently, a checkpoint on that drive can be lost with the data. A backup provides a separately managed recoverable copy, possibly combined with retained log history for point-in-time recovery. Test by restoring to a clean environment and checking application-level consistency; finding a recent checkpoint is not a substitute. Likewise replication may carry accidental deletions to every follower, so replication and backup serve different failure scenarios.

**Answer:** A backup needs separate durable data and log retention practices.
