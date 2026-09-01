<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831581316/Modal+bottom+sheet | Last modified: Aug 21, 2026 -->

# Modal bottom sheet

Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f92f2203-ccaf-485c-95b9-58161c1874c6&&collection=contentId-2831581316&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| [Modal bottom sheet on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7293) | Ready ✅ | Ready ✅ | Ready ✅ |

[Modal bottom sheet on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-modal--docs)

---

## Usage

Modal bottom sheets are used to display contextual information that is related to the current screen or to offer actions that are relevant to the user's current context.

### Platform

We use platform-specific modal bottom sheets that differ between Web, iOS and Android.

#### Web

On the Web, the component appears as a bottom sheet on phones and as a modal on desktop. The modal bottom sheet is not draggable on the Web.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e8da2de9-d708-49cf-af48-a5cce9bee871&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Phone

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d9b5372c-98d6-470b-9899-52ca6b3973d9&&collection=contentId-2831581316&height=698&occurrenceKey=null&width=1242&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Desktop

#### iOS

On iOS, we use native, draggable modal bottom sheets. As on the web, the component looks like a bottom sheet on phones and a modal on tablets. The tablet modals have a fixed height on iOS. If you have a small amount of content, please use the pop-up component instead.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d42b5500-4a0d-4088-93eb-2a1b1a661244&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Phone

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9e07e305-cd7c-4f04-a8d3-384ed763b587&&collection=contentId-2831581316&height=931&occurrenceKey=null&width=698&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Tablet Portrait

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f6770f3f-3b15-4c0e-abeb-0adc6a549bc7&&collection=contentId-2831581316&height=698&occurrenceKey=null&width=931&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Tablet Landscape

#### Android

On Android we use native, draggable modal bottom sheets. The component appears as a bottom sheet on phones. On tablet you can choose between a bottom sheet (`ModalBottomSheet`) or a modal (`SheetSuite`).

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9559cfe4-77bc-4035-93ea-829ed48eb84e&&collection=contentId-2831581316&height=384&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use modals when it's important to get the user's full attention. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0371af13-5db2-4752-b85f-a89c64f87806&&collection=contentId-2831581316&height=384&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use modal bottom sheets when the information or action isn't urgent or can be completed inline without interrupting the user's flow. They can be disruptive if overused. Use other components such as feedback messages, snackbars or info states. |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b60f9460-68c0-426a-8f9d-349d170ee52c&&collection=contentId-2831581316&height=384&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use a modal bottom sheet to present additional content, actions or supplementary information related to the current context. |

### Related Components

| Component | Usage |
| --- | --- |
| **Modal bottom sheet** | Modal bottom sheets are used to display contextual information that is related to the current screen or to offer actions that are relevant to the user's current context. |
| [**Alert**](https://zeroheight.com/626199550/p/7142d3-alert) | Alerts are used for critical information that requires immediate attention or confirmation before proceeding. Since the alert has not yet been developed for the Web, modal bottom sheets should be used instead. |

---

## Variants & Modifiers

### Sizes

The modal bottom sheet is available in different heights.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a06e4f30-0c96-4425-b55d-1f6a9704f247&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the default size when the modal contains a small amount of content. Since the height adjusts to fit the content, it's ideal for compact information or simple actions that don't require scrolling. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d0cafef2-b1b4-478d-9116-e226d3ce59b7&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the full-height size when the modal contains a large amount of content and may require scrolling. The fixed height ensures consistency within flows. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d3ce3b92-9d8b-4dee-bcc1-5cc7cd66f217&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use full-screen size for extensive content or detailed data entry. Full-screen modals are ideal when users need to focus solely on the modal content without distractions. It's useful for displaying maps or full-width images. |

### Modifiers

#### Padding

The modal bottom sheet can be used with or without padding.

| With padding | Without padding |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5aeed650-d5d6-4552-9a96-bc5290c6df53&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ed6d878e-f33b-4520-a9e0-fab60f78364d&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8f2eb5a2-9a06-48dc-9816-13bf7f969766&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the modal bottom sheet with padding for most use cases. The padding helps separate text, illustrations and components from the border. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=206c9148-6812-40a1-8551-ccc94ea9aeb6&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the modal bottom sheet without padding when you want to display maps or images in full width. |

#### Header and footer

The modal bottom sheet contains an optional header and footer.

| Header and footer | Only footer | Only header |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1891ce72-6f32-4210-bbb4-22f8c12d54d4&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=25cf1d78-f4d6-48e8-a713-8431ccf6a74e&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6a7276c3-95c9-4b50-93d2-fa0d24869a27&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Header**

The header has a close button on the left, a title in the middle and either a secondary button or up to 2 icons on the left. All elements of the header are optional.

| Header with button | Header with 1 - 2 icons |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=23e8be27-e388-4a16-84df-6022252fe2d3&&collection=contentId-2831581316&height=58&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4f84e66b-4074-46cd-a9f8-ca509be8bfb9&&collection=contentId-2831581316&height=58&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| CAUTION |
| --- |
| **CAUTION:** If a close button is needed, it should be on the left. Please don't change the position in the top bar. |

**Footer**

The footer (bottom bar) has 1 - 2 buttons. They can be aligned horizontally or vertically. We recommend vertical alignment only if there is not enough space to align them side by side.

| Footer with 1 button | Footer with 2 horizontal buttons | Footer with 2 vertical buttons |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3c7313d1-ccb5-4c26-a49f-fd997abeab9b&&collection=contentId-2831581316&height=109&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6cfedfb4-1c79-4dbc-97f2-3402dc536220&&collection=contentId-2831581316&height=109&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=fa912d92-ae12-4e38-bd21-1b65e5874f55&&collection=contentId-2831581316&height=109&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interaction

Modal bottom sheets appear in response to a user action, such as clicking a button, submitting a form, or completing a task. They can also appear automatically based on user behavior, such as reaching a certain scroll depth, spending time on a page, or attempting to exit.

They can be closed by clicking the close button, performing an action, or clicking outside the modal. On iOS and Android, they can also be closed by dragging them down.

| Clicking the x-button | Clicking an action | Clicking outside | Dragging modal |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7bfe1957-c2db-44c1-b35c-b64e786597e9&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web and app | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=349e5cd8-f644-4616-a09b-1dc667e2969c&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web and app | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f99bb1c6-0012-4008-bb44-e0ba96a717e6&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web and app (can be defined by consumer) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6ce682fd-b23a-4c06-959d-7f349af33243&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) App only |

**X-button vs. cancel button**

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b92d795d-69f7-4723-9b09-e6dd932c571e&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** In most use cases, the close button is located in the upper left corner. The "X" is quick to locate and is best for quick exits. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d691aa22-95a4-478e-8bd4-67efd71b54fa&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When using modals as alerts that require users to take action or make a decision, include a "Cancel" button next to the primary action. |

### Scrolling

When the content exceeds the available space, the modal becomes scrollable, allowing users to access all the information without having to resize or close the modal. Whether the scrollbar is visible or not depends on the user's system settings. To better separate the content from the header, a divider line appears when the user scrolls the modal.

| Default | Scrolling |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bca5f8d5-50e0-4f81-9ccd-ce1f8add7c35&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c89857bc-1881-4e18-a325-3ffadf8bbcf7&&collection=contentId-2831581316&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Interactive States & Loading

Not documented

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

The style of the modal bottom sheet depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). Breakpoints are different on iOS and Android. Check the [platform documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet/t/a053439e7a) to see the differences.

| Bottom sheet | Modal |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e8da2de9-d708-49cf-af48-a5cce9bee871&&collection=contentId-2831581316&height=582&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - SM (0 - 767 px) Android: Compact (0 - 599 dp) iOS: iPhone | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d9b5372c-98d6-470b-9899-52ca6b3973d9&&collection=contentId-2831581316&height=698&occurrenceKey=null&width=1242&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: MD - XXXL (> 767 px) Android Medium - Expanded (> 599 dp) iOS: iPad |

---

## Content & UX Writing

**Title:** The title should be short and concise. Titles are optional, but recommended to improve clarity and explain the purpose of the modal.

**Content:** Give users enough context within the modal itself to understand what they're being asked to do without having to refer to the main screen. Format the modal content with headings, bulleted lists, or short paragraphs to make it easy to read quickly. Include only essential information; remove anything irrelevant to the decision or action the user needs to take.

**Buttons:** Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** {Action Verb} + {Noun}, in the infinitive tense, leading with an action verb — except for common actions like "Done," "Close," "Cancel," or "OK."
* **Length Limits:** Keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
