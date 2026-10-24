# Unit 7 — Network operations

## Measurement

**Measurement: conceptual explanation**

Network measurement begins with an observable quantity: throughput, latency, loss, jitter, utilization or error counts. Packet captures show traffic at a particular point, not omniscient truth about an entire path. Sampling and clock accuracy matter when inferring round-trip time from timestamps.

### Deep technical explanation

A network measurement is meaningful only if its observation point and definition are known. One-way propagation delay differs from round-trip time, and an application request's wall-clock latency can include DNS, transport setup, server queuing, application work, and retransmissions. Link utilization is a ratio of carried bits to nominal capacity, not a direct measure of user experience. Packet loss may be inferred from transport behavior but a capture on one endpoint can be affected by hardware offload and capture drops. Report how metrics were collected before interpreting them.

A baseline captures normal variability. Measure distributions such as median, 95th percentile, and 99th percentile rather than only averages. A service with 10-ms typical latency and occasional 2-second pauses can have a respectable mean but poor interactive performance. Align clocks if comparing logs across devices; millisecond-level timing claims are invalid if host clocks differ by seconds. Separate active probes that create measurement traffic from passive observations of existing traffic. Probes can be deprioritized by routers or treated differently by firewalls.

A useful performance budget can assign latency to stages. Record a trace ID, timestamp, hop or interface, payload size, and response category at each stage where possible. Use confidence intervals or repeat measurements under controlled load to decide whether a change is real. The purpose of measurement is not to produce the highest possible number but to discriminate between competing explanations of a user-visible failure.

### Controlled experiment and observation notebook

Record a trace spanning client, proxy, application, and database for a single request, with synchronized timestamps if possible. Estimate contributions of DNS, connection setup, queue delay, application compute, and network propagation. Compute p50, p95, and p99 from repeated measurements, explaining the sample-size uncertainty. Next compare one-way and round-trip probe results without treating them as equal. Introduce offload in a test capture and examine whether apparent huge packets are artifacts of the observation point. Document the exact device and tool version used for each metric so another student can reproduce the result.

## Troubleshooting

**Troubleshooting: conceptual explanation**

Troubleshooting works best as a sequence of falsifiable tests: local interface, address assignment, local gateway, name resolution, remote endpoint and application behavior. A successful ping does not prove that HTTPS works, while failed ICMP may reflect filtering rather than lack of connectivity.

### Deep technical explanation

Troubleshooting is a sequence of falsifiable hypotheses. Start with the symptom and a precise scope: which users, sites, protocols, and times are affected? Establish whether the failure is at the physical link, local addressing, name resolution, route selection, transport negotiation, security policy, or application. A simple decision tree can reduce unnecessary changes. For example, if the default gateway responds but a named service does not, test the resolved address and port separately before treating DNS as the root cause.

Use changes to evidence, not just to configuration. A failed request from one client may be caused by a browser proxy, an expired local certificate store, or a local firewall while all network switches are healthy. Conversely, many clients in one VLAN failing simultaneously suggests shared infrastructure. A route table snapshot, ARP or neighbor entry, interface counter, packet trace, and server log each covers a different failure stage. No single tool reveals the whole path. ICMP filtering can make a traceroute look broken even when application traffic is forwarding normally.

During a live incident, record what was changed and when. Applying three fixes at once makes the cause impossible to infer. Use a reversible change with a success metric, ideally in staging first. After recovery, write a concise timeline, actual trigger, detection gap, and preventive action. A post-incident analysis should separate the initiating event from architectural conditions that amplified its impact.

### Controlled experiment and observation notebook

Create a lab fault tree for “browser cannot load the page.” First resolve the name, then test the intended address, TCP or QUIC reachability, TLS negotiation, and HTTP status. Introduce one controlled fault at a time: wrong DNS answer, missing default gateway, blocked server port, or expired certificate. Record which observation falsifies which hypothesis. Show why a missing traceroute hop can be caused by control-message filtering rather than failed application forwarding. Finish with a reversible change plan: evidence to collect, expected improvement, rollback condition, and post-incident timeline.

## Traffic Analysis

**Traffic Analysis: conceptual explanation**

Traffic analysis inspects protocol mix, flow sizes and temporal variation. Mean bandwidth alone can hide short bursts that overflow buffers. When sampling packet traces, record capture location, snap length and packet loss; otherwise absence of packets may reflect measurement failure.

### Deep technical explanation

Traffic analysis characterizes who is communicating, over which transport, at what rate, and with which timing patterns. A five-tuple flow view is useful but imperfect: encryption obscures higher-layer content, tunnels can conceal inner endpoints, and address translation can merge many clients behind one public IP. Packet sampling reduces collection overhead but may miss small short-lived flows. Flow records provide aggregate counters without requiring payload inspection, improving privacy in many operational contexts.

Burstiness matters because equal average bit rates can place very different demand on buffers. A 10-Mbit/s mean produced by a smooth sender can be easier to serve than repeated bursts at 100 Mbit/s separated by idle periods. A bottleneck queue sees the instantaneous arrival and service processes, not only the long-term mean. Microbursts may cause drops even when a one-minute utilization graph shows spare capacity. Capture resolution, counter polling intervals, and NIC telemetry determine what short events can be detected.

Before diagnosing an elephant flow as malicious, check scheduled backups, software updates, and data synchronization. Compare source/destination distribution, protocol mix, flow duration, retransmission fraction, and application deadlines. Minimize packet payload retention and apply an approved retention policy because raw traffic may include credentials or personal data. A useful diagnosis prioritizes repeatable observations and avoids making claims about users' intent from a few header fields.

### Controlled experiment and observation notebook

Construct two traffic sources with identical average offered rate but different temporal burst shapes. Feed them to a queue with finite buffers and record short-term occupancy, drops, and end-to-end latency. Compare a 1-second rate counter with a 60-second counter to expose microbursts that disappear in coarse aggregation. Classify flows by duration and byte count without collecting payload content. Add one large scheduled backup flow and explain why its volume does not alone prove malicious activity. Evaluate privacy risks of retaining flow metadata, particularly when many users share the same public address.

## Quality Of Service

**Quality Of Service: conceptual explanation**

Quality of service allocates resources among competing classes through marking, shaping, policing and scheduling. Priority queues can improve delay for one class while starving another under sustained overload. QoS cannot create missing physical capacity, and service targets must include explicit load assumptions.

### Deep technical explanation

Quality of service is the management of contention when traffic demands exceed available service at some moment. Classification places traffic into classes; marking carries policy signals; scheduling decides which queued packet transmits next; policing limits offered traffic; shaping delays traffic to smooth bursts. These are different tools. Priority scheduling can protect small interactive packets but can starve lower classes if unlimited traffic receives the highest priority. Weighted fair queuing seeks a more deliberate division of capacity among classes.

An application should be classified by its observable needs rather than its marketing label. A voice call values low delay and modest loss, whereas a large backup can often tolerate additional latency but needs sustained throughput. Misclassifying a high-volume backup as real-time traffic makes prioritization ineffective. End-to-end markings might be rewritten or ignored across providers. A local priority class cannot force an upstream Internet bottleneck to honor the same policy.

To validate QoS, run a controlled mixed workload with interactive probes and bulk transfers. Record delay percentiles, jitter, throughput, and drop rates before and after policy under the same offered load. Check the location of the actual bottleneck; shaping after a congested upstream link cannot undo already-lost packets. Protect control and management traffic without making a universal claim that priority removes congestion. A good design documents which service loses resources first during overload.

### Controlled experiment and observation notebook

Generate a mixed workload containing delay-sensitive voice packets and a large background transfer. Configure a hypothetical strict-priority queue, measure the voice delay, and check whether the background transfer starves. Replace strict priority with a bounded or weighted scheduler and compare both classes. Apply shaping at the local egress and then move the bottleneck upstream; demonstrate why local scheduling cannot undo upstream drops. Record what happens if all traffic is mistakenly marked high priority. Define an acceptance criterion using delay percentiles and minimum throughput, not a vague claim that every application has improved.

## Integrated Case Study and Model Limitations

### Integrated case study

An online classroom has complaints of sporadic delay. Operators see 30 percent average utilization on a link and initially rule out congestion. That conclusion is premature: a minute-average graph cannot reveal a hundred-millisecond microburst that overflows a shallow buffer. Build a test with a background file transfer and short interactive probes. Record a timestamped event log, interface drops, queue occupancy where supported, retransmissions, p50 and p99 RTT, server CPU time, and application request identifiers. Describe collection points: sender, bottleneck router, proxy, and receiving application. Clock synchronization is essential for a reliable cross-device timeline.

Introduce a simplified M/M/1 model with 20 jobs/s service capacity. At 10 arrivals/s, utilization is 0.5 and the expected jobs in the system is one; at 16 arrivals/s, utilization is 0.8 and the expected jobs rises to four. Mean queue waiting time rises correspondingly. These values are valid only under the Poisson-arrival, exponential-service, and steady-state assumptions. Real networks can be self-similar or bursty and may have multiple service disciplines. Use the model to build intuition, then use actual queue measurements to judge the real incident. A sustained 80 percent utilization is not intrinsically safe or unsafe without a latency and workload specification.

Run a controlled QoS comparison. Give voice-like probes a modest high-priority class and bulk transfer a lower class. Under moderate load, both may succeed without any visible benefit from prioritization. Under overload, scheduling may reduce voice tail latency while limiting bulk throughput. If all packets are classified as high priority, the mechanism no longer distinguishes applications. Strict priority can starve lower queues; weighted schemes involve explicit minimum shares. Local marking might not survive an Internet provider's domain, so record precisely where the policy operates.

Finish with a scientific incident report. State the user symptom and measurement window, list competing hypotheses, show evidence supporting or rejecting each, and identify the smallest reversible intervention. Possible remedies include pacing a batch sender, resizing a buffer with a latency budget, fixing a server hot path, changing a physical link, or updating classification. The selected remedy should match the diagnosed bottleneck. After the fix, repeat the same workload with the same metrics and report any remaining uncertainty. This prevents an attractive but unsupported fix from becoming the official explanation.

### Engineering review and field notebook

Operations work should combine measurement with controlled change. A useful problem statement has a user-visible symptom, a defined affected population, a time window, and a success criterion. "The network is slow" lacks all four. "Students in one building see p99 page latency above two seconds during a scheduled backup between 10:00 and 10:30" provides a more testable starting point. The operator can then compare link utilization at a suitable time scale, drops, retransmission, application queue delay, and server work. A high average latency alone cannot identify where the problem originates.

Every metric has an observation cost. Very frequent high-fidelity packet capture may consume disk, CPU, and sensitive payload storage; very coarse counters may hide the incident. Select the least intrusive measurement with adequate temporal resolution. A 60-second utilization graph can miss a 100-millisecond egress burst. A packet trace may show transport retransmissions without revealing whether loss occurred on the wireless hop, the provider network, or the capture interface itself. Identify alternative explanations explicitly and collect discriminating evidence before acting.

Performance mathematics should be taught as conditional reasoning. M/M/1 queue formulas can demonstrate the rapid growth of expected delay as arrival rate approaches service rate, but they assume Poisson arrivals, exponential service times, and steady state. If students try to model a finite bursty buffer with this stationary queue and obtain an implausibly smooth result, the error is not a reason to abandon mathematics; it is a signal that the model's premises do not describe the observed workload. Choose a model appropriate to the question and then validate it against measurements.

After intervention, compare the same workload. If the fix is traffic shaping, do not celebrate improved voice p95 while ignoring backup starvation. If the fix is a bigger switch buffer, check whether tail latency grew. If the fix is a new DNS resolver, check whether the original application failure was in fact DNS-related. A reliable incident report gives the chosen change, measurement before and after, risks of the intervention, rollback condition, and untested alternatives. It treats technical uncertainty as part of operations, not as an embarrassment to hide.

Capacity planning must distinguish an average demand estimate from a service-level objective. Suppose an online exam system handles many small requests at the beginning of an exam, followed by quieter reading and a second wave of submission events. The minute-mean request rate might appear comfortably below a server's nominal capacity, yet the initial arrivals can create a long queue precisely when users need immediate feedback. Design a workload generator with a realistic time profile: ramp, short burst, steady phase, and recovery. Report per-phase arrival rates, response time percentiles, queue length where observed, and errors. Synthetic tests must be rate-limited and confined to infrastructure you control. If the generator itself becomes CPU limited, its numbers cannot be interpreted as a server capacity result.

Error budgets connect measurements to action. A service might require that at least 99 percent of interactions complete within one second for a defined set of clients and test intervals. Averages alone cannot evaluate that threshold. Mark every failed or missing response consistently instead of deleting timeouts from the sample: removing failures can make p99 artificially flattering. Define whether client-side network failures, application validation rejections, and user cancellations belong in the objective. Comparing two releases also requires matched endpoints, approximate load mix, deployment region, and enough observations to limit sampling noise. Without that control, the new release's apparent improvement could be the consequence of a quiet hour rather than a software change.

The protocol stack provides a useful incident narrative. A request can incur DNS delay, TLS setup delay, router queueing, application processing, and database waiting. If only total time is captured, optimization teams may argue about ownership without evidence. A distributed trace with correctly correlated clocks can allocate measured spans, but asynchronous work and shared-resource contention complicate interpretation. Distinguish elapsed wall-clock critical path from the sum of overlapping component spans; adding concurrent spans can produce a number larger than the user's actual response time. Finish with a correction report that names the dominant observed component, the competing explanations, the chosen reversible intervention, and the precise condition under which rollback should occur.

### Key technical vocabulary

**p99 latency.** Value at or below which roughly ninety-nine percent of the sampled latencies fall.

**jitter.** Variation in packet delay or interarrival spacing under a defined measurement.

**utilization.** Fraction of a service resource consumed during a stated interval.

**M/M/1.** A single-server queue model with memoryless interarrival and service-time assumptions.

**tail latency.** Behavior of unusually slow requests, typically evaluated with upper percentiles.

**QoS classification.** Assignment of traffic to policy classes based on observable attributes.

**traffic shaping.** Buffering or pacing output to meet a defined transmission rate profile.

**policing.** Enforcement of a traffic rate or burst allowance, sometimes by dropping or marking.

**queue discipline.** Rule choosing which waiting packet or job is served next.

**fault tree.** Structure connecting a symptom to testable possible causes and discriminating checks.

## Three fully worked problems

### Queue behavior near service capacity

A simple M/M/1 classroom queue serves 20 jobs per second, with Poisson arrival and exponential service times. Compute the stationary expected number of jobs in the system and the mean waiting time before service for arrivals of 10 and 16 jobs per second. State when this model becomes invalid.

**Check stability and utilization**

For a stationary M/M/1 model, arrival rate lambda must be less than service rate mu. With mu=20 jobs/s, lambda=10 gives rho=0.5 and lambda=16 gives rho=0.8. Both are under the stability condition. At lambda≥20, the stationary finite-mean formulas no longer apply.

**Compute expected number in system**

The M/M/1 expected system population is L=lambda/(mu−lambda). At lambda=10, L=10/10=1 job. At lambda=16, L=16/4=4 jobs. This includes jobs waiting plus any in service; do not confuse it with Lq, the queue-only mean.

**Compute waiting before service**

The expected queue wait is Wq=lambda/[mu(mu−lambda)]. For lambda=10, Wq=10/(20×10)=0.05 s or 50 ms. For lambda=16, Wq=16/(20×4)=0.20 s or 200 ms. The mean time including service would be larger by 1/mu=50 ms.

**State the correct interpretation**

The strong rise as utilization approaches one is an insight of this assumed model. Real traffic burstiness, priorities, finite buffers, multicore service, and changing workload can invalidate the stationary M/M/1 prediction. Use measured latency distributions for decisions about actual networks.

**Answer**

At 10/s: L=1, Wq=50 ms; at 16/s: L=4, Wq=200 ms.

### A reproducible network incident fault tree

Students report that a web application is unreachable. A resolver returns the expected IP address; a TCP connection to port 443 succeeds; the TLS handshake fails because the certificate name does not match the requested hostname. Explain which hypotheses are weakened by these observations, what the next action should be, and why disabling certificate verification is an unsound production fix.

**Bound evidence from DNS**

The resolver supplied an answer for the requested name, reducing the likelihood of a simple missing-record problem from that vantage point. It does not prove every resolver has the same answer, or that the resulting address is the intended host under every security policy.

**Interpret transport reachability**

The successful TCP connection shows that a path permitted a TCP handshake to the chosen endpoint and port. It does not prove that the endpoint provides the correct secure application, that authorization will succeed, or that user-visible content exists.

**Locate the identified failure**

A hostname mismatch is a TLS identity-validation failure. Investigate the server certificate's authorized names, requested hostname, SNI and proxy configuration. Correct the name or certificate deployment through an approved workflow, then validate with the same affected client.

**Protect the trust guarantee**

Disabling certificate verification removes a key defense against impersonation and interception. It masks the symptom without establishing the true intended peer. Document the final certificate chain and hostname match as part of verification.

**Answer**

Diagnose a TLS hostname identity mismatch; fix endpoint naming or certificate configuration, not client verification.

### QoS classification under overload

A router carries latency-sensitive voice packets and bulk backup traffic on a saturated egress. An operator puts every packet into the highest priority class and announces that QoS has been enabled. Explain why this cannot provide differentiation, propose a bounded alternative policy, and define measurements needed to evaluate a claimed voice improvement.

**Explain the logical error**

Priority queuing matters only if traffic classes differ. If every packet is marked highest priority, the scheduler has no lower class from which to take service and cannot protect voice against bulk within that single class. This is a classification failure, not necessarily a scheduler implementation bug.

**Define class and fairness constraints**

Classify voice using an approved signal or application identity that cannot be spoofed casually. Give the latency-sensitive class a bounded share or cap so background traffic is not indefinitely starved. Assign backup traffic a lower scheduling weight or a shaped rate consistent with capacity.

**Measure both user experience and collateral effects**

Record voice packet delay variation, p95 or p99 latency, loss, backup throughput, link queue occupancy, and dropped packets before and after under matched offered load. A voice benefit with complete starvation of necessary backups may violate the service objectives.

**Check the bottleneck location**

The configured router must actually be the congested egress where packet scheduling influences order. Markings may be ignored beyond the organization's domain, and local QoS cannot reverse losses that occurred before packets reached the queue.

**Answer**

Putting everything in the same top class provides no prioritization; classify carefully and measure all classes under matched overload.