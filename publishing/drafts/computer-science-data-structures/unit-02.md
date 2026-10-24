# Data Structures — Unit 2: Sequential structures

**DRAFT — length threshold and independent review outstanding.**

## 2.1 Dynamic Arrays

### Dynamic Arrays

A dynamic array maintains a logical size and reserved capacity. Geometric resizing makes repeated append operations amortized constant time, although an individual resize copies many existing elements. Random access remains O(1).

## 2.2 Linked Lists

### Linked Lists

Linked lists support local pointer changes when the predecessor or node reference is known. Finding a position by index costs O(n) in a basic singly linked list. Correct implementations handle empty, singleton, head, and tail cases.

## 2.3 Stacks

### Stacks

A last-in-first-out stack supports push, pop, and peek. It is used in expression parsing, depth-first search, and call management. Its contract must specify whether popping an empty stack raises an exception or returns a distinguished result.

## 2.4 Queues

### Queues

A first-in-first-out queue processes older entries before newer ones. Circular arrays use modulo arithmetic for head and tail positions, avoiding linear shifts; linked implementations manage head and tail references.

### Extended design study: matching operations to sequential representations

Consider a web server that processes requests arriving at unpredictable times. New requests join a queue, and the worker retrieves the oldest request. The interface is FIFO, so its data structure should preserve arrival order even when multiple requests have equal timestamps. A bounded circular buffer can perform enqueue and dequeue without physically shifting the stored elements. A linked queue can achieve the same abstract behavior with head and tail references. The distinction becomes important when choosing a capacity policy: a fixed ring must reject, block, or overwrite when full, while a linked queue can grow until memory limits or backpressure policies intervene. These choices belong to the application contract.

Arrays are particularly effective when the workload repeatedly needs random access. A batch of measurements sorted by timestamp supports direct indexing and efficient scans through contiguous storage. Inserting an entry into the middle of such an array may require moving many later entries, however. A linked list changes only nearby pointers when the insertion position is already known, but finding that position by value still takes linear time. Claiming "linked-list insertion is O(1)" without saying the node is known hides the lookup cost. The operation being timed or analyzed must include the work the caller actually performs.

The dynamic-array growth policy is another point where mathematical analysis informs practice. If capacity doubles, growing from 1 to 2, then 4, then 8, and so on, old elements moved during reallocations form a geometric series. In contrast, growing capacity by exactly one each time copies 1+2+⋯+(n−1) elements over n appends. The same logical append contract can therefore have substantially different total costs. Reallocation also affects references: code that stores raw addresses into the backing array must understand when those addresses cease to be valid.

A separate exercise is to build a queue using two stacks. One stack receives arriving items; another serves departing items. When the outgoing stack is empty, move all items from the incoming stack into it, reversing their order so the oldest item appears on top. An individual transfer can be linear, but every item is pushed and popped only a constant number of times across its lifetime; the resulting queue has amortized constant time per operation. This illustrates why amortized analysis can describe an efficient design even when particular operations occasionally require a large burst of work. Tests should compare its outputs to a reference FIFO sequence after random operations, including underflow and long alternations of enqueue and dequeue.

## Worked problem 2.1

Starting with capacity 1, a dynamic array doubles whenever full. Insert 9 items. List the growth capacities and count old elements copied.

**Define the data and method**
Reallocations before insertions 2,3,5,9 copy 1,2,4,8 old elements respectively. New capacities are 2,4,8,16.

**Derive and interpret the result**
The total is 1+2+4+8=15 copies over 9 inserts. One append can cost linear time; repeated appends have constant amortized cost under geometric growth.

## Worked problem 2.2

Given linked nodes A→C→D, insert B immediately after A. Name the required pointer-update order and explain why.

**Define the data and method**
Allocate B and set B.next=A.next, retaining the pointer to C. Only then set A.next=B. The result is A→B→C→D.

**Derive and interpret the result**
Assigning A.next=B first without retaining the original link can make the suffix unreachable. The insertion itself uses O(1) pointer updates when A is already known.

## Worked problem 2.3

A ring queue of capacity 4 enqueues A,B,C, dequeues twice, and then enqueues D,E. What is the visible sequence?

**Define the data and method**
After A,B,C the sequence is [A,B,C]. Removing A and B leaves [C]. Enqueue D then E makes [C,D,E], regardless of which physical array positions wrap.

**Derive and interpret the result**
The answer is C,D,E. A correct circular-buffer implementation preserves FIFO order, with indices computed modulo capacity.


### Applied investigation: Linked traversal and circular queue invariants

A singly linked list stores each node’s value and a link to the next node, permitting constant-time insertion at a known location but not constant-time random indexing. Reaching one-based position n from the head requires n−1 next-pointer transitions. An iterator may expose sequential traversal without exposing raw pointers. Invalid links, cycles and stale references are separate safety hazards that a simple pointer-count model cannot detect.

A circular array queue represents a logical sequence using head, tail and capacity. After n dequeues, a head initially at zero moves to n mod capacity, provided enough items were enqueued. Distinguish an empty queue from a full queue by tracking length or reserving one slot. Tests should enqueue to capacity, trigger a wrap, dequeue and reenqueue, and verify FIFO order, rather than checking only a modular arithmetic display.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Sequential containers and the lifetime of references

A stack is defined by last-in, first-out behavior, not by a particular memory layout. A stack implemented over a resizable array pushes and pops at the end without shifting all existing elements. A linked implementation allocates a new head node for push and detaches it for pop. Both provide constant-time individual operations in a model that ignores occasional array expansion or allocation cost, but their failure modes differ. The array can run out of contiguous memory and reallocation can invalidate pointers into its storage; the linked version can fragment the heap and requires explicit attention to ownership. This distinction is easy to miss when comparing only abstract operation names.

Take the stack sequence push A, push B, push C, pop, push D, pop, pop. The successive popped values are C, D and B, leaving A. A queue would instead remove A first. We can verify an implementation using this trace and then test emptiness, capacity exhaustion, repeated alternating operations and an attempt to pop an empty container. Empty removal must have a documented contract: error, optional result or sentinel value. The last option is hazardous if the sentinel could itself be a legitimate stored value.

A circular array queue stores head, length and capacity. Given capacity seven, a state with head index five and length four occupies logical positions 5, 6, 0 and 1. Enqueueing adds to the slot at (head + length) modulo seven, provided the queue is not full. A dequeue removes from head and advances the index. The physical array order does not generally equal the logical queue order after wraparound. Tests should deliberately cross the wrap boundary, because examples that never wrap will not expose a missing modulo operation.

Singly linked lists deserve a careful cost statement. Removing the first node is constant-time when the head pointer is available; removing a node at an arbitrary logical index first requires walking to its predecessor, usually linear in the index. Removing a known node is only constant-time if the implementation's structural and ownership conditions allow it. In a singly linked list, deleting the last node from only a pointer to that node cannot in general be done without finding the predecessor. Doubly linked lists trade a second link and extra update rules for easier removal of known nodes.

Aliasing introduces a more subtle concern. Suppose two clients hold a reference to the same mutable linked node. If one client splices the node out and deallocates it, another client's reference may be invalid in an unmanaged language. In a garbage-collected language the object may remain allocated, but its membership in the list can still change. An iterator's promise should specify whether it is stable across mutation, invalidated on structural edits, or provides a snapshot.

For a browser history application, two stacks can implement back and forward navigation. Visiting a new page pushes the current page onto the back stack and clears the forward stack. Back navigation transfers the current page into the forward stack and pops the back stack. The underlying proof of correctness is an invariant relating the current page and the two histories. A popular but incorrect implementation forgets to clear the forward stack on a fresh navigation; a focused test can detect this with the sequence A → B → C, Back to B, visit D, then attempt Forward.


### Implementing a ring buffer and checking ownership

### Separate abstract order from physical slots

Build a bounded queue with capacity C, head index h and current length k. The logical element at position j is stored at physical index (h+j) mod C for zero <= j < k. The tail insertion location is (h+k) mod C. These expressions define the mapping completely; the raw array order is only an implementation detail. For an empty queue h may remain where the last removal left it. There is no need to reset h to zero unless an interface contract requires it. A full queue satisfies k=C, not h=tail, because h=tail is also true when k=0 unless the design maintains an extra status bit or reserves one unused slot.

Choose capacity five and start with an empty queue whose head is zero. Enqueue A,B,C,D and dequeue twice. The remaining logical sequence is [C,D], head index two and length two. Enqueue E,F,G; the physical occupied locations are two, three, four, zero and one, while the logical order remains [C,D,E,F,G]. A mistaken debug print that reads raw array indices zero through four would show [F,G,C,D,E] and might make a correct queue appear broken. The proper output order uses the modular logical mapping.

### What exactly does dequeue promise?

Dequeue must either return and remove the oldest item or report that the structure is empty. If the queue stores objects with destructors, the removed object should be transferred or copied according to language semantics before its slot is made unoccupied. After removal, advancing head and reducing length must preserve the invariant. If an exception occurs during value extraction, the library has to state whether the element was removed. Exception safety is not merely a C++ concern: state transitions across async callbacks and serialization can fail in other languages as well.

Linked implementations use a head and tail pointer instead of modular arithmetic. For a singly linked FIFO queue, enqueue adds a node after the current tail and updates tail; dequeue removes head. Removing the last node must also reset tail to null. If the implementation forgets this, the next enqueue can link onto an invalid old tail and lose the new element. Test the empty-to-one-to-empty-to-one transition because ordinary tests with many elements may never exercise it.

### Stack frames, recursion and memory pressure

A program's call stack is related to but distinct from the stack abstract data type. A recursive depth-first traversal consumes one runtime stack frame per active recursive call unless its language or implementation performs a relevant optimization. Even when each frame is small, traversing a chain with millions of nodes can exceed the call-stack limit. An explicit stack allocated in heap memory gives the program control over depth and overflow handling, although it does not change the asymptotic memory bound for worst-case depth. A breadth-first traversal instead needs a queue that can become as wide as an entire graph layer.

### Safe linked traversal

A linked-node search should treat the head pointer as a current position and advance until either a matching value or the null terminator is reached. Never dereference null before checking it. Cycle detection requires a different contract because a cyclic list has no terminating null. Floyd's tortoise-and-hare method advances one pointer by one edge and another by two; if they ever meet away from null, a cycle exists. A cycle-free list terminates when the fast pointer or its next link becomes null. This algorithm uses constant additional pointers and does not mutate nodes, but its correctness relies on a stable link structure during the traversal.

### Laboratory checks

For the seven-slot queue simulation, changing the input from six to eight wraps the head index from six to one. The displayed head index is not a count of remaining items, and the model assumes enough items were enqueued to support every requested dequeue. Add tests for size zero, full capacity, wraparound, multiple cycles and simultaneous enqueue/dequeue; a model that only advances a head index does not implement all of those behaviors. For a general queue implementation, compare against a simple reference deque under randomly generated valid operations and ensure every removal returns the oldest outstanding item.


## Additional original authored teaching sections

# Sequential containers in parsers, editors, and event systems

A sequential container has at least two notions of position. Its logical position expresses the order exposed to the user; its physical position expresses where an element currently lives in memory. In a contiguous array these notions are often aligned, whereas a circular queue intentionally separates them. When an event collector has capacity eight, head index six and length four, its logical contents occupy physical indices six, seven, zero and one. Appending the next event writes index two. A renderer that simply prints indices zero through length minus one will display the wrong logical order after wraparound, even if enqueue and dequeue have returned correct individual values so far.

A ring buffer can be specified with three state variables: storage of fixed capacity c, a head h, and a count n. Its occupied positions are `(h+i) mod c` for i from zero through n minus one. The queue's next insertion position is `(h+n) mod c`, provided n is less than c. An enqueue writes this slot and increments n. A dequeue reads at h, advances h by one modulo c and decrements n. The invariant `0 <= n <= c` and the mapping from logical to physical indices are sufficient to derive the ordinary sequential behavior. The empty state is exactly n equals zero, while the full state is exactly n equals c; relying on head equaling tail is ambiguous unless an extra convention or occupancy flag is added.

A common incorrect implementation increments the tail before writing rather than after, so the first insert skips one slot. Another forgets to apply the modulus when an index reaches c, causing out-of-range access. Yet another treats a full queue as indistinguishable from an empty queue because both can produce head equals tail. An effective test suite includes one element, exactly c elements, a dequeue followed by enqueue, several wraps, and alternating operations for many cycles. Compare all returned values with a reference queue implemented as a simple list; the latter may be slower but is easier to validate for modest test sizes.

Stacks have applications well beyond a command-line demonstration of push and pop. A parser evaluating nested expressions pushes opening delimiters and checks that each closing delimiter matches the most recent unclosed opening delimiter. The required invariant after reading any input prefix is that the stack contains exactly those opening delimiters that have not yet been matched. At the end, an empty stack is necessary for balanced input. It is not sufficient if the parser failed to reject a premature closing delimiter during processing. This explains why the algorithm must check both mismatched closers during the scan and leftover openers after the scan.

An undo system highlights a second stack concept: transactions. Editing a document is not always equivalent to recording every keystroke as a separate undo step. The user may expect typing a word to undo as one action while an autocomplete operation should be atomic. A command stack therefore stores reversible semantic operations or snapshots. If a new operation is executed after undoing several earlier operations, the redo history usually must be invalidated. If the operation has external effects, undo may not be possible merely by restoring an in-memory state: sending an email, charging a card, and deleting a remotely replicated record require domain-specific compensation policies. The stack models the order of recovery, not a universal guarantee of reversibility.

Linked lists trade locality for pointer-oriented structural changes. With a doubly linked list, insertion immediately after a known live node can modify a bounded set of next and previous references. Yet the phrase 'known node' is essential. If the caller provides only the index 50,000, finding the node may require 50,000 or more traversals. If an existing iterator points to a removed node, retaining its pointer may violate the iterator's contract even if other nodes remain valid. Memory safety and logical membership are separate concerns; a managed-language reference can remain allocated after the referenced node no longer belongs to the list.

Sentinel nodes can reduce edge-case branching by giving an empty doubly linked list a dummy header whose next and previous pointers refer back to itself. Inserting at either end becomes ordinary link rewiring without special null checks. The correctness argument still requires verifying all four affected pointers. Deletion must reject removal of the sentinel itself. A useful test asserts that following next pointers from the sentinel visits each live node once, that following previous pointers gives the reverse order, and that next.previous and previous.next return to the starting node for every reachable entry.

# A practical comparison of editing representations

Suppose a text editor stores a document as a single string. Insertion near the front of a long immutable string can allocate and copy much of the content. A gap buffer stores a contiguous array with an unused gap at the cursor. Typing at the cursor fills part of the gap, so repeated nearby insertions avoid moving the entire tail each time. Moving the cursor far away relocates the gap by copying characters across the new position. A rope stores text in a balanced tree of chunks, allowing a large document to be edited without copying all characters on many operations, at the price of tree nodes, balancing logic, and more complex indexing.

These structures differ not because one has a better name but because cursor locality differs from random editing. For an ordinary user who mostly types at the current cursor, a gap buffer's costs may be favorable. For a collaborative editor applying remote edits in many regions, a balanced tree or other indexed sequence may be more appropriate. A rope needs weight or length metadata at internal nodes so that an index can be translated into a path through the tree; those metadata must change after splits and joins. Failure to update one internal weight can make later cursor movement land on the wrong character without immediately crashing.

Unicode adds a correctness dimension. The document's user-visible cursor usually moves across grapheme clusters, not arbitrary bytes. A Unicode string may use multiple code points for one displayed character; in UTF-8 a single code point can use multiple bytes. The length used by the editor's logical indexing API must be distinguished from byte offsets used by its storage. A naïve cursor operation that moves one byte can land in the middle of a multibyte sequence. A rope whose metadata counts code points but whose cursor API expects grapheme clusters requires additional segmentation logic. Complexity analysis must specify what one indexed unit means.

For a browser's tab history, a doubly linked list might seem convenient because it supports moving to previous or next entries. But browser history is often better represented by a linear sequence and one current-position index: moving backward decrements the index; moving forward increments it; navigating after going back truncates the forward suffix before appending the new page. An array provides efficient indexed access and easy serialization. Choosing a linked list solely because navigation is described as 'next' and 'previous' confuses an application's vocabulary with its actual workload.

An experiment should compare the representation under three traces: append-only typing, concentrated cursor edits, and uniformly random edits. Count bytes moved, not just operation calls. A gap buffer can have few bytes moved on the first trace and many on the third. A rope can avoid copying the entire document but pay in allocations and tree operations. Also evaluate memory retention after deleting a large range; some implementations retain oversized backing chunks unless compaction occurs. An implementation that is fast when growing but never releases unused capacity can create long-lived memory pressure.

Do not treat benchmark outputs as correctness evidence. A document editor must preserve every character and every logical offset despite edits, undo, and serialization. One property-based test generates random inserts and deletes, applies them both to the optimized representation and an immutable-string reference, and compares their fully materialized contents after each step. Another test checks cursor boundaries around combining marks, emoji sequences, and newlines. The most informative test suite crosses abstraction boundaries: logical Unicode indices, physical storage layout, and undo semantics. Efficiency becomes valuable only once these three agree.
