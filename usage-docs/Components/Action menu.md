<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831482931/Action+menu | Last modified: Aug 13, 2026 -->

# Action menu

Action menus display context-specific actions in a dropdown list.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1e2ffc34-75ce-4880-9900-3425095a3c7b&&collection=contentId-2831482931&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | To Do 🚧 |

* [Action menu on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7287)
* [Action menu on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-actionmenu--docs)

---

## Usage

Action menus display a list of context-specific actions in a dropdown list. They are used when additional options are available to the user, but space is limited.

The action menu does not support submenus or subsections.

### Platform

We use platform-specific action menus that differ between Web/Android and iOS. The difference is the position of the icons and that we use a native dropdown list on iOS. On iOS a destructive action is available; on Web/Android it's not.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=32f036a8-043c-436d-9534-94d19b677878&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use action menus to display a list of actions. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d9223e2b-5ec1-49f3-86b5-c7ed20ca7f2a&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use action menus as selection elements inside a form. Use dropdowns instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b0a52c93-2e1b-4e92-a8ef-d41889ae04f7&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use action menus to filter pages. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0d0a640e-6afe-4119-9396-75472b10d533&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use a backdrop behind the action menu. If you want to block the content, use a modal bottom sheet instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Action menu** | Action menus display a list of context-specific actions. Although they are primarily used on desktop, they can also be used in apps if they contain only a few actions. |
| [**Modal bottom sheet menu**](https://zeroheight.com/626199550/p/28f40b-modal-bottom-sheet-menu) | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. |
| [**Dropdowns**](https://zeroheight.com/626199550/p/98cf75-dropdown) | Dropdowns are used in forms to allow users to select an option from a list. |

---

## Variants & Modifiers

### Modifiers

#### Trigger

The action menu can be opened with the following button types: tertiary icon button, floating icon button and text button.

If you use a different trigger, please share your use case with us so we can improve our guidelines and documentation.

| Tertiary icon button | Floating icon button | Text button |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=32f036a8-043c-436d-9534-94d19b677878&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Use icon buttons when space is limited or the action is commonly recognized, such as the three-dot menu icon. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b0a52c93-2e1b-4e92-a8ef-d41889ae04f7&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Use a floating icon button when the action menu is on top of a image or map. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=efe940ba-57dd-4f78-8766-833e030fb92c&&collection=contentId-2831482931&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Use a text button when the action needs to be explicitly clear, especially for less common or more complex tasks. Use it to filter pages. |

#### Icons

Icons can be added to the dropdown list. They act as visual cues to provide clarity to the user. On Web/Android the default icons are on the left and the external link icon on the right. On iOS all icons are on the right.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=efaf64f6-b1f4-4111-95b6-aae32140eb07&&collection=contentId-2831482931&height=896&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** If some items don't have an icon, remove all icons. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3112c272-935f-490e-a544-3927b17ce0a2&&collection=contentId-2831482931&height=858&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't mix menu items with and without icons, as it reduces readability. |

#### Menu items

Menu items can be actions or links. If the menu item is a link, the external link icon is displayed.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e67e7270-1a7c-4b99-bace-19b1c168a026&&collection=contentId-2831482931&height=560&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Links are marked with the external link icon. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=34019715-32eb-4e12-b49b-23a57603fdf9&&collection=contentId-2831482931&height=560&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't hide the link icon, as it can be misleading to the user. |

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hovered / Pressed:** The items in the dropdown list have the states default, hovered, and pressed. They can be selected or unselected.
* **Interaction:** The action menu list opens when the user clicks or taps on the button. When it's focused, it can also be opened by pressing the return key or the space bar. It closes when the user clicks on the button again, selects an option from the list, clicks outside the action menu, or presses the Esc key. It's not possible to have two or more action menus open at the same time on the same page.

### Touch Target & Layout

* **Position:** The dropdown menu can appear at the bottom, top, left, or right of the opening trigger. The opening trigger can be aligned to the left, center, or right. On iOS, it's not possible to position the menu manually — it uses the default native behavior. To avoid complexity, not all positions are available in Figma; feel free to detach the component.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web — Mobile (0–600px, XXS/XS)** | A [modal bottom sheet](https://zeroheight.com/626199550/p/5942fd-modal-bottom-sheet) is used instead of the dropdown list. |
| **Web — Desktop (>600px, SM and above)** | The dropdown list is used, 320px wide by default, or set to hug the content. See our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). |
| **Android / iOS** | Both the dropdown list and modal bottom sheet components can be used regardless of screen size. |

### Scrolling

Scrolling is technically possible, but we don't recommend using it. We recommend using fewer options or using a [modal bottom sheet menu](https://zeroheight.com/626199550/p/28f40b-modal-bottom-sheet-menu) in apps.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=92aca55b-6bd2-4458-aa70-f9f3774349b5&&collection=contentId-2831482931&height=896&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use fewer options to prevent scrolling. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c3bc443e-b9c6-4b4a-97a3-451ea3ba99d9&&collection=contentId-2831482931&height=896&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid using too many menu items to prevent usability issues. For longer lists consider using a modal bottom sheet menu on apps. |

---

## Content & UX Writing

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** Lead with an action verb that encourages action, in the infinitive tense.
* **Length Limits:** Try to keep menu item labels under 2 lines.
* For more information, refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
