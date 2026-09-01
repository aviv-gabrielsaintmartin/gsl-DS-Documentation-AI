<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831712357/Feedback+message | Last modified: Aug 21, 2026 -->

# Feedback message

Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6bf7c280-09de-4865-bab6-83ebcb56b809&&collection=contentId-2831712357&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Feedback message on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7299)
* [Feedback message on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-feedbackmessage--docs)

---

## Usage

Feedback messages are used to provide guidance to the user about their current task or to provide general information about things like system processes. They persist until they are dismissed or the issue that caused the notification is resolved.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=27da21a5-f039-4daa-88fc-78b77db33ead&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use feedback messages to provide guidance related to the user's current task. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=295a06f5-7a9f-4548-81bd-41667c0db1d4&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use feedback messages for general information related to the system or website/app. |
| **DO:** Use feedback messages to confirm actions. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9b57f21a-4e70-4871-8aa9-13a67a137bb1&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use feedback messages for warnings or non-critical errors. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=10cc97e1-a5b7-46a1-a9cd-7da3086eeb2d&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use feedback messages for critical information that interrupts the user flow. Use alerts instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| [Snackbar](https://zeroheight.com/626199550/p/54ff4c-snackbar) | Low | Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that don't require user confirmation. | Seeker saves listing to favorites |
| **Feedback message** | Medium | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. They inform users of system processes or provide additional information about a task. They can be used for critical alerts or as passive feedback. | Seeker receives warning that he has reached the limit of saved searches |
| Banner (not a gemini component) | Medium | Banners are used for important, persistent information. They remain until the user closes them or the problem that caused the banner is solved. | Seeker is shown static information about search results on map |
| [State message](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/ced82a7a5e) | Medium | State messages are used for inline feedback in forms to guide users, correct errors, or provide additional information. | User enters incorrect password |
| [Alert](https://zeroheight.com/626199550/p/7142d3-alert) | High | Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken. | Agent deletes listings |
| [Info State](https://zeroheight.com/626199550/p/84818f-info-state) | High | Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states. | User is not connected to the Internet |

---

## Variants & Modifiers

### Type

Feedback messages come in the following types: info, success, warning, and error.

### Floating and corner radius

Feedback messages can be floating and non-floating. The floating version floats above the content, the non-floating one is used inline with the content.

Feedback messages are available with and without corner radius. The version without corner radius is manly used to create floating banner at the top of the page.

#### Breakpoints

We recommend displaying the the floating feedback message with rounded corners on desktop and without corners (as a banner) on tablet and phones.

### Modifiers

#### Title and description

Titles are optional, but recommended for clarity. Descriptions are mandatory.

#### Buttons

Feedback messages are available with 1 - 2 buttons or without buttons.

#### Close button

Dismissible messages have a close button (x-icon), non-dismissible messages don't. Whether a message should be dismissible or not depends on the information you want to communicate. For example, critical global messages should stay displayed permanently, and errors should stay displayed until the problem that caused the error is fixed. A simple success confirmation, on the other hand, can be dismissible.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9b57f21a-4e70-4871-8aa9-13a67a137bb1&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use close buttons when the feedback message provides non-critical information that users can dismiss after reading. This helps reduce visual clutter and allows users to focus on other important tasks without being repeatedly reminded of the same message. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=295a06f5-7a9f-4548-81bd-41667c0db1d4&&collection=contentId-2831712357&height=1080&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use close buttons for feedback that requires ongoing action. Keeping it visible ensures that the reminder stays in place until addressed. |

---

## Behavior & Responsiveness

### Interactive States & Loading

Feedback messages either appear in response to user actions, or they appear automatically to notify users of system processes. Dismissible feedback messages can be closed by clicking the x-button. Non-dismissible messages are either persistent or disappear when the issue that caused the message gets solved.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web and Android** | On web and Android the alignment of the buttons depends on the breakpoint. To learn more, see the [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). |
| **iOS** | On iOS the alignment is done manually. |

---

## Content & UX Writing

#### Title

The title should be short and concise. Titles are optional, but recommended to improve clarity.

#### Description

Descriptions are mandatory. Use clear and simple language and don't overwhelm the user with too much information. Provide clear instructions or next steps, especially when users need to take action. Keep descriptions to 1-2 sentences.

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like "Done," "Close," "Cancel," or "OK." Use sentence case without punctuation. Try to keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/v/latest/p/324518-intro) and [Feedback message guidelines](https://gemini.zeroheight.com/styleguide/s/92948/p/348cca-feedback-messages).

---

## Accessibility (a11y)

Not documented
