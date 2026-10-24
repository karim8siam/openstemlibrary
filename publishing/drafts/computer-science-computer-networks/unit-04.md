# Unit 4 — Transport

## Reliability

**Reliability: conceptual explanation**

Transport reliability uses sequence spaces, acknowledgments, timers and retransmissions to cope with loss or reordering. The receiver must distinguish duplicate data from new data, and timeouts can cause needless retransmissions. Reliability covers the bytes in a connection, not necessarily successful application processing or durable storage.

### Deep technical explanation

A reliable byte transport must recover from losses, duplication, and reordering without falsely giving the application multiple copies of the same bytes. TCP numbers bytes in a stream and uses acknowledgments and retransmission to infer delivery progress. An ACK with a particular value typically states the next byte expected in sequence; it is not a count of packets received. Selective acknowledgments can supply additional information about out-of-order blocks. A receiver that observes two copies of a retransmitted segment should still place each byte exactly once into the logical stream.

A sender maintains timers because silence cannot distinguish a dropped segment from a delayed ACK. Too short a timeout induces spurious retransmissions; too long a timeout prolongs stalls. Round-trip estimates and variability influence recovery. A packet capture can show retransmissions, but a retransmission alone does not prove loss at the point where the capture was taken; capture limitations and offload features can produce confusing traces. Correlate both sides when possible.

Reliable stream delivery does not supply message boundaries. If an application writes two records with separate socket calls, the receiver may observe them combined or split among reads. Correct framing at the application layer is still necessary. Also distinguish transport delivery to the receiving stack from successful processing by the server's business logic. A payment API that retries after a timeout needs idempotency semantics to avoid duplicate charges, even if the TCP stream itself is reliable.

### Controlled experiment and observation notebook

Generate a stream with application records A, B, and C, each spanning multiple bytes. Deliver corresponding transport segments out of order and with one duplicate. Update a receiver's next-expected-byte pointer as each arrival occurs. Demonstrate why delivered application bytes must be ordered and why record boundaries are not preserved by stream read calls. Simulate a retransmission triggered by timeout and then by duplicate acknowledgments; distinguish observing retransmission from proving actual packet loss. Add an application operation that has a side effect and describe the idempotency rule it needs when the entire request is retried.

## Flow Control

**Flow Control: conceptual explanation**

Flow control protects a receiving endpoint against data arriving faster than its buffers are consumed. In TCP, the advertised receive window constrains sender flight size, while congestion control separately responds to perceived network capacity. A fast network path does not override a small advertised receive window.

### Deep technical explanation

Flow control protects a receiver from a sender that can deliver data faster than the receiver's buffers or application can consume it. In TCP, the receiver advertises an available receive window. The sender's usable flight budget is constrained by the receiving window and by congestion-control state, which represents a different limit. A large network capacity does not help if the receiver can accept only a small amount of unacknowledged data. A zero-window advertisement can pause transmission while the sender probes for reopening.

The bandwidth-delay product estimates the in-flight data needed to fill a path. A 10-Mbit/s bottleneck with 40-ms round-trip delay has BDP 10,000,000 × 0.040 / 8 = 50,000 bytes. A receive window much smaller than that may cap throughput below the path's capacity even without packet loss. But simply enlarging buffers is not a universal improvement. Oversized queues can increase latency under load, and memory budget must consider the number of concurrent connections.

Trace a slow transfer by comparing advertised receive window, outstanding bytes, acknowledgment spacing, and application read behavior. If an endpoint fails to read promptly, transport backpressure may be the correct behavior, not a fault in the router. The cure could be a faster consumer, bounded work queue, stream compression, or a different application batching strategy. Design capacity tests that vary RTT and receiver read rate independently so flow control is not confused with congestion control.

### Controlled experiment and observation notebook

Select three round-trip delays, 5 ms, 40 ms, and 100 ms, on a fixed 10-Mbit/s path. Compute the bandwidth-delay product in bytes for each, and determine a hypothetical receiver window too small to fill the path. Then introduce a sender limited by its congestion window and show why increasing the receiver buffer alone does not resolve that separate constraint. Record the packet capture's advertised receive windows, bytes in flight, and application read rate. Explain a zero-window event and safe reopening. Discuss the memory and tail-latency consequences of very large buffering across thousands of concurrent flows.

## Congestion Control

**Congestion Control: conceptual explanation**

Congestion control reacts to shared-network overload using information such as losses, delays and acknowledgments. The congestion window limits in-flight bytes, but it is not equal to the receiver buffer size. Evaluating only bandwidth without round-trip delay misses the bandwidth-delay product that governs achievable flight size.

### Deep technical explanation

Congestion control protects the network when multiple senders compete for a finite bottleneck. The congestion window limits how much data a sender puts in flight based on its interpretation of network feedback. A sender can use loss, explicit congestion notification, or timing information as signals, depending on the implemented algorithm. Different algorithms react differently to RTT and queue dynamics. A simplified additive-increase/multiplicative-decrease model grows a window cautiously and reduces it after congestion, illustrating a distributed search for capacity rather than guaranteeing fairness.

Queueing creates a latency-throughput tradeoff. A bottleneck link with service rate 20 packets/s and arrivals approaching that rate can have rapidly increasing expected wait under a simple queue model. Real Internet traffic has burstiness, correlated flows, and non-exponential service, so the textbook M/M/1 formula is an analytical comparison, not a production prediction. Large standing queues can preserve high throughput while degrading interactive response time. Active queue management and fair queuing attempt to address different aspects of the problem.

A careful congestion diagnosis compares throughput, RTT percentiles, retransmissions, ECN markings, bottleneck utilization, and application demand. A low transfer speed might instead reflect flow control, server CPU limits, receiver disk performance, or insufficient data available to send. Distinguish the mechanism before tuning parameters. When sharing a path with real-time calls, perform load testing within a controlled lab rather than imposing unbounded traffic on a production network.

### Controlled experiment and observation notebook

Place an M/M/1 queue beside a real traffic trace and compare their assumptions. With service rate 20 packets/s, compute steady-state expected queue size and waiting time for arrival rates 5, 10, and 16 packets/s. Note how these estimates rise as utilization approaches 1. Next apply a bursty arrival schedule with the same average and show why the simple stationary formula can miss short spikes. Add an explicit receive-window limit as a different bottleneck and explain why both effects cannot be diagnosed from throughput alone. Use controlled traffic generation, with limits that prevent disruption to shared services.

## Multiplexing

**Multiplexing: conceptual explanation**

Multiplexing distinguishes application conversations using endpoint identities such as transport ports and protocol numbers. The same port can be used by many connections because their complete endpoint tuples differ. Source and destination ports are service-demultiplexing fields, not authorization tokens or encryption.

### Deep technical explanation

Transport multiplexing lets multiple applications or streams share underlying connectivity. The five-tuple of protocol, source address, source port, destination address, and destination port often identifies a TCP flow for demultiplexing. Many simultaneous connections may use the same server port because their other tuple fields differ. UDP also uses port numbers, but applications must implement their own message handling and, where needed, reliability or ordering. A port number is a routing aid inside a host, not proof of application identity or authorization.

Multiplexing inside one connection raises a second question: can independent logical operations make progress when some data is lost? HTTP/2 multiplexes several streams within one TCP connection. Because TCP delivers an ordered byte stream, a lost transport segment can delay delivery of later bytes for all streams on that connection. QUIC carries multiplexed streams over UDP and supports reliable delivery at the stream level, avoiding some cross-stream head-of-line delays, though the path still has finite congestion-control capacity.

A useful test transfers two independent objects: one very large and one tiny. Compare tail latency while injecting limited packet loss under HTTP/1.1, HTTP/2, and HTTP/3 in a controlled environment. The apparent result depends on connection reuse, server implementation, caching, crypto handshake, path conditions, and browser policy. Do not attribute all observed latency changes to multiplexing without controlling these variables.

### Controlled experiment and observation notebook

Model two HTTP streams, one large response and one small response, carried over a single ordered TCP connection. Mark a transport packet containing bytes needed before the small response and temporarily remove it from the arrival sequence. Observe which later bytes cannot be delivered until recovery. Repeat with two independent QUIC streams conceptually, emphasizing that independent stream delivery does not remove shared congestion capacity or all possible application blocking. Compare p95 latency, retransmissions, protocol negotiation, and handshake time before attributing any measured improvement to transport multiplexing alone.

## Integrated Case Study and Model Limitations

### Integrated case study

A student uploads a large project archive over a path with a nontrivial round-trip delay. To understand performance, draw both the receiver's flow-control boundary and the network's congestion-control boundary. If the bandwidth is 10 Mbit/s and RTT is 40 ms, the BDP is 50,000 bytes. A receiver window of 12,000 bytes caps possible in-flight data at less than a quarter of that estimate, even with a healthy network. But a congestion window of only 8,000 bytes can impose a tighter bound regardless of the receiver's capacity. Compute a rough throughput upper bound from flight budget divided by RTT before introducing losses or protocol overhead. This is a ceiling under assumptions, not a guarantee.

Use a timeline of bytes 0 through 9999 sent in segments. Delay the second segment while delivering the third. Show how receiver buffering and cumulative acknowledgments preserve the byte stream, and distinguish an ACK boundary from packet counting. After the missing bytes arrive, the receiver can deliver the complete continuous prefix. The application still needs its own record delimiter or length prefix because transport reads can split a file's logical records arbitrarily. If the upload request's acknowledgment response is lost, repeating the full operation may need an idempotency key at the application layer to prevent duplicate records.

Introduce congestion: a second bulk transfer now competes for the bottleneck. RTT rises and a queue begins to grow. A packet drop may trigger transport recovery; an application can perceive stalls that are not explained by the original physical propagation delay. Separately, a slow receiving application can advertise a small or zero receive window even if the network is otherwise idle. Design observations capable of distinguishing these conditions: bytes in flight, receive window, congestion-window approximation if available, RTT trends, retransmission counters, and receiver CPU usage.

Finally compare multiple HTTP exchanges over one TCP connection with separate streams over QUIC. QUIC's stream independence can prevent an unrelated stream from waiting for missing bytes of another, but its congestion controller still manages shared path capacity. Reference the relevant protocol specifications when describing exact mechanisms; do not invent a generalized claim that QUIC is always faster. Run an authorized loss-injection experiment on a controlled service and compare end-to-end latencies while preserving client version, TLS settings, object sizes, and network condition. A valid conclusion identifies which mechanism changed the observation.

### Engineering review and field notebook

A transport diagnosis can be represented as a hierarchy of limits. First determine whether the application has enough data available to transmit. Next consider the receiver's advertised ability to buffer and process incoming bytes. Then consider the sender's congestion controller, which reflects competing traffic and perceived path capacity. Finally consider the path's propagation, link rate, queues, and loss. Each can limit throughput independently. A single observation such as 2 Mbit/s user throughput does not identify which factor is active. Better evidence includes application write demand, advertised receive window, bytes in flight, round-trip estimates, and recovery events.

It is tempting to treat reliability as an absolute yes-or-no property, but the relevant contract has more nuance. A reliable ordered byte stream can preserve bytes and order while still failing to complete within an application's deadline. A caller may give up after five seconds, yet a server could finish the operation at six seconds. When the caller retries, correct business semantics require deduplication or safe repeatability. This remains true even if the transport itself never delivered duplicate bytes within one connection. Networks do not provide a magic exactly-once business transaction primitive merely because transport is reliable.

Consider message delivery over a datagram protocol. Applications may choose to recover some losses, ignore others, use sequence numbers, or add forward error correction. A real-time audio receiver sometimes prefers to skip an overly late packet instead of waiting for recovery that would add delay to subsequent audio. A file transfer prefers exact content, typically allowing more recovery time. Transport policy should therefore be evaluated against application objectives: completeness, deadline, ordering, fairness, and resource use. The right design for interactive voice need not be the right design for archival backups.

Create a comparison matrix for a TCP stream, independent QUIC streams, and a basic UDP request/reply protocol. Record what each abstraction guarantees and what the application must implement. TCP supplies stream ordering and retransmission under standard conditions, but not application record boundaries. QUIC supplies multiplexed stream semantics and transport-integrated security under specified negotiated conditions, but not a magical guarantee of zero latency. A raw UDP datagram preserves datagram boundaries but does not promise reliable ordered delivery. The matrix should include congestion behavior, failure handling, authentication requirements, and operational availability, not only developer convenience.

### Key technical vocabulary

**acknowledgment.** A transport signal reporting reception progress according to protocol semantics.

**retransmission.** A repeated transmission used to recover after suspected loss or missing acknowledgment.

**receive window.** Receiver-advertised constraint on acceptable outstanding transport bytes.

**congestion window.** Sender-side constraint representing perceived network capacity or congestion state.

**BDP.** Bandwidth times round-trip delay, interpreted as approximate in-flight path inventory.

**head-of-line blocking.** Later work waits behind missing or incomplete earlier ordered data.

**RTT.** Elapsed time for a signal and associated response to complete a round trip.

**goodput.** Useful application data delivered per unit time, excluding specified overhead.

**idempotency.** Property that repeating an operation has no additional logical side effect.

**stream multiplexing.** Interleaving multiple logical data flows over a shared transport association.

## Three fully worked problems

### Stop-and-wait goodput at variable RTT

A sender transmits 12,000 useful bits in 1.2 ms and waits for acknowledgment. Assume acknowledgment round-trip delay of 8 ms after transmission, no losses, no acknowledgment serialization, and no other processing. Compute the idealized useful goodput. Then explain why the link rate cannot be inferred from this number.

**Establish the cycle time**

One complete send-and-wait cycle occupies 1.2+8.0=9.2 ms. A new packet is not started until the acknowledgment is received under this deliberately simple stop-and-wait rule. The sender therefore completes one useful block per 0.0092 seconds.

**Evaluate the data rate with units**

Goodput equals 12,000/0.0092=1,304,347.8 bits/s, or about 1.304 Mbit/s. This uses application bits delivered per elapsed cycle time, not the count of link symbols or raw interface capacity.

**Identify the bottleneck behavior**

The sender is idle during most of the waiting interval. Even a very fast physical link cannot remove the stop-and-wait idle period when RTT dominates. Sliding-window protocols allow multiple blocks in flight, subject to flow and congestion limits.

**Explain what is not proved**

Loss, retransmissions, headers, ACK traffic, delayed ACK policy, and application scheduling all change actual performance. The result describes the specified model, not a universal throughput achievable by TCP.

**Answer**

Idealized stop-and-wait goodput is approximately 1.304 Mbit/s.

### Bandwidth delay and receive-window ceiling

A path has capacity 10 Mbit/s and 40-ms round-trip time. Calculate BDP. A receiving application advertises an effective window of 12,000 bytes; estimate a simple RTT/window throughput ceiling and compare it to raw link capacity. State which other control limit can produce a lower rate.

**Calculate path inventory**

BDP in bits is 10,000,000 bit/s × 0.040 s = 400,000 bits. Dividing by eight gives 50,000 bytes. That amount of in-flight data would fill the path in an idealized steady-flow model.

**Apply the receive-window limit**

A 12,000-byte effective window is 96,000 bits. A rough RTT/window upper bound is 96,000/0.040=2,400,000 bits/s, or 2.4 Mbit/s. This is below the 10-Mbit/s path capacity and assumes each full window can be acknowledged every RTT without other overhead.

**Separate congestion from flow control**

The sender also respects its congestion-control state. If its congestion window admits only 8,000 bytes, that becomes the tighter flight limit. Application pacing, traffic availability, CPU, and retransmissions can lower observed useful throughput further.

**Choose a diagnostic measurement**

Collect advertised windows, bytes in flight, RTT, retransmissions, and receiver read rates. A buffer increase is unlikely to help if a congested path or CPU-limited application rather than receiver backpressure is the actual bottleneck.

**Answer**

BDP 50,000 bytes; with a 12,000-byte flight budget, idealized RTT/window ceiling is 2.4 Mbit/s.

### Reliability and independent stream semantics

An application sends two logical messages over one ordered TCP byte stream. Bytes 0–999 are received, bytes 1000–1499 are lost, and bytes 1500–1999 arrive. What prefix can an ordinary in-order reader receive before recovery? Why does a second application stream over a QUIC connection change some delivery dependencies without creating extra network bandwidth?

**Locate the contiguous prefix**

A TCP receiving stack can acknowledge that bytes through 999 form the continuous received prefix. Later bytes 1500–1999 can be buffered but must not be exposed as a continuation of the ordered stream while bytes 1000–1499 are missing. A reader cannot assume delivery of the later range as an ordered byte-stream prefix.

**Recover the gap**

After the lost block is retransmitted or otherwise recovered, the receiver can extend the contiguous sequence to byte 1999. The application may still see an arbitrary grouping of reads because TCP does not preserve message boundaries. It needs separate framing to reconstruct messages.

**Contrast multiplexed transport models**

With HTTP/2 over TCP, the byte-stream gap can delay frames belonging to independent HTTP streams. QUIC uses transport-level streams that can advance independently with respect to stream-specific ordered delivery. A lost packet can still affect any stream whose frames were in that packet.

**Bound the performance claim**

QUIC streams share connection-level congestion control and path capacity. Independent delivery avoids one category of cross-stream blocking; it does not promise every stream has an independent bandwidth guarantee or that every deployment beats TCP.

**Answer**

Only bytes 0–999 are continuously deliverable before recovery; QUIC stream independence changes some ordering dependencies, not shared path capacity.