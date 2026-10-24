# Human–Computer Interaction — Unit 3: Interaction Design

**Editorial teaching draft.** Examples are constructed to teach design reasoning. Any timings, costs, or failure probabilities are explicit assumptions, not measurements from real users.

## Learning outcomes

The reader should be able to distinguish a possible action from a signifier that communicates it; model a control as a state transition with appropriate feedback; organize navigation around tasks and information scent; design recovery for recoverable and irreversible errors; and evaluate a workflow using explicit success criteria. Two bounded simulations illustrate the accumulation of independent per-step failure risk and the capacity cost of retaining undo history. Neither simulation is an empirical prediction of how a particular user will behave.

## 3.1 Affordances, signifiers, and mappings

### What an interface permits is not the same as what it communicates

An affordance is a possible relationship between a user and an object or system. A physical door may be pushable; a digital file may be selectable, movable, or shareable. A signifier is a perceptible cue that helps the person recognize an available action. A handle suggests pulling, a labeled button suggests activation, and an underlined link suggests navigation. Digital interfaces often hide their true capabilities behind a visual layer, so signifiers become especially important. A rounded rectangle that resembles a button may do nothing; a plain text label may be clickable without looking interactive. Both cases break the user's expectation and create avoidable uncertainty.

Consider a university course portal with a small download icon beside each assignment. The icon may mean download the instructions, export the submission, or save an attachment. The action is technically possible, but the signifier is ambiguous. A text label such as *Download assignment brief (PDF)* reduces the need to infer the icon's meaning. For icon-only controls, accessible names are essential for screen-reader users, and visible tooltips can help sighted users, though a tooltip that appears only on hover excludes some touch and keyboard interactions. A control should communicate its purpose through more than a decorative shape.

Mappings connect an action to an outcome. A volume slider whose handle moves right as sound increases has a conventional spatial mapping. A timetable control that shows the next week when the user presses a right arrow also follows a familiar temporal mapping. Problems arise when controls use a mapping that conflicts with their labels or context. A toggle labeled *Email notifications* should make its on/off state clear; an unlabeled switch that moves without feedback leaves users uncertain whether notifications are enabled. Avoid treating visual convention as universal. Cultural reading direction, device norms, and prior experience can influence expectations, so testing remains necessary.

Constraints can prevent mistakes by limiting available actions. A date picker can disable impossible past dates when future booking is required. A submit button can be unavailable until required fields are valid, but a disabled button without explanation can trap the user. Show which requirement is unmet and how to resolve it. Constraints should follow the task model rather than arbitrary implementation convenience. Preventing the user from editing a reservation after submission may simplify code but create expensive support requests. A safe, bounded edit window can be more useful than a permanent lock.

The relationship between signifiers and feedback is temporal. Before an action, a signifier indicates what can be done. During an action, progress or a pressed state indicates that input was received. After an action, feedback communicates the result. A button that changes color when clicked but never confirms whether a payment succeeded gives feedback about the click, not about the transaction. Designers must identify which state the user actually needs to know. In a financial transfer, *request sent*, *processing*, *completed*, and *failed* are different states with different consequences.

### Evaluate discoverability through tasks

A discoverability study should give a participant a goal, not an instruction to press the control under examination. Instead of *Click the blue button to download your transcript*, ask *How would you obtain a copy of your transcript for a scholarship application?* Observe the first choice, detours, hesitations, and interpretations of labels. A person who eventually succeeds after opening four unrelated menus has technically completed the task but revealed weak information scent. A person who cannot find the action may have encountered an accessibility barrier, a terminology mismatch, or a navigation problem. Record these separately before proposing a fix.

Designers often confuse aesthetic simplicity with cognitive simplicity. Removing all labels can make a toolbar look cleaner while requiring users to memorize icons. Conversely, showing every action simultaneously can overwhelm the primary workflow. Progressive disclosure is useful when secondary controls can be revealed without hiding essential actions. For a course portal, *Submit assignment* should remain prominent; advanced export settings may be behind a clearly labeled disclosure. The right balance depends on user frequency and task consequences. An expert workflow may benefit from shortcuts while novice users need visible alternatives.

## 3.2 Feedback, system status, and state machines

### Model the system before choosing the animation

Feedback tells the user what the system has recognized and what happened as a result. It is most reliable when it reflects the underlying state rather than a cosmetic effect. Consider an online exam answer. The interface may move through *edited locally*, *queued for sync*, *received by server*, and *confirmed saved*. These states should not all be displayed as a generic green check. A green check immediately after local editing may mislead a student into thinking the server has stored the answer. A state model forces the team to decide what is true, which transitions are allowed, and what the interface can safely promise.

A simple state machine has states, events, guards, and transitions. For example, *draft* moves to *submitting* when the user presses Submit, but only if validation succeeds. *Submitting* moves to *confirmed* when the server acknowledges the request; it moves to *retryable error* on a network failure. The user may return from *retryable error* to *submitting* without re-entering data. The design should also specify what happens when a late server response arrives after the user navigates away. State-machine reasoning exposes cases that a single happy-path wireframe misses.

Feedback has several dimensions: immediacy, specificity, visibility, persistence, and accessibility. A quick toggle may need only a changed state and a short announcement to assistive technology. A multi-minute upload needs progress information, the ability to cancel when feasible, and a durable result. Avoid fake progress indicators that suggest certainty the system does not possess. When exact completion cannot be estimated, an indeterminate indicator paired with a meaningful status message is more truthful than a countdown that repeatedly resets. Feedback should not disappear before the user can read it or rely only on color or sound.

Repeated actions can create duplicate consequences. If a student presses Submit twice during a network delay, a naive backend might create two submissions or charge twice for a paid application. A good interface disables or guards the action while the first request is in flight and explains why. More importantly, the server should support idempotency where duplicate requests are dangerous. Frontend feedback cannot compensate for an unsafe backend. The user-facing state should be consistent with the actual transaction record, and the interface should offer a way to inspect the final status.

### Design failure states as carefully as success states

Error messages should state what failed, what was preserved, and what the user can do next. *Something went wrong* is rarely enough. A better message might be *Your answer is saved on this device but has not reached the server. Keep this page open or retry when your connection returns.* This message is appropriate only if local persistence actually exists. A design must not promise recovery it cannot deliver. Likewise, telling a user that a reservation failed without saying whether a room was held can cause repeated bookings and support calls.

A useful failure taxonomy separates user input errors, recoverable system errors, permission problems, and irreversible failures. For a form validation error, preserve correct entries and identify the field with a clear explanation. For a network timeout, retain state and provide a safe retry. For an expired session, explain whether unsaved work survives reauthentication. For an irreversible deletion, present consequences before the action and provide recovery if technically possible. Different categories need different interaction patterns; a single red toast is not a complete error strategy.

Test feedback with interpretation questions. After an action, ask *What do you believe has happened?* and *What would you do if you closed the page now?* The participant's explanation reveals whether the interface communicates the intended state. Observe behavior when latency is injected, when a request fails, and when a confirmation arrives late. A design that looks polished under instant success can fail catastrophically when the network is unreliable. Testing state transitions under adverse conditions is therefore a central part of interaction design, not a late engineering detail.

## 3.3 Navigation, information architecture, and wayfinding

### Structure information around goals and recognizable labels

Navigation helps users answer three questions: where am I, what can I do here, and how can I reach the next relevant place? An information architecture organizes content and actions so those questions have coherent answers. For an academic portal, possible top-level destinations include courses, assessments, grades, and account settings. But the appropriate grouping should be tested with the intended audience. A developer may group features by backend service, while students think in terms of tasks such as *submit an assignment* or *check feedback*. Technical module boundaries rarely make good navigation labels by themselves.

Information scent is the extent to which a label or preview suggests that a path leads toward the desired information. A menu item labeled *Resources* may be too vague when the user needs a laboratory manual. *Lab manuals and worksheets* gives a more specific clue. Avoid labels that are meaningful only to the organization, such as internal project acronyms. A navigation hierarchy can be deep if categories are predictable, and shallow navigation can still be confusing if labels overlap. Counting clicks alone is a weak measure; error rate, hesitation, confidence, and recovery effort also matter.

A breadcrumb can show the relationship between a current page and its parent categories, but it should not be used to excuse a confusing hierarchy. Search supports users who know a target term, while browsing supports those who need to discover options. Both need meaningful results and recovery from empty states. A search box that silently returns nothing for a common synonym may be less useful than a simple, well-labeled category page. Search logs can reveal vocabulary mismatches when collected lawfully and interpreted carefully, but they cannot explain every user's intent.

Navigation must remain usable across devices and input methods. A hover-only submenu is inaccessible to touch users and can be difficult for keyboard users. A mobile menu should expose its expanded state, keep focus management predictable, and allow users to return to content without losing their place. Sticky navigation may help orientation but can consume valuable screen space, especially when a virtual keyboard is open. Test the actual viewport and interaction mode rather than assuming a responsive layout is usable because it does not overflow horizontally.

### Compare alternative structures experimentally

Card sorting asks participants to group items in ways that make sense to them. Open card sorting can reveal vocabulary and category patterns; closed card sorting tests a proposed taxonomy. Tree testing presents a navigation structure without the visual design and asks users to find a destination. These methods isolate different questions. A card sort does not prove that the resulting navigation will work in a complete interface, and a tree test cannot reveal every visual affordance problem. Use the methods as evidence within a broader design process.

Suppose a team tests two navigation structures for finding an assignment rubric. In structure A, 14 of 20 attempts reach the correct destination; in B, 17 of 20 do. Observed success rates are 70% and 85%, a 15-percentage-point difference. The sample is small, and participants may differ between conditions. A difference in observed proportions is not automatically evidence of a population-level effect. Randomization, within-person order control, task variation, and uncertainty intervals would improve inference. Qualitative path traces can still show that the label *Assessment criteria* is clearer than *Course administration*.

Wayfinding also involves continuity. If a student opens a rubric, returns to the assignment, and loses their partially entered answer, the problem is not merely navigation. It is state preservation. A design should support back navigation, deep links, and meaningful browser history without accidentally repeating irreversible actions. Pages should have distinctive titles and headings. A user arriving from search or a shared link should understand context without first visiting the homepage. This matters for accessibility, reliability, and ordinary web usability.

## 3.4 Error prevention, undo, and recovery

### Prevent high-cost mistakes without creating new traps

Error prevention reduces the chance that a user makes an unintended action. For a payment, show the amount, recipient, and currency before final confirmation. For a file deletion, distinguish moving to trash from permanent erasure. For a laboratory control, display units and safe bounds. Prevention should be proportional to risk. Confirming every harmless preference change creates fatigue and teaches users to dismiss dialogs automatically. High-consequence, low-frequency actions justify stronger safeguards than reversible cosmetic changes.

Undo provides a different kind of protection. Instead of interrupting an ordinary action with a confirmation, the interface may allow immediate reversal. This is effective when reversal is genuinely possible and the user can discover it. A deleted draft might remain in trash for a documented retention period; an edited text field may have an undo history; a sent email may have a short cancellation window before transmission. Do not label an action *Undo* if it merely sends a compensating request that can fail without explanation. Recovery semantics must be precise, especially when external systems or other people are affected.

Good recovery preserves context. When a student uploads an unsupported file, the page should retain the assignment selection and explain the accepted formats and size limits. If a booking slot disappears during checkout, show nearby alternatives while preserving group size and accessibility filters. Resetting the entire workflow may be easy for developers but expensive for users. Recovery should also be accessible: error summaries need to be perceivable, linked to affected controls, and reachable by keyboard. A screen-reader user should not have to scan the whole form to discover a new validation message.

Error prevention can be evaluated by constructing representative failure scenarios. Test an invalid date, a dropped network connection, a duplicate click, an expired session, a full storage quota, and a partially completed form. Observe whether the user understands the outcome and can continue without losing important work. Record both successful recovery and unsafe assumptions. If a participant thinks a payment failed and retries when it actually succeeded, the interface has a potentially serious state-communication problem even if the transaction backend behaved correctly.

### Evaluate risk without mistaking a toy model for evidence

A simple teaching model assumes n independent workflow steps, each with identical error probability p. The probability of at least one error is 1-(1-p)^n. This illustrates why adding steps can increase cumulative opportunities for error under the model's assumptions. It does not establish that every real additional step is harmful: a verification step can reduce a more serious downstream error. In practice, errors are correlated, probabilities vary by step, and interface safeguards change behavior. Use the model to discuss assumptions, not to justify removing all confirmation screens.

Undo history also has engineering costs. Suppose an editor retains a fixed 64 KiB snapshot for each action and holds n snapshots. A naive storage estimate is 64n KiB, excluding metadata and compression. That makes the tradeoff visible but ignores real implementation strategies such as storing differences, coalescing edits, and limiting history by age or memory. The user-centered requirement is not a particular snapshot count; it is a reliable ability to recover from plausible mistakes within resource limits. Performance and recovery testing should accompany any optimization.

An integrated design review should connect affordances, state feedback, navigation, and recovery. Imagine a student who cannot find the submission control, eventually presses it twice, sees an ambiguous success icon, and then discovers that the wrong file was attached. Each symptom maps to a different failure mechanism: discoverability, duplicate-action safety, status clarity, and error recovery. Fixing only the button color leaves the workflow unsafe. A coherent design identifies the full task and its failure branches, then tests whether users can complete and recover from them under realistic conditions.

## Worked questions and complete solutions

### Question 1 — Design a submission state machine

**Problem.** A student uploads an assignment while the network may fail. Specify at least four states, the relevant transitions, and a feedback message for the uncertain state. Explain why a green check immediately after clicking Submit is unsafe.

**Step 1: Define states.** Use *editing*, *queued locally*, *submitting*, *confirmed by server*, and *retryable failure*. Distinguish local persistence from server confirmation. The state model must reflect actual implementation, not a desired visual effect.

**Step 2: Define transitions.** Clicking Submit with valid input moves *editing* to *submitting*; a server acknowledgment moves to *confirmed*; a timeout moves to *retryable failure*; a safe retry moves back to *submitting*. If offline queueing is implemented, *editing* may move to *queued locally* before synchronization.

**Step 3: Specify truthful feedback.** In the uncertain state, say *Your submission has not yet been confirmed. Your draft is preserved on this device; retry when connected*, but only if preservation is implemented. The early green check would falsely imply confirmed server storage and could cause a student to close the page before the upload succeeds.

**Answer.** Use explicit states and guarded transitions, server-acknowledgment-based confirmation, and an honest retry path. Add backend idempotency so duplicate requests do not create duplicate submissions.

### Question 2 — Compare navigation success rates carefully

**Problem.** In a small fictional tree test, 14 of 20 attempts using navigation A and 17 of 20 attempts using navigation B find a rubric. Calculate observed success rates, absolute percentage-point difference, and relative increase. Explain two reasons the result alone does not establish a general improvement.

**Step 1: Compute rates.** A succeeds in 14/20=0.70, or 70%; B succeeds in 17/20=0.85, or 85%.

**Step 2: Compute comparisons.** The absolute difference is 0.85-0.70=0.15, or 15 percentage points. The relative increase compared with A is 0.15/0.70≈0.2143, or 21.43%.

**Step 3: State limitations.** The sample is small and may not represent the intended population. If different people performed the conditions, group differences can confound the result; if the same people performed both, practice and order effects matter. The result should guide further testing, not be reported as a proven universal benefit.

**Answer.** A: 70%; B: 85%; absolute difference 15 percentage points; relative increase about 21.43% in this illustrative sample.

### Question 3 — Quantify a toy workflow-risk model and undo budget

**Problem.** A toy model assumes independent per-step error probability p=0.03. Compare the probability of at least one error across four and ten steps. Separately, an editor stores 64 KiB per undo snapshot. How much memory is required for ten snapshots? State one reason each model could mislead design decisions.

**Step 1: Write the risk model.** P(at least one error)=1-(1-0.03)^n=1-0.97^n. At four steps, P≈0.11470719, or 11.47%.

**Step 2: Evaluate ten steps.** At ten steps, P≈0.26257587, or 26.26%. This difference is a mathematical consequence of the independence and equal-probability assumptions, not a measured property of an interface. A confirmation step might reduce downstream risk despite increasing n.

**Step 3: Estimate undo memory.** Ten snapshots require 10×64=640 KiB before metadata and allocator overhead. Delta encoding, compression, and bounded history can change actual memory consumption; a storage calculation cannot by itself determine the appropriate recovery design.

**Answer.** Modeled risk is approximately 11.47% for four steps and 26.26% for ten; ten 64-KiB snapshots occupy 640 KiB in the simplified model.

## Sources and further reading

- W3C Web Accessibility Initiative, “Accessibility, Usability, and Inclusion,” https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/ — relationship between accessible interaction, usability, and inclusive design.
- W3C Web Accessibility Initiative, “Involving Users in Evaluating Web Accessibility,” https://www.w3.org/WAI/test-evaluate/involving-users/ — testing real workflows and avoiding overgeneralization.
- UK Government Service Manual, “Plan a round of user research,” https://www.gov.uk/service-manual/user-research/plan-round-of-user-research — task-focused objectives, methods, and research preparation.

**Research integrity note:** Numerical examples and failure rates are hypothetical and are not attributed to these sources. No user testing with participants was conducted for this chapter.
