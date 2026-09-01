<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3453419713/Chip+group | Last modified: Aug 17, 2026 -->

# Chip group

Chip groups are collections of chips that allow users to filter, select, or manage multiple related options simultaneously.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cbbfe0b5-98f7-4e77-96bf-5f3e7e0003b7&&collection=contentId-3453419713&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To do 🚧 | To do 🚧 |

* [Chip group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7273)
* [Chip group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-chipgroup--docs)

---

## Usage

Chip groups are dynamic, interactive collections of chips that allow users to filter content, toggle options, or make multiple selections within a related set, providing an efficient way to organize and manage complex choices or actions.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1613736c-36bc-40f6-a383-ccd76ad192cc&&collection=contentId-3453419713&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use chip groups to allow users to filter content, make selections, or perform actions. | **DON'T:** Don't use chip groups to display static, non-interactive labels. Use tags instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Chip group** | — | Collections of chips that allow users to filter, select, or manage multiple related options simultaneously. | — |
| [**Chip**](https://zeroheight.com/626199550/p/32f686-chip) | High | Dynamic, clickable standalone component for selecting, filtering, or removing items. | Only a single, standalone chip is needed |
| [**Button**](https://zeroheight.com/626199550/p/97e03c-button) | Med | Triggers actions. | A primary or critical action, not filtering/selection |
| [**Tag**](https://zeroheight.com/626199550/p/28d2fb-tag) | High | Non-interactive component for fixed information such as labels, categories, or statuses. | Displaying a static label or status with no interaction |

---

## Variants & Modifiers

### Type

#### Filter chips

Filter chips are used to represent filters in a set of options. They allow users to toggle selections on and off, providing a way to dynamically apply or remove filters.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=82abbf37-635b-4c08-ad3f-5e79ecdf1c7e&&collection=contentId-3453419713&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use filter chips to filter content. |

#### Input chips

Input chips represent user input, selections, or entries within a form. They can be removed with the close icon.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d0e520b6-f326-44fe-84f9-d9b2c51f5f3c&&collection=contentId-3453419713&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use input chips to select items or enter information into a field. |

#### Action chips

Action chips trigger actions when clicked, often performing contextual tasks that enhance the primary functionality of a page. They are lightweight, intuitive, and designed for quick, secondary actions.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=aa8f496b-4603-4215-bcb9-d1e3a997e2b3&&collection=contentId-3453419713&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use action chips when users need a lightweight, dynamic way to perform quick actions relevant to their current task. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9e2d9dc7-c6f5-4b9c-9d4f-2a416ce6c734&&collection=contentId-3453419713&height=1200&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use action chips as primary navigation or for critical actions. Don't use them to move to the next/previous step or to complete/progress in a user journey. Use buttons instead. |

### Modifiers

#### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the chips more intuitive and easier to understand.

---

## Behavior & Responsiveness

### Interactive States & Loading

The states of the individual chips in the chip groups are the same as for [standalone chips](https://zeroheight.com/626199550/p/32f686-chip).

* **Filter chips:** Default, hover and pressed states; can be selected or unselected.
* **Input chips:** Default, hover and pressed states; can be selected or unselected.
* **Action chips:** Default, hover, and pressed states, but cannot be selected.

### Touch Target & Layout

* **Touch Target:** To ensure accessibility, the touch target of each chip has a height of 40px.
* **Width Adaptability:** Chips wrap to a new line if there is not enough space for all of them.

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
