# Unit 6: Reliability and security

## 6.1 Input Risks

Web inputs cross a trust boundary whenever user-controlled data influences a database query, HTML rendering, filesystem operation, network call, or operating-system command. Injection arises when untrusted data is treated as control syntax rather than as inert values. Parameterized SQL queries keep data separate from query structure; escaping alone is fragile when contexts and encodings differ. In a template, output encoding must match the sink: HTML text, HTML attribute, URL, JavaScript string, and CSS context are not interchangeable. Modern frameworks often escape ordinary interpolation but can expose deliberate raw-HTML APIs that bypass the protection.

Cross-site scripting can allow injected code to run in another user's browser under the application's origin, potentially manipulating displayed data or issuing actions. Content Security Policy may reduce exploitation, but strong prevention begins with safe DOM APIs, contextual encoding, and avoiding untrusted HTML interpretation. Server-side request forgery is another boundary problem: if a service fetches a user-supplied URL, the destination may resolve to an internal address, metadata endpoint, or other resource not meant to be publicly accessed. Validate the intended destination class and manage redirects and DNS changes, rather than trusting a simplistic hostname substring check.

File uploads require careful design. Restrict size and permitted content based on business need; do not rely only on an extension. Store files under server-generated identifiers outside executable application directories, scan when appropriate, and serve with safe content-type and download policies. Parsing images, documents, or archives can consume unexpectedly large resources. A 'zip bomb' expands small compressed input into excessive storage or memory. A document extractor also carries vulnerabilities and should operate with limited privileges. Input validation and infrastructure resource limits address different parts of this risk.

Build adversarial tests around real data flows. Trace a comment from HTTP request through storage and later display; an apparently safe input may become dangerous when rendered in a different context. Trace a remote URL through redirections and name resolution. Trace an identifier through authorization checks. Security reviews should focus on how data changes trust level, not merely scan for forbidden characters. The OWASP Top 10:2025 names broken access control, misconfiguration, supply-chain failures, cryptographic failures, and injection among the principal web application risks. The categories guide attention, but the actual controls depend on the application's threat model.

### Applied design, experiment, and interpretation

**Case analysis: unsafe comments in a lesson forum.** A student writes text containing HTML-like syntax. It is safe when inserted with textContent, but becomes dangerous if passed to innerHTML without appropriate sanitization. Input should remain data even when an administrator later views reports, or when an email digest includes the comment. If rich text is required, use a well-maintained context-aware sanitizer with a restrictive policy and avoid executing arbitrary embedded scripts. SQL queries must likewise use parameters rather than concatenating student text into query syntax.

**Research exercise.** Trace the same input through database storage, HTML display, CSV export, and email. Identify each sink and required encoding or escaping rule. Also test a remote-image fetcher against internal or link-local targets and redirections. The exercise is defensive: the goal is to show correct data handling and blocked unauthorized destinations, not to construct a harmful exploit chain.

## 6.2 Session Protection

Sessions connect consecutive requests to an authenticated identity and related context. For cookie-backed sessions, the server may issue a cryptographically unpredictable session identifier, stored by the browser and returned under cookie rules. The identifier is a bearer credential: anyone possessing it may be able to act as the user until it expires or is revoked. Secure, HttpOnly, and SameSite cookie attributes reduce particular attack surfaces, but no attribute makes application authorization checks unnecessary. A session should have an appropriate idle timeout and absolute lifetime, and high-risk actions may require recent authentication.

Cross-site request forgery takes advantage of the browser's tendency to send credentials on certain cross-site requests. SameSite settings help in many flows, but robust systems still consider CSRF tokens or other origin verification where appropriate, especially for state-changing operations. CORS does not by itself prevent a malicious site from causing all types of requests; it primarily controls access to responses from scripts under browser policy. A developer who confuses those mechanisms may build an application that appears protected in a manual test but remains vulnerable to state changes initiated from another origin.

Session fixation is a separate problem. If an attacker can make a victim use a known session identifier before login and that identifier remains valid after authentication, the attacker may gain access. Rotate or replace the session identifier at meaningful privilege transitions. On logout, invalidate server-side state; for stateless bearer tokens, consider short lifetimes and revocation mechanisms with their operational tradeoffs. Do not store sensitive tokens in browser storage merely because it is convenient; script access and extension behavior are significant considerations. Avoid placing tokens in URLs, logs, analytics, or referrer-exposed locations.

Test session protection by opening multiple browser contexts, switching identities, logging out, and attempting stale requests. Verify that private responses are not shared through caches, that session rotation really occurred, and that staff role changes take effect according to documented policy. Race conditions can exist when requests issued before logout complete afterward. Define whether a credential is evaluated at request entry or immediately before a sensitive mutation. Users expect logouts and revocations to mean something, so security semantics should be expressed clearly rather than inferred from UI behavior.

### Applied design, experiment, and interpretation

**Case analysis: logout from a shared computer.** A student signs out after reviewing private grades on a library machine. The application removes its local UI state but leaves the server session active. Someone using the same browser can open the grade endpoint directly, so the visual sign-out was misleading. Revoke or expire the authoritative session, clear relevant cookies using matching attributes, and prevent sensitive personalized responses from being shared-cached. Under a token-based design, explicitly define how long already issued credentials remain valid after logout.

**Research exercise.** Authenticate in two browser contexts, log out in one, and attempt the same protected read from both. If global logout is offered, verify both sessions are revoked; otherwise document per-session semantics. Inspect whether a cached grade can be viewed without network access after logout and decide what privacy guarantee can realistically be made in a browser cache model.

## 6.3 Dependency Management

A modern web application incorporates code from package managers, build tools, runtime dependencies, container images, deployment pipelines, and external scripts. That supply chain can introduce defects or malicious behavior beyond the application's own source code. Pinning a dependency version improves reproducibility, but it does not automatically make that version safe. Lockfiles, integrity checks, trusted registries, review procedures, and vulnerability advisories are complementary controls. The goal is to know which artifacts are running, where they came from, and how quickly an unsafe component can be replaced.

Dependency risk is not proportional only to the number of packages. A package that executes in a build pipeline with access to production credentials is more sensitive than a small utility used only in a sandboxed local test. Installation scripts and transitive dependencies can run code unexpectedly. Minimize permissions of CI tokens, prevent untrusted pull requests from receiving deployment secrets, and separate preview environments from production authority. Reproducible builds make it easier to compare expected outputs, although perfect byte-level reproducibility may require carefully controlled toolchains and timestamps.

Software bills of materials can list relevant components and versions; signing and attestation can help verify provenance. Those mechanisms do not certify that code is bug-free. An engineering team also needs update ownership: who receives a dependency advisory, who assesses exploitability in the actual deployment, and who can execute a safe rollback? Avoid blanket automation that blindly merges breaking major updates, but also avoid indefinite freezes that leave known vulnerabilities exposed. A controlled upgrade process uses tests, staged deployment, and monitoring.

An external analytics script adds a particularly visible tradeoff. It can affect page speed, user privacy, and origin execution rights. Limit third-party code, apply suitable loading policy and Content Security Policy, and document data transmission clearly. The security boundary changes if a script executes with first-party page authority rather than in a restricted iframe. In educational platforms collecting minors' data, dependency and tracking choices may raise additional compliance concerns. Treat supply-chain management as an ongoing operating discipline rather than an occasional version bump.

### Applied design, experiment, and interpretation

**Case analysis: a compromised build dependency.** A small CSS-processing tool runs during production builds. An update unexpectedly adds a post-install script with network access and filesystem permissions. Even though the tool is 'only for styling,' its execution context may expose credentials in CI. Pin trusted versions, minimize token privileges, review release provenance, and run builds in isolated environments. A dependency scanner might flag known vulnerabilities, but it cannot prove the absence of unknown malicious code. Reproducible build artifacts and signed provenance strengthen investigation.

**Research exercise.** Inventory the build's direct and transitive dependencies, record which ones can execute code, and identify credentials available at each step. Test a controlled dependency update in staging, comparing asset hashes and permitted network destinations. Design a rollback that restores a known artifact without regenerating it from an untrusted toolchain during an incident.

## 6.4 Rate Controls

Rate controls limit how quickly a principal, client, or resource can consume service capacity. They can protect login endpoints from online guessing, search APIs from accidental overload, and expensive document-generation functions from runaway use. The correct key might be a verified account identifier, a network source, a device signal, or a combination. Each choice has failure modes: many legitimate users may share one public IP address at a campus, while a malicious actor can distribute requests across many addresses. Rate limiting should be only one layer alongside authentication, authorization, queueing, and resource budgets.

A fixed-window counter is simple but can permit bursts around a window boundary. Sliding-window counters reduce some boundary effects at higher state cost. A token bucket provides an average refill rate with an explicit burst allowance; a leaky bucket model can regulate output flow. For example, a service granting ten tokens of burst capacity and adding two tokens per second can permit a short spike without allowing unlimited sustained traffic. Distributed instances need consistent accounting or approximate coordinated limits; purely local counters can multiply effective capacity with the number of application replicas.

Responses should help legitimate clients recover. HTTP 429 signals that too many requests were made; an appropriate Retry-After value can reduce blind retries. If a dependency is slow, immediately retrying every failed call may create a positive feedback loop that worsens overload. Backoff with jitter, bounded queues, circuit breakers, and load shedding can protect the service, but all require careful tuning. A circuit breaker that opens too aggressively can become the cause of an outage. Graceful degradation might serve a cached chapter list while disabling computationally expensive recommendations.

Test both fairness and isolation. Put one client under heavy load and verify that other students retain usable service. Exercise burst patterns around clock boundaries, malformed identities, and retry storms. Monitor rejected requests, accepted throughput, queue depth, and errors; counting only 429 responses can obscure a service that fails before the limiter runs. For administrative users, an exemption should be explicit, least-privileged, and auditable rather than an unbounded bypass. Rate controls turn capacity policy into executable behavior.

### Applied design, experiment, and interpretation

**Case analysis: a campus behind one public IP address.** An API allows forty search requests per minute per IP. Hundreds of students behind a university gateway begin searching before an exam, and many are blocked despite legitimate behavior. A rate limit keyed to verified accounts can improve fairness after login; an anonymous endpoint may need a carefully chosen mixed strategy. Attackers can create accounts or distribute addresses, so account limits alone are not a complete defense. Rate controls should also protect expensive underlying queries and queue capacity.

**Research exercise.** Simulate a token bucket with burst capacity twelve and refill rate three requests per second. Feed requests at irregular intervals and verify token depletion and replenishment. Compare the result with a fixed-window counter at a boundary. Use separate identities in the test and examine fairness: a rate limiter that protects the server but denies a majority of ordinary students may require a different capacity plan.

### Integrated laboratory: threat model for a small academic portal

Define a system with accounts, private student grades, a course forum, file uploads, and an instructor dashboard. Draw boundaries around the browser, internet, reverse proxy, application code, database, object storage, external services, and build pipeline. Mark which actors can influence which data. Students can edit their own forum text, but they cannot authorize themselves to grade peers. A teacher can inspect assigned submissions but should not receive broad access to financial records. Public requests can reach the proxy, but that does not mean they are authenticated or entitled to data.

List abuse cases before selecting controls. A comment might be rendered as executable HTML; a user might alter an object identifier to read another student's submission; a file upload might exhaust processing resources; a remote-image fetcher might reach an internal service; a leaked session token could impersonate a user; and a compromised build dependency might read deployment credentials. Choose controls matched to each flow: safe rendering APIs, server-side authorization checks, size and parser limits, trusted destination restrictions, credential lifecycle controls, and least-privileged CI. A generic firewall is not a complete mitigation for application logic flaws.

Implement a few defensive tests in a local environment. Send ordinary text containing angle brackets and verify that it remains inert when displayed. Use two test users to confirm that a student cannot read another student's file, including through bulk export and background jobs. Test upload size boundaries and temporary-file cleanup. Inspect cookie attributes after login and re-authentication. Check that logout invalidates the promised scope of sessions. These tests should not involve production attacks or real student data; use synthetic accounts and representative records.

Build a rate-limiting exercise around an intentionally low capacity. Compare a per-IP limit with an authenticated per-user token bucket. The first may unfairly affect dozens of students behind one campus NAT address; the second may be evaded by multiple compromised accounts. Demonstrate how the bucket refills and how the server responds to excess traffic. Add bounded retries on a downstream failure and make sure the retries do not intensify an overload. Verify that helpful error messages do not leak stack traces or internal addresses.

Finally inspect the deployment pipeline. Identify which dependencies can execute build scripts, which tokens can deploy, and what changes are allowed from untrusted pull requests. Maintain an inventory of external scripts running in the browser. Use the OWASP Top 10:2025 categories as a vocabulary for review without assuming that category presence alone proves exploitability. Prioritize risks based on likely harm, exposed assets, and actual control gaps. This laboratory connects web data flows to concrete defensive evidence.

### Synthesis: review risks where information changes trust level

A web security assessment should follow information through real transformations. A text comment becomes HTML, an uploaded filename becomes storage metadata, a session cookie becomes an authenticated identity, a resource identifier becomes an authorization decision, and a package update becomes code executed inside a build. Each crossing deserves its own safety invariant. The phrase 'validate user input' is too vague to cover all of them. A SQL parameter, a text node, a restrictive fetch destination policy, and a database-scoped authorization query protect different sinks against different failure modes.

For a small educational portal, identify the highest-impact assets first: private grades, credential recovery, submissions, and authoritative enrollment actions. Then record the attacker-controlled fields and controls applied at each entry point. Negative tests should verify cross-user denial, session expiration, unsafe markup handling, and resource-size limits. Rate limits must also be evaluated for fairness to legitimate users sharing a university network. Dependency and CI privileges matter because attackers may never send an ordinary application request at all. Secure design is a system of explicit trust contracts supported by operational evidence, not a promise that installing a security package will make every route safe.

## Worked questions

### Defend against unsafe forum rendering

A forum stores the text `<b>Hello</b>` from a student. Explain how to show it as literal text and why storing the string safely does not guarantee safe later rendering.

**Separate data and executable markup.** If the intended output is literal user text, set a text node or assign via textContent. The browser then displays the angle-bracket syntax as characters instead of parsing a bold element. This is the appropriate default for comments that do not require rich formatting. The input can be stored unchanged as data if the storage layer handles it safely.

**Trace each output context.** A later administrator dashboard may render the same value inside HTML, an attribute, a PDF template, or a CSV export. Each sink needs context-appropriate handling. Blindly injecting the stored value into innerHTML can turn harmless text storage into unsafe execution. Parameterized database operations protect SQL syntax separately; they do not implement HTML output encoding.

**Specify a defensive test.** Insert representative markup-like strings into a local test account, read them through every presentation path, and assert that they remain inert unless explicitly authorized rich text sanitization applies. Supplement with server-side authorization and Content Security Policy. The purpose is robust data-boundary handling, not demonstrating a live exploit against a production site.

### Evaluate a token bucket

A token bucket starts with 10 tokens and refills at 2 tokens per second. A client consumes 8 immediately, waits 3 seconds, then requests 5. Is the request permitted?

**Calculate remaining capacity.** After consuming eight tokens, the bucket contains two. It then refills at two per second. Three seconds yields six additional tokens, so the candidate balance is eight, below the capacity of ten; no overflow truncation applies in this example.

**Apply the request.** The client requests five tokens and the current balance is eight, so the request is allowed and three tokens remain. If the request had been for nine tokens, it would be denied under a rule that requires enough tokens before deducting any. A real limiter must define discrete versus fractional token arithmetic, clock monotonicity, and concurrency effects.

**State fairness limitations.** A per-IP limiter may unfairly throttle many students sharing one university network. A per-account limit provides a different tradeoff and can be evaded through multiple accounts. The token-bucket calculation describes one idealized capacity policy; it does not guarantee protection from every login attack or overload condition.

### Prevent session reuse

A student logs out of a shared browser. The UI hides their name, but an earlier session cookie remains accepted by the server. Diagnose the defect and propose verification.

**Identify false logout.** Changing a client interface state is not the same as invalidating the credential that the server accepts. A user opening the protected endpoint directly may still receive grades or submissions. This matters especially on devices shared in libraries or laboratories.

**Define revocation semantics.** Invalidate authoritative server-side session state, clear cookies with matching attributes, and send suitable no-store controls for personalized content. If a signed self-contained token is used, document how revocation or short expiry works, including any delay before all copies stop authorizing requests.

**Verify the guarantee.** Log in, capture a test session, log out, then retry an authenticated read in the same browser and a separate context as appropriate. Confirm that private data is denied under the promised policy and check browser cache behavior. Never log the actual session token into an ordinary QA report; record only safe evidence.

