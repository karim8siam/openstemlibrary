# Unit 7: Reliability testing

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 7.1 Stress

### Core reasoning and definitions

Stress testing deliberately operates beyond expected limits to learn how a system degrades and recovers. Load testing usually examines behavior within a target workload, while stress testing pushes arrival rate, concurrency, memory pressure, or dependency latency until capacity or protective mechanisms become visible. A good stress experiment has a safety boundary and stops before harming shared infrastructure. Measure throughput, latency quantiles, failure modes, queues, and recovery time rather than merely counting requests sent. Open-loop load generation submits work according to an external schedule, while closed-loop clients wait for responses; the latter can conceal overload when slow responses reduce offered load. Use representative request mixes and data shapes. A small health endpoint surviving extreme traffic proves little about a complex transaction.

### Original investigative exercise

For a synthetic assignment service, raise arrival rate in steps from 40 to 100 to 160 requests per second while service capacity remains approximately 120 successful operations per second. Monitor queue growth, completed throughput, p95 latency, and rejection behavior. At 160 arrivals per second with a fixed 120 service capacity, an idealized backlog grows by 40 requests per second if all excess work queues. Define a queue bound and verify that overload shedding prevents uncontrolled memory growth. After returning to 40 per second, measure how quickly the queue drains and whether submitted assignments remain durable.

### Limits and counterexamples

A stress test run from one laptop may saturate the client or network first; the server can appear to have low capacity for the wrong reason. Report both generator-side and server-side evidence.


### Deep dive: quantitative load testing and failure domains

Reliability analysis begins with a unit of observation. Is the outcome a successful HTTP response, an authorized completed transaction, or a usable textbook page? The distinction matters under degradation. A server can return many fast errors and appear to have excellent latency while delivering almost no useful service. Before generating load, define success as an end-to-end outcome and specify which failure codes are acceptable responses under overload-control policy. Choose a duration long enough to observe steady-state behavior and transient effects, and record client-side as well as server-side timings.

Use a simple queue calculation to build intuition. Let arrival rate be lambda=160 requests per second, service capacity mu=120 requests per second, and duration t=30 seconds. If the queue starts empty, has infinite capacity, and never drops requests, backlog after the interval is t*max(0,lambda-mu)=1200 requests. If arrivals then fall to 90 per second and service remains 120, the net drain is 30 requests per second, so clearing the accumulated queue takes 40 seconds. These exact arithmetic results belong only to the idealized constant-rate model. If load causes the service rate to drop due to locking, garbage collection, or database contention, the actual queue can grow faster than predicted.

Percentiles convey behavior differently from averages. Suppose 95 of 100 requests take 100 ms, and five take 2000 ms. Their arithmetic mean is `(95*100+5*2000)/100 = 195 ms`, a value experienced by none of the requests. The 95th percentile depends on the quantile convention and may sit near the boundary between the fast and slow group. A release gate should specify how it computes percentiles, how many samples it needs, and whether it includes client/network effects. Changing the aggregation window can conceal tail spikes; recording raw histogram buckets or request samples helps retrospective diagnosis.

Availability calculations require a failure model. For three independent replicas each down 10 percent of the time, the chance that all three are down together is 0.1 cubed, or 0.001, giving 99.9 percent chance at least one is available at a randomly sampled instant. This does not mean the product has a 99.9-percent end-to-end availability guarantee. The replicas may share a power feed, database, DNS, load balancer, deployment mechanism, or faulty code. Independence fails in these common-cause events. The service also needs successful routing to the remaining replicas and consistent data if one fails. Failure-domain testing should deliberately remove a shared dependency and check whether the redundancy model's assumptions actually hold.

Fault injection needs containment. In a staging environment, terminate a selected worker, throttle a network link, or return controlled dependency errors while synthetic traffic is running. Declare safeguards such as test-tenant isolation, a maximum experiment duration, rollback instructions, and monitoring for runaway retries. Measure not only whether the service remains available but whether side effects are duplicated or lost. A payment write retried after an ambiguous timeout may create two transfers if idempotency is missing; that is a correctness defect even when the service's HTTP success rate is high.

Concurrency faults differ from capacity faults. A slow query under load can cause a bottleneck; a lost update can silently corrupt state even at low load. Use barriers to force a precise interleaving between two progress-save operations or reservations. Compare final committed state with the declared conflict-resolution policy. Random stress tests may be helpful for discovering unexpected schedules, but a deterministic reproduction is essential for verifying a fix. Also test data recovery after the experiment: records should remain consistent, abandoned leases should expire according to contract, and any queued work should eventually be accounted for.

Write the final report as evidence rather than a marketing figure: offered arrival rate, achieved throughput, percentile conventions, errors by category, observed queue depths, resource saturation, fault onset and end, recovery interval, and untested failure domains. A successful exercise under one region's synthetic traffic does not prove global reliability, but its scoped results can guide a concrete architectural decision.


### Unit synthesis: workload measurements and fault reasoning

Quantitative reliability claims require a workload and a failure model. A server that can complete 120 requests per second does not necessarily handle arrivals of 160 per second: an ideal queue accumulates 1,200 requests in thirty seconds, assuming unlimited buffering and unchanged capacity. A service with three independent replicas and ten-percent individual unavailability has 99.9-percent modeled instantaneous availability, but a shared regional outage breaks independence. A system can also be available by transport metrics while corrupting concurrent writes. Students should produce three reports: a load test with actual offered and achieved throughput, a fault-injection observation with recovery behavior, and a deterministic state-consistency test with barriers creating a conflicting interleaving. Compare each observed result against a specific model and document where simplifying assumptions cease to apply. Reliability is not one percentage that substitutes for correctness, security and accessibility.

## 7.2 Fault Injection

### Core reasoning and definitions

Fault injection deliberately causes controlled failures to determine whether recovery assumptions hold. Failures can occur before an operation, midway through a transaction, after commit but before acknowledgement, or while a dependent service is unavailable. Inject packet loss, delay, process termination, database disconnect, stale cache data, and disk errors only in isolated or explicitly authorized environments. The experiment should state the expected invariant, trigger, affected component, and cleanup. Reliability engineering distinguishes fault tolerance from fault masking: hiding an error without confirming correctness can make the system less trustworthy. Chaos experiments require blast-radius controls, a rollback plan, and useful telemetry. Start with a hypothesis about resilience rather than randomly killing processes.

### Original investigative exercise

In a certificate-generation workflow, simulate a worker crash after writing an output object but before acknowledging a queue message. On redelivery, an idempotent consumer should detect the existing artifact and avoid issuing a duplicate certificate version. Repeat with a crash before writing and after publishing completion status. Track job identifiers, storage keys, and durable database state after recovery. Test the boundary where the retry budget is exceeded; the job should enter an inspectable failure state instead of disappearing. Record restoration of normal processing and cleanup of orphan artifacts.

### Limits and counterexamples

Killing random processes during a demo may make an impressive dashboard but provides little evidence if the expected durable state and failure timing are not recorded. Never run destructive tests against live user data without permission.


### Applied laboratory: testing resilience of a high-load reading platform

A textbook portal experiences a sudden increase in traffic near an examination deadline. A load test should not start by firing the maximum possible number of requests; it should start with a service-level question. Suppose the product promises that 95 percent of chapter reads complete within 400 milliseconds under a specified population of active readers and a declared region. Define the measurement boundary: browser navigation timing includes network and rendering, while API processing latency does not. If a cache serves 90 percent of reads, report cache hits and misses separately. A single average latency hides the long tail that students experience when an origin server is overloaded.

Create a reproducible workload mix. For example, 70 percent of requests read popular chapters, 20 percent search the catalog, and 10 percent submit a saved reading position. Use synthetic accounts and generated content; avoid submitting real student tokens to a load generator. Add a warmup stage so caches and runtime compilation stabilize. Ramp arrival rate gradually while measuring throughput, the distribution of response times, queue depth, CPU saturation, memory, and error codes. Record the offered arrival rate as well as completed requests. If the generator cannot sustain the offered load, apparent stability may mean the load tool is saturated rather than the service healthy. Test from more than one generator node if needed, with synchronized timestamps and documented network conditions.

Use a simple queue model as a teaching aid. With a service capacity of 120 requests per second and arrivals of 160 per second for 30 seconds, idealized backlog grows by `(160-120)*30=1200` requests. This calculation assumes a fixed service rate, no request dropping, no finite queue cap, and no feedback from latency to arrivals. Real systems may shed load, scale horizontally, throttle clients, or experience a declining service rate from contention. Therefore the simulator should label its assumptions and avoid presenting backlog as an exact forecast of production. Complement it with measurements of actual queue depth and rejection behavior under the chosen overload-control policy.

Reliability experiments should include recovery, not merely fault creation. Terminate a worker during a save-position transaction. If the operation already committed, a retry should not duplicate a user event; if not, the system should eventually expose a consistent result. Disconnect a downstream analytics service and check that core reading remains available when analytics is designed to fail open. Deliberately corrupt one cache entry and measure whether validation or revalidation prevents a broken textbook page from persisting. For each fault state the expected degraded mode: read-only operation, explicit temporary failure, retryable request, or hidden optional feature. A suite that reports "passed" simply because the site returned some page is insufficient.

Test concurrent reads and writes to a shared progress record. Two tabs may save positions at different timestamps. A last-write-wins policy can move the reader backwards if an old delayed update arrives late. Specify whether the business rule chooses maximum progress, latest user action by server sequence, or independent per-device cursors. Capture the order of logical operations, the request identifiers, and final persisted state. Use barriers to create the conflict rather than hoping random load will. If a property depends on serializability, inspect database isolation and transaction boundaries. A stress test can expose this race, but the deterministic conflict test explains it.

After injecting faults, return the system to a clean state and verify recovery time. Report the fraction of successful reads, observed latency percentiles, error budget consumed, and duration until normal service resumes. Avoid extrapolating an artificial lab's uptime to a yearly availability guarantee. The laboratory should teach that performance, correctness, and resilience are interrelated but distinct claims, each requiring its own workload model, observable output, and limiting assumptions.


## 7.3 Concurrency Testing

### Core reasoning and definitions

Concurrency testing targets defects arising from interleavings among independently scheduled operations. Ordinary tests can miss races because the machine repeatedly chooses the same timing. Data races involve unsynchronized conflicting accesses to shared memory; higher-level logical races may occur even when each database operation is individually thread-safe. Deadlocks require circular waiting patterns, while livelocks involve continued activity without useful progress. Deterministic schedulers, explicit synchronization barriers, systematic concurrency testing, and state-model exploration improve reproducibility. Thread sanitizers and database transaction tests answer different questions: the first examines certain memory-access patterns, while the latter explores isolation and atomicity at a storage boundary. A passing stress loop is evidence, but not proof, that every schedule is safe.

### Original investigative exercise

Start with a shared counter increment implemented as read-modify-write. Two workers may both read zero and both write one, losing an update. Synchronize them after the reads to reproduce the defect, then protect the operation with an atomic primitive or appropriate lock. Record the expected final value two. Extend the experiment to a bank transfer with a database transaction; check conservation of total balances under concurrent opposite transfers. Add cancellation and timeouts to look for leaked locks. Keep a minimal interleaving trace so that the fix can be regression-tested deterministically.

### Limits and counterexamples

A test that waits for two tasks to finish but never forces overlap may always execute serially. Its green result is not evidence that a race is impossible.

### How to interpret the interactive model: queue overload

The queue model assumes capacity 120 requests per second, a fixed thirty-second measurement window, no discarded requests and an unbounded queue. If arrivals are 160 per second, backlog increases by (160-120)*30 = 1,200. When arrivals are ninety per second, the service could drain an existing backlog at thirty per second if its service capacity remained unchanged, although the simulator reports that rate without modeling initial backlog. Real networks and servers may shed load, time out clients, scale capacity, or slow under contention. A queue can therefore fail differently from the idealized line. Test observed throughput, tail latency, queue depth and recovery while documenting generator limits. Avoid treating the model as proof that an actual Cloudflare site will handle a specified visitor count.

## 7.4 Performance Regression

### Core reasoning and definitions

Performance regression testing compares quantitative behavior across versions under controlled workloads. A meaningful comparison pins hardware or a repeatable environment, workload mix, data volume, cache state, dependency behavior, and instrumentation. Means can hide slow tails; p95 or p99 latency, allocation volume, throughput, and error rate provide complementary evidence. Variability from CPU frequency scaling, background activity, network jitter, and garbage collection can dominate small observed differences. Use repeated measurements and confidence intervals where appropriate rather than declaring a regression from one run. Choose budgets that reflect user experience, and account for correctness: a fast service that skips validation is not an improvement.

### Original investigative exercise

Benchmark a JSON validation endpoint with 10,000 synthetic records at two versions. Warm both versions consistently, collect several independent batches, and compare medians and tail latencies. Also verify every version returns the same expected validation errors; optimization that silently drops malformed rows is a correctness regression. If the baseline p95 is 180 ms and a candidate p95 is 270 ms under matched conditions, the observed increase is 50 percent; investigate CPU, allocation, database calls, and cache misses before assigning cause. Archive raw timings and environment metadata for reproducibility.

### Limits and counterexamples

Performance tests against an empty database can hide the cost of indexes, joins, and realistic contention. A single impressive throughput number without workload details is not an actionable guarantee.

### How to interpret the interactive model: redundant availability

This model assumes three statistically independent replicas, each unavailable with probability p. The probability all three fail is p cubed, so the probability at least one is available equals one minus p cubed. At p=10 percent, that yields 99.9 percent instantaneous modeled availability. The computation is straightforward; the assumption is the hard part. Replicas often share a datastore, deployment image, region, credentials or network path. A shared outage can take down every replica even if individual hardware failures are rare. Availability also requires correct routing, valid response data and acceptable latency. Students should compare independent-failure arithmetic with a scenario involving one common-cause failure and report why the simple formula may be optimistic.

## Fully worked questions

### Worked problem 7.1: Stress

A server processes 120 requests per second; for 30 seconds, new requests arrive at 160 per second. Under an idealized fixed-rate queue with no drops, compute backlog growth.

**Define the property and assumptions.** Assume arrival and service rates are constant, the queue has unlimited capacity, and every arrival must wait if capacity is exhausted. Net excess demand is max(0,160-120)=40 requests per second.

**Compute or execute the reasoning.** Over 30 seconds the backlog increases by 40*30=1200 requests. If the arrival rate falls to 90 requests per second afterward and service remains 120, backlog drains at 30 requests per second, so it would take 1200/30=40 seconds to clear the accumulated requests in this simplified model.

**Interpret the conclusion and limitations.** A real system may have finite queues, timeouts, load shedding, autoscaling, caching and service-rate degradation. Confirm latency and loss characteristics from measurement; do not treat the closed-form queue as a forecast of production behavior.

### Worked problem 7.2: Fault Injection

A service uses three statistically independent replicas, each with a 10 percent chance of being unavailable at a randomly selected instant. What is the probability that at least one replica is available?

**Define the property and assumptions.** The event of total unavailability requires all three replicas to fail simultaneously. Under the stated independence assumption, multiply their three unavailability probabilities: 0.10*0.10*0.10.

**Compute or execute the reasoning.** The chance all three are unavailable is 0.001 = 0.1 percent, so the chance at least one is available is 1-0.001=0.999 or 99.9 percent. This is instantaneous modeled availability, not a measured service-level objective over a year.

**Interpret the conclusion and limitations.** Real failures are often correlated through shared power, network, software deployments or control planes. The independence assumption must be supported or replaced by a failure-domain model. Passing this arithmetic test does not demonstrate graceful failover or correct data consistency.

### Worked problem 7.3: Concurrency Testing

Two tabs save reading progress at offsets 40 and 55, but the network delivers the older action last. Derive the final state under two different conflict-resolution policies.

**Define the property and assumptions.** Under last-arrival-wins, the server applies progress 55 and then 40, so the stored value becomes 40 despite the user's newer progress. Under monotonic-max, the server stores max(existing, incoming), so 55 remains after either order of delivery.

**Compute or execute the reasoning.** The two policies are not interchangeable: monotonic-max can be wrong if the user intentionally restarts a book and expects a reset to zero. A server-sequenced user action policy could preserve the latest intentional action, but it needs an ordering identifier rather than relying on packet arrival time.

**Interpret the conclusion and limitations.** Design an integration test using barriers to reverse completion order and assert the chosen contract. Log the action identifiers and persisted state without assuming that a UI slider alone reveals the write conflict. A fast stress run cannot reliably substitute for a deterministic interleaving.

