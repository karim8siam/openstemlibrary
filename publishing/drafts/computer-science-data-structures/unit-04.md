# Data Structures — Unit 4: Associative structures

**DRAFT — length threshold and independent review outstanding.**

## 4.1 Hashing

### Hashing

A hash maps a key into a bucket-selection code. Collisions occur when different keys share a bucket; correct tables still use equality to distinguish them. Hash stability and key immutability matter.

## 4.2 Collision Resolution

### Collision Resolution

Separate chaining holds colliding entries together. Open addressing probes alternative slots; deletion must preserve search chains, often through tombstones. Probing behavior depends on capacity and key distribution.

## 4.3 Load Factors

### Load Factors

The load factor is occupied element count divided by bucket capacity. It influences expected lookup cost but does not rule out pathological collisions. Chaining may have load above one, while open addressing cannot.

## 4.4 Resizing

### Resizing

Rehashing rebuilds a table at a new capacity and recomputes bucket placement. Geometric growth can make resize costs amortized manageable. All key–value pairs must survive a rebuild unchanged.

### Extended design study: a keyed measurement registry

A measurement application associates sensor identifiers with the latest observed reading. Operations include storing a reading, retrieving it by identifier, replacing an existing value, and removing a sensor. A hash table is a natural candidate, but its interface contract must distinguish absence from a present reading of zero. Returning zero for every missing identifier would make valid measurements indistinguishable from missing data. A tagged option value or a separate membership test makes the state observable. This example also shows why key equality and hash compatibility matter: two identifiers that compare equal must select compatible hash paths.

A collision is not evidence of an error. If integer identifiers 8, 15, and 22 are placed in a seven-bucket table by modulo arithmetic, they share one bucket. Separate chaining can retain all three entries and compare keys inside the chain. Linear probing instead walks subsequent slots until it reaches an unused location. Both approaches may have fast expected behavior for a suitable distribution but can perform poorly if many keys systematically collide. For open addressing, deletion must not confuse a previously occupied slot with one that has never been used, because a lookup may need to pass a deleted location to find a later element in the same probe sequence.

Resizing changes the mapping from hash codes to physical buckets. At capacity eight, a key assigned by `key mod 8` may move to a different bucket when the capacity becomes sixteen. Merely copying physical slots into the same positions in a larger array does not constitute a correct rehash, even if every item is still present somewhere. The rebuilding operation must preserve semantic pairs, recompute placements, and respect the collision-resolution strategy. For systems allowing concurrent readers and writers, a resize also raises synchronization questions; the single-threaded introductory model does not automatically transfer to a concurrent implementation.

A productive experiment constructs three key distributions: uniform-looking integers, sequential integers, and deliberately colliding integers. For each, collect average and maximum probe counts at a sequence of load factors. Verify every returned value using a simple reference dictionary. Do not infer that a nominal threshold such as 0.75 is universally optimal; its effect depends on probing method, cache locality, memory budget, hash cost, and the application's mix of successful and unsuccessful lookups. A practical engineering decision should document both the stated average-case assumptions and the failure mode under adversarial inputs.

## Worked problem 4.1

With a size-7 hash table and h(k)=k mod 7, where do keys 8,15,22 go under separate chaining?

**Define the data and method**
8 mod 7=1, 15 mod 7=1, 22 mod 7=1. All keys share bucket 1, which must store distinct key-value pairs and resolve equality within its chain.

**Derive and interpret the result**
Occupancy is 3 keys in bucket 1 and zero elsewhere. Hash collisions are legal and do not imply that keys are equal.

## Worked problem 4.2

Using linear probing in capacity 7, insert 8,15,22, then remove 15. Explain why slot 2 cannot be marked never-used.

**Define the data and method**
The keys probe to slots 1,2,3. Searching for key 22 probes 1,2,3. If slot 2 is treated as a never-used empty slot, the search would stop there and incorrectly report absence.

**Derive and interpret the result**
Use a tombstone or a carefully specified relocation algorithm. The proof of lookup correctness relies on distinguishing deleted and never-occupied slots.

## Worked problem 4.3

A hash table doubles capacity from 4 to 8 when adding the fourth key. Compute its load factor after inserting five keys.

**Define the data and method**
At five occupied entries and eight slots, alpha=n/capacity=5/8=0.625. Every existing key must be assigned a new bucket using the capacity-8 hash mapping.

**Derive and interpret the result**
The post-resize load factor is 62.5%. Reusing old bucket indices is unsafe because the modulus and collision pattern can change.


### Applied investigation: Hash collisions and open addressing

A hash function maps a key to an integer bucket index, but two different keys can map to the same bucket. Separate chaining stores colliding entries in a per-bucket collection. In the deliberately adversarial model, keys 1, 8, 15 and 22 all map to bucket one modulo seven. Looking up one key requires comparing stored keys, not merely finding its bucket.

Linear probing uses open addressing: on collision it checks successive slots modulo capacity until it finds an empty slot or the key. Deleted entries normally require a tombstone marker so search does not stop early. Performance depends strongly on load factor and clustered occupancy. Testing insertion into almost-full tables and search for a missing key exposes behavior that a simple collision trace omits. Rehashing changes both bucket count and placement, so a single static visualization is only a local experiment.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Hash maps and adversarial workload analysis

A hash map couples a hash function to an equality relation. A valid hash scheme requires equal keys to have equal hash codes, but unequal keys are allowed to collide. A classroom example that takes each integer modulo seven intentionally maps keys 1, 8, 15 and 22 to the same bucket. A chained hash table can store them all, preserving full keys and using equality checks within the chain. The simulation is designed to make that worst-case pattern visible. It does not demonstrate that all hash functions or workloads suffer the same concentration.

In separate chaining, insertion may place a new entry at the head of a bucket list or search for an equal key first. If the collection is a map rather than a multimap, blindly inserting duplicate keys breaks the map contract. In open addressing, every entry lives in the table itself and probing finds an available slot. Deleting an entry by making its slot completely empty can break lookup paths for keys placed after a collision. A tombstone or a carefully designed relocation procedure is needed, depending on the probing scheme.

Let a linear-probing table have capacity seventeen and hash h(k) = k mod 17. Insert keys 1, 18 and 35. They initially target slot one, so the final occupied run begins at slots one, two and three. A lookup for 35 must probe all three positions. If key 18 is removed and slot two is simply marked empty, a naive search for 35 will stop prematurely. A test that inserts three colliding keys, deletes the middle one, then searches for the last one is therefore much more diagnostic than independent successful insertions.

Load factor is the ratio of occupied entries to bucket or slot capacity, with a slightly different operational meaning for chaining and open addressing. As load factor rises, open-addressing probe clusters generally worsen; the amount depends on the probing strategy and key distribution. Resizing and rehashing can restore useful capacity, but resizing must account for all still-live keys and maintain equality semantics. A key with a mutable hash-relevant field can become effectively unreachable if its hash changes while it is in the map. This is why immutable keys or stable hash attributes are common requirements.

There are two distinct claims about hash-table complexity. Expected constant-time performance assumes a reasonable input distribution, a suitable hash family or randomization, and controlled load. A deterministic collision pattern can create linear probes or a long chain. Security-sensitive systems exposed to attacker-chosen keys may need collision-resistant hashing, randomized seeds or alternative worst-case structures. Even when denial-of-service is not a concern, latency percentiles can matter more than the mean.

An experiment should vary the hash function independently of the keys. Hold the inserted keys fixed and compare modulo seven, modulo eleven, and a mixing function whose behavior is clearly specified. Record bucket counts, maximum chain length and search comparisons. Do not interpret an arbitrary graphic labeled “collisions” as evidence about a real production language runtime, because different languages can use different resizing thresholds, hash mixing, bucket structures and ordering guarantees.


### A collision-focused hash-table laboratory

### An implementation with explicit tombstones

Build a linear-probing map with an array of slots, each in state EMPTY, OCCUPIED or DELETED. To find a key, start at hash(key) modulo capacity and inspect a sequence of slots. If an occupied slot has an equal key, return its value. If a slot is DELETED, continue because keys may have been displaced past it. If an EMPTY slot is reached, the lookup can stop under standard linear probing because insertion would not have passed an empty slot on that probe path. This distinction is the reason deletion cannot simply reset every removed slot to EMPTY.

Insertion scans the same probe path, remembers the first deleted slot and checks whether a matching occupied key already exists. If so, update the value and preserve map cardinality. Otherwise place the new entry into a suitable deleted or empty position. The algorithm must still search through deleted positions to avoid creating duplicate keys. Rehashing into a larger table clears tombstones and redistributes entries. Counting occupied slots alone understates the cost of an overloaded table with many tombstones; an implementation may need to track both live entries and ever-used slots to decide when to rebuild.

### An exact adversarial trace

Let capacity be seventeen and h(k)=k mod 17. Insert 1,18,35,52. Their initial bucket is one, so linear probing places them into slots one through four. Remove 18: slot two becomes a tombstone. Searching for 52 must visit slots one, two, three and four. Inserting 69 may reuse slot two but must first verify no occupied 69 is later in the cluster. This example contains a deletion correctness issue and a performance issue: a sequence of colliding keys creates a long cluster even when the overall table is far from full.

Double hashing changes the probe step, typically using a second hash value that is relatively prime to table capacity so the sequence can visit all slots. Quadratic probing uses a nonlinear displacement sequence, but not every arbitrary table capacity and formula guarantees that every slot is reached. These are algorithm design choices, not cosmetic variations. A correct implementation specifies which table sizes are allowed, how a full-cycle search terminates, and how replacement or deletion works under its chosen probe strategy.

### Semantic consistency for real keys

Hashing a string creates a representation of its bytes, characters or normalized form. If equality treats canonically equivalent Unicode strings as equal but hashing uses different byte representations, the equal-hash requirement is violated. Floating-point keys present other corner cases: positive and negative zero typically compare equal in standard numerical equality and should receive compatible hashes, while not-a-number values require an explicit library policy. Composite objects need stable equality and stable hash fields while stored. Mutating a key after insertion can make the map unable to find its own entry.

### Load factor and resizing decisions

For separate chaining with n entries and m buckets, expected chain length depends on n/m under distribution assumptions; for open addressing, performance often deteriorates steeply as occupancy approaches capacity. A measured average under uniformly random keys is not a guarantee against adversarial collisions. Resizing by a factor near two permits amortized reasoning similar to dynamic arrays, but each resize recomputes bucket placements, and the threshold for resizing should be chosen by empirical workload and latency goals.

### Comparison to ordered maps and probabilistic filters

A balanced search tree map offers ordered iteration and worst-case logarithmic operations under its balancing contract. A hash map offers expected near-constant-time exact lookup but no intrinsic sorted order. A Bloom filter adds an orthogonal idea: it represents approximate set membership compactly, allowing false positives but—under ordinary non-deleting operation and correct hashing—no false negatives for inserted keys. A Bloom filter is not a replacement for a map that must retrieve associated values. The decision depends on what a query actually needs.

### Verification workbook

Use a reference dictionary to evaluate one thousand generated operations, including repeated insertion, deletion of absent keys and deliberate collisions. Record a small trace when a mismatch occurs. Assert that every occupied key is reachable by its own lookup; that deleting one colliding key leaves the others reachable; and that rehashing preserves all values. Analyze collision histograms separately from operation counts. The provided collision simulator deliberately maps many keys to one bucket; it illustrates a mathematical worst case and should never be described as measured production performance.


## Additional original authored teaching sections

# Hash tables under unusual keys and adversarial access

A hash table has two relationships to preserve. First, equivalent keys must map to equivalent hash outcomes under the chosen equality policy. Second, a stored key must remain discoverable after collisions and updates. The first is a semantic rule, whereas the second is a representation invariant. A collision means different keys produce the same initial bucket or probe path. It is not itself a correctness failure. Correctness fails when insertion, lookup, and deletion do not agree about how to search the affected bucket group.

For separate chaining, each bucket contains a collection of entries that share an initial hash index. Lookup scans entries in the selected bucket and compares complete keys using the equality relation. A common cost model assumes a sufficiently well-distributed hash function; then expected chain length is linked to the load factor, the number of entries divided by the number of buckets. If inputs are chosen to collide intentionally, one chain may contain most of the entries, making lookups linear in the chain length. A performance statement must say whether it assumes random keys, random hashing, a known input distribution, or a defense against adversarial keys.

Open addressing places entries directly in table slots. Linear probing checks consecutive positions after the initial bucket, wrapping around as needed. The table must maintain a termination condition even when nearly full, and deletion requires careful handling of probe continuity. Consider capacity eleven and a hash of `key mod 11`. Inserting 3, 14, and 25 occupies positions three, four, and five. If the key fourteen is removed by marking its slot empty, a subsequent search for twenty-five may stop at position four and incorrectly conclude that the key is absent. A tombstone records that the slot can be reused but cannot terminate an existing probe sequence. Rebuilding the table clears accumulated tombstones and restores efficient probing.

Linear probing has good locality because nearby slots tend to occupy nearby memory, yet it can suffer primary clustering. Quadratic probing and double hashing alter the probe pattern, but the chosen arithmetic must still guarantee a suitable search path. A nonzero second-hash step that shares a factor with table capacity may visit only a subset of slots. For instance, stepping by four in a table of capacity twelve visits only three distinct positions before repeating. If the table's implementation assumes that one probe sequence reaches every slot, it can report 'full' while free slots exist. A robust implementation chooses compatible table sizes and steps and tests full-cycle behavior.

Key mutability is an underappreciated source of bugs. Suppose a dictionary uses an employee object as a key and computes the hash from the employee's display name. If the display name is edited after insertion, lookup can visit a different bucket and fail to find the same object. The correct choice is often an immutable internal identifier. For composite keys, define stable field equality and field hashing consistently. If a coordinate pair is used as a key, decide whether two floating-point values that differ by a tiny tolerance count as equal; approximate equality is difficult to combine safely with conventional hashing because it may not define a true equivalence relation.

Text keys introduce normalization questions. Two strings may display identically while differing in Unicode representation. If the application treats canonically equivalent strings as equal, normalize them consistently before both hashing and equality comparison. Case-insensitive email handling, locale-specific case folding, and path canonicalization are domain-specific decisions; a hash table must not silently invent those semantics. Hash values are implementation aids, not meaningful permanent identifiers. Storing a raw runtime hash code as a stable database key can fail after a language-version change, random-seed change, or platform migration.

Hash-flooding attacks exploit predictable collisions to consume CPU. A public-facing application that accepts untrusted keys should evaluate whether a keyed hash function, bucket treeification, or another collision-resistant strategy is necessary. Cryptographic collision resistance and table distribution are not synonymous, but predictable weak hashes can create exploitable worst cases. The implementation should also cap resource consumption, validate request sizes, and avoid leaking raw internal hash seeds. An algorithm that is usually fast on trusted demo inputs may behave differently under adversarial traffic.

# Rehashing, concurrency, and an independently checkable experiment

Growing a hash table means building a new representation with a new capacity and relocating each live entry according to the new bucket rule. Merely copying entries into the same array positions is usually wrong because the bucket index depends on capacity. The operation has linear work in the number of live entries in a simple sequential implementation. With geometric growth, the total copying across many inserts can have favorable amortized bounds, but one growth step may be expensive enough to affect application latency. An implementation can spread relocation across multiple operations, yet incremental rehashing has additional invariants: while the transition is underway, lookups may need to search the old table, the new table, or both.

A resize example reveals this dependency. Suppose a map with five buckets contains keys 2, 7, and 12, all colliding under modulo five. Expanding to eleven buckets sends the keys to buckets two, seven, and one respectively. If the existing chain is copied into bucket two without recomputing hashes, lookup for key twelve under modulo eleven searches bucket one and fails. Every entry must be reinserted or otherwise relocated according to the new policy. This is not an optimization detail; it is a correctness condition.

Concurrent access creates a separate challenge. Two threads inserting into the same bucket without synchronization may overwrite each other's links or lose an increment to the entry count. A reader that observes a partially updated probe array can return an incorrect result. Locks, carefully designed atomic operations, or immutable snapshots can establish consistency, but their performance must be measured under contention. A concurrency claim needs a precise semantic target: linearizability means each public operation appears to take effect at one instant between its call and return, while weaker consistency models offer different guarantees. A sequential data structure's proof does not automatically prove its concurrent version.

To test a sequential map, generate random operations: insert or replace a key, remove a key, lookup an existing key, and lookup a missing key. Apply every operation to a simple reference dictionary and compare return values and final contents. Force collisions by choosing keys with the same residue modulo capacity. Trigger resizes at exactly the load-factor threshold, not only far before and after it. Delete from the middle of a probe cluster and check that later keys remain reachable. Repeat after inserting into tombstones. Track the number of live entries and assert that a replacement does not increase that count.

For a multi-threaded map, tests must go beyond running the same sequential oracle in different threads. Construct schedules where two writers target the same key, one reader races with a resize, and deletion occurs during a chain traversal. Record operation invocation and completion times and compare short histories to a reference specification when checking linearizability. Some races are rare, so randomized stress tests should be supplemented by deterministic schedule control or instrumentation. A test suite that passes one thousand sequential operations cannot certify freedom from concurrent lost updates.

Finally measure collision frequency, probe length distribution, resize count, memory overhead, and high-percentile latency. Under uniform keys, report the distribution of observed probes rather than just one average. Under adversarial keys, report how gracefully performance degrades. Under delete-heavy workloads, report the tombstone fraction and rebuild behavior. These diagnostics explain why a map performs as it does; they also provide a reproducible basis for comparing chaining, linear probing, double hashing, and ordered-tree alternatives. A meaningful teaching simulation should expose these state variables instead of displaying only an attractive collection of buckets.
