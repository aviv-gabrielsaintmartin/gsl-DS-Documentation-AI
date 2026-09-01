<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830958639/Checkbox | Last modified: Aug 17, 2026 -->

# Checkbox

Checkboxes are used to select one or more options from a list.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7a90065a-2960-4cd1-b36f-e5fc83eca4ce&&collection=contentId-2830958639&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Partially available |

* [Checkbox on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7276)
* [Checkbox on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-checkbox--docs)

---

## Usage

Checkboxes are selection components that are used for multiple choices. They allow the user to select none, one or more items. They can also be used to display a single option that requires acceptance or confirmation before submission.

### Platform

On the web and iOS, we use custom checkboxes. On Android, we use native checkboxes.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=964924cf-3caf-414a-a115-228b3f4a7390&&collection=contentId-2830958639&height=288&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use a standalone checkbox in forms where the selection takes effect only after the form is submitted. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d331392a-bf45-4f5b-9c39-8751707ca1fb&&collection=contentId-2830958639&height=288&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid using a checkbox to toggle a state on and off immediately. Use a switch instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e40ba756-3ebf-4914-8222-1195d1d11023&&collection=contentId-2830958639&height=480&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use checkboxes to allow users to select one or more options in a list of related choices. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=517ed2c9-01da-4ee8-8e39-32048ac7bbd9&&collection=contentId-2830958639&height=536&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use checkboxes for mutually exclusive choices or when only one item can be selected. Use radio buttons instead. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1d88d87a-ebd5-4e48-960c-608a7f6b6e31&&collection=contentId-2830958639&height=480&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** When you want to use checkboxes in a list, consider using the checkbox group component. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Checkbox** | — | Allows users to select one or more choices independently; used in forms that must be submitted before the change takes effect. | — |
| [**Radio button**](https://zeroheight.com/626199550/p/55bfd7-radio-button-group) | High | Mutually exclusive choices, submitted before the change takes effect. | Only one option can ever be selected at a time |
| [**Toggle**](https://zeroheight.com/626199550/p/51f970-toggle-group) | High | Binary, mutually exclusive choices that take effect immediately, no submit/save needed. | Turning a setting on/off with instant effect |

---

## Variants & Modifiers

### Border

Checkboxes can be used with or without a border. Add a border when you want to emphasize the options more clearly. Borders can also help to distinguish each checkbox.

### Label

Checkboxes should be used with a label in most cases. Only in a few exceptions, when the context is clear, can checkboxes be used without labels. For example, in tables.

### Modifiers

Checkboxes have the same elements as all form components:

* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the checkbox

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

## Behavior & Responsiveness

### Interaction

Not only the checkbox itself is clickable, but also the entire row. The row height is 48px.

### Interactive States & Loading

* **Default / Hover / Pressed / Disabled:** Checkboxes have the states default, hover, pressed, and disabled. They can be selected, unselected or indeterminate, and they can be in an error state.

### Touch Target & Layout

* **Width Adaptability:** The width of the checkbox component is determined by its content. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start each list item with a capital letter; don't use commas or semicolons at the end of each line.
* **Label Formula:** Not documented.
* **Length Limits:** Less than 3 words; don't use an ellipsis to cut off label text — wrap to 2 lines if necessary.

**Checkbox labels:** Always use clear and concise labels for checkboxes. Labels appear to the right of checkbox inputs. A label is always required in the code for a checkbox, even if it's not shown in the interface.

**Overflow content:** Make sure that the text under the checkbox wraps to the next line, and that the checkbox and its label are aligned at the top.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

* **Keyboard Navigation:** Not documented.
* **Screen Readers:** A label is always required in the code for every checkbox, even when it's not visibly shown in the interface, so it can still be announced.
