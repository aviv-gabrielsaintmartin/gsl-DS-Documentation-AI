<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831843417/Snackbar | Last modified: Aug 21, 2026 -->

# Snackbar

Snackbars are used to provide quick feedback after an action is taken.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d478d135-2d60-42a4-b88d-708ecb37d930&&collection=contentId-2831843417&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Not documented | Ready ✅ | Ready ✅ | Ready ✅ |

* [Snackbar on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7301)
* [Snackbar on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-snackbar--docs)

---

## Usage

Snackbars are short messages that appear at the bottom of the screen to inform users of the outcome of an action without interrupting their current activity. They should be used to provide quick, non-intrusive feedback that doesn't require user confirmation before proceeding. They don't block the user from continuing their task. An action may be encouraged, but not required.

### Platform

The snackbar has a close button (x-icon) on the web. On iOS/Android, it doesn't have a close button, but disappears automatically after 4 seconds.

| Web | iOS/Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b64abaaa-ecf2-4f5d-960d-616eee588ac6&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=55b51b87-6040-4db7-907a-fd30ee3b05fc&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e7950bc7-1867-454c-9bd2-842ef0ceaaf4&&collection=contentId-2831843417&height=840&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use snackbars to provide non-critical feedback after an action has been taken. For example, saving, sending, or deleting items. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=50068a95-fab4-42cf-9647-a03d39d352bd&&collection=contentId-2831843417&height=840&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use snackbars for non-intrusive feedback on actions that doesn't require user confirmation before proceeding. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3165a2c5-c52d-4da3-8fa4-a0353e8ae5b4&&collection=contentId-2831843417&height=840&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use snackbars for static information that are not a result of a user action. Use feedback messages instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cf34fb1c-fce2-408c-8af0-1e4fdb36b8ef&&collection=contentId-2831843417&height=840&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use snackbars for error messages that point to a specific part of the page. Use feedback messages instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=fb6d8665-1b87-4b84-9daa-031d03c5256e&&collection=contentId-2831843417&height=840&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use snackbars for critical messages that require the users attention. Use feedback messages or alerts instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cb2c212c-c0b8-47be-ba17-51a5c336cf33&&collection=contentId-2831843417&height=848&occurrenceKey=null&width=722&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use snackbars if you need to block the users flow. Use alerts instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Snackbar** | Low | Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that doesn't require user confirmation before proceeding. They don't block the user from continuing their task. An action may be encouraged, but not required. | Seeker saves listing to favorites |
| [**Feedback messages**](https://zeroheight.com/626199550/p/8754bc-feedback-message) | Medium | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. They inform users of system processes or provide additional information about a task. They can be used for critical alerts or as passive feedback. | Seeker receives warning that he has reached the limit of saved searches |
| **Banner** (not a gemini component) | Medium | Banners are used for important, persistent information. They remain until the user closes them or the problem that caused the banner is solved. | Seeker is shown static information about search results on map |
| [**State message**](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/ced82a7a5e) | Medium | State messages are used for inline feedback in forms to guide users, correct errors, or provide additional information. | User enters incorrect password |
| [**Alert**](https://zeroheight.com/626199550/p/7142d3-alert) | High | Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken. | Agent deletes listings |
| [**Info State**](https://zeroheight.com/626199550/p/84818f-info-state) | High | Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states. | User is not connected to the Internet |

---

## Variants & Modifiers

### Type

Snackbars come in the following types: info, success, warning, and error. These variations help users quickly understand the nature of the message, whether it's informational, confirms success, issues a warning, or highlights an error.

| Info | Success | Warning | Error |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=804d3452-ee7e-4876-a440-7c8e83c42fea&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7d6b3ea8-a3f6-4f10-9bbd-d5d986b518f0&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f45b8b40-8a0d-429c-ad27-8295347f74c4&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5c1a13b9-ef70-43ce-8fff-2bf44038fd01&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The icons associated with each snackbar type are standardized and shouldn't be changed to ensure consistency and clarity across our products.

### Actions

Snackbars contain optional action buttons. Short actions appear on the same line as the snackbar message, longer actions appear below the snackbar message.

| Short action | Long action | Without action |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=85dc41a2-7d9a-484a-90aa-d8543c9d6bf9&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=96dfd448-fff3-4913-a39f-87478b41db94&&collection=contentId-2831843417&height=256&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6a8452eb-cbce-4c35-b39f-ac6326df80cc&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

Snackbars appear in response to a user action, such as clicking a button, submitting a form, or completing a task.

**Web:** On the web, snackbars remain on the screen until the user clicks the close or action button to dismiss them. For accessibility reasons we can't make snackbar disappear automatically on web. Learn more: [WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG21/Understanding/timing-adjustable.html)

**App:** On iOS and Android, snackbars can be either auto-dismissable or persistent. Auto-dismissable snackbars disappear automatically after 5 seconds (default value) or when the action button is clicked. Persistent snackbars remain until the user takes an action. We recommend using auto-dismissable snackbars only for noncritical messages.

| Web — clicking the close button | Web — clicking the close button | iOS/Android — clicking action button or waiting 5 seconds |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0d317b02-cb25-49c8-9d96-d85207e8fe6b&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=07f5efa6-d718-4a23-9065-334ced1abc4d&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4f32b4f6-339c-43c0-962d-9c3acd4919f8&&collection=contentId-2831843417&height=176&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Snackbars are positioned on the bottom of the screen. On web the spacing from the bottom depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

#### Single snackbars

| Phone | Phone (above navigation bar) | Phone (above button bar) | Tablet | Desktop |
| --- | --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=24ab0ff8-5a0e-40e4-9269-7f02fd453c46&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b0a1af62-c0f5-4cef-b7fc-c3dce218b015&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=056490bc-c129-4c67-86c8-6fb091b82192&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0efee3fe-1e1f-4f13-8949-7d4cb5cac132&&collection=contentId-2831843417&height=500&occurrenceKey=null&width=1686&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: SM - LG (600 - 1279 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d7accbe6-7eae-4782-a133-9287891b1721&&collection=contentId-2831843417&height=500&occurrenceKey=null&width=1686&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XL - XXXL (> 1279 px) |

#### Stacked snackbars (Web only)

| Phone | Phone (above navigation bar) | Phone (above button bar) | Tablet | Desktop |
| --- | --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=500cbcb1-8d20-4e45-946a-47e57dc1d951&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=addd6921-d39d-4dda-a2ca-9ef3a9438ed2&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b3d4a300-eba6-4810-9526-70e0b18291cf&&collection=contentId-2831843417&height=556&occurrenceKey=null&width=808&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9460b102-2a1b-430d-a372-dc66c3a9aa81&&collection=contentId-2831843417&height=500&occurrenceKey=null&width=1686&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: SM - LG (600 - 1279 px) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=38bcf6ef-b8c1-4504-aefc-9adabfe6a1c6&&collection=contentId-2831843417&height=500&occurrenceKey=null&width=1686&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XL - XXXL (> 1279 px) |

Snackbars can only be stacked on the web. On apps, only one snackbar is visible at a time. When a second snackbar appears, the previous one disappears.

---

## Content & UX Writing

* **Capitalization:** Not documented
* **Voice & Tone:** Write in an active voice and clearly state what happened as a result of the user's action, avoiding unnecessary details. Make sure the message is straightforward and easy to understand at a glance. For example: "Message sent."
* **Label Formula:** Use a concise, verb-based label for the action button. For example: "Undo"
* **Length Limits:** Keep the message to 1-2 sentences.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

* **Keyboard Navigation:** Not documented
* **Screen Readers:** Not documented
