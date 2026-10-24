# Data Structures — Unit 5: Priority structures

**DRAFT — length threshold and independent review outstanding.**

## 5.1 Heaps

### Heaps

A binary heap stores a complete tree in an array, enforcing a parent-child priority inequality. It supports constant-time inspection of the highest-priority element and logarithmic insertion and extraction.

## 5.2 Priority Queues

### Priority Queues

A priority queue removes entries by priority, not by arrival order. Binary heaps are a common implementation. Handling tied priorities requires an explicit stable ordering policy when reproducibility matters.

## 5.3 Heap Construction

### Heap Construction

Bottom-up heapification sifts down internal nodes from the last parent toward the root. Because most nodes are near leaves, the total work is linear rather than n log n.

## 5.4 Scheduling Applications

### Scheduling Applications

Priority queues can order tasks by urgency or deadline. Choosing an effective priority policy requires considering starvation, fairness, preemption, and how priorities change over time.

### Extended design study: dispatching work by priority

Imagine a small numerical-computing service with tasks that have an estimated urgency. A FIFO queue would respect arrival order, but it would not guarantee that the most urgent waiting task is processed next. A priority queue supports insertion of a task with priority p and removal of a task with highest priority under a defined convention. In a min-heap design, smaller numerical priorities are considered more urgent. A task with priority 2 is selected before one with priority 9 regardless of which arrived first. This behavior should be documented because some libraries instead interpret larger scores as more urgent.

A binary min-heap is represented as an array with parent index floor((i-1)/2) and children 2i+1 and 2i+2. When inserting, append the item and repeatedly swap it upward while its key is smaller than its parent's. When extracting, remove the root, move the final array entry to the root, and sift it downward by swapping with the smaller child where necessary. The heap-order invariant must hold after both operations. Array order is not sorted order: only each parent's relation to its children is guaranteed. Arbitrary exact-key search therefore does not inherit the efficient root access bound.

The build-heap method illustrates how aggregate analysis beats a superficial multiplication of operation costs. Inserting n separate values one by one can take O(n log n) worst-case total work. Bottom-up heapification starts from the last internal node and sifts downward. Most nodes sit close to the leaves and have little work to do. The number of nodes capable of traveling h levels decreases roughly geometrically with h, so summing the work across all heights gives a linear total bound. This result should not be confused with the O(log n) worst-case cost of a single extraction after the heap has been built.

Real schedulers introduce complications beyond the simple priority abstraction. Tasks may have equal priorities, deadlines may change after insertion, and a steady stream of urgent work may starve less urgent work forever. Stable tie-breaking can be implemented by attaching an insertion sequence number and comparing `(priority, sequence)`. Supporting a decrease-key operation efficiently may require an index map from task identifier to heap position that is updated after every swap. A scheduler should also consider fairness and aging, which can modify effective priority as a function of waiting time. A simulation based on a fixed heap does not model these policies unless they are implemented explicitly. The data structure solves a narrow ordering problem; the operational policy determines whether the service behaves acceptably.

## Worked problem 5.1

Is array [2,5,3,9,8,7] a valid min-heap, and is it sorted?

**Define the data and method**
For indices 0,1,2, compare each parent to existing children: 2<=5,3; 5<=9,8; 3<=7. Thus all required parent-child inequalities hold.

**Derive and interpret the result**
It is a valid min-heap, but not sorted (5 precedes 3). Heap order supports constant-time peek-min, not binary search over the raw array.

## Worked problem 5.2

Using a min-priority queue, insert jobs with priorities (A,4),(B,2),(C,5),(D,1). In what priority order will they be removed?

**Define the data and method**
Removing the minimum repeatedly selects priority 1 then 2 then 4 then 5. Associate these priorities with D,B,A,C, respectively.

**Derive and interpret the result**
The removal order is D,B,A,C. If priorities tie, a stability rule or a secondary insertion counter must be specified separately.

## Worked problem 5.3

A heap of n elements is built bottom-up. Why is this O(n) rather than O(n log n)?

**Define the data and method**
Most nodes are near the leaves and require at most one or two levels of sift-down. Bound the total by summing the number of nodes at height h times O(h), approximately n*sum(h/2^(h+1)).

**Derive and interpret the result**
The geometric weighted series converges, giving O(n) comparisons in the standard heapify analysis. This does not imply that each individual sift-down is O(1).


### Applied investigation: Heap invariants and priority queue contracts

A binary min-heap stored in an array places the children of zero-based index i at 2i+1 and 2i+2. The heap property says each parent priority is no larger than its children. It does not require the entire array to be sorted. Insertion appends a new item and exchanges it with its parent until the property holds. The number of exchanges is bounded by heap height.

Remove-min returns the root and then moves the last item to the root before sifting down. To test a heap, assert both that repeated removal yields nondecreasing priorities and that the invariant holds after every mutation. Ties need a documented stability policy if items with equal priority carry distinct payloads. The displayed array is one legitimate heap representation, not the only one.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Heaps, priority queues, and stable ordering

A binary heap is a nearly complete binary tree encoded compactly in an array. A min-heap invariant requires each parent's priority to be no greater than its children's priorities. The minimum lives at the root, but the array is not globally sorted. For zero-based indexing, the parent of a node at index i greater than zero is floor((i−1)/2); children are at 2i+1 and 2i+2 where those indices exist. Those formulas depend on the array representation, not on a separately allocated linked tree.

Insert the priorities 8, 3, 7 and 1. Beginning with an empty heap, insert 8 to get [8], insert 3 and sift up to get [3, 8], insert 7 to get [3, 8, 7], and insert 1, swapping with 8 and then 3, to obtain [1, 3, 7, 8]. Each swap repairs the local parent-child violation along a single path. A valid heap may have multiple possible array layouts for the same set of priorities, because its invariant is weaker than complete sorted order.

Delete-min replaces the root with the last item, shrinks the array, and sifts that item downward until the invariant is restored. Each step chooses the smaller eligible child. A common bug compares only against the left child and ignores a smaller right child. A focused adversarial test can expose the error by building a root whose right child is smaller than its left child. Verify the heap invariant after every mutation as well as the final output sequence.

Heap construction has an important distinction. Repeatedly inserting n items takes O(n log n) in the general upper bound, but Floyd's bottom-up heapification runs in O(n): most nodes are near the bottom and can move only a small distance. A proof groups nodes by height and sums their possible sift costs, yielding a convergent geometric series multiplied by n. The fact that a single sift is logarithmic does not imply that every bottom-up call incurs the maximum.

Priority queues require an ordering policy beyond the raw data type. A hospital triage system might use urgency as its primary key and arrival time as a tie-breaker. Without a tie-breaker, a binary heap does not necessarily preserve arrival order among equal priorities. To obtain stable behavior, compare pairs (priority, insertion_sequence) instead of only the priority. Editing an existing item's priority poses another implementation problem: unless the heap can locate that item efficiently, decrease-key may require a mapping from external identifiers to heap indices.

For a discrete-event simulator, the event queue stores future events ordered by simulation timestamp. Processing the minimum time and then scheduling new events preserves chronological order if time never moves backward. The application must also decide how to handle equal timestamps, canceled events and events scheduled during callbacks. A heap supplies an ordering mechanism; it does not by itself define the semantics of the event-driven model.


### An indexed priority queue with decrease-key

### Separate heap order from identity

A binary heap efficiently selects the smallest priority but does not automatically locate an arbitrary item whose priority changes. In a task scheduler, an item has a stable task identifier and a mutable urgency score. If the only representation is an array of priorities, the scheduler would need to scan linearly to find the task before changing it. An indexed priority queue stores both a heap array of task identifiers and a map from each identifier to its current heap position. Each swap during sift-up or sift-down updates the map for both items. With a hash-based position map, locating an item has expected constant cost and repairing heap order takes logarithmic time.

Represent a task by (identifier, priority, insertion_sequence). If smaller numerical priorities run earlier, compare first by priority and then by sequence number so equal-priority tasks remain stable. The heap array contains identifiers and a separate dictionary stores their attributes. This avoids stale values if task metadata changes but requires the mapping and heap order to remain synchronized. In a single-threaded implementation the invariants can be checked after each completed public operation. A concurrent scheduler additionally needs atomicity around changes to both structures.

### A precise decrease-key trace

Suppose the heap currently stores tasks A:4, B:7, C:6 and D:9. Reducing D's priority from nine to two should move D toward the root. Starting from D's recorded heap index, compare the new key to its parent and repeatedly swap until the order condition is satisfied. The map from identifiers to heap indices must change after every swap. The final root is D because it now has the smallest priority. A mistaken implementation that repairs only the heap array but forgets the position map may appear to work for this operation yet fail on the next update of B.

Increase-key moves in the opposite direction. If the root's priority grows from two to ten, it should sift down, selecting the smaller child at each step. Removing an arbitrary task can be handled by moving the last entry into its slot and repairing either upward or downward depending on the new key's relation to its neighbors. That dual possibility is a common source of latent bugs.

### Complexity and construction

An ordinary binary heap supports peek-min in constant time, insertion and extract-min in logarithmic time, and bottom-up construction in linear time. The indexed version adds a position map but must maintain it during every swap. It does not improve worst-case heap depth; it changes how quickly a non-root item can be found for update. The map itself has cost and may need rehashing. A system that rarely changes priorities may not benefit enough to justify the extra complexity.

### Canceled and delayed events

A discrete-event engine may schedule a future event, cancel it, and schedule a replacement. One approach removes the canceled item from the heap using its index map. Another marks it canceled and lazily discards it if it later reaches the root. Lazy cancellation is simpler but can retain many useless entries until cleanup, increasing memory use. The API should state whether canceled handles can be reused and how generation identifiers prevent a stale handle from canceling an unrelated new event.

### Independent test oracle

Maintain an independent sorted list of active tasks ordered by (priority, insertion_sequence). Generate inserts, updates, cancels and extract-min operations. After every step, compare the heap root with the reference minimum, check that all recorded heap indices match the actual array positions, verify parent-child priority ordering, and ensure no task identifier appears twice. Include equal priorities, empty extraction, update of the root, update of the final leaf and canceled events. These checks are stronger than observing a smooth animation of heap insertions.


## Additional original authored teaching sections

# Priority queues in scheduling, routing, and streaming systems

A priority queue returns an item with minimum or maximum priority according to a comparator. It is not the same as a sorted list: the abstract interface normally promises efficient insertion and access to the current extreme, not a complete sorted enumeration at every moment. A binary heap supports these operations using the shape of a complete binary tree stored in an array. For zero-based indexing, the children of index i are at indices 2i+1 and 2i+2, and its parent is at floor((i-1)/2). The array layout avoids one node allocation per element, but the heap-order property is weaker than total sorting. In a min-heap, each parent key is no larger than its children; two elements in unrelated subtrees may appear in either order.

Insertion appends the item at the next available array position and restores heap order by repeatedly exchanging it with its parent while necessary. The number of upward exchanges is at most the tree height, logarithmic in the number of entries. Removing the minimum returns the root, moves the last element to the root, reduces the occupied length, and shifts that element downward by exchanging it with the smaller child when needed. The common error is to choose the left child unconditionally; if the right child has a smaller key, heap order remains broken after the exchange. Test the two-child comparison explicitly and cover equal priorities, one-item heaps, and removal until empty.

A heap is not uniquely determined by its set of keys. Several array layouts can satisfy heap order for the same set. Therefore, validating an implementation by demanding one exact internal array is too strict unless insertion order and tie-breaking rules are also fixed. A better oracle asserts the parent–child heap property after every mutation and checks that successive removals form a nondecreasing sequence. Equal-priority items require a policy if stable order matters. A scheduler can store a tuple `(priority, sequence_number)` so that earlier enqueued jobs come first when priorities match. This explicit tie-breaker turns potentially unstable scheduling into predictable scheduling.

Bottom-up heap construction starts from the final internal node and applies downward heapification toward the root. Although one downward heapify can take logarithmic time, the total construction cost is linear in the number of items: most nodes are near the leaves and require very few exchanges. Treating n heapify calls as n independent worst-case logarithmic operations gives a valid loose bound but misses the stronger aggregate result. This distinction matters when a system receives a large batch of initial jobs. Building one heap from the batch can be more efficient than inserting every job separately with individual upward traversals.

Priority queues often need more than push and pop. Dijkstra's shortest-path algorithm may discover a shorter tentative distance for a vertex already in the queue. An indexed heap maintains a mapping from vertex identifier to heap position so that decrease-key can locate the element and restore order in logarithmic time. Without the mapping, searching for the element inside the heap is linear in the worst case. A simpler implementation can push multiple entries for the same vertex and ignore stale entries when popped, trading extra queue work and storage for simpler code. Both variants can be correct, but their complexity analysis and memory usage differ.

A task scheduler illustrates operational policy. Suppose tasks A, B, and C have priorities five, two, and five. Under a min-priority policy, B runs first; among A and C, an implementation may choose either unless a stable tie-breaker is included. When priority changes while a task is queued, simply mutating its priority field can invalidate heap order because no sift operation is triggered. An indexed queue should perform an explicit update and choose upward or downward repair according to whether the key decreased or increased. The correct priority semantics belong in the API rather than being left to incidental array order.

# Streaming top-k, median maintenance, and worst-case behavior

A large stream may require its five highest observations without storing every reading. Maintain a min-heap containing at most k values. For each new value, insert it if fewer than k values are stored. Otherwise compare it with the heap minimum, which is the smallest of the current top k; replace that minimum only if the new value is larger. Each accepted replacement costs logarithmic time in k, while rejecting a small observation needs constant comparison work. For a stream of n entries, the space requirement is proportional to k, not n. This is an algorithmic consequence of choosing the right maintained summary.

Take k equal to three and observations 7, 2, 9, 1, 8, 5. The first three values produce a heap containing 2, 7, and 9 in some valid heap order. Value one is rejected because it does not exceed the current minimum two. Value eight replaces two; the retained values become 7, 8, and 9. Value five is then rejected. The result is the correct set of top three values, but the heap array itself need not be sorted. If the application requires descending display order, it must copy and sort the summary or remove values from a separate heap.

Online median maintenance can use two heaps: a max-heap for the lower half of observations and a min-heap for the upper half. Maintain two invariants: every item in the lower heap is no larger than every item in the upper heap, and their sizes differ by at most one. When a new observation arrives, insert it into the appropriate half, then rebalance if necessary. For an odd number of values, the median is the top of the larger heap. For an even number, a numerical application may define the median as the average of the two tops, but a discrete or categorical ordering may use a lower or upper median instead. State which definition the interface implements.

This two-heap scheme raises numerical corner cases. Computing the average `(a+b)/2` can overflow a fixed-width integer even when the mathematical average is representable; a carefully chosen formula or larger numeric type may be needed. Floating-point observations may include NaN values whose comparison semantics do not define a normal total order. If the comparator is inconsistent, a heap cannot maintain a meaningful ordering invariant. Input validation must exclude unsupported values or specify a deterministic ordering policy. Correctness requires a comparator that behaves coherently under every comparison the heap performs.

A scheduler's performance also depends on update frequency and priority distributions. If jobs frequently change priority, an indexed heap can outperform a lazy approach that accumulates stale entries. If priorities come from a tiny integer range, a bucketed priority queue may offer simpler operations than a comparison heap. If nearly all work is processed in FIFO order at each priority, an array of queues indexed by priority is a sensible hybrid. The complexity of a priority queue therefore depends on permitted operations and key domain. Do not import logarithmic bounds as a universal statement about every conceivable queue design.

A meaningful simulator can show the heap array and the logical binary tree simultaneously, animate comparisons, and expose the parent–child inequality after each operation. Include a deterministic input trace and a reset mechanism so two variants can be compared fairly. For the top-k exercise, render the retained set and separately render its sorted presentation, making the distinction between heap order and total order visible. Tests should evaluate output values against an independently sorted reference, verify all parent–child inequalities, and cover duplicate priorities and empty or singleton cases. An animation that looks plausible but does not check these invariants is a visualization, not a validated model.
