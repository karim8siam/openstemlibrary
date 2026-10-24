# Computer Architecture — Unit 7: Parallel architectures

## 7.1 Multicore Systems

**Core model — Multicore Systems**

Multicore systems execute independent instruction streams with shared and private resources. Parallel speedup is limited by serial work, communication and synchronization.

**Original worked illustration**

If 80% of an application is perfectly parallelizable, four cores give Amdahl speedup 1/(0.2+0.8/4)=2.5.

**Boundary conditions and checks**

More cores can increase cache contention and memory bandwidth pressure; a processor count is not a performance guarantee.

### Extended technical chapter: Multicore Systems

A multicore processor contains multiple execution cores that can work on separate instruction streams, often sharing portions of a memory hierarchy and external bandwidth. Parallelism increases possible throughput but introduces coordination costs and contention. Amdahl's law treats workload size as fixed and bounds ideal speedup by the serial fraction. For a workload whose serial fraction is 0.2, four ideal workers produce speedup 1/[0.2+0.8/4]=2.5. Eight workers produce 1/[0.2+0.8/8]=3.33, not eight. These are ceiling-like results under unusually generous assumptions; scheduling overhead, locking and memory traffic generally reduce achieved performance.

Different parallel decomposition strategies create different bottlenecks. Task parallelism assigns independent jobs to workers, while data parallelism partitions one operation's data. Work stealing redistributes tasks from busy workers but costs synchronization and can harm locality. Load balance matters: if one worker owns a slow task while the others finish early, elapsed time is determined by the slowest worker rather than the average task duration. A useful scheduling trace lists each task's work, dependency constraints and core assignment. Compute the critical path, the total amount of work divided by worker count, and the observed makespan. The maximum of the first two values is a lower bound for an ideal schedule.

Multicore scalability must also consider memory hierarchy and NUMA placement. Multiple cores that independently read a large shared table can saturate bandwidth, while frequently updating the same cache line may cause coherence traffic. Even separate counters can false-share when located in one cache line. A laboratory can compare a single shared counter protected by a lock, per-core counters combined at the end, and an atomic counter. The discussion should cover result correctness, contention, memory ordering and measurement methodology. More cores are not a substitute for partitioning data and minimizing coordination; parallel speedup is a property of the complete workload and hardware system.

## 7.2 Simd

**Core model — Simd**

Single-instruction multiple-data execution applies one operation across multiple lanes. Vector width is useful only if the workload has enough independent elements.

**Original worked illustration**

An eight-lane SIMD operation can add eight pairs of numbers in parallel if both input vectors are ready and the operation has lane-local semantics.

**Boundary conditions and checks**

Tail processing, alignment, divergent control and reduction operations diminish ideal gains for irregular workloads.

### Extended technical chapter: Simd

Single-instruction multiple-data execution applies one operation across multiple lanes of a vector at once. A vector instruction could add four, eight or more elements per instruction depending on element width and architectural capabilities. This reduces control overhead and can increase arithmetic throughput, but not all algorithms map well to uniform lane operations. Data dependencies, irregular memory access and branches can leave lanes inactive. A vector-capable instruction set also does not guarantee a compiler will vectorize a particular source loop: aliasing uncertainty, loop-carried dependencies and observable language semantics may block transformations.

Suppose an array has 1025 elements and vector instructions operate on eight elements per full vector. There are 128 complete groups of eight, covering 1024 elements, with one remainder element. A compiler may use a scalar cleanup iteration or a masked vector operation for the tail. The operation count and elapsed time need not decrease by a factor of eight because loading data, storing results and handling alignment incur costs. If a loop is memory-bandwidth bound, doubling arithmetic width might yield almost no improvement. If the loop computes a reduction, the reassociation of floating-point additions may produce slightly different answers because finite-precision addition is not associative.

SIMD can be compared to SIMT, a common programming model for groups of lanes whose control flow is coordinated but may diverge. Divergent branches can require execution under masks, reducing utilization even when the nominal vector width is large. A laboratory should mark active and inactive lanes for a short conditional vector loop, count useful lane operations, and compare the utilization of sorted versus alternating data. Then explain how packed element widths affect the number of lanes and numerical range. The correct conclusion distinguishes theoretical peak operations from achieved throughput, and it reports whether changes preserve the program's allowed numerical error and memory-safety behavior.

## 7.3 Coherence

**Core model — Coherence**

Cache coherence ensures a consistent visibility protocol for writes to shared memory locations across private caches. Coherence and language-level memory consistency are related but distinct.

**Original worked illustration**

When core A writes shared x, core B must not indefinitely use a stale private copy once the coherence protocol requires it to observe the update.

**Boundary conditions and checks**

A coherent cache alone does not make a racy increment atomic; synchronization is still required for read-modify-write correctness.

### Extended technical chapter: Coherence

Cache coherence seeks to make copies of a memory location across private caches behave consistently under an architectural protocol. If one core writes a line, other cores must not indefinitely keep using stale copies in ways that violate the machine's coherence guarantees. A simplified MSI protocol labels lines Modified, Shared or Invalid. A read miss may obtain a shared copy; a write to a shared line typically requires exclusive ownership and invalidates competing copies. The exact details differ among protocols such as MESI or MOESI and among real interconnect topologies.

Imagine cores A and B both cache a shared counter with value five. If A wants to write six, it must obtain an appropriate ownership state so that B does not keep silently treating its old shared copy as a current authoritative value. A state trace should track the directory or bus messages, each line state and the resulting data. Coherence operates at line granularity, not source-language variable granularity, which explains false sharing: two independent variables in the same line can repeatedly invalidate one another when separate cores update them. Padding or redesigning data layout can reduce these transfers, but padding also consumes capacity.

Coherence is not a substitute for a memory consistency model. A protocol can keep a single address coherent while a language or ISA permits other reads and writes to become visible in different orders. Synchronization requires the specified atomic operations, fences or higher-level constructs. A data race in a language with strong restrictions cannot be repaired merely by assuming coherent hardware. A teaching exercise should compare the line-state evolution of read-read, read-write and write-write access sequences, then identify whether the application also needs ordering constraints. Avoid claiming that an observed test run without stale values proves a concurrent algorithm correct; its schedule may simply have failed to expose the race.

## 7.4 Synchronization Hardware

**Core model — Synchronization Hardware**

Synchronization hardware includes atomic read-modify-write operations and fences, which support software locks and memory-order protocols.

**Original worked illustration**

A compare-and-swap operation that changes x from 0 to 1 only if x was 0 lets one contender acquire a lock while others fail and retry.

**Boundary conditions and checks**

Busy-wait spinning can waste CPU under preemption. Memory ordering must be specified, especially on weakly ordered systems.

### Extended technical chapter: Synchronization Hardware

Concurrent software relies on hardware-supported atomic operations and an explicitly defined memory model. A read-modify-write instruction such as compare-and-swap can check a memory location and conditionally update it as one indivisible atomic operation with respect to participating threads. Plainly executing load, addition and store as separate instructions is not equivalent. If two threads both load counter=7, both compute 8 and both store 8, one increment is lost. This race arises even on a coherent multicore system because coherence alone does not combine the two mathematical increments.

Locks, spinlocks, semaphores and lock-free algorithms build on atomic operations but solve different problems. A spinlock wastes CPU cycles while waiting but may be appropriate for very short critical sections under controlled conditions. A blocking mutex allows a waiting thread to sleep, often preferable for longer waits. A compare-and-swap loop can update a shared counter without a conventional mutex, though it may retry repeatedly under contention. Atomicity does not automatically imply fairness or freedom from starvation. A lock-free algorithm permits system-wide progress under suitable assumptions, which is weaker than guaranteeing every individual thread finishes promptly.

Memory ordering determines whether data written before a synchronization action is visible after a corresponding acquisition. Acquire and release semantics can establish a publication relation for a shared object when correctly paired. Relaxed atomics offer atomic modification of one object without necessarily ordering unrelated ordinary memory accesses. Students should trace a producer writing payload data and then publishing a ready flag, followed by a consumer reading the flag and then the payload. Mark the necessary ordering relations and distinguish them from mere wall-clock ordering in one observed run. An effective verification exercise explores all legal interleavings of a small concurrent algorithm and checks invariants such as 'count equals number of completed increments' rather than trusting a stress test alone.

### Integrated laboratory: parallelizing a shared analytics pipeline

A workload scans one million records and computes eight aggregate statistics. First measure its work in an explicitly idealized model: twenty percent of elapsed time is serial input parsing and report assembly, and eighty percent is independent per-record computation. On a single core the normalized time is one. With four equal workers, the Amdahl estimate is 0.2+0.8/4=0.4, giving speedup 2.5. With eight workers it is 0.3, giving speedup about 3.33. Moving from four to eight workers improves the idealized elapsed time by just a quarter rather than doubling throughput. The extra workers may still be valuable at larger workloads, but the fixed-workload model shows diminishing returns.

Suppose workers update one shared counter for each accepted record. If each update uses ordinary load-add-store instructions, two simultaneous updates can race: both load the same old count and both write the same incremented value. The final count might be lower than the number of accepted records. Atomic fetch-add or a correctly used lock fixes the atomicity issue, but doing one contended atomic operation per record can be expensive. A per-worker local counter combined after processing reduces contention at the cost of a final reduction step. The safe final total is the sum of disjoint worker counts under a partitioning scheme that prevents duplicated or omitted records.

Next introduce a data-layout fault. Worker A updates a counter for group A; worker B updates a different counter for group B. If both counters reside in the same cache line, repeated writes can bounce ownership between cores even though the source-language variables are independent. This is false sharing. Place the counters on separate cache lines or accumulate in private memory and compare modeled coherence transactions. Padding adds memory use and can hurt capacity under some conditions, so the fix should be assessed against a measured workload rather than applied reflexively to every structure.

A SIMD implementation processes eight 32-bit fields per vector instruction. For one million elements, there are 125,000 full eight-element groups, but data alignment, masking, loads, stores and branch patterns affect achieved speed. If each record requires a branch on a rare exception, a scalar fast path may work well; if most lanes diverge, vector utilization falls. The computed aggregates may also change slightly for floating-point fields if the reduction tree changes addition order. Specify a numerical tolerance and test it against a high-precision reference. Speed improvements that silently change an important financial or scientific result are not correct optimizations.

Memory bandwidth is another possible ceiling. If each record requires 64 bytes of input and produces 8 bytes of output, reading one million records moves at least 64 MB of input under decimal units, plus output and intermediate traffic. A hypothetical memory interface sustaining 16 GB/s cannot transfer those input bytes in less than four milliseconds even before computing. Adding arithmetic cores beyond that point cannot eliminate the bandwidth lower bound. Cache reuse or compression might reduce transferred bytes, but those changes require their own CPU and correctness costs.

Finally write a concurrent correctness test. The test generates a deterministic record set, partitions indexes across workers, and compares final aggregate values against a single-thread reference. It varies worker counts, deliberately schedules yields around shared updates, and exercises the empty and one-record cases. A stress test is helpful but not a proof of all possible interleavings. Explain which operations are atomic, where acquire/release ordering is necessary, which objects are immutable during execution, and how worker failures are reported. A complete evaluation includes wall time, instructions, cache misses, coherence traffic and energy where available, not just worker count.

### Review lens: scalability is not a single curve

Parallel scaling measurements must state whether they hold the total problem fixed, grow the problem with worker count or run more independent jobs. Fixed-workload speedup, scaled-workload throughput and throughput per watt are different targets. An algorithm can show excellent throughput scaling while one request's latency worsens from queueing or coordination. It can also scale on a carefully partitioned dataset but degrade when real traffic concentrates updates on one shared object. A defensible experiment compares several input distributions, measures contention and checks result invariants against a sequential reference. Report both hardware utilization and useful completed work. Count retries, lock waits and failed speculative operations separately from successful application operations. Do not confuse the number of logical threads with the number of physical cores, or an abstract SIMD lane count with a guaranteed rate of useful arithmetic operations.

### Additional guided investigations for multicore behavior

**Fixed-workload limit.** A workload has ten seconds serial work and ninety seconds parallel work. On five ideal workers, modeled execution is 10+90/5=28 seconds, giving speedup 100/28≈3.571. On ten workers it is nineteen seconds and speedup≈5.263. The serial fraction caps limiting speedup at ten. Any practical communication overhead lowers the observed speedup, so a reported value above ten for the same fixed workload would demand investigation into changed work, caching or measurement boundaries.

**SIMD tail.** An array of 103 integers is processed eight at a time. Twelve full vector groups cover 96 elements, leaving seven for masked or scalar tail processing. Under a four-lane layout, twenty-five full groups cover 100 elements and the tail is three. Count the number of logical lane slots used under a masked final vector and distinguish useful lanes from inactive lanes. Nominal lane width alone does not predict execution time when vector instructions have different memory traffic or throughput.

**Coherence trace.** Two cores first read shared cache line X, producing shared copies in a toy MSI model. Core A writes X, so it must obtain exclusive ownership and invalidate B's copy. Core B then reads X and triggers a coherence transaction to obtain current data. Count conceptual ownership transitions but do not equate them to one fixed latency; interconnects differ. Move two independent counters into the same line and explain how false sharing adds ownership traffic without a logical data dependency between counters.

**Atomic update.** Begin shared counter zero and schedule two threads with read, increment and write steps. Interleave both reads before either write; the final count becomes one if neither operation is atomic. Repeat with atomic fetch-add twice and obtain count two regardless of the order in which the two atomic modifications linearize. Add a payload published behind a flag and identify why atomic counter correctness does not automatically establish correct visibility of unrelated payload fields.

### Diagnostic challenge: establish a lower bound on parallel time

Six tasks have work estimates [8,6,4,4,2,2] abstract units. Their total work is twenty-six, so even a perfect schedule on four identical workers requires at least 26/4=6.5 units, ignoring task dependencies. Since the largest indivisible task takes eight units, makespan cannot be less than eight under a non-preemptive model. A naive assignment placing both the eight-unit and six-unit tasks on one worker produces fourteen units for that worker, even while another worker finishes early. Construct an improved schedule and compute actual makespan. Then introduce a dependency that task eight must complete before the two-unit finalization task begins, adding a critical-path lower bound of ten units. These bounds are independent of cache coherence, locks and memory bandwidth, which can create additional delays in a real machine. A useful parallelism assessment measures both theoretical available concurrency and where the actual schedule loses time.

## Three worked problems

### Multicore Systems: worked application 1

For a system with serial fraction 20% and four identical cores, compute Amdahl speedup.

**Set up the model and conditions**

Parallel fraction p=0.8, residual serial fraction 0.2.

**Carry out the calculation or proof**

Time fraction =0.2+0.8/4=0.4.

**State the result and its scope**

Speedup=1/0.4=2.5.

**Independent verification, conditions, and interpretation**

Amdahl's fixed-workload model divides normalized execution time into a serial part and a perfectly parallelizable part. With serial fraction s=0.2 and four workers, predicted time is s+(1−s)/4 = 0.2+0.8/4=0.4 of the one-worker baseline. Speedup is the reciprocal, 1/0.4=2.5. Another check decomposes a 100-second job into twenty serial seconds plus eighty parallel seconds. Four ideal workers reduce the eighty-second portion to twenty seconds, yielding forty seconds total and a factor of 100/40=2.5. If workers increase without bound, serial time remains twenty seconds and maximum idealized speedup tends to five. This is not a promise of reaching five; task distribution, memory bandwidth, communication and scheduling add overhead. If the workload grows with worker count, Gustafson's scaled-workload reasoning addresses a different question and cannot be substituted without changing assumptions. A reported application speedup should specify whether problem size was fixed. This distinction prevents comparing incompatible parallel benchmarks.

### Simd: worked application 2

An SIMD instruction has eight lanes and an array has 18 elements. How many vector operations plus tail elements?

**Set up the model and conditions**

Two full eight-element vectors cover sixteen elements.

**Carry out the calculation or proof**

Subtract 16 from 18 to obtain two remaining scalars.

**State the result and its scope**

Two full vector instructions plus a two-element tail are required without masking.

**Independent verification, conditions, and interpretation**

With eighteen elements and an eight-lane SIMD operation, divide eighteen by eight. The integer quotient is two complete eight-element groups covering sixteen elements; the remainder is two. Without predication or masking, the program needs two full vector operations and a scalar or otherwise separate two-element cleanup. A masked vector instruction could instead process a partial vector with only two lanes active, but that is a different execution and instruction-count model. A programmer must avoid reading or writing beyond the array bounds merely to fill all lanes. If data are 32-bit integers, one eight-lane input vector contains 256 bits of payload, but the ISA may have special register or packing constraints not described by this abstract calculation. For a length of sixteen, no remainder exists; for length seven, there are zero full groups and seven tail elements. These boundary checks validate the division. The number of vector operations is not an execution-time estimate, since loading, storing, masking, alignment and issue width can dominate. The answer describes the partitioning of data into legal vector groups.

### Coherence: worked application 3

Explain why two concurrent increments can lose an update even with cache coherence.

**Set up the model and conditions**

Both cores may read shared x=5 before either writes.

**Carry out the calculation or proof**

Each computes 6 and both eventually store 6, which coherence serializes.

**State the result and its scope**

Final value is 6 instead of 7; atomic read-modify-write is needed.

**Independent verification, conditions, and interpretation**

An unsynchronized increment usually involves three logical stages: read current value, compute value+1, and write the result. Starting from shared counter five, thread A can read five while thread B also reads five. Each computes six, and both write six, leaving final result six although two increments were requested and a sequential execution would produce seven. Cache coherence can ensure that reads and writes of the same line use a coherent ownership protocol, but it does not merge the two separate arithmetic updates into one atomic transaction. An atomic fetch-add ensures each increment acts as one read-modify-write operation for the shared counter, producing final result seven under the simplified two-increment scenario. A lock protecting the entire read-add-write sequence would also work if used correctly by all participants. Atomicity alone does not specify ordering of unrelated data; concurrent publication patterns may additionally need acquire/release synchronization. A complete test enumerates the interleaving that loses an update, explains why coherent caches still allow it, and checks that the proposed solution eliminates that interleaving at the language and architecture level.
