# Operating Systems — Unit 3: Concurrency

synchronization; locks; condition variables; deadlock

## §3.1 Synchronization

**Core model — Synchronization**

Synchronization coordinates critical sections and shared invariants. Mutual exclusion is necessary when interleaved memory operations would otherwise violate a required state property.

**Original worked illustration**

An account balance updated by read-modify-write must exclude another overlapping updater or use a suitable atomic operation to avoid lost updates.

**Boundary conditions and checks**

A lock protecting different variables may still be insufficient if the invariant spans both and transactions can observe inconsistent intermediate states.

### Atomicity, race conditions, and invariant preservation

Synchronization is needed when legal interleavings of operations can violate a shared-state invariant. The canonical counter example is useful because the expected result is simple, but real invariants are often relational. In a bounded queue, the write index, read index, item count, and actual storage must stay consistent. In a money-transfer system, debiting one account and crediting another should not expose a state with lost funds to a concurrent observer unless the design explicitly permits provisional states. The important unit of reasoning is the critical operation whose externally observable effects must be controlled, not necessarily a single source-code statement. A compiler or processor may split a high-level expression into multiple memory operations.

A data race in a language with a formal memory model can have consequences beyond an intuitively 'wrong value.' Some languages treat races on ordinary memory as undefined behavior, allowing compiler optimizations that defeat naive reasoning about interleaving. Atomic variables, locks, message passing, and thread confinement address different parts of the problem. Atomic load and store operations avoid torn values under the relevant memory model, but a multistep invariant can still fail if it requires a transaction rather than one atomic cell. Memory-ordering guarantees also matter: publishing a pointer before fully initializing the pointed-to object can expose partially constructed state if synchronization is incorrect.

One practical exercise is to specify an inventory rule: available count may never become negative, and every accepted reservation must decrement availability exactly once. If two workers both read one available item and both approve, the rule is violated. Surrounding only the final write with a mutex does not solve the stale decision. Instead, put read-check-decrement within a single protected region or use an atomic conditional update with a clear success/failure outcome. Prove safety by showing every successful reservation observes positive availability and commits exactly one decrement. Then discuss liveness: a system that preserves safety by blocking forever is not a useful reservation service. Instrument the example with randomized task interleavings, record each operation's logical timestamp, and distinguish a deterministic failure trace from a probabilistic reproduction rate.

## §3.2 Locks

**Core model — Locks**

A lock provides exclusive access but adds waiting, scheduling and possible priority inversion. Deadlock-free locking rules often impose a global acquisition order.

**Original worked illustration**

If every thread acquires lock A before lock B, a cycle in which one holds A waiting for B while another holds B waiting for A cannot arise from conforming threads.

**Boundary conditions and checks**

Nonblocking progress and fairness are separate: a deadlock-free program can still starve a thread.

### Locks, fairness, and the scope of protected state

A mutex provides mutual exclusion over a programmer-defined critical section; it does not know which variables form the application invariant. A correct locking plan lists all state whose relationships need protection and ensures every modifying path follows the same policy. Locking a counter update while reading a related limit without protection can still break the invariant. Conversely, holding one broad lock through a disk operation may preserve correctness but turn a parallel system into a serialized queue. Fine-grained locking can improve throughput but increases the number of potential lock-order cycles and consistency states an engineer must reason about.

Suppose a cache has a map of keys to entries and a least-recently-used list recording access order. The map and the list must agree. If a writer removes an entry from the map but another thread reads the list before the removal is reflected there, the reader may follow a pointer to an invalid object. A single lock protecting both structures provides a simple proof. More complex designs can use reference counting, per-bucket locks, read-copy-update, or versioned snapshots, but every technique demands a careful account of reclamation and reader visibility. A lock-free data structure is not automatically faster; it can create retries and memory-reclamation challenges under contention.

Fairness is also not guaranteed by every lock API. A thread that releases a lock may reacquire it before waiting threads execute, and high-priority work can wait behind a low-priority holder. Priority inversion occurs when a high-priority task depends on a resource held by a low-priority task, possibly while medium-priority work consumes CPU time. Priority inheritance is one possible mitigation when supported and appropriate, but it does not magically solve arbitrary cycles or lengthy critical sections. For a lab, plot lock-hold time, acquisition wait time, and total useful throughput as worker count grows. Vary how much computation occurs inside versus outside the critical region. Identify where adding workers ceases to help and why. The lesson is not simply to use fewer locks; it is to write down the invariant, choose the smallest correct protection scope, and measure contention honestly.

## §3.3 Condition Variables

**Core model — Condition Variables**

A condition variable allows waiting until a predicate becomes true while releasing and reacquiring an associated mutex. The predicate is rechecked in a loop.

**Original worked illustration**

A consumer waits while a queue is empty, releasing the mutex. After a producer inserts an item and signals, the consumer reacquires the mutex and rechecks nonemptiness.

**Boundary conditions and checks**

Signals are not durable messages. Using if instead of while can fail under spurious wakeups or competition from other consumers.

### Condition variables and predicate-based waiting

A condition variable signals that some state *may* now satisfy a predicate. It is not a mailbox that remembers an unlimited number of events. The standard discipline is to hold an associated mutex, check a shared predicate, and wait in a loop while the predicate is false. Waiting releases the mutex atomically with entering the wait state under the library's documented semantics, allowing another thread to modify state and signal. On return, the waiter reacquires the mutex and checks again because notifications may be spurious or competing consumers may have already changed the state.

Consider a producer and consumer sharing a bounded queue with capacity three. A producer must wait while the queue is full; a consumer waits while it is empty. Inserting an item changes the empty predicate and may justify signaling a consumer; removing one changes the full predicate and may justify signaling a producer. If a producer checks queue size without the mutex and then waits, it can miss a notification between the check and the wait. The queue then has free space but the producer sleeps indefinitely. The condition variable did not fail; the program violated the atomic check-and-wait discipline. The full and empty predicates should be written as exact expressions over protected state.

Broadcast wakes multiple waiters, but it does not promise that all will pass their predicates. A system may choose signal rather than broadcast when exactly one task can progress, although cases with multiple different predicates may require broader wakeups. A timeout introduces an additional outcome that must be distinguished from ordinary notification and cancellation. Build an interleaving table with columns for queue count, mutex owner, waiting producers, waiting consumers, and the predicate each evaluates. Walk through two producers and two consumers from an empty queue, then create a hypothetical missed wakeup by separating the predicate check from its locking protocol. A model checker can enumerate a small bounded number of operations; in human reasoning, an explicit transition table is often enough to expose the incorrect step.

## §3.4 Deadlock

**Core model — Deadlock**

Deadlock requires a cycle of waiting under conditions such as exclusive resources and hold-and-wait. Prevention, avoidance, detection and recovery have different costs.

**Original worked illustration**

Thread 1 holds A and waits for B while thread 2 holds B and waits for A; neither can advance. Consistent lock ordering removes this example.

**Boundary conditions and checks**

A wait-for cycle is sufficient for deadlock in common single-instance models, but resource multiplicity requires more careful analysis.

### Deadlock, livelock, and recovery

Deadlock occurs when a collection of activities cannot proceed because each waits for resources held or conditions dependent on others in the collection. The familiar necessary conditions in a resource-allocation model are mutual exclusion, hold-and-wait, no forced preemption, and circular wait. Breaking one of those conditions can prevent deadlock, but the costs differ. A global lock order prevents a circular wait when all code follows it. Acquiring all resources at once may avoid hold-and-wait but waste resources. Forced rollback may restore progress for transactional resources, yet is unsafe for irrevocable physical effects. A wait-for graph is a useful diagnostic only when edges faithfully represent the blocking relationship.

Suppose worker A holds lock X and requests lock Y, while worker B holds Y and requests X. Draw edges A→B and B→A. Neither can advance under ordinary blocking mutex semantics. If the application imposes X-before-Y order on both workers, B cannot acquire Y before X in the relevant path, removing the cycle. But adding a third lock Z through a helper method can silently violate that order, so the rule must be checked at every acquisition point. Timed try-lock with retries avoids some deadlocks but can cause livelock: both workers repeatedly retreat and retry in synchrony without completing useful work. Backoff or deterministic ordering may be required.

A production deadlock report needs more than the statement that the application stopped responding. Collect stacks showing threads waiting, the resources and owners, and the operations required for release. Differentiate true cycles from slow I/O, starvation, resource exhaustion, and a failed worker that never sends completion. For an educational exercise, provide a resource matrix of two resource classes and three processes, then test a candidate execution sequence for safe completion rather than guessing from totals alone. Note that a 'safe state' in avoidance theory means there exists a completion sequence under declared maximum claims; it is not a prediction that the actual workload will choose that sequence. A recovery policy should specify whether rollback, process termination, or administrator intervention is acceptable for the affected resources.

### Integrative case study — a bounded queue with two producers and three consumers

A bounded work queue has capacity four. Two producers place jobs into it; three consumers remove jobs and process them. The correctness requirements are not just that the queue size stays between zero and four. Each successfully submitted job must be removed exactly once unless an explicit cancellation or drop policy applies; no consumer may read an uninitialized slot; and shutdown must not strand threads permanently waiting for a condition that will never become true. A simple shared representation has a circular buffer, head and tail indices, and a count. All four values form a related invariant. One mutex can protect their updates while condition variables indicate potential changes to the nonempty and nonfull predicates.

A producer locks the mutex and waits in a loop while count equals capacity, then writes a job into the tail slot, updates tail modulo capacity, increments count, and signals a consumer before unlocking. A consumer locks, waits in a loop while count equals zero and producers are still active, takes the head job, updates head modulo capacity, decrements count, and signals a producer. It releases the mutex before performing expensive job processing. Keeping processing inside the critical section would serialize all consumers and make the concurrency largely fictional. But moving the dequeue itself outside the lock would create races over indices and ownership. The critical section protects just the shared queue-state transition.

Why use a loop around the condition wait? A waiting consumer may wake spuriously, or another consumer may remove the only job before this one reacquires the mutex. The signal means the shared predicate should be checked again, not that the receiving thread owns a job. To expose a lost wakeup, write an incorrect version in which the consumer checks count without a mutex, the producer inserts and signals, and the consumer then begins waiting. The queue contains a job but the consumer sleeps. A correct atomic check-and-wait arrangement prevents that interval. This is a proof about the synchronization protocol, not a guarantee that the scheduler will always run the consumer promptly.

Shutdown adds a nontrivial state transition. When the last producer stops, set a closed flag under the mutex and broadcast to consumers. A consumer awakened to find the queue empty and closed may exit. If jobs remain, it should drain or discard them according to a documented shutdown policy. One possible design rejects future submissions once closed, continues processing existing entries, and signals joiners after all consumers finish. Cancellation needs the same careful thought: a producer canceled while holding the mutex must not leave it permanently locked, and a consumer canceled after removing a job needs a defined handoff or failure record.

To test the queue, enumerate all interleavings of two producers each submitting one tagged job and two consumers each requesting one job, under a bounded deterministic simulator. Check no loss, no duplication, and the count bounds. Then test capacity one, multiple consumers waiting on empty, producer waiting on full, and shutdown before any item is submitted. Measure throughput with short and long job processing times. As processing grows, parallel consumers may help; as the lock hold time grows, the queue becomes the bottleneck. Distinguish safety (invariants never violated) from liveness (work eventually progresses under stated fairness conditions). Both are required for a useful operating-system service.

### Diagnostic exercise — prove and break a shared-state invariant

Define the bounded queue invariant as 0≤count≤capacity, with read and write positions always in range. Add the stronger statement that each accepted item has exactly one owner: a producer before submission, the queue while enqueued, or one consumer after removal. Verify each atomic transition preserves the invariant if the mutex is held. Then intentionally move a count increment outside the critical region and enumerate an interleaving that loses an update or exposes an inconsistent queue. Draw a wait-for graph when two locks protect separate resources; show a cycle and then impose a total acquisition order. Introduce a timeout and ask whether it resolves deadlock, livelock, or starvation in the trace. Finish with shutdown while one producer is blocked on a full queue: if consumers exit first without signaling, the producer may remain asleep forever. Document a closed state and broadcast rule that lets all waiters recognize terminal conditions.

### Boundary cases and falsifiable design claims

The notion of an 'atomic operation' depends on the abstraction level. A CPU instruction may atomically update one aligned memory word under specified conditions, but a multi-field application invariant can still be exposed between separate atomic updates. A compare-and-swap loop can implement conditional updates, yet must handle retries and appropriate memory ordering; it may also suffer starvation under contention. Avoid the simplistic idea that changing every shared variable into an atomic value automatically makes an entire concurrent object correct. Linearizability requires that each operation appears to take effect at a valid single point between invocation and response; that is stronger than each individual register load being atomic.

Deadlock diagnosis needs blocked edges, not merely two busy threads. A thread consuming CPU in an infinite loop may prevent a cooperative worker from progressing without forming a mutex wait cycle. A livelock can involve threads repeatedly acquiring and releasing locks while making no useful progress; metrics may show activity rather than sleep. Starvation means a particular task fails to receive service even though the system as a whole continues progressing. These conditions have distinct remedies: lock ordering, backoff, admission fairness, or fixing a spin condition. A watchdog terminating tasks indiscriminately may restore availability while destroying incomplete critical updates.

An extra exercise compares two producers racing to close a queue. If the first producer closes it while the second has pending work, the second may lose accepted jobs unless ownership of shutdown is coordinated. Use a producer-reference count or one supervising coordinator, and write down when the queue becomes terminal. At exactly full capacity, an additional enqueue should either wait, reject, or replace an item under an explicit policy. Silent overwrite violates at-most-once ownership if the consumer has not yet acquired the displaced item. Every exit path must wake the right waiters or the system may remain blocked indefinitely.

## Three worked questions

### Synchronization: worked application 1

Two threads each increment a shared counter from five without locks. Show lost update.

**Set up the model and conditions**

Thread A reads 5; thread B reads 5 before A stores.

**Carry out the calculation or proof**

Both compute 6 and both write 6.

**State the result and its scope**

Final value can be 6 rather than the expected 7.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

The unsafe trace begins with count five. Thread A reads five, thread B reads five, A computes and stores six, and B computes and stores six. The final count is six even though two increments were requested, violating the expected postcondition count=old+2=7. This is a lost update, not an arithmetic overflow. The precise order of the two stores does not matter because both computed the same stale value. A correct implementation protects the entire read-modify-write critical section or uses an atomic fetch-add operation with appropriate memory semantics. Protecting only the final store would still allow both threads to compute six. Test that a synchronized implementation produces seven for every allowed ordering of the two complete atomic increments, and explain why the programming language's memory model matters when ordinary non-atomic variables are raced.

### Locks: worked application 2

A consumer wakes from a condition-variable wait. May it assume the queue is nonempty?

**Set up the model and conditions**

The wakeup only says a notification or spurious wake occurred.

**Carry out the calculation or proof**

Another consumer may remove the queued item before this thread reacquires the mutex.

**State the result and its scope**

No; re-check queue nonemptiness in a while loop while holding the mutex.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

A consumer awakened after waiting must hold the associated mutex and re-evaluate the predicate queue_nonempty. An earlier signal proves only that the predicate may have become true at some time. Another consumer can remove the item before the first waiter reacquires the mutex; spurious wakeups may also occur. The safe protocol is `while queue empty and not closed: wait(condition,mutex)` with a clearly defined closed-queue outcome. An `if` is inadequate because it checks at most once. Verify the behavior using an execution trace: producer inserts one item, broadcasts; consumer A acquires the mutex and removes it; consumer B subsequently acquires the mutex and finds the queue empty. B must wait again or exit under shutdown rules, not access a missing element. This is a demonstration of predicate correctness, separate from whether the operating system guarantees fairness in which waiter runs first.

### Condition Variables: worked application 3

Threads T1 holds A waiting B and T2 holds B waiting A. Identify the deadlock cycle.

**Set up the model and conditions**

T1 cannot proceed until T2 releases B.

**Carry out the calculation or proof**

T2 cannot proceed until T1 releases A.

**State the result and its scope**

Wait-for graph T1→T2→T1 is cyclic; global ordering prevents this case.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Build a wait-for graph with one vertex per thread and an edge X→Y when X cannot progress until Y releases a resource. Here T1 holds A and needs B held by T2, so T1→T2. T2 holds B and needs A held by T1, so T2→T1. The two edges form a directed cycle. Under the stated nonpreemptive mutex conditions, neither worker can complete. A prevention rule is to acquire A before B on every code path: a worker that currently holds B cannot then request A without violating the order. Timeouts might break the blocking behavior but require safe rollback and may introduce repeated livelock. Test an acyclic case such as T1 holding A while requesting B held by T2, with T2 not waiting on any other resource; once T2 releases B, progress is possible. The presence or absence of a graph cycle is meaningful only when graph edges accurately represent real blocking dependencies.
