# Unit 1 — Network architecture

## Layers

**Layers: conceptual explanation**

The layered model is an engineering separation of concerns, not a promise that all networks implement exactly seven OSI layers. A sender passes application bytes down through transport, network and link processing; a receiver processes the headers in reverse order. Implementations may combine functions across layers.

### Deep technical explanation

The protocol stack is a set of contracts between components, not a physical stack of boxes. The link layer moves frames between neighbors on one link. The Internet layer carries datagrams across internetworks, placing a destination address in every packet and relying on routers to forward it. A transport can provide reliable bytes, unreliable datagrams, or independently managed streams to applications. Application protocols define what messages mean: a status code is useful only if both participants agree on its interpretation. Distinguish service, interface, and implementation. A socket API provides a service to a program; TCP specifies observable transport behavior; the operating system implements the state machine.

A packet walk reveals why these boundaries matter. Suppose a laptop communicates with a server separated by three routers. The destination IP address is normally stable for the journey, while the source and destination link-layer addresses change for each hop. A new frame is constructed at each outgoing interface. A port identifies a transport endpoint within a host, not the router next to that host. Encryption can make much of the application content invisible to intermediate devices. The familiar OSI model is educational vocabulary; Internet implementations do not necessarily map one-to-one onto seven independently implemented modules.

An engineer should identify the exact contract a diagnosis depends upon. A DNS error is not proof of physical link failure, and a Wi-Fi association is not proof of Internet reachability. Captures at different layers answer different questions. A link-layer capture might show successful ARP resolution while an IP-layer test still fails because there is no correct route. Layering narrows responsibility but cannot eliminate interactions: a small transport send can produce many packets if the path fragments payloads or retransmits losses.

### Controlled experiment and observation notebook

Build a small topology with a client, an Ethernet switch, a router, and a server. Label each interface with a concrete link address and each host with an IP address. Send an application message over TCP and write four distinct views: the client socket state, a frame captured on the first switch port, the IP packet at the router, and the receiving application's bytes. Change the server's application port without changing its IP. Predict what fails and which layers continue working. Then remove the default gateway and repeat the test to expose the dependence on local routing. Draw a fault tree with the first observation that excludes each competing explanation.

## Protocols

**Protocols: conceptual explanation**

A protocol defines formats, state transitions, timing and error behavior between participants. A packet field alone is not a complete protocol: TCP sequence numbers matter because both endpoints maintain connection state and acknowledge ranges of bytes. An incompatible interpretation can fail even when packets arrive intact.

### Deep technical explanation

A protocol is both a language and a coordinated sequence of actions. Syntax specifies how a receiver finds fields. Semantics specifies how those fields affect state. Timing determines when a sender waits, retries, or expires an exchange. Error handling specifies what happens when a message is delayed, corrupted, duplicated, or delivered after the sender has moved on. Merely transmitting a correctly formatted message does not guarantee interoperability. Endpoints may disagree about a version, a stream identifier, sequence wraparound, or a timeout.

A state-machine view provides discipline. Draw circles for states, label transitions with received events and timers, and write a condition for every transition. An initial TCP connection establishment is not simply three arbitrary packets: the peers exchange synchronization of sequence space and prove enough state to begin transmitting bytes. The acknowledgment field acknowledges a byte boundary in the stream. Reordering creates a gap; retransmission fills the gap without changing the application's intended byte sequence. Protocol traces therefore require a timeline as well as a list of header values.

Versioning deserves equal care. A sender should not assume that a new optional field is understood by an older peer. Extensibility involves negotiation or documented rules for unknown fields. On a production rollout, deploy a small compatibility matrix: clients with old and new versions, server responses to malformed lengths, duplicated messages, expired credentials, and delayed responses. A robust protocol refuses ambiguous inputs instead of guessing what they meant.

### Controlled experiment and observation notebook

Create an abstract request/response protocol with states CLOSED, WAITING, COMPLETE, and FAILED. Define legal input lengths and a transaction identifier. Deliberately deliver the same reply twice and ask whether a naive client performs a duplicate action. Next delay a reply until after the timeout, and explain why a retransmitted request cannot be interpreted solely by arrival order. Implement a bounded deduplication store and document its expiry semantics. Record what happens when an old client receives an unfamiliar status field. The goal is interoperability under abnormal ordering, not merely sending packets that satisfy a happy-path trace.

## Encapsulation

**Encapsulation: conceptual explanation**

Encapsulation adds a header or trailer so each layer can express information for its peer, such as addresses, checksums or ports. The link frame carries an IP packet; that packet carries a transport segment, which in turn may carry an HTTP request. Header bytes consume bandwidth, and the maximum transmission unit can constrain payload size.

### Deep technical explanation

Encapsulation gives each layer a place to record decisions for its own scope. An Ethernet frame can contain an IP packet, which contains a transport segment, which carries application data. Fields are not cost-free. A 1,200-byte application payload carried with a 20-byte IPv4 header and a 20-byte TCP header has 1,240 bytes before link overhead. That ratio is about 96.8 percent, but it excludes Ethernet framing, options, retransmissions, acknowledgment traffic, and possible security records. Never describe this as a universal TCP efficiency figure.

The maximum transmission unit limits the IP packet size one link can carry without further handling. With an IPv4 MTU of 1,500 bytes and ordinary 20-byte IPv4 plus 20-byte TCP headers, the familiar TCP maximum segment size is 1,460 bytes. Options and tunnels reduce this budget. Path MTU Discovery tries to learn a workable size; a black hole can occur if required control messages are filtered. IPv6 routers do not fragment packets in transit, so source packetization matters even more. The designer should also know whether an encapsulation is added only at an endpoint or on every leg of a tunnel.

Use a byte-accounting table when measuring throughput: useful application bytes, payload framing, transport headers, network headers, link framing, and repeated bytes. A small-message service can be dominated by headers and interrupts even when link utilization appears low. Larger messages can amortize headers but may delay urgent requests. The correct unit of comparison is measured useful data delivered within a specified deadline, not the nominal link bit rate alone.

### Controlled experiment and observation notebook

Prepare a table with payload sizes of 64, 256, 1200, and 1400 bytes. Calculate the percentage of useful bytes if 40 bytes of IP and TCP headers are added, then add an illustrative 38 bytes of link-related overhead in a separate column. Explain why those numbers are not the exact framing cost of every technology. For the largest payload, discuss which paths could accommodate it inside a 1500-byte MTU and how extra tunnel headers alter the budget. Ask learners to measure bytes at the application and NIC counters and explain why these can disagree without either measurement being wrong.

## End-To-End Principles

**End-To-End Principles: conceptual explanation**

The end-to-end argument asks whether a function belongs at an intermediate network element or at the communicating endpoints. A link checksum can detect corruption on one hop, but an application still needs end-to-end integrity if intermediate hosts or storage can modify data. End-to-end design is a reasoning principle, not a prohibition on useful in-network services.

### Deep technical explanation

The end-to-end argument is a test for responsibility. Some functions can be implemented completely and reliably only by the endpoints that know the application's goal. A hop-local checksum detects errors on a link, but an application receiving a file may need to verify the entire object after decompression, caching, storage, and transfer. An intermediary cannot generally certify that the recipient has the intended document because it lacks application semantics. At the same time, link-local error correction is valuable: it can recover quickly from a noisy medium without imposing a remote end-to-end round trip.

Consider an upload with a content hash. The sender computes a digest from the intended bytes. A router forwards encrypted packets but does not interpret the file; the receiver computes the digest and compares it to the trusted expected value. If hashes disagree, additional transfers or diagnostics are required. The digest alone does not authenticate the sender unless it is received through a trusted mechanism. This distinction illustrates how reliability, integrity, authenticity, and availability differ. An end-to-end design asks precisely which property is being established and by whom.

Middleboxes complicate the argument. Firewalls, address translation, caching proxies, and load balancers can improve performance or enforce policy, but may also interfere with new transport features. The path may be asymmetric, making captures on one leg misleading. A sensible design keeps critical correctness properties verifiable by endpoints while treating network assistance as an optimization with failure modes. Ask whether a hypothetical intermediate failure can cause an undetected wrong answer; if so, an endpoint-level check may be necessary.

### Controlled experiment and observation notebook

Transfer a file with an end-to-end digest and run three controlled tests. In the first, corrupt data before it enters the network stack; in the second, simulate a transient link transmission error and let the link retry; in the third, alter stored data after successful network delivery. Decide which components can detect each fault. Repeat with a malicious sender who replaces both the file and an unauthenticated digest; discuss why an authenticated source of the expected digest matters. Keep availability separate from correctness: a connection timeout is evidence of missing timely delivery, not evidence that the file content would have been invalid.

## Integrated Case Study and Model Limitations

### Integrated case study

A complete request trace starts before any HTTP bytes exist. A person types a secure URL into a browser; the browser checks local state for relevant DNS answers and connections. If it needs an address, it performs resolution through a configured resolver, possibly receiving an answer from cache. The client chooses a destination address, source address, route, and transport. A local Ethernet or Wi-Fi hop must reach a next-hop device, so neighbor discovery may occur before the first routed packet can leave. The application hands bytes to transport, transport produces segments or streams, network processing selects IP addresses and packet sizes, and link processing constructs frames for the next neighbor. Multiple paths can be involved when DNS, content, authentication, and telemetry endpoints are on different hosts.

Draw a trace with five columns: application intent, transport action, IP packet, local frame, and observation point. At the client link, record source and destination MAC addresses; at the router output, write the new pair. Do not change an end-to-end destination IP simply because the link destination changes. At a translator, distinguish the exceptional case where source or destination IP and port may be rewritten. Show where link CRC checking happens and where authenticated application integrity can be verified. State which processes can see encrypted payloads; the presence of a TLS session changes what intermediaries can inspect. A topology diagram that ignores security boundaries is incomplete.

Consider a performance budget for transferring a 100-kilobyte object. Suppose application processing takes 9 ms, DNS on a cache miss takes 22 ms, initial connection setup consumes 45 ms, and data transfer takes 35 ms. A first request can take approximately 111 ms under this deliberately additive toy model, while a cache hit and connection reuse might remove much of the first two components. Do not claim that these values are universal. If throughput is the bottleneck, examine useful bytes per second and retransmission. If response time is the bottleneck, examine round trips and queueing. Small objects may be dominated by setup costs. Test both a cold-cache and warm-cache scenario with identical payloads and clearly recorded assumptions.

Finally introduce four faults at different layers: the Wi-Fi connection disappears, DNS gives an obsolete address, the remote port rejects transport connections, and an application responds with an error. For each, describe one observation likely to distinguish it from the others and one observation that cannot. A local gateway ping does not prove DNS works; resolving a name does not prove the service accepts TLS; a successful TLS handshake does not prove that the application resource exists. A useful network engineer learns to combine narrow evidence into a causal chain without assuming one check certifies the entire path.

### Engineering review and field notebook

The first principle of architectural measurement is to record the boundary at which each claim is valid. A full-page request trace is not one packet, and a packet captured at the source is not identical to every link frame that later carries it. Consider the distinction between a connection and a message: a TCP connection can carry many requests, a TLS session can protect multiple records, and a browser can open concurrent connections to independent services. When an observer says "the request used TCP," ask whether this was measured at the affected client and time or inferred from an older configuration. HTTP/3, for example, can use QUIC instead. Always record negotiated transport rather than guessing from the URL scheme.

Use a trace notebook with a column for confidence. A packet capture that shows SYN and SYN-ACK supports a claim about transport establishment but does not show an authenticated application identity. A DNS response with one address supports a claim about that resolver's answer, not every client's cached result. A router's FIB entry supports a claim about its chosen next hop at the recorded instant, not whether the receiver eventually accepted the payload. Treat the combination of independent observations as a chain. When any essential link is missing, the final statement should explain the missing evidence instead of inventing it.

For a design review, compare an architecture that relies on one gateway for all traffic with another that has two redundant gateways. Redundancy improves only the failure modes for which there are independent paths and correct failover. If both gateways share one faulty route policy, the added hardware does not solve the policy risk. Similarly, two network links connected to the same upstream switch are not independent of that switch. An architecture document should show physical failure domains, control-plane dependencies, and the path of each application dependency. Review both ordinary service delivery and recovery during faults.

Finally require a unit test for the mental model itself: provide a capture with normal link framing but failed application authorization; provide another with DNS success but missing routes; and provide a third with TCP success but incorrect TLS identity. A reader who can classify these failures without conflating layers has learned more than a reader who can recite seven labels. The deeper objective is to know which measurements would change a diagnosis, what assumptions a protocol layer makes of lower layers, and what correctness property the application must still verify end to end.

### Key technical vocabulary

**service interface.** The operations or guarantees a lower component offers to an upper component.

**protocol state.** Remembered local information governing what events are legal next.

**encapsulation.** Wrapping a unit of data with header or trailer fields for a different communication scope.

**MTU.** Largest IP packet size supported by a particular link or path under a specified interpretation.

**MSS.** Maximum TCP segment data quantity negotiated under protocol constraints.

**next hop.** Adjacent device to which an outgoing link frame is sent toward a routed destination.

**end-to-end verification.** Checking a correctness property at the ultimate communicating or application endpoints.

**control plane.** The functions that compute and distribute forwarding choices.

**data plane.** The functions that apply forwarding choices to individual packets.

**capture point.** The interface, software layer, and time at which traffic was observed.

## Three fully worked problems

### Encapsulation, MTU, and useful-data fraction

An application sends 1,200 data bytes using TCP over IPv4. Assume a 20-byte TCP header and a 20-byte IPv4 header, no options, no retransmissions, and ignore link framing. Calculate the network-level payload efficiency. Then assess whether a 1,460-byte application segment fits a 1,500-byte IP MTU. Finally identify two realistic changes that would invalidate this exact arithmetic.

**Account for the distinct byte quantities**

The 1,200 bytes are application data, not the transmitted IP packet size. The TCP segment is 1,200+20=1,220 bytes and the IPv4 packet is 1,220+20=1,240 bytes. These two headers are not application payload. Including the link framing would require another explicit overhead assumption.

**Compute a dimensionless efficiency**

The fraction of IP packet bytes containing useful data is 1,200/1,240=0.9677419, or about 96.77 percent. The denominator must be total counted transmitted bytes. Dividing by nominal interface bit rate would answer a different question. The percentage is not an observed TCP goodput metric.

**Test the maximum-segment boundary**

For 1,460 bytes of application data, 20+20 bytes of headers bring the IP packet to exactly 1,500 bytes, satisfying this stated MTU. An additional IPv4 option, TCP option, or tunnel overhead makes it larger. The endpoint may then use a smaller segment size or another valid path-MTU mechanism.

**Conclude with model limitations**

Ethernet, Wi-Fi, TLS records, IPsec tunnels, losses, acknowledgments, and application pacing change wire-level efficiency. A correct report states that the 96.77 percent applies to one hypothetical unfragmented IPv4/TCP packet under the given header sizes.

**Answer**

96.77% of counted IP packet bytes carry application data; a 1460-byte segment exactly fills the assumed 1500-byte IP MTU.

### Packet versus frame forwarding through routers

A student captures a packet on a laptop Ethernet link, at a router egress, and at a destination server. The frame is forwarded across two separate links without translation. What header fields are expected to change on each routed hop, which end-to-end identifiers normally remain stable, and what observations would distinguish an ordinary router from a translating gateway?

**Identify per-link scope**

The incoming Ethernet frame is addressed to the router interface as its link destination. The router removes that incoming framing and chooses the next-hop neighbor on the outgoing interface. It constructs a new link frame with the outgoing source MAC address and next-hop destination MAC address. A link-layer CRC from the incoming frame is not carried unchanged across the new link.

**Identify Internet-layer continuity**

Without a translator, the packet's source and destination IP addresses normally stay the same during forwarding, while the IPv4 TTL or IPv6 Hop Limit is reduced. The IPv4 header checksum must be updated when covered header fields change. IPv6 has no IPv4-style base-header checksum. A transport connection uses IP addresses and ports to distinguish its communication context.

**Consider exceptional changes**

A NAT gateway may rewrite source or destination IP information and transport ports. Tunnels can add an outer packet header; a firewall can drop or modify policy-relevant fields. Comparing captures at two vantage points requires accounting for offload and capture placement. An IP address change is not proof of a router malfunction if a translation policy was intentionally applied.

**State a falsifiable check**

Pair packets by stable identifiers and timing, then compare the link addresses, IP endpoints, hop limit, and ports on each side of the router. If the expected next hop never receives frames, inspect neighbor discovery and the outgoing interface before debugging application logic.

**Answer**

Link addresses are hop-local; IP endpoint addresses normally survive routing unless translation or tunneling changes the visible envelope.

### End-to-end integrity versus hop-local recovery

An uploaded file passes through a wireless hop, a router, an HTTPS reverse proxy, and a storage service. A link CRC and TLS are both enabled. The file stored at the destination differs from the source because of a storage-side software defect. Explain which mechanism can detect this, why a checksum on one hop is insufficient, and how an authenticated expected digest changes the trust argument.

**Place each mechanism at its boundary**

The link CRC checks a frame's accidental alterations on one link and may trigger local recovery. It does not validate the file after processing in a proxy or application. A TLS record provides protection for data within one TLS security association. If the proxy terminates TLS, a separate backend security association may be required to protect that leg.

**Construct an end-to-end test**

Compute a cryptographic digest of the intended file and convey the expected digest through a trustworthy mechanism. After storage and retrieval, compute the digest of the received file. A mismatch shows that the file bytes differ from the intended bytes with overwhelming probability for a suitable cryptographic hash, independently of whether each intermediate link accepted its frames.

**Separate integrity from authenticity**

A malicious party capable of replacing both the file and an unauthenticated advertised digest defeats a naive comparison. Digitally signed metadata or an authenticated channel to a trustworthy source establishes why the expected digest should be believed. That issue is not solved by a link CRC.

**Limit the claim**

A matching digest does not prove the user received the file on time or that the application displayed it correctly. Integrity, sender authentication, completeness, and availability are separate properties that require separate tests.

**Answer**

Use a trusted end-to-end digest comparison; hop-local CRC or one terminated TLS connection cannot alone certify stored-file identity.