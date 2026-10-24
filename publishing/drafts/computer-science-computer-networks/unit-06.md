# Unit 6 — Network security

## Encryption Interfaces

**Encryption Interfaces: conceptual explanation**

Encryption interfaces must specify algorithms, nonce behavior, key distribution and the threat model. Authenticated encryption protects confidentiality and detects tampering when used correctly, but encrypting data cannot protect a compromised endpoint that already holds plaintext. Nonce reuse can be catastrophic in some modes.

### Deep technical explanation

Cryptography protects information under stated trust assumptions; encryption does not inherently establish who sent a message. Confidentiality hides plaintext from observers without the key. Integrity detects unauthorized modification when authenticated encryption or appropriate message authentication is used. Authentication ties a peer to an identity that the verifier has reason to trust. Network security designs must separate these properties because a system can encrypt data to an attacker if it accepts the wrong public key.

Authenticated encryption with associated data binds ciphertext and selected unencrypted metadata to an authentication tag. A nonce must satisfy the algorithm's uniqueness requirements; repeating a nonce under the same key can cause severe failures in schemes that assume non-repetition. The application should rely on maintained libraries and protocol constructions rather than inventing a cipher or a handshake. Transport security is often terminated at a proxy, which creates a new trusted boundary between the proxy and downstream service.

A packet capture of a TLS connection can confirm that the connection used an encrypted protocol, but it cannot certify that the destination identity was checked correctly. Verify trust-store settings, endpoint name verification, certificate validity, and whether client authentication was expected. Measure the performance cost of handshakes and encryption separately from application latency. Weaknesses frequently arise from key management, trust decisions, and error handling, not from the mathematical cipher itself.

### Controlled experiment and observation notebook

Implement an authenticated-encryption demonstration using a maintained cryptographic library in a controlled exercise. Encrypt a sample message with associated authenticated metadata, then deliberately change one ciphertext byte and confirm decryption fails authentication. Demonstrate, without using real secrets, why reuse of a nonce under an algorithm that requires uniqueness violates assumptions. Make a separate test in which data is encrypted to an unverified attacker's public key: confidentiality may exist, but the recipient identity is wrong. Do not write a custom cipher or claim a checksum provides sender authenticity. Record whether the protection is end-to-end or terminated by a trusted proxy.

## Authentication

**Authentication: conceptual explanation**

Authentication establishes a claimed identity using evidence such as credentials, keys or multi-factor challenges. Authorization is a separate decision about permitted actions. A valid TLS connection to a hostname does not make an application's user account privileged; service identity and end-user identity sit at different layers.

### Deep technical explanation

Authentication answers whether a peer controls credentials associated with an asserted identity. Authorization answers which operations the authenticated identity may perform. They are different checks: a valid login does not entitle a user to another account's records. Credentials may include passwords, public-key proofs, certificates, one-time codes, or short-lived tokens. A session cookie or bearer token represents authority for whoever can present it, so its protection and scope matter even if the initial login was strong.

A certificate-based TLS client can validate the server's asserted DNS name against a trusted certification path. The relevant hostname, validation period, trust anchor, and certificate extensions matter. Disabling verification for a test environment creates a dangerous path into production if not tightly contained. Mutual TLS authenticates both endpoints at the transport layer but does not automatically implement an application-level role policy. Likewise, possession of an API token should not grant privileges beyond its declared audience, expiry, and scope.

Security tests should include expired tokens, incorrect hostnames, revoked credentials where revocation is available, changed roles during a session, and replayed requests. Logs must identify which authorization decision failed without exposing secrets or personal data. Rate limiting helps manage guessing and abuse but cannot substitute for secure credential storage and strong session management. Model identity propagation through proxies so headers from external clients cannot impersonate trusted internal assertions.

### Controlled experiment and observation notebook

Create a permission matrix for a viewer, editor, and administrator, with explicit operations on two unrelated accounts. Authenticate a sample user and test every authorization decision; one valid password must not grant access to all resources. Rotate a short-lived token and confirm the old token is rejected after expiry. Test wrong audience and wrong scope. In a certificate simulation, compare the requested hostname with the certificate's permitted names, validate expiry using a controlled clock, and enforce trust-chain requirements. Explain why turning off certificate verification in a client is not an authentication workaround acceptable in production.

## Secure Transport

**Secure Transport: conceptual explanation**

Secure transport such as TLS negotiates parameters, authenticates peers where configured and establishes traffic keys. Certificate validation includes name matching and a trust path; disabling verification defeats an important part of security. The security of a connection depends on implementation and endpoint handling as well as cryptography.

### Deep technical explanation

Transport Layer Security negotiates cryptographic parameters and authenticates peers according to the configured trust policy. In modern deployments TLS 1.3 is widely used for TCP-based HTTPS, while QUIC uses a TLS 1.3-based handshake integrated into its transport. The handshake establishes shared secrets and transcript integrity; later application records are protected with derived traffic keys. A high-level timing diagram should distinguish network round trips from processing and certificate verification. Connection resumption can reduce setup cost but changes the security and replay considerations.

Early data is a particularly important exception. QUIC and TLS mechanisms can allow some data to be sent before a fresh handshake is fully complete in a resumed session. Such data can be replayed in some threat models; an application must limit it to operations safe under replay or enforce protections. A non-idempotent financial transfer or destructive operation should not be casually sent using early data. The presence of encryption alone does not remove replay or application authorization risks.

To diagnose a handshake failure, record the negotiated protocol, offered cipher suites where observable, ALPN, hostname, certificate chain validation, and the exact alert or application error. A TCP port accepting connections is insufficient evidence that TLS succeeds, and a TLS handshake completing is insufficient evidence that the HTTP route exists. Test from affected client environments, because trust stores, clock skew, and proxy interception may differ across devices.

### Controlled experiment and observation notebook

Draw a TLS 1.3-style conceptual timeline separating round-trip delay from CPU and certificate-validation work. Use a toy two-RTT latency model only as an accounting exercise, not an exact description of every resumed or QUIC handshake. Create a table for new connection, resumed connection, and application transaction, recording which bytes may be transmitted before fresh confirmation. Discuss early-data replay and exclude non-idempotent actions from replay-prone paths. For a failing connection capture hostname, protocol negotiation, trust-store outcome, and error alert; a successful TCP connect by itself does not establish cryptographic success.

## Attack Surfaces

**Attack Surfaces: conceptual explanation**

Attack-surface analysis enumerates exposed parsers, services, administration interfaces and trust boundaries. A reachable port is not automatically exploitable, but unnecessary exposure increases opportunities for mistakes. Defense uses least privilege, patching, monitoring and segmentation instead of treating a firewall as a complete guarantee.

### Deep technical explanation

A network-facing service exposes parsers, authentication endpoints, dependencies, control interfaces, and operational processes to untrusted traffic. A threat model starts with assets and trust boundaries: what can an unauthenticated Internet client influence, what is merely internal, and what data must remain protected? An exposed management plane and a public read-only website have different consequences. Address translation and private IP numbering are not substitutes for access policy, hardening, or robust authentication.

Denial-of-service risks range from saturating links to exhausting CPU, memory, connection tables, or application workers. A bandwidth dashboard can look normal while an expensive query path consumes all server threads. Conversely, a large volume of legitimate flash-crowd traffic can trigger the same bottlenecks without an attacker. Mitigation combines capacity planning, quotas, request validation, connection limits, caching, and coordinated upstream response. Rate-limiting the wrong shared IP can block thousands of legitimate clients behind one translator.

Defensive logging should capture enough metadata for investigation while minimizing collection of sensitive payloads. Test malformed input handling with controlled, authorized requests rather than scanning third-party systems without permission. Vulnerability severity depends on reachability, privilege, impact, and exploitability. A scan report is a hypothesis until verified. Patch strategy must account for rollback, compatibility, and service continuity so a security improvement does not accidentally disable the network.

### Controlled experiment and observation notebook

Draw a threat model for a public API, an internal database, and a management plane. Label which interfaces are reachable from outside and which operations require identity and authorization. List three resources vulnerable to exhaustion: application workers, connection state, and upstream bandwidth. Set bounded lab limits for malformed inputs and high request rates; do not direct attack traffic at third-party hosts. Add a defensive rate limit behind a shared NAT and analyze how legitimate users might be collateral damage. Specify exactly which logs are needed to investigate abuse without retaining unnecessary payload or secrets.

## Integrated Case Study and Model Limitations

### Integrated case study

A secured university service has a public HTTPS endpoint, a private application network, and an administrative control plane. Define the trust boundaries first: anonymous clients may request published course pages but should not be able to query private student records or configure infrastructure. Create an authorization matrix of viewer, instructor, operator, and service roles. Trace how an authenticated identity travels from the edge proxy to the application. If internal headers carry identity, the application must accept them only from trusted infrastructure, not arbitrary client-supplied copies.

Describe TLS as protection with specific conditions. The client verifies a certificate chain and expected hostname, then exchanges application data under established keys. A TLS tunnel to a legitimate-looking but unverified endpoint offers insufficient identity protection; disabling hostname checks during troubleshooting may silently create an interception risk. A gateway terminating TLS is a deliberate security boundary: decrypted bytes are available to that gateway, and the downstream hop needs its own protection appropriate to the threat model. Authenticated encryption provides tamper detection under its assumptions but is not a substitute for business authorization.

Use a threat model with three distinct adversary goals: read private data, change submitted grades, and make the service unavailable. Confidentiality controls address the first, integrity and authorization address the second, and capacity management and response plans address the third. An encrypted service can still suffer denial of service. Apply rate limits carefully where many students share a campus NAT; a low per-source-IP threshold can deny access to innocent users. Monitoring should avoid logging passwords or complete authentication tokens.

Build a test matrix: correct user and operation; correct user but forbidden record; expired credentials; wrong certificate name; revoked authorization; oversized request body; duplicate state-changing request; and loss of the management controller. In each case, state the expected status and safe failure behavior. For a resumed connection or early data, discuss replay and exclude operations that cannot tolerate it. Keep experiments defensive and conducted only on systems under explicit control. Security is demonstrated by negative tests and documented trust assumptions, not by a padlock icon alone.

### Engineering review and field notebook

A threat model needs concrete trust boundaries rather than a broad label of "encrypted." The communicating parties must decide which services are trusted to read plaintext, which services may make authorization decisions, and where a credential can be presented. An HTTPS reverse proxy is often trusted to terminate TLS, which means it can see application data; if the backend connection is not protected, confidentiality on the client-facing leg cannot extend automatically through the whole system. Protect backend links according to risk and make identity propagation explicit. Headers that an arbitrary browser can set must not be accepted as proof of an internal user's identity.

A useful security test suite contains negative cases. Expired credentials must fail appropriately. A certificate for the wrong hostname should not be accepted just because its cryptographic signature is valid. A read-only user should not be able to update records. A duplicate state-changing request should not silently create two effects when the application promises idempotency. A malformed length field should be rejected before causing huge memory allocation. A failed security test often reveals more about system correctness than another successful login demonstration.

Availability protection is different from confidentiality and integrity. A service can use modern cryptography and still be taken offline by exhausted CPU, database connection pools, or network capacity. Defensive rate limits can help, but grouping users by shared source IP can penalize an entire campus. Choose rate-limit keys and thresholds in light of application identities, deployment topology, and expected bursts. Monitoring should record aggregate resource pressure and unusual error rates while minimizing secret and payload retention. Avoid turning visibility into an unnecessary privacy or data-security risk.

Real security assessment requires controlled environments and authorized targets. The exercises in this book are mathematical illustrations or defensive simulations, not permission to scan or stress systems owned by someone else. Where current security mechanisms matter, follow maintained protocol specifications and library guidance. Cryptographic details, certificate validation, and browser defaults change as implementations evolve; a static textbook should explain fundamental properties while pointing readers to authoritative current documentation for production decisions.

### Key technical vocabulary

**confidentiality.** Protection against unauthorized disclosure of information.

**integrity.** Ability to detect unauthorized modification under stated trust assumptions.

**authentication.** Process establishing a peer identity or credential claim.

**authorization.** Decision whether an identity may perform a particular operation.

**TLS termination.** End of a transport security association at a component that can access plaintext.

**trust anchor.** Root of a credential or certification validation chain.

**nonce.** Algorithm-specific value whose uniqueness or freshness requirements matter.

**replay.** Reuse of previously recorded legitimate protocol data in a new context.

**attack surface.** Reachable interfaces and parsing or privilege boundaries subject to malicious input.

**rate limiting.** Controls that restrict request or resource consumption according to a defined policy.

## Three fully worked problems

### Identity and confidentiality across a proxy

A student accesses an HTTPS application through a reverse proxy that terminates TLS. The proxy forwards traffic to a backend over another connection. Explain which communication legs are encrypted, what the client has authenticated, and which additional checks are required before the backend may trust an identity header supplied by the proxy.

**Draw the trust boundaries**

The client-to-proxy TLS association protects traffic on that leg and authenticates the proxy's presented identity according to client policy. The proxy sees decrypted application data by design. The connection to the backend is a separate association whose encryption and authentication depend on its own configuration.

**Prevent forged identity headers**

The backend must not treat arbitrary external client-supplied headers as trusted identity assertions. The proxy should discard or overwrite any such untrusted fields, and the backend should accept them only from an authenticated trusted proxy path. Authorization at the backend must still check whether the user is permitted to perform the requested operation.

**Distinguish guarantees**

TLS confidentiality is not an application access-control list. Authentication of a server does not mean every user is authorized to read every record. If a backend hop is plaintext, observers on that trusted segment may have visibility not present on the client-to-proxy leg.

**Define a negative test**

Send requests with a forged identity header from an untrusted client and verify that the backend ignores it. Test expiry of user credentials and revocation of roles after initial authentication. Record outcomes without logging secret token material.

**Answer**

The client authenticates the TLS endpoint; backend identity assertions require trusted proxy enforcement and separate authorization.

### Independent exposure model is not a breach forecast

A classroom assumes that each of ten hypothetical independent trials has event probability 0.01. Calculate the probability of at least one event, then explain why this number should not be published as a real cybersecurity breach forecast for ten login attempts or ten endpoints.

**Use the complement**

If events are independent and each has probability p=0.01, the probability of zero events over ten trials is (1-p)^10 = 0.99^10. Therefore at least one event has probability 1−0.99^10 ≈ 0.0956179, or 9.56 percent.

**Check assumptions**

Real-world attack attempts may be highly correlated. Their probabilities depend on attacker skill, exposure, controls, monitoring, and vulnerability distribution; they are not known to be uniform 1 percent Bernoulli trials. Treating every event as independent without evidence makes the numerical conclusion unreliable.

**Separate relative illustration from empirical calibration**

The formula illustrates accumulation under a hypothetical model. To estimate actual risk, define the event precisely, collect suitable exposure data with relevant controls and time periods, assess model bias, and report uncertainty. A security risk score derived from an invented probability is not evidence.

**Make a safe decision**

Use defensible mitigations such as strong authentication, least privilege, secure patching, and rate limits appropriate to the real threat model. The toy calculation can help teach complement probability but cannot rank a production network's security posture.

**Answer**

1−0.99^10≈9.56% only under the explicitly hypothetical independent 1%-per-trial model.

### Replay of early application data

A resumed secure transport may allow application bytes to be sent before a fresh session is fully confirmed. An API supports read-only course retrieval and a non-idempotent money transfer. Explain which operation is safer to place on replay-prone early data, identify the required application safeguard for state changes, and give a negative test.

**Define replay risk**

An attacker or network behavior may cause certain early data to be replayed under the protocol's threat model even though ordinary application traffic is cryptographically protected. Encryption and authentication alone do not guarantee a side-effecting request is executed once.

**Classify operations by semantics**

A read-only course retrieval is generally easier to tolerate if repeated, although privacy and rate limits still matter. A money transfer or destructive update is not intrinsically replay-safe. A sensible policy avoids early execution of unsafe actions unless strict replay protections are designed and verified.

**Describe safeguards**

Application-level idempotency keys, durable deduplication, freshness limits, and server-side replay defenses may reduce risk. The exact policy depends on endpoint semantics and protocol implementation. Merely requiring HTTPS does not make a payment operation safe to repeat.

**Propose a controlled negative test**

Send identical requests twice in a staging environment with simulated transport replay. Verify that a read remains consistent and that the unsafe mutation occurs at most once. Record exactly which layer enforces the property and whether logs expose replay attempt evidence.

**Answer**

Read-only idempotent operations are generally safer for replay-prone early data; state changes need explicit replay protection.