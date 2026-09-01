<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832039962/Button | Last modified: Aug 17, 2026 -->

# Button

Buttons are used to trigger an immediate action. Button labels express what action will occur when the user interacts with it.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=49389108-1cf1-41de-831a-5ea170aef3c4&&collection=contentId-2832039962&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Button on Figma](https://www.figma.com/file/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?type=design&node-id=11%3A27&mode=design&t=dkkP9LV7KntXJ8DP-1)
* [Button on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-button--docs)

---

## Usage

Buttons are clickable elements that are used to trigger actions. They communicate calls to action to the user and allow users to interact with pages in a variety of ways. Button labels express what action will occur when the user interacts with it.

However, buttons are not intended to be navigational elements and should not be used to navigate to different areas of a website or app. Using buttons for navigation can confuse users, as buttons are generally associated with actions like submitting forms, triggering events, or performing specific tasks. For navigation, links should be used instead, as they are specifically designed to guide users to different pages or sections, ensuring a clear and intuitive user experience.

**Navigation button:** To guide users back to the previous page, use a tertiary button featuring a left-facing arrow and the label "Back." The recommended spacing between header and button depends on the content underneath: if there is a headline, 24px is recommended, but the spacing can be larger if there is an empty state below, for example.

**Read more button:** Use a "Read more" button to display additional content only when users choose to see it. By expanding or collapsing text, users control what they want to read, which makes interfaces cleaner and easier to navigate. The overlapping gradient indicates that the text is expandable. The read more button uses a text button, which is a different component than the normal button.

### Platform

On iOS and Android, an animated floating button is available. When the user starts scrolling, the button smoothly transitions to a smaller, circular icon button. The animation uses a duration of `500ms` and an easing `ease`.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9bc81061-f455-4224-b011-057afa948c29&&collection=contentId-2832039962&height=520&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use buttons to trigger actions, such as sharing, saving or opening a modal with a contact form. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=87570592-42e3-47c8-93ad-6027e830365c&&collection=contentId-2832039962&height=520&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use buttons as navigational elements. Instead, use links when the desired action is to take the user to a new page. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Button** | — | Buttons trigger actions. | — |
| **Link** | — | Links are navigational elements that take users to different pages or sections. | — |

---

## Variants & Modifiers

### Emphasis

These different types of buttons are based on the level of emphasis we want to give to various actions. The most important aspect is to establish a visual hierarchy among the buttons in your UI. Keep these best practices in mind.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=47c11ee6-5fae-4ba7-ae6b-af76159255f0&&collection=contentId-2832039962&height=362&occurrenceKey=null&width=840&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Proportion of emphasis used across AVIV products

| Emphasis | Purpose |
| --- | --- |
| Primary | For the main call to action on the page. Primary buttons should only appear once per section. |
| Secondary | For secondary actions on each page. Secondary buttons can be used in conjunction with a primary button. |
| Tertiary | For less prominent, and sometimes independent, actions. Tertiary buttons can be used in isolation or paired with a primary button when there are multiple calls to action. Tertiary buttons can also be used for sub-tasks on a page where a primary button for the main and final action is present. |
| Danger | Reserved for destructive actions. These actions normally delete user's data and cannot be reverted. Depending on the severity of the action a confirmation modal can follow a Danger button action. |

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8879b9ad-9ea8-4ca8-b98b-a590b25353b8&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use only one primary button per section. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dcff6926-bfb8-4d1d-a3e2-b68b1b8b36ca&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use more than one primary button per section. |

| DO |
| --- |
| **DO:** You can use secondary and tertiary buttons without the need to include a primary one. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f2bf02a0-5c36-4429-bc3d-847ec2b2f2ef&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** You can group multiple secondary and tertiary buttons. |

| CAUTION |
| --- |
| **CAUTION:** Be cautious using a standalone tertiary button as without context these buttons could be overlooked as actions. |

Data tracking in the [CDP](https://avivgroup.atlassian.net/wiki/spaces/ADS/database/1123451029) showed that the button change from secondary to tertiary initially caused a short-term drop in engagement but led to a sustained long-term increase. It is now performing the same / slightly better.

### Size

At AVIV we use our 40px height button as the default but there's no strict rule that prevents designers from using the 48px or 32px height one, however when using the different sizes be mindful of the white space around them: the more white space around a button or a group of buttons you'll have, the more chances to use a bigger button.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d7b579ae-570a-45da-accb-e3029e886429&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the same size of the button or field aside. | **DON'T:** Do not use a different size between two buttons aside or the field next to the button. |

### Context

Buttons change appearance depending on their context and background to better adapt to the environment, maintaining the same level of accessibility and usability.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=88713e4e-96cc-47ab-9199-a04ccb31eea1&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the floating variant for buttons that overlap images. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6843e8b3-dbfd-47fe-b900-4aa849be7f6a&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the floating variant for buttons that overlap images. |

### Modifiers

#### Icons

Icons are used to emphasize the action stated in the label of the button. By default we use the left aligned button. Icon-only buttons should contain icons that easily depict the action intended.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c1f5b7af-35a2-4623-a2a7-0956bd8189bc&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Icons that serve an interactive function must be placed within an icon-only button. This ensures accessibility, and clear affordance for user interactions. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ce98df21-8940-4bb5-a1ff-4e2836389e74&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Icons should not be added to layouts with the intent of being interactive. Icons themselves do not support different states or interactions and must be placed within appropriate interactive components, such as buttons, to ensure usability and accessibility. |

#### Badge

Badges in buttons are used to display dynamic information that grabs the user's attention. They can be used for things like notifications, alerts, or filtering.

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Buttons have the states default, hover, pressed and disabled.
* **Disabled State Guidance:** We don't recommend using disabled buttons in most cases. They can be frustrating because they provide no feedback or information about why the button is disabled or what the user needs to do to enable it. This can lead to confusion and a negative user experience. This lack of guidance adds to the cognitive load and can make them inaccessible to neurodivergent people. In addition the low-contrast text is difficult to read for people with visual impairments. [User feedback from a Hotjar survey in the estimation funnel](https://docs.google.com/spreadsheets/d/1JzOYL405ef3BOIfBJ2nZwaXvxdSdubZNS04VhMvOJdo/edit?pli=1&gid=0#gid=0) showed that users didn't understand why the continue button was disabled and what they needed to do to enable it.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=37c6c561-5e6f-4be7-bdf3-9a5b4078e182&&collection=contentId-2832039962&height=880&occurrenceKey=null&width=640&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Keep the button active and mark mandatory fields as required. Show error messages when the user clicks the button but hasn't filled all mandatory fields. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=88a32d36-8f1d-47c8-835b-5015491f2efe&&collection=contentId-2832039962&height=880&occurrenceKey=null&width=640&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid using disabled buttons. |

**Loading:** This state is typically triggered when the action initiated upon click involves an API call or server query. This provides the user with a visual indication that their action is being processed. When a button is in a Loading state, the user can still navigate the page. However, if they initiate a new action before the previous one is completed, a message or alert may appear.

### Touch Target & Layout

* **Touch Target:** To ensure accessibility, the touch target of the 32px button has a height of 40px. For all other sizes, the touch target is the same height as the button.
* **Width Adaptability:** The width of the button adapts to the width of its content unless intentionally we span the width to the full of its container, specially in Mobile devices.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d634691c-e32b-4bf5-9935-ad4f443211a6&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use full width buttons on mobile devices. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=146638df-04ed-4b17-8f0b-1ac937b68528&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use full width buttons on smaller containers on desktop devices. |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Buttons solicit an action from the user and trigger that action. Buttons should be clear and inciting. Our users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb that encourages action, in the infinitive tense. For more information on content guidelines, please refer to UX Writing principles.

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** {Action Verb} + {Noun}, except in the case of common actions like "Done," "Close," "Cancel," or "OK."
* **Length Limits:** Under 4 words and/or 30 characters maximum in English.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9f013dfe-3057-4bc7-bb4a-cb38f1d0fddf&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Give actions a clear naming. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4c6c801d-30c3-4cef-8c30-ab4c2bc31691&&collection=contentId-2832039962&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't give actions a vague naming. |

---

## Accessibility (a11y)

Not documented
