# Data Structures — Unit 8: Implementation analysis

**DRAFT — length threshold and independent review outstanding.**

## 8.1 Iterator Design

### Iterator Design

An iterator provides a controlled traversal protocol. The interface must define validity, end-of-sequence behavior, and what mutations invalidate an existing cursor.

## 8.2 Memory Management

### Memory Management

Allocation patterns, object headers, cache locality, and pointer stability affect performance. Safety-critical implementations must also reason about ownership, aliasing, leaks, and use-after-free.

## 8.3 Correctness Tests

### Correctness Tests

Property-based tests can compare a complex implementation to a simple reference model. Invariants, boundary cases, differential tests, and deliberately adversarial sequences reveal bugs that example-only tests miss.

## 8.4 Workload Benchmarks

### Workload Benchmarks

Benchmark conclusions require representative inputs, controlled environments, repeat measurements, and explicit separation of setup cost from operation cost. Always verify correctness before measuring speed.

### Extended design study: selecting and measuring an implementation

Suppose two implementations of a collection satisfy the same external interface, but one uses an array and the other uses linked nodes. A valid comparison starts with a correctness oracle: generate operations such as insert, remove, and lookup, apply them to both implementations and to a simple reference, and compare public outputs and final sequences. A benchmark of an incorrect implementation is meaningless. Furthermore, all test inputs must obey stated preconditions; silently feeding invalid indices to one implementation while filtering them for the other invalidates the comparison.

Iterator behavior must be specified separately from container semantics. A raw pointer into a resizable array may become invalid after reallocation; a position index might remain usable but refer to a different element after insertion. A fail-fast iterator can track a modification generation and reject traversal after a structural mutation. Such behavior is an API choice, not a guarantee that every language or collection provides. Tests should include mutation before iteration, during iteration, and after iteration ends, together with empty and singleton containers. This keeps correctness distinct from an implementation-specific notion of reference stability.

Memory measurements are also more complicated than multiplying element count by element size. Packed arrays may hold numeric values contiguously, whereas node chains carry pointers, object headers, and allocator metadata. Alignment and internal capacity slack affect allocation totals. A high-level language's list may store references to separate objects, not the raw machine integers a student imagines. A careful report states which runtime, element type, allocation scope, and accounting method were measured. Peak memory during resize may substantially exceed steady-state storage, because old and new arrays temporarily coexist.

Performance benchmarks require reproducibility. Define the dataset, operation mix, seed, initialization strategy, and measurement boundary. Time repeated operations rather than one operation near timer resolution, warm up runtimes where appropriate, and report multiple trials. Separate data construction from lookup if comparing lookup. Compare worst-case or adversarial behavior in addition to average workloads. Distinguish wall-clock results, number of comparisons, allocations, and cache misses: they are different metrics that illuminate different bottlenecks. Final implementation selection should account for reliability, maintainability, and actual product requirements, not only the smallest single benchmark number.

## Worked problem 8.1

An iterator over a resizable array stores a raw pointer to its first element. What can happen after an append triggers reallocation?

**Define the data and method**
A resize may allocate a new block and copy the current elements, then release the old block. The iterator still points into the original location and no longer identifies the live array elements.

**Derive and interpret the result**
In a language with invalidatable raw pointers, dereferencing the old iterator may be unsafe. An API should specify invalidation rules or provide stable-index/version-based alternatives.

## Worked problem 8.2

Compare storing 1,000 32-bit values in an exactly sized packed array with a node chain having one 64-bit next pointer per value. Ignore other metadata.

**Define the data and method**
The packed numeric payload is 1000*4=4000 bytes. A node chain needs at least 1000*(4+8)=12000 bytes before alignment, headers, or allocator overhead.

**Derive and interpret the result**
The lower bounds are 4,000 and 12,000 bytes. Real node-chain usage may be higher; the computation illustrates why O(n) structures can differ substantially in constants.

## Worked problem 8.3

You benchmark list lookup against dictionary lookup. How should you make a fair correctness-first comparison for n=100,1000,10000?

**Define the data and method**
Generate deterministic keys and an equal mix of present and absent queries, then check both implementations against the same expected outcomes. Separate build time from lookup time; warm up the environment and repeat measurements.

**Derive and interpret the result**
Report a distribution of timings and operation counts, not a single arbitrary run. Hash maps have average-case behavior under assumptions and worst-case collision behavior that timing alone may not expose.


### Applied investigation: Space costs and iterator invalidation

An array of n 32-bit values uses 4n bytes for its values, before container metadata. A linked representation may require at least 4n bytes of values plus n pointers, alignment and allocation overhead. A simplified 12n estimate assumes eight-byte links but omits allocator and object headers. It is a comparative lower-bound model, not a RAM profiler. Cache locality may matter more to observed performance than asymptotic storage notation.

A versioned iterator stores an expected collection generation number. When a structural mutation changes that generation, continuing with the old iterator is rejected rather than producing an unpredictable traversal. Actual languages and containers vary: some iterators remain valid after appending, while others invalidate only on reallocation. Tests must match the declared contract, including mutations that replace a value without changing structure. A basic counter demonstration is not itself a concurrency safety guarantee.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Testing data structures rather than example outputs

A public container interface is a collection of contracts. For a set, inserting an already present item should not increase size. For a map, updating an existing key changes its associated value without changing the number of keys. For a queue, removal returns the oldest still-present entry. These contracts can be expressed as properties across many generated operation sequences rather than tested only with a fixed sequence written by the same developer.

A reference implementation is particularly useful. Compare a custom stack to a plain language list using append and pop operations; compare a custom hash map to a standard dictionary on a stream of distinct and repeated keys; compare a custom priority queue to a separately sorted multiset. This is differential testing, but it is only sound if the reference and custom implementations share the same specification. A language's built-in map may have different iteration-order or missing-key behavior, so define the comparison domain carefully.

Consider a hash map with the operations insert(A,1), insert(B,2), insert(A,3), delete(B), lookup(A). A map contract predicts size one and lookup(A)=3. A weaker test that merely checks that lookup(A) returns some non-null result would miss incorrect replacement behavior. For a heap, after each insertion or extraction, test every parent-child relationship in the current array and compare the extracted sequence with an independently sorted copy. These checks detect internal corruption before a dramatic user-facing failure occurs.

Property-based testing benefits from shrinking. If a random sequence of a thousand actions produces a failure, try deleting actions while keeping the failure reproducible. A minimal trace such as insert collision X, insert collision Y, delete X, lookup Y may expose a tombstone bug far more clearly than the original workload. Record the random seed and generated trace so that regression tests can reproduce the defect. Random testing without reproducibility is weaker evidence.

Space and performance tests require a defensible experiment. Warm up a managed runtime where appropriate, avoid benchmarking I/O together with an in-memory operation, vary collection sizes across orders of magnitude, and report distributions rather than only one timing. A complexity model predicts trends, not absolute wall-clock time; cache locality, allocation costs and branch prediction can dominate at small n. If measured results contradict a simple big-O expectation, investigate the workload and constants before concluding the theory is wrong.

Thread safety is another independent dimension. A collection can have correct sequential operations and fail when threads interleave. A check-then-act sequence can observe an empty queue and then race with another consumer. Correct concurrent containers define linearization points or other explicit consistency semantics, and their tests must explore scheduling interleavings. Finally, document ownership: is a returned iterator stable after insertion, and can a caller retain references into the internal buffer? These API guarantees determine whether a theoretically efficient data structure is safe to use in a real program.


### A practical verification strategy for mutable collections

### Model-based tests

The strongest unit tests for a container compare a small implementation under test with an independently implemented abstract model. For a mutable map, the model can be a straightforward list of unique key-value pairs with linear search, even when the implementation under test uses hashing. Using a deliberately slower model makes it easier to reason about correctness. Generate valid operations from a defined grammar: insert, update, lookup, delete and clear. After each operation, compare visible key sets and values and inspect invariants that external callers cannot see. Include an operation counter and a stored seed so every failure is reproducible.

For a queue, a reference list with removal at index zero is acceptable for a correctness oracle even if it is slow. For a heap, a sorted reference multiset checks extracted order; a separate parent-child check verifies internal representation. For a balanced tree, inorder traversal should equal sorted keys, subtree-size fields should match recomputed sizes, and each stated balance condition should hold. No single oracle covers everything: an implementation can accidentally output sorted keys while still containing bad parent pointers that will break a later deletion.

### Structured edge-case matrix

Every public operation should be tested at emptiness, singleton size, just below capacity, exactly at capacity, and after a grow or shrink transition if the representation has those states. For indexed operations also test negative indices, the last valid index and the first invalid index. For hash maps test repeated keys and collisions; for trees test monotone insertion, duplicates under policy, all three deletion shapes and root removal. For iterators test mutation before the first step, halfway through iteration and after apparent exhaustion. These are meaningful equivalence classes, not arbitrary large input samples.

### State-machine fuzzing and shrinking

A stateful test generator records both the input operation sequence and the expected abstract state. A bug may surface only after twenty otherwise benign operations, so shrinking is essential. Shrink by deleting operations while preserving the failure, simplifying keys toward small integers and minimizing the data structure size. A four-operation trace that reveals a collision-deletion error is easier to debug and to retain permanently than a random thousand-step log. Treat every discovered minimal trace as a new deterministic regression test.

### Complexity evidence without misleading graphs

Operation counts and wall-clock timings answer different questions. Instrument the number of comparisons, pointer hops, allocations and elements copied. These counts should match mathematical expectations for controlled inputs: finding the minimum of n known entries by a full scan takes n−1 comparisons after initialization; a traversal to one-based position n in a linked list takes n−1 next-pointer hops. In contrast, measurements of nanoseconds depend on CPU scheduling, garbage collection, JIT compilation, caching and data representation. Benchmark suites should separate setup time from measured operations, repeat runs and report dispersion.

A useful benchmark contrasts contiguous arrays with linked lists under sequential iteration and random indexed lookup. Keep the logical number of elements and payload size comparable and distinguish the cost of allocating the structures from the cost of accessing them. Do not claim that an asymptotically favorable complexity guarantees lower latency for all n; a tree lookup with fewer theoretical operations may still lose to a short linear scan that uses contiguous memory and predictable branches.

### Concurrency and lifecycle

A data structure that is correct under sequential calls is not necessarily safe under concurrent access. Consider two threads both reading the same queue head and attempting removal. Without coordination, they may return the same item or corrupt pointers. Locks, atomic instructions and memory-ordering rules can ensure appropriate synchronization, but correctness depends on a specified consistency model. A linearizable queue should make each completed operation appear to occur at a single point between invocation and response. A lock-free algorithm additionally needs rigorous progress and reclamation arguments; using atomic pointers alone does not establish memory safety.

### Review checklist for a finished educational library

Review each documented operation against its preconditions, postconditions and exceptional cases. Verify source code syntax, data-structure invariants, counterexamples and mathematical costs independently. Exercise UI simulations at their minimum and maximum allowed inputs, change controls repeatedly and confirm Reset restores the defined initial state. Inspect mobile rendering and keyboard access, including text labels for numerical inputs. Finally, mark any synthetic operation count as synthetic; it should never be presented as a measurement from production hardware or a universal guarantee. That separation between model, demonstration and empirical result is central to credible technical teaching.


## Additional original authored teaching sections

# From a plausible implementation to a trustworthy data structure

A collection can pass every demonstration and still be wrong. The reason is that demos typically show a few successful operations, while correctness concerns all valid sequences of operations. An efficient verification strategy begins with a reference model that is deliberately simple. For a map, the model could be a sorted list of key–value pairs; for a priority queue, a list sorted after each update; for a disjoint-set structure, an explicit array labeling the group of each element. Such models may be far slower than optimized implementations, but they are easier to reason about and are entirely adequate for short randomized traces.

A property-based test generates operations rather than single input–output examples. For a stack, generate pushes and pops while preventing invalid pops unless empty-pop behavior is under test. Apply the same operations to the candidate implementation and a list-based reference. After every operation, check returned values, size, and the complete observable sequence where an iterator exists. If a failure occurs, reduce the trace to a minimal reproducing sequence. A sequence such as push A, push B, pop, push C, pop may expose an index bug that an isolated push or pop test misses.

Metamorphic testing provides useful invariants even without an independent oracle for a complicated output. If adding a new key to a map is followed by reading that key, the retrieved value should match the insertion unless a documented replacement rule intervenes. In a min-heap, adding a value lower than every existing value should make it the next removed minimum. In an undirected graph, adding an isolated vertex should not change the connectivity relationship among existing vertices. In a trie, inserting a longer word should not make an already present shorter word disappear. These transformations generate many coherent checks from a few algebraic properties.

An exact invariant checker can inspect internal structure at the end of each operation. For a binary heap, assert that every parent key is no larger than its children. For a search tree, recursively validate global key bounds and any balance metadata. For a doubly linked list, walk forward and backward and check that each next link has the corresponding previous link. For a hash table, confirm that every stored key can be located by the public lookup algorithm and that the number of distinct live keys matches the reported size. Internal checks do not replace public behavior checks: an object can be internally consistent yet implement the wrong abstract interface.

Tests should be designed around state transitions that are easy to overlook. A resize changes backing storage and can expose stale pointers. A delete introduces holes and tombstones. A rotation rearranges multiple tree links. A root deletion changes the entry point to an entire structure. An iterator used after mutation can expose invalidation assumptions. Construct short adversarial traces around these transitions rather than distributing tests only across common steady-state reads. Edge cases are not special decorations to add after implementation; they are where representation invariants are most likely to be violated.

# Measuring performance without confusing it with validity

Once a structure is correct under a reasonable test suite, measure its efficiency. Timing must not include unrelated work such as generating random inputs or printing results unless that overhead is part of the real application. Run enough repetitions to distinguish systematic effects from random fluctuation and report the distribution of runtimes. Median throughput, high-percentile latency, and maximum observed pause can lead to different engineering choices. When measuring a resizable array, a rare capacity expansion may have little effect on average throughput but still cause a noticeable latency spike.

Benchmark at several input sizes and compare the shape of growth, not merely raw numbers. If a routine performs n squared pair comparisons, doubling n can roughly quadruple the dominant operation count; if it sorts n elements using an efficient comparison sort, the growth is closer to n log n. Hardware caches and memory allocation can distort small tests, so asymptotic behavior should be assessed over a useful size range. Test workloads must be representative: a search tree that receives uniformly random insertions can look balanced by chance, whereas ordered insertion into an unbalanced tree reveals linear-height behavior.

Memory profiling should separate logical payload bytes from representation overhead. Compare a vector that reserves twice its occupied size with one that reserves exactly enough; the former spends more memory but may allocate less frequently during growth. A linked list's allocation overhead may exceed its pointer overhead, depending on allocator and language runtime. Persistent trees can share nodes across versions, making a naïve sum of each version's logical size substantially overestimate physical storage. Report retained memory after deletions and old-version release, not only peak memory during construction.

Concurrency tests require a different standard from sequential tests. Operations must have a defined consistency contract before a race can be labeled a bug. For a linearizable concurrent queue, each enqueue and dequeue should appear to occur at some instant between its invocation and completion, preserving FIFO semantics under one valid ordering of overlapping operations. Merely obtaining the right number of items after a stress test does not prove that no duplicate removal occurred during the run. Short histories can sometimes be checked exhaustively against the sequential specification; deterministic schedule injection helps reproduce subtle interleavings.

An implementation review should include resource lifetime. A custom structure may maintain correct pointers yet leak nodes after deletion, hold references to large objects in unused array slots, or run a callback while retaining a lock that leads to deadlock. The structure should document which operations may allocate, which may throw exceptions, which invalidate iterators, and which are safe under concurrent access. These are observable engineering properties, even if introductory complexity tables omit them. A formally correct lookup algorithm cannot compensate for undefined lifetime behavior in its surrounding API.

For the final assessment, treat evidence as a series of distinct claims. A word count proves that a manuscript contains text, not that its explanations are original or correct. A syntax check proves that code parses, not that it implements the intended model. Unit tests verify the particular behaviors they exercise, not every state transition. A browser test proves behavior in the browser and viewport actually tested, not universal accessibility. Independent mathematical checks, property-based oracles, responsive interface checks, and academic editorial review complement rather than replace one another. This distinction makes a textbook itself a responsible demonstration of the engineering standards it teaches.
