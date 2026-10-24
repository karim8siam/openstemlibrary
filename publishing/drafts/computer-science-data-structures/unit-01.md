# Data Structures — Unit 1: Foundations

**DRAFT — length threshold and independent review outstanding.**

## 1.1 Abstract Data Types

### Abstract Data Types

An abstract data type specifies operations and their observable behavior independently of the representation. Stack and queue operations are defined through preconditions, postconditions, and state transitions. Implementations may use arrays or nodes while satisfying the same interface contract.

**Practical interpretation.** The important engineering decision is which public operation must be efficient, what invariant protects correctness, and what assumptions justify the stated bound. A representation is not correct merely because its simple cases work: invalid inputs, empty instances, repeated values, and failures during mutation must be specified.

**Verification in this unit.** Use the worked problems below to trace state transitions and check results independently. For implementations, compare returned values against a reference model and inspect the full state after every mutation; do not rely only on timing.


## 1.2 Representation Invariants

### Representation Invariants

A representation invariant is a logical property every valid instance must satisfy. Typical requirements include a correct element count, acyclic links, and valid array indices. Correct mutating operations preserve the invariant from a valid starting state.

## 1.3 Complexity

### Complexity

Computational complexity bounds the growth of resource use. Big-O describes an asymptotic upper bound, while Θ describes matching upper and lower bounds. Worst-case, expected, and amortized claims must not be confused.

## 1.4 Memory Models

### Memory Models

Arrays store elements in contiguous locations, whereas pointer-linked structures connect separately allocated nodes. Cache locality, alignment, garbage collection, and reference stability affect practical behavior beyond asymptotic memory bounds.

### Extended design study: a bounded event history

A logging tool may offer an interface that stores only the most recent k records. This creates a useful example of an abstract data type. The visible contract is not "an array of size k"; it is a sequence of records ordered by arrival time, in which appending one record evicts the oldest record when the bound is exceeded. An implementation might use a circular array or a linked chain. Both must preserve the same sequence after every public operation. If the interface also supports reading the ith oldest record, however, an array-backed ring has an important advantage: its logical index can be mapped directly to a physical slot using modulo arithmetic, while a basic linked structure must traverse successive references.

State invariants make this comparison precise. For a ring of capacity k, maintain an integer size in [0,k] and head in [0,k-1]. The ith oldest record is at physical position (head+i) modulo k. Appending to a nonfull ring uses position (head+size) modulo k, then increases size. Appending to a full ring overwrites the oldest record and advances head by one. Both transitions preserve the bounds. A correct black-box test can build a reference sequence with an ordinary list: append to it, discard its first item if the length exceeds k, and compare the visible sequences after every operation.

The time bound depends on the operation and the representation. A ring offers O(1) access by logical index and O(1) overwrite under the RAM model; an ordinary list that discards its first element by shifting can take O(k) per overflow event. A linked chain with direct head and tail pointers gives O(1) append and eviction but not random access. None of these claims quantifies actual latency in a particular garbage-collected runtime, where allocation, indirection, and cache behavior can matter. Complexity is best interpreted as a model of scaling, with measurements used to assess constants only after correctness is established.

A fixed-size event history must also define exceptional cases. Capacity zero can mean "store nothing," but the implementation must treat that as a deliberate case rather than calculating modulo zero. The application may allow a resize, yet shrinking from capacity ten to four creates a semantic question: which four records survive? The usual "most recent" contract preserves the last four, whereas an arbitrary slice of the backing array may preserve the wrong physical entries after wraparound. Writing a reference test around that resize detects a subtle but realistic bug. Here the theory of ADTs, invariants, complexity, and memory models meets a concrete software design problem.

## Worked problem 1.1

A stack has push, pop and peek. Starting empty, run push(4), push(9), peek, pop, push(2), pop, pop. Record outputs and final contents.

**Define the data and method**
Push appends to the abstract sequence; peek reads the final item without removing it. The first peek yields 9. Subsequent removals yield 9, then 2, then 4.

**Derive and interpret the result**
The stack ends empty, with no underflow. The removal order differs from insertion order because the contract is last-in-first-out.

## Worked problem 1.2

For a capacity-5 circular queue, head=4 and size=3. At which physical slots are the logical items, and where is the next enqueue stored?

**Define the data and method**
Logical position j maps to (head+j) mod 5. For j=0,1,2, positions are 4,0,1; the next rear position for size 3 is (4+3) mod 5 = 2.

**Derive and interpret the result**
The queue invariant 0<=size<=5 is satisfied, and slot 2 is available. This calculation illustrates why head is not itself the rear index.

## Worked problem 1.3

A sequential scan tests n=12 elements once. How many comparisons are required to find a minimum and what is the asymptotic cost?

**Define the data and method**
Initialize the current minimum from the first element without comparing it to itself. Each of the other 11 elements is compared to the stored minimum exactly once.

**Derive and interpret the result**
There are 11 key comparisons and linear O(n) time. This is independent of input ordering, under the specified scan implementation.


### Applied investigation: Resizable arrays and representation invariants

A dynamic array keeps a logical length n and allocated capacity c, requiring 0≤n≤c at every valid state. If the capacity starts at one and doubles whenever full, append number nine triggers copying eight prior elements into new storage of capacity sixteen. The individual append is expensive, but the geometric expansion schedule bounds copying over a long sequence. A correct implementation must also preserve element order, retain access to valid indices and never expose uninitialized capacity slots as logical elements.

In a scan for the minimum, initializing the result to the first item requires a nonempty collection. For n elements this particular algorithm uses n−1 comparisons; the result does not depend on key distribution. A useful experiment changes the input order while holding its size fixed and checks that the comparison count is unchanged. Do not confuse the abstract array interface with contiguous storage guarantees for every high-level container.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Choosing a representation under real workload constraints

The phrase “a collection of values” does not identify a data structure. A library catalog, for example, might need to append acquisitions, retrieve a record by stable identifier, list titles in lexical order, and remove discontinued entries. Those operations induce different access patterns. A dynamic array gives constant-time indexing in its current representation and amortized constant-time append with geometric growth. It does not make insertion at the beginning constant-time: if n elements must move right, the number of shifts grows linearly with n. A dictionary keyed by accession number supports expected constant-time exact lookup under suitable hashing assumptions, but does not provide alphabetical iteration. A balanced search tree supports ordered range queries at logarithmic search cost but typically uses more per-element metadata. An engineering design might therefore maintain two indexes over the same underlying records, accepting additional update work and consistency obligations.

Consider twelve records, an array capacity of sixteen, and three actions: append a record, retrieve the ninth record by index, and insert one at position three. Appending needs a single new occupied slot without reallocation. Indexed retrieval follows the base address plus element-size times index, assuming a flat fixed-width layout. Insertion shifts the original elements at positions three through eleven, or nine existing items if indexing starts at zero. The same collection has a constant-time operation and a linear-time operation. Calling the whole structure either “fast” or “slow” conceals the workload that matters.

A representation invariant is an assertion that must hold at every public operation boundary. For an array-backed sequence, it could be 0 ≤ length ≤ capacity and the first length slots contain valid entries in logical order. During growth the implementation may temporarily allocate another buffer, copy entries and update capacity, but callers should never observe a half-copied state. In a concurrent implementation even this guarantee needs a synchronization strategy; an invariant stated for sequential execution is not automatically atomic under concurrent reads.

Use a cost model before committing to a design. Let a workload contain 70 percent reads by index, 20 percent appends and 10 percent middle insertions. A dynamic array is plausible, particularly if reads dominate and memory locality matters. Change the workload to 70 percent ordered predecessor queries and 20 percent deletions: a balanced tree is now a stronger candidate. The choice also depends on element sizes, stability of handles, allocator behavior and worst-case latency requirements. This explains why a big-O table is a starting point rather than a substitute for requirements.

The geometric-growth simulation uses an initial capacity of one and doubling on overflow. If n equals nine, capacity progresses through one, two, four, eight and sixteen. The cumulative copies caused by those expansions are 1 + 2 + 4 + 8 = 15, while the ninth append writes one new element. This upper-bounds aggregate growth work by a constant multiple of the number of appends, but an individual append that triggers reallocation can still require linear time. For systems with hard real-time constraints, the rare expensive append may be unacceptable even if the amortized average is attractive.

Experiment with the memory model and ask what it omits: a managed runtime can attach object headers, alignment padding, garbage-collector metadata and bounds checks. A linked node may require two pointers in a doubly linked list; an array of references stores pointers rather than the referenced objects. State the representation actually being compared before interpreting a byte total as a universal benchmark.


### A complete array-backed sequence design and proof

### Specify the observable behavior before optimizing

Design a generic sequence with operations size(), get(i), set(i,x), append(x), insert(i,x), erase(i) and clear(). All indices for get, set and erase must satisfy zero <= i < length. Insertion permits i equal to length because insertion at the end is meaningful. That one-character inequality distinction is responsible for many off-by-one defects. A caller should not need to know the current storage capacity, because capacity is a representation detail; revealing it in a teaching laboratory is useful, but basing application correctness on it would create unwanted coupling.

Define a record consisting of a pointer to allocated storage, a nonnegative length and a capacity at least as large as length. For the empty state, choose either a zero-capacity null allocation or an allocated minimum-capacity buffer. Both are valid, but tests and memory-management code must handle the choice consistently. The capacity invariant matters during mutation: a successful append increases length by one and places the new item at the previous logical end. If an allocation fails, a strong exception-safety policy can leave the original sequence unchanged rather than exposing a partially modified state. That requires allocating the replacement buffer first, copying or moving entries safely, and committing the new pointer only after the construction succeeds.

### Exact trace of insertion and erase

Let the logical array contain [11, 22, 33, 44] with capacity eight. insert(1,99) must produce [11, 99, 22, 33, 44] and length five. The mutation starts by moving the rightmost original element to slot four, then moves the elements at original indices two and one one position to the right. It cannot shift from left to right because writing 99 or moving 22 too early would overwrite data that still needs to be copied. When removing index two from the result, the implementation must shift 33 and 44 left, giving [11,99,33,44]. It must then decrement length, and in a language with explicit object lifetimes destroy the now-logically-unused trailing object or move it into the correct state. A fixed-capacity teaching implementation may avoid shrinkage entirely; an optimizing implementation can shrink only after the load falls below a separate threshold to avoid repeated grow-shrink oscillation.

### An aggregate amortized-cost argument

Assume capacity doubles whenever an append would exceed it. If initial capacity is one and the collection grows to n objects, capacities follow powers of two. Every reallocation copies all previously present objects, so the total number of copy operations up to n successful appends is the geometric sum 1+2+4+... up to the last completed growth. For n=9 that sum is fifteen, and for general n the sum is strictly less than twice n. Adding the n writes for newly appended objects yields a total amount of sequence-storage work that grows linearly with n, which implies constant amortized work per append. This reasoning does not give a constant worst-case bound for an individual append: the unlucky operation immediately after filling a large buffer must move many objects.

For a more formal potential-method analysis, assign a potential proportional to the occupied capacity so that cheap appends deposit credits and an expensive resize spends accumulated credits. The potential must be nonnegative at operation boundaries and should be zero or controlled at the empty starting state. Do not use the phrase “amortized means average over random inputs”; this result is deterministic across any sequence of appends and does not require a probability distribution. Conversely, once middle insertions are allowed, the repeated element shifts can make a sequence of n such operations quadratic even though geometric reallocation is amortized.

### Memory, locality and correctness experiments

A sequence storing fixed-width numeric values contiguously has predictable indexed address arithmetic. But a managed-language list may actually store pointers to separately allocated objects, so “array indexing” does not always mean that the numeric payloads themselves are adjacent. Measure the number of structural operations first, then ask whether machine-level locality, allocator behavior and object representation are consistent with the teaching model. Avoid claiming measured nanoseconds from a model that only counts element copies.

Construct a property test by generating a sequence of valid insertions, removals and replacements and applying the same operations to an independently implemented reference list. After each step compare length and all visible elements, then inspect internal capacity and initialization state. Explicitly test insert(0) into an empty sequence, insert(size), remove the sole element and a reallocation where moving one element throws an error. A robust library will state whether iterators and element references survive a reallocation; an implementation with raw pointers into the old buffer cannot preserve those references automatically.

### Interpretation checkpoint

For a collection of seven values in a capacity-eight buffer, appending the eighth requires no growth, but appending the ninth requires a new buffer. If we insert at index zero when length seven, seven existing elements must move, even though there is spare capacity. Therefore capacity slack solves allocation frequency, not the fundamental movement cost of ordered middle insertion. State these two costs separately in every performance report.


## Additional original authored teaching sections

# A data structure as a contract between users, algorithms, and memory

A data structure is not adequately specified by its diagram. It has a set of permitted operations, an interpretation of stored values, consistency conditions, and a cost model. Consider a learning platform that stores course registrations. The system must insert a student, find every course for one student, print a course roster, cancel a registration, and reconstruct what happened after a crash. A dynamic array of registration records is sufficient for storage but inadequate for efficient lookup unless an index is added. A hash map indexed by student identifier accelerates exact lookup but does not naturally answer ordered roster queries. A balanced tree indexed by a composite pair of course code and student number supplies ordering but changes the complexity and failure surface of updates. Before choosing any representation, specify how often each query occurs, how large the collection becomes, and whether a delayed lookup or an expensive update is more damaging.

The abstract data type, or ADT, defines observable behavior while leaving the representation open. For a map, useful operations include `put(key,value)`, `get(key)`, `remove(key)`, and `contains(key)`. The specification must decide what happens when an existing key is inserted: overwrite its value, reject the insertion, or retain multiple values. These policies produce different abstract data types even if all three use a bucket array internally. For a queue, removal returns the oldest element that has not already been removed. That statement is independent of whether the implementation uses a ring buffer, linked nodes, or two stacks. A correct representation preserves the ADT's behavior under every permitted sequence of operations, not merely under the first few examples in a tutorial.

Representation invariants are the bridge between storage and interface. For an array-based map whose occupied region has length n and capacity c, require `0 <= n <= c`; every occupied entry has a valid key and value; and keys are unique under the equality relation. For a hash table, add an invariant about probe reachability or membership in the correct chain. For a linked structure, require that each reachable next pointer identifies a live node and that traversal eventually terminates, unless the structure is intentionally circular. Such conditions must hold when a public method returns. During a private resizing operation they may be temporarily relaxed, but exposing the object to concurrent clients or callbacks at that moment becomes dangerous. A proof should distinguish intermediate states from observable states.

The difference between preconditions and invariants matters. A stack's invariant might be that length equals the count of reachable entries. A `pop` operation's precondition could be that the stack is nonempty, although a safer public API may instead return an empty optional value. A precondition restricts what the caller may request; an invariant restricts what the implementation may permit. If a library uses exceptions to report invalid operations, its error handling should restore all invariants before propagating the exception. Otherwise clients can observe a partially updated object after catching the error.

There is no single universally correct measure of memory consumption. For a fixed-width array, a simple model is header bytes plus capacity times element width. For an array of references, the array slots store machine references, and each referenced object may have its own header, alignment padding, or allocator overhead. A doubly linked list with n nodes typically requires at least two references per node in addition to its payload and allocation overhead. Yet a list with extremely large payload objects might spend only a small fraction of total memory on links. The relative advantage depends on what a node stores and what the runtime allocates, not on the phrase 'linked lists use more memory.'

Compare three potential representations for 100,000 eight-byte integer records on a platform with eight-byte pointers. An idealized contiguous array requires about 800,000 bytes for occupied values, excluding container headers and spare capacity. A singly linked node containing a value and pointer requires at least 16 bytes before allocation overhead, giving a lower bound of 1,600,000 bytes. A doubly linked node requires at least 24 bytes, giving 2,400,000 bytes before overhead. Real layouts may be larger because of alignment and allocation metadata. These estimates justify measuring actual memory in the intended language rather than copying textbook figures into performance decisions.

Two programs that implement the same ADT may also differ in their treatment of stable identifiers. Suppose a customer retains a reference to an array element, and the array later grows by reallocating its entire backing buffer. In languages with raw pointers, the old address can become invalid. A linked representation may preserve the address of an existing node across insertion, but a deletion can still invalidate it. A hash map can rehash when its load factor changes, invalidating references to bucket positions even though logical keys survive. If consumers need stable identities, store immutable record identifiers or allocate objects separately and maintain an indexing structure over those identifiers. Stable logical identity is not the same as stable physical address.

A useful contract includes negative requirements. A map does not promise sorted enumeration unless the interface says so. A priority queue does not promise FIFO ordering among equal priorities unless it includes a tie-breaking rule. A disjoint-set forest does not usually support arbitrary deletion from the middle of a set. Making these limitations explicit prevents callers from depending on accidental properties that disappear when the representation is optimized. The design goal is a small set of strong guarantees, not a vague promise that the structure is 'efficient.'

# An explicit cost model and a reproducible selection experiment

Asymptotic notation describes how the number of abstract operations scales; it does not measure a particular computer's elapsed time. A dynamic array's random access is constant-time in a RAM model because a fixed number of arithmetic operations computes an address. A linked list's indexed access is linear because reaching an arbitrary position requires following links. However, the number of CPU cache misses, branch mispredictions, memory allocations, and bounds checks can dominate wall-clock runtime for practical n. A correct evaluation should state whether the cost is measured in comparisons, pointer traversals, bytes transferred, storage pages accessed, or microseconds.

Consider a workload with 10,000 existing records and 1,000 requests. Suppose 800 are indexed reads, 150 are appends, and 50 insert near the beginning. A vector needs roughly 800 direct indexing operations and 150 ordinary append writes, apart from occasional capacity growth. Each early insertion may shift nearly 10,000 elements, so 50 such insertions could cause on the order of half a million assignments. A linked list with only a head pointer can insert near the beginning cheaply after finding the position, but each of 800 indexed reads may traverse thousands of links. The fact that one implementation excels at append does not settle the case. Convert operations into estimated work, and validate those estimates with representative traces.

A benchmark should isolate construction cost from query cost. If you time building a balanced search tree and then time searching it, compare that total with the construction and searches for a hash table or sorted array. Sorting a static collection once can be attractive when updates are rare, but the preprocessing work becomes relevant when the collection is rebuilt after every import. Conversely, evaluating only lookup latency favors a heavily indexed design while concealing maintenance costs. The correct objective may be total work per hour, p99 query latency, memory per record, or the maximum time spent holding a lock.

To conduct a fair experiment, generate a deterministic sequence of operations and apply it to several implementations. Begin with a simple reference model, such as a list of key–value pairs, whose result is easy to reason about. Record each request and its expected result before timing the optimized versions. Use the same input keys, deletion pattern, and distribution of hot keys for each implementation. Warm caches consistently if evaluating steady-state performance, or deliberately start cold when cold-start cost matters. Report n and the hardware/runtime characteristics alongside the result; a single isolated measurement without context cannot establish a general superiority claim.

A particularly revealing experiment uses skew. Generate 90 percent of lookups for 10 percent of keys and compare the result with uniformly distributed lookups. The relative value of an LRU cache, a compact vector, and a hash table may change because cache residency changes. Next generate keys whose hashes collide and test hash-table robustness. Next insert sorted values into an unbalanced search tree and check whether its height approaches n. These are not unfair tricks; they represent distributions and adversarial inputs that a production implementation may have to handle. Average-case claims are conditional on workload assumptions.

Amortized analysis answers a different question from a benchmark. When a vector doubles from capacity eight to sixteen, copying eight entries makes that append expensive. But charging the preceding appends a small amount of credit can pay for the copy, yielding constant amortized append work over a long valid sequence. A ten-millisecond pause during one grow is still a ten-millisecond pause: a latency-sensitive request can miss its deadline even when the mean insertion cost is low. Engineering decisions should retain both amortized throughput and worst-event behavior, and avoid silently substituting one for the other.

The experiment should culminate in a decision record: state the operations, observed distributions, maximum size, required correctness properties, alternatives examined, measurements, and reasons for rejection. This document is often more useful than a microbenchmark chart because it explains the assumptions under which the decision was made. It is also a plan for future reevaluation: if the product begins performing ordered range searches or if record volume rises by two orders of magnitude, the original representation should be reconsidered. Data structure selection is a response to requirements, not a declaration of taste.
