# Human–Computer Interaction — Unit 7: Interaction modalities

> Original editorial teaching draft. All datasets and model coefficients are illustrative. Not academically reviewed or production-approved.

## 7.1 Touch, gestures, and physical input

#### Touch is direct but not precise by default
Touch interfaces make it possible to manipulate visible objects without a separate pointing device, but the contact area of a finger is larger than the perceived point of intent. Occlusion matters: a finger can hide the control being selected or the feedback produced by the selection. Small adjacent targets increase the risk of accidental activation, especially during movement or when the user has reduced dexterity. Designers should distinguish the visual size of an icon from its actual interactive hit region. A tiny icon can be placed inside a generous target, while a large decorative image can misleadingly appear clickable without offering a reliable target.

Touch also changes posture and reach. A person holding a phone with one hand may struggle to reach a top corner, while a tablet resting on a desk allows a different range of movements. There is no single universal thumb zone because grip, hand size, device dimensions, and handedness vary. Test important controls in representative postures and with realistic tasks. For a ticket-booking app, the Confirm action should not be placed so close to a destructive Cancel action that a slight slip has costly consequences. Spatial separation, confirmation for irreversible operations, and undo can reduce harm more effectively than merely increasing visual contrast.

#### Gesture discoverability and alternatives
Gestures such as swipe, pinch, drag, and long press can be efficient once learned, but they often lack visible affordances. A card that disappears when swiped may look identical to a static card. If the only way to delete an item is to swipe left, some users will never discover the function and others may be unable to perform it. Provide an explicit action or menu alternative and communicate consequences. A drag-and-drop ordering tool should offer buttons or another single-pointer method when dragging is not essential. Keyboard operation also matters for people using hardware keyboards with tablets and phones.

Gestures require state design. A horizontal swipe within a vertically scrolling page can be interpreted as navigation, scrolling, or object manipulation. Define how the interface distinguishes intentional gestures from incidental movement. Provide immediate, reversible feedback where possible. A swipe that archives an email should indicate what happened and allow undo for a reasonable interval. Avoid animations that delay control or make the user wait for an effect before proceeding. Motion preferences and device performance should influence transitions, especially in educational apps where the goal is sustained reading rather than entertainment.

#### Touch data and error prevention
Touch coordinates are noisy observations of intention, not perfect measurements. A test can record the distribution of taps relative to target centers and examine near misses, but the measurement must account for device scaling and layout changes. Heatmaps can be misleading if aggregated across different screen sizes without normalization. A target-size calculator can demonstrate how hit area changes with padding, yet it cannot predict the probability that a real person will make an error. Actual error rates depend on motor ability, posture, urgency, and interface feedback. Use models to explore geometry and user tests to estimate performance.

Consider a mobile chemistry quiz with a diagram and four answer options. If the diagram captures all touch events, users may be unable to scroll past it. If the answer choices are closely packed, an accidental tap may immediately submit the question. A better design separates exploratory diagram gestures from answer selection, makes selected state visible, and requires an explicit final submission when the consequence warrants it. Test the entire sequence with screen magnification, reduced motion, and a keyboard. An interface is not 'touch friendly' merely because buttons respond to a finger.

#### Designing a comparative test
A useful experiment compares two target layouts on the same task and devices, counterbalances order, and records attempts, errors, completion time, and subjective confidence. Participants should practice each layout before measurement to reduce novelty effects. Distinguish mis-taps from misunderstood labels: increasing target size will not repair a button whose purpose is unclear. A field study may reveal problems absent from a laboratory, such as glare or unstable grip. Report the conditions under which a design performed better rather than declaring one spacing value universally optimal. The objective is dependable task completion across realistic use, not maximizing a single gesture metric.

## 7.2 Speech interfaces and conversational repair

#### Speech changes the shape of interaction
A spoken interface replaces visible choices with a sequence of utterances and responses. Speech can support hands-free work and users who cannot comfortably operate a screen, but it creates new burdens: users may not know which commands exist, may forget long menus, and may struggle to verify what the system heard. Background noise, microphone quality, accents, language switching, and domain-specific vocabulary all affect recognition. Recognition accuracy is not the same as task success. A system can transcribe every word correctly and still misunderstand the user's intent or provide an unusable answer.

A well-designed voice interaction begins by making its scope discoverable. Instead of saying 'How can I help?' when the system supports only three actions, it can offer concise examples such as checking a deadline, opening a course, or reviewing saved work. Avoid lengthy spoken menus that require the listener to remember many alternatives. Confirm high-consequence actions with a short restatement: 'You are about to submit the final application; should I proceed?' Low-risk requests may not require explicit confirmation. The design must balance speed against the cost of errors and the difficulty of recovering from them.

#### Recognition, interpretation, and response
A speech pipeline may include audio capture, speech recognition, language understanding, dialogue state, action execution, and speech synthesis. Each stage introduces different failure modes. A noisy environment may corrupt recognition; an ambiguous phrase may confuse intent classification; an outdated dialogue state may apply a correct command to the wrong course. Logging should distinguish these failures rather than collapsing them into a single 'voice did not work' category. Because audio may contain personal information, data retention and access controls must be defined before collecting recordings for debugging.

Consider a student asking, 'Move my physics tutorial to Thursday.' The system needs to know which tutorial, which Thursday, whether rescheduling is permitted, and what conflicts exist. If two tutorials match, guessing can produce a harmful action. A clarification question should target the missing information: 'Do you mean the quantum mechanics tutorial at 10 a.m. or the laboratory tutorial at 2 p.m.?' Once a unique target is identified, the system should summarize the planned change and request confirmation if it modifies a real schedule. If the user changes topic mid-conversation, the dialogue state must handle the interruption without silently completing the old action.

#### Multimodal recovery
Speech should not be the only path to essential information when a display or alternative input is available. Show recognized text and allow correction; provide captions for spoken output; support typed input for private or noisy settings. A person in a shared dormitory may not wish to speak financial details aloud. A person with a speech impairment may need an alternative way to provide commands. Some users prefer voice for search but touch for reviewing a long list of results. A multimodal design should preserve context when switching channels rather than forcing the user to restart the task.

Errors need cooperative repair. If recognition confidence is low, ask for a short repetition or offer visible alternatives rather than repeating an entire long prompt. If a requested action is unsupported, explain the boundary and suggest a supported action without pretending the system understood. Repeated fallback messages can trap users in loops; after several failures, provide a direct route to a different interface or human assistance where appropriate. Measure successful recovery and abandonment, not just the number of utterances recognized. A voice assistant that achieves a high word accuracy but cannot recover from a misheard date is not reliable for scheduling.

#### Evaluation and fairness
Evaluate speech interfaces across relevant accents, speaking rates, languages, noise levels, and device types. Do not infer that one demographic group is inherently difficult to understand from a small convenience sample. Model and dataset coverage, microphone quality, and domain vocabulary may explain observed disparities. Use consent and appropriate privacy safeguards when recording speech. Report word error rate alongside task completion, clarification turns, harmful actions, and successful recovery. For safety-critical or irreversible tasks, error severity may matter more than average recognition accuracy. The central design question is whether people can accomplish their goal with predictable consequences, not whether the assistant sounds human.

## 7.3 Tangible and embodied interfaces

#### Connecting physical objects with digital state
A tangible interface uses physical objects or surfaces as part of interaction with digital information. Examples include instrumented blocks that represent simulation parameters, a tabletop where moving a token changes a map, and laboratory equipment with physical controls linked to a digital display. The appeal is not simply that objects can be touched. Physical form can make state visible, support spatial reasoning, and allow people to coordinate around a shared workspace. However, the mapping between physical action and digital consequence must be learnable. A rotating dial that changes a graph's time scale can feel direct, while an unlabeled cube whose orientation changes unrelated settings can be mysterious.

Embodied interaction also depends on the environment. A classroom tabletop may have enough space for several learners, but a small desk may not. Physical tokens can be lost, damaged, or difficult to manipulate. An interface designed for a single person may become confusing when multiple people move objects simultaneously. The system should communicate ownership, conflicts, and current state. If a token is removed from the table, does the associated digital object disappear, pause, or persist? These decisions must be explicit because physical actions can be accidental and difficult to reconstruct after the fact.

#### Mapping and feedback
A good mapping preserves a meaningful relationship between action and effect. Moving a model car forward can advance a simulated vehicle; turning a knob clockwise can increase a parameter if that convention is clear in the context. Arbitrary mappings require memory and are vulnerable to mistakes. Feedback must be timely enough to maintain the connection between physical and digital state. A delayed graph update can cause repeated adjustments and overshoot. Yet immediate feedback is not always appropriate: an unstable sensor can produce visual jitter, so filtering may be needed. Filtering introduces latency and can hide rapid changes. Designers should test this tradeoff with the intended task rather than selecting a smoothing value by aesthetics.

A physics education example is a physical slider that controls the angle of a virtual projectile. Learners can vary angle and observe predicted range under an explicitly simplified model. The model should display its assumptions, such as no air resistance and equal launch and landing heights. If a student moves the slider beyond a valid range, the system should constrain the input or explain the invalid state. A digital keyboard alternative matters for students who cannot manipulate the physical slider. The educational value comes from linking manipulation, prediction, and explanation, not from the novelty of a sensor.

#### Reliability and calibration
Physical sensors produce measurements with uncertainty. A dial may report slightly different values at the same apparent position; a camera tracking markers may lose an object under poor lighting. Calibration should define a repeatable mapping between measured signals and interface values. A linear example maps sensor reading s in [smin,smax] to normalized value (s-smin)/(smax-smin), but only if the range is nonzero and the mapping is suitable for the sensor. Clamping can prevent out-of-range output, yet silent clamping may conceal hardware faults. When a sensor disconnects, the interface should distinguish stale data from a valid stable reading.

Multiuser tangible systems need conflict rules. If two students turn different controls that affect the same simulation, the system can combine inputs, assign roles, or serialize changes. Each policy has social consequences. Locking one user out may reduce errors but undermine collaboration; accepting every update may create flicker or inconsistent results. A visible activity history can help participants understand what changed. Evaluate coordination by observing how people negotiate control and repair misunderstandings, not just by measuring how quickly the system processes sensor events.

#### Accessibility and evaluation
Tangible interaction can help some users by making controls tactile, but it can exclude others when objects are heavy, require fine motor control, or provide feedback only through a projected display. Provide alternative input and output where feasible. A physical dial may need an equivalent keyboard or switch control, and a color-coded token should also have a shape or label. Evaluate setup time, physical effort, mapping comprehension, error recovery, and collaborative behavior. A tangible interface is justified when physical manipulation supports the task better than a simpler control; it is not automatically more intuitive or inclusive because it uses real objects.

## 7.4 Immersive interaction and spatial computing

#### Presence is not the same as task performance
Virtual and augmented reality place digital content in a spatial frame. Immersion can support training for tasks that depend on three-dimensional relationships, such as understanding equipment layout or rehearsing a procedure. But visual realism and a strong sense of presence do not guarantee learning or efficiency. A flat diagram may be better for comparing precise numerical values, while a spatial scene may help a learner understand orientation and reach. Select the medium according to the cognitive work required. The question is whether spatial interaction adds meaningful information that is hard to communicate in another form.

A virtual chemistry laboratory illustrates the tradeoff. A learner can approach an apparatus, identify components, and practice the order of safe operations without consuming reagents. Yet if every measurement must be read by turning the head toward a tiny virtual label, the interface may add unnecessary effort. A well-designed scene keeps essential information legible, provides accessible alternatives, and avoids requiring physical motions unrelated to the learning objective. Simulated safety behavior should not be mistaken for certification to perform a real laboratory procedure. Training claims need evidence of transfer to the actual task.

#### Spatial reference frames and interaction
Immersive systems may use head orientation, hand tracking, controllers, gaze, or physical movement. Each input method has noise and failure modes. A gaze-based selection can be fast but may trigger actions when the user merely looks at an object. Hand gestures can feel natural but may be difficult to detect under occlusion. Controller buttons provide explicit actions but require learning. Designers should distinguish pointing, previewing, and committing. For a destructive action, an explicit confirmation mechanism is preferable to interpreting an incidental gaze or hand motion as consent.

Spatial interfaces also require consistent reference frames. A panel attached to the user's head remains visible but can obstruct the scene; a panel fixed in the virtual room can be lost when the user turns away. A world-anchored label may drift if tracking is inaccurate. The interface should make important state recoverable and avoid placing essential controls outside comfortable reach. Do not assume that a seated user can stand, rotate freely, or extend both arms. Offer seated and limited-motion interaction paths when appropriate. These choices must be evaluated with the actual headset and tracking setup, not just in a desktop preview.

#### Comfort, safety, and privacy
Immersive displays can cause discomfort for some users, particularly when visual motion conflicts with vestibular cues. Comfort depends on individual sensitivity, content, latency, field of view, and session duration. Avoid unnecessary camera acceleration and provide options such as teleportation, snap turning, shorter sessions, or non-immersive alternatives. These options should be tested rather than described as universal remedies. Physical safety matters too: users may collide with furniture or other people while attending to virtual content. The experience should communicate boundaries and allow immediate pause or exit.

Headsets and sensors may collect motion traces, voice, eye-gaze, and environmental imagery. Such data can reveal sensitive behavior or bystanders' surroundings. Collect only what the task needs, explain retention, and avoid using precise behavioral traces for unrelated analytics without appropriate consent and safeguards. An educational institution should consider whether a student can complete equivalent learning outcomes without consenting to unnecessary tracking. Immersive interaction should expand access to learning, not make expensive equipment or intrusive data collection a prerequisite for essential participation.

#### Measuring educational value
Evaluate immersive systems using meaningful outcomes: correct procedural steps, retention, transfer, error severity, completion time, and comfort. Compare against a credible alternative, such as a well-designed desktop simulation, rather than against no instruction. Counterbalance practice order where possible and account for novelty effects. A learner may initially report high enjoyment while performing worse on a later real-world task. Separate subjective presence, usability, and actual learning in the analysis. An immersive design is justified when its benefits exceed its costs in hardware, development, support, accessibility, and potential discomfort. The medium is a tool for the task, not the task itself.

## Worked problems

### Compare touch hit areas

A small icon is 16 by 16 CSS pixels. Layout A makes only the icon clickable. Layout B adds 12 CSS pixels of clickable padding on each side. Calculate the two square hit areas and their ratio. Explain why the ratio is not a measured reduction in error probability.

- **Compute the original hit area:** Layout A is 16×16=256 square CSS pixels.

- **Compute the enlarged target:** Layout B has width 16+2×12=40 CSS pixels, so its area is 40×40=1600 square CSS pixels. The ratio is 1600/256=6.25.

- **Interpret cautiously:** The hit region is 6.25 times larger in area, but actual mis-taps depend on finger placement, spacing, posture, feedback, and motor variability. No empirical error-rate improvement follows from area alone.

**Answer:** Areas 256 and 1600 square CSS pixels; the second is 6.25 times the first. This is geometry, not a behavioral prediction.

### Calculate word error rate without conflating it with intent

In a constructed 40-word reference transcript, a recognition system makes two substitutions, one deletion, and one insertion. Compute word error rate (WER). Explain why this number does not determine whether the user successfully scheduled a tutorial.

- **Define the metric:** WER=(S+D+I)/N, where S is substitutions, D deletions, I insertions, and N reference words.

- **Substitute the constructed counts:** WER=(2+1+1)/40=4/40=0.10=10 percent.

- **Interpret downstream effects:** The incorrect word could be a harmless article or the date of the tutorial. Intent understanding, clarification, confirmation and action execution determine task success; WER alone does not.

**Answer:** WER is 10%. It is a transcription metric, not a complete measure of conversational success.

### Calibrate a physical slider and plan fallback

A sensor reads 420 units within a calibrated range of 100 to 900. Map it linearly to an angle from 10 to 70 degrees. Compute the normalized value and resulting angle, then explain what the interface should do when the sensor disconnects.

- **Normalize the reading:** The normalized position is (420−100)/(900−100)=320/800=0.40.

- **Map to the output interval:** The output angle is 10+0.40×(70−10)=10+24=34 degrees.

- **Design failure behavior:** If the sensor disconnects, label the reading stale and prevent an old value from appearing live. Offer a keyboard or on-screen alternative, and permit reconnection with clear calibration state.

**Answer:** Normalized reading 0.40; mapped angle 34 degrees. The number assumes a valid linear calibration and live sensor.

## Interactive models

The following isolated toy models are for numerical exploration, not measured human performance.

## Sources and review limits

- W3C WCAG 2.2 input modalities: https://www.w3.org/TR/WCAG22/#input-modalities

- W3C WAI accessible mobile guidance: https://www.w3.org/WAI/standards-guidelines/mobile/

- W3C WAI Accessible Rich Internet Applications: https://www.w3.org/TR/wai-aria-1.2/

No real participants were recruited. Academic review, external originality screening, and production integration remain outstanding.
