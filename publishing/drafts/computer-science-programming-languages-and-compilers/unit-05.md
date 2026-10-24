# Unit 5: Runtime systems

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Memory Layouts
**Memory Layouts: conceptual explanation**

Runtime layout divides work among memory regions, but an implementation should not assume that a particular language object always occupies a familiar region. A typical native call frame contains return information, saved registers, spill slots and local temporaries, while heap objects outlive a particular call and global storage may contain static objects. A compiler must obey the target ABI’s stack alignment and calling convention; a wrong alignment can break foreign calls even when the compiler's own tests appear to run. Escaping variables captured by closures cannot simply become invalid when their declaring function returns.

Use a frame layout exercise. Suppose a target requires 16-byte stack alignment and a function needs 24 bytes of local storage plus 8 bytes of saved state; the total is already 32 bytes, but adding one extra 8-byte spill may require rounding to 48 to preserve alignment. A real ABI’s pre-call and entry alignment rules must be applied rather than assuming all architectures share this convention. Distinguish the logical stack discipline from implementation: tail-call optimization may reuse frames, async functions may store activation records on the heap, and green-thread runtimes may grow or move stacks. Correctness tests include deep recursion, foreign function calls, exceptions, and closure escape after the creating call has finished.

### Design investigation: frame layout with escaping state
Define a procedure with two integer parameters, 24 bytes of locals, one saved register and one spilled temporary under a hypothetical ABI requiring 16-byte stack alignment. Compute the required frame size carefully and describe which stack-pointer state is aligned at call boundaries. Avoid asserting one exact layout for all real ABIs. Add a returned closure capturing a local variable; show why deallocating the entire call frame cannot also destroy the captured cell. Compare allocating a closure environment on the heap with copying an immutable value into a separate object. Run a recursion test deep enough to exercise multiple frames and an exception that unwinds through two calls. Verify that saved registers and root references are still valid. A function’s correctness depends on both logical semantics and physical boundary protocol.

## Garbage Collection
**Garbage Collection: conceptual explanation**

Tracing garbage collection begins with a defined root set: registers, active stack slots, globals or runtime-managed handles. The collector walks the object graph reachable from those roots and reclaims unreachable objects under the language’s memory-safety assumptions. If root A points to B and B points to C, C must remain live even without a direct root reference. Mark-sweep marks reachable objects and sweeps the rest, while copying collectors move live objects into a new region and update references. Generational collectors exploit empirical allocation patterns, but their write barriers must record old-to-young references to avoid losing live objects.

Reference counting is conceptually different: increment counts on new strong references, decrement on release, and reclaim when a count becomes zero. Cycles such as A pointing to B and B pointing back to A are not recovered by basic reference counting without an additional strategy. Liveness is not semantic usefulness: an unused object may remain reachable from a cache, so the collector cannot know that the application no longer cares about it. Investigate the difference between a memory leak caused by accidental reachability and one caused by an incorrect native allocation with no release. A timing trace should separately report allocation rate, pause duration, throughput and retained heap size rather than advertising a single unexplained “GC speed” metric.

### Design investigation: reachable is not the same as useful
Draw objects A,B,C,D,E with edges A->B, B->C, D->E and E->D. If the only root points to A, a correct tracing collector retains A,B,C and reclaims D,E. If the root changes to D, it retains D,E and may reclaim A,B,C. Basic reference counting would not reclaim the isolated D/E cycle when external references disappear. Now add a global cache pointing to A even though the application never reads A again: the collector must keep it because it remains reachable, illustrating retention caused by application references. Track root set at an exception handler and a foreign callback, not just ordinary stack locals. Build an independent DFS reachability oracle and compare the collector's survivor list on randomly generated directed object graphs. State whether the toy collector models weak references and finalizers; if not, exclude them instead of pretending they work.

## Closures
**Closures: conceptual explanation**

A closure pairs executable code with an environment containing captured bindings. Consider `makeCounter()` creating local c=0 and returning `increment() { c=c+1; return c }`. Two calls to one returned closure should yield 1 then 2, but a separately created closure should normally start at 1. To implement this, determine whether the closure holds a mutable cell or a copied scalar. Copying c at closure creation without mutation semantics can accidentally make repeated calls return 1 forever; sharing one global cell can make separate counters interfere.

Escape analysis identifies storage whose lifetime must exceed the current stack frame. Some closures can be allocated on the stack when the compiler proves that they never escape; others require heap-backed environments. Capturing immutable values, mutable variables, references to external objects, and loop variables may have different rules. In concurrent contexts the environment may need synchronization or prohibit simultaneous mutation. Build an interpreter environment model with parent pointers, then write a source-level test for nested closures shadowing the same identifier. Draw the object graph after the creating function returns: code pointer, captured environment, mutable cell, and any transitive objects. The compiler's allocation optimization is sound only if observable closure behavior is preserved.

### Design investigation: mutable closure identities
Construct two counters from `makeCounter`, one stored in a and one in b. Call a twice, b once, and a again; expected sequence is 1,2,1,3 under separate mutable environments. Dump closure object identifiers and captured cell addresses. If both counters share one cell, the sequence might become 1,2,3,4, demonstrating a capture bug. Add a closure that reads a nested binding with the same source spelling as a global binding and verify that lexical identity wins. Free the creating function’s stack frame before invoking the closure and check that captured storage remains valid. In a moving garbage collector, ensure the closure environment references are updated or represented through handles. A test that only calls the closure before its creator returns does not establish escape correctness. Explain the lifetime invariant that makes this design work.

## Exception Handling
**Exception Handling: conceptual explanation**

Exceptions introduce nonlocal control flow. A `throw` skips ordinary statements until a matching handler is found; cleanup rules must specify when deferred actions, destructors or finally blocks execute. If a function acquires a lock, allocates memory and then fails, the runtime must not silently abandon cleanup. The semantics also needs to decide what happens if cleanup itself raises another exception. A simple compiler can lower try/catch to explicit landing-pad blocks, unwind tables or a runtime search strategy, depending on the target ABI and supported operations.

Observe code `try { open(); f(); } finally { close(); }`. Whether `f` returns or throws, `close` should run according to the language contract, although failure of open may require a guard. Exception unwinding interacts with register state, debug information, foreign frames and garbage collector roots. Comparing exceptional and normal CFG edges prevents optimizations from moving side effects past an operation that might throw. Asynchronous cancellation is not necessarily a normal exception; code may need cancellation-safe critical regions. Test nested handlers, rethrow, partially initialized objects, cleanup failure, return from finally if permitted, and cross-language exception boundaries. Make a clear distinction between tested semantics and the host platform’s accidental behavior.

### Design investigation: unwinding plus resources
Write a function that opens a resource, allocates an object and calls a function that throws. Use a finally block or language-specific defer to release the resource according to the language contract. Instrument a log: Open, Allocate, Call, Throw, Unwind, Close, Handle. Confirm that Close occurs once even when control exits through the exception. Introduce a second exception during cleanup and define which error is observed; languages differ, so the policy must come from the source semantics. Include a nested handler that catches only one exception type and permits another to propagate. Test that garbage collector roots for the exception payload remain live while unwinding frames. An optimizer must not move an effectful operation after a potentially throwing call merely because the normal-return path would still produce the same value.

## Integrated Case Study and Model Limitations
A closure returned from `makeCounter` captures a mutable count variable. If the variable's storage lived only on the caller stack, the returned closure could reference invalid memory. An implementation may use heap-allocated environments or escape analysis to retain captured storage. In the same program, garbage collection should reclaim unreachable closures but must not reclaim an object still reachable through a live captured reference. A reference-counting collector needs another mechanism to break cycles between objects. Describe how an exception thrown during counter initialization affects cleanup and observable state.

### Laboratory: implement closure capture and tracing collection together

Extend a small interpreted language with nested functions, allocation of pair objects, mutation and a `makeCounter` function. The function should return a closure whose captured variable remains valid after the surrounding call has returned. Represent a closure as `(code, environment)` where the environment contains cells for captured mutable values. Test one closure twice and two separately created closures alternately. Expected behavior depends on the language specification: each counter has its own cell unless an explicit shared object is passed. If every call returns one, a snapshot copy may be used in place of mutable capture. If different counters interfere, an unintended shared global might have been introduced.

Build a heap graph from nodes with identifiers and reference fields. Designate roots from global variables, interpreter operand stack and active frames. Mark all nodes reachable from roots; sweep those not marked. For a graph A -> B -> C and isolated cycle D -> E -> D, roots containing A should keep A, B and C and permit reclaiming D and E. Now remove A from the root set: A, B and C become reclaimable too, provided no other roots reference them. A tracing collector is not allowed to reclaim an object because the source compiler considers its variable dead if a live runtime handle may still exist.

Add an explicit foreign-handle table to the root set. Suppose a native library stores a pointer to an object that the language VM wishes to move during compacting collection. Without a stable handle or pinning protocol the native pointer can become invalid even though the object remains reachable. Decide on one supported policy and test it. Basic mark-sweep with nonmoving objects is easier as a first implementation; generational and copying designs introduce forwarding pointers, write barriers and remembered sets. Implement one policy fully before adding optimizations with complex invariants.

Model exceptions and stack unwinding. Make a function allocate a pair, register a cleanup callback, then throw. The handler should observe the exception; cleanup should run according to the language contract; unreachable objects should be collected later rather than leaked through a stale frame root. If the cleanup also throws, define which exception is delivered. An exception must not cause a heap object to be collected while it remains referenced from the exception payload or handler environment. Instrument root snapshots at every allocation and handler transition.

Assess performance with simulated allocation traces rather than unsupported claims about real runtimes. Record total allocations, bytes retained after collection, time or operation count spent marking, and peak heap usage. A small cyclic graph can show why reference counting alone may fail; it does not establish that tracing is better on every workload. Validate collector behavior against a simple graph reachability implementation written independently. Your final result should demonstrate correctness on escaped closures, aliasing, cycles, nested exceptions and foreign roots before discussing tuning.

### Failure clinic: a disappearing closure under garbage collection

A runtime uses a conservative stack scan as its only root discovery mechanism and moves objects during compaction. A native callback keeps a raw pointer to a closure environment while the original language function has returned. The callback invokes the closure later, and occasionally the pointer refers to moved or freed storage. The bug depends on allocation history, so ordinary unit tests pass inconsistently. Diagnose the ownership and root protocol. A foreign-held pointer must either be stable through a runtime handle, pinned according to the collector's rules, or updated when the object moves. Conservatively scanning currently active stack frames does not discover an arbitrary pointer retained in native library state.

Construct a controlled reproduction. Create a closure capturing a mutable counter; hand an invocation handle to the mock foreign library; drop ordinary language references; force repeated allocations and collection; then invoke the callback through the handle. The expected counter sequence must continue rather than resetting or crashing. Record handle creation, protection, release and collection cycles. Add a negative test that releases the handle and confirms the runtime no longer promises the callback remains valid; the foreign library must not call it after the documented release event.

A related leak arises when the root table never removes handles after callbacks are unregistered. Tracing collection properly retains every reachable object, so the heap grows even though the application no longer needs those closures. Distinguish incorrect garbage collection from incorrect application reachability. Capture a heap graph and count roots across registration and deregistration operations. A heap snapshot showing objects retained by a global table can reveal a leak that simply increasing the collection frequency cannot fix.

Finally test exception unwinding. A callback raises a language exception during a native call that has no compatible unwind ABI. The exception must be translated into a supported error result or routed through an explicitly tested callback boundary. Do not allow arbitrary language exceptions to cross foreign frames on the assumption that every platform uses the same unwinding format. The runtime’s correctness contract includes allocation, capture lifetime, root management, cleanup, exceptions and foreign ownership, all of which interact in this one apparently simple callback scenario.

### Worked comparative study: lifetime, aliasing and exception semantics

In a simple interpreter, values may appear to be numbers stored in a dictionary. Real runtimes must also represent heap objects, closures, calls, stack frames, exceptions and foreign references. A variable binding and an object lifetime are different concepts. Removing a local variable from scope does not necessarily make its referenced object unreachable: a returned closure, global cache or foreign handle may still refer to it. Conversely, a programmer may still consider an object logically useful even though no runtime root can reach it; the collector must follow reachability rules, not human intention.

Compare two memory management models. In reference counting, assignment of an additional strong reference increases a count, and releasing a reference decreases it. A simple cycle can preserve positive counts after external references vanish. Tracing collection instead walks from roots and can reclaim unreachable cycles. Each has implementation costs and edge cases; hybrid runtimes exist. Even tracing collection cannot reclaim an object retained by an accidental global reference. Record the root set and graph before claiming a particular algorithm has a leak or correctness defect.

Exceptions connect memory to control flow. When an operation throws, frames may unwind without executing ordinary return statements. Cleanup constructs must restore resource invariants and release locks. The runtime still needs correct roots for any exception object and captured environment used by handlers. Optimizations that eliminate a seemingly dead local may be safe at the source level but must leave appropriate roots for the runtime at safepoints. Native interfaces complicate this because the runtime may not be able to inspect or relocate arbitrary foreign pointers.

Construct a combined test. Create a closure capturing a heap object, register it as a callback, leave the creating stack frame, force collection, invoke the callback, and then throw an exception from its body. Check that the captured object survives, cleanup runs according to policy, the exception is reported through a supported boundary, and release of the foreign handle eventually permits collection. Document any features not supported by the small runtime. This case illustrates why the semantics of closures, garbage collection, foreign ownership and unwinding cannot be verified completely in isolation.

### Unit review: audit all roots and cleanup paths

Draw a heap graph before and after returning a closure and before and after an exception unwinds the stack. Show the runtime roots that keep a captured environment alive. Introduce a foreign callback handle and decide whether it is pinned, copied or represented by a movable collector-aware handle. A collector can reclaim only objects unreachable from the actual root set; an unexpected global reference can keep otherwise useless objects alive indefinitely. Check that resource cleanup executes on both normal and exceptional paths and that exceptions do not cross incompatible native unwind frames without a defined protocol. If the small simulator omits finalizers, weak references or concurrent collection, record those omissions. Their complexity is not removed by drawing a simpler object graph.

### Worked question: Trace reachable objects
In a heap graph A->B->C with root A and isolated cycle D<->E, identify what mark-sweep may reclaim.

**Set up definitions and premises**
Starting from root A, mark A, then follow A->B and B->C to mark B and C. Neither D nor E is reachable from any root under the specified graph.

**Derive the result**
Sweep reclaims unmarked D and E. A reference counter without cycle detection might keep D/E allocated after external references disappear because they still reference each other.

**Validate limits and interpretation**
If a foreign handle points to D, it must be treated as an additional root; D and E would then be live. The collector is correct relative to its actual roots, not to a guessed application intention.

**Answer:** Retain A,B,C; reclaim D,E only when no root, including foreign roots, reaches them.

### Worked question: Evaluate separate counters
Two closures are produced by separate calls to makeCounter and each captures its own mutable integer starting at zero. Find outputs of a(),a(),b(),a().

**Set up definitions and premises**
Closure a owns cell ca=0 and closure b owns cb=0. Calling a increments ca to one and returns one, while the second call increments it to two and returns two.

**Derive the result**
Calling b increments cb to one without changing ca. Calling a again increments ca from two to three. Keeping captured cells distinct is necessary for these observations.

**Validate limits and interpretation**
A runtime storing c only in the creation frame can use freed storage after return; a runtime using one shared global cell makes the third call return three instead of one. Both designs violate the stated separate-closure semantics.

**Answer:** Outputs 1,2,1,3 under independent captured mutable environments.

### Worked question: Exception cleanup trace
A function opens a resource, calls a function that throws, and has a finally cleanup. Describe the mandatory event order under ordinary finally semantics.

**Set up definitions and premises**
The function opens the resource successfully and enters the protected region. The nested call throws; ordinary instructions after the call are not executed.

**Derive the result**
The unwinder invokes the finally cleanup before the exception is delivered to the surrounding handler. Record Open, Call, Throw, Cleanup, Handle, with exactly one cleanup if the contract specifies that outcome.

**Validate limits and interpretation**
A cleanup that itself throws creates another semantic question: which exception is propagated or suppressed? Test the selected language policy. Cross-FFI unwinding must not be assumed legal across incompatible runtimes.

**Answer:** Cleanup precedes outer handling after the throw; secondary cleanup failure is language-specific.
