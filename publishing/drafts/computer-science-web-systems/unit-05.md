# Unit 5: Web performance

## 5.1 Caching

Caching reduces repeated work by reusing prior results, but correctness depends on the cache's key, freshness policy, and invalidation behavior. Browser caches, service workers, edge caches, reverse proxies, and application caches can all coexist. A response may be cacheable by one layer but unsafe for another. The presence of a Cache-Control header does not guarantee that every intermediary behaves identically, nor does it remove the need to understand the content's sensitivity. RFC 9111 defines HTTP caching rules, including freshness and validation, while application caches also require domain-specific strategies.

Consider a free textbook chapter that changes monthly. A public cache with appropriate max-age can reduce origin requests substantially. Its ETag lets clients revalidate efficiently after freshness expires. A student's private examination result requires a different policy because sharing a cached representation across users is unacceptable. Query parameters and request headers may affect the cache key; a cache that ignores the edition number in /book?edition=2 can serve the wrong material. Vary can make response selection depend on selected request headers, but careless use causes fragmentation and may not solve every personalization risk.

Application-level caching brings invalidation dilemmas. Suppose a library dashboard caches its count of available seats for sixty seconds. A new enrollment commits to the database, but the dashboard still shows an obsolete count. For a noncritical informational indicator, a short delay may be acceptable if the interface says availability is subject to confirmation. For a payment or booking decision, the authoritative transaction must validate live capacity. Write-through, write-behind, and cache-aside approaches make different consistency and failure tradeoffs. A cache is a performance mechanism, not a substitute for source-of-truth correctness.

Measure hit ratio carefully. A high global hit ratio can conceal a low hit ratio for expensive critical endpoints. Cache misses may cluster after a deploy or key expiration, causing a stampede where many clients request the same costly object simultaneously. Request coalescing, staggered expiration, and controlled stale-while-revalidate can mitigate such effects for suitable data. Before caching, identify what may become stale, who is allowed to see it, and how to remove an incorrect value. Cache invalidation is manageable when its invariants are explicit rather than treated as an afterthought.

### Applied design, experiment, and interpretation

**Case analysis: personalized chapter progress.** The static chapter content is identical for every reader and benefits from public caching, but reading-progress indicators are user-specific. Combining both into one cached HTML response risks leaking another reader's state. Serve a cacheable public chapter representation and load progress through an authenticated no-store endpoint, or use an equivalently safe isolation design. A cache key must incorporate all relevant representation differences, and the system should test the CDN's behavior rather than trusting an origin header alone. After content revisions, ETag validation can limit unnecessary transfers.

**Research exercise.** Request the same chapter as two users and compare edge cache headers and response bodies. Confirm that private progress is never visible to the other user. Simulate a cache stampede after expiration and see whether origin request coalescing limits the burst. Test a chapter revision under an old cached HTML document and determine whether its script and stylesheet assets remain compatible.

## 5.2 Rendering

Rendering is the transformation from application data and code into visible and accessible interface content. Server rendering generates HTML before it reaches the browser; client rendering constructs much of the interface after JavaScript loads; static generation produces pages at build time. Streaming can deliver partial HTML progressively, while hydration attaches client behavior to existing markup. None of these approaches is universally superior. An educational library with thousands of largely stable chapters may benefit from pre-rendered HTML because content becomes visible before application code initializes. An interactive lab can then enhance that page with simulation controls.

Rendering costs must be divided across server execution, network transfer, browser parsing, scripting, style calculation, layout, and paint. A fast server-rendered page can still be slow if hydration executes a large script bundle. A small client-side application can feel responsive after startup but show nothing during a poor initial connection. Route-level code splitting, progressive enhancement, and static content often provide more dependable experiences than extreme reliance on one rendering mode. Interactive elements should reserve layout space before initialization so that content does not jump when scripts load.

Hydration mismatches arise when server and browser render different initial trees. A component that reads the current local time or random identifier during both render phases may produce inconsistent markup. Differences in locale, time zone, authentication context, or feature detection can have the same effect. The fix is to define deterministic initial output, serialize necessary data carefully, and move browser-only behavior into a phase where it cannot invalidate the initial document contract. Sensitive data must not be embedded in public HTML merely to make hydration convenient.

Rendering tests need more than screenshot comparison. Load with JavaScript disabled and check whether the explanatory content is readable. Slow the CPU and network to see whether the interaction remains usable. Verify that navigation and headings have sensible semantics. Compare representative pages on desktop and mobile with the browser performance profiler, not just a stopwatch around a server function. A major design principle for teaching sites is that reading should not depend on the successful loading of every interactive enhancement.

### Applied design, experiment, and interpretation

**Case analysis: a readable chapter before JavaScript.** A dynamic reader originally renders every paragraph from a script after fetching one large course-data file. Under a blocked CDN, students see a blank page. Pre-render each chapter to HTML with the article and worked questions available as normal document nodes, then attach interactive controls after the page loads. The initial HTML can be indexed and read independently of simulation code. A small script initializes only the models visible in the chapter. Reserve simulation slot heights so loading does not shift the text, and keep an explanation if graphics are unavailable.

**Research exercise.** Disable JavaScript and compare content completeness against the enhanced page. Throttle CPU and network, then capture FCP and time until the first slider can be changed. Check for hydration mismatches in console output and ensure that form elements retain correct names. The goal is a progressively enhanced reader, not a claim that every page must use one particular rendering framework.

## 5.3 Asset Delivery

Asset delivery concerns the many files a page needs beyond its initial HTML: stylesheets, scripts, fonts, images, video, and interactive model data. Their sizes, cacheability, compression, and dependency relationships determine much of the page experience. Modern browsers can decode efficient image formats, but the best choice depends on compatibility, content type, and actual file size. A sharp vector diagram may be appropriate as SVG; a photograph usually benefits from raster compression. Responsive images can avoid sending a desktop-sized photograph to a narrow phone, provided dimensions and candidate descriptors are correct.

Bundling requires balance. A single giant JavaScript bundle may reduce request count but causes every reader to download, parse, and execute code for unrelated sections. Thousands of microscopic assets can create other overhead and dependency problems. Split by route and by interaction that actually requires code. Defer noncritical scripts and ensure that critical CSS and fonts do not delay meaningful content unnecessarily. An external CDN can improve geographic delivery but also introduces additional trust, configuration, and availability dependencies. Measure the actual waterfall rather than assuming that a CDN domain guarantees low latency.

Cache-busting usually uses content-hashed asset filenames so that a new release has a new URL. These assets can then be cached for a long period while HTML receives a shorter freshness policy that refers to the current hashes. If HTML is cached longer than compatible scripts and styles, users can experience version mismatches. Subresource integrity can help ensure some externally loaded static assets match an expected digest, but it is not a general substitute for trustworthy dependency management. A service worker needs an explicit update strategy, otherwise it may keep stale assets after a deployment.

An asset budget can be expressed by bytes, requests, and execution time. Suppose a lesson loads a 3 MB illustration, a 900 KB framework, and a 700 KB simulation library. Compressing markup does not solve the image and JavaScript transfer burden. Replace oversized imagery, lazy-load below-the-fold media, and load the simulation only when the relevant chapter is opened. Reserve width and height to prevent layout shift. Test a slow mobile device, where JavaScript evaluation and image decoding may dominate transfer time. Asset performance is a systems question connecting design choices to real user hardware.

### Applied design, experiment, and interpretation

**Case analysis: the overloaded lesson page.** A chapter contains a 4 MB image, a 1.2 MB bundled simulation library, and a decorative web font loaded synchronously. Replacing the image with appropriately sized responsive variants reduces bytes for narrow devices; splitting the simulator bundle by chapter avoids downloading code for unrelated experiments. A content-hashed asset path allows long-lived caching, while the small HTML document can be revalidated more frequently. Reserve dimensions for media and consider fallbacks for blocked third-party services.

**Research exercise.** Inspect resource size after compression and decoded bytes separately. Repeat a cold-cache and warm-cache load at multiple mobile profiles. Compare network transfer savings with JavaScript execution time; a bundle can remain expensive even when compressed. Verify that a cached older HTML page still references files available on the deployment, or use a compatibility window during asset rotation.

## 5.4 Network Latency

Network latency is the delay introduced by propagation, routing, handshakes, queuing, and application processing. Bandwidth and latency are distinct: a connection capable of transferring many megabits per second can still take a long time to respond to a small request if its round-trip time is high. A request that depends on another request creates a serial chain. If a page makes six dependent requests, each paying a 120 ms round trip before useful processing, the latency floor can approach hundreds of milliseconds even when payloads are tiny. Eliminating unnecessary dependencies often helps more than compressing an already small response.

Use an explicit timing model. Total user-visible delay is not just RTT plus server work; it includes connection establishment, request queuing, response transfer, parsing, and rendering. Protocols can multiplex streams and reuse connections, but head-of-line blocking and transport behavior differ among HTTP versions. HTTP/3 maps HTTP onto QUIC, with stream behavior intended to reduce some transport-level blocking, yet it does not remove server overload or application waterfall dependencies. An origin behind a CDN may be physically close to the user while its database is a continent away.

A university platform serving Bangladesh and Europe should measure regional experience rather than relying on averages from one cloud region. A content-heavy library can cache static chapters at the edge, but account actions still reach authoritative services. Moving the application closer to users may reduce RTT but increase replication complexity or operational cost. An edge function that must query a distant database on every request may show little improvement. The architecture must be evaluated end to end, including where session validation and state mutations occur.

Diagnose latency through breakdowns: DNS and connection time, TLS, TTFB, download, main-thread processing, and backend spans. Use percentiles such as p95 to avoid hiding slow experiences behind an average; p95 is a quantile of a specified sample, not a guarantee about every request. Simulate packet loss and mobile throttling in controlled tests, and collect real-user observations with privacy safeguards. Make each proposed change answer a measurable question: which component is slow, under which conditions, and what observed result would justify the added complexity?

### Applied design, experiment, and interpretation

**Case analysis: slow enrollments in a second region.** Students in one region observe a 60 ms median signup request while those abroad see 520 ms. A trace shows several sequential calls from the app server to a distant identity service and database. Merely deploying a CDN in the students' region does not remove these origin dependencies. Reducing redundant sequential calls may improve latency with less operational risk than moving authoritative enrollment writes across regions. Geographic replication could help reads, but conflict handling and data residency must then be considered.

**Research exercise.** Sketch a dependency graph and add measured service times to the critical path. Compare a serial chain with independent parallel calls, noting that independence must be real. Calculate expected bounds before implementing a change, then test p50 and p95 across regions. Watch for retries under packet loss: they may turn a small latency improvement into a worse tail during partial outages.

### Integrated laboratory: performance budget for a digital textbook

Choose a representative chapter containing 50 KB of compressed HTML, 35 KB of CSS, 250 KB of JavaScript, a 600 KB image, and a 100 KB font resource. This is a hypothetical teaching workload, not an observed OpenSTEM measurement. Calculate the total bytes fetched on a cold load using a consistent definition of KB, then ask which bytes are avoidable for students who only want the text. Provide a warm-cache scenario in which the hashed CSS and JavaScript assets are fresh while the HTML is revalidated; calculate the resulting origin and transfer savings. The precise savings depend on cache controls and whether a response can be reused at the browser or edge.

Run the prototype under at least two network profiles and two CPU profiles. Capture a waterfall with request start times, transfer sizes, resource priorities, and response reuse. Follow it with a main-thread trace: JavaScript may consume more time to parse or execute than it takes to download over a fast network. Set a performance budget for page weight and interaction readiness, but do not claim a universal 'fast enough' number that ignores user context. Report p50 and p95 from repeated trials or real-user measurements with suitable privacy controls.

Try one optimization at a time. First replace the oversized image with a responsive candidate and reserved dimensions. Then defer the simulation bundle until the reader opens the experiment. Finally consider static generation for the instructional content. Compare not only cold-load timing but also regressions: does the lazy-loaded model still respond to keyboard focus? Do a cached older HTML page and newly deployed scripts remain compatible? Does a service worker accidentally continue to display a stale chapter? The purpose is to discover tradeoffs through evidence, not to declare every optimization good by definition.

For caching, write explicit policies. A public static explanation may allow shared caching; personalized progress must not be shared between students. An ETag can validate an unchanged representation while saving transfer bytes, but it cannot authorize access. Create two browser sessions with different users and verify that their progress indicators never cross. Measure how a cache stampede behaves when a popular chapter changes after a long freshness period. A controlled stale-while-revalidate strategy might be appropriate for public content, but not for a live seat reservation.

Summarize the design in a performance decision record with baseline numbers, the proposed change, expected mechanism, measured outcome, potential correctness risks, and rollback conditions. If the improvements only affect a synthetic benchmark on a powerful laptop, say so. A responsible web engineer optimizes for the reader who has limited bandwidth and computing resources, while preserving accurate content, privacy, and operable simulation controls.

### Synthesis: performance optimization must preserve correct representations

The fastest wrong answer is still wrong. Caches, pre-rendering, asset splitting, and connection reuse can make a web service responsive, but each introduces assumptions about identity, versioning, and freshness. A public physics chapter is suitable for broad reuse; a personalized exam result is not. A script bundle can be delivered rapidly yet remain expensive to execute on a weak mobile CPU. A server near the user may still depend on a remote database. Avoid choosing optimizations from a single benchmark number divorced from those end-to-end constraints.

Construct a performance decision record for a chapter reader. State what is public, what is private, which assets change with each release, how old HTML and new scripts coexist, and where the critical path lies. Compare cold and warm page loads, because caching can mask transfer and computation costs in a warm local test. Measure the effect of pre-rendering on content availability with scripts disabled. Consider whether a CDN cache key differentiates every representation that must stay distinct. The best change may eliminate an unnecessary remote call rather than buy faster hosting. Quantitative analysis should drive the decision, and correctness tests should prevent the performance improvement from becoming a data-leak or stale-content defect.

## Worked questions

### Estimate a cache transfer saving

A 320 KB static chapter is requested 1,000 times. Assume a valid shared cache serves 900 requests and misses 100; ignore response-header overhead. Compare origin content bytes with no cache.

**Compute the uncached baseline.** Without caching, each of 1,000 requests transfers 320 KB of chapter content from origin. The illustrative total is 320,000 KB, using a decimal convention throughout. This calculation counts origin response-body traffic, not TLS overhead, cache storage, or traffic between browser and edge.

**Compute cache-origin traffic.** With the stated 900 hits and 100 misses, origin sends the body only 100 times, for 32,000 KB. The origin body-byte saving is 288,000 KB, or 90 percent of the baseline. Client traffic may be different because a CDN cache hit still transfers bytes to the end user unless the browser also has a usable local copy.

**Review correctness constraints.** These savings assume a publicly reusable chapter with consistent representation selection. Private student progress must not be included in the shared cached page. Check cache keys, validators, deployment versioning, and invalidation. A high hit ratio is beneficial only when the reused response is semantically correct for the requesting reader.

### Separate critical rendering work

A mobile reader performs 130 ms of server work, 290 ms of transfer, and 900 ms of scripting under a simplified sequential model. What improvement is possible if 700 ms of scripting is deferred after reading becomes possible?

**Calculate the baseline.** Under the stated no-overlap teaching model, the initial readiness total is 130 + 290 + 900 = 1,320 ms. Real browser work overlaps and includes additional rendering stages, so this number is a simplified budget rather than a measured Core Web Vital or a promise of actual user perception.

**Compute the hypothetical result.** If 700 ms of nonessential scripting can be deferred without delaying essential content, the corresponding budget becomes 130 + 290 + 200 = 620 ms. The difference is 700 ms. This is attractive for text reading, but the interactive feature still has startup cost when first requested.

**Validate the tradeoff.** Pre-render explanatory text and worked questions as HTML. When the student opens the simulation, initialize the relevant script and provide a loading state. Profile actual main-thread and interaction timing across mobile hardware. Ensure the deferred component remains keyboard-accessible and does not shift the document unexpectedly.

### Analyze a dependent request chain

Four dependent API requests each pay 100 ms of network round-trip delay and 25 ms of server work. Under a sequential model, estimate critical-path time and explain what parallelism may change.

**Compute serial delay.** Each request contributes an illustrative 100 + 25 = 125 ms, ignoring connection setup, transfer, and other overhead. Four strictly dependent requests therefore contribute 4 × 125 = 500 ms to the critical path. The dependency is what prevents useful overlap, not a universal limit of the HTTP protocol.

**Distinguish independent calls.** If the calls can genuinely run in parallel and have similar duration, the longest may set a lower latency bound near 125 ms rather than 500 ms, subject to server and network contention. However, a call whose parameters depend on a prior response cannot simply be issued early without redesigning the data flow.

**Measure and protect semantics.** Use a trace to identify the actual request dependency graph, then consider combining related data or removing redundant calls. Do not turn an authoritative transaction into eventually consistent reads merely to win a benchmark. Evaluate tail latency and correctness under slow regions and retries, not just one controlled local run.

