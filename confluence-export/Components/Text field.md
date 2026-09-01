<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831057031/Text+field | Last modified: Aug 21, 2026 -->

# Text field

Text fields are used to enter and edit single-line text content.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a24e8918-42d8-4cfa-95c8-49febd51c352&&collection=contentId-2831057031&height=1500&occurrenceKey=null&width=5512&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Text field on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7284) · [Text field on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textfield--docs)

---

## Usage

Text fields allow users to input and edit short free-form content. They are commonly used in forms for purposes such as contact and property information, login, registration and search queries.

### Platform

We use platform-specific text fields that differ between Web/iOS and Android. The main difference is the behavior of labels and placeholders.

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8dfd200c-cf61-404b-85a1-7c164d33422f&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=50d900d7-8520-43d0-9231-ad1683169fc7&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e6c01194-6700-403a-bc98-354d31500ffa&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6309c098-bcd1-4afe-b708-b726f5b2e9d5&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=45e2463a-c32e-42b5-a202-a2252d099bdb&&collection=contentId-2831057031&height=144&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1e28f8cb-4090-4452-bc6e-cdebad38243f&&collection=contentId-2831057031&height=164&occurrenceKey=null&width=640&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a36b0e52-fd92-419b-93a6-37ae59b44cc6&&collection=contentId-2831057031&height=162&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2f7e1b6d-7df6-483e-b000-4f3abab853d3&&collection=contentId-2831057031&height=162&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=57dbe62a-0d7a-42f8-9748-adef21327aca&&collection=contentId-2831057031&height=800&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use text fields for short single-line content such as name and address. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b8d23cba-d44c-4307-8f77-efcc2343c292&&collection=contentId-2831057031&height=800&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Use text fields for large amounts of content that exceed one line. Use the text areas instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6696f96c-83ad-4a95-9191-7425553df1e1&&collection=contentId-2831057031&height=360&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Use text fields for phone numbers. Use the phone number field instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3fe68cef-b9e9-40bf-94c0-cda3a0fae132&&collection=contentId-2831057031&height=360&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Use text fields for date selection. Use the date field instead. |

### Related Components

| Component | Usage |
| --- | --- |
| [**Text area**](https://zeroheight.com/626199550/p/438e9d-text-area) | Text areas allow multi-line text content. |
| [**Phone number field**](https://zeroheight.com/626199550/p/490309-phone-number-input) | Phone number fields are only used to input phone numbers. |
| [**Date field**](https://zeroheight.com/626199550/p/33c9e4-date-picker) | Date fields are only used to input dates. |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, text fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e7cbb5d2-5428-4f9c-85fb-45750711071c&&collection=contentId-2831057031&height=232&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Text fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

#### State message

State messages can be used to provide additional information or feedback on the usage of the text field.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

| Error (Web, iOS, Android) | Information (iOS/Android) | Success (iOS/Android) | Warning (iOS/Android) |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=93f1a33d-8649-4052-a55a-a69307453f33&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c00fbfd5-7992-4098-8926-e67c29dccba5&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ed5df1dd-7c6c-446c-992b-81671e39f5ec&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1b637e81-e258-48e8-837c-f65e6f056a52&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

More information: [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79) · [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

#### Icons

Icons can be added as visual cues to provide clarity to the user. Icons on the left are non-clickable. Icons on the right can be clickable (icon button) or non-clickable.

| Left | Right | Left and right |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=147d0eed-c2c2-4c07-8dbd-256294121818&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=134e2b5e-5c50-4ef8-b56c-9cf0e360c6cd&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=78f4edf9-8dfd-4095-ab1f-41f5f2099877&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1213f772-3a0c-4edc-ac62-6b8bbb80aa47&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use non-clickable icons to provide visual cues to the user. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=13678feb-d7b5-4761-8d93-297acd907037&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use clickable icon buttons for actions related to the text field, such as deleting the contents of the box. |

#### Suffix

The suffix can be added to provide additional context or constraints for the user input.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=af4280fb-3c5e-4466-ab61-968cacb863b9&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7ec834fc-824b-48d8-ba67-ed3df5c124aa&&collection=contentId-2831057031&height=520&occurrenceKey=null&width=280&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the suffix for measurements, currency, or contextual information. |

---

## Behavior & Responsiveness

### Interactive States & Loading

Text fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, they change to the active state when a user presses on the text field.

#### Neutral

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8dfd200c-cf61-404b-85a1-7c164d33422f&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d860612e-9b80-4015-b121-8efeee5c3343&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e6c01194-6700-403a-bc98-354d31500ffa&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=58514468-ab8e-4784-a0fc-c645b926bab0&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=50d900d7-8520-43d0-9231-ad1683169fc7&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=324c27f8-2813-419f-a136-d18215db696f&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6309c098-bcd1-4afe-b708-b726f5b2e9d5&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=50331be4-bc75-478e-893a-31f4f681d979&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Error

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d8b8a697-9f3d-43c7-8ba6-df85ff2ba08b&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=21364f78-5664-4202-99ac-553e945abc5e&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=85114f92-7c18-49dd-b054-27e3fba9493a&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=829dc600-1231-4382-8b3f-5ec01289c9ce&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=19a53606-1def-4970-833c-8aebdcfd5911&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=aa2c9d6a-2161-47cb-a73e-ef7d17337f33&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=824a81b8-6ba4-4b72-b3c4-699a04731174&&collection=contentId-2831057031&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=adca10f9-3b48-46f4-9d13-b94f5f8fa40c&&collection=contentId-2831057031&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

* **Overflow content:** If a user's content is too long for the single line of text input, the value content can scroll horizontally within the field container as the cursor moves from one end of the value to the other.

### Touch Target & Layout

**Width Adaptability:** The width can be set to 100% (full-width) or 50% of the container. For special use cases it is also possible to define a fixed size. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=086d93ee-8051-47b3-b9b4-aa84643cadd3&&collection=contentId-2831057031&height=552&occurrenceKey=null&width=852&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Labels:** Text fields should always have a label, to help the user understand what information to enter. Keep the label short and concise (1-3 words) and in noun form. Start with a capital letter and use no punctuation (including colons).
* **Helper text (optional):** Add a helper text if the user needs assistance completing a field, such as explaining the correct data format. Use sentence-style capitalization and punctuation. Helper text is an optional feature and can be used instead of a tooltip. When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text in apps.
* **Placeholder text:** Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.
* **Placeholder text - numbers:** When designing a text field that will contain numbers (price, size, etc.) please make sure you use numbers or leave the text field empty. For example a text field for minimum price to maximum price should say 0 €, allowing the user to type in a number if they wish. See the [Number Guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers) to learn more about the rules for designing with number-related text.

---

## Accessibility (a11y)

Not documented
