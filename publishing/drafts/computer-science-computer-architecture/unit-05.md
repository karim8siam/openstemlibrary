# Computer Architecture — Unit 5: Memory hierarchy

## 5.1 Caches

**Core model — Caches**

Caches exploit spatial and temporal locality by retaining data in blocks near the processor. Mapping policy, block size and associativity shape hit behavior.

**Original worked illustration**

With 16-byte blocks, addresses 0 and 12 lie in the same block while address 16 belongs to the next block. A sequential scan can benefit from spatial locality.

**Boundary conditions and checks**

Increasing block size can waste bandwidth on unused bytes; conflict misses occur even when total cached capacity appears sufficient.

### Extended technical chapter: Caches

A cache stores copies of selected memory blocks closer to the processor. Temporal locality motivates reuse of recently accessed data; spatial locality motivates fetching neighboring bytes in one cache line. A reference to an address is partitioned into block offset, set index, and tag under a chosen cache organization. For a direct-mapped cache with four sets and sixteen-byte blocks, byte addresses zero and sixty-four have block numbers zero and four and both map to set zero. Alternating access between those two blocks causes repeated conflict misses even though the working set is only two lines. Increasing associativity can retain both blocks in one set, provided capacity and replacement rules permit it.

Separate compulsory, capacity and conflict misses. The first access to a line in an empty cache is compulsory. A working set larger than total available cache capacity can cause capacity misses even with fully associative placement. Set conflicts can evict useful data even though other cache sets are empty. In a realistic system, classification depends on the idealized reference model and replacement policy. Average memory access time is often approximated as hit time + miss rate × miss penalty. If hit time is one nanosecond, miss rate 4 percent and extra miss penalty 50 nanoseconds, the model produces three nanoseconds average; it does not mean every access takes three nanoseconds. Real out-of-order processors can overlap misses, and multiple cache levels complicate the arithmetic.

Line size, capacity, associativity, replacement and write policy interact. A larger line may exploit spatial locality but waste bandwidth on irregular workloads. A write-through cache propagates writes along the hierarchy by its policy; a write-back cache can postpone lower-level writes until eviction of a dirty line. An educational cache trace should annotate each access with byte address, block number, set, tag, hit/miss outcome, replacement victim and dirty status. Re-run the same trace under direct mapping and two-way set associativity. Without changing the addresses, explain why the miss count changes. Never extrapolate a tiny synthetic trace to a real processor's latency without qualifying the enormous difference in parallelism and system activity.

## 5.2 Virtual Memory

**Core model — Virtual Memory**

Virtual memory provides each process with translated virtual addresses, using page tables and protection checks. The virtual address can be divided into page number and offset.

**Original worked illustration**

For 4 KiB pages, virtual address 8197 has page number 2 and offset 5 because 8197 = 2*4096+5.

**Boundary conditions and checks**

A TLB miss is not automatically a page fault; the page-table entry may be present in main memory.

### Extended technical chapter: Virtual Memory

Virtual memory gives each process an address space abstraction rather than exposing raw physical DRAM addresses. A memory reference uses a virtual address that must be translated to a physical address while permissions are enforced. Page-based systems divide the address space into fixed-size pages; a page-table entry maps a virtual page number to a physical frame number or indicates a special condition such as not-present. A process may legally address a virtual page that is not currently resident, triggering a page fault. That fault is not automatically a program error: the operating system may load the page, allocate backing storage, or reject the access depending on the mapping and permissions.

With 4096-byte pages, the twelve least significant address bits form the page offset. A virtual address 0x12345 therefore has an offset of 0x345, while the remaining upper bits select a virtual page number. Translation replaces the virtual page number with a physical frame number while retaining the offset. If the mapping points to physical frame 0xAB, the resulting physical address is 0xAB345. This exercise describes the structure of a translation; it does not assert a particular number of page-table levels, address-space width or processor architecture. Most contemporary systems contain page-walk caches, TLBs and additional protection features that change the timing.

Virtual memory is also a protection boundary. A user process generally cannot access arbitrary kernel-only mappings or write to a read-only page merely by computing its address. Address-space layout randomization makes selected mappings less predictable but does not replace permission checks. Copy-on-write allows two mappings to share a physical page until a write requires separation. A complete laboratory should trace a page-table hit, a TLB miss with valid translation, a not-present fault resolved by the operating system, and a permission violation. Identify which layer detects each condition and distinguish correctness from performance. Memory-mapped I/O and device-managed translation add further cases, so avoid calling all addresses ordinary DRAM.

## 5.3 Translation

**Core model — Translation**

Address translation combines a virtual page number with an offset that remains unchanged for equal page sizes. Translation caches accelerate this lookup.

**Original worked illustration**

A virtual page 7 with offset 123 mapped to physical frame 11 produces physical address 11*4096+123=45179 for 4 KiB pages.

**Boundary conditions and checks**

Permissions, page size and frame mapping must be checked before trusting a numeric translated address.

### Extended technical chapter: Translation

Address translation commonly benefits from a translation lookaside buffer, a small associative cache of recent virtual-to-physical mappings. A TLB hit bypasses some or all page-table lookup work; a miss triggers an architectural or software-controlled walk depending on the system. An effective-address computation performed by an instruction is not the same as a successful translation. In particular, a pointer can be within the integer range representable by a register but outside a mapped region or barred by access permissions. Hardware checks the mapping's attributes, often including read, write, execute and privilege restrictions.

Consider a toy TLB with capacity two entries and least-recently-used replacement, initially empty. Access virtual page numbers A, B, A, C, B. The first two accesses miss and fill the TLB. The third hits A and makes it recently used. C then misses and replaces B. The final B access misses and replaces A. The sequence has one hit and four misses. This is a deterministic trace, not a measured hardware miss rate. If page-table lookup adds forty cycles only on a TLB miss, a naive non-overlapping model assigns 160 extra cycles to the five references. A real core might overlap some translations, prefetch, or use multiple TLB levels.

Page-table organization balances address-space flexibility, memory overhead, and walk latency. Multilevel tables avoid allocating entries for large unmapped regions, while huge pages cover larger contiguous regions with fewer translation entries at the cost of internal fragmentation and mapping flexibility. The exercise should compare 4 KiB pages and 2 MiB pages for a hypothetical contiguous 1 GiB allocation, calculating entries required and considering TLB reach. It should also describe a sparse address space where huge pages are inappropriate. When a context switch or page-table update occurs, cached translations require correct coherence or invalidation mechanisms. The precise shootdown details are platform-dependent; their existence is central to correct address-space isolation.

## 5.4 Locality

**Core model — Locality**

Locality is an empirical property of access traces, not a guaranteed application trait. Working-set size matters more than raw cache capacity for many workloads.

**Original worked illustration**

For repeated accesses [0,1,2,0,1,2], a cache holding three blocks can retain all references after initial misses; capacity two may thrash under an unfortunate replacement policy.

**Boundary conditions and checks**

A perfectly sequential scan can have excellent spatial but weak temporal locality once its working set exceeds cache capacity.

### Extended technical chapter: Locality

Locality is a property of an access pattern, not a magic feature of a cache. Traversing an array sequentially often benefits from spatial locality because neighboring elements occupy nearby memory addresses. Reusing a small set of variables in an inner loop benefits from temporal locality because recently fetched lines remain useful. A linked list with nodes scattered through memory has different behavior: it may suffer cache misses even though it performs fewer arithmetic operations. Data layout and algorithm choice therefore influence memory behavior at least as strongly as nominal CPU speed.

Suppose a row-major matrix has 1024 columns of four-byte integers and a cache line holds sixty-four bytes. Reading across a row uses sixteen integers per line. Reading down a column instead jumps 4096 bytes between successive elements, potentially touching one new line per access. The full-matrix traversal eventually reads the same number of values, but its immediate working set, reuse distances, and prefetch opportunities differ. Cache capacity and associativity determine the actual difference. This is why a matrix-transpose implementation often uses tiling: small blocks permit repeated use of cache-resident data before moving to the next region.

A locality investigation must define reuse distance, line size, and cache assumptions. For an address trace, count unique lines and record the number of intervening distinct lines between repeated accesses. Then compare naive and tiled matrix multiplication. A blocked algorithm may execute the same mathematical number of multiply-adds but reduce transfers between levels of the memory hierarchy. Multi-core interference, NUMA placement and write-allocate behavior complicate the picture further. Avoid concluding that sequential access is always faster: vectorization, compiler loop transformations, and prefetch engines can alter outcomes. The strongest statement connects a precisely described access pattern to a specific memory model, then reports measurements under a documented machine configuration.

### Integrated laboratory: one memory trace under four organizations

Define a byte-addressed machine with sixteen-byte cache lines. A direct-mapped L1 cache has four sets and is initially empty. Execute the address trace 0, 4, 8, 64, 0, 64, 16, 20, 0. The first three addresses occupy one cache line, so only the access at address zero is a compulsory miss; accesses four and eight are hits. Address sixty-four belongs to block four and maps to the same set as block zero, evicting it. The next access to zero therefore misses and evicts block four; the following access to sixty-four misses again. Addresses sixteen and twenty occupy block one, making sixteen a miss and twenty a hit. The final zero misses because it was replaced by sixty-four earlier. The resulting direct-mapped count is six misses and three hits for this particular trace.

Repeat the trace using a two-way set-associative cache with two sets but the same total line count of four, and an LRU replacement rule. Blocks zero and four now both map to set zero, which holds two ways, so they can coexist. The first reference to each block misses, as does the first reference to block one; all their later references hit. This gives three misses, assuming no other blocks enter set zero. The example illustrates conflict misses without changing the program's semantic memory requests. It does not claim that doubling associativity always halves misses: replacement behavior, tag comparison and hit time may change, and some traces cannot benefit.

Address translation adds another layer. Suppose pages are 4096 bytes and virtual page 0x12 maps to physical frame 0xAB. Virtual address 0x12345 contains virtual page number 0x12 and offset 0x345, producing physical address 0xAB345. An access to a page without a valid translation may trigger a page fault rather than continuing to the physical cache. The lab must specify whether the cache is indexed with virtual or physical address bits and whether a TLB sits before the relevant tag lookup. For a simple teaching model, translate first, then access the physically addressed cache; later discussions can explain how real L1 caches overlap some translation and indexing work.

Now study locality by changing the application access order. A row-major matrix traversal over contiguous 32-bit integers consumes sixteen elements per 64-byte cache line. Visiting every sixteenth element instead may use the same number of arithmetic instructions but extract fewer useful values from each fetched line. The comparison depends on matrix dimensions, loop order, line size and cache capacity. If the entire data set fits in a cache, an irregular traversal may still perform well after warm-up. When designing the experiment, flush or warm caches consistently and report both cold-start and steady-state results rather than mixing them.

Compute a first-order average memory access time: assume L1 hit time one nanosecond, miss rate ten percent and extra miss penalty forty nanoseconds. The result is 1+0.1×40=5 nanoseconds. Reducing the miss rate to five percent gives 3 nanoseconds, a reduction of forty percent in the model. But these averages are not guaranteed per-access latencies; multiple outstanding misses and out-of-order execution can hide some memory delay. To estimate total program benefit, determine what fraction of the baseline execution was actually stalled on memory. Optimizing memory hits cannot accelerate unrelated serial work.

The written report should identify the exact tag, index and offset decomposition for every address; present both cache-state tables; show one translated virtual address; and describe whether observed speedup depends on cache capacity, locality or prefetching. Include a deliberately adversarial trace alternating colliding addresses. Finish by explaining why 'the cache has enough bytes to hold both objects' is not sufficient to guarantee both remain resident in a direct-mapped organization. That distinction is essential for understanding architecture-sensitive performance anomalies.

### Review lens: why a faster cache test may not speed the application

A synthetic cache trace reports hits and misses under an exact address sequence. An application contains instruction fetches, data access, prefetches, speculative traffic and other threads that can alter the sequence actually reaching each cache level. Even a sharp reduction in modeled miss rate does not guarantee comparable end-to-end speedup if the processor hides misses behind independent work. Conversely, fewer misses may also save energy or reduce contention even when response time hardly changes. Evidence should include working-set size, line size, set count, associativity, replacement policy, write behavior and whether the trace is cold or warm. For translation experiments, page size and TLB organization also matter. A reproducible result should name one behavior that would falsify its proposed explanation, such as changing cache associativity without changing total capacity and observing whether the claimed conflict pattern disappears.

### Additional guided investigations for the memory stack

**Cache indexing.** For sixteen-byte blocks in a four-set direct-mapped cache, map addresses 0, 16, 64 and 80 to (block,set) pairs: (0,0), (1,1), (4,0) and (5,1). The first pair and third pair conflict in set zero; the second and fourth conflict in set one. Explain why adding cache capacity by increasing the number of sets can resolve some conflicts, whereas adding line size without changing sets may produce a different access grouping. This is an exercise in addresses and modular arithmetic, not a prediction of measured cache time.

**Page split.** Take decimal virtual byte address 12345 with four-KiB pages. Three complete pages account for 12288 bytes and leave offset 57; the virtual page number is three. Suppose page three maps to physical frame forty. Physical address is 40×4096+57=163897. Verify the offset lies within [0,4095]. If the mapping is read-only, a read may succeed while a write must follow the architecture's protection-fault behavior. Translation and permission checking must both be present in the state model.

**TLB replacement.** Simulate a two-entry fully associative TLB under LRU on virtual-page sequence A,B,A,C,B,C. Begin empty. A and B miss; the second A hits and becomes most recent; C misses and evicts B; B misses and evicts A; the final C hits if still resident. Count hits and misses, and state exactly when LRU metadata updates. Repeat with FIFO: because hits do not change FIFO insertion order, the victim choice can differ. Reproducibility requires the policy, initial state and tie-breaking behavior.

**Layout investigation.** A contiguous array of 1024 four-byte integers occupies 4096 bytes, or sixty-four 64-byte cache lines if aligned. Sequential traversal should require at most one first-touch miss per line in a non-evicting ideal cache, whereas accessing one integer per line gives only one sixteenth of each fetched line's content as useful data for that pass. Real prefetch and replacement may modify timing. Build a separate result table for bytes transferred and useful elements consumed, not just the number of instructions executed.

### Diagnostic challenge: miss count versus stalled time

Suppose a memory trace has one hundred accesses, ten L1 misses and an additional penalty of forty cycles per miss. A purely serial, non-overlapping model adds 400 miss cycles. If another arrangement halves the misses to five, the model predicts 200 saved cycles. But in an out-of-order machine, some misses may overlap with independent computations or each other; saving five misses does not necessarily save exactly 200 wall-clock cycles. Construct an extreme comparison where all missed loads depend on previous results, then another where ten independent loads can proceed concurrently. Both may have equal miss counts yet different critical paths. Add page-translation activity: TLB misses can occur even for L1 cache hits, so one cannot infer translation cost from cache miss count. The useful output is a miss classification, an ordering/dependency graph and a labeled statement of how the time model handles overlap. This tests understanding of memory latency rather than memorization of the average memory access time equation.

## Three worked problems

### Caches: worked application 1

For 16-byte cache blocks, do addresses 0 and 12 map to the same block?

**Set up the model and conditions**

Block number is floor(address/16).

**Carry out the calculation or proof**

Both floor(0/16) and floor(12/16) are zero.

**State the result and its scope**

They share cache block zero; address 16 is in block one.

**Independent verification, conditions, and interpretation**

A cache block containing sixteen bytes covers a contiguous aligned address range. The block number for a byte address a is floor(a/16). Address zero lies in block zero because floor(0/16)=0. Address twelve also lies in block zero because floor(12/16)=0. The offset values within that line are zero and twelve, respectively. Address sixteen begins block one, since floor(16/16)=1. The result concerns block identity, not necessarily the cache set. A direct-mapped cache needs an additional number of sets to determine which set a block maps to. For four sets, blocks zero and four collide in set zero, whereas blocks zero and one use different sets. A miss is not implied by merely observing that addresses occupy different blocks: both may already reside in the cache. Likewise, sharing a block does not guarantee a hit if the line has been evicted. To independently check boundaries, inspect the final byte of block zero, address fifteen, and the first byte of block one, address sixteen. Write the full interval as [0,15] to avoid confusing sixteen-byte length with an inclusive ending address.

### Virtual Memory: worked application 2

For a 4 KiB page size, find page and offset of virtual address 8197.

**Set up the model and conditions**

Use divisor 4096 bytes.

**Carry out the calculation or proof**

8197=2×4096+5.

**State the result and its scope**

Virtual page number is 2 and offset is 5.

**Independent verification, conditions, and interpretation**

A page size of 4 KiB means 4096 bytes per page. For virtual byte address 8197, compute the integer quotient and remainder on division by 4096. Two complete pages account for 8192 bytes, leaving remainder five. The virtual page number is therefore two and the page offset five, with zero-based page numbering. The check reconstructs the original address: page×page_size+offset = 2×4096+5=8197. The offset is within the required range from zero through 4095. In hexadecimal, 8197 is 0x2005, making the low twelve bits 0x005 and the higher page index 0x2. This is only decomposition of a virtual address; it does not identify the physical frame or prove the page is mapped. A page-table entry and permission state are required for translation. If that virtual page is not resident, a page fault may be resolved or rejected depending on operating-system policy. Changing page size to two MiB changes the split substantially, so all page calculations must state page size explicitly.

### Translation: worked application 3

Translate virtual page 7 offset 123 to physical frame 11 with 4 KiB pages.

**Set up the model and conditions**

Translation replaces the virtual page number with physical frame number.

**Carry out the calculation or proof**

Physical byte address = 11×4096+123.

**State the result and its scope**

The address is 45179.

**Independent verification, conditions, and interpretation**

A translated physical address keeps the offset and substitutes the mapped physical frame number for the virtual page number. For 4 KiB pages, a physical frame numbered eleven begins at byte address 11×4096=45056. Add the original offset 123 to obtain 45179. As a hexadecimal cross-check, frame eleven is 0xB and offset 123 is 0x07B, producing physical address 0xB07B. The virtual page number seven is important only for finding the mapping; after the mapping is selected, the physical frame number determines the new page base. A protection check must also confirm that the attempted read, write or instruction fetch is allowed. The address arithmetic cannot indicate whether the mapping is writable or present. The example assumes equal-sized virtual and physical pages and a straightforward mapping to a frame. Huge pages, nested translation for virtual machines, and memory-mapped I/O introduce additional details but preserve the basic principle that offset within a page stays unchanged by ordinary page translation. A sound trace records the original virtual address and final physical address separately.
