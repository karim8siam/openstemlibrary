# Unit 5 — Application protocols

## Naming

**Naming: conceptual explanation**

Naming decouples human-readable names from underlying addresses or resources. DNS answers can be cached until their TTL expires; a cached answer is not evidence that a service is reachable. DNS resolution can involve multiple delegated zones, and DNSSEC addresses authenticity of DNS data, not confidentiality.

### Deep technical explanation

Domain Name System resolves symbolic names into data such as address records. It is not a direct, permanent mapping from a user-visible URL to one machine. A resolver may consult a cache, recursively query authoritative infrastructure, or receive a negative answer for a missing name. Different record types support addresses, aliases, mail exchange, service metadata, and delegation. The time-to-live controls how long cache entries may remain fresh; it does not schedule an exact universal instant at which every client changes its answer.

Separate the recursive resolver from the authoritative server. A recursive resolver acts on behalf of clients, uses cached data, and follows delegation when needed. An authoritative server publishes zone data for names within its delegated authority. A DNS lookup succeeds when an answer exists, but the resulting endpoint can still fail TCP, TLS, or HTTP. Conversely, an already open connection can remain functional while later DNS queries fail. A resolver error is not interchangeable with an application server error.

For an incident after changing a record, collect the queried name, type, server, response code, answer, TTL, and timestamp. Check negative caching, split-horizon policy, DNSSEC validation, and whether the application pins an earlier result. If a site uses multiple addresses or a content distribution network, different clients may receive different valid answers. The operational question is whether the answer received by the affected user points to a healthy and authorized service at that moment.

### Controlled experiment and observation notebook

Use a test zone you control and create address records with two different TTLs. Query through a recursive resolver and an authoritative server, recording each answer, response code, and remaining TTL. Change the authoritative record and examine why clients may continue using the cached version. Repeat a nonexistent-name query to observe negative caching behavior if supported. Introduce a deliberately incorrect name type and explain why receiving NOERROR with no desired answer differs from an outright network outage. Keep the experiment confined to a controlled zone instead of changing production DNS during active service.

## Web Protocols

**Web Protocols: conceptual explanation**

HTTP defines requests, responses, methods and representations at the application layer. A successful 200 response, a redirect and a cache validation response mean different things; idempotence is a property of method semantics, not a guarantee that no side effect can occur anywhere. HTTP versions differ in multiplexing and transport behavior.

### Deep technical explanation

HTTP defines request and response semantics independent of the particular wire representation. A method expresses intent, a status code reports the outcome category, headers convey metadata, and the representation body contains application data. Caching depends on explicit freshness rules and validation metadata; repeated GET requests may be served without repeatedly contacting the origin. Cookies introduce state to otherwise stateless exchanges. A reverse proxy may terminate TLS or rewrite headers, so origin logs and browser-observed behavior can differ in important ways.

HTTP/1.1, HTTP/2, and HTTP/3 are not just cosmetic versions. HTTP/2 adds binary framing and stream multiplexing over TCP. HTTP/3 maps HTTP semantics onto QUIC, which uses streams and incorporates cryptographic protections. A user may observe different connection setup costs, loss recovery behavior, and deployment compatibility. HTTP/3 does not guarantee lower latency in every network; middlebox UDP filtering or server configuration can force fallback. Protocol negotiation and graceful interoperability matter.

Analyze a redirect chain as part of total cost. An initial request may encounter several responses before the browser reaches content, and some connections require DNS resolution, transport setup, certificate validation, and authentication. Cache-control mistakes can leak personalized responses or prevent needed updates. For reproducible testing record exact URLs, methods, cache headers, status codes, content lengths, and connection negotiation; a screenshot of a page alone cannot establish protocol behavior.

### Controlled experiment and observation notebook

Design a cacheable public image and an authenticated account dashboard. Specify Cache-Control behavior for each, then demonstrate how mistakenly marking the private dashboard as publicly shared cache content can expose information. Capture request method, status, response size, freshness, validators, and protocol version. Send repeated requests before and after freshness expiry and measure how many reach the origin. Contrast this application behavior with the toy deterministic cache model. Compare HTTP/2 and HTTP/3 in a lab with loss introduced on one path, while noting that QUIC negotiation and UDP accessibility affect which protocol is actually used.

## Email

**Email: conceptual explanation**

Email delivery uses a store-and-forward architecture. SMTP transfers mail between systems, whereas IMAP is commonly used by a client to access its mailbox; these roles should not be conflated. SPF, DKIM and DMARC help evaluate sender-domain claims but do not prove that every message is benign.

### Deep technical explanation

Email is a store-and-forward application system, not a single reliable call from sender to recipient. A submitting client typically sends a message to a mail submission service; separate message transfer agents then relay it using SMTP. A receiving service may accept a message before it is placed into the user's mailbox. A successful SMTP acceptance response is evidence that the next system took responsibility, not proof that a human read the mail. Queue retries and delivery status notifications handle some failures, but filtering and policy can still affect delivery.

Mail headers and message bodies have different roles. MIME encodes attachments and multiple content types. SPF relates an envelope identity to permitted sending hosts, DKIM associates a cryptographic signature with selected message content and headers, and DMARC expresses policies linking alignment with a domain in visible From fields. These mechanisms help recipients judge domain authenticity but do not prove the message content is truthful. Forwarding can complicate SPF, and modifications can affect DKIM validation.

When diagnosing mail loss, trace message IDs, acceptance timestamps, queue state, retry responses, reputation policy, recipient rules, and bounce messages. Never assume that delivery failures can be solved simply by opening TCP port 25 on a laptop. Providers impose rate limits and authentication requirements, and large mailing systems need abuse controls. Build a controlled test using mail accounts you own, with explicit consent and no unsolicited mass messaging.

### Controlled experiment and observation notebook

Send one test email between accounts you control and record message ID, submission acceptance, relay stages, and final mailbox arrival. Create a MIME message with plain-text and HTML alternatives plus a small attachment; inspect how each part is encoded. Examine SPF, DKIM, and DMARC results without confusing a successful signature with proof that the message content is truthful. Inject an invalid destination into an offline simulation and inspect how queue retries differ from permanent rejection. Record which stage can truthfully claim acceptance, successful relay, mailbox placement, or recipient reading; these are not interchangeable events.

## Application Design

**Application Design: conceptual explanation**

An application protocol should specify framing, error responses, retries and backward compatibility. A client can time out after the server completed an operation, so blind retry of a non-idempotent request risks duplicate effects. Stable request identifiers and explicit server deduplication rules can make retry semantics safer.

### Deep technical explanation

Application protocols should reflect failure semantics rather than pretending the network is a local function call. A client that sends a request can time out before seeing a response even when the server completed the operation. Retrying may duplicate an effect unless the operation is idempotent or uses a unique request key. Names, version negotiation, authentication, message framing, and deadlines are part of the application contract. A serial protocol that works on localhost can fail on a wide-area network because of delay variation, transient disconnections, partial reads, or intermediary behavior.

Consider a remote reservation API. The client sends a request with an idempotency key; the server commits once and records the outcome against that key. If the response is lost, the client retries with the same key and receives the original result rather than creating a second reservation. This is application-level semantics, not a property that TCP automatically guarantees. A different operation such as viewing an item can often retry harmlessly. Document which actions are safe to repeat and which require deduplication.

A well-designed protocol states payload limits and validation rules. If a declared message length is very large, reject it before allocating unbounded memory. An error response should be useful without exposing secrets. Add metrics for timeouts, retries, duplicate suppression, version mismatch, and rejection reasons. Test the client against an intentionally slow or faulty server, because success on a fast local host is weak evidence that network fault handling is correct.

### Controlled experiment and observation notebook

Specify a purchase-style API with an idempotency key, deadline, and explicit error codes. Simulate a server committing an operation and losing the reply, followed by a client retry. Verify that the duplicate key returns the original result without creating a second side effect. Next generate an oversized length field and require the server to reject it before allocation. Test incompatible client versions and unknown optional fields. Log the timing, correlation identifier, retry policy, and deduplication outcome. Contrast request completion at the server with delivery of the response to the client; the former may happen when the latter does not.

## Integrated Case Study and Model Limitations

### Integrated case study

A service depends on domain names, secure web requests, and email notifications. Diagram the request path from client to recursive resolver, authoritative DNS infrastructure, reverse proxy, application, and origin datastore. A recursive resolver can cache a record and continue returning it until freshness expires, so changing an authoritative address does not instantly change every client's behavior. Explain a cache miss and a cache hit under a deterministic TTL, then identify real-world complications such as prefetch, negative caching, multiple resolvers, and clock handling. Distinguish the address used for connection from the hostname used for TLS certificate validation and HTTP authority semantics.

Study two HTTP resources: a public document that changes monthly and a private account dashboard. The document might benefit from an explicit freshness period and validator, while the authenticated dashboard requires rules preventing shared caches from exposing personalized responses. Create a table for method, status, Cache-Control, ETag or Last-Modified, content type, cookie behavior, and repeat-request origin traffic. A GET request is conventionally safe and cacheable under applicable rules, whereas a state-changing operation needs deliberate retry and deduplication policy. Do not infer cache behavior from response size alone.

Next draw how a notification email leaves the application and reaches a recipient. Submission to a mail server is only the first milestone; relays and destination acceptance are separate events. SPF, DKIM, and DMARC help validate sending-domain claims, but successful authentication cannot prove a recipient read the content. Delivery status is probabilistic at operational scale because filtering and recipient mailbox state are outside the sender's direct control. Track message IDs, SMTP responses, retry queues, bounce classifications, and receiving-domain policy.

For an end-to-end exercise, imagine a user reports "I signed up but received no confirmation." A good diagnosis does not immediately send many duplicate emails. Verify that the signup transaction committed once, whether the notification job was enqueued, whether it was accepted by the submission service, whether subsequent relays reported failure, and whether the recipient address is correct. In parallel, check whether the registration API timed out but actually completed, which affects whether a retry could duplicate an account. A protocol-aware application reports specific, user-actionable states rather than collapsing all failures into "network error."

### Engineering review and field notebook

Application performance is often dominated by policies far above the IP layer. A DNS answer from cache may save a lookup, yet an application can immediately discard the benefit by opening excessive sequential connections. A reverse proxy can reduce origin load through caching but accidentally serve stale private data if it ignores identity-dependent cache rules. Mail submission can complete successfully while a recipient's mail system later rejects or quarantines the message. These are different lifecycle stages that need different operational metrics and user-facing error states.

A dependable client should classify failures rather than endlessly retry. Network timeouts suggest uncertainty about whether the request succeeded; an authentication rejection usually requires new credentials or a corrected authorization rule; an explicitly invalid request generally should not be retried unchanged. A server can provide machine-readable error categories and correlation identifiers. For an operation that creates a resource, an idempotency key can make repeated attempts safe when implemented with durable atomic bookkeeping. Without that design, a client cannot always infer from missing replies whether a remote side effect occurred.

Developers should know that cache behavior interacts with URL design. Immutable files identified by content version can be cached for long periods because a new version is addressed differently; mutable resources need freshness and revalidation rules. The HTTP response method, status and headers govern cache semantics, not a simplistic assertion that "all GETs are safe to cache". Authenticated or sensitive representations require explicit care. Test caching through the actual reverse proxy and browser combination, because a unit test against only the origin can miss a shared-cache data leak.

Operational reports about notifications should distinguish queued, submitted, relayed, accepted, delivered to a mailbox, and read. The sender may lack reliable evidence for later stages. SPF, DKIM, and DMARC are domain-authentication mechanisms, not content truth validators or promises of inbox placement. A robust reporting system shows what it actually observed and refrains from telling a user that an email was read merely because an upstream relay accepted it. This lesson generalizes: express each network protocol's observation honestly, then provide the next diagnostic action that observation justifies.

### Key technical vocabulary

**recursive resolver.** A DNS service that obtains answers for clients and often maintains caches.

**authoritative server.** A DNS server designated to provide records for a zone or delegation.

**TTL.** A cache freshness lifetime with implementation-specific operational interactions.

**negative caching.** Retention of relevant responses indicating an absent DNS record or name.

**ETag.** HTTP entity tag used as representation metadata for conditional requests.

**cache validator.** Metadata permitting a cache to ask whether a stored response still applies.

**SMTP.** Mail transfer protocol used for submission and relay under applicable configurations.

**MIME.** Message format mechanisms supporting multiple content types and attachments.

**correlation identifier.** ID used to link application request events across services and logs.

**retry policy.** Rules controlling whether and when an uncertain operation may be attempted again.

## Three fully worked problems

### TTL caching under an exact time schedule

A toy recursive cache receives identical queries at integer times t=0,1,2,...,12. A cache miss fetches a record that remains fresh for exactly five time units, becoming stale at t=5,10, and so on. Count origin lookups. Explain why changing a DNS record on the authoritative server at t=2 does not force all resolvers to show the new answer at t=2.

**Set the freshness interpretation**

The first query at t=0 misses, so a cached answer becomes fresh for t=0 through just before t=5. Queries at t=1,2,3,4 are served from cache under the stated model. Freshness expires exactly at t=5, prompting another origin lookup.

**Count subsequent misses**

The same schedule repeats at t=5 and t=10, giving three lookups for the 13 queries at times 0 through 12. The count is not the number of different domain names because the problem contains one repeated name and type.

**Explain propagation of authority changes**

The authoritative server's update at t=2 changes what future authoritative queries return, but it does not recall already cached responses that remain fresh. Other resolvers may have filled at different times, so different clients can legitimately observe different still-cached values.

**State real-world departures**

Negative caching, multiple resolvers, prefetch, connection reuse, service failover, record types, and local client caches are excluded. A user-report investigation needs the queried name, record type, resolver, TTL, answer, and timestamp rather than a blanket claim that DNS must update globally at a precise moment.

**Answer**

Origin lookups occur at t=0,5,10: three misses for thirteen queries.

### HTTP caching for two data classes

A service provides a public immutable course diagram and a personalized grades page. Choose a high-level HTTP caching strategy for each. Explain the data-exposure risk of applying the public resource policy to the private page, and describe evidence that a repeated request was served from a cache rather than the origin.

**Classify the two resources**

The public diagram is identical for authorized and anonymous readers and can often use a long freshness period when its URL includes a content version. Its cache strategy must include an update path such as a new versioned URL or appropriate validation rules.

**Protect personalized information**

The grades page depends on the authenticated user's identity. A shared intermediary must not reuse one student's grades representation for another. Apply appropriate private or no-store directives according to the application threat model, and ensure authorization is checked for each request. Cookie handling and cache keys require particular care.

**Measure behavior rather than guessing**

Inspect request/response headers, cache indicators where available, status codes, ETags or validation responses, and server access logs. A fast response alone does not prove a cache hit, because the application or network may also be fast.

**Include protocol and deployment details**

HTTP/2 and HTTP/3 transport HTTP semantics differently, but privacy rules for an authenticated resource still matter. A reverse proxy configuration change should be tested with two different accounts before release, not just one signed-in browser session.

**Answer**

Versioned public resources may be cached broadly; private grades require policies that prevent cross-user shared-cache disclosure.

### Idempotent API retry after a lost response

A client requests creation of a single enrollment with idempotency key K. The server creates the enrollment and commits its database transaction but the response is lost. The client retries the identical request with K. What outcome must a correct idempotency implementation produce, what state needs to be stored, and why does TCP reliability not solve this application-level ambiguity?

**Recognize the ambiguity**

The client knows only that it did not receive the success response. It cannot infer whether the server accepted, rejected, or completed the request. A timeout is not a rollback signal. Blindly repeating a state-changing operation without safeguards risks creating a second enrollment.

**Define deduplication semantics**

The server should associate K with the authenticated caller, the operation's identifying inputs, and its durable result. On retry with the same key and compatible request details, it returns the original committed outcome or a documented equivalent without creating another enrollment. An inconsistent request reusing K should be rejected under explicit rules.

**Explain atomicity and expiry**

Ideally, the idempotency record and business mutation are committed atomically or protected by a design with equivalent correctness. Keys must be retained long enough for retries within the documented window; expiration policy determines when reuse may once again cause an operation.

**Separate layer responsibilities**

TCP can reliably deliver bytes for one connection but cannot prove that the remote application committed a database transaction before a response was lost. Application protocol semantics, durable state, and transaction handling are required.

**Answer**

The retry with key K must return the original result without a second enrollment, using durable deduplication tied to the operation.