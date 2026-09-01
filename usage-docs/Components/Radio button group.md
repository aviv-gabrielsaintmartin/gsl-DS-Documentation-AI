<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831810661/Radio+button+group | Last modified: Aug 21, 2026 -->

# Radio button group

Radio button groups are used to select one option from a group of mutually exclusive choices.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5c601c29-4133-4f4b-b52f-6076b223d30c&&collection=contentId-2831810661&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Radio group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7281)
* [Radio group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-radiogroup--docs)

---

## Usage

Radio buttons are used for mutually exclusive choices, not multiple choices. Only one radio button can be selected at a time. When a user selects a new item, the previous selection is automatically deselected.

### Platform

On the web and iOS, we use custom radio buttons. On Android, we use native radio buttons.

| Web/iOS | Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6786c402-4b2a-41fb-b57c-04002b1d5eb8&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=224&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9ca97966-e408-49ea-b022-11ea8d14b20e&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=224&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5954ebce-ed8a-44c4-ba96-c45b38f2181a&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use radio buttons for mutually exclusive choices. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1d4df745-496c-474e-95b9-9f2b7e5728e5&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use radio buttons to allow users to select multiple options independently. Use checkboxes instead. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d68b91a7-ace0-4c31-a065-2dd28061e66a&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use radio button groups for binary choices that should take effect immediately. Use toggle groups instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Radio button group** | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. |
| [**Checkbox group**](https://zeroheight.com/626199550/p/41df87-checkbox-group) | Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. |
| [**Toggle group**](https://zeroheight.com/626199550/p/51f970-toggle-group) | Toggle groups are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving. |

---

## Variants & Modifiers

### Alignment

Radio button groups can be aligned vertically or horizontally, depending on the use case and layout structure. For better readability, arrange radio buttons vertically whenever possible.

| Vertical | Horizontal |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=df7fc531-968b-45c5-97fc-435526f6999e&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=efdfb92b-903e-45c1-be61-58fee1f2b2be&&collection=contentId-2831810661&height=152&occurrenceKey=null&width=906&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Modifiers

#### Border

Radio button groups can also be used with or without a border. Add a border if you want to emphasize the options more clearly. Borders can also help to distinguish each radio button.

| Without border | With border |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e86bd423-c168-4aa1-89ea-a14ef92259f8&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=304&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cd4e0330-8390-49df-a55f-7b901404f295&&collection=contentId-2831810661&height=696&occurrenceKey=null&width=304&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3c0702e2-c909-4f8c-a15a-8b101478554f&&collection=contentId-2831810661&height=1390&occurrenceKey=null&width=640&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use radio buttons without borders when the radio button group is simple and the options are easily distinguishable without added visual emphasis. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5f97f859-2679-4053-8e96-5698b20c7447&&collection=contentId-2831810661&height=1390&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use borders around radio button groups when you want to clearly distinguish options, especially in complex forms. Borders help visually separate each option, making it easier for users to scan and understand their choices. |

#### Columns

Vertical radio button groups are available in one or two columns.

| One column | Two columns |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=df7fc531-968b-45c5-97fc-435526f6999e&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Single columns are used for concise layouts with fewer options, especially on mobile devices or when vertical space is limited. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e494e039-b53f-4c1b-868c-9ed4ed8c9438&&collection=contentId-2831810661&height=536&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) The two-column layout is used when presenting more options (6 or more) to efficiently use space, improve scannability, and facilitate comparison. It is especially useful for desktop interfaces. |

#### Header

Like all form components, radio button groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=94036ff8-656f-4b3a-89b8-50133fa16adb&&collection=contentId-2831810661&height=616&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

### Interactive States & Loading

Radio button groups have the states default, hover, pressed, and disabled. They can be selected or unselected, and they can be in an error state. When in error state, they contain an error message.

| Neutral | Error |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=77ca1913-a7e9-4336-b4ff-34de5be37ac3&&collection=contentId-2831810661&height=384&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=641fd3ee-d17e-45ab-9c01-e5f1b92d5387&&collection=contentId-2831810661&height=384&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20b9fc9d-8ab3-46ec-b13e-2c459a0ad2ab&&collection=contentId-2831810661&height=576&occurrenceKey=null&width=360&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Radio button group with error message.

More information:

* [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
* [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

### Touch Target & Layout

Not only the radio button itself is clickable, but also the entire row. The row height is 48px.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9d47774b-7255-4605-9ddd-07e1efbdf39a&&collection=contentId-2831810661&height=440&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
The width of the radio group component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

**Vertical wrapping:** Text that exceeds the available space is automatically wrapped to a new line. Radio button and content are aligned on top.

| One column | Two columns |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=92eb6d96-1208-4ee9-af41-b3648a30c468&&collection=contentId-2831810661&height=680&occurrenceKey=null&width=472&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Row height is determined by the content. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=45b98338-77ca-4725-baad-001e873419a1&&collection=contentId-2831810661&height=296&occurrenceKey=null&width=646&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) The row height is determined by the radio button with the longest content. |

**Horizontal wrapping:** Radio buttons wrap to a new line if there is not enough space for all of them. Only if the text of a radio button is longer than the width of the available space, the text is wrapped. Radio button and content are aligned on top.

| Short content | Long content |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2c8719ad-adfe-4c9b-a57a-d5f251763bcf&&collection=contentId-2831810661&height=256&occurrenceKey=null&width=612&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Radio buttons wrapping onto a new line. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c72deecd-b2cf-4d9f-9152-b204d0d555bc&&collection=contentId-2831810661&height=408&occurrenceKey=null&width=572&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Text breaking onto a new line. |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

### Main elements

**Radio labels** appear on the right of radio button inputs. Always use clear and concise labels for radio buttons. Make sure to:

* List options in a rational order that makes logical sense
* Start with a capital letter
* Not end in punctuation, if it's a single sentence or word

**Group labels (optional):** Add a label to a group of radio buttons to provide additional clarity. In some cases, a group of radio buttons may be within a larger group of components that already have a group label. In this case, no additional group label is needed for the radio button component itself. A group label can either indicate the category of the grouping, or it can concisely instruct what action to take depending on the context.

**Helper text (optional):** Add a helper text below the label to provide additional context and help the user make a decision.

### Overflow content

We recommend that radio button labels be less than 3 words. If you are running out of space, do not ellipsis the radio button label text; instead, put the text on 2 lines. Text should wrap under the radio button so that the control and label are top-aligned.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
