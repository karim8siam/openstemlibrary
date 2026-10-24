# Unit 3 — Internet routing

## Addressing

**Addressing: conceptual explanation**

An IP address identifies an interface within a routed addressing system. IPv4 subnet prefixes partition an address space; the same host can have multiple interfaces and addresses. Private-address ranges and network address translation are deployment conventions, not changes to IP routing fundamentals.

### Deep technical explanation

IP addressing is a forwarding abstraction distinct from human names and link addresses. An IPv4 address has 32 bits, and an IPv6 address has 128 bits. A prefix denotes a set of addresses sharing leading bits; the prefix length controls how many bits are fixed. Routing frequently aggregates adjacent networks into a single prefix to reduce table size, but aggregation is only valid when forwarding for the whole aggregate leads to the correct next hop or a deliberate covering route. An address assigned to a host does not by itself create a route back from every network on the Internet.

Private IPv4 ranges can be used behind translation devices, but private addresses are not globally routed across the public Internet. Network Address Translation rewrites endpoint information and can complicate inbound connections, protocols carrying addresses inside messages, and logging of users behind shared public addresses. IPv6 provides a much larger address space but does not make firewall policy or privacy considerations disappear. Addresses can be link-local, global, multicast, or otherwise scoped; a link-local destination generally cannot be sent across ordinary routers as though it were global.

For a diagnostic trace, record the source and destination IP addresses at each vantage point and distinguish them from the Ethernet addresses. Ask whether the endpoint selected the correct source address and gateway, whether a route exists, and whether a reply can return. A successful ping to a gateway rules out some local faults but cannot prove that a remote service, its transport port, or its application policy will accept traffic.

### Controlled experiment and observation notebook

Take a host configured with address 192.0.2.40/24 and gateway 192.0.2.1. Explain what can be reached through local neighbor resolution and what is sent to the gateway. Add a second interface and a more specific static route, then predict the source address and egress interface used for two destinations. Repeat with an IPv6 link-local peer and explain the interface scope requirement. Document why these documentation-only example ranges should never be treated as evidence of global public reachability. Finally introduce a NAT boundary and compare packet fields visible from inside and outside it.

## Subnetting

**Subnetting: conceptual explanation**

Subnetting converts a prefix length into a set of addresses sharing high-order bits. A /26 IPv4 network contains 64 addresses, although traditional host counts subtract network and directed-broadcast addresses; special /31 and /32 uses require separate treatment. Always state whether the question concerns block size or conventional host addresses.

### Deep technical explanation

A subnet is defined by a prefix and associated address set, not by an arbitrary label such as "office network". For an ordinary IPv4 /26, there are 2^(32-26)=64 addresses. Historically common host assignment reserves one network address and one directed broadcast address, leaving 62 conventional host addresses. That convention does not apply unchanged to /31 point-to-point links or /32 single-host routes. Modern designs should explicitly state their use case before applying a memorized subtract-two formula.

Suppose a /24 allocation must serve departments needing 100, 50, and 20 address slots. Variable-length subnetting could allocate a /25 with 128 total addresses, a /26 with 64, and a /27 with 32. An engineer must also account for growth, gateways, reserved IP addresses, routing boundaries, and any platform-specific constraints. The placement of the blocks should respect binary alignment: a /26 network starts at an address whose last octet is a multiple of 64 within its /24. A visually tidy scheme that ignores alignment will not match real prefix membership.

Subnet masks are not an access-control policy. Hosts on different IP prefixes can communicate through a router if routes and filters permit it. Conversely, two hosts nominally configured on the same subnet may fail to talk if a Layer-2 VLAN separates them. Check DHCP scope, host mask, gateway setting, and route tables as a set. A subnetting exercise is complete only when both address arithmetic and the intended packet path are correct.

### Controlled experiment and observation notebook

Design an address plan for four isolated groups requiring 100, 50, 20, and 10 conventional IPv4 hosts. Begin with a /24 allocation, place each variable-length block on a proper alignment boundary, and list usable ranges and broadcast addresses. Verify every pair of allocations is disjoint using bitwise masks, not just visual inspection. Include a point-to-point interface and explain why the ordinary host-count shortcut is not universal there. Discuss operational tradeoffs: space reserved for growth, simplicity of summarization, fragmentation of free blocks, and the risk of treating IP subnet boundaries as if they automatically enforced access policy.

## Forwarding

**Forwarding: conceptual explanation**

A router chooses a next hop from its forwarding information base, typically using longest-prefix matching. If 192.0.2.0/24 and 192.0.2.128/25 both match a destination, the /25 entry wins. Forwarding is per-packet application of installed rules; routing is the separate process that produces those rules.

### Deep technical explanation

A router selects a next hop for each packet using its forwarding information base. The usual IP rule is longest-prefix match: among matching routes, prefer the entry with the greatest prefix length. If 203.0.113.0/24 and 203.0.113.128/25 both exist, an address ending in 140 matches both, so the /25 route wins. The administrative reason a route entered the table and the forwarding lookup used for a packet are related but distinct steps. Control-plane processes produce routes; forwarding hardware or software applies the chosen entries at line rate.

The router normally decrements the IPv4 Time to Live or IPv6 Hop Limit. This prevents indefinite circulation during routing loops. If the value would reach zero, the router drops the packet, often generating a control message rather than forwarding it. The router may also handle MTU limits, encapsulations, policy routing, and quality-of-service markings. A firewall rule can discard a packet even when the route table says there is a next hop. Therefore "route present" does not mean "packet delivered".

A forward-path investigation should gather a timestamped set of route entries, prefix matches, interface state, ARP or neighbor cache, and policy counters. Route changes during the incident can invalidate an after-the-fact snapshot. For asymmetric paths, the return direction may use different routers and fail for different reasons. Tools such as traceroute provide indirect evidence from control responses and can be affected by filtering, ECMP hashing, and rate limits; they are not a complete route-map oracle.

### Controlled experiment and observation notebook

Create a forwarding table containing 0.0.0.0/0, 10.0.0.0/8, 10.20.0.0/16, and 10.20.5.0/24 with distinct next hops. For selected destinations, compute which entries match and choose the longest. Delete the most specific entry and repeat. Add an interface-down event and explain how the control plane may install a replacement forwarding entry only after route recomputation. Show how a local access-control rule can still block a packet after a valid route lookup. Use a low TTL to demonstrate loop termination conceptually, without generating uncontrolled routing loops.

## Routing Algorithms

**Routing Algorithms: conceptual explanation**

Routing algorithms balance reachability and changing network topology. Link-state protocols distribute topology information and compute shortest paths; distance-vector approaches exchange distance estimates with neighbors. Neither algorithm by itself guarantees security or convergence under arbitrary failures, and policy-based interdomain routing differs from simple shortest-path routing.

### Deep technical explanation

Routing algorithms exchange information so each participating router can choose paths through a changing graph. Link-state protocols distribute descriptions of local adjacencies and derive paths by running a shortest-path algorithm over a shared topology view. Distance-vector approaches exchange estimates from neighbors and update local distances using variants of the Bellman-Ford recurrence. Policies, administrative distances, metrics, areas, and filtering determine whether an advertised path is eligible at all. Shortest-path cost is a mathematical quantity chosen by the protocol, not automatically the shortest geographical distance or lowest observed delay.

Consider vertices A,B,C,D with directed or symmetric link costs A-B=1, B-D=2, A-C=4, C-D=1. The path A-B-D has total cost 3 and is preferred to A-C-D with cost 5 under additive metrics. If B-D fails, a new path may be selected after detection, advertisement, computation, and installation. Convergence delay is distinct from packet forwarding delay. During transition, different routers can briefly disagree, producing loops or black holes. The design question is not only whether a route eventually exists but how traffic behaves while the topology changes.

BGP introduces path policy at interdomain scale, where business relationships and export constraints can outweigh simple hop minimization. An ISP may prefer a customer route over a shorter route from a provider. Engineers should document policy separately from reachability. Testing a routing design requires failure injection or controlled simulations of link down/up events, examination of convergence timers, and proof that failover does not violate intended security boundaries.

### Controlled experiment and observation notebook

Represent a four-node network as an adjacency matrix with link costs. Run a shortest-path algorithm from node A and record tentative distances after every iteration, then delete one edge and run it again. Contrast the final shortest path with the transient state during reconvergence. Introduce an export policy that forbids one externally learned path and ask why the numerically shortest route is unavailable. Measure time to install a replacement route in a controlled virtual lab while generating low-volume probes. Note that traceroute can show a partial picture if devices filter or de-prioritize time-exceeded messages.

## Integrated Case Study and Model Limitations

### Integrated case study

A branch campus receives an IPv4 /24 for several student and staff networks. Start with the demand rather than assigning equal-size blocks. Suppose teaching labs need 100 conventional host addresses, staff needs 50, devices need 20, and a management network needs 10. A /25 offers 126 ordinary host addresses, a /26 offers 62, a /27 offers 30, and a /28 offers 14. These use 128 + 64 + 32 + 16 = 240 of the 256 address positions. Give exact boundaries and show which 16 addresses remain, rather than claiming a huge reserve. Address a planned expansion explicitly: doubling the teaching population may require a larger allocation or renumbering.

Now provide a sample route table. A general prefix points to the campus core, while a more specific prefix points to a laboratory gateway. For a destination matching both, longest-prefix match selects the specific entry. Explain that the route calculation and its installation in hardware are distinct. A host in the staff VLAN may have an IP route to the laboratory but still be denied by firewall policy. A physical uplink failure can cause a route to disappear only after the control system detects the failure and recomputes. During that interval, packets may be dropped or looped. A failure test must inspect transient as well as final behavior.

Construct a shortest-path graph with explicit additive link weights. Compute a shortest route from A to D under the stated weights, remove an edge, and recompute. Contrast shortest-path algorithms used within routing domains with interdomain route policy, where a commercial or security preference may exclude the arithmetically shortest path. Explain why not every router necessarily has an identical instantaneous view. Compare the calculated path to observed traceroute output while acknowledging packet filtering and flow hashing. When diagnosing reverse-path problems, collect routes in both directions.

Make the address plan auditable. Include a CSV-like table of prefix, first usable, last usable, broadcast, gateway, VLAN, and assigned purpose. Validate alignment mathematically. Include a written policy: which groups may initiate connections to services in other groups, which ports are necessary, and where the filters are enforced. Document IPv6 scope and the role of link-local addresses separately; a valid IPv4 plan does not automatically confer equivalent IPv6 security. The goal is not rote binary conversion but defensible choices about addressing, segmentation, routing, and observed connectivity.

### Engineering review and field notebook

Address design becomes difficult when the organization changes. A perfectly efficient subnet plan for today's host count may be expensive to renumber when a lab expands. Address ranges are a finite allocation resource in IPv4; route summarization is another resource because a clean topology can be represented with fewer prefixes. These objectives can conflict. Reserving a larger block for future growth leaves fewer positions for other groups, while tightly packing blocks may complicate later expansion. A strong design report includes an explicit growth forecast, even when labeled uncertain, and identifies which groups can be moved with limited disruption.

Routing and addressing must be audited together. A route that advertises a /16 aggregate while only one /24 behind it is reachable can accidentally attract traffic for destinations the advertising router cannot actually deliver. Conversely, withdrawing an aggregate after a link failure can make healthy subnets unreachable if they depend on that advertisement. In BGP, business policy and route filtering can dominate such choices. Within an enterprise routing domain, link metrics and area boundaries influence the control plane. A destination's longest-prefix lookup happens after these routes are installed. Confusing route origin with forwarding selection leads to diagnostic mistakes.

For a reproducible lab, capture route tables immediately before and after a controlled topology event. Note administrative state, forwarding adjacency, next-hop resolution, and a low-rate continuity probe. A link can report administratively enabled but have a neighbor-resolution failure; a route can exist without an operational egress; an application can fail because the return path is different. Running traceroute once and drawing a definitive map from its output is not enough, especially if routers suppress control replies or paths are load-balanced. Inspect both directions using appropriate observability.

A security review should place firewalls and segmentation deliberately. A VLAN boundary isolates broadcast scope but does not automatically restrict routed access. A private IP address is an addressing convention, not a guarantee that the host cannot be reached from a compromised internal network. IPv6 frequently coexists with IPv4; a rule protecting only one family may leave an equivalent service reachable through the other. Document every exposed address family and route domain. A good subnet assignment is simultaneously correct binary arithmetic, maintainable operations, consistent policy, and measured reachability.

A final routing diagnostic should explicitly distinguish the event that caused a path change from the measured response to it. Imagine a provider-facing link that physically fails at 12:00:00.000. Interface detection occurs after a measurable interval, adjacent routers receive new topology information, algorithms produce updated candidates, and forwarding state changes asynchronously. At 12:00:00.050 a host may still send toward the failed route despite a valid backup already existing in the underlying topology. At 12:00:01.000 the backup might be active but an upstream policy may still filter some traffic. Without a shared timeline, an investigator could attribute the outage duration to algorithm complexity when the actual delay came from detection or rule installation. Record link state, routing protocol event, FIB update, and actual probe recovery as independent timestamps.

Another subtlety is that routing reachability and transport reachability differ in both directions. A SYN reaches a service through a valid forward path but its SYN-ACK is discarded by a strict reverse-path policy or an incorrect return route. On the client, the failure resembles a silent service; on the server, packet capture shows the inbound attempt. If a translating gateway exists, the recorded translation mapping can expire or be inconsistent with a subsequent flow. Diagnosing such cases requires two observation points and the relevant state, not another attempt to resize subnets. For IPv6, route and neighbor discovery evidence should be collected with the correct scope and interface context. A link-local address alone is not a routable destination across an ordinary internetwork.

Summarization is an example of optimization that needs its own correctness argument. Advertising 10.20.0.0/16 is convenient when all subnets inside that block are reachable through the same next hop. If one constituent subnet is actually attached elsewhere and no more-specific corrective route exists, the aggregate can attract packets into a black hole. Before consolidating routes, prove that every affected destination has an intended path or deliberate rejection behavior. The same logic applies to network security: a neat addressing hierarchy helps policy management but is not the policy itself. Include negative tests from a disallowed segment to show that segmentation has enforcement behind it.

### Key technical vocabulary

**prefix length.** Number of fixed leading address bits in a routed network block.

**longest-prefix match.** Forwarding choice based on the most specific matching route.

**route metric.** Protocol-defined value used to compare eligible paths.

**aggregation.** Advertising a larger prefix to summarize several address blocks.

**convergence.** Process of detecting topology change and installing consistent forwarding choices.

**FIB.** Forwarding Information Base applied by a router to packets.

**NAT.** Address or transport information rewriting at a network boundary.

**link-local.** An address scoped to its local link rather than an ordinary global routing destination.

**asymmetric routing.** Condition in which return traffic follows a different network path.

**policy routing.** Choice of packet forwarding based on configured rules beyond destination prefix alone.

## Three fully worked problems

### Variable-length subnet allocation

Allocate nonoverlapping IPv4 blocks inside 192.0.2.0/24 for four groups requiring 100, 50, 20, and 10 conventional hosts. Show prefix lengths, block boundaries, usable host ranges and broadcast addresses. State whether the usual subtract-two rule applies to every IPv4 link prefix.

**Order demands and choose aligned block sizes**

A 100-host group needs 128 address positions, a /25. A 50-host group needs 64, a /26. A 20-host group needs 32, a /27. A 10-host group needs 16, a /28. Allocate from low to high to retain clear alignment: 192.0.2.0/25, 192.0.2.128/26, 192.0.2.192/27, and 192.0.2.224/28.

**Calculate usable ranges**

The first block uses 192.0.2.0–127, conventional usable 1–126, broadcast 127. The second uses 128–191, usable 129–190, broadcast 191. The third uses 192–223, usable 193–222, broadcast 223. The fourth uses 224–239, usable 225–238, broadcast 239. Addresses 240–255 remain within an unallocated /28.

**Prove there is no overlap**

The blocks cover consecutive, disjoint integer intervals aligned to their binary sizes. Each block's first address is divisible by its block size relative to the /24. A subnet plan should confirm interval disjointness with masks instead of relying only on visually tidy names.

**Clarify edge cases and policy**

The conventional network-and-broadcast reservation does not directly describe /31 point-to-point use or /32 single-host routes. VLAN and firewall policy are separate from address arithmetic, and the small remaining free block provides limited growth space.

**Answer**

Allocate /25, /26, /27 and /28 on .0, .128, .192 and .224 boundaries; .240/28 remains unallocated.

### Longest-prefix forwarding selection

A router has entries 0.0.0.0/0 via R0, 10.0.0.0/8 via R1, 10.20.0.0/16 via R2, and 10.20.5.0/24 via R3. Choose the next hop for 10.20.5.19, 10.20.8.4, 10.40.1.1, and 203.0.113.8. Then delete the /24 entry and reconsider the first destination.

**Find all matches, not just the first row**

Destination 10.20.5.19 matches the /0, /8, /16 and /24 routes. It selects R3 because /24 has the most fixed prefix bits. Destination 10.20.8.4 matches /0, /8, and /16 but not the /24, so it selects R2.

**Apply the fallback hierarchy**

Destination 10.40.1.1 matches the /8 and default but not the /16, so it uses R1. Destination 203.0.113.8 matches only /0, so it uses R0. These decisions follow binary prefix matching; they are not comparisons of alphabetical route order.

**Remove the most specific route**

After deleting 10.20.5.0/24, address 10.20.5.19 still matches 10.20.0.0/16 and is forwarded via R2, assuming the route remains installed and policy permits it. A route deletion can change path selection without making the destination unroutable.

**Distinguish forwarding from policy and reachability**

A configured filter can drop the packet even after this route lookup, and the next hop may be unreachable. Confirm interface state, neighbor resolution, and return-path routing before concluding that an installed forwarding entry establishes end-to-end connectivity.

**Answer**

R3, R2, R1, R0; after deleting /24, 10.20.5.19 falls back to R2.

### Shortest path and reconvergence

An undirected weighted graph has edges A–B=1, B–D=2, A–C=4, and C–D=1. Find the shortest route from A to D. After B–D fails, find the shortest remaining route. Explain why the path after failure is not necessarily used instantaneously by every router.

**Enumerate candidate simple routes**

Initially A–B–D has cost 1+2=3. A–C–D has cost 4+1=5. Under these stated positive additive weights and only the provided edges, the first path is the shortest between A and D. The cost represents configured routing metric, not geographical kilometers unless expressly defined that way.

**Recalculate the changed graph**

Removing B–D eliminates the cost-3 path. The remaining A–C–D route has cost 5 and becomes the shortest among the supplied alternatives. The change in final shortest path is mathematically immediate once a program has the updated graph.

**Discuss protocol convergence**

Operational routers must detect the loss, communicate new information or updated distances, compute preferred routes, and install entries. During these steps, devices can hold inconsistent states, causing transient loss or loops. Convergence time should be measured separately from per-packet path latency.

**Introduce policy constraints**

An interdomain route may be prohibited or deprioritized for commercial or security reasons. An arithmetic shortest-path result cannot predict BGP behavior without policy information. Document the routing protocol and selection criteria before assuming lowest numeric cost means selected route.

**Answer**

Initially A–B–D, cost 3; after loss of B–D use A–C–D, cost 5, after convergence.