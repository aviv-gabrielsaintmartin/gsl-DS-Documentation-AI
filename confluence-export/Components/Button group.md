<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832400411/Button+group | Last modified: Aug 17, 2026 -->

# Button group

Button groups display multiple related choices in a horizontal row, allowing users to select one or more options.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1e419ed4-93d4-46fe-8385-d0f7f511f501&&collection=contentId-2832400411&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Button group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7272)
* [Button group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-buttongroup--docs)

---

## Usage

Button groups allow users to select one or more options from a group. They are similar to [radio buttons](https://zeroheight.com/626199550/p/55bfd7-radio-button-group) (single-select) and [checkboxes](https://zeroheight.com/626199550/p/41df87-checkbox-group) (multi-select).

### Platform

The button group component is available on all platforms.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=997fbc80-bd9f-4f5f-8580-f0646d531eac&&collection=contentId-2832400411&height=82&occurrenceKey=null&width=532&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the button group component on all platforms. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=30b17cdd-8602-489c-8576-126906b4663f&&collection=contentId-2832400411&height=88&occurrenceKey=null&width=732&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't replace the button group component by the native iOS segmented control. |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1f088aee-a130-4095-aa1a-5f1016c15c54&&collection=contentId-2832400411&height=776&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use button groups inside forms. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b6212797-ec17-4b01-8da1-d117105778e5&&collection=contentId-2832400411&height=768&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid using the button group as navigation. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| [**Radio button group**](https://zeroheight.com/626199550/p/55bfd7-radio-button-group) | High | Single-select alternative | Only one option can ever be selected at a time |
| [**Checkbox group**](https://zeroheight.com/626199550/p/41df87-checkbox-group) | High | Multi-select alternative | Users need to select several options at once |

---

## Variants & Modifiers

### Number of items

The button group contains 2 to 9 items. Button groups with more than 7 items are mainly used for energy selection on desktop.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a479a509-2c72-4667-96ef-fad1c6559cbd&&collection=contentId-2832400411&height=82&occurrenceKey=null&width=1220&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Limit button group items to 7 or fewer for most cases to avoid accessibility problems. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5f1c46ec-782e-467f-9307-5aab184cdc75&&collection=contentId-2832400411&height=856&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** If you want to display more than 7 options use chip groups for multi-select and dropdowns for single-select instead. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=33172725-ed0d-459b-b6bb-62c14155067b&&collection=contentId-2832400411&height=80&occurrenceKey=null&width=762&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** More than 7 items are only used in the energy selection. |

### Modifiers

#### Icons

Icons can be added as visual cues to provide clarity to the user. The icon is always to the left of the label.

| DO | DON'T | CAUTION |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a2fdce96-1e4a-4b57-ae1a-6469e3643d89&&collection=contentId-2832400411&height=80&occurrenceKey=null&width=460&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Combine icons with text for clarity. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bced61f3-871f-48e2-ab22-9d9cb00cf2fa&&collection=contentId-2832400411&height=82&occurrenceKey=null&width=306&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid mixing different combinations. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=71a426a6-8fc5-4e3a-b27f-9c5f17921145&&collection=contentId-2832400411&height=82&occurrenceKey=null&width=209&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Make sure icons clearly communicate its meaning when they are used without a label. |

#### Border highlight

The highlight is used for energy and co2 selection.

#### Header

When the button group is used in a form add the header and use a clear and concise label. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

#### Helper Text

Include a helper text to improve accessibility. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-71) for more information.

---

## Behavior & Responsiveness

### Interaction

For single selection, the button group allows users to select one item. For multiple selection, users can select multiple items.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=19fb6371-18b9-43fa-90d8-7e0ed3b7ad75&&collection=contentId-2832400411&height=608&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use checkboxes, radio buttons, or chip groups to avoid having both single- and multi-select button groups on the same page. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8983a944-6bf1-4121-baa0-9049fed6d542&&collection=contentId-2832400411&height=576&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid mixing single-select and multi-select. |

### Interactive States & Loading

* **Default / Hover / Pressed / Disabled:** Button groups have the states default, hover, pressed and disabled, both in selected and unselected modes.

### Touch Target & Layout

* **Touch Target:** Available in 40px and 48px heights.
* **Width Adaptability:** Hugs content by default; can be changed to fill the container (full-width).

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=083ede6b-8a40-46e2-933a-76eecbdb2019&&collection=contentId-2832400411&height=82&occurrenceKey=null&width=658&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use short labels of similar lengths. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f8cfb585-188d-44e5-b510-064ae012a938&&collection=contentId-2832400411&height=162&occurrenceKey=null&width=657&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid wrapping onto new lines. |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start with a capital letter; do not use punctuation (nor colons).
* **Label Formula:** Noun form, e.g. {Noun}.
* **Length Limits:** 1-3 words, of similar length between items.

For information on header and helper texts please go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-71). For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/v/latest/p/324518-intro).

---

## Accessibility (a11y)

Not documented
