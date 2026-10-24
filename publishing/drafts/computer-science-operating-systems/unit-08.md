# Operating Systems — Unit 8: Distributed and practical systems

networking interfaces; observability; containers; performance diagnosis

## §8.1 Networking Interfaces

**Core model — Networking Interfaces**

Network interfaces expose sockets and packet delivery abstractions. The OS handles buffering, route selection and demultiplexing.

**Original worked illustration**

A TCP socket identifies an endpoint within a connection using addresses and ports; multiple connections may share a server's listening port.

**Boundary conditions and checks**

TCP is a byte stream, not a message API. One recv call need not return one application request.

### Socket abstractions, framing, and partial I/O

An operating system exposes networking through interfaces such as sockets, which provide an application endpoint abstraction over protocol processing and device delivery. TCP offers an ordered byte stream with connection semantics; it does not preserve application-level message boundaries. UDP sends datagrams with different delivery and ordering properties. A successful write into a socket buffer does not imply the remote application has decoded or durably processed the message. A client must define its own application framing, acknowledgments, retries, and idempotency rules according to the consequences of failure.

Suppose a server expects records prefixed by a four-byte unsigned length. It must accumulate exactly four bytes to decode the length, validate that length against configured bounds, and then accumulate the payload. A read call can return one byte of header, three bytes, a full record, or multiple records at once. The parser therefore maintains state across reads; treating one receive call as one record will intermittently fail under ordinary network behavior. If a client times out after sending a request, it may be unable to tell whether the server processed it but the response was lost. Blind retries of non-idempotent operations can create duplicate charges or writes. Sequence numbers or idempotency keys are application design choices that address that ambiguity.

Connection closure also has several meanings. A graceful read-side end-of-stream is different from a temporary lack of available bytes, local cancellation, and a reset. Backpressure from a slow receiver can fill sender buffers and eventually block or reject new sends depending on API mode. An educational lab models a stream as a list of arbitrary chunk sizes, feeds a framed record one chunk at a time, and asserts the same decoded result for every partitioning of the same byte sequence. Add a malformed oversized length and truncated payload. Then compare an at-most-once request protocol with one that retries but uses an idempotency key, showing exactly which failures still require explicit operator decisions.

## §8.2 Observability

**Core model — Observability**

Observability gathers logs, metrics and traces to explain running behavior. A useful diagnosis connects measured symptoms to process states and resource contention.

**Original worked illustration**

If CPU utilization is low but request latency is high, inspect blocking I/O, lock waits and queueing rather than optimizing arithmetic first.

**Boundary conditions and checks**

High aggregate utilization may hide one saturated core; sample intervals and clock resolution limit diagnosis.

### Observability, queuing, and causal diagnosis

Observability means collecting enough evidence to explain how a system behaves, including under unexpected load. Common signals include throughput, latency distributions, queue depth, CPU utilization, memory pressure, I/O waiting, error counts, and traces spanning dependency calls. Metrics should be interpreted together. A server whose CPU is only 20 percent busy can still be overloaded if requests are waiting on a saturated disk or a serialized lock. A high average throughput can coexist with unacceptable p99 latency. Measurement labels should distinguish wall-clock time, CPU execution time, and blocked time, since optimizing the wrong component wastes effort.

Start with the service's user-visible objective. If a request takes 200 milliseconds, a trace might attribute 2 milliseconds to parsing, 18 to local computation, and 180 to a database wait. Even eliminating parsing entirely can save no more than 1 percent of the observed total. Increasing parser performance tenfold is even less significant. This is an example of Amdahl-style bounded optimization: speedup depends on the fraction of time affected. The trace could still be misleading if it omits queuing before request acceptance or if sampling biases results toward successful fast calls. Always record the exact measurement boundary and sample inclusion rule.

Queue growth is an important early signal of capacity limits. For a stable arrival process, Little's Law relates mean number in system, arrival throughput, and mean time in system, but it does not identify the slow component without further evidence. Instrument each stage's arrival and completion events and compare input rate to service rate. A lab supplies a synthetic timeline of twenty requests with timestamps for queue entry, worker start, database completion, and response. Compute wait times, service times, and overall latency separately, then calculate the mean and a clearly specified percentile method. Repeat after an artificial database slowdown and identify which metric changes first. Avoid using a single mean to justify a user experience claim for interactive workloads with heavy tails.

## §8.3 Containers

**Core model — Containers**

Containers package processes with namespace and resource-control configurations. They provide deployment consistency but not a new hardware abstraction.

**Original worked illustration**

Two containers can share the same Linux kernel while having different mount namespaces and constrained memory budgets.

**Boundary conditions and checks**

Container images do not remove kernel vulnerabilities; 'containerized' is not synonymous with fully isolated.

### Containers, namespaces, cgroups, and operations

Containers bundle an application with its user-space dependencies while relying on operating-system isolation mechanisms. Process identifiers, mount views, network interfaces, users, and other namespaces can provide differentiated views of the host. Resource controllers can limit CPU time, memory usage, and I/O weights or limits subject to kernel and orchestrator support. An image is a packaging artifact; a running container is an execution context. Confusing the two leads to security mistakes, such as believing an immutable image prevents runtime data writes or assuming a process inside a container has no access to host resources under misconfigured mounts.

A memory limit is not the same as a performance guarantee. If an application allocates too much memory, a controller may trigger memory pressure or terminate work. If the host is oversubscribed, CPU quotas and priorities influence scheduling but cannot create physical capacity. Containerized workloads also need correct signal handling and shutdown rules. A service receiving a termination request should stop accepting new work, finish or cancel in-flight operations under a deadline, release its resources, and exit with a meaningful status. Replacing the main application process with a wrapper that does not forward signals can prevent graceful shutdown, even though the image builds and the service starts normally.

For a practical exercise, design a container deployment for a worker that accepts jobs and writes output to one mounted directory. Specify image contents, read-only root filesystem if feasible, numeric user identity, resource limits, writable paths, network policy, and how credentials are injected without baking them into the image. Next, introduce a failed downstream dependency. Show how readiness and liveness checks should differ: a temporary database outage may make the service unable to accept work without proving that its process is irrecoverably dead. Compare a single container on one machine with multiple replicas behind a queue. Analyze duplicate processing on worker crash and explain why scaling a stateless frontend differs from scaling a stateful database.

## §8.4 Performance Diagnosis

**Core model — Performance Diagnosis**

Performance diagnosis begins with a workload, a baseline, a reproducible measurement and a bottleneck hypothesis. Improve the limiting resource, then measure again.

**Original worked illustration**

If throughput is 100 requests/s and queue time dominates a 200 ms response, caching a small parsing step cannot plausibly halve response time.

**Boundary conditions and checks**

Optimizing a non-bottleneck stage produces little system benefit; use distributions including tail latency, not mean alone.

### Bottlenecks, controlled experiments, and production diagnosis

Performance diagnosis is an iterative process: define the observable failure, isolate the time or resource range, form competing hypotheses, and run a measurement that discriminates between them. A request becoming slower during peak load could be caused by CPU queueing, lock contention, database saturation, kernel socket buffers, disk writeback, or downstream rate limits. The fact that CPU utilization is high is evidence, not a complete causal explanation. It could reflect useful work, busy waiting, excessive serialization overhead, or a pathological retry loop. Similarly, low CPU utilization does not imply that adding CPU cores will help.

A useful experimental strategy changes one resource constraint at a time while keeping workload shape constant. Record throughput and p50, p95, and p99 latency for a fixed input distribution; then adjust concurrency or queue capacity, keeping all other assumptions stable. If throughput no longer rises while latency and queue size grow, demand may have exceeded the bottleneck's service capacity. If performance improves sharply after reducing an unnecessary lock scope, contention was important. But production systems introduce background noise: caches warm, autoscalers react, other tenants compete, and data distribution shifts. Replicated runs and comparison controls help avoid crediting a change that merely coincided with lower load.

Consider a report generator taking 500 milliseconds: 10 milliseconds parsing, 20 rendering, 430 waiting on storage, and 40 serializing output. Making parsing ten times faster reduces its contribution from ten to one millisecond, so the total falls to about 491 milliseconds, a 1.8 percent improvement under this fixed-component model. That is not a reason never to optimize parsing; it is a reason to match optimization effort to target outcomes. A lab should derive an upper bound for three candidate improvements, then propose one instrumentation change and one controlled test for each hypothesis. Afterward, write a short incident analysis stating observations, ruled-out explanations, uncertainty, and the next measurable decision. A completed exercise avoids claiming production causality from a single synthetic benchmark.

### Integrative case study — investigating a slow API service

A web API reports increased response times during peak activity. Initial dashboards show modest CPU utilization but many pending requests. A common mistake would be to add CPU instances before identifying why requests wait. Instead construct a stage-level trace: accept request, parse input, authenticate, query storage, compute response, transmit reply. Record timestamps at each transition, together with queue depth and concurrent operations. The stage with the largest elapsed time is not necessarily the only cause, but it is a more productive starting hypothesis than guessing from total latency. A blocked I/O call and a runnable thread waiting for CPU demand different interventions.

Suppose a representative request takes 200 milliseconds: two parsing, eighteen local computation, 170 waiting for a database result, and ten serialization/network response. Parsing makes up one percent of total latency. A twofold parser speedup saves one millisecond, only a half-percent reduction if every other contribution stays fixed. Doubling local computation speed saves nine milliseconds, a 4.5 percent reduction. Reducing database waiting by half potentially saves 85 milliseconds, subject to changes in queueing and dependencies. These are upper-bound arithmetic comparisons under a fixed decomposition, not a production performance forecast. The database component may be slow because of disk queueing, contention on locks, poor query selection, missing indexes, or an overloaded network path; a single 'database wait' label does not distinguish them.

Now consider Little's Law. If a stable service completes fifty requests per second and average in-system time is 0.2 seconds, the average number of requests present is about ten. If measured in-flight requests double while throughput remains the same and the system remains within a meaningful steady state, average time in system must also increase. However, during an overload transition, averages over mismatched windows can violate a naive comparison. Measure arrival rate, completion rate, and queue length on the same time scale. Track timeouts and abandoned requests; counting only successful responses biases the reported latency downward precisely when the service is failing.

Plan a controlled experiment. Hold input mix and data volume stable, measure throughput and p95 latency over repeated trials, and separately change database concurrency, worker pool size, and a query index under review. Each intervention should have a predicted direction of change and a possible adverse effect. Raising concurrency may initially increase throughput but eventually raise queueing and lock contention. Increasing a cache may reduce reads but increase memory pressure and garbage-collection pauses. An index may accelerate reads while making writes more expensive. Evaluate end-to-end user-visible latency rather than selecting the component that yields the most dramatic microbenchmark.

A practical incident report includes a short timeline, observed metrics, hypotheses, tests, and remaining uncertainty. Suppose traces show 150 milliseconds blocked behind a storage semaphore, CPU remains low, and disk service time increases as queue depth rises. That strengthens a storage-contention hypothesis, but further tests should distinguish device saturation from a poorly configured application connection pool. Preserve a rollback path for configuration changes and verify that a fix does not degrade other endpoints. The final recommendation should be proportional to evidence: 'reduce oversized batch writes and retest p95 under the original load' is better grounded than 'the operating system cannot handle traffic.' The goal is to produce decisions that remain defensible when the workload changes.

### Diagnostic exercise — avoid optimizing the wrong stage

An API endpoint spends two milliseconds parsing, eight doing CPU computation, 180 awaiting a downstream operation, and ten sending its response. Without overlap, total latency is 200 milliseconds. A tenfold faster parser reduces the total by 1.8 milliseconds to 198.2 milliseconds, not to twenty milliseconds. A twofold faster downstream operation could save ninety milliseconds under the same additive model. These are bounds conditioned on unchanged queues and dependencies. Instrument a request timeline showing when each stage begins and ends, then introduce a separate admission queue before the first recorded trace span. Explain how omitting that queue could produce deceptively good latency numbers. Compare the mean with a p99 dominated by occasional storage stalls; define how many samples and which percentile convention the exercise uses. Finish with one falsifiable hypothesis about queue depth and one controlled measurement capable of weakening that hypothesis.

### Boundary cases and falsifiable design claims

Mean service latency and tail latency answer different questions. Suppose ninety-nine requests finish in ten milliseconds and one takes one second. The mean is approximately 19.9 milliseconds, but the slowest one percent experiences an entirely different quality of service. A percentile must specify an estimator and a sample window; on a small data set, two valid conventions can differ. Averages computed only over successful responses also hide timeout failures and cancellations. A useful dashboard pairs latency distributions with error rates, request counts, and in-flight queue depth so that dropped demand does not masquerade as improved responsiveness.

CPU accounting also needs context. A service blocked on a single serial lock may use little CPU even while its queue grows. Increasing the worker count can increase contention and make latency worse. A storage service with a deep queue can saturate without high application CPU usage. A slow dependency can cause retry storms that raise load further, and timeouts chosen without backoff can synchronize bursts across clients. Controlled experiments should track attempted requests and completed requests separately, with explicit deadlines and retry policy.

A capstone diagnosis compares a baseline workload against a changed workload with the same total request rate but larger response payloads. If latency increases, possible causes include network transmission, response serialization, allocation, and queueing. The investigator should not automatically blame the database. State two rival hypotheses, record which trace spans would distinguish them, and select a safe, reversible intervention for the next test. This makes performance analysis falsifiable and teaches the discipline of measuring the system actually built rather than optimizing a preferred abstraction.

## Three worked questions

### Networking Interfaces: worked application 1

For a TCP socket, a sender writes a 100-byte message. Must the receiver get exactly 100 bytes from one recv call?

**Set up the model and conditions**

TCP supplies an ordered byte stream, not application-message boundaries.

**Carry out the calculation or proof**

A recv may return fewer bytes, requiring buffering until the application protocol frame is complete.

**State the result and its scope**

No; loop over partial reads and explicitly frame application messages.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

TCP presents an ordered byte stream. A sender's hundred-byte write does not obligate the receiver to obtain those hundred bytes from a single receive call. The receiver might read twenty, then thirty, then fifty bytes, or any other partition permitted by buffering and the call contract. Application-level protocols therefore need explicit message framing, such as a length field, delimiter with escaping, or a fixed-size record. A robust receiver accumulates bytes, checks the declared total, and handles EOF before completion as a truncated message. A successful send may mean bytes entered local buffers rather than proof the remote application committed them. Verify a parser by partitioning the same valid record into one-byte, random-size, and whole-record chunks and asserting identical decoded output. Separately test maliciously large length fields and premature stream closure.

### Observability: worked application 2

CPU is 20% busy while requests wait 150ms on a disk queue. Which resource merits investigation?

**Set up the model and conditions**

Low CPU occupancy makes arithmetic throughput a weak first hypothesis.

**Carry out the calculation or proof**

A large queue delay directs analysis toward storage saturation, I/O concurrency, service time and queue depth.

**State the result and its scope**

Investigate storage waits first, then confirm with a controlled measurement.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

CPU busy fraction and request delay measure different phenomena. A CPU reading twenty percent utilization may have ample idle execution capacity while tasks block on storage completion, lock ownership, or external network service. A measured 150-millisecond disk queue wait suggests investigating queue depth, request service time, writeback behavior, and concurrency at the storage layer. It is still a hypothesis: instrumentation errors or unrelated slow stages can mislead. Compare disk wait spans in request traces to block-device latency metrics, verify that timestamps share a consistent clock, and inspect both the median and upper tail under the same load window. Adding CPU cores will not shorten a serial disk queue if storage remains the limiting service station. A controlled test that reduces concurrent storage requests or isolates the workload can distinguish saturation from an application-level semaphore bottleneck.

### Containers: worked application 3

A service takes 200 ms with most time waiting for database I/O. Can reducing a 2 ms parser to 1 ms halve total latency?

**Set up the model and conditions**

Reduce parser by one millisecond at best without changing other work.

**Carry out the calculation or proof**

New latency is roughly 199ms rather than 100ms.

**State the result and its scope**

No: parser optimization alone saves only about 0.5% of baseline latency.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Baseline latency is two hundred milliseconds, of which parsing takes two. Halving parser work saves at most one millisecond if every other component stays constant; estimated new latency is 199 milliseconds. The relative reduction is one divided by 200, or 0.5 percent. To halve the entire response to one hundred milliseconds while changing parsing alone would require an impossible negative parsing duration, since the other components already consume 198 milliseconds. This is a simple instance of Amdahl-style reasoning. A performance engineer should identify the expensive database wait and test what causes it, rather than optimizing a convenient small function. The arithmetic applies to the stated serial component decomposition, not automatically to concurrent pipelined execution in which reducing one stage could affect queues elsewhere.
