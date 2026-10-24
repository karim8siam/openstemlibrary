# Unit 8: Delivery and observability

## 8.1 Deployment

Deployment is the controlled movement of a tested artifact into an environment where users can reach it. A repeatable pipeline builds from a known commit, runs tests, packages immutable outputs, and deploys with documented configuration. Manual editing on a server undermines reproducibility because the running code can diverge from version control. Static-site deployments can publish an entire artifact atomically, but an application with database migrations and multiple services requires coordination. Configuration and secrets must be separated from public build artifacts; a key copied into client JavaScript is public no matter how the source repository is configured.

Deployment strategies have distinct failure profiles. Blue-green release keeps two environments and switches traffic after verification; canary release moves a small fraction of traffic before expanding exposure; rolling release replaces instances gradually. A rollback of application code may be easy, but a destructive database migration may not be reversible. Favor backward-compatible schema changes that permit old and new versions to coexist during rollout. Smoke tests should exercise a representative real interaction, not merely show that the server returns a homepage.

Consider deploying a free textbook platform with newly generated chapters. A clean sitemap must list only published, accessible pages. If the build accidentally exposes editorial drafts, a search crawler can index incomplete or misleading content. A proper deployment check verifies chapter URLs, canonical metadata, robots rules, sitemap entries, and behavior for nonexistent paths. A missing chapter that returns HTTP 200 with the homepage is a soft-404-like defect, even if the visual home page looks correct. Data and navigation should be checked before claiming release success.

Record deployment identifiers, source commits, start and finish times, smoke-test evidence, and rollback paths. Protect production credentials from pull-request builds and avoid permissions broader than the task requires. If a release partially succeeds, communicate which services or routes changed. Never equate 'CI passed' with 'users received the new site'; a CDN can serve an old artifact or a deployment can fail after tests. Deployment is an operational verification process, not the final line of a script.

### Applied design, experiment, and interpretation

**Case analysis: a generated STEM textbook release.** A build assembles static chapter pages and creates a sitemap from the published catalog. An incorrect generator includes unfinished chapter previews with noindex metadata, while the sitemap tells crawlers to discover them. Keep editorial sources outside the deploy output and validate that only finished URLs appear in sitemap.xml. Ensure a nonexistent chapter returns an actual 404 rather than the homepage with status 200. Preview the build artifact separately from production before changing the Cloudflare Pages release.

**Research exercise.** Deploy an immutable staging artifact and compare representative chapter hashes, canonical URLs, headings, interactive scripts, and 404 behavior. Introduce a deliberate malformed sitemap entry in a test branch and assert that CI fails. Write a rollback step using a known-good artifact. Do not alter publication dates for unchanged chapters simply to generate fresh metadata.

## 8.2 Monitoring

Monitoring observes whether a system performs its intended service over time. Metrics summarize measurements such as request rate, error proportion, latency, and queue depth. Logs record discrete events; traces show causal relationships across components. Each answers different questions. A dashboard with many charts is not necessarily effective if it cannot tell operators whether students can log in, read a chapter, or submit an exam. Choose service-level indicators tied to user outcomes, then set objectives and alert thresholds that reflect acceptable performance and available response capacity.

A useful request-latency summary includes quantiles rather than only the mean. The 95th percentile means that approximately 95 percent of observations in the sample are at or below that value; it does not guarantee that every user experiences that delay or identify which individuals are slow. Histograms can support aggregate latency analysis when buckets and labels are chosen sensibly. High-cardinality labels such as full student identifiers can overwhelm metric storage and create privacy risks. Keep personally identifiable data out of telemetry unless clearly necessary and protected under an explicit policy.

Alerts must be actionable. An alert that fires whenever a single request fails may cause fatigue and mask serious outages. Better alerts consider sustained error budgets, important endpoint availability, queue lag, or sharp deviations coupled with supporting signals. Synthetic probes test known flows, but they may miss regional problems or authenticated behavior. Real-user monitoring provides valuable distributional evidence if it is implemented with consent, minimization, and suitable sampling. Traces help explain why a seemingly simple chapter request makes repeated database calls.

Incident diagnosis begins by identifying impact, not guessing the root cause from the first alarming graph. Check recent deployments, dependency changes, resource saturation, geographic concentration, and retry behavior. Preserve timestamps and trace identifiers sufficient to correlate evidence without dumping private request contents. After recovery, review whether monitoring detected the issue, whether rollback was possible, and which architectural assumption failed. Monitoring is most valuable when it changes decisions before users repeatedly report the same problem.

### Applied design, experiment, and interpretation

**Case analysis: silent failure in a course reader.** A deployment returns HTTP 200 for chapter pages, but the simulation initialization throws an exception for every second unit. A basic uptime probe sees a healthy site. Add synthetic interaction checks for a representative slider and solution disclosure, monitor client errors in aggregate, and trace important chapter loads. Keep telemetry free of student answers or private tokens. Alerts should distinguish minor browser-specific presentation problems from a full inability to read or submit work.

**Research exercise.** Create a dashboard with page availability, error rate, p95 chapter loading, and simulation-init failures. Set a service objective and decide what evidence warrants an alert. Simulate an outage after a deployment and evaluate whether operators can identify the source commit and revert safely. A successful restoration also needs validation from the user's perspective.

## 8.3 Automated Checks

Automated checks provide evidence that a system satisfies specified properties. Unit tests verify isolated logic, integration tests exercise service and storage boundaries, contract tests protect interface expectations, and end-to-end tests check selected user journeys in a real browser. No single category replaces the others. A mocked database can verify that a handler requested a transaction while failing to demonstrate whether the actual SQL enforces a concurrency invariant. Conversely, a browser test can pass without exploring malformed API inputs or uncommon race conditions. The test suite must mirror the system's actual failure surfaces.

Property-based testing generates varied inputs to exercise invariants, such as ensuring URL encoding then decoding preserves intended values under an agreed contract. Metamorphic tests compare transformations when exact outputs are hard to predict. For a sorted search response, adding an irrelevant record should not alter the order of existing equal-score items if a stable tie-breaker is specified. Fuzzing can uncover parser and boundary defects. Generated input is valuable, but tests must have independent oracles: a test that repeats the same calculation as the implementation can reproduce the same bug and pass falsely.

Frontend tests should exercise keyboard controls, responsive widths, focus, error states, and script failures. Screenshot comparisons catch visible changes but can be brittle when fonts or dynamic content vary; semantic assertions often provide stronger evidence about behavior. A simulation needs initial-state, reset, edge-value, invalid-value, and numerical correctness checks. For security-sensitive code, negative tests must verify that unauthorized users cannot access data. Build pipelines should fail on consequential regressions, while flaky tests should be diagnosed rather than ignored or endlessly rerun until green.

Testing also has a maintenance cost. Large end-to-end suites can be slow and expensive, and poorly chosen fixtures may stop resembling production data. Use a focused pyramid of cheap deterministic checks supported by representative integration and browser tests. Keep a record of which requirement each check covers and whether a manual review remains necessary. A report stating 'all tests passed' proves only that the tests executed as expected; it cannot establish complete correctness, academic accuracy, accessibility compliance, or resistance to every attack.

### Applied design, experiment, and interpretation

**Case analysis: simulation arithmetic drift.** A JavaScript calculation displays the number of IPv4 hosts for a subnet, but an incorrect implementation returns the total address count without reserving conventional network and broadcast addresses for ordinary prefixes. A test that calls the same helper function as the display can repeat the bug and pass. Use an independently written oracle, test edge prefixes separately, and document when standard special cases apply. Similarly, a rate-limit simulator should verify token-bucket refill from closed-form arithmetic rather than duplicating its internal update loop.

**Research exercise.** Test initial state, multiple input changes, reset, minimum and maximum bounds, invalid values, and narrow viewport overflow. Inject a deliberate implementation error and prove the test suite detects it. Track which educational claims were actually checked, not just how many UI clicks were executed. External academic review remains necessary for the surrounding prose.

## 8.4 Compatibility

Compatibility asks whether a web experience remains usable across browsers, operating systems, input methods, network conditions, and application versions. Web standards give a shared baseline, but implementations differ in release cadence, supported features, storage policies, and security restrictions. Feature detection is usually safer than assuming a browser supports a capability because of its brand or version string. Progressive enhancement begins with essential HTML and adds behavior when support is available. This approach is especially valuable for educational content intended to survive many years.

Consider a physics simulation built around a recent browser graphics API. Some students have older mobile devices or locked-down institutional computers. If the simulation is the only way to understand the lesson, unsupported hardware blocks access to the underlying concept. Provide a meaningful static illustration, text explanation, and worked numeric example. When advanced graphics are available, enhance rather than replace that baseline. Test touch, keyboard, reduced motion, and landscape versus portrait orientations; responsive layout alone is not a guarantee of interaction compatibility.

Backward compatibility matters for APIs too. A deployed mobile application might continue sending an old field name for months. A service release that removes that field immediately can strand users even though the web frontend works. Maintain a deprecation schedule, observe usage of legacy contracts, and test older clients where support is promised. Content migrations can affect bookmarked chapter URLs; stable redirects and clear canonical links preserve navigation and trust. Compatibility must be defined as a supported contract, not an unlimited promise that every historical browser will always work.

A compatibility matrix should list representative browser engines, desktop and mobile operating systems, viewport sizes, network profiles, and assistive technologies. Record specific features under test and define graceful degradation. Check browsers with JavaScript disabled where core content is expected to remain readable. If a feature fails, explain precisely whether it blocks reading, assessment, or only an optional visualization. Engineers should distinguish confirmed compatibility from untested assumptions and update their matrix as software evolves. Long-lived web infrastructure is successful when it remains useful despite changes in user devices and deployment technologies.

### Applied design, experiment, and interpretation

**Case analysis: an old mobile browser.** A new lesson uses a recent JavaScript API for animated graph rendering, but the feature is missing on some institutional devices. Instead of showing an empty page, the application supplies a static graph and fully worked numerical example, with the interactive layer loaded only after feature detection succeeds. Long code samples are scrollable inside their own panels, and all navigation works by ordinary links. A browser-dependent performance optimization should not become a content-access requirement.

**Research exercise.** Build a compatibility matrix for two desktop browser engines and two mobile profiles. Disable JavaScript, reduce motion, block an optional external asset, and increase zoom. Classify any failure as blocking essential reading, blocking an optional simulation, or cosmetic. Record actual browsers and versions rather than claiming universal compatibility based on one test machine.

### Integrated laboratory: a release and observability gate for OpenSTEM

Define a staging build of eight textbook chapters, their simulation assets, and a catalog listing. The generated pages should be readable directly as HTML, with a navigation outline and worked solutions. Simulation models may enhance the reader but should not own the educational prose. Write a repeatable build command that starts from a pinned source revision and produces an immutable output directory. Keep authoring drafts out of the public directory. The release should fail if a source has unresolved placeholders, missing chapters, broken internal links, or inconsistent sitemap and canonical entries.

Design tests at three levels. Unit tests independently check calculations in simulations. Integration tests verify that the page initializes each model and displays the appropriate result for a known input. Browser tests exercise keyboard navigation, slider changes, reset behavior, solution disclosure, and layout across wide and narrow screens. Test a page without JavaScript to ensure the instructional material remains accessible. Use an independent oracle for quantitative results; a model tested against itself offers weak evidence. Record the versions of browsers and libraries used during testing.

Prepare a release check for real HTTP behavior. A valid chapter must return the intended representation and HTTP 200. A nonexistent chapter must return HTTP 404 rather than falling back to the homepage with a misleading status. Each canonical URL must correspond to the published route, and the sitemap must include only finalized pages. Check robots rules and cache headers. If a deployment is behind a CDN, inspect its public URL instead of assuming that a successful build means the latest content is delivered. Preserve the existing publisher advertising configuration rather than modifying unrelated financial settings.

Create basic observability. Measure success rates for chapter loads and simulation initialization, collect aggregated JavaScript errors without personal student data, and time representative page interactions. A synthetic monitor can load one chapter and verify an output, while sampled real-user timing can expose regional or device-specific problems. Set alert thresholds that correspond to meaningful reader impact. Correlate an incident with a deployment identifier and maintain an actual rollback procedure. A red dashboard after a release is useful only if the team knows what action to take.

Publish a final evidence report distinguishing structural pass, numerical pass, browser pass, editorial word count, academic review status, and actual production verification. Those are separate claims. A locally tested 25,000-word manuscript is still not a peer-reviewed or publication-approved textbook. If the repository has a stricter 50,000-word publishing gate, do not silently lower it because a draft meets a separate editorial threshold. The laboratory teaches integrity of engineering claims as much as it teaches build and deployment mechanics.

### Synthesis: published claims must be supported by reproducible checks

Deployment and observability close the loop between development intent and the service readers actually receive. A test suite may validate calculations in isolation, yet a chapter deployed to the wrong path can still be unavailable. A browser interaction may work locally, yet the public CDN may continue serving outdated assets. Conversely, a site can respond with 200 while scripts fail for every simulation. Build and runtime verification therefore belong to different evidence categories, which should be reported separately rather than merged into one 'all green' status.

For an educational release, maintain a specific checklist: each authored unit exists, static content is readable, navigation and canonical URLs are coherent, a nonexistent route returns 404, the sitemap lists only intended published pages, and the simulated calculations match independent oracles. Test at least one desktop and one mobile browser interaction. Document scripts blocked by network failures and any loss of essential explanatory content. Preserve versioned release artifacts and a realistic rollback path. If specialist academic review has not happened, say so even when all software tests pass; a program cannot certify every scientific explanation merely by executing successfully. The professional habit to learn is calibrated evidence: make only the claims that the tests and reviews actually support.

## Worked questions

### Verify a chapter deployment

A build publishes chapter pages and generates sitemap.xml. A nonexistent chapter returns HTTP 200 with homepage HTML. Explain why this is wrong and design a test.

**Identify the response mismatch.** A missing resource should not be represented as a successful chapter page. Returning HTTP 200 with unrelated home content confuses clients, accessibility expectations, and search discovery, and may be classified as a soft 404. A real 404 response better expresses that the requested chapter does not exist.

**Design the release check.** Deploy to staging, fetch a representative published chapter and verify HTTP 200, canonical URL, expected heading, and readable content. Fetch an intentionally nonexistent chapter and assert HTTP 404. Also check that sitemap entries correspond to real published routes and do not list unfinished noindex editorial previews.

**Preserve rollback evidence.** Record the source commit and immutable output artifact. If deployment tests fail, stop promotion or roll back to the verified artifact. A passed unit-test suite cannot prove that CDN routing and public HTTP behavior are correct. Do not change publication dates on otherwise unchanged chapters simply to refresh a sitemap.

### Interpret p95 latency

A monitoring window contains 200 requests. Its empirical 95th-percentile latency is 900 ms. Explain what that means and what it cannot establish.

**Interpret the sample quantile.** The percentile describes an order statistic or interpolated quantile depending on the monitoring method. Roughly 95 percent of observed requests in the measured window were at or below around 900 ms. The exact interpolation and boundary observation depend on the method and histogram resolution.

**Avoid a false guarantee.** The metric does not guarantee that every future request completes within 900 ms, identify which students experienced the slowest responses, or establish whether the sample represents all regions and device classes. A small or biased sample can conceal the groups with the worst experience.

**Choose useful supporting signals.** Combine latency quantiles with request rates, error proportion, geographical breakdown where privacy-safe, and traces that explain expensive operations. Define an alert when a meaningful objective is persistently breached rather than treating one p95 measurement as proof of global system health. Correlate observations with deployment changes.

### Test a simulation independently

A calculator displays total capacity as requests/second multiplied by worker count. Describe how to test its arithmetic and browser controls without reusing the same buggy implementation as its oracle.

**Build a separate numeric oracle.** For a simplified model with five workers processing eight requests per second each, expected aggregate capacity is forty requests per second under ideal independent conditions. Compute this using an independently written formula or trusted test data, not by calling the same JavaScript function that drives the display.

**Exercise the interface.** Load the local chapter in a browser, change worker and per-worker rate controls, and assert that the visible output changes correctly. Reset and verify that the original values return. Test minimum, maximum, and invalid numeric values, as well as keyboard control and a narrow viewport.

**Qualify the model.** The calculation assumes no shared database bottleneck, contention, retries, or variable processing time. The simulator is pedagogical, not a performance prediction for a real web service. Document these limits beside the controls and never claim production capacity solely from the model output.

