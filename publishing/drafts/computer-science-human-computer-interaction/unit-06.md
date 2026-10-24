# Human–Computer Interaction — Unit 6: Inclusive design

> Original editorial teaching draft. All datasets and model coefficients are illustrative. Not academically reviewed or production-approved.

## 6.1 Accessibility: designing for independent task completion

#### Accessibility is an interaction property
Accessibility is not an optional visual theme applied after the interface has been designed. It is the degree to which people with different abilities, devices, and environmental constraints can perceive information, understand it, operate controls, and complete meaningful tasks. A student who cannot submit an exam with a keyboard has encountered an operational barrier even if every sentence is readable. A student who can submit but receives an error only as a red border has encountered an information barrier. A public service that requires listening to an audio instruction excludes people who cannot hear that instruction or who must use the service in a silent room. Each example concerns the relationship between the person, the task, the interface, and the setting. None can be evaluated reliably by looking at a screenshot alone.

The Web Content Accessibility Guidelines organize many requirements under four principles: perceivable, operable, understandable, and robust. Perceivable information can be accessed through an appropriate sensory channel; operable components can be controlled without assuming a single input device; understandable interfaces communicate their structure and consequences; robust content exposes reliable semantics to browsers and assistive technologies. These principles are useful for design reviews, but a checklist does not replace observing a user complete a task. A form can satisfy numerous individual checks while still containing an ambiguous question that prevents someone from registering. Conversely, an automated checker may flag a condition that needs human judgment before a conformance decision is possible.

#### Semantic structure is functional infrastructure
A meaningful heading hierarchy lets a reader understand the organization of a chapter and lets a screen-reader user navigate between sections. A genuine button communicates that it is actionable and supports expected keyboard activation; a styled span with a click handler may not. A properly associated label gives a form control a usable accessible name. These are not merely programming conventions. They determine whether a user can discover a control, predict its purpose, and operate it with unfamiliar software. Begin with native elements such as headings, buttons, links, lists, and form controls. Add accessible attributes when native semantics do not express the necessary state, and test the result rather than assuming that an attribute makes the widget accessible.

Consider a course enrollment form with fields for name, email, and course selection. The visual layout might place a caption above each field, but if the caption is not programmatically associated with its input, the user may hear only 'edit text' while navigating. An error message that appears in a floating notification may be missed if focus remains elsewhere and the notification is not announced. A practical correction associates every input with a persistent label, links a specific error to its field, identifies invalid input without relying on color, and preserves what the user already entered. The task is not simply to announce that an error occurred; the interface should explain what needs correction and how to recover.

#### Contrast, focus, and target geometry
For ordinary text, WCAG 2.2 Level AA generally requires a contrast ratio of at least 4.5:1, with specified exceptions; large text has a 3:1 threshold. Contrast is computed from relative luminance, not from subjective descriptions such as 'dark blue on white.' The contrast ratio is (Llighter + 0.05)/(Ldarker + 0.05). A ratio is a property of two rendered colors under the calculation, not a guarantee that a person can read the text under every viewing condition. Font size, weight, spacing, glare, and magnification still matter. Likewise, a chart that encodes 'failed' only in red remains ambiguous for some viewers even when its red text meets contrast thresholds. Use labels, patterns, or other redundant cues.

Keyboard focus must remain visible and understandable as a person moves through a page. The focus order should follow the reading and task order rather than jumping between distant columns. Opening a dialog generally requires a coherent focus-management strategy; closing it should return the person to an appropriate point. Sticky banners must not hide the focused control. Pointer targets need sufficient size and spacing: WCAG 2.2 Level AA has a 24 by 24 CSS-pixel target-size minimum with important exceptions, including spacing and equivalent controls. Treat the minimum as a conformance boundary, not an ideal target for every application. Larger targets may be necessary for a shaky bus ride, gloved hands, or people with reduced dexterity. A design should be tested under the conditions it is intended to support.

#### An evidence-based accessibility audit
An audit should start with critical journeys: finding a course, reading an assignment, submitting an answer, correcting a validation error, and retrieving a receipt. For each journey, record input modes, expected output, failure conditions, and severity. Run automated checks for detectable issues such as missing labels, then manually test keyboard operation, magnification, reflow, reduced motion, and relevant assistive technologies. Observe users with disabilities when possible and compensate them appropriately. Document the browser, device, software versions, and task scripts so a reported failure can be reproduced. Do not claim that one successful screen-reader pass establishes universal accessibility: assistive technologies differ, and real tasks can expose problems that isolated controls do not.

A useful finding names the barrier, the affected task, its consequence, a reproducible sequence, and the proposed correction. 'The icon is inaccessible' is too vague; 'The unlabeled icon after the payment total is announced only as button, so a keyboard and screen-reader user cannot identify the download receipt action' is actionable. Retest after changes, including negative paths such as invalid input and expired sessions. Accessibility is a continuing quality practice because new components, translated content, and third-party integrations can reintroduce barriers. Its central success measure is independent, reliable task completion, not the number of green checks in a tool.

## 6.2 Assistive technologies and adaptable interaction

#### Different tools expose different assumptions
Assistive technology includes screen readers, screen magnifiers, switch controls, voice control, alternative keyboards, braille displays, captioning systems, and tools that simplify or transform presentation. These tools do not form a single 'accessibility mode.' A screen reader interprets semantic information and provides speech or braille output; a magnifier enlarges a portion of the screen; a switch user may move sequentially through controls. An interface that works with one tool can still fail with another. For example, an unlabeled icon may be impossible to identify by speech, while a very small button may be difficult for someone using a head pointer. Testing should be matched to plausible task and technology combinations.

A screen reader depends on a meaningful accessible name, role, and state. The name answers 'what is this?', the role answers 'what kind of control is this?', and state communicates properties such as expanded, checked, or disabled. A button called 'Show solution' should indicate when the solution is expanded, and its controlled region should be findable. A custom dropdown built entirely from generic containers may look convincing but requires substantial keyboard and state management to behave like a real selection control. Prefer native elements when they meet the interaction need; the complexity saved can be invested in better error recovery and clearer content.

#### Keyboard and switch access
A keyboard-only walkthrough should begin at the top of the page and attempt every task without a mouse. Tab should move among interactive controls; arrow keys may operate specific composite widgets; Enter or Space should activate controls according to their semantics. The exact keyboard pattern depends on the widget, so inventing a unique pattern for each interface creates unnecessary learning work. The person must be able to escape overlays, detect focus, and avoid traps where the only exit requires a pointer. A switch user may reach a control by repeated scanning steps, making long, disorganized sequences particularly costly. Grouping actions, providing landmarks, and avoiding duplicate hidden controls can reduce this burden.

Consider a timed quiz with a question palette, answer options, and a Submit button. If the palette contains thirty unlabeled circular elements, a screen-reader user may hear thirty identical 'button' announcements. If every answer change resets focus to the beginning, a switch user pays an enormous navigation penalty. The correction is not merely to add labels. Provide a consistent order, announce question number and answered state, retain focus after ordinary updates, and allow direct navigation where the input method supports it. The test should include submitting a blank quiz, reviewing flagged questions, and recovering from a network interruption, not only selecting the first answer.

#### Zoom, reflow, and dynamic content
People who magnify content often see a smaller effective viewport. A two-column layout may become a long linear sequence; floating action bars can cover input fields; a modal can extend beyond the visible area. Test at narrow viewport widths and substantial zoom, then inspect whether controls remain reachable without requiring simultaneous horizontal and vertical scrolling for ordinary text. Complex data tables may require a different responsive strategy, but hiding essential columns without a disclosure mechanism is not an acceptable shortcut. Text spacing adjustments can also expose clipped labels and fixed-height containers. Designing flexible layouts is therefore part of supporting assistive technology, not a separate cosmetic concern.

Dynamic updates create another class of problems. A live price, validation message, or progress state may change visually while remaining silent to assistive output. Announce important status updates without repeatedly interrupting reading. Avoid making an entire changing region live when only one concise status message matters. If an action deletes an item, confirm what changed and provide undo where appropriate. If the action takes time, expose a state such as 'Uploading 40 percent' without overwhelming the user with announcements every few milliseconds. The correct design depends on task urgency and frequency of change, which should be tested with realistic activity.

#### Research with assistive-technology users
Recruiting only people who happen to use the same screen reader and browser can conceal incompatibilities. A small exploratory study can reveal severe failures, but it cannot establish that the interface works for all combinations. Document each participant's preferred setup, permit familiar devices when possible, and avoid treating slower task completion as evidence of lower competence. Differences may reflect interface barriers, device familiarity, task knowledge, or environmental factors. Record breakdowns at the level of observable interactions and invite participants to explain their strategies without requiring them to educate the research team for free. The researcher should avoid taking over the controls at the first difficulty, because that prevents observation of the actual barrier.

A strong outcome is a prioritized repair plan. Separate blockers that prevent completion from friction that adds time, and from preferences that vary among users. Preserve the user’s agency: offer customization rather than assuming a universal high-contrast theme or mandatory speech output. Accessibility benefits from design systems that include tested focus styles, dialog behavior, error components, and responsive patterns. Such shared components reduce repeated mistakes, but they still require testing in the real context where content, localization, and application state interact.

## 6.3 Internationalization and localization

#### Language changes interface structure
Internationalization prepares software to support different languages, scripts, formats, and cultural conventions without rewriting core logic. Localization adapts a particular experience for a defined audience. Translation is an important part of localization, but not the whole process. A date such as 04/05/2026 may mean April fifth or May fourth depending on locale. A price without a currency code may be misleading. A translated button label can be much longer than its English source, breaking a narrow layout. The correct design stores meaning in structured data and renders it according to an explicit locale rather than treating English strings as permanent dimensions.

A course catalog for Bangladesh and international students provides a useful case. The interface may show Bengali and English course titles, prices in different currencies, local time zones, and application deadlines. A student should know whether a deadline is expressed in Dhaka time or the time of the institution receiving the application. Store a timestamp as an unambiguous instant with an appropriate time-zone model, then format it for display. For dates that represent a calendar day rather than an instant, use a calendar-date representation instead of arbitrarily converting midnight through time zones. Testing must include transitions near midnight, daylight-saving changes in relevant regions, and missing locale preferences.

#### Bidirectional and mixed-script interfaces
Right-to-left scripts introduce layout concerns beyond reversing the order of words. Numbers, Latin acronyms, URLs, and mathematical expressions can appear inside right-to-left sentences, producing mixed-direction content. Use semantic direction and language attributes and the platform's bidirectional-text handling instead of manually reversing strings. Icons with a spatial meaning, such as 'back' and 'forward,' may need mirroring, while logos, playback symbols, and numerical charts may not. Test actual content rather than substituting repeated placeholder words. A translated page with a few short strings will not reveal clipping caused by long institutional names or mixed-script form entries.

Fonts are part of localization because glyph coverage and shaping differ. A font that displays Latin characters beautifully may omit characters needed for Bengali, Arabic, or other scripts. Fallback behavior can change line height, break alignment, and reduce legibility. Inputs should accept legitimate names without imposing an ASCII-only validation rule. Sorting and searching may require locale-aware comparisons, but the user’s expectations for alphabetical order can differ from a developer's default. Avoid treating language preference as a proxy for nationality, religion, or proficiency. Offer a clear language selector and preserve the selected language through critical tasks such as authentication and payment.

#### Translating intent, not only vocabulary
Interface language conveys actions and consequences. 'Save draft,' 'Submit application,' and 'Pay now' are different commitments; their translations must preserve that distinction. A translation memory can improve consistency, but it cannot resolve ambiguous source text. Write source strings that explain one action clearly, avoid concatenating fragments whose grammar changes by language, and provide translators with screenshots and context. Error messages should tell the user what failed and how to recover, rather than merely reporting an internal code. Inclusive content also avoids unnecessary idioms and references that require local cultural knowledge to interpret.

Some concepts require local policy research rather than linguistic substitution. Address formats, phone numbers, honorifics, tax fields, and identity documents vary across jurisdictions. A form that requires a 'state' or a five-digit postal code may reject valid international addresses. Design data models around the actual supported populations, including optional fields and varied lengths, rather than forcing every person into a domestic template. Payment options and legal consent language may require professional review. A localization checklist cannot substitute for regulatory expertise when personal data, children, or financial transactions are involved.

#### Evaluation and failure analysis
A localization test should include language switching mid-task, long labels, text resizing, screen readers with the relevant language voice, mixed-script names, and error recovery. Compare equivalent user journeys rather than merely counting translated strings. If a Bengali-language student cannot find the same scholarship filter available in English, the two versions are not functionally equivalent. Record where localization creates different information architecture and decide whether that difference serves a real audience need or reflects accidental divergence. Include native speakers in review, and compensate them for specialized linguistic work.

A useful quality measure is not '100 percent of strings translated' but the fraction of critical tasks that can be completed correctly and confidently in the intended locale. Quantitative measurements may reveal a problem, while qualitative observations explain whether it comes from terminology, visual layout, unfamiliar policy, or a software defect. Internationalization is most effective when built into content models and component design early; otherwise each new locale creates an expensive patchwork of exceptional layouts and validation rules.

## 6.4 Diverse users, situational constraints, and inclusive research

#### Designing for variation without inventing a typical user
People vary in age, motor control, vision, hearing, literacy, technical experience, language, access to devices, and confidence with institutions. These characteristics interact with circumstances. A highly experienced user may struggle when using a cracked phone screen on a moving bus. Someone with excellent vision may temporarily need large text after an eye procedure. A person fluent in one language may be a beginner in another. Inclusive design considers this variation without claiming that a single persona represents everyone. It asks which assumptions the current design makes, who those assumptions exclude, and which alternatives preserve task completion.

A university application flow illustrates interacting constraints. One applicant has a fast laptop and stable internet; another shares a phone with family and relies on intermittent mobile data. A third uses a screen reader; a fourth needs additional time to understand unfamiliar administrative terms. A design that saves progress only at the final step can disadvantage several groups for different reasons. Autosave with explicit status, resumable sessions, concise instructions, and accessible recovery can reduce the combined risk. These features should be justified by observed tasks and service requirements rather than presented as a universal cure.

#### Representation in research
Sampling only university students who use modern smartphones may produce an interface optimized for that group. Recruitment should reflect the intended audience and the variation most likely to affect the task. This does not mean every small study must be statistically representative. Formative research can deliberately recruit people likely to expose specific barriers, such as those using older devices or alternative input methods. A quantitative prevalence estimate, however, requires a suitable sampling design and explicit uncertainty. Do not mix exploratory observations with population-level claims. Record whose experiences were included and which remain untested.

Accessibility and inclusion are not synonymous. An interface may satisfy a technical standard while using culturally unfamiliar terminology or requiring documents that some legitimate users cannot obtain. Conversely, a culturally sensitive interface may still be impossible to operate with a keyboard. An inclusive evaluation plan therefore includes functional accessibility, language comprehension, device constraints, privacy expectations, and the social conditions of use. These dimensions need different evidence. A checklist can identify missing controls; interviews can expose misunderstood policies; field observation can reveal connectivity barriers; a legal review may be necessary to evaluate identity requirements.

#### Design tradeoffs and competing needs
Not every preference can be maximized simultaneously. A dense expert dashboard may improve efficiency for trained operators but overwhelm occasional users. A simplified view may hide essential information from professionals. The solution can involve progressive disclosure, configurable density, or distinct workflows, but each option introduces maintenance costs and potential inconsistency. Evaluate tradeoffs against the tasks people actually perform. A default should be safe and comprehensible, while alternative presentations should preserve the same underlying capabilities and data integrity. Avoid a segregated 'accessible version' that becomes stale and lacks new features.

Constraints can also conflict in communication. A persistent notification might help someone who misses brief messages but distract someone who is sensitive to visual motion. Offer dismissible, nonessential notifications and settings that persist when appropriate. Captions help many users, yet inaccurate automatic captions can misrepresent technical terminology; provide correction mechanisms for important content. Voice control can support hands-free use, but it may be inappropriate in shared spaces. Inclusive design aims for flexible paths to the same goal rather than assuming that one channel suits every user.

#### Ethics, measurement, and iteration
Inclusion research requires attention to consent, compensation, confidentiality, and the power imbalance between a service provider and participants. Do not recruit people in vulnerable situations merely to produce compelling case studies. Explain what data will be recorded, allow withdrawal where feasible, and avoid collecting medical or demographic details without a clear research purpose. When reporting findings, focus on barriers and design conditions rather than portraying participants as deficient. A participant who cannot finish a task may have demonstrated a system failure, not an individual limitation.

Track outcomes such as independent completion, recoverable errors, and ability to resume work across relevant conditions. Segment findings only where the data and consent justify doing so; tiny groups can create privacy risks and misleading comparisons. A meaningful iteration cycle identifies a barrier, proposes a change, verifies that the change removes the barrier, and checks for new problems in other workflows. Inclusive design is never finished by creating a persona or passing a single audit. It is an ongoing discipline of testing assumptions against the diversity of people and environments the service claims to support.

## Worked problems

### Audit a text contrast boundary

A designer proposes opaque #777777 text on white for ordinary-size labels. Compute the contrast ratio using the WCAG relative-luminance formula. Would it satisfy the ordinary-text 4.5:1 AA threshold? Compare with #767676 and explain why passing the ratio is not a complete accessibility test.

- **Convert sRGB gray to linear luminance:** For a gray channel c=119/255≈0.466667, use ((c+0.055)/1.055)^2.4 because c>0.04045. All three channels are equal, so their weighted sum equals that linear channel.

- **Calculate the two contrast ratios:** The white relative luminance is 1. For #777777, the linear gray luminance is approximately 0.184475, so (1.05)/(0.184475+0.05)≈4.478. For #767676, the linear luminance is approximately 0.181164, giving 1.05/(0.181164+0.05)≈4.542.

- **Interpret the result and its scope:** The first ratio falls below 4.5, while the second exceeds it, for ordinary text under the stated assumptions. Rendering, text size, focus indication, semantics and real reading conditions still require evaluation.

**Answer:** About 4.478:1 for #777777 (below 4.5:1), versus 4.542:1 for #767676 (above 4.5:1). The ratio is only one accessibility criterion.

### Evaluate an enlarged pointer target

A 16 by 16 CSS-pixel icon is inside a square button with 6 CSS pixels of clickable padding on every side. Compute the interactive target width, height, and area. State whether the geometry alone clears the 24 by 24 CSS-pixel size threshold in WCAG 2.2 AA, and identify two remaining checks.

- **Distinguish icon and hit area:** The visible icon occupies 16 by 16 pixels. Clickable padding is part of the button target only if pointer events actually reach the padded region.

- **Compute geometry:** The target width and height are 16+2(6)=28 CSS pixels; the area is 28×28=784 square CSS pixels. A 24 by 24 square fits within the target.

- **State the limit of the calculation:** The size condition is met in this simplified square geometry, but test target separation, clipping, responsive layouts, keyboard focus and actual hit testing. Other exceptions and criteria may also apply.

**Answer:** 28×28 CSS pixels, area 784 CSS pixels². The size is above 24×24, but that does not establish overall accessibility.

### Translate a deadline without shifting its instant

A submission deadline is stored as 2026-10-24 18:00 UTC. Show the same instant in Dhaka (UTC+06:00) and Tokyo (UTC+09:00), including the local calendar date. Explain why storing only a locale-formatted date string would be unsafe.

- **Identify the time-zone offsets:** Dhaka is six hours ahead of UTC and Tokyo is nine hours ahead of UTC for this constructed example. The stored UTC instant is the shared reference.

- **Apply the offsets and calendar rollover:** 18:00+06:00=24:00, which is 00:00 on 25 October in Dhaka. 18:00+09:00=27:00, which is 03:00 on 25 October in Tokyo.

- **Explain the data model:** Keep the deadline as an unambiguous instant with time-zone-aware formatting. A display string such as 25/10/2026 omits the time and zone and cannot reconstruct the original instant.

**Answer:** Dhaka: 2026-10-25 00:00 (+06:00); Tokyo: 2026-10-25 03:00 (+09:00). Both are the same instant.

## Interactive models

The following isolated toy models are for numerical exploration, not measured human performance.

## Sources and review limits

- W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/

- W3C WAI-ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/

- W3C WAI Involving Users in Accessibility Evaluation: https://www.w3.org/WAI/test-evaluate/involving-users/

- W3C Internationalization: https://www.w3.org/International/

No real participants were recruited. Academic review, external originality screening, and production integration remain outstanding.
