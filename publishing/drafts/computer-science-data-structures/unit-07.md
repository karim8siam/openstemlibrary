# Data Structures — Unit 7: Specialized structures

**DRAFT — length threshold and independent review outstanding.**

## 7.1 Tries

### Tries

A trie stores strings along shared character-prefix paths. Traversal cost is linked to key length rather than the number of stored keys, though branching and node representation influence memory usage.

## 7.2 Disjoint Sets

### Disjoint Sets

A union–find structure maintains a partition of elements under find and union. Union by rank or size and path compression yield nearly constant amortized time across long operation sequences.

## 7.3 Range-Query Trees

### Range-Query Trees

Fenwick trees and segment trees aggregate intervals under operations such as sum, minimum, or count. The choice depends on the required update and query algebra.

## 7.4 Persistent Structures

### Persistent Structures

Persistent structures retain access to earlier versions after updates. Structural sharing avoids copying every element, but requires careful ownership, immutability, and garbage collection.

### Extended design study: fast updates in a shared research index

A lab keeps a list of experiment counts by day and must frequently update one day while answering sums over a date interval. Recomputing every interval sum from scratch takes time proportional to interval length. A prefix-sum array answers each query with two arithmetic operations, but updating one daily count may require revising every later prefix. A Fenwick tree instead maintains carefully chosen partial sums so both a single-index update and a prefix query take O(log n) time. The choice depends on the expected mixture of updates and queries; static prefix sums remain appropriate when data are immutable.

A Fenwick tree typically uses one-based indices. Entry `tree[i]` stores the sum of a suffix of the prefix ending at i, with block length given by the lowest set bit of i. A point update at index i modifies `tree[i]`, then repeatedly advances i by `i & -i` until it exceeds n. A prefix query accumulates `tree[i]`, then repeatedly subtracts the lowest set bit. A half-open interval sum `[l,r)` is calculated as `prefix(r)-prefix(l)` when `prefix(k)` sums the first k elements. Getting the boundary convention wrong is a frequent source of off-by-one defects.

A trie is useful for a different workload: searching strings by prefix. If a catalog contains cat, car, cart, and dog, the first three keys share the edges c→a, saving repeated storage of common prefix symbols. The trie must mark which nodes correspond to complete keys, because a prefix such as ca can exist without itself being a stored word. Tries can offer search time proportional to key length, but a naïve array of child pointers at every node may consume much more memory than compact alternatives. The claim of efficiency must specify whether time, memory, or prefix enumeration matters.

A disjoint-set union structure solves another different problem: maintaining components as relationships are added. A union merges two sets and find returns a representative. Union by rank or size and path compression produce very low amortized costs over a long sequence, even though a particular individual find may still follow several pointers. Persistent versions of these structures introduce additional design constraints. To preserve earlier versions of a segment tree, one can copy nodes only on the path affected by an update and share untouched subtrees. This supports historical queries at the cost of additional allocations and a version-management policy. These structures should not be merged into one "universal" implementation; they solve different operation sets.

## Worked problem 7.1

Insert cat, car, cart, dog into a trie. What strings match prefix ca and how many terminal nodes occur?

**Define the data and method**
Both cat and car share root→c→a. The node r is terminal for car, and its child t is terminal for cart; a different t is terminal for cat. dog starts with d.

**Derive and interpret the result**
Prefix ca matches cat, car, cart, and there are four terminal word markers overall. Shared prefixes save nodes but do not imply that every prefix is a full word.

## Worked problem 7.2

Initially 6 elements are singleton disjoint sets. Apply union(1,2), union(2,3), union(4,5), union(3,5). How many sets remain?

**Define the data and method**
The first union reduces six sets to five; the second to four; the third to three; and the fourth combines {1,2,3} with {4,5}, leaving {1,2,3,4,5} and {6}.

**Derive and interpret the result**
Two connected components remain. Union-by-rank and path compression improve the amortized cost but do not change the partition result.

## Worked problem 7.3

For array [2,1,3,4,5], calculate the sum over half-open interval [1,4), and describe a Fenwick-tree method.

**Define the data and method**
A half-open interval [1,4) includes indices 1,2,3, so 1+3+4=8. Compute prefixSum(4)-prefixSum(1), where prefixSum(k) sums the first k elements.

**Derive and interpret the result**
The result is 8. Each Fenwick prefix query takes O(log n), so the interval sum is O(log n) under the usual mutable prefix-sum representation.


### Applied investigation: Tries and Fenwick-tree prefix sums

A trie represents strings as paths labeled by characters, sharing a prefix when several words begin alike. Inserting cat, car and cart shares the ca prefix but introduces different terminal paths; a terminal marker is necessary to distinguish car from cart. Alphabet choice and Unicode normalization influence both memory cost and lookup behavior. Counting nodes does not prove a complete search or deletion implementation.

A Fenwick tree stores partial sums indexed by the least significant set bit. To compute a prefix sum at index i, repeatedly subtract i & −i from i, accumulating the tree values encountered. For updates, repeatedly add the same least significant bit to move to responsible ancestors. The indexing convention is one-based. Test sum of an empty prefix, last valid prefix, an update and a second query; a correct initial prefix sum is not sufficient evidence that updates work.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Tries, indexed aggregates, and persistent versions

A trie stores strings along paths whose edges correspond to characters or symbols. Its fundamental invariant is that the path from the root to a node spells a prefix of at least one stored key. Words such as cat, car and cart share the prefix ca, which reduces redundant storage of shared character transitions. The total space still depends on the representation of child maps and the number of distinct prefix nodes. A dense fixed alphabet array per node can waste space if most nodes have few children; a dictionary of existing children changes the constant factors and access characteristics.

The terminal marker is essential. If car and cart are both stored, reaching the node for car must indicate that car itself is a complete key, not merely a prefix. Deleting car should clear its terminal marker but retain the path needed for cart. Removing unused nodes is safe only after checking whether descendants or other terminal keys still depend on them. Unicode text complicates what a character means: byte sequences, code points and user-perceived grapheme clusters need not align, so normalization and locale behavior are part of the actual specification.

A Fenwick tree represents an array under point updates and prefix-sum queries. For positive one-based index i, the least significant set bit lowbit(i) = i & (−i) determines the range summarized at that position. A prefix query accumulates tree[i] and repeatedly subtracts lowbit(i) until reaching zero. An update adds a delta at i and repeatedly advances by lowbit(i). Each step clears or adds one relevant binary segment, giving logarithmic complexity in array length.

For values [2, 1, 3, 4, 5], the prefix sum of the first four values is ten. The Fenwick query starts at index four, adds the block covering positions one through four, and terminates at zero. To find the sum of positions three through five, subtract prefixSum(2) from prefixSum(5): fifteen minus three equals twelve. The range query is not a separate walk over the three individual entries. If values are updated, the tree must adjust exactly the affected aggregate blocks.

A segment tree offers a more general framework for interval aggregates. Each internal node combines the values of its children through an associative operation, for example addition, minimum or maximum. The identity value must match that operation: zero for addition and positive infinity for minimum. Lazy propagation can defer updates to entire ranges when the update and aggregate operations admit a correct composition law. A careless implementation that uses addition's identity for a minimum tree gives wrong results even if its tree navigation is perfect.

Persistent data structures preserve earlier logical versions instead of overwriting all nodes in place. A path-copying persistent tree can share most unchanged subtrees and allocate new nodes only along a modified path, resulting in logarithmic additional nodes per update for a balanced tree. Sharing requires immutability of the shared nodes; otherwise mutating a child through a new version corrupts the old one. Persistence is useful for undo history and snapshot semantics but creates storage-reclamation questions, since a retained old root keeps its reachable nodes alive.


### Indexed trees as mathematical summaries

### The Fenwick tree in binary

For an array A indexed from one to n, define lowbit(i) as i bitwise-AND negative i using two's-complement arithmetic. Fenwick entry F[i] stores the sum over the interval from i−lowbit(i)+1 through i. For example, F[8] covers eight values, F[12] covers positions nine through twelve, and F[10] covers positions nine and ten. To compute prefixSum(13), inspect F[13], then F[12], then F[8], and stop at zero. Those intervals are disjoint and together cover positions one through thirteen. The query uses no data-dependent search; its route comes from the bits of the index.

For A=[2,1,3,4,5,1,2,6], prefixSum(6)=16. The query visits F[6], which summarizes positions five and six, and F[4], which summarizes positions one through four. A point update adding three to A[6] modifies F[6] and F[8] but not F[4], since F[4] does not summarize position six. A correct test should compare every prefix sum to a direct array sum after each update, not only the total sum of the entire array.

### Segment trees and monoids

A segment tree applies a binary associative combine operation across intervals. Associativity means combine(combine(a,b),c)=combine(a,combine(b,c)), allowing the algorithm to group subintervals differently without changing the answer. Addition, minimum and maximum are associative. Subtraction is not, so a naive segment tree using subtraction as its combine operation would depend on traversal grouping and fail to represent a well-defined range subtraction in the intended sense. The operation also needs an identity element for empty disjoint pieces: zero for sum, positive infinity for min and negative infinity for max.

A segment tree over eight values has a root for the entire range, children for halves, and leaves for individual entries. To answer a range-sum query for positions three through six, descend only into nodes whose intervals intersect the query. Completely covered nodes contribute their stored aggregate; disjoint nodes contribute the identity. A point update changes the leaf and recomputes aggregates on the path to the root, taking logarithmic time when tree height is logarithmic.

### Range updates and lazy information

If adding delta to every value of an interval, a sum node fully covered by the update increases by delta times the number of represented elements. A lazy tag records the pending addition so the algorithm need not visit every leaf immediately. When that node is later partially queried or updated, push the tag to its children and clear or adjust the parent's pending state. For sums under additive updates, composing pending tags is addition. Other operations may have different composition laws, and not every data structure supports arbitrary combinations of update and query in the same way.

### Prefix indexes and dictionaries

Tries support prefixes but not automatically substrings. If the keys are cat, car and cart, a prefix query ca can enumerate all three. A query ar appears inside car, but a simple prefix trie does not provide a direct suffix or substring index. Suffix arrays, suffix trees or n-gram indexes solve related but different search problems. Keep the terminal marker separate from the existence of a prefix node so deleting one key does not erase a longer key that shares its path.

### Persistence and snapshots

A persistent segment tree creates a new root when an update occurs and shares all unaffected subtrees with the previous root. For a balanced tree, one update normally allocates a new node along each level of its root-to-leaf path. Queries against an earlier root still see earlier values. This requires immutable shared nodes; modifying a node in place could corrupt every version referencing it. Many versions can coexist, but retained roots keep old nodes alive, so version retention and garbage collection are part of the real storage cost.

### Verification workbench

Maintain a small reference array and random update/query sequences. For Fenwick trees, compare direct prefix sums to computed ones after every update. For segment trees, compare minimum and sum queries to direct slices, remembering the correct empty-range policies. For persistence, store copies of the historical reference arrays and verify that older version queries do not change when a new version is created. These oracle calculations are independent of the internal indexed-tree navigation and therefore catch errors that self-consistency checks can miss.


## Additional original authored teaching sections

# Specialized indexing structures and their operational boundaries

A prefix trie stores strings by following transitions for successive symbols. Its advantage comes from sharing prefixes: the strings `star`, `start`, and `stack` can reuse the first several transitions. Each node may record whether a complete key ends there; without that terminal marker, storing `star` and `start` can make it impossible to distinguish an actual word from a prefix that merely leads to a longer one. A search for a full key checks the terminal marker at the final node, whereas prefix search only checks whether the transition path exists. Confusing these operations is a common source of autocomplete defects.

A fixed array of child pointers per node supports constant-time transition indexing for a small known alphabet, but may waste memory when most nodes have only one or two children. A map of children reduces sparse allocation at the cost of hash or tree lookup and per-node container overhead. A compressed trie, or radix tree, stores multiple symbols along edges to avoid long chains of single-child nodes. These variants are worth comparing for a dictionary of natural-language words, a router's prefix table, and a collection of binary identifiers because alphabet size and shared-prefix distribution differ dramatically among them.

Disjoint-set union, also called union–find, represents a partition of elements into groups. Each element initially belongs to its own group. A `find` operation returns a representative for the containing group, while `union` merges the groups containing two elements. Union-by-size attaches the smaller tree below the larger root; path compression shortens parent chains while searching for representatives. The two techniques together give near-constant amortized operation time over long sequences in the classical analysis, but a representative's numeric identifier is not generally stable. It may change after a union. An application that stores representatives as permanent user-facing group IDs can break when future merges choose a different root.

Suppose elements one through six begin separate. Union one with two, two with three, and four with five. The structure now represents groups {1,2,3}, {4,5}, and {6}. Calling `find(3)` and `find(1)` must return the same root, but that root need not equal one. Union three with five must merge the first two groups, after which `find(2)` and `find(4)` agree. No operation in this trace should change membership of six. Tests should compare group equivalence relations, not force a particular parent-array layout; different valid union choices and path compressions can yield different internal forests.

A Fenwick tree, or binary indexed tree, efficiently maintains prefix sums over a sequence that receives point updates. Its array indexing uses the least significant set bit of each one-based index to identify ranges aggregated in each stored cell. To calculate a prefix sum, repeatedly subtract the low bit from the current index; to apply a point update, repeatedly add the low bit while inside the array. Both traverse logarithmically many indices. A Fenwick tree is compact and elegant for invertible prefix aggregation, but it does not automatically support every range operation. For example, finding a range minimum with arbitrary point replacements is not equivalent to subtracting two prefix minima.

Take one-based values [3,1,4,1,5,9]. Their prefix sums are [3,4,8,9,14,23]. If position four increases by two, all prefix sums at or beyond four increase by two, but earlier prefix sums remain unchanged. A correctly updated Fenwick tree must return [3,4,8,11,16,25] through its query interface without rebuilding the entire structure. The reference implementation can simply update the raw list and compute prefix sums by direct addition. Comparing the two representations after randomized updates catches incorrect low-bit increments, off-by-one errors, and missing termination conditions.

# Range queries, persistence, and versioned states

Segment trees store aggregate summaries over nested intervals. A node covers a range of positions and records a value derived from its children, such as their sum, minimum, or maximum. A point update changes one leaf and recomputes the summaries on its path to the root. A range query decomposes the requested interval into a logarithmic number of disjoint covered nodes under the standard balanced layout. Unlike a raw prefix-sum array, it can support many range aggregates without requiring an inverse operation. The aggregate function must obey an associative combination rule to make recursive grouping legitimate.

For example, storing minimum values allows the query for positions two through five to combine a few covered interval minima. There is no general subtraction operation that recovers the minimum of an arbitrary middle interval from a pair of prefix minima. This explains why a segment tree is suitable where a Fenwick tree's simple sum-difference technique is not. An efficient implementation should explicitly distinguish inclusive interval endpoints from half-open intervals; otherwise a query intended for [2,5] may accidentally omit position five. Empty ranges need a documented identity element or an error policy.

Lazy propagation supports updates to an entire range by deferring work. For range addition combined with range sum, a node covering length L may increase its stored sum by L times the pending increment. The pending increment is propagated to children only when a future operation requires it. The correctness invariant now relates each node's stored aggregate to a deferred update tag. Failure to scale the increment by segment length returns an incorrect sum; failure to push tags before descending can cause a later point query to see an outdated value. A useful test alternates whole-range additions with small-range queries and compares against a directly updated reference array.

Persistent structures preserve older versions after updates. A persistent segment tree can copy only the nodes along the update path, sharing untouched subtrees with the previous version. This creates a new root representing the updated collection while the old root remains valid for historical queries. The asymptotic extra storage per point update can be logarithmic rather than copying all n entries. Nevertheless, garbage collection and lifetime management become important: if no user needs an old root, retaining it unnecessarily can keep large shared subgraphs alive. Persistence guarantees historical logical views, not automatic storage reclamation.

Versioning creates semantic choices. A historical query must specify which version is intended, and an update may branch from a prior version rather than always extending the latest one. Some persistent structures support easy reads from old versions but permit edits only from the newest version; others support full branching persistence. If the application describes 'undo' without naming these distinctions, its desired behavior can be unclear. For a scientific data analysis tool, versioned arrays might let researchers compare results before and after calibration while retaining a reproducible record of transformations. The identity and provenance of each version matter as much as the data structure's efficiency.

A test suite for range indexes should generate a small reference array, perform deterministic and randomized updates, and query every short interval after each update. Use large negative values, zeros, repeated updates at the same index, and boundary positions. For persistent versions, store the reference array snapshot for every version and confirm that updating a new version never mutates answers from an old one. A simulation should make those version roots and shared subtrees visible and permit the learner to switch historical states; merely drawing a binary tree without executing the update rules misses the educational point.
