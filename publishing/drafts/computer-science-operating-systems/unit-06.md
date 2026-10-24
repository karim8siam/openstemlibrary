# Operating Systems — Unit 6: Storage and I/O

device interfaces; buffering; storage scheduling; asynchronous I/O

## §6.1 Device Interfaces

**Core model — Device Interfaces**

A device driver exposes commands and completion events using hardware-specific registers and queues. A general interface shields applications from hardware protocols.

**Original worked illustration**

An application reads a file descriptor while a block driver may assemble several device requests, retries and completions to satisfy it.

**Boundary conditions and checks**

Driver correctness includes alignment, error propagation, timeout and cancellation; successful happy-path I/O is not enough.

### Devices, commands, DMA, and interrupts

A device driver bridges an abstract OS interface and a concrete hardware control protocol. It may configure command queues, map buffers for direct memory access, handle completion interrupts, and report status. A DMA engine moves bytes without the CPU executing one load and store per byte, but it does not remove the need for ownership, mapping, and cache-coherence rules. The device must not write into memory that the application has already freed or reassigned. Where an IOMMU is present, device-address translations and permissions can further constrain which physical regions a device may touch. A DMA mapping is an explicitly managed resource, not automatically equivalent to a user pointer.

Interrupt-driven completion avoids continuous polling at some workloads, but each interrupt has a processing cost. Devices can aggregate completion events to trade a little notification delay for lower CPU interrupt overhead. Polling can be efficient at very high rates if useful work is likely on each check, yet waste energy and CPU cycles at low rates. Driver design thus depends on service latency, event frequency, power goals, and fairness to other tasks. Hardware retries and command reordering make application-visible ordering distinct from the sequence in which a process issued requests. The operating system uses queues, barriers, and completion notifications to impose required semantics where appropriate.

Model a network adapter receiving four packets while a user process is suspended. The adapter writes received bytes into authorized buffers, marks descriptor status, and signals completion. The kernel or userspace stack then validates packet length and metadata before making data visible to the application. A malformed length field must not allow out-of-bounds access. An instructor can ask students to map every resource owner over time: who owns the RX buffer before submission, while DMA is active, after completion, and after the application consumes it? Then inject cancellation during active DMA. The correct answer cannot be simply to free the buffer immediately; ownership transfer or synchronization must guarantee the device has stopped using it. Measure conceptual costs for polling versus interrupt notifications while declaring fixed per-event overhead assumptions.

## §6.2 Buffering

**Core model — Buffering**

Buffering absorbs rate mismatch and amortizes expensive device operations. Buffer size trades memory use against throughput and latency.

**Original worked illustration**

Writing 1000 records individually may need 1000 writes; grouping 100 records per buffer uses ten bulk writes if each fits and flushing is managed.

**Boundary conditions and checks**

A buffer that improves throughput may worsen tail latency or lose unwritten data on failure unless durability is separately enforced.

### Buffering, batching, and backpressure

Buffers decouple producers and consumers whose instantaneous rates differ. A kernel pipe, network socket, block queue, and application log writer can all have buffers, but their guarantees and ownership policies vary. Buffers smooth short bursts; they cannot sustainably compensate for a producer that runs faster than its consumer forever. Under such overload, queue length grows until a finite capacity is reached or latency violates requirements. Backpressure tells an upstream component to slow or stop, using blocking writes, credits, flow-control windows, rejected requests, or explicit rate-limiting signals. Silently dropping work may be acceptable for some telemetry but catastrophic for financial records.

Batching often amortizes fixed overhead. If writing each record incurs a fixed setup cost of 50 microseconds plus a one-microsecond marginal transfer cost, sending 100 records one at a time costs about 5.1 milliseconds under a serial idealization. A single batch of 100 records costs about 150 microseconds. The reduction is in setup overhead, not magical acceleration of the underlying transfer requirement. Batching also creates waiting: an early record in a batch may sit until enough companions arrive or a timer fires. That increases latency at low load even as it improves throughput at high load. A service should choose batch size and timeout based on its explicit latency service-level objective.

A bounded queue with capacity ten and arrival rate of twelve tasks per second but service capacity ten tasks per second accumulates backlog at approximately two tasks per second in a deterministic fluid approximation, until backpressure or loss occurs. After five seconds it would have reached ten queued tasks if starting empty and if service runs smoothly. Actual stochastic arrivals cause jitter and sometimes earlier overflow. Little's Law, L=lambda*W, applies to a stable system under its usual average-flow assumptions; it does not give a meaningful steady-state waiting time for a permanently overloaded system. In a lab, compare throughput and maximum wait under batch sizes one, five, and twenty, then introduce a fixed timeout. Record queue occupancy over time and explicitly show how application memory can grow when backpressure is absent.

## §6.3 Storage Scheduling

**Core model — Storage Scheduling**

Storage scheduling changes request order to reduce seeks or improve fairness. Elevator-style policies suit spinning disks more than devices where seek costs are negligible.

**Original worked illustration**

From head position 50, requests at 10, 55 and 90: servicing 55 first moves 5 cylinders, whereas servicing 10 first moves 40.

**Boundary conditions and checks**

SSD queues and deadlines have different cost structures; seek-minimizing rules can starve far-away requests.

### Scheduling requests on mechanical and solid-state storage

A conventional mechanical disk incurs seek and rotational delays that depend on head position and platter state. Under an intentionally simplified cylinder-distance model, first-come-first-served serves requests in arrival order, while shortest-seek-time-first chooses the pending request nearest the current cylinder. At head position 50, requests at cylinders 10, 55, and 90 have initial distances 40, 5, and 40. SSTF chooses 55 first. That is a local greedy decision; a continuing stream of nearby arrivals can postpone a distant request for a long time. SCAN-like policies sweep in a direction to bound behavior differently, but exact edge handling must be specified for a reproducible model.

Solid-state drives have no mechanical seek arm, so a cylinder-distance objective is not a faithful SSD performance model. Flash translation layers map logical addresses to physical pages, manage erase blocks, distribute wear, and perform garbage collection. Random requests can still differ in latency because of internal parallelism, queue depth, write amplification, cache effects, and thermal or power-management behavior. Storage stacks can reorder requests for throughput while preserving required barriers and flush semantics. The combination of device queue scheduling and higher-level filesystem access makes naive seek calculations an incomplete representation of observed I/O latency.

A useful lab uses a sequence 50→10→55→90 under FCFS and then computes an SSTF sequence. For FCFS, cylinder movement is |50−10|+|10−55|+|55−90|=120. For SSTF, choose 55 (5), then 90 (35), then 10 (80), for 120 as well in this particular set; the first decision reduces immediate movement but does not necessarily improve total. To see a genuine improvement, test different request sets rather than concluding from one arrangement. A second lab compares latency under queue depths one, four, and sixteen for a hypothetical SSD with a declared parallel service capacity. Keep mechanical distance separate from SSD request concurrency, and identify which model assumptions would make the observed result change.

## §6.4 Asynchronous I/O

**Core model — Asynchronous I/O**

Asynchronous I/O initiates work and receives completion later, allowing useful computation or independent I/O meanwhile.

**Original worked illustration**

An event loop can issue three independent reads and process completions as each arrives, rather than blocking for each one in sequence.

**Boundary conditions and checks**

Async does not imply the storage is faster; it may improve overlap and scalability but also increases state-management complexity.

### Asynchronous I/O, completion semantics, and cancellation

An asynchronous operation can begin without forcing the submitting execution context to wait for the physical operation to finish. Completion may arrive through callbacks, futures, completion queues, or event-loop notifications. The central benefit is overlapping independent work, not guaranteeing that a single device request becomes faster. If a single read takes eight milliseconds and computation takes two milliseconds, sequential execution might take ten milliseconds while careful overlap could approach eight, subject to dependencies and overhead. If the computation consumes the data being read, however, that computation cannot precede the read's completion. A dependency graph is necessary before claiming overlap gains.

Cancellation is a request to stop work or stop waiting, not necessarily proof that the device has ceased touching the buffer. An operation may complete concurrently with cancellation, and a callback may still execute unless the API guarantees suppression and ownership transfer. Buffer lifetimes, descriptor closure, callbacks, and cleanup must be safe under both outcomes. A common design assigns each operation a generation identifier and records whether its result remains relevant. A late completion with an older generation can be discarded at the application layer without freeing memory while the kernel still uses it. This solves stale-result handling; it does not replace correct kernel or runtime lifetime management.

Consider a file download racing a five-second timeout. At 4.9 seconds, the timeout handler begins cancellation while the network stack receives the final bytes. Both timeout and completion events may be queued. A robust state machine includes pending, completed, cancellation-requested, canceled, and failed states with explicit permitted transitions. Exactly one path should publish a final user-visible result; cleanup must run once even when both completion and cancellation notifications occur. For a lab, enumerate the legal interleavings and write assertions about double callbacks, use-after-free, and leaks. Compare event-driven and blocking implementations under ten concurrent operations with declared service times. Distinguish concurrency *capacity* from throughput, which also depends on device and downstream limits.

### Integrative case study — an I/O pipeline under burst traffic

A telemetry system receives records at varying rates, parses them, compresses batches, and writes them to storage. The intake process produces work, while compression workers and the storage device consume it. Three distinct resource constraints must be considered: CPU time for parsing and compression, memory for outstanding records, and storage service capacity. A system can be underloaded on average yet experience short queue spikes; it can also be permanently overloaded if long-run arrival rate exceeds service rate. Increasing the in-memory queue may delay the point at which failure becomes visible without increasing sustainable throughput.

Assume deterministic arrival of twelve records per second and downstream service capacity of ten. From an empty queue, backlog grows at two records per second if the rates remain constant and no backpressure is applied. A queue holding ten records reaches that capacity after approximately five seconds. An actual finite-state simulation must account for arrivals and departures as events, so overload may occur a little earlier or later depending on event ordering at tied timestamps. The key mathematical conclusion is that the queue cannot remain bounded indefinitely under continuous positive excess demand. Stable long-run operation requires load shedding, producer throttling, scaling effective service capacity, or reducing work per record.

Now add batching. A storage request costs a fixed 50 microseconds plus one microsecond per record under a simplified serial model. Writing a hundred records individually costs 100×51 = 5100 microseconds. One batch of a hundred costs 50+100 = 150 microseconds. The faster service model comes with a latency trade-off: if records arrive slowly, the first record waits for batch completion or a maximum wait timer. A hybrid batching rule flushes when either batch size reaches a threshold or the age of the oldest queued record exceeds a deadline. Specify which event takes precedence when both happen simultaneously. A correctness test compares the ordered set of accepted records to the ordered set written, including partial-batch shutdown.

Asynchronous writes allow computation to overlap with device work, but only if their dependencies permit it and buffer ownership remains valid. A compressed buffer submitted for asynchronous I/O must not be reused before completion unless the API explicitly copies the data. If a shutdown timeout occurs while a write is pending, cancellation may race with completion. A single state machine must own the final response and reclaim the buffer safely. This is especially important in a logging system because reporting an operation as durably committed when it was only submitted or buffered is a serious contract violation.

Instrument enqueue timestamps, batch-flush timestamps, completion timestamps, queue length, dropped records, and durable-commit acknowledgments. Evaluate p50 and p99 end-to-end latency for different batch sizes under a bursty trace; record throughput separately. Add a sudden storage slowdown that halves service capacity and check that backpressure activates before memory exhaustion. A successful design states what occurs during overload: reject new requests, block producers, spill to a bounded durable queue, or intentionally drop lower-priority telemetry. There is no universally correct policy, but silent unbounded accumulation is not a stable one.

### Diagnostic exercise — prove bounded operation

Model an input queue with capacity twenty items, fixed arrival rate fifteen items per second, and processing rate twelve. Starting empty, the fluid backlog increases by three per second and reaches capacity in roughly 6.67 seconds unless a producer is slowed or work is discarded. Replace the constant service assumption with batches that pay one millisecond setup plus 0.1 millisecond per item; compute service capacity for batch sizes one, five, and ten, then account for batch-assembly delay. The setup-cost arithmetic improves throughput in an idealized model, but does not by itself establish low p99 latency. Add an asynchronous buffer whose completion arrives after a timeout and show a safe ownership transition. Finally compare a disk head's cylinder-distance trace with an SSD queue model and explain why the same scheduling objective cannot be transferred unchanged between them.

### Boundary cases and falsifiable design claims

Batches need a maximum wait, not merely a target size. If the arrival rate falls to one record per minute and batch size is one hundred, waiting for a full batch can delay the first record for almost two hours in a perfectly regular deterministic stream. A flush timeout bounds that delay at the cost of submitting smaller batches. The ideal timing analysis must include fixed setup cost, per-item transfer, buffer wait, and queueing at the device. Under heavy load, a request can wait far longer in a storage queue than its own transfer time. Reducing batch overhead may improve throughput yet increase latency for the oldest item depending on policy.

A queued asynchronous request may complete out of submission order. If application correctness needs ordered effects, it must enforce sequencing at the appropriate layer rather than assuming completion callback order equals issue order. Likewise, cancellation may arrive after completion has logically occurred. A state machine can ignore a stale completion, but it cannot safely reuse a DMA buffer until ownership is established. Instrument operation generation identifiers and associate every completion with the correct outstanding request to avoid confusing a new request with a late response from a previous one.

A lab uses head positions 0, 50, and 100 and compares FCFS and SSTF over identical mechanical request traces. Students should calculate total absolute cylinder movement and identify a possible starvation pattern for a distant request if nearby new requests keep arriving. Then explicitly switch to an SSD-style model with queue parallelism and remove cylinder distance as an explanatory variable. Ask which observable metrics—latency distribution, queue depth, controller busy time, bandwidth, and write amplification—would be relevant. The change of model is itself an important lesson in applying abstractions only where their assumptions hold.

## Three worked questions

### Device Interfaces: worked application 1

A buffer groups 1000 records into batches of 100. How many batch writes are needed?

**Set up the model and conditions**

Divide 1000 records by 100 records per batch.

**Carry out the calculation or proof**

1000/100=10 exact full batches.

**State the result and its scope**

Ten bulk writes are needed in this idealized case.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

One thousand records divided into batches of one hundred gives exactly ten batches. Because the division has no remainder, no partial final batch is required. A more general expression is ceiling(total_records/batch_capacity), so 1001 records would require eleven batches with the final batch containing one record. This computation concerns the count of batch write calls, not the count of underlying disk operations: the kernel or device may combine, split, or reorder I/O. If each batch has a fixed overhead, batching can lower total setup cost, but holding records until a batch fills can increase latency. A correct design also needs a flush rule for shutdown and for low-traffic periods, or the last partial batch could remain buffered indefinitely. Test the zero-record case and the boundary at exactly one hundred records.

### Buffering: worked application 2

A disk head is at cylinder 50 and requests are 10,55,90. Which request minimizes immediate seek?

**Set up the model and conditions**

Calculate distances from 50: 40,5,40 cylinders.

**Carry out the calculation or proof**

The smallest immediate movement is toward 55.

**State the result and its scope**

Service request 55 first under shortest-seek-time-first.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

From initial head position fifty, the absolute cylinder distances are |50−10|=40, |50−55|=5, and |50−90|=40. Shortest-seek-time-first therefore selects 55 as its first target. After that choice the remaining distances must be recomputed from the new head position; one cannot sort every request once by distance from the original position. For the remaining requests ten and ninety, distances from fifty-five are forty-five and thirty-five, so the next target is ninety, then ten. This yields total movement five+thirty-five+eighty=120 cylinders. FCFS order [10,55,90] also happens to give forty+forty-five+thirty-five=120 in this example, showing why a greedy first decision does not always reduce total travel. The mechanical-cylinder model does not represent SSD internals.

### Storage Scheduling: worked application 3

What happens if an async read completes after its initiating task is cancelled?

**Set up the model and conditions**

The I/O subsystem may still deliver a completion despite the cancellation request.

**Carry out the calculation or proof**

Code must track ownership of buffers and task state to avoid using released storage.

**State the result and its scope**

Cancellation and late completion need an explicit lifecycle policy.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Cancellation and completion may race. A submitted asynchronous read can remain active after the requesting task decides it no longer needs the result. If the buffer is released while the device or kernel may still write into it, memory corruption can occur. The program must follow the relevant API's explicit cancellation guarantee, manage buffer ownership until completion or a confirmed quiescent state, and ensure only one final outcome is published. One common logical pattern tracks a generation or operation identifier so that a late result can be ignored without invalidating its storage prematurely. Test four event orders: completion before cancellation, cancellation before completion, cancellation request with confirmed cancellation, and operation failure concurrent with timeout. In each case, verify one cleanup path and no use-after-free. This reasoning is about lifecycle correctness, not a guarantee that every OS exposes the same cancellation primitive.
