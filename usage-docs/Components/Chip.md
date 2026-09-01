<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831941723/Chip | Last modified: Aug 17, 2026 -->

# Chip

Chips are used to filter content, make selections, display input information or trigger actions.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7d505f72-340e-46fb-8efc-21f1a05743a4&&collection=contentId-2831941723&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Chip on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7273)
* [Chip on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-chip--docs)

---

## Usage

Chips are dynamic, interactive elements that allow users to filter content, enter information, make selections, or perform actions, making tasks faster and easier to complete.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9cc37054-a2e2-4545-8e1d-49501270e276&&collection=contentId-2831941723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use chips to allow users to filter content, make selections, or perform actions. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e82d4167-dd15-417b-b068-9eb241be4dd0&&collection=contentId-2831941723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use chips to display static, non-interactive labels. Use tags instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Chip** | — | Dynamic, clickable standalone component allowing selecting, filtering, or removing items. | — |
| [**Chip group**](https://zeroheight.com/626199550/p/792d1e-chip-group) | High | Collections of chips for filtering, selecting, or managing multiple related options simultaneously. | User needs to manage several related filters/selections at once |
| [**Button**](https://zeroheight.com/626199550/p/97e03c-button) | Med | Triggers actions. | A primary or critical action, not filtering/selection |
| [**Tag**](https://zeroheight.com/626199550/p/28d2fb-tag) | High | Non-interactive component for fixed information such as labels, categories, or statuses. | Displaying a static label or status with no interaction |

---

## Variants & Modifiers

### Type

#### Filter chips

Filter chips are used to represent filters in a set of options. They allow users to toggle selections on and off, providing a way to dynamically apply or remove filters.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8e46eb3a-7673-4e86-97c8-c6b06d203b92&&collection=contentId-2831941723&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use filter chips to filter content. |

#### Input chips

Input chips represent user input, selections, or entries within a form. They can be removed with the close icon.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9469f4d8-11b7-4c7d-a70f-7087304d0f2a&&collection=contentId-2831941723&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use input chips to select items or enter information into a field. |

#### Action chips

Action chips trigger actions when clicked, often performing contextual tasks that enhance the primary functionality of a page. They are lightweight, intuitive, and designed for quick, secondary actions.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0c134473-edae-4796-bcc6-7db888c74c53&&collection=contentId-2831941723&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use action chips when users need a lightweight, dynamic way to perform quick actions relevant to their current task. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=796f8b30-db20-4462-80b9-910319e98233&&collection=contentId-2831941723&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use action chips as primary navigation or for critical actions. Don't use them to move to the next/previous step or to complete/progress in a user journey. Use buttons instead. |

### Modifiers

#### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the chip more intuitive and easier to understand.

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Filter chips:** Default, hover and pressed states; can be selected or unselected.
* **Input chips:** Default, hover and pressed states; can be selected or unselected.
* **Action chips:** Default, hover, and pressed states, but cannot be selected.

### Touch Target & Layout

* **Touch Target:** To ensure accessibility, the touch target of the chip has a height of 40px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Sentence case, without punctuation.
* **Label Formula:** For action chips, {Verb} + {Noun}, leading with an action verb in the infinitive tense.
* **Length Limits:** 2-3 words, about 20-30 characters in English.

**Filter chips:** Use concise, descriptive labels that clearly communicate the purpose of the filter. Keep labels consistent across similar filters.

**Input chips:** Write labels that are specific and relevant to the input or selection being represented. Maintain brevity while ensuring that users can easily identify the context or purpose of the input.

**Action chips:** Use action-oriented labels that clearly indicate the task being performed. Keep labels short and concise. To provide enough context to users, use the {verb} + {noun} content formula.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
