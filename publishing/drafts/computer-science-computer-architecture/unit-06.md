# Computer Architecture — Unit 6: Input and output

## 6.1 Interrupts

**Core model — Interrupts**

An interrupt transfers control to an exception or interrupt handler, saving enough machine state to resume or schedule other work. Masking and priority rules affect latency.

**Original worked illustration**

A device raising 100 interrupts per second with 20 microseconds of handler work consumes 2 ms per second of CPU service, ignoring context costs.

**Boundary conditions and checks**

Not every exception is asynchronous: divide-by-zero faults originate from the current instruction and have different return semantics.

### Extended technical chapter: Interrupts

An interrupt lets a processor respond to an event without continuously executing software that polls the event source. The hardware and operating system cooperate to preserve sufficient state, select a handler and eventually resume interrupted work. An interrupt is not equivalent to a normal function call: privilege levels, automatic state saves, nesting rules and controller priorities may apply. Device interrupts typically indicate that an event needs attention, whereas synchronous exceptions arise from executing an instruction, such as an illegal opcode or a page fault. Distinguishing the two is critical when reasoning about restartability and the source of control transfer.

Latency and throughput trade off in interrupt-driven I/O. If a handler consumes 20 microseconds of CPU time and an event source generates ten thousand interrupts per second, the simplified handler cost is 0.2 CPU seconds per wall-clock second, equivalent to twenty percent of one core's time. That says nothing about cache disruption, kernel scheduling or deferred work. If every event triggers a separate interrupt, very high event rates can dominate CPU budgets. Interrupt coalescing can reduce per-event overhead by grouping notifications but may add waiting latency. A real-time device may prefer lower latency over maximum throughput.

For a lab, construct a timeline involving user instruction execution, an interrupt arrival, priority arbitration, context saving, handler dispatch, device acknowledgment and return. Trace which data is architectural state and which is controller state. Then simulate simultaneous higher- and lower-priority events, specifying whether nesting is enabled. The number of instructions in a handler is not a substitute for measured latency, because a cache miss or disabled-interrupt region can dominate response time. Correct software must also handle the race between an event becoming pending and software checking or clearing its status; incorrect acknowledgment ordering can lose events. These are protocol bugs rather than mere optimization issues.

## 6.2 Dma

**Core model — Dma**

Direct memory access allows a controller to move buffers between a device and memory without CPU copying each word, although setup and completion still consume CPU work.

**Original worked illustration**

For 4096 bytes copied by a controller after a single setup operation, CPU per-byte transfer instructions can be avoided; memory bandwidth is still consumed.

**Boundary conditions and checks**

DMA does not eliminate coherence, pinning, address translation or security concerns; untrusted devices must not freely access arbitrary RAM.

### Extended technical chapter: Dma

Direct memory access permits a device or DMA engine to transfer data to or from memory without requiring the CPU to explicitly move every payload word. The CPU usually still configures descriptors, performs setup and handles completion or errors. DMA is not automatically faster for all transfers: short messages may spend more time in setup than would have been required for programmed I/O. Nor is DMA automatically free of CPU involvement or memory traffic. The intended benefit often concerns CPU overhead and efficient bulk transfer, with bus bandwidth and memory arbitration remaining finite resources.

A simple cost model illustrates the crossover. Suppose programmed I/O consumes ten nanoseconds of CPU activity per transferred word, while DMA setup costs one hundred nanoseconds plus one nanosecond of CPU work per word. For ten words, programmed I/O costs 100 nanoseconds and DMA costs 110; for one thousand words the costs are 10,000 versus 1,100. These are deliberately fictional CPU-cost assumptions, not device timing benchmarks. Solve 10N=100+N to find a crossover slightly above eleven words. In reality a descriptor-ring controller, cache maintenance, interrupt handling and transfer-completion latency can shift the crossover substantially.

Correct DMA requires attention to ownership, alignment, permissions and coherency. A CPU can write a buffer, issue DMA, then inspect completion only after the device has finished. If the CPU and device have incoherent caches or weak memory ordering, additional synchronization may be needed before consuming data. An IOMMU constrains which memory regions a device can access and can translate device-visible addresses. A laboratory diagram should track buffer ownership through CPU fill, device read or write, completion signal and CPU consumption. Inject a device error and show what prevents stale or partially transferred data from being interpreted as complete. The difference between bytes transferred and application-visible progress should be explicit.

## 6.3 Buses

**Core model — Buses**

A bus interconnect carries addresses, data and control transactions among agents. Arbitration governs which requester can use shared resources.

**Original worked illustration**

Two devices both demanding 100 MB/s cannot each receive that bandwidth indefinitely on a 150 MB/s shared bottleneck; queueing or throttling results.

**Boundary conditions and checks**

Nominal bus width times clock frequency is an upper bound that ignores protocol overhead and contention.

### Extended technical chapter: Buses

A bus or interconnect carries transactions among processing cores, memory controllers and peripherals. The architectural discussion involves address selection, transaction type, payload, ordering, arbitration and error handling. A narrow legacy shared bus and a modern switched point-to-point fabric may satisfy similar communication needs while having very different contention characteristics. Nominal signaling rate is not the same as delivered useful bandwidth: protocol overhead, encoding, directionality, packet headers, arbitration and competing traffic all affect throughput.

For an idealized sixty-four-bit data path transferring one word per clock at 200 MHz, raw data capacity is 8 bytes × 200 million cycles per second, or 1.6 GB/s in decimal units. If only 70 percent of cycles carry useful payload, effective throughput is 1.12 GB/s before counting software and memory-system constraints. A burst protocol amortizes address-phase overhead over multiple data beats. For an eight-beat burst preceded by two overhead cycles, payload efficiency on that link is 8/(8+2)=80 percent. The result is model-specific; it cannot simply be multiplied into every real interconnect without inspecting its actual protocol.

Ordering and isolation matter as much as bandwidth. A device might post writes and later issue a read requiring completion ordering, while another endpoint may observe reordering unless protocol guarantees forbid it. Multiple masters contending for a shared channel raise fairness and starvation questions. In a teaching exercise, schedule transactions from three requesters under round-robin and fixed-priority arbitration, count wait cycles, and show how a long burst blocks another requester. Then add a time-critical interrupt-related transaction and discuss how service guarantees can be enforced. The exercise should not mistake an ideal arbitration schedule for a physical design closure or electromagnetic signal-integrity verification.

## 6.4 Peripheral Interfaces

**Core model — Peripheral Interfaces**

Device interfaces expose registers, queues, descriptors and interrupts or polling. Drivers must observe specified ordering guarantees.

**Original worked illustration**

A ring of eight completion entries wraps index 7 to index 0. Producer and consumer indices disambiguate which descriptors remain outstanding.

**Boundary conditions and checks**

A bare status-register read may race with an interrupt or completion update; some devices require memory barriers and exact acknowledgement order.

### Extended technical chapter: Peripheral Interfaces

A peripheral interface is both a hardware protocol and a software contract. Register-mapped devices expose control, status and data registers whose reads and writes can have side effects. A status bit might clear on read, while a command bit triggers work when written. Treating these registers as ordinary cached memory can break interaction with the device. Drivers use appropriately ordered and width-controlled accesses, often alongside interrupts or DMA, to implement a reliable higher-level operation. A producer–consumer queue or descriptor ring commonly bridges asynchronous hardware and software timing.

Consider a transmit descriptor containing a buffer address, length and ownership flag. The CPU first fills the buffer, then writes descriptor fields, and finally transfers ownership to the device. Once ownership changes, the driver must not reuse or modify the buffer until completion is confirmed. If it changes the buffer too early, a transfer might contain mixed old and new data. If it sets the ownership flag before descriptor writes become visible to the device, the device can fetch an incomplete descriptor. The precise ordering primitive depends on the machine's coherence and memory model, which must be documented by the platform interface.

Interface documentation should specify reset defaults, legal ranges, error flags, maximum transfer sizes, alignment requirements and how errors are cleared. A state diagram can cover idle, configured, active, completed and failed states. Validate transitions such as a second start command while already active or a completion interrupt after software cancellation. A mock device simulator should deliberately return malformed status combinations to test defensive driver code. The purpose is not to imitate every transistor of an actual peripheral; it is to test the control protocol and expose assumptions that fail when the device is slower, faster, unavailable or adversarially misbehaving.

### Integrated laboratory: receive a data block without losing it

A fictional device transfers a block of four thousand 32-bit words to host memory. Three software designs are considered: polling for each word, interrupt-driven service for each word, and DMA. Each design must deliver the same four thousand words in order or report an error; it is not sufficient to move quickly if the payload is corrupted. Start by writing a data-integrity invariant: the receiver must not expose a buffer as complete until all required words are present and validation has succeeded. The buffer must not be reused while the device still owns it. This invariant can be checked under long delays, timeout and cancellation, not just a happy path.

Suppose programmed I/O consumes ten nanoseconds of CPU work per word. The simple CPU overhead is 40,000 nanoseconds. Suppose DMA setup costs one hundred nanoseconds, and per-word DMA bookkeeping costs one nanosecond of CPU time. Its modeled CPU overhead is 4100 nanoseconds. These numbers are fictional and deliberately omit elapsed bus transfer, memory contention and completion-handling cost. A claim of nearly tenfold reduction in CPU bookkeeping cannot legitimately become a claim of tenfold faster file download. A real device may be limited by throughput and still complete at the same wall-clock speed under either design.

An interrupt-based implementation should choose a notification strategy. If every word generates one interrupt and the handler costs five microseconds, processing four thousand words consumes twenty milliseconds of handler time, much more than the simplified raw movement overhead. Grouping notifications into batches could reduce interruptions, but waiting for a batch introduces additional response latency. Specify event rate and handler cost before selecting an approach. A bounded device ring adds another constraint: if software cannot process descriptors fast enough, ring entries may be overwritten or packets dropped under a specified policy. The architecture must expose status and error information sufficient for recovery.

DMA buffers require careful lifetime and memory-ordering rules. A producer-side CPU fills descriptor fields with buffer address and size, ensures those fields are visible, and only then sets ownership for the device. A device reads the descriptor, performs its transfer and signals completion after the relevant writes are visible. A consumer-side CPU checks completion, performs any required synchronization, and then reads the payload. A weakly ordered platform may need fences, cache maintenance or a coherent DMA allocation. Writing 'DMA completed' in a log before the buffer is safe to consume is a protocol defect. An IOMMU can limit device access to mapped regions, but a misconfigured mapping can still fail or permit an unintended region.

Bus bandwidth provides a separate lower bound. If the four-thousand-word payload is sixteen thousand bytes and the ideal payload bandwidth is 1.6 GB/s, its minimum raw transfer time is ten microseconds under the decimal-byte simplification. If protocol efficiency is fifty percent, the modeled transfer time is twenty microseconds. These times cannot be lower than physical link capabilities; they also exclude fixed command latency and the possibility that competing devices consume available bandwidth. A protocol trace should label address, data and completion phases so students do not silently merge setup cost with payload throughput.

The failure-injection notebook should test a DMA descriptor pointing to an unmapped address, a truncated transfer, a device reset halfway through delivery, an interrupt lost or delayed, and repeated completion signals. For each case, record what state is safe to expose to the application and how buffers return to the reusable pool. The correct solution prioritizes ownership and integrity before raw throughput. Hardware–software boundaries are most revealing when the device is not cooperating with the code's ideal timing assumptions.

### Review lens: protocol-level correctness before device throughput

I/O is a conversation between independently progressing components, so local arithmetic correctness is not enough. A descriptor may be numerically valid while the device reads it before the payload is ready. An interrupt handler may acknowledge an event correctly in one ordering but accidentally discard a newly arriving event in another. A fast DMA implementation may return a buffer to the free pool too early. Good tests therefore model ownership and completion explicitly, pause devices at sensitive steps, and inject timeouts or duplicated notifications. Timestamping transactions can diagnose latency, but passing a short timing benchmark cannot prove the protocol correct. The essential invariants concern not overwriting unread data, not exposing incomplete transfers, and eventually releasing resources under the specified recovery policy. Measure throughput only after those invariants hold under adversarial schedules.

### Additional guided investigations for asynchronous I/O

**Interrupt budget.** An input controller produces five thousand interrupts each second. If an average handler consumes ten microseconds, the directly modeled service cost is 50,000 microseconds per wall-clock second, or five percent of one core. At the same rate, increasing handler time to fifty microseconds raises modeled utilization to twenty-five percent. This comparison illustrates the sensitivity to handler work but cannot establish deadline satisfaction without arrival bursts, priority and maximum interrupt latency.

**DMA threshold.** Suppose a programmed transfer consumes eight CPU nanoseconds per word while DMA requires 160 nanoseconds setup plus two per word. Solve 8N=160+2N, giving crossover N=160/6≈26.67. For an integer payload of 26 words, programmed work is 208 nanoseconds while DMA work is 212, so programmed transfer is cheaper in this fictional model. For 27 words, programmed work is 216 and DMA work 214, reversing the ranking. Do not apply these imaginary numbers to a commercial device.

**Bus protocol.** A four-byte-wide interface operates at 100 million payload-capable cycles per second; raw maximum payload rate is 400 MB/s. If one out of five cycles is unavailable for payload due to overhead, modeled effective rate is 320 MB/s. If each transaction also requires a fixed startup delay, large batches improve efficiency by amortizing that cost. Compute for a 4096-byte payload before and after reducing utilization to fifty percent. Distinguish byte rate from CPU overhead and end-to-end service time.

**Device-state investigation.** Model peripheral states IDLE, CONFIGURED, ACTIVE, DONE and ERROR. A start command in CONFIGURED moves to ACTIVE, while a start in ACTIVE is rejected or queued according to the documented policy. A completion event becomes DONE only after all buffer writes are visible. Inject a device reset during ACTIVE and choose an explicit strategy for identifying incomplete data. A robust driver cannot silently mark the buffer complete because the completion interrupt may have been lost or delayed.

### Diagnostic challenge: avoid a lost completion notification

A driver submits a DMA descriptor, checks a device-completion flag and goes to sleep awaiting an interrupt. If the device completes and generates the notification between the flag check and the sleep operation, an incorrectly designed driver can miss the event and wait indefinitely. Safe designs combine state checks and waiting under synchronization primitives or use event mechanisms whose semantics prevent the race. Model the sequence as CPU_CHECK, DEVICE_COMPLETE, CPU_SLEEP and ask why this interleaving is dangerous. Then design a recovery strategy with a bounded timeout and a subsequent status recheck; a timeout mitigates indefinite waiting but is not a substitute for a correct event protocol. Distinguish delivery of an interrupt from completion of the data transfer, because device memory writes may need explicit ordering and synchronization before buffers are consumed. The exercise demonstrates that performance features require protocol-level correctness across asynchronous agents and that a passing transfer-speed test does not validate all scheduling interleavings.

## Three worked problems

### Interrupts: worked application 1

Given 100 interrupts per second and 20 microseconds service each, find CPU service time per second.

**Set up the model and conditions**

Multiply event rate by handler cost: 100×20 μs.

**Carry out the calculation or proof**

Result is 2000 μs=2 ms.

**State the result and its scope**

The direct service share is 0.2% of one second, excluding other overhead.

**Independent verification, conditions, and interpretation**

One hundred interrupts per second times twenty microseconds of direct service per interrupt gives 2000 microseconds of service activity each second. Since one second contains one million microseconds, the CPU-service fraction is 2000/1,000,000=0.002, or 0.2 percent of one core's time. The dimensional check is interrupts/second × microseconds/interrupt = microseconds/second. This figure assumes every event arrives and is serviced and that the handler cost is fixed. It excludes context-switch effects, caches, controller arbitration and deferred work. If the event rate rises to ten thousand per second under the same cost model, service rises to 200,000 microseconds per second, or twenty percent of a core. That tenfold rate comparison helps expose why high-frequency events are often batched or coalesced. But coalescing can delay notification and change latency, so the optimization objective should be specified. The question does not measure maximum interrupt latency, which depends on the longest delay before a handler can start as well as handler duration. A utilization calculation alone cannot establish a real-time deadline guarantee.

### Dma: worked application 2

For ring queue capacity eight and initial producer index seven, advance by three writes.

**Set up the model and conditions**

Update position as (7+3) mod 8.

**Carry out the calculation or proof**

10 mod 8 is 2.

**State the result and its scope**

The producer index becomes 2, assuming capacity/space constraints are separately satisfied.

**Independent verification, conditions, and interpretation**

A circular ring of capacity eight uses indices from zero through seven. Starting at producer index seven and advancing three logical writes yields (7+3) mod 8 = 10 mod 8 = 2. The path crosses slots seven, zero and one, leaving the next available producer position at two under a convention in which the index points to the next slot to write. This is index arithmetic only. Whether all three writes are legal depends on the consumer position and the ring's full/empty convention. Some designs reserve one slot to distinguish full from empty, while others maintain a separate count or phase bit. A real descriptor ring must also define ownership and memory ordering so the consumer never processes a partially initialized slot. If the producer wraps but the consumer has not advanced, the correct action may be to block, return an error or drop data rather than overwrite unread descriptors. Verify separately the zero-write case, a full eight-slot advance, and two complete wraps. The modulo result is necessary for correctness but insufficient for an entire concurrent queue implementation.

### Buses: worked application 3

A DMA controller copies 4096 bytes after a CPU setup operation. What work remains for the CPU?

**Set up the model and conditions**

The CPU prepares descriptors and validates buffer ownership/mapping.

**Carry out the calculation or proof**

The controller performs the transfer while the CPU may execute other tasks and later handles completion.

**State the result and its scope**

DMA avoids per-byte CPU copy instructions, but setup, synchronization and memory bandwidth remain.

**Independent verification, conditions, and interpretation**

DMA means a controller transfers the four-thousand-ninety-six-byte payload using bus and memory transactions after being configured; the CPU generally avoids executing one explicit copy instruction per byte or word. The CPU still typically prepares a descriptor, supplies buffer addresses and lengths, starts the transaction, synchronizes relevant memory, and handles completion or errors. The DMA engine still consumes memory-system bandwidth, which can contend with processor requests. A raw lower bound for transferring 4096 bytes over an ideal 1 GB/s link is 4096 nanoseconds, about 4.096 microseconds, before protocol overhead. That quantity is elapsed-transfer capacity, not CPU overhead saved. A correct response must also discuss the device's permissions: an IOMMU can restrict DMA access to intended memory regions. The buffer cannot be reused until completion is certain and any necessary visibility rules have been satisfied. If the transfer is interrupted, the program must not expose partially filled data as complete. DMA improves the architecture of data movement, but its effectiveness depends on transfer size, setup overhead and the surrounding protocol. Comparing DMA and programmed I/O without these variables is incomplete.
