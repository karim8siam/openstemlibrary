# Human-Computer Interaction — Unit 1: Human foundations

**Incomplete editorial draft — not approved for publication.**

## 1.1 Perception
### Interfaces are interpreted by perceptual systems, not read as raw pixels
An interface is a collection of signals that a person must detect, distinguish, and interpret. A designer can place two icons at different pixel coordinates and still fail to communicate their different purposes if their shapes, labels, and context are too similar. Perception is influenced by contrast, size, spatial grouping, motion, prior experience, and the conditions in which a device is used. A mobile screen viewed in bright sunlight offers a different effective contrast from the same screen in a dim office. A laboratory mock-up with perfect lighting is therefore only one part of interface evaluation.

Visual hierarchy guides attention by making some elements more salient than others. Relative size, spacing, alignment, and contrast can suggest which items belong together and which action is primary. Gestalt principles such as proximity and similarity describe common perceptual grouping tendencies, but they are not strict laws that override task knowledge or cultural conventions. Two buttons separated by a small gap may appear grouped, yet a user can still distinguish them if their labels and surrounding structure are clear. The design question is not whether a rule was followed in isolation; it is whether users reliably identify the intended controls in realistic conditions.

Color is useful for highlighting status, but color alone is a fragile information channel. Users differ in color perception, displays vary, and environmental lighting can reduce differences. An error indicator should include text or an icon in addition to a red tint. A chart should provide a legend with units and use distinguishable patterns or labels where possible. Color contrast requirements also depend on text size and presentation context. Automated contrast checks can catch some problems, but they do not establish that a message is comprehensible or that the chosen colors carry the right meaning.

Motion attracts attention, which can be helpful for showing a transition between states. However, continuous movement competes with reading and can create discomfort for users sensitive to animation. A subtle movement indicating that a panel has opened may improve spatial understanding; an animated background behind an exam question can be distracting. Respect reduced-motion preferences and ensure that critical information does not depend on observing a short animation. A transition should explain a state change rather than merely decorate it.

Auditory and haptic feedback extend perception beyond vision. A short sound can confirm an action when the user is not looking at the screen, but it may be inappropriate in a library or classroom. A vibration can signal a notification, but different devices provide different haptic precision. Use multiple channels as complements rather than assuming every user can access all of them. The design must allow feedback to be understood when sound is muted, haptics are unavailable, or the screen is read through assistive technology.

Perceptual design should be tested with tasks rather than aesthetic judgments alone. Show users a realistic screen and ask them to identify where they would go to correct an incorrect billing address. Record which element they choose, how long they take, and what they think will happen. A button that designers describe as obvious may be missed if it competes with a brighter promotional banner. The goal is not to maximize salience everywhere; when every element demands attention, the interface loses hierarchy.

## 1.2 Attention
### Human attention is selective and task-dependent
People cannot process every available signal with equal priority. A student completing a timed test may focus on the current question and overlook a small autosave indicator. A driver using a navigation display must divide attention between the road and the device. Attention can be directed intentionally by goals and captured involuntarily by salient events. A notification that is useful during a waiting period can be disruptive during a complex calculation. Designing around attention therefore requires knowing what the user is trying to accomplish and what interruptions cost.

Visual search becomes harder when targets resemble distractors or when the layout provides no predictable organization. Grouping related controls, using consistent labels, and preserving stable locations can reduce search effort. Adding more icons is not automatically harmful if categories are clear, but a crowded toolbar with near-identical symbols can increase mistakes. Search performance also depends on familiarity: an expert may recognize a distinctive icon immediately while a new user must read a tooltip. An interface for a mixed audience should not assume expert recognition without evidence.

The Hick–Hyman relationship is an empirical approximation that describes how choice reaction time can increase with the information content of a choice set. A common illustrative form is T=a+b log2(n+1), where n is the number of equally likely alternatives and a and b are fitted parameters. It is not a universal prediction for arbitrary menus. Real menu choices differ in probability, visual organization, labeling, and familiarity. A well-structured menu with many recognizable options can be easier than a short menu with ambiguous categories. Use the relationship to reason about selection demands, not to claim that every additional button creates a fixed delay.

Attention can also be interrupted by system feedback. If a user clicks Save and the interface silently pauses, they may click again or navigate away. A prompt status indicator can communicate that work is proceeding. Yet excessive progress animations can create the opposite problem by pulling attention away from the task. Prefer feedback that is proportional to the action's importance and duration. For a quick toggle, the changed control state may be sufficient. For a long file upload, progress, cancel behavior, and failure recovery deserve explicit design.

Multitasking has costs when tasks compete for cognitive resources. Switching from reading a research paper to responding to a notification requires the reader to reconstruct context afterward. A learning platform can reduce unnecessary interruptions by batching low-priority alerts and keeping the current work visible. In a safety-critical application, however, an urgent alarm must interrupt. The difficult design problem is prioritization: which events justify capturing attention, how reliably can the user distinguish them, and what happens when several arrive together?

An attention study should define the primary task and measure interference. For example, compare test completion time and error rate with notifications disabled versus notifications enabled. Randomize condition order where practical and consider practice effects. An observed increase in completion time does not automatically identify the mechanism; participants may spend time reading notifications, recovering context, or becoming cautious. Qualitative observation can help explain the quantitative difference. Avoid drawing a universal conclusion from a handful of participants performing an artificial task.

## 1.3 Memory
### Recognition is often easier than recall, but neither is free
Working memory supports temporary maintenance and manipulation of information, such as remembering a verification code while switching between apps. Its capacity is limited and varies with task complexity, familiarity, and how information is grouped. It is misleading to treat a single fixed number of items as a universal capacity rule for all people and situations. A user can remember a familiar word more easily than an equally long string of unrelated symbols because prior knowledge supports chunking. Good interface design reduces unnecessary memory demands instead of relying on a simplistic numeric threshold.

Recognition allows a user to identify a visible option, while recall requires producing information without that cue. A menu of recent documents supports recognition; asking a user to type an exact filename from memory requires recall. Search, autocomplete, history, and visible navigation trails can reduce recall burden. However, recognition also requires scanning and comparing alternatives, so a very long unorganized list can still be difficult. The design tradeoff is between exposing useful cues and overwhelming the user with options.

Consistency helps users form reusable expectations. If a control labeled Download always initiates a file download, users can rely on that mapping across pages. If the same icon alternates between Save, Export, and Share depending on hidden context, users must repeatedly infer its meaning. Consistency should be applied at the level of behavior and terminology, not merely visual styling. A perfectly consistent but confusing convention may need to be changed, especially when it conflicts with common platform expectations.

External memory aids are valuable in long workflows. A checkout flow can show the current shipping address and payment summary before final confirmation. A research tool can preserve filters, previous queries, and citations when the user returns. A laboratory interface can display the units and calibration settings next to measured values. These choices prevent errors caused by remembering stale state. The cost is screen space and potential clutter, so information should be placed where it is needed rather than repeated indiscriminately on every page.

Error recovery also interacts with memory. After a form validation failure, clearing all previously entered fields forces the user to reconstruct work from memory or retype it. Preserving valid entries and marking the specific fields that need correction is usually more supportive. Similarly, undo and version history reduce the cognitive burden of anticipating every possible consequence before acting. The ability to reverse an action can encourage exploration, but irreversible operations still require appropriate confirmation and clear consequences.

Memory evaluation should use realistic delays and interruptions. A participant who can recall a code immediately after seeing it may fail when asked to navigate another screen first. Measure both accuracy and completion time, and note whether participants invent workarounds such as writing values down. A workaround can be evidence that the interface imposes unnecessary memory demands. It is not automatically a failure of the user or a reason to ban external notes.

## 1.4 Mental models
### People act according to their understanding of the system
A mental model is a user's internal explanation of how a system works and what actions will cause. It need not match the software architecture. A user may think of a cloud folder as a physical container even though files are stored as objects and metadata. That metaphor can be useful if it predicts ordinary behavior, such as moving a document between folders. It becomes harmful when the metaphor implies something false, such as assuming that deleting a local shortcut necessarily deletes every remote copy.

Designers also have a conceptual model: the explanation they intend the interface to communicate. The implemented system has its own actual rules and state transitions. Problems arise when these models diverge. Suppose a student presses Submit on an online exam and sees the button become gray. Does this mean the answer was sent to the server, stored locally, or merely that the button was temporarily disabled? Without explicit feedback, users may construct different explanations. A reliable design communicates important state transitions through labels, confirmations, and recoverable history.

Affordances and signifiers help users infer possible actions. A physical button affords pressing because of its shape and resistance; a digital button relies more heavily on visual signifiers such as a border, label, cursor behavior, and placement. A flat decorative rectangle may look clickable even if it is not. Conversely, a link that appears as ordinary body text may be overlooked. Interactive elements should have discoverable actions, meaningful names, and visible focus states for keyboard users.

Mapping describes the relationship between controls and effects. A slider that moves right to increase brightness has a familiar mapping in many contexts. A two-dimensional control for camera orientation may need explicit axes and a preview because the relationship is less obvious. Natural mapping is task-dependent: turning a virtual knob clockwise may increase a parameter, but in a mirrored camera view the apparent motion can be confusing. Test the mapping with actual users rather than assuming the developer's coordinate convention will be intuitive.

Feedback helps users update their mental model after acting. If a filter changes the result count immediately, the user can infer that the filter is active. If the filter applies only after pressing an unlabeled button, the user may think the system is broken. Delayed operations need progress indicators and a clear distinction between pending, successful, and failed states. Optimistic interfaces that display success before server confirmation should provide a visible recovery path if the operation later fails.

Mental models can be studied by asking users to predict what will happen before they click and then comparing predictions with outcomes. A think-aloud study can reveal why a participant chose an action, but the facilitator should avoid leading questions. Ask what the participant expects, not whether they noticed the designer's intended icon. A single successful click does not prove understanding: a user may have guessed correctly and still misunderstand the system. Repeat tasks that depend on the same concept to see whether the explanation generalizes.

## 1.5 Integrated investigation: redesigning an online exam interface
### Measure comprehension rather than aesthetic preference
A university exam platform receives complaints that students submit the wrong answer, miss save confirmations, and accidentally leave timed tests. The design team initially proposes brighter colors and larger icons. These changes might help, but they do not establish the causes of the reported errors. Begin by mapping the actual workflow: opening a question, selecting an option, saving, navigating, reviewing unanswered questions, and final submission. Identify which actions are reversible and which have serious consequences.

Observe a small set of representative students using the existing interface under realistic conditions. Ask them to complete a practice test while recording errors, navigation patterns, and points of hesitation. Include keyboard users and participants on smaller screens where feasible. Distinguish a misclick from a misunderstanding of system state. If students repeatedly press Save because no confirmation appears, the problem is feedback. If they choose the wrong adjacent answer option, spacing and target design may be involved. If they forget which questions remain unanswered, external memory support may be missing.

Redesign the interface with explicit answer-state labels, a stable question navigator, and a clear difference between Save and Final Submit. Preserve selected answers during temporary connection failures when technically feasible, and show whether a change is stored locally, queued, or confirmed by the server. The confirmation message should correspond to the actual persistence guarantee. Do not claim “saved” merely because a click handler executed. For a timed test, display the remaining time clearly but avoid distracting animations on every second unless users need that granularity.

Compare the original and revised interfaces using the same representative tasks. Measure wrong-answer selection, unintentional navigation, time to recover from a failed save, and successful completion. Counterbalance the order of interface versions to reduce learning effects, and record device type and network conditions. Participants may prefer the new interface without making fewer errors, or may complete tasks faster while overlooking an important confirmation. Report these outcomes separately. A successful redesign is one that improves the relevant behavior under stated conditions, not merely one that looks more modern.

## Worked problem 1: Hick–Hyman choice-time comparison
**Question.** An illustrative choice-time model is T=a+b log2(n+1), with a=0.25 s and b=0.15 s/bit. Calculate predicted times for menus with n=7 and n=15 equally likely alternatives. Explain what the difference does and does not imply.

**Step 1 — Evaluate the seven-choice case.** For n=7, log2(7+1)=log2(8)=3. Thus T7=0.25+0.15×3=0.70 s.

**Step 2 — Evaluate the fifteen-choice case.** For n=15, log2(15+1)=log2(16)=4. Thus T15=0.25+0.15×4=0.85 s. The modeled difference is 0.15 s under the stated parameters.

**Step 3 — Interpret scope.** The relationship is a fitted approximation, not a universal prediction. Grouping, labels, familiarity, choice probabilities, and motor movement can alter observed times. The result does not prove that reducing every menu from fifteen to seven items will save exactly 0.15 s.

**Answer.** Predicted times 0.70 s and 0.85 s; modeled difference 0.15 s.

## Worked problem 2: Fitts-law pointing-time estimate
**Question.** A pointing model uses T=a+b log2(1+D/W), with a=0.20 s and b=0.10 s/bit. The pointer travels D=240 pixels to a target of effective width W=30 pixels. Estimate the movement time. Recalculate for W=60 pixels, keeping the same distance and fitted parameters.

**Step 1 — Compute the initial index of difficulty.** For W=30, ID=log2(1+240/30)=log2(9), approximately 3.169925 bits. The predicted movement time is 0.20+0.10×3.169925, approximately 0.516993 s.

**Step 2 — Increase target width.** For W=60, ID=log2(1+240/60)=log2(5), approximately 2.321928 bits. The predicted movement time becomes 0.20+0.10×2.321928, approximately 0.432193 s.

**Step 3 — Interpret carefully.** The model predicts an improvement of about 0.0848 s under these conditions. Effective target width depends on task geometry and movement direction; touch interaction, accuracy demands, and user ability can change the fitted parameters. Making a button visually larger does not help if its clickable area remains unchanged.

**Answer.** Approximately 0.5170 s at width 30 px and 0.4322 s at width 60 px, a modeled reduction of about 0.0848 s.

## Worked problem 3: Evaluate an error-prevention intervention
**Question.** In a controlled practice task, a baseline interface produces 18 incorrect selections across 120 submitted answers. A revised interface produces 9 incorrect selections across 120 answers. Calculate the error rates and the relative reduction. State why the result alone is insufficient to establish a general improvement.

**Step 1 — Calculate baseline error rate.** The baseline rate is 18/120=0.15, or 15 percent of submitted answers.

**Step 2 — Calculate revised error rate.** The revised rate is 9/120=0.075, or 7.5 percent. The absolute reduction is 7.5 percentage points. The relative reduction is (0.15-0.075)/0.15=0.50, or 50 percent.

**Step 3 — Assess inference.** These are observed sample proportions. They do not by themselves establish a causal effect or statistical significance. The design must account for participant differences, repeated answers by the same person, task difficulty, order effects, and sample size. A properly designed study with uncertainty estimates is needed before generalizing to all students.

**Answer.** Baseline 15 percent, revised 7.5 percent; absolute reduction 7.5 percentage points and relative reduction 50 percent in the observed sample.
