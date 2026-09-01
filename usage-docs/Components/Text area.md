<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831024256/Text+area | Last modified: Aug 21, 2026 -->

# Text area

Text areas are used to enter and edit multi-line text content.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a10bb02e-87b4-4697-a292-3665cdc8409b&&collection=contentId-2831024256&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Text area on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7285)
* [Text area on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textarea--docs)

---

## Usage

Text areas are used for entering and editing larger amounts of text compared to single-line [text fields](https://zeroheight.com/626199550/p/980e7b-text-field). They are commonly used in forms for purposes such as entering descriptions, comments, and messages.

### Platform

We use platform-specific text areas that differ between Web, iOS and Android. The main difference is the behavior of labels, placeholders and the resize handle.

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled. On Web, the field contains a resize handle; on iOS, it doesn't.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7a9b3971-e4f5-4632-957e-d254bf72db50&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=701149c1-d9d6-4eff-abdd-49287422b4c5&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7b63ef93-3c6f-4657-9f17-3d120f8621fe&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dd6fbd8d-a0c3-49ba-ba90-0eda47d4ea52&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4adf0136-2295-4fe5-8591-820ae1a7a30e&&collection=contentId-2831024256&height=192&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=80953d6f-c405-4664-8cf9-3dd5fea3922b&&collection=contentId-2831024256&height=212&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c0c3f0e4-6a50-42b4-8547-c5694d889063&&collection=contentId-2831024256&height=210&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4e7d5b7b-93c3-4ea5-b4d9-c66a3ea8d782&&collection=contentId-2831024256&height=210&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=75e7c38c-f9c6-4ac7-85f4-8d40adedcea8&&collection=contentId-2831024256&height=476&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use text areas for multi-line text content. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f05c8e10-81bf-4ad9-84ae-204da7757e47&&collection=contentId-2831024256&height=476&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use text areas for single-line content. Use text fields instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Text area** | Text areas allow multi-line text content. |
| [**Text field**](https://zeroheight.com/626199550/p/980e7b-text-field) | Text fields allow short single-line and free-form content. |
| [**Phone number field**](https://zeroheight.com/626199550/p/490309-phone-number-input) | Phone number fields are only used to input phone numbers. |
| [**Date field**](https://zeroheight.com/626199550/p/33c9e4-date-picker) | Date fields are only used to input dates. |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, text areas contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ab46784d-7b97-4632-9a72-29e9122fac51&&collection=contentId-2831024256&height=328&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Text areas should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

#### State message

State messages can be used to provide additional information or feedback on the usage of the text area.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

More information:

* [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
* [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

#### Icons and suffix

Unlike the text field, the text area does not contain any icons or suffixes.

#### Character counter

A character counter can be added to display the number of characters entered and the total number of characters allowed.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2dee95c4-df6e-4817-bf02-e2f10ccca3d1&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Depending on the platform, there is different behavior when the character count is exceeded.

| Web | Android | iOS |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=edd97e1e-7337-4788-b6e2-bba9ca38681f&&collection=contentId-2831024256&height=326&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) The counter goes into an error state. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8a5a9588-e400-4be4-b58d-61b67675e03c&&collection=contentId-2831024256&height=344&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) The entire field goes into an error state and an error message is displayed. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dce941a1-57d1-4ae3-be9d-f6cd47673516&&collection=contentId-2831024256&height=326&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) It is not possible to type in more characters than are allowed by the character limit. |

#### Resize handle

Only on Web the text area contains a resize handle. It allows the user to change the height of the field. It is not possible to change the width of the field with the handle. It's also not possible to make the field smaller than the min-height (96px).

On Android, the field automatically grows if the content is longer than the field.

On iOS, the field has a fixed height. The user cannot resize the field.

| Web | iOS | Android |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4bbd0b69-018a-4963-8bb5-b7e99ae223c7&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b12f30a9-94ab-4045-aeb1-8330303f32d1&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=07b0415f-b581-4499-9461-30e22a1703b7&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

Text areas have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, it changes to the active state when a user presses on the text area.

#### Neutral

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7a9b3971-e4f5-4632-957e-d254bf72db50&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4e8d6aeb-e9c8-4e7a-b389-26ab7ce6f6fe&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7b63ef93-3c6f-4657-9f17-3d120f8621fe&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4ac47dff-9058-4c7b-bedd-0a04de14e0ac&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=701149c1-d9d6-4eff-abdd-49287422b4c5&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=155f1790-79ff-44c0-bf0c-d5b7c8ec242b&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dd6fbd8d-a0c3-49ba-ba90-0eda47d4ea52&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=76d815e2-31e8-4866-92e3-571731c5acb9&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Error

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3f35a608-c3d2-4980-a1b5-95401c1eea98&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=606328bc-e225-484e-9a43-51410b0b20d4&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f4121323-44d8-45e8-9ad3-938508b1eae7&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6d6b6348-9a01-475a-8249-ffdaeabe394e&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d6b903b8-6a61-49f4-8241-0a5a84e9f968&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=029c4657-b22d-4269-aece-571ad9f13d3e&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4721942d-f414-40e6-beac-5ecb9608f7d9&&collection=contentId-2831024256&height=296&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6b8c421c-6d3c-4f32-976f-37362fd763d8&&collection=contentId-2831024256&height=248&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

The text area can have a fixed width or can be set to 100% (full-width) of the container. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

The min-height of the text-area is 96px. On Web the user can make the field longer by pulling on the resize handle. On Android, the field automatically grows if the content is longer than the field. And on iOS, the field has a fixed height, which the user cannot resize. When the field is smaller than the content inside, vertical scrolling is available.

| Default height | Height increased by user | Height smaller than content |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=293c047a-6501-4785-a7ee-43e8d34cc8a4&&collection=contentId-2831024256&height=456&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=35424e25-e1c0-4bdf-afc0-b75621d5b6f0&&collection=contentId-2831024256&height=456&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7c6514ec-82fe-4678-a307-f28eca423011&&collection=contentId-2831024256&height=456&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

### Main elements

#### Labels

Text areas should always have a label, to help the user understand what information to enter.

* Keep the label short and concise (1-3 words) and in noun form.
* Start with a capital letter and use no punctuation (including colons).

#### Helper text (optional)

Add a helper text if the user needs assistance completing a field.

Use sentence-style capitalization and punctuation.

Helper text is an optional feature and can be used instead of a tooltip.

When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text.

#### Placeholder text

Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.

### Overflow content

If a user's content exceeds the vertical space of the variable text area, the user can either expand the field container using the resize handle or scroll the content vertically within the set field container.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
