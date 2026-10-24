# Unit 3: System testing

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 3.1 User Journeys

### Core reasoning and definitions

A user journey is a sequence of meaningful interactions undertaken to achieve an outcome, not merely a sequence of pages. The path includes preconditions such as identity and enrollment, transitions such as opening a course and submitting a quiz, and observable end conditions such as a durable confirmation. A realistic journey also describes what should happen when a user returns, uses the back button, loses connectivity, or has insufficient permissions. Journey tests bridge product requirements and technical interfaces. They are valuable because many defects occur between individually working components: a score may compute correctly but fail to persist, or a payment may commit while the confirmation screen shows failure. Test journeys should be selected by impact and risk rather than attempting all combinations of screens.

### Original investigative exercise

For a student account, trace registration, email verification, login, course selection, quiz submission, and result review. Seed a student with no prior attempts. Assert the final server-side result belongs to the authenticated student and remains after a new login, not just that a success banner appears. Introduce a network drop immediately after submit and investigate whether refresh duplicates an attempt. Explore the denied path when a visitor opens the result URL without authorization. Keep a diagram linking visible states with backend transitions. Include expected accessible labels and keyboard controls in the journey record.

### Limits and counterexamples

A single “happy path” passing through every screen is still one sample. It cannot justify claims that invalid accounts, slow connections, and session expiration all behave correctly.


### Deep dive: observability and diagnosis of whole-system failures

A web interface, server API, background worker, and datastore may all independently report healthy status while the student fails to achieve a goal. A student clicks Enroll and the page says Confirmed; the server writes a temporary request record; the worker drops the queue message; the enrollment never becomes durable. End-to-end testing must therefore define a clear end state and a means of observing it. One practical approach assigns a synthetic transaction identifier to the test and carries it across request logs, queue events, and database records. A test should not require reading private developer traces to decide success, but traces are valuable for diagnosing a failure after a public oracle detects it.

Build an evidence tree. The browser layer asserts that controls are exposed with useful names, input validation gives clear feedback, and successful submission shows a transaction reference. The API layer asserts that the reference corresponds to an authenticated learner and an accepted request. The durable-state layer asserts the final enrollment exists exactly once and obeys capacity constraints. The background-processing layer asserts that notification attempts and audit records follow the declared delivery contract. Failure in the final state is a real user-impacting defect even if all intermediate layers returned successful transport statuses. Conversely, a notification email failing may not invalidate enrollment if the contract explicitly treats email as optional.

A service spanning regions raises timing questions. An enrollment write can commit in one region and become visible to a read replica later. If a test immediately queries the replica and sees no row, it may report a false defect unless the product promises strongly consistent reads. Specify a measurable visibility bound, and point the test at the correct observation interface. A model that says “the row must appear eventually” without a finite operational bound makes automated acceptance difficult, because no finite wait can prove it never will. Choose service-level thresholds that reflect user experience and can be measured under controlled conditions.

Reproduce failures systematically. Capture a deterministic seed for generated form values, a clean database fixture, feature-flag states, server and browser versions, and a relative event timeline. Use network interception to drop exactly one request or to delay its response; avoid changing production traffic. A screenshot can document wrong visual state, but it cannot prove backend correctness. A trace can document a submitted request, but it cannot prove the UI announced completion accessibly. Evidence should join observations from independent surfaces without confusing them.

Accessibility creates additional system-level failure modes. An enrollment modal might trap keyboard focus, lose focus after a validation error, or announce only “invalid” rather than identifying the form field. Automated DOM checks catch some semantic defects, yet may miss an unusable focus sequence. Test the journey with the keyboard at increased text zoom and at narrow viewport widths. Screen-reader smoke testing should sample representative controls and transitions. Use synthetic profiles; exposing live student data in recordings is unnecessary and risky. For an interface localized into multiple languages, test that error messages remain understandable and that date and number formatting follow the chosen locale rather than browser defaults.

Browser matrix testing needs purposeful selection. Different layout engines interpret some CSS, form elements, and text metrics differently, so a single Chromium viewport cannot establish universal compatibility. Prioritize supported combinations based on audience evidence, then use representative cases for Safari and Firefox, Android touch behavior, and slower devices. Characterize any unavailable platforms explicitly. Testing every possible browser version is infeasible, and claims of “all-device compatibility” are weaker than a documented, maintained support matrix.

Finally connect release findings to production monitoring. A synthetic journey might run every few minutes against a safe test tenant and assert that enrollment reaches a terminal state within the agreed bound. Alerts need actionable context: failed checkpoint, request identifier, observed latency, and version. They should not expose student data or flood operators when an external dependency is known to be down. An end-to-end test suite and observability system complement each other: tests explore controlled faults before release, while monitoring detects behavior under actual workloads that no finite laboratory matrix can reproduce exactly.


### Unit synthesis: independent evidence from one user journey

Trace one synthetic enrollment from the first keyboard action through durable confirmation. The first observation concerns interaction: whether users can discover and operate the form, including assistive-technology users. The second concerns protocol: whether the authenticated request has the expected schema and response semantics. The third concerns committed state: whether capacity constraints and unique enrollment guarantees hold. A screenshot is useful for visual evidence but not proof of durable state; a database row confirms persistence but not keyboard accessibility. When an asynchronous projection is involved, identify the precise visibility guarantee and poll that condition with a bounded timeout. If it fails, preserve diagnostic evidence and distinguish contract violation from instrumentation delay. A competent system test explains why the suite covers the observed user outcome and which environments, browsers and disability-related interactions remain untested. Avoid expansive claims such as “all devices supported” from one local Chromium session.

## 3.2 End-To-End Tests

### Core reasoning and definitions

End-to-end tests exercise a representative path across the system's actual boundaries, often using a real browser, API, database, and deployment-like configuration. They can detect mismatched routing, missing assets, incompatible authentication cookies, and persistence defects missed by isolated tests. Their breadth makes them valuable but also expensive and harder to debug. Use a small, high-value suite grounded in stable user outcomes, and keep most combinatorial logic checks at lower levels. Every end-to-end test needs predictable setup, a clear success condition, and cleanup. Favor semantic element locators and observable state transitions over brittle fixed sleeps. Waiting for an arbitrary number of milliseconds can both slow the suite and fail on a heavily loaded machine.

### Original investigative exercise

Automate a course purchase in a local sandbox using a fake payment gateway with realistic authorization and settlement callbacks. Check that two browser windows attempting duplicate checkout do not create duplicate orders. Wait for a specific receipt state with a reasonable upper bound, not a fixed three-second pause. Capture browser console errors, network failures, and server correlation IDs when an assertion fails. Rerun with a narrow mobile viewport and keyboard-only interaction, and isolate whether a failure comes from transport, UI, backend, or fixture. Keep payment operations synthetic; do not test by charging real cards.

### Limits and counterexamples

A green end-to-end suite using only mocked APIs cannot prove the actual database and authentication configuration work. Equally, a suite that depends on production account data is not reliable evidence of release quality.


### Applied laboratory: a student registration journey across browsers and assistive technologies

A student registration portal can appear correct to developers using a mouse and a high-speed desktop browser while failing for keyboard users, mobile devices, and unstable networks. Describe the journey in terms of learner goals: discover an available course, inspect prerequisites, sign in, enroll, and obtain durable confirmation. The portal might permit wait-list enrollment after capacity is reached, but that policy must be explicit. Define successful completion not as a green toast but as a valid enrollment tied to the correct student and course in persistent records. Build a trace identifier that joins browser actions to backend logs without revealing personal details in public test artifacts.

Divide the journey into checkpoints that reveal different failures. Discovery verifies that search results match the chosen course. Authentication verifies an accessible login path and correct redirect. Enrollment verifies capacity, prior-registration constraints, and transactional state. Confirmation verifies an identifier that can be retrieved after page refresh and after a browser restart. Recovery verifies the result after the client connection drops immediately following submission. This last case is essential: the browser may believe the request failed while the server committed it. An idempotent retry should not create a duplicate enrollment. Each checkpoint needs an oracle, and not all oracles should depend on the same frontend code that performs the action.

Run the journey first in a narrow desktop test environment with a seeded course and frozen clock. Then use a phone-width viewport with a slower network profile and content zoom. Horizontal overflow, obscured actions, inaccessible navigation panels, and stale loading indicators are real functional defects for the user. Verify focus order by tabbing through the form, not merely checking that elements have labels in the DOM. Trigger a validation error and confirm that the error is announced through an appropriate live region or descriptive association. Ensure the next interactive action is discoverable without a mouse. Color contrast checking is useful, but passing a contrast ratio does not guarantee a logical heading hierarchy or correct keyboard behavior.

Separate automated accessibility checks from manual assistive-technology evaluation. Automated tools can detect missing form labels, duplicate identifiers, some contrast failures, and invalid ARIA relationships. They cannot reliably judge whether a label is informative, an instruction makes sense, or a complex modal workflow is usable with a screen reader. Include a documented keyboard-only traversal and a screen-reader smoke test in the release plan; do not write “fully accessible” because one checker returned no violations. Browser compatibility also has scope: specifying current stable Chrome, Firefox, and Safari is more meaningful than saying “all browsers,” and a supported-version matrix should be reviewed as users change devices.

Introduce a deliberately flaky condition: the confirmation endpoint becomes visible only after an asynchronous event. A test that sleeps for two seconds sometimes passes and sometimes fails under load. Replace the blind delay with polling for a specific durable state using a bounded timeout. If the system's consistency contract allows an eventual update within 20 seconds, measure and assert that the condition becomes true within that bound. Record the time budget in the test plan rather than hiding it in helper code. Distinguish a genuine service latency regression from the test runner starving the application process of resources.

At the end, produce an evidence packet: exact application build, browser versions, device dimensions, seeded dataset identifier, test timestamps, accessible interaction transcript, and backend trace. Capture only synthetic student accounts and sanitize session tokens. If a screenshot shows the interface after a click, attach a state assertion that proves the enrollment persisted. If a screen reader announces the wrong label, keep that observation separate from the backend success. Successful system testing joins evidence from multiple layers; it does not equate visual appearance with correctness.


## 3.3 Accessibility Checks

### Core reasoning and definitions

Accessibility testing examines whether people with different sensory, motor, and cognitive needs can perceive information and operate the product. Automated rules can catch missing labels, some contrast violations, structural errors, and incorrect ARIA syntax, but they do not establish that an interaction makes sense to a screen reader user. Keyboard focus order, error recovery, visible instructions, timing controls, and alternatives for visual-only information require direct interaction tests. WCAG defines testable success criteria, yet claiming full conformance needs an appropriate evaluation process and scope. For an educational simulation, the numeric state should be available as text and controls should have meaningful names, range, and units. A graph that changes with a slider may need a textual interpretation of its trend and limitations.

### Original investigative exercise

Inspect a lesson reader at 320 and 1280 CSS pixels, with browser zoom increased, keyboard navigation, and reduced-motion preferences. Move the simulation slider using arrow keys and confirm that the displayed value and result can be understood without seeing its colors. Expand a worked solution and check that the button exposes its current state and that focus is not lost. Deliberately remove the input label in a local copy; a static checker should flag it, while a manual check confirms the user-facing cost. Log each issue against a specific interaction and success criterion rather than treating an overall score as proof of usability.

### Limits and counterexamples

A screenshot with beautiful layout can hide broken focus order or inaccessible canvas content. A screen reader announcing a button name does not prove that the button's subsequent feedback is usable.

### How to interpret the interactive model: journey coverage

A system journey is a learner-observable path, such as course discovery through confirmed enrollment. This model defines a finite inventory of twenty-four named scenarios and lets the user change how many have been executed. Six exercised scenarios give 25 percent scenario coverage. The choice of twenty-four is illustrative, not a universal count for an education platform. A scenario can be executed yet fail, and two nominal scenarios may have identical underlying paths. Checkpoints within a journey can fail independently; counting one browser success does not demonstrate correct database persistence. A useful scenario catalog separates authentication, capacity edge cases, interrupted submissions, access needs, and recovery. The model cannot judge whether missing paths are low or high risk. Combine its count with a traceability table and evidence of outcomes, not an unqualified badge of quality.

## 3.4 Compatibility

### Core reasoning and definitions

Compatibility testing studies whether a feature behaves as promised across supported browsers, operating systems, device dimensions, locales, APIs, and network conditions. Compatibility is an explicit support policy rather than an attempt to test every possible environment. Record which behaviors rely on standardized platform features and which degrade when an API is missing. Test feature detection before use, fallback content for unsupported capabilities, and the distinction between a browser engine and a particular device brand. Locale differences can affect decimal parsing, sort order, date displays, font metrics, and text expansion. Network conditions affect the timing of requests, offline behavior, and progressive rendering; browser storage may be disabled or partitioned in some contexts.

### Original investigative exercise

Exercise a university application form in Chromium and Firefox at both narrow and wide viewports, then set language preferences and simulate a slow network. Enter a birth date near a daylight-saving transition using an explicit date-only domain representation to avoid accidental time-zone shifts. Verify that a dropdown remains operable without touch gestures, that error text does not overflow, and that the form's submitted payload follows the same schema. Deliberately disable local storage and confirm optional preferences fall back safely rather than preventing login. Record actual versions tested and do not imply other versions were covered.

### Limits and counterexamples

Testing one desktop browser at two widths does not establish mobile-device compatibility. An emulator can mimic viewport dimensions but may miss virtual keyboard, accessibility-service, and browser-specific behavior.

### How to interpret the interactive model: contrast ratio

The contrast model compares a chosen foreground relative luminance to a white background of luminance one. It computes (1.05)/(L+0.05) because the background is brighter. With foreground luminance zero, ratio 21:1 is maximal for this pair; with luminance 0.18, ratio is approximately 4.565:1. The boolean indicates whether the numerical threshold 4.5 is crossed in this simplified scenario. Actual interfaces have variable backgrounds, overlay opacity, anti-aliasing, state changes, and text sizes, so this slider cannot establish complete accessibility. Luminance must already be linearized from sRGB; plugging ordinary 8-bit component values into the ratio directly is mathematically wrong. After numeric experiments, test labels, semantic relationships, keyboard focus, screen-reader announcements, and touch target behavior as independent properties.

## Fully worked questions

### Worked problem 3.1: User Journeys

An enrollment button returns HTTP 200 but no enrollment row is committed. Explain three distinct assertions needed to detect this defect and a retry scenario that might hide it.

**Define the property and assumptions.** The browser assertion should check an accessible confirmation associated with the submitted course and authenticated learner, not just HTTP status. The backend contract assertion should verify that the response identifier is a valid persisted enrollment and that its foreign keys identify the correct entities.

**Compute or execute the reasoning.** Query the database through an independent observation path after the operation reaches its stated consistency boundary. Expect exactly one active enrollment row. Drop the connection immediately after sending the request and resend with the same idempotency key; the outcome should create at most one active row and ideally return the same logical result.

**Interpret the conclusion and limitations.** A front-end mock can fabricate both the 200 and confirmation text while hiding the persistence defect, so the integrated test must exercise the actual write path. Avoid arbitrary sleep as synchronization; poll a documented durable condition within a bounded deadline. Record real failures rather than retrying until a green screen appears.

### Worked problem 3.2: End-To-End Tests

For black text of relative luminance zero against white of luminance one, compute the contrast ratio. Repeat for text luminance 0.18. Is a passing ratio sufficient evidence of accessibility?

**Define the property and assumptions.** Use the WCAG relative luminance contrast formula (Llighter+0.05)/(Ldarker+0.05), with luminances already correctly computed from linearized sRGB. For absolute black and white, the numerator is 1.05 and the denominator is 0.05.

**Compute or execute the reasoning.** Black on white yields 21:1. Text luminance 0.18 on white yields 1.05/(0.18+0.05)=1.05/0.23, approximately 4.565:1. These ratios reflect an idealized specified pair, not necessarily every rendered pixel, antialiased boundary, or overlaid translucent component.

**Interpret the conclusion and limitations.** Even when the threshold for ordinary text is met, the form may lack informative labels, logical focus order, keyboard operability, and correct semantic grouping. Follow automated checks with keyboard traversal and assistive-technology evaluation. Specify font size, background, and interaction state when recording contrast evidence.

### Worked problem 3.3: Accessibility Checks

A confirmation endpoint is eventually consistent with a stated bound of 10 seconds. Replace a fixed sleep with a sound test wait, and interpret a state observed after 11 seconds.

**Define the property and assumptions.** Capture the operation token and start the timer at the documented event boundary. Poll a reliable server-visible committed state at a reasonable interval, such as 200 milliseconds, without assuming the first response means the projection is current.

**Compute or execute the reasoning.** If the expected state appears within ten seconds, the bounded timing assertion passes. If it first appears at eleven seconds under valid test conditions, the stated bound is violated even though the operation eventually succeeded. A fixed sleep for twelve seconds would mask the regression and slow every successful execution.

**Interpret the conclusion and limitations.** Measure clock synchronization and test-runner scheduling delay before declaring a product defect. Distinguish eventual-consistency allowance from an unlimited liveness promise. A timeout is an observation about this run and contract, not proof that the state can never converge.

