# Operating Systems — Unit 2: Processes and threads

execution contexts; scheduling; context switches; thread models

## §2.1 Execution Contexts

**Core model — Execution Contexts**

A process contains a virtual address space, security context and resources. Threads within a process normally share address space while retaining distinct execution state and stacks.

**Original worked illustration**

Two threads updating a shared counter without synchronization may both read 5 and both write 6, losing an increment.

**Boundary conditions and checks**

Sharing memory reduces explicit message passing but introduces races and lifetime hazards not present in isolated-process data.

### Address spaces, execution contexts, and lifecycle

A process is a managed execution environment with an identity, protection context, virtual address mappings, descriptors, and other kernel-tracked resources. A thread is a schedulable flow of control with its own program counter, register state, and stack. Common threading models allow threads in one process to share mappings and file resources, but not an identical logical execution stack. Treating a thread as 'a small process' loses crucial sharing semantics: an accidental write through a shared pointer can damage another thread's data without crossing a hardware memory-protection boundary. Separate processes usually provide a stronger fault boundary but require explicit interprocess communication and more deliberate handling of shared state.

The states 'new,' 'ready,' 'running,' 'blocked,' and 'terminated' are a useful teaching model, not a universal list of concrete kernel flags. A blocked thread may await a condition variable, disk completion, timer, or socket readability. The transition to ready means it can be considered for execution; it does not promise immediate access to a CPU. A scheduling decision can preempt a running thread, or a thread can voluntarily yield. If a process exits while other threads exist, the runtime must define what happens to their work and pending I/O. Join operations coordinate completion and resource reclamation; detach operations change the party responsible for joining, not the fact that resources eventually need cleanup.

For a trace, define two threads A and B with independent register sets and a shared counter. Let A load the counter into a register, then be preempted. B loads and increments the old value, stores its result, and yields. A resumes and stores an increment based on stale state. Each thread individually followed a plausible instruction sequence; the shared result is wrong. The problem arises because a read-modify-write sequence is not automatically atomic. To contrast isolation models, run the conceptual trace again with each worker in a separate process and the counter stored only in a private mapping. The lost update disappears, but so does shared progress; an explicit message or shared-memory object becomes necessary. Evaluate systems by ownership and synchronization assumptions, not merely the number of processes or threads displayed in a task manager.

## §2.2 Scheduling

**Core model — Scheduling**

CPU scheduling chooses which runnable execution entity uses a processor. Different objectives include fairness, throughput, average turnaround, interactive response and deadlines.

**Original worked illustration**

For jobs arriving at time 0 with bursts 4 and 2, FCFS order [4,2] yields completion times 4 and 6; shortest-job-first [2,4] yields completion times 2 and 6.

**Boundary conditions and checks**

Shortest-job-first needs burst estimates and can starve long jobs under continuous arrivals; fairness and mean completion time are competing objectives.

### Scheduling objectives, fairness, and measurable trade-offs

Scheduling algorithms answer which runnable task receives a processor next, but there is no single performance metric that captures all workload goals. Turnaround time is completion minus arrival; response time is first execution minus arrival; waiting time sums intervals ready but not running. Throughput counts completed jobs per period. Interactive services often value quick initial response and bounded tail latency, while batch jobs may prioritize throughput. A scheduler minimizing average turnaround under ideal information can create very long waits for some jobs. Fair allocation may produce larger average turnaround but more predictable treatment. Context-switch cost further complicates comparisons when time quanta become very short.

Under first-come-first-served scheduling, all jobs arriving at zero execute in submission order. For bursts 8, 2, and 1, the completion times are 8, 10, and 11, yielding mean turnaround 29/3 time units. With shortest-job-first order 1, 2, 8, the completion times are 1, 3, and 11, and the mean becomes five units. This does not prove that SJF is universally superior: the short-job lengths may be unknown, jobs may arrive later, and starvation becomes possible when short jobs continuously enter. Preemptive shortest-remaining-time policies allow newly arriving jobs to interrupt longer ones, trading implementation complexity and overhead for a different turnaround profile. A carefully designed comparison must specify arrival times, burst knowledge, quantum, and the treatment of ties.

Round robin allocates each runnable task a bounded slice before moving to the next, assuming it has not blocked or completed. For quantum two and the three jobs above, simulate a queue rather than simply dividing bursts by quantum; a completed task does not reenter, and newly arriving tasks require a declared insertion rule. Smaller quanta tend to improve opportunities for response while raising the rate of switches, but effective response also depends on ready-queue size and priorities. In a lab, implement a discrete-event scheduler that emits start/end intervals and then independently reconstruct turnaround, response, and waiting times from that timeline. Introduce a switch cost and show where CPU time is consumed without completing useful application work. Never report a performance claim from a timeline that ignores the overhead it is ostensibly comparing.

## §2.3 Context Switches

**Core model — Context Switches**

A context switch saves and restores execution state, including registers and address-space identifiers where needed. Its cost includes direct save/restore and indirect cache effects.

**Original worked illustration**

If 1000 switches each cost 5 microseconds of direct CPU work, the overhead is 5 milliseconds, excluding cache and TLB disruption.

**Boundary conditions and checks**

Switch cost is workload- and hardware-dependent; multiplying a published constant without measurement creates false precision.

### Context switches and the cost of changing execution ownership

A context switch saves enough state for one execution context to resume and restores state for another. Depending on the platform and transition, state can include integer registers, program counter, stack pointer, floating-point or vector registers, address-space identifiers, and accounting metadata. Not every trap or system call forces a switch to a different thread, and not every user-to-kernel transition requires replacing the active address space. Conversely, a thread can be switched while still remaining inside kernel code. Distinguish a privilege transition, a scheduling decision, an address-space switch, and a hardware interrupt instead of treating all four as interchangeable events.

The direct switching time often understates its performance consequences. A new thread may displace useful instruction and data cache lines, disrupt branch predictor history, change the active translation context, or compete for shared cache capacity. Some architectures provide address-space identifiers that permit multiple translation contexts to coexist in a translation cache; others require invalidation in specific situations. That means two measured tasks with the same apparent switch count can incur different overhead depending on working-set size, affinity, and memory hierarchy. Timing an empty yield loop is informative about one narrow path, not a complete estimate for a loaded application server.

Suppose one thousand switches each require five microseconds of direct bookkeeping. Multiplication gives five milliseconds. If the switch rate is one thousand *per second*, the direct fraction of one CPU-second spent in switching is five milliseconds divided by one second, or half a percent. Those two calculations answer different questions; avoid labeling the first as an utilization percentage. Add an estimated ten microseconds of cache-rewarm penalty only if the experiment specifies a consistent model for that penalty. Under that assumption the total would be fifteen milliseconds, or 1.5 percent at the stated switch rate. To investigate the real system, trace CPU migration, runnable queue depth, involuntary versus voluntary switches, and cache-miss rates. Make a performance recommendation only after comparing a representative workload under controlled affinity and load. A shorter quantum cannot fix a task blocked on a slow network database.

## §2.4 Thread Models

**Core model — Thread Models**

User-level and kernel-level thread models choose where scheduling and blocking operations are managed. One-to-one threads enable parallel execution but consume kernel resources.

**Original worked illustration**

A user-level scheduler can switch coroutines without a kernel transition when no blocking operation occurs, while a blocking system call may obstruct progress if not integrated with asynchronous I/O.

**Boundary conditions and checks**

The word thread does not imply a specific runtime or preemption policy; clarify green threads, OS threads and async tasks.

### Thread libraries, work pools, and structured concurrency

A language-level thread is not always a one-to-one kernel thread. Some runtimes multiplex lightweight tasks or coroutines over worker threads; others create one kernel-managed thread per user thread. The mapping affects where blocking is observed. If a lightweight task invokes an operation that blocks its entire worker thread, the runtime must either integrate with a nonblocking interface, hand the blocking work to a separate pool, or accept reduced parallel progress. Calling work 'asynchronous' does not create parallel hardware execution by itself. A single event loop can overlap waiting activities yet still serialize CPU-heavy callbacks; multiple workers can process CPU work concurrently but incur synchronization and scheduling costs.

Consider a server with four CPU cores and a hundred connections. Launching a hundred active CPU-bound threads does not provide a hundred processors; it produces contention for the same four cores, often with extra switching and cache pressure. A bounded worker pool can cap active CPU computation at a small multiple of available cores while queuing additional requests. For primarily waiting tasks, more concurrent requests may be useful, but connection limits, memory occupancy, downstream rate limits, and cancellation behavior become essential. A concurrency limit is a resource-policy choice, not a universal tuning constant.

Structured concurrency treats child tasks as belonging to a scope whose completion, errors, and cancellation are managed together. Without such structure, a child may continue using a buffer after its parent request has returned, or exceptions may be silently discarded. A safe workflow declares task ownership and ensures that exit waits for children or cancels them according to a well-defined policy. A lab should contrast three designs: one thread per request, a fixed worker pool, and an event-driven design with explicitly bounded CPU workers. List each design's maximum active computation, memory-per-task estimate, error propagation path, and shutdown behavior. Include a simulated slow downstream call and a CPU-heavy handler so the difference between overlap and parallelism is visible. Evaluate throughput alongside tail latency and cancellation correctness.

### Integrative case study — choosing a job scheduler under load

Consider a single CPU that must handle three jobs arriving simultaneously, with known CPU bursts of eight, two, and one millisecond. Under FCFS in that order, finish times are eight, ten, and eleven milliseconds. The mean turnaround is 29/3, about 9.67 milliseconds. Under nonpreemptive shortest-job-first, their service order becomes one, two, eight, with finish times one, three, and eleven and mean turnaround five milliseconds. The example shows an improvement for one specified workload and objective. It does not establish that SJF provides acceptable response time when burst lengths are uncertain or when short tasks keep arriving ahead of a long task.

Now introduce interactive arrivals. Job A arrives at time zero and needs eight milliseconds; job B arrives at two and needs one; job C arrives at three and needs two. Nonpreemptive FCFS runs A from zero to eight, B from eight to nine, and C from nine to eleven. Turnaround times are eight, seven, and eight, giving mean 23/3. A preemptive shortest-remaining-time policy interrupts A when B arrives, runs B from two to three, then runs C from three to five, and resumes A from five to eleven. Turnaround times are eleven, one, and two, yielding mean 14/3. The timeline must include arrival and completion instants explicitly to avoid assigning idle or blocked periods to the wrong task. If preemption costs one millisecond every time, the advantage shrinks and requires a fresh trace rather than a post-hoc subtraction.

Round robin with a quantum of two and all three original jobs at time zero illustrates a different objective: each process gets early processor access. Begin with queue A,B,C. Run A for two, B for two and complete it, C for one and complete it, then continue A until finished. First response times become zero, two, and four milliseconds, which may be fairer than giving the shortest job immediate preference. Yet the long job finishes later because other work is interleaved, and a very small quantum increases direct switch costs. The scheduler's queue-insertion rule at simultaneous arrivals must be fixed so that students can reproduce its timeline.

A practical scheduler must also distinguish CPU bursts from waiting. Suppose job B runs one millisecond, blocks five milliseconds on network I/O, then runs another millisecond. Recording B as seven consecutive CPU milliseconds would falsely attribute its waiting to processor demand and distort the scheduling comparison. A discrete-event model should support READY, RUNNING, BLOCKED, and DONE states and schedule CPU and I/O completion as separate events. It should record useful CPU time, switch overhead, idle time, response time, and turnaround per task. The sum of all CPU occupation intervals, including switching, should not exceed the modeled available processor time.

The engineering decision depends on service goals. A batch queue seeking low average turnaround might favor predicted short jobs with an aging mechanism to protect long jobs. An interactive service might reserve latency-sensitive capacity or use time-slicing. A real-time task may require explicit deadline and admission guarantees rather than ordinary fairness. State whether priorities can preempt running work and whether starvation is allowed. Validate the implementation using a hand-checkable three-job trace, then test a job arriving exactly at a quantum boundary and a job whose burst equals one quantum. A sophisticated implementation that cannot pass those small correctness cases is not ready for a realistic workload.

### Diagnostic exercise — reason from complete timelines

A correct scheduling trace has an invariant: on a single-core nonoverlapping model, exactly zero or one job occupies the CPU at any instant. Include context-switch intervals explicitly if modeled. Supply four tasks with arrivals 0, 2, 2, 5 and bursts 3, 4, 1, 2; set quantum to two. Run FCFS, SJF with only ready jobs eligible, and round robin under a declared simultaneous-arrival tie rule. For every result, compute response time, waiting time, turnaround, and completion timestamp; verify turnaround equals waiting plus CPU burst when jobs have no blocked I/O and switch cost is excluded. Look for starvation in a workload where tiny jobs arrive repeatedly ahead of one long job. Do not use this artificial trace to select a production scheduler; it isolates properties and teaches auditing. Next introduce an I/O block to one job and ask why response and turnaround change even when CPU service demand remains fixed. This challenges students to separate CPU allocation from completion latency.

### Boundary cases and falsifiable design claims

Scheduling comparisons are particularly sensitive to jobs whose arrival or completion coincides with a time quantum boundary. When a job completes exactly as another arrives, the simulation must define whether the completion is processed before the arrival and whether a switch cost applies. An unspecified tie rule can change response times even with identical bursts. A job with zero CPU demand is a boundary case: some models should complete it immediately without consuming a quantum, while others reject zero as outside their workload definition. Every simulator should state this choice. A blocked job must leave the ready queue until its I/O completion event; otherwise the CPU timeline would overcount work.

Fairness claims require an observation window. Round robin offers repeated scheduling opportunities for runnable tasks under suitable assumptions, but it cannot guarantee each task finishes quickly if one process repeatedly waits on external resources or higher-priority work interrupts normal scheduling. Priority boosts and aging can reduce starvation, while affinity can improve locality yet produce uneven load between cores. On a multicore machine, assigning four active tasks to one core while leaving another idle has different implications than the same tasks distributed evenly. This makes processor affinity and migration part of scheduling policy, not merely optimization afterthoughts.

A lab should produce two workload distributions with the same total burst demand but different mixes of short and long jobs. Calculate mean turnaround and maximum response for each policy, not just aggregate throughput. Add a scenario where a job arrives one microsecond before another instead of simultaneously, and verify that the specified tie rule no longer determines their order. Use a monotonic simulation clock and reject negative burst lengths. Finally, check conservation of CPU time: aggregate useful execution equals the sum of completed CPU burst demands, with switch overhead and idle gaps recorded separately. This catches timeline bugs in ways a final mean can conceal.

## Three worked questions

### Execution Contexts: worked application 1

For jobs of burst times 4 and 2 arriving at zero, compute mean turnaround under FCFS [4,2].

**Set up the model and conditions**

Completion times are 4 and 6 because the second job waits for the first.

**Carry out the calculation or proof**

Turnaround equals completion time minus arrival time, both zero.

**State the result and its scope**

Mean turnaround is (4+6)/2=5 units.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Define each job's turnaround time as completion minus arrival. With both arrival times zero, FCFS order [4,2] produces first completion at four and second completion at six. Turnaround values are four and six, so the arithmetic mean is five. Waiting time for the first job is zero and for the second is four; mean waiting time is two. If the second job arrived at time three instead, its turnaround would be six minus three, or three, so the original average would no longer apply. The example assumes one CPU, no preemption, no context-switch overhead, and purely CPU-bound bursts. Draw the timeline as intervals [0,4) and [4,6). Checking the schedule visually guards against counting a completion boundary twice. The mean turnaround is a performance metric for this scenario, not a proof that FCFS satisfies fairness or interactive response objectives.

### Scheduling: worked application 2

The same jobs 4 and 2 use SJF. Find mean turnaround.

**Set up the model and conditions**

Run burst 2 first (completes at 2), then burst 4 (completes at 6).

**Carry out the calculation or proof**

With arrival zero, turnaround times are 2 and 6.

**State the result and its scope**

Mean turnaround is (2+6)/2=4 units.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

SJF selects the two-unit job before the four-unit job because both are available at time zero and burst times are assumed known. The first completion occurs at two; the second occurs at six. With zero arrivals, their turnarounds are two and six; mean turnaround is four. The improvement relative to FCFS [4,2] is one unit of mean turnaround, or twenty percent of the FCFS mean under this model. This should not be confused with a twenty-percent throughput improvement: total useful CPU work remains six units and both schedules finish the last job at time six. The benefit comes from the distribution of completion times. Include an arriving job at time three and show why nonpreemptive SJF cannot interrupt an already-running longer burst, whereas a preemptive shortest-remaining-time policy may do so. The rule and available information must be specified before comparing algorithms.

### Context Switches: worked application 3

If 1000 context switches cost 5 microseconds directly, compute total overhead.

**Set up the model and conditions**

Multiply count by per-switch overhead.

**Carry out the calculation or proof**

1000×5 μs=5000 μs=5 milliseconds.

**State the result and its scope**

The direct overhead is 5ms, excluding indirect cache effects.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Multiplying one thousand switches by five microseconds gives five thousand microseconds, or five milliseconds of direct switching overhead. If the switches happened over one second of continuous CPU availability, this would be 0.5 percent of that CPU-second; if they occurred over ten milliseconds, the fraction would be fifty percent. Therefore the raw five-millisecond total cannot alone establish CPU utilization. Context switching can also reduce cache or translation locality, effects deliberately excluded from the five-microsecond constant. Record whether the reported cost includes save/restore instructions, scheduler selection, kernel entry/exit, and cache rewarming. A check can use dimensional analysis: [switches]×[microseconds/switch] gives microseconds, never requests per second or bytes. Test the limiting case of zero switches: direct overhead should be zero, though other scheduler overhead may remain.
