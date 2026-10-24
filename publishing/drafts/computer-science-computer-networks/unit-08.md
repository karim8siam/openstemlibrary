# Unit 8 — Modern architectures

## Software-Defined Networking

**Software-Defined Networking: conceptual explanation**

Software-defined networking separates a logically centralized control process from distributed data-plane forwarding rules. It does not require a physically single controller: replication and failure recovery affect availability and consistency. A match/action rule is only useful while its installed state matches policy.

### Deep technical explanation

Software-defined networking separates, to varying degrees, decisions about forwarding policy from the act of forwarding packets. A controller can compute or distribute rules, while switches execute match/action processing on packet headers or metadata. This abstraction enables centralized policy reasoning but creates control-plane availability and consistency concerns. A device may continue forwarding with installed rules when a controller becomes unavailable, or it may fail closed, depending on the implementation. Neither behavior is universal.

Suppose a controller installs a path update across three switches. If it updates the middle switch before the edge, packets can temporarily enter a route that has not been installed end-to-end. Ordered updates, version tags, or consistent-update techniques reduce such transitions. A high-level topology diagram alone will not reveal these temporal bugs; an experiment needs to record actual update order, traffic sent during the transition, and the observed path. Controller authorization is also important: a compromised central control point can propagate harmful policy broadly.

Define what the controller is authoritative for, how it obtains topology information, and how failover works. Data-plane counters should be reconciled with intended policy. Tests should cover controller restart, delayed rule installation, link failure, packet-in floods, and bad configuration rollback. SDN is not synonymous with a particular open protocol, virtualization product, or cloud network service; it is a family of architectural choices about programmable forwarding.

### Controlled experiment and observation notebook

Deploy a three-switch virtual forwarding path with a simple controller. Install an initial path, then push new forwarding entries in the wrong order while sending timestamped probes. Observe transient black holes or loops in the controlled simulator. Repeat with a staged version tag so packets use only a coherent rule set. Restart the controller and document whether the switches keep forwarding, stop forwarding, or use fallback policy, according to the chosen software. Confirm that data-plane counters reflect the intended paths after reconnection. Include a policy-authentication check: not every process that can reach the controller should be able to push rules.

## Datacenter Networks

**Datacenter Networks: conceptual explanation**

Datacenter networks often use many equal-cost paths to connect racks and services. ECMP hashes flows across available paths, which reduces but does not eliminate hotspots. East–west service traffic, oversubscription and failure domains matter more to design than a single aggregate link-rate number.

### Deep technical explanation

Datacenter fabrics connect many servers with short paths and high aggregate traffic. A leaf-spine design provides multiple equal-cost routes between leaves through spines. The attractive symmetry does not mean all traffic receives identical throughput. A small number of very large flows can hash onto one link while parallel links remain underused, and oversubscription ratios depend on uplink and downlink capacity. Workloads also differ from wide-area browsing: east-west service calls, storage replication, distributed jobs, and microbursts can dominate.

Path diversity can improve resilience, but it complicates diagnosis. Equal-cost multipath commonly assigns a flow to one of several links based on a hash of header fields so individual packets of the same flow remain ordered. With four lanes and n independent randomly distributed flows, the expected number of unused lanes is 4(3/4)^n. This elementary occupancy model ignores unequal flow sizes and correlated hashes; it describes neither throughput fairness nor guaranteed balance. It still reveals why adding links does not ensure small flow populations will use them evenly.

Evaluate failure domains and operational cost. A single badly configured route policy can affect many racks even when the physical fabric is redundant. Observe link errors, queue occupancy, flow skew, convergence, and service latency. Separate fabric capacity from server NIC, storage, or CPU bottlenecks. Upgrade strategies should avoid simultaneous failure of redundant planes and should be tested with staged drain and rollback procedures.

### Controlled experiment and observation notebook

Model a leaf-spine fabric with four equal-cost paths and a small number of client flows. Hash flow identifiers with a documented deterministic seed and count which paths are used. Compare observed idle-path count with the independent uniform-hash expectation 4(3/4)^n, then introduce one very large flow and several small ones. Explain why the occupancy expectation does not predict bandwidth balance. Delete a spine link and measure convergence and transient congestion within the simulator. Record whether the bottleneck is a switch egress queue, a server network card, or storage. Do not assume adding equal-cost routes automatically improves latency for every flow.

## Overlays

**Overlays: conceptual explanation**

An overlay network encapsulates tenant traffic over an underlay that provides physical reachability. Overlay isolation requires correct identities and policy enforcement, not merely different virtual network identifiers. Added headers reduce effective payload MTU and can create black-hole failures if fragmentation assumptions are wrong.

### Deep technical explanation

An overlay presents a logical network atop an existing underlay. Tunnels encapsulate tenant or virtual-network packets inside transport or network headers that the physical fabric can route. This can decouple tenant address choices from physical topology and simplify workload mobility. The cost is additional encapsulation, endpoint state, MTU management, and another layer of troubleshooting. An overlay does not create physical bandwidth; every encapsulated packet still consumes capacity in the underlay.

For a 1,500-byte physical IP MTU, a tunnel adding dozens of bytes of headers reduces the safe maximum inner packet size unless the physical fabric supports a larger MTU. If endpoints assume the unmodified MTU, fragmentation or drops can appear only for large transfers, while small pings continue to work. It is therefore valuable to test payloads across a range of sizes and to check path-MTU behavior at tunnel ingress and egress. The exact overhead depends on the encapsulation and address families used.

The logical isolation of a tenant requires more than a tunnel identifier. Enforce authorization, control-plane integrity, and policies restricting which endpoints can join an overlay. Trace both the inner destination used by the workload and the outer destination used by the fabric. A packet capture on the physical wire may show only tunnel endpoints, so operators need mappings to interpret service impact. During failure analysis ask whether a fault exists in the logical route, encapsulation endpoint, or underlay path.

### Controlled experiment and observation notebook

Design a tenant overlay that adds an illustrative 50 bytes of total outer encapsulation and runs over a physical path with a 1500-byte IP MTU. Determine a conservative inner packet budget and test small and large payloads. Change the outer address family and explain that actual overhead depends on the selected encapsulation and optional fields. Capture a packet before tunnel ingress and after encapsulation and label inner versus outer addresses. Deliberately misconfigure one tunnel endpoint in a bounded lab and show how overlay reachability can fail while underlay pings work. Document tenant-policy controls separately from the tunnel identifier.

## Edge Networking

**Edge Networking: conceptual explanation**

Edge networking moves some computation or caching closer to users or devices to reduce some path latency and upstream load. Placement requires tradeoffs among consistency, resource cost and privacy. A closer geographical location does not always yield lower latency if congestion or routing policy differs.

### Deep technical explanation

Edge networking places processing, caching, or application services closer to some users to reduce particular latency components or conserve backbone traffic. "Closer" is a property of network paths and workload placement, not merely straight-line geographical distance. A nearby facility can have a poor peering route, whereas a more distant one can have an efficient direct path. The end-to-end response may be dominated by computation, cold starts, database synchronization, or authentication rather than propagation. Measure the component the edge is intended to improve.

A placement decision needs workload semantics. A read-only cache can serve nearby users efficiently if objects are fresh and invalidation is correct. A stateful transaction may need coordination with an authoritative database, so placing a front end at the edge without changing the backend may not reduce critical-path latency. Multi-region writes introduce consistency and conflict-resolution questions. An edge node may be isolated briefly from its origin and must know whether to serve stale content, reject writes, or queue an operation.

Design an experiment with matched clients in two regions and measured DNS selection, transport RTT, application compute time, cache hit ratio, and consistency violations. Compare p50 and p99 response times under cache-warm and cache-cold conditions. Record route changes and deployment versions so an apparent gain can be attributed to placement instead of a simultaneous software upgrade. Security controls and telemetry should follow the application to edge locations without silently broadening trusted access.

### Controlled experiment and observation notebook

Run an edge placement study using two client locations and a central origin. Partition end-to-end response time into DNS choice, RTT, cache lookup, computation, and origin access. Compare warm-cache and cold-cache scenarios, including stale data after an origin update. Simulate one region becoming disconnected from the authoritative database and state which operations remain safe. Present p95 and p99 response times, not just median. The toy hop-delay simulator is only one term of the budget; it cannot forecast real deployment latency without observations. Decide whether additional edge nodes meaningfully improve the actual critical path.

## Integrated Case Study and Model Limitations

### Integrated case study

A modern cloud application uses leaf-spine network paths, overlay tenant separation, programmable policy, and regional edge caching. Draw three nested views: the physical underlay connecting racks, the overlay carrying tenant addresses through tunnels, and the application dependencies spanning regions. Every overlay packet still traverses a physical link, so the configuration must account for outer headers and available MTU. An underlay path can be healthy while an overlay route is absent or points to the wrong tunnel endpoint. Conversely, a correct logical tenant mapping cannot compensate for an overloaded physical egress.

Analyze flow placement across four equal-cost lanes. If n equal and independently hashed flows choose among four lanes uniformly, the expected unused lanes is 4(3/4)^n. At n=2, that expectation is 2.25; at n=8 it is about 0.40045. The model says nothing about one huge flow among many tiny ones, so it cannot predict load balance from count alone. Run a seeded hashing experiment with explicit flow sizes and compute both active lane count and bytes per lane. Compare the results and explain why adding physical paths can improve capacity yet fail to improve a specific collision of elephant flows.

Controller failures add time-dependent behavior. A rule set may be valid after all devices update but unsafe during a staggered rollout. Simulate installing the middle switch before edge switches and identify the possible black hole. Then use staged or versioned updates and record the difference. Define the intended behavior when a controller is unreachable: continue with existing entries, use a safe fallback, or stop forwarding for selected sensitive flows. This choice should reflect application security and resilience, not convenience alone.

Finally decide which operations truly benefit from edge placement. A public static textbook page is a candidate for a cache near readers, provided invalidation is correct. A state-changing submission requiring a distant authoritative database may remain dominated by backend coordination. Compare cold versus warm caches and separate propagation RTT, cache lookup, application work, and origin database dependency. Under temporary region isolation, decide whether stale reads, rejected writes, or queued actions satisfy correctness. The evaluation criterion is measured user experience and consistent state under failure, not merely the number of advertised edge sites.

### Engineering review and field notebook

Architecture decisions in programmable, virtualized networks involve several kinds of state at once. A controller manages forwarding policy; the physical fabric carries outer packets; tunnels map logical workloads to physical endpoints; edge services hold cached or mutable application data. These systems can become inconsistent independently. A controller update may be partially installed, a tunnel map may be stale, a physical link may fail, or an edge cache may serve obsolete data. Redundancy at one layer does not automatically correct inconsistency at another. A thorough review labels the owner and recovery mechanism of each state component.

A four-lane fabric illustrates the distinction between structural capacity and actual traffic distribution. If several equal-sized independent flows hash uniformly to lanes, occupancy has an elementary probabilistic model. But enterprise workloads often contain a small number of large transfers mixed with many tiny requests; hash collision of two large flows can congest one lane despite idle capacity elsewhere. Assess bytes per lane and queue occupancy, not just the count of active links. Consider flowlet techniques or other traffic engineering only after stating reordering and implementation constraints.

An overlay adds flexibility but also hides part of the network path from application tools. A host may see an inner tenant address while underlay routers see only tunnel endpoint addresses. Without a mapping from tunnel IDs and endpoint addresses to workload ownership, troubleshooting becomes guesswork. MTU budgeting must include actual encapsulation rather than a fixed assumption copied from a different product. Test large packets as well as small packets, and verify that necessary path-MTU feedback can reach its intended endpoint.

Edge placement is a tradeoff between latency, resource duplication, and consistency. Caching a public textbook chapter near readers can improve response time if the cached version is fresh; accepting globally consistent state-changing submissions at disconnected edge sites is a different problem. Define which operations require centralized coordination. Measure how often a request actually touches the distant origin, and compare cold-cache and warm-cache latencies with correctness outcomes. A good edge deployment optimizes an observed dependency and has an explicit policy for stale data and link isolation, not merely a larger number of facilities.

### Key technical vocabulary

**SDN.** Architecture that makes forwarding behavior programmable through separately managed control logic.

**underlay.** Physical routed network carrying the outer packets of a virtualized deployment.

**overlay.** Logical connectivity mapped onto an underlying packet-carrying network.

**ECMP.** Use of multiple equal-cost forwarding next hops according to implementation rules.

**leaf-spine.** Datacenter switching design offering many relatively short paths among racks.

**tunnel endpoint.** Device that adds or removes a packet encapsulation for an overlay.

**control-plane consistency.** Agreement among installed forwarding policies and active topology state.

**edge cache.** Service retaining reusable content closer to some clients under freshness rules.

**cold-cache request.** Request for which the needed representation is not presently stored and fresh nearby.

**failure domain.** Shared dependency whose failure can affect several nominally redundant components.

## Three fully worked problems

### ECMP occupancy expectation

A datacenter fabric has four equal-cost next-hop lanes. Suppose each of eight small independent flows is hashed uniformly to one lane. Calculate the expected number of lanes receiving no flow. Then explain why this is not an expected unused bandwidth percentage when flow sizes differ.

**Define one lane as an indicator variable**

For any named lane, the probability that a single flow avoids it is 3/4. With eight independent uniformly hashed flows, the probability that this lane remains unused is (3/4)^8≈0.100113. Independence is assumed across flows, not across lane-indicator events.

**Use linearity of expectation**

The number of unused lanes is the sum of four binary indicators. By linearity of expectation, its expected value is 4×(3/4)^8≈0.400452 lanes. The formula does not require the four lane-indicator variables to be independent.

**Separate flow count from byte load**

A lane can contain one enormous flow while other lanes each contain several tiny flows. Occupancy counts only whether at least one flow uses a lane; it ignores bytes, peak rate, and queueing. Thus 0.400452 expected unused lanes is not 10 percent unused bandwidth.

**Design a better load study**

Hash a reproducible set of flow IDs, attach actual or synthetic flow sizes, and calculate bytes per lane and p99 queue occupancy. Compare before and after additional lanes or hash-policy changes. State which simulated assumptions differ from real switch behavior.

**Answer**

Expected unused lanes: 4(3/4)^8≈0.400452; not a bandwidth-utilization estimate.

### Overlay overhead and MTU budgeting

A physical IP path supports an MTU of 1,500 bytes, and a hypothetical overlay adds 50 bytes of outer encapsulation overhead to an inner packet. Estimate the largest inner IP packet that fits without fragmentation under this model. Explain which real deployment details can change the 50-byte assumption and give a falsifiable large-packet diagnostic.

**Define the accounting boundary**

The specified physical 1,500-byte IP MTU counts an outer packet including its encapsulation but excludes unspecified local link overhead. The inner packet plus 50-byte outer overhead must be no greater than 1,500 bytes.

**Compute the bound**

Maximum inner packet size is 1,500−50=1,450 bytes under the stated toy accounting model. If an application adds inner transport and network headers, the application payload must be smaller still. Do not equate the 1,450-byte inner packet budget with TCP application maximum segment size without more details.

**List variable dependencies**

IPv4 versus IPv6 outer headers, optional fields, security encapsulation, tunnel type, and underlay path MTU can alter the overhead. Some fabrics permit larger physical MTUs; others have stricter limits. A fixed 50-byte figure is an example, not the size of every tunnel.

**Diagnose path MTU failures**

Probe increasing packet sizes between known overlay endpoints in a controlled setting, inspect ICMP Packet Too Big or fragmentation-needed handling where applicable, and capture before and after tunnel ingress. Small pings working while large transfers stall can be consistent with an MTU black hole, but other explanations should still be tested.

**Answer**

Maximum modeled inner IP packet is 1,450 bytes; actual overlay headers and path MTU must be measured.

### Controller update order and edge placement

A three-switch SDN path changes its forwarding rules during a rollout, while a nearby edge cache serves some requests without reaching the central origin. Explain a plausible transient black hole from the wrong rule-installation order, how staged updates help, and why placing a state-changing application at the edge may not remove backend latency.

**Describe an inconsistent intermediate state**

If the ingress switch begins sending traffic into a new path before an intermediate or egress switch has a matching rule, those packets can be dropped. The final configuration may be correct even though the transition loses requests. The relevant variable is rule-installation timing, not only the steady-state topology.

**Coordinate the transition**

A controller can use versioned or staged updates, confirming downstream readiness before switching ingress traffic. A rollback path and bounded lifetime for old rules help prevent prolonged inconsistent state. Test the rollout with continuous low-rate probes and timestamped rule-state logs.

**Evaluate the application critical path**

An edge cache can satisfy a public read using fresh local data, reducing trips to the origin. A write requiring synchronous approval from a central authority still depends on that authority and its coordination latency. Moving only a front-end process does not eliminate the remote database transaction.

**State safe operation during isolation**

Define whether disconnected edge nodes may serve stale reads, reject writes, or queue actions for later reconciliation. Measure correctness as well as p95 latency under both warm-cache and region-disconnection scenarios.

**Answer**

Stage SDN forwarding rules to avoid transient black holes; edge placement helps only when the workload critical path becomes local.

### Case investigation: a mobile client reports that only large responses fail

Suppose a student can load short course descriptions but repeatedly fails when the browser requests a larger chapter image. The pattern alone does not prove a server bug. A path MTU problem, an incorrectly configured proxy, a stalled congestion window, a partial response implementation, or a failing CDN object can all produce superficially similar symptoms. Begin by recording which origin, host name, protocol version, and response-size thresholds correlate with the failure. Capture a harmless synthetic transfer at several known sizes and compare the results on two networks. Do not infer packet loss from an application timeout without corroborating transport evidence. For HTTP, inspect status, content length or chunk framing, range semantics, caching headers, and any content-encoding transformations. If the transfer succeeds directly from origin but fails through the cache, isolate the intermediate configuration and capture the request identifiers. If it fails only on a mobile network, examine transport and MTU behavior before changing application logic. An effective diagnosis states one hypothesis at a time, predicts a discriminating observation, and records whether that observation occurred. Successful small requests are evidence about a subset of traffic, not proof that the network path is generally healthy. 
