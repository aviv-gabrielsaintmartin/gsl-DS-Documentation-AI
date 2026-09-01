<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831155273/Modal+bottom+sheet+menu | Last modified: Aug 21, 2026 -->

# Modal bottom sheet menu

Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=b323c6833d1a&id=5b5e50c6-7d6a-4142-a5ce-7a4f476edaed&&collection=contentId-2831155273&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

* [Modal bottom sheet menu on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=16366-21887&t=CDJo3x00MVOumTTf-4)
* [Modal bottom sheet menu on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/story/ui-navigation-actionmenu--default)

---

## Usage

Modal bottom sheet menus display a list of context-specific actions in a bottom sheet. As with the action menu, they are used when additional options are available to the user, but space is limited. They are only used on mobile screens or on apps.

### Platform

On web the modal bottom sheet menu is part of the Action menu. The bottom sheet is only displayed on breakpoints smaller than SM. On larger breakpoints the action menu displays a dropdown list.

On iOS/Android the modal bottom sheet menu and action menu are two separate components that can be used regardless of the screen size.

The style of the modal bottom sheet slightly differs between each platform. For more information please refer to the modal bottom sheet documentation.

| Web mobile & iOS/Android | Web desktop & iOS/Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3155c4c38dbe&id=13dbedd3-5b35-4bb4-99bf-be5156eefeb2&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Modal bottom sheet menu | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=244c6c1ba133&id=64554f0e-e997-4b57-8a4c-269c4737171a&&collection=contentId-2831155273&height=486&occurrenceKey=null&width=680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Action menu |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=d5d91ffa4d52&id=dad7d28d-d809-4eb6-8a9e-77497f0829ed&&collection=contentId-2831155273&height=792&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use modal bottom sheet menus to display a list of actions on mobile devices or in apps. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6c7534fb1832&id=b87a3fe2-0967-4ab3-a70e-e1a34c2a8caf&&collection=contentId-2831155273&height=1492&occurrenceKey=null&width=1536&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use modal bottom sheet menus on breakpoints larger than XS (in Web). Use the action menu instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Modal bottom sheet menu** | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. |
| **Action menu** | Action menus display a list of context-specific actions. Although they are primarily used on desktop, they can also be used in apps if they contain only a few actions. |

---

## Variants & Modifiers

### Modifiers

#### Trigger

Like the action menu, the modal bottom sheet menu can be opened with the following button types: tertiary icon button, floating icon button and text button.

If you use a different trigger, please share your use case with us so we can improve our guidelines and documentation.

| Tertiary icon button | Floating icon button | Text button |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f8d4a324292c&id=5bc6924d-5bb0-4122-a473-81a7f0dd9a58&&collection=contentId-2831155273&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6377e9c31998&id=9d8dd9e6-ff6d-47a7-b8cc-56833de02baf&&collection=contentId-2831155273&height=112&occurrenceKey=null&width=112&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=2aaba70c8dd2&id=4cbc1255-d626-4605-b849-d7c5175900c6&&collection=contentId-2831155273&height=80&occurrenceKey=null&width=158&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Header

The modal bottom sheet menu contains an optional header. It has a close button on the left, a title in the middle and either a secondary button or up to 2 icons on the left. All elements of the header are optional.

| With header | Without header |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=741fee0b8701&id=5ceae9ca-d739-44f6-802f-82d414e462a5&&collection=contentId-2831155273&height=984&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=905d65f0e34e&id=2d2af4c2-c889-4660-8cb3-cc3ec5a50e03&&collection=contentId-2831155273&height=984&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Icons

Icons can be added to the menu list. They act as visual cues to provide clarity to the user.

| With icons | Without icons |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=752bd26d8c1c&id=00a8e3f5-f48b-4bee-90bf-00d03c33fc93&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7734e14ecdf5&id=202dd503-3975-4d86-ad45-645376b34c0d&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Title & body text

Each menu item contains a body text and an optional title.

| Body text | Title and body text |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=94315561d098&id=00a8e3f5-f48b-4bee-90bf-00d03c33fc93&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f86e1605aa92&id=ad84f7e6-6cb3-4d2e-b7df-b229d63b5b94&&collection=contentId-2831155273&height=736&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Actions & links

Menu items can be actions or links. If the menu item is a link, the external link icon is displayed.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=84f1526796fa&id=341e722e-1e57-486b-bff5-426b0ac64502&&collection=contentId-2831155273&height=736&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

### Interactive States & Loading

The items in the menu list have the states default, hovered, and pressed. They can be selected or unselected.

| Unselected | Selected |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4e08854ae7ee&id=4105792e-5dab-45ba-ab9e-e9b3d7134a5a&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=633f557839fc&id=0bc3706a-fa9d-4101-8f7b-4942a566cff2&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

Tappable items within the menu must meet a minimum touch target of 44×44pt (iOS) / 48×48dp (Android). The sheet itself occupies full viewport width on mobile. On tablet, maximum width is 560px, centered.

### Interaction

The modal bottom sheet menu opens when the user clicks or taps on a button. When it's focused, it can also be opened by pressing the return key or the space bar.

It closes when the user selects an option from the list, clicks on the close button, clicks outside the modal bottom sheet menu or presses the esc key. On apps it is possible to close it by dragging the modal down.

| Selecting and closing | Clicking the x-button | Closing | Dragging modal |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=776028eb98b3&id=7cc380f4-e41c-4f14-95ab-4a165f04ca18&&collection=contentId-2831155273&height=696&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Clicking an option | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4f9da5749216&id=ccab81d5-74c7-4379-895c-28a11b7854b6&&collection=contentId-2831155273&height=696&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web and app | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4ab57001bdc1&id=3ceca9d3-4200-43df-b2d7-b27290731719&&collection=contentId-2831155273&height=696&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Clicking outside the action menu or pressing esc | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6a211d526bbb&id=8b607fc3-8e00-414b-b5f7-e02ae7384cfe&&collection=contentId-2831155273&height=696&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) App only |

### Breakpoints & Platform Adaptations

On the Web, for XXS and XS breakpoints (from 0 to 600px) the modal bottom sheet menu is used. For the breakpoints above SM, the action menu is used.

On Android and iOS both components can be used regardless of the screen size.

To learn more about our breakpoints, see our grids and breakpoint guidelines.

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=092dfe483787&id=13dbedd3-5b35-4bb4-99bf-be5156eefeb2&&collection=contentId-2831155273&height=568&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **Modal bottom sheet menu** | Web: XXS to XS (0 - 599 px) Android and iOS: used on all breakpoints |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a45fcc3d970c&id=64554f0e-e997-4b57-8a4c-269c4737171a&&collection=contentId-2831155273&height=486&occurrenceKey=null&width=680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **Action menu** | Web: SM to XXXL (> 599 px) Android and iOS: used on all breakpoints |

### Scrolling

When the content exceeds the available space, the modal bottom sheet menu becomes scrollable. For more information please refer to the modal bottom sheet documentation.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=8a1ad68b9515&id=e5a56af2-acd0-4e16-b2ed-36f055ea72f7&&collection=contentId-2831155273&height=802&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Content & UX Writing

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** Lead with an action verb that encourages action, in the infinitive tense.
* **Length Limits:** Try to keep it under 2 lines.

For more information on content guidelines, please refer to the UX Writing principles.

---

## Accessibility (a11y)

Not documented
