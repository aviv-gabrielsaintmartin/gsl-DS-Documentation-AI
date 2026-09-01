<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830991419/Dropdown | Last modified: Aug 17, 2026 -->

# Dropdown

Dropdowns are used to select one option from a list.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d221454c-4668-4778-a3c7-639df216029b&&collection=contentId-2830991419&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Dropdown on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7279)
* [Dropdown on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-dropdown--docs)

---

## Usage

Dropdowns allow users to select one option from a list. They are most commonly used in forms.

### Platform

We use platform-specific dropdowns that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders and the appearance of the dropdown list.

**Web:** The label is always on top of the field. The placeholder is visible until an option is selected.

**iOS:** As on the Web, the label is always on top of the field, and the placeholder is visible until an option is selected. On iOS, we use the native dropdown list.

**Android:** The label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible when the field is active.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4c724899-9d8a-45df-afb2-049cee819c3a&&collection=contentId-2830991419&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use dropdowns to allow users to select one option from a list. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=058c7e46-9272-4aa5-952d-9243a27d0072&&collection=contentId-2830991419&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use the dropdown to display a list of actions. Use the action menu instead. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=36398a54-0790-4d7b-af6c-626c4692fc50&&collection=contentId-2830991419&height=906&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** It's possible to use dropdowns to filter pages, but for consistency reasons we recommend using the action menu instead. For now the dropdown only supports single-select — for multi-select, please use another component, e.g. the [checkbox group](https://zeroheight.com/626199550/p/41df87-checkbox-group). |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Dropdowns** | — | Used in forms to allow users to select an option from a list. | — |
| [**Action menu**](https://zeroheight.com/626199550/p/16f691-action-menu) | High | Displays a list of context-specific actions. | The list represents actions to trigger, not options to select |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, dropdowns contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

#### Icons

Icons can be added to the field and the dropdown list. They act as visual cues to provide clarity to the user. All icons are non-clickable.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3621f54e-da2b-4985-91cb-e35baaddf3ca&&collection=contentId-2830991419&height=616&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** If some items don't have an icon, remove all icons. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=82c081de-03f9-4948-9798-3c526a62315c&&collection=contentId-2830991419&height=616&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't mix list items with and without icons, as it reduces readability. |

#### Suffix

The suffix can be added to provide additional context.

---

## Behavior & Responsiveness

### Interaction

The dropdown list opens when the user clicks in the field. It closes when the user clicks on the button again, selects an option from the list, clicks outside the dropdown or presses the esc key.

### Position & Scrolling

By default, the dropdown list is positioned below the field. If there is not enough space below it, it is positioned on top of the field. When the options exceed the available space, the dropdown becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings. To avoid complexity, not all positions are available in Figma — feel free to detach the component.

### Interactive States & Loading

* **Default / Hover / Active / Disabled:** The field of the dropdown has the states default, hover, active, and disabled. It can be empty or filled, and it can be in an error state. When in an error state, the dropdown contains an error message. The field doesn't have a pressed state — instead, it changes to the active state when a user presses on it.
* **Dropdown list:** The rows in the dropdown list have the states default, hover and pressed. They can be selected or unselected.
* **Loading:** The loading state indicates to users that the data is loading and will appear shortly.

### Touch Target & Layout

* **Width Adaptability:** The width can be set to 100% (full-width) or 50% of the container. For special use cases it is also possible to define a fixed size. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Sentence-style capitalization for helper text, written as a full sentence with punctuation.
* **Label Formula:** Not documented.
* **Length Limits:** Labels: 1 line. Items: under 2 lines.

**Labels:** Labels inform users what to expect in the list of dropdown options. Keep the label short and concise by limiting it to 1 line of text.

**Placeholders:** Placeholder text is displayed in the field by default when no selection is made. This is important if the dropdown does not have a label above it. Use clear placeholder text for the dropdown trigger so that users understand the purpose.

**Helper text:** Should only be used when the user needs additional help to select the correct item from the dropdown menu.

**Items:** We recommend presenting the options in a logical or alphabetical order. Try to keep it under 2 lines.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
