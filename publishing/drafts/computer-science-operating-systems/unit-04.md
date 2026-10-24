# Operating Systems — Unit 4: Memory management

allocation; paging; virtual memory; replacement policies

## §4.1 Allocation

**Core model — Allocation**

Memory allocation manages free regions and object lifetimes. Fragmentation can be internal (unused space inside allocations) or external (free space split into small pieces).

**Original worked illustration**

Allocating a 100-byte object in a 128-byte size class leaves 28 bytes of internal fragmentation before allocator metadata.

**Boundary conditions and checks**

Low allocation latency does not prove low memory use; page granularity, alignment and long-lived holes change capacity planning.

### Allocators, object lifetimes, and fragmentation

An allocator converts requests for memory regions into managed blocks, with constraints on alignment, sharing, and lifetime. Internal fragmentation is unused space inside an allocated region. External fragmentation is free space dispersed among blocks so that a large request cannot be satisfied despite adequate total free bytes. They are distinct from process address-space fragmentation and from physical memory pressure. A request for 100 bytes placed into a fixed 128-byte size class wastes 28 bytes of block capacity before allocator metadata; the ratio can be described relative to allocated bytes or requested bytes, but the denominator must be stated. For many small objects, metadata, alignment, and caching of free blocks can dominate apparent efficiency.

First-fit, best-fit, segregated size classes, slab allocation, and buddy allocation have different trade-offs. First-fit selects the earliest sufficiently large free span under a chosen traversal order; it does not necessarily minimize leftover waste. A buddy allocator splits power-of-two blocks and can coalesce only when matching buddies become free. That design makes split/coalesce operations systematic but may overallocate for an awkward request size. A slab allocator maintains caches of similarly sized kernel objects, improving locality and avoiding repeated general-purpose metadata work, at the cost of reserved capacity when objects are not actively needed.

Memory lifetime errors are correctness bugs, not merely inefficiencies. Returning a pointer to an object after its storage has been freed creates a dangling reference; freeing the same allocation twice can corrupt allocator metadata; losing every reference to an allocated object leaks memory until reclamation. Automatic memory management mitigates some failure modes but introduces collection scheduling, retained-object graphs, and runtime overhead. A lab should trace allocation and free requests as a sequence of labeled intervals, compute both internal and external fragmentation, and display an allocation failure despite sufficient *aggregate* free space. Then repeat with compaction allowed in an abstract model. Real C and C++ allocators cannot always move arbitrary live allocations, because programs may store untracked pointers; the compaction thought experiment must state its assumptions.

## §4.2 Paging

**Core model — Paging**

Paging maps fixed-size virtual pages to physical frames. Page tables record mappings and permission bits; TLBs cache recent translations.

**Original worked illustration**

For 4 KiB pages, address 12290 is virtual page 3 and offset 2. A valid mapping to physical frame 8 produces address 32770.

**Boundary conditions and checks**

A TLB miss can be resolved from page tables without disk I/O, while a true page fault may require zero-filling or paging storage.

### Page tables, address decomposition, and permissions

A page-based virtual memory system splits a virtual address into a virtual page number and a page offset. With 4 KiB pages, the offset occupies twelve bits because 4096 equals 2^12. To translate virtual address 12290, divide by 4096: the page number is three and the offset is two. A page-table entry, if present and accessible, yields a physical frame number; physical address computation combines that frame with the unchanged offset. The arithmetic is straightforward, but the operating system must also enforce the page's access attributes. A write to a read-only mapping is not authorized simply because its virtual page number is valid.

Large virtual address spaces make a flat page table wasteful when most addresses are unused. Multi-level structures allocate lower-level pages only where needed, reducing metadata for sparse address spaces at the expense of multiple memory accesses on a miss. Translation lookaside buffers cache recently used translations, so many references can avoid repeating the walk. An effective access time model might use a TLB hit fraction h, TLB lookup cost t, memory cost m, and a page-walk cost k*m on misses: expected time approximately t+h*m+(1−h)*(k*m+m), under explicit assumptions about serialized accesses and absent faults. Real CPUs overlap work and cache page-table entries, so this is an educational estimate, not a prediction of measured latency.

An address-space switch may change the meaning of the same virtual page number. Two processes can each map page three to different physical frames. Shared memory instead arranges for distinct or identical virtual addresses to refer to a common physical backing. Copy-on-write allows initially shared pages to diverge after a write fault, preserving private-state semantics without eager copying. A lab should implement a tiny table mapping virtual page numbers to frame numbers with read/write/execute permissions, then submit reads and writes near page boundaries. Print a translation or a specific fault reason: not-present, permission denied, or malformed address. Keep address translation separate from the question of whether a fault is ultimately recoverable, since demand paging may resolve a missing mapping.

## §4.3 Virtual Memory

**Core model — Virtual Memory**

Virtual memory provides isolation and a large sparse address space but can create faults and expensive working-set misses.

**Original worked illustration**

A process can reserve many virtual pages without committing equivalent physical frames until access, subject to the OS policy.

**Boundary conditions and checks**

Overcommit does not create RAM. When active pages exceed available memory, page replacement and thrashing can overwhelm useful work.

### Demand paging, working sets, and fault cost

Virtual memory can present an address space larger than the immediately resident physical memory by retrieving or creating pages when referenced. A page fault is a processor-detected condition that transfers control to the operating system for resolution or termination. Not every fault implies disk I/O: a zero-fill-on-demand page may be supplied from available RAM, a copy-on-write page may be copied, and a protection violation may be fatal to the process. A major fault that requires backing-store reads generally costs orders of magnitude more than a normal memory access. A performance analysis must distinguish those pathways rather than treating 'fault count' as a single uniform time charge.

A working set is the collection of pages a program actively references over a relevant window. If the combined active working sets exceed available frames, the system may repeatedly evict and reload pages, producing thrashing. That can drive CPU utilization low while storage activity rises, tempting an operator to add more runnable work and make the problem worse. Replacement algorithms such as FIFO, LRU approximations, and CLOCK encode different histories and practical costs. Exact LRU requires tracking recent use ordering; real systems approximate recency and account for dirty pages, file-backed pages, and memory pressure across processes.

Trace the reference string 1,2,3,1,4 with three initially empty frames under FIFO. The first three accesses fault, the second reference to one hits, and the request for four causes a fourth fault. FIFO's oldest resident page is still one, despite its recent access, because FIFO does not update arrival order on hits. Under a true LRU policy, one becomes recently used at the fourth reference, so the fifth request evicts two instead. Both produce four faults on this short trace, but leave different resident contents; later references can separate their fault counts. A lab should therefore compare complete frame states after every reference, not only final totals. Include a known reference sequence exhibiting Belady's anomaly for FIFO if studying non-stack policies, while noting that the property is not universal for every possible string.

## §4.4 Replacement Policies

**Core model — Replacement Policies**

Replacement policies choose a victim frame when a new page must be loaded into a full memory set. FIFO, LRU and approximations make different tradeoffs.

**Original worked illustration**

For reference sequence [1,2,3,1,4] with three frames, FIFO faults on 1,2,3 and 4, evicting 1 at the last step; LRU would evict 2.

**Boundary conditions and checks**

FIFO can exhibit Belady's anomaly, so adding frames does not necessarily reduce faults for all traces.

### Replacement policy and dirty-page accounting

A page-replacement decision needs a policy for choosing which resident page to evict when memory is full. FIFO selects by admission time, LRU by most recent reference, and CLOCK maintains a circular hand with reference bits to approximate recency efficiently. A policy may prefer clean file-backed pages because discarding them does not require writing modified data first, but this creates further trade-offs in fairness and application performance. A replacement mechanism also must avoid evicting pinned pages needed for DMA or critical kernel operations. Treating every frame as equally evictable is a simplification appropriate only to a classroom model.

For a toy cache of three frames, consider 1,2,3,1,4,2. FIFO misses on 1,2,3,4 and possibly 2 depending on its subsequent state: after 4 evicts one, the final 2 is a hit. LRU after accessing 1 makes page 2 least recently used; inserting 4 evicts 2, so the final reference to 2 misses. This demonstrates that 'more sophisticated' does not mean fewer faults on every possible finite trace. To judge a policy, compare distributions of workloads, not a hand-picked example. The theoretical optimal algorithm replaces the page whose next use is farthest in the future, but its required future knowledge makes it a lower-bound reference rather than a general online implementation.

Dirty bits and writeback schedules complicate latency. If a victim page has been modified, it may need to be written before its frame is reused or before crash consistency requirements are satisfied. An asynchronous background writer can reduce foreground stalls, but it cannot promise durability without a suitable ordering and flush protocol. A useful trace displays page identifier, hit or miss, reference bit, dirty bit, chosen victim, and any required writeback. Repeat with a read-only sequence and then a mixture of reads and writes. Evaluate fault count, writeback count, and the maximum queue size as separate metrics. The learner should understand that a low fault count is not sufficient evidence of low wall-clock latency under storage constraints.

### Integrative case study — a process under memory pressure

An application allocates a 300 MiB working set and repeatedly scans it while the available physical frame budget fluctuates. A simplistic model with 4 KiB pages says 300 MiB comprises 300×1024×1024/4096 = 76,800 pages. That number does not imply that the process immediately occupies 76,800 physical frames; mappings may be lazy, pages may be shared, and untouched regions may not yet be resident. The page table records translation states while the operating system decides when to back memory with physical frames. A reference to an unmapped or not-present page may cause a recoverable fault or an illegal-access condition depending on the mapping and access rights.

First analyze address translation in isolation. For address 12290 with 4096-byte pages, the virtual page number is three and the offset is two. If page three maps to physical frame seven with read-write permission, the corresponding physical address in a simple flat model is 7×4096+2 = 28,674. If that mapping is read-only, attempting a write must not silently succeed. If the page is not present but part of a valid demand-paged region, the fault handler can acquire a frame and update the mapping; a subsequent instruction retry may then succeed. If the address falls outside the process's valid regions, a fault handler cannot infer that it should allocate arbitrary memory just because the process requested it.

Now give the process three page frames and the reference sequence 1,2,3,1,4,2. For FIFO, the first three references fill frames, the repeated one hits, and four evicts the oldest admitted page one. Reference two then hits, giving four total faults. With LRU, the hit on one makes it recently used; on reference four, page two is least recently used and is evicted. The final reference two faults, giving five. This controlled counterexample teaches that one trace can favor FIFO despite LRU's more informative recency policy. Good policy evaluation uses representative families of traces, not a theorem inferred from six accesses.

Add dirty pages. Suppose frame holding page one has been written after admission and must be evicted. A simple model counts one writeback before reuse if no clean replacement is available. That extra I/O may dominate the cost of choosing the victim. Actual systems can clean pages in the background, prioritize clean file-backed pages, and use more complicated reclaim heuristics. Reporting fault rate without writeback and device latency may therefore mislead. A working-set policy should also consider fairness across processes: one application's scan should not always evict another application's hot control pages if isolation and throughput objectives matter.

A laboratory records all page references with timestamp, virtual page, access type, hit/miss, chosen frame, dirty state, and writeback event. It also computes residency over a sliding observation window to approximate the active working set. Test three, four, and five frames and explain when additional frames help; do not assume fault count is strictly monotonic for FIFO. Then switch from sequential scan to a small repeated hot loop and observe reduced faults after warm-up. Finally, introduce a CPU utilization dashboard that drops when disk paging grows. The correct diagnosis is not immediately to schedule more CPU work: first test whether memory pressure and repeated fault stalls are consuming elapsed time.

### Diagnostic exercise — test three separate memory truths

For every synthetic memory access, print (a) whether the virtual address belongs to a valid region, (b) whether its virtual page is resident and accessible, and (c) which physical frame supplies the bytes if successful. These are different questions. Begin with one page mapped read-only and attempt both reads and writes; compute the address decomposition but reject unauthorized mutation. Then simulate FIFO and LRU replacement for the sequence 1,2,3,1,4,2 with three frames, recording final resident sets as well as fault totals. Add a dirty bit to one victim and count writebacks separately from faults. A learner should be able to explain why two policies that produce the same number of faults can still leave different states, and why a page fault is not always a disk read. Finally, grow the working set beyond frame capacity and observe repeated evictions. Avoid treating the toy policy as evidence of real-world CPU cache or swap performance.

### Boundary cases and falsifiable design claims

At page boundaries, arithmetic errors are easy to detect. For 4096-byte pages, address 4095 belongs to page zero with offset 4095, while address 4096 belongs to page one with offset zero. An algorithm that rounds the quotient instead of taking floor division will misclassify addresses near boundaries. Virtual addresses are also context-dependent: a page number without the address-space identity does not specify its physical backing. A TLB entry must be used only in the correct translation context or under a valid shared/global mapping arrangement. Incorrect reuse can become an isolation defect as well as a performance error.

Demand paging introduces faults with different consequences. Reading an untouched anonymous mapping might trigger zero-fill allocation; writing a copy-on-write shared page might allocate a private replacement; attempting to execute non-executable mapped memory should be denied under the applicable protection policy. These are not equivalent events, even if they all enter a fault handler. Modern kernels may use huge pages, memory compression, swapping, or file-backed mappings, which alter the relationship between page counts and physical media usage. A toy simulator should say clearly that it models fixed-size pages and a small set of frames without those features.

A diagnostic assignment asks students to create a trace whose FIFO fault count increases when the number of frames rises. This is possible for certain reference strings because FIFO lacks the stack property; it is not a claim that every string shows the anomaly. By contrast, an idealized exact LRU stack cache cannot incur *more* misses simply by increasing capacity for the same sequence under the usual assumptions. The exercise should compute frame contents for each reference, not guess based on policy labels. Include dirty writeback cost and a page that is temporarily pinned so learners understand the limitations of replacing any arbitrary frame.

## Three worked questions

### Allocation: worked application 1

An allocator gives a 100-byte object a 128-byte block. Compute internal fragmentation.

**Set up the model and conditions**

Subtract requested payload bytes from block capacity.

**Carry out the calculation or proof**

128−100=28 bytes.

**State the result and its scope**

There are 28 unused bytes in the assigned block, excluding metadata.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

A 128-byte block serving a 100-byte request leaves 28 unused bytes inside that allocated block. Its internal waste fraction relative to allocated block space is 28/128≈21.875 percent; relative to payload requested it is 28/100=28 percent. Both ratios can be useful, but comparing them without identifying the denominator is misleading. The answer excludes allocator metadata, alignment outside the 128-byte block, and page-level waste. With one thousand independently allocated objects of this size class, the simple model reserves 128,000 block bytes for 100,000 payload bytes, wasting 28,000 bytes internally. That scaling assumes no compression, sharing, reuse within a block, or other allocator special cases. A stronger experiment varies size-class rounding and request-size distribution, because one example does not determine overall fragmentation.

### Paging: worked application 2

For 4 KiB pages translate virtual address 12290 to page and offset.

**Set up the model and conditions**

Divide by page size 4096.

**Carry out the calculation or proof**

12290=3×4096+2.

**State the result and its scope**

VPN=3 and offset=2; physical location requires a page-table mapping.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Page size is 4096 bytes, so integer division of 12290 by 4096 gives quotient three and remainder two: 12290=3×4096+2. The quotient is the virtual page number; the remainder is the page offset. The offset can also be obtained by taking the lowest twelve bits of the address. A physical address cannot be calculated without a valid mapping from virtual page three to a physical frame. For illustration only, mapping that page to frame seven would yield 7×4096+2=28,674, provided the requested access rights are granted. Boundary tests should check 4095 (page zero, offset 4095), 4096 (page one, offset zero), and 8192 (page two, offset zero). These examples catch errors where a page boundary is incorrectly assigned to the preceding page.

### Virtual Memory: worked application 3

For FIFO page replacement with 3 empty frames, trace [1,2,3,1,4]. Count page faults.

**Set up the model and conditions**

1,2,3 each fault and fill the frames.

**Carry out the calculation or proof**

The fourth reference 1 is a hit; 4 faults and evicts the oldest page 1.

**State the result and its scope**

Four page faults occur.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Initialize three empty frames. Reference one faults and occupies the first frame; two faults into the second; three faults into the third. The fourth reference to one is a hit and does not change FIFO admission order. Reference four faults because it is absent and requires eviction; FIFO chooses the oldest admitted page, one. The fault indicators are [1,1,1,0,1], summing to four. A complete answer should also report final residency [4,2,3] under a specified frame-order representation. LRU would also have four faults on this short trace but evict page two instead, leaving [1,4,3] in the corresponding conceptual state. Thus fault totals alone cannot distinguish the future behavior of the policies; a subsequent reference to one versus two would. The sequence and initial frame state are part of the problem's specification.
