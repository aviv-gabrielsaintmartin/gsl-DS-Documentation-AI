<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831253628/Info+state | Last modified: Aug 21, 2026 -->

# Info state

Info states are placeholders used to inform users about success, error and empty states.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=382ced04be02&id=19b20c35-feef-430a-bf8e-c8ef6c023378&&collection=contentId-2831253628&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Info state on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7261)
* [Info state on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-infostate--docs)

---

## Usage

Info states are used to communicate system status, errors, or other relevant information to users. They typically include:

* **Empty states:** Shown when there is no content to display or resources are missing
* **Error states:** Indicates problems such as network outages
* **Success states:** Acknowledge successful actions, such as submitting a form
* **Loading states:** Notifies users that data or content is being processed or loaded

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=be3d4b76d9e5&id=3b58f986-17cb-407a-a1e9-e54d1025c256&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the info state component for empty states, when there is no data to display. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5be44c382643&id=df406bc7-12cd-48dd-af41-31f08ee894ec&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use info states to display errors such as network outages. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a132f917fccc&id=75c426a2-b92f-4329-92a6-26c4b3b44c75&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use info states to confirm successful actions. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6a0aae10ed93&id=61f04a8d-d20a-43ca-b29a-cd12a2b24551&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use info states to inform users that content is loading. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=da9d9ce509ca&id=40ee0f27-70fa-4740-93e0-8527b3829628&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use info states for quick inline notifications. Use feedback messages instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=34f3268554e5&id=bd203b8b-1735-4360-b8b0-072840cae7a3&&collection=contentId-2831253628&height=1160&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use info states for warnings or errors that should block the user flow. Use alerts instead. |

### Related Components

| Component | Priority | Usage | Example |
| --- | --- | --- | --- |
| [Snackbar](https://zeroheight.com/626199550/p/54ff4c-snackbar) | Low | Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that don't require user confirmation. | Seeker saves listing to favorites |
| [Feedback message](https://zeroheight.com/626199550/p/8754bc-feedback-message) | Medium | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. They inform users of system processes or provide additional information about a task. They can be used for critical alerts or as passive feedback. | Seeker receives warning that he has reached the limit of saved searches |
| Banner (not a gemini component) | Medium | Banners are used for important, persistent information. They remain until the user closes them or the problem that caused the banner is solved. | Seeker is shown static information about search results on map |
| [State message](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/ced82a7a5e) | Medium | State messages are used for inline feedback in forms to guide users, correct errors, or provide additional information. | User enters incorrect password |
| [Alert](https://zeroheight.com/626199550/p/7142d3-alert) | High | Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken. | Agent deletes listings |
| Info State | High | Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states. | User is not connected to the Internet |

---

## Variants & Modifiers

### Modifiers

#### Illustration/Icon

Info states can be used with an icon, an illustration, or neither. You can't use them with an icon and an illustration at the same time.

If you use an illustration we recommend the usage of hero illustrations.

| With illustration | With icon | No icon/illustration |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c2c2a3d9fced&id=02b0c0ae-4bbb-4eee-a43a-dbe85f645063&&collection=contentId-2831253628&height=872&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=2038dbcc6198&id=27d4309e-4c61-4b43-a67e-eab0b16b469a&&collection=contentId-2831253628&height=632&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=734564fb2942&id=674ff2d8-070c-463d-9cc6-be2e7870e3b7&&collection=contentId-2831253628&height=520&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Figma tip:** To select the correct illustration, go to the common page in the illustration library. For example: [Common Hero Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-312).

There you will find illustrations for most use cases, such as informational purposes, error messages, and more. If you can't find the illustration you're looking for, please request it on #gemini_symbols.

[Learn more about the symbol library process](https://kugawana.slack.com/archives/C03HLJU6E3U/p1723193835245029)

#### Title and description

Both title and description are mandatory.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=d067cd55733d&id=674ff2d8-070c-463d-9cc6-be2e7870e3b7&&collection=contentId-2831253628&height=520&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Buttons

Info states can be used with 1-2 buttons, or without any. If two buttons are used, we recommend combining the primary and tertiary buttons.

They should be used when they provide clear next steps or actions for users, such as retrying after an error, navigating to another page, or resolving an issue.

| With two buttons | With one button | Without buttons |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5ca729a4b638&id=674ff2d8-070c-463d-9cc6-be2e7870e3b7&&collection=contentId-2831253628&height=520&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=bb0e66544db6&id=614c26e4-68e4-43c8-b86a-2c3478965df2&&collection=contentId-2831253628&height=408&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=55674fb46b2d&id=252b4d5b-c2e9-4780-9220-db77c429da92&&collection=contentId-2831253628&height=248&occurrenceKey=null&width=1192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

Info states appear in response to system events such as errors, loading processes, empty content, or successful actions.

They disappear when the user takes action, such as retrying or navigating away, or when the system resolves the problem on its own, such as completing a load process. In some cases, they disappear automatically after a short period of time, or they may require manual dismissal by clicking an action button.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=e957ed923f49&id=da9f29cc-5e99-4c42-a6cc-4f3c33411453&&collection=contentId-2831253628&height=856&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

The width of the info state and its buttons depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Layout | Breakpoint behavior |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=59c830891d78&id=f0973abb-ae0e-479a-9ec2-0b0ce741194b&&collection=contentId-2831253628&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **Width: 100%** | Web: XXS - XS (0 - 599 px) Android: Compact (0 - 599 dp) iOS: device 0 - 523 px |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=26b52e86fd11&id=1fc5867f-0f01-4ff8-9612-608b53b791e4&&collection=contentId-2831253628&height=1440&occurrenceKey=null&width=2560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **Reduced width** | Web: SM - XXXL (> 599 px) → width: 50%, max-width: 570px Android: Medium - Expanded (> 599 dp) → max-width: 429 dp iOS: device > 524 px → max-width 524 px |

---

## Content & UX Writing

* **Title:** The mandatory title should be short and concise. It should contain a brief and clear statement or question.
* **Description:** Descriptions are mandatory and are used to give additional context and details. Use clear and simple language and don't overwhelm the user with too much information. Tell the user what happened and what they need to do to proceed. Don't blame the user. Stay positive and empathetic but don't say please and sorry. Don't use "Oops". Keep the description to 1-2 sentences.
* **Buttons:** Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb in the infinitive tense, using the {verb} + {noun} formula, except for common actions like "Done," "Close," "Cancel," or "OK." Use sentence case without punctuation. Keep it under 4 words and/or 30 characters maximum in English.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro) and [Info state guidelines](https://zeroheight.com/626199550/v/latest/p/85a997-info-state).

---

## Accessibility (a11y)

Not documented
