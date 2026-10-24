# Unit 6: Formal verification

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 6.1 Temporal Properties

### Core reasoning and definitions

Temporal properties describe how propositions behave across sequences of states. A safety property says something bad never happens, such as two users never simultaneously owning one exclusive lock. Liveness says something good eventually happens under stated fairness and environmental assumptions. Temporal logics provide operators such as “always,” “eventually,” “next,” and “until”; they express requirements about traces rather than isolated output snapshots. In Linear Temporal Logic, `G p` means proposition p holds globally on a trace, and `F q` says q eventually becomes true. A finite test execution cannot generally establish unbounded liveness, because the promised event might occur after the test stops; bounded response properties require an explicit deadline or step limit. Fairness assumptions determine whether a scheduler could ignore a task forever.

### Original investigative exercise

Model an exam submission flow with states Draft, Accepted, Processing, and Recorded. State the safety requirement “a recorded submission belongs to an accepted attempt,” and a conditional liveness requirement “an accepted, durably queued attempt eventually becomes recorded if workers keep making progress.” Generate traces that include repeated acknowledgement loss and worker crashes. Test a bounded variant asserting that with healthy workers and bounded queue size the outcome is recorded within ten simulation steps. A failing long trace should be reduced to its critical transitions before concluding the implementation violates the property.

### Limits and counterexamples

Testing three successful traces cannot prove `G p` for every possible interleaving. A liveness argument that ignores indefinite dependency failure conceals the very assumption on which progress depends.


### Deep dive: bridging model checking and implementation testing

Formal verification starts by choosing the world to model. A simplified job queue may represent each worker as Idle, Waiting, or Running, plus a shared lease owner. Its model assumes atomic transitions because the real datastore exposes some atomic operation. If that assumption is wrong, proof results cannot be carried to deployment. Begin by identifying observable operations: enqueue, acquire lease, renew lease, acknowledge completion, and time out. Decide whether clients can observe intermediate states or only committed states. Map every abstract operation to a concrete storage transaction or protocol interaction whose semantics are documented.

Safety and progress require distinct tests. A safety property forbids two workers from simultaneously owning a valid exclusive lease. It can be falsified by a finite trace with two owners. Liveness says accepted jobs eventually make progress, typically under fairness and availability assumptions. A finite execution ending in a queued job is not necessarily a counterexample to unbounded liveness; the job might complete later. For an automated test, use a bounded service-level claim such as a healthy, non-overloaded job completing within ten processing steps, and be clear that the bound is part of a toy model, not an operational service guarantee.

A finite-state model checker can search the reachable state graph with breadth-first search. Store a visited-state set and a predecessor edge for reconstructing the shortest path to a violated invariant. If three independent clients have three local states each, the raw local-state product has 27 tuples. Adding a shared lease owner with four possibilities can raise the raw count to 108, although many combinations may be unreachable. Partial-order reduction can combine independent interleavings that do not affect the property. Symmetry reduction treats interchangeable clients as equivalent representatives. Every reduction must preserve the property being checked, and the report must state whether completeness holds within the reduced model.

Counterexample traces are valuable because they suggest concrete fault-injection tests. If the model discovers that a lease expires before an owner learns its renewal failed, create a controlled schedule in which the old worker pauses, another worker acquires the lease, and the first resumes. The production implementation may require fencing tokens so that stale workers cannot commit writes after losing a lease. A mutex inside one process would not address a distributed lease race across machines. The test should inspect durable outputs and the fencing/version check, not just the log message claiming the worker stopped.

Hoare-style reasoning is useful for local state changes. For `i=0; while(i<n){i++}`, invariant `0<=i<=n` establishes partial correctness under n>=0, and the decreasing variant n-i establishes termination if integer arithmetic behaves as modeled. A more complex queue cannot be proved by copying this pattern unchanged. It needs separate invariants for durable queue membership, lease ownership, duplicate suppression, and state transitions. Proof obligations should be broken into small lemmas. A failed proof step often identifies either a missing assumption or a real transition that violates the intended property.

Refinement connects a concrete implementation to the abstract machine. The concrete system may perform several invisible operations before one abstract enqueue transition is deemed to occur. A correct refinement should preserve the externally observable behavior, while permitting implementation details such as logging and retry scheduling. For concurrent APIs, linearizability asks whether each operation can be placed at an instant between invocation and response consistent with real-time ordering. A stale read replica may violate a strong-read contract even if reservations themselves are atomic; separate each API's consistency promise.

The final claim should state precisely: a named invariant holds for all reachable states of a bounded model, under its transition rules and environment assumptions; a set of implementation tests reproduces known counterexample patterns; and unmodeled dependencies remain risks. That is much stronger and more honest than declaring a production distributed system “formally verified” because a simplified state diagram passed a checker.


### Unit synthesis: from bounded models to real implementations

A model checker can completely enumerate a finite transition system, but the word completely applies only to the constructed model. If the model omits message loss or clock skew, a successful safety proof does not cover them. A shortest counterexample can still be valuable when translated into a deterministic integration test. Write the mutual-exclusion invariant, identify a transition that could violate it, and map that abstract transition to an actual storage operation. For progress, distinguish eventual success under fairness assumptions from completion within a fixed bound. A finite incomplete trace cannot refute eventual success unless the model has a counterexample lasso or a stronger bounded claim. Include the code-level semantics of integer arithmetic, database transactions and worker lease renewal in the refinement discussion. The goal is a scoped verification argument whose assumptions are visible and whose experimental counterparts test what the abstract machine cannot represent.

## 6.2 Model Checking

### Core reasoning and definitions

Model checking explores a finite or finitely abstracted transition system to establish whether modeled properties hold in all reachable states. A model contains states, initial conditions, transitions, and atomic propositions. Exhaustive state-space search can find short counterexample traces for deadlocks, invariant violations, and protocol errors. State-space explosion is the main practical obstacle: multiplying clients, message queues, clocks, and retries rapidly increases combinations. Symmetry reduction, partial-order reduction, abstraction, and bounded checking can shrink the search but also affect which properties are proved under what assumptions. Model validity is essential; a correct verifier evaluating an inaccurate model says nothing reliable about the real system.

### Original investigative exercise

Construct a two-process mutual-exclusion model. Each process has Idle, Waiting, and Critical states, and an owner variable holds none, A, or B. Explore reachable states under valid lock transitions and assert that A and B are not both critical. Then introduce an unsafe transition that sets a process to Critical without claiming ownership and search for a shortest counterexample. Record number of explored states, visited transitions, and whether fairness constraints were used. Link the counterexample to an integration test that attempts the same interleaving against a real lock implementation.

### Limits and counterexamples

Proving a tiny idealized model free of deadlocks does not establish a production service cannot deadlock when network partitions, timeouts, or storage operations are absent from the model.


### Applied laboratory: proving a miniature job queue correct under a precise model

A background job queue receives a task, stores it durably, assigns it to a worker, and records either completion or an explicit terminal failure. Its requirements can be expressed as a small transition system. Let job states be New, Queued, Running, Completed, and Failed. The transition from New to Queued must create a durable queue record. A worker can move Queued to Running under an exclusive lease. On successful execution the job moves to Completed; on a recognized permanent error it moves to Failed; and on worker death a timed-out Running job can return to Queued. Not every transition should be reversible. A completed job should not be reexecuted merely because an acknowledgement packet was lost, unless the task's idempotency contract explicitly permits replay.

Formulate safety properties first. A job cannot be Completed before it has been accepted into durable storage. There must be at most one current lease holder for any job identifier. A completed output must correspond to the correct input and declared schema version. These are invariants over reachable committed states. Formulate liveness separately: if healthy workers continue processing and the queue remains within its operating capacity, every valid queued job eventually reaches a terminal outcome. This conditional statement needs fairness, bounded failures, and enough service capacity. Without assumptions, a permanent network partition can prevent progress forever, and a formal liveness assertion that ignored it would be misleading.

Write a toy model enumerator with a state tuple `(job_state, lease_owner, attempts)`. Limit attempts to three for tractability. Starting from New, generate valid transitions and collect reachable states using breadth-first search. Assert that Completed states have no active worker lease, and that no state grants the same job lease to two workers. Introduce a faulty transition that grants a lease without clearing the previous owner; the shortest counterexample is a path beginning with acquisition by one worker and erroneous acquisition by another. A model checker produces a trace in the model, not direct proof that a production system executes that same sequence. Turn the trace into an integration test with a controllable scheduler or lease-store fake and observe the real atomicity boundary.

Compare bounded testing and theorem proving. An integration suite with ten thousand random job sequences can miss a single rare interleaving. A complete model checker can prove the specified property over every state in a deliberately bounded model. A theorem proof may establish that an abstract `acquire` transition preserves uniqueness for all admissible jobs, but only if its precondition and state-update rules accurately represent production. A refinement argument must connect the concrete storage lock, transaction, retry, and timeout implementation to that abstract transition. Missing details such as clock skew or eventual consistency can invalidate a claim that an abstract proof covers the deployment.

Consider the temporal assertion `G(Completed -> WasQueued)` and a conditional progress assertion `G(Queued and Healthy -> F Terminal)`. The first expresses a safety history relationship; the second requires an interpretation of sustained health and fairness, not just a snapshot boolean. In a finite-trace simulator, a bounded alternative can check that a healthy job reaches a terminal state within ten steps. If the job has not finished by step nine, the run has not yet violated a ten-step deadline. If step eleven is reached, the bound is violated. This is not a general proof of unbounded liveness. The simulation deliberately exposes the difference between a pedagogical bounded property and a complete model of a distributed queue.

Prepare a refinement checklist: specify which concrete event corresponds to accepting a job, which storage operation constitutes lease acquisition, what a retry token means, which states are externally observable, and which transient steps may be ignored by the abstract machine. Add traceability from each invariant to model assertions and deployment tests. The output is not simply "verified": it is a scoped statement that a named property holds within a named model under explicit environmental assumptions, with counterexamples and unmodeled cases recorded separately.


## 6.3 Theorem Proving

### Core reasoning and definitions

Theorem proving establishes logical statements from axioms, definitions, and proof rules, often with computer assistance. A Hoare triple `{P} C {Q}` asserts that if command C starts in a state satisfying P and terminates, the resulting state satisfies Q; total correctness requires a separate termination argument. Interactive proof assistants allow a developer to define data types and discharge obligations with trusted kernels, while automated SMT solvers can handle many arithmetic and logical fragments. Every proof is conditional on the formal model and trusted computing base. A successful proof does not validate that the implemented parser, network interface, or compiler conforms to the model unless a correspondence argument connects them.

### Original investigative exercise

Verify a simple bounded counter loop. Use invariant `0<=i<=n` for code starting at i=0 and incrementing until i=n under precondition n>=0. Show initialization, preservation after an increment, and termination via decreasing variant n-i. Then analyze how integer overflow or a mistaken condition `i<=n` invalidates the argument. For a transfer operation, encode a conservation invariant and show atomic state transitions preserve the sum. Write test cases derived from failed proof obligations, including n=0 and n at the machine integer limit.

### Limits and counterexamples

A proof that assumes all arithmetic is unbounded mathematical integer arithmetic may not carry to fixed-width integers. Formal elegance is not a substitute for explicit implementation assumptions.

### How to interpret the interactive model: bounded progress

The bounded progress model varies a recorded completion step between zero and thirty while holding a declared deadline of ten steps. Completion at nine satisfies the deadline; completion at eleven violates it by one step. This is a finite bounded-response property, not a proof of eventual success over every infinite system trace. One must define when step counting begins, which events count as steps, and which worker health or scheduler fairness assumptions are active. A job that has not finished at step nine is not yet known to violate the ten-step bound, while finishing later does not erase an already missed guarantee. Real time-based objectives require measured time and operating conditions; simulation steps are not interchangeable with milliseconds.

## 6.4 Refinement

### Core reasoning and definitions

Refinement relates a concrete implementation to an abstract specification. The abstract system permits intended externally observable behavior; the concrete system introduces representations, caches, retries, protocol messages, and internal steps. A refinement relation maps concrete states to abstract states so that each externally visible concrete transition corresponds to a permitted abstract behavior, often allowing invisible stuttering steps. Refinement is stronger than checking one final output because it considers possible execution histories. Linearizability applies a related viewpoint to concurrent objects: operations should appear to take effect atomically at some point between their invocation and response while respecting real-time precedence. Choosing the right abstraction and observable boundary is central to meaningful correctness claims.

### Original investigative exercise

Specify an abstract inventory counter with atomic reserve-if-available. Implement it with database row locking and retries. For a one-item inventory, examine histories of two concurrent reservation requests; no valid abstract history can include two successes. Capture start and end times and committed results, then attempt to place a linearization point within each interval. A read replica displaying stale remaining stock might not violate the reserve contract but can violate a separately promised strongly consistent read. State which behavior is observable and what consistency level each method promises.

### Limits and counterexamples

If the abstract specification accidentally permits overselling, an implementation that oversells may formally refine it. The quality of the abstract requirements is as important as the proof technique.

### How to interpret the interactive model: state space

For n independent clients with three possible local states each, the raw Cartesian product has 3^n state tuples. Three clients give twenty-seven tuples; eight give 6,561. The reported transitions upper bound scales with n times the raw count and is merely a rough counting illustration. It is not the number of reachable transitions of any particular protocol. Constraints, initialization and guards can make many combinations unreachable, while adding a shared lease owner, message queues or clocks can expand the state space dramatically. Formal verification often employs reductions that must preserve the relevant property. The simulator makes growth visible but cannot decide deadlock, liveness, mutual exclusion or refinement on its own. A real model checker must represent transitions and search reachable states.

## Fully worked questions

### Worked problem 6.1: Temporal Properties

A healthy-job contract promises completion by step 10. A simulation records completion at step 11. Does it violate safety, liveness, or a bounded-response property?

**Define the property and assumptions.** A safety invariant forbids an invalid state such as two owners holding one exclusive job lease. Unbounded liveness promises eventual progress under assumptions. A bounded-response property adds a concrete deadline for progress.

**Compute or execute the reasoning.** Completion at step 11 violates the declared ten-step response bound while still demonstrating eventual completion in that run. It does not automatically violate the exclusive-lease safety invariant. If the contract never promised a deadline, the observation cannot by itself refute unbounded liveness.

**Interpret the conclusion and limitations.** Explicitly state when counting begins, what a step means, and which healthy-worker assumptions hold. Real elapsed time is different from abstract simulation steps. The bounded teaching model should not be presented as proof about all possible infinite traces.

### Worked problem 6.2: Model Checking

Three independent clients each have three local states. Count the raw global product states, then explain why a model checker might visit fewer.

**Define the property and assumptions.** For n independent clients with k possible states each, the Cartesian product count is k^n. Here n=3 and k=3, so there are 3*3*3 possible assignments, before adding shared locks, clocks, and queues.

**Compute or execute the reasoning.** The raw product contains 27 state tuples. The reachable set may be smaller because some transitions cannot occur from the initial state, some states violate modeled invariants and are excluded, or symmetric clients are reduced to representatives. Conversely, adding shared resource state multiplies the raw space.

**Interpret the conclusion and limitations.** A state-space count is not a correctness verdict. Record modeled transitions, initialization, fairness assumptions, and whether reduction preserves the property of interest. A counterexample is meaningful only if the modeled sequence maps to feasible implementation behavior.

### Worked problem 6.3: Theorem Proving

Prove partial correctness of `i=0; while(i<n){i++}` under precondition n>=0 using an invariant. What extra argument establishes termination?

**Define the property and assumptions.** Choose invariant 0<=i<=n. At initialization i=0 and n>=0, so the invariant holds. If the loop guard is true, i<n and the body increments i to i+1<=n while preserving nonnegativity.

**Compute or execute the reasoning.** When the loop exits, the invariant combined with not(i<n) yields i=n, which establishes the desired postcondition if execution terminates. To prove termination, use variant n-i: it is a nonnegative integer while the guard is true and decreases by one on each iteration.

**Interpret the conclusion and limitations.** This argument assumes mathematical integers or checked arithmetic with representable n. For fixed-width machine integers, overflow and language semantics must be considered. A proof of this tiny loop says nothing about concurrent mutations of n unless those are ruled out in the model.

