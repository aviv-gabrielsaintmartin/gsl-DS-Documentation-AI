<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3491856865/Phone+number+field | Last modified: Aug 25, 2026 -->

# Phone number field

The phone number field is used to input and format phone numbers.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d9d78a42-72cc-41cc-9c86-17ce93250826&&collection=contentId-3491856865&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Web | iOS | Android |
| --- | --- | --- |
| Ready ✅ | To do 🚧 | Ready ✅ |

* [Phone number field on Figma](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?node-id=3696-294)
* [Phone number field on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/patterns-phonenumber--docs)

---

## Usage

The phone number field allows users to enter phone numbers commonly used in forms for contact information, registration, and verification. It includes intuitive country code selection for accurate entry across platforms.

### Platform

We use platform-specific phone number fields for Web/iOS and Android, with main differences in label and placeholder behavior.

**Web/iOS:** the label is always on top of the field. The placeholder is visible until the field is filled.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2e9a69d6-656b-4887-9415-776696ab6c96&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=32415b1d-bd06-4574-aa10-dd20fc06de8a&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bc21655f-91c6-41e2-8de3-28bc7f129fb1&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a29b0b29-8505-4a76-a476-66b09edbb209&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Android:** the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1f9aa710-cbd0-4698-b425-bef3b30f5d3b&&collection=contentId-3491856865&height=53&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9825cd19-5618-450f-9cd8-145ae3f61f42&&collection=contentId-3491856865&height=53&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a3704704-fc16-475f-8278-47696ac87f6b&&collection=contentId-3491856865&height=53&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6ef96803-dc84-4eb1-8ddd-a9629d04396c&&collection=contentId-3491856865&height=53&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4b679bce-85d8-4fbf-b554-37ab1e61b1d0&&collection=contentId-3491856865&height=364&occurrenceKey=null&width=342&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the phone number field with a country code selector in forms, and prefill the country code based on the user's location whenever possible to improve usability. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=14ab9465-413d-4657-b42a-6534dd7fd5be&&collection=contentId-3491856865&height=164&occurrenceKey=null&width=342&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Leave the country code unselected, as this can cause user confusion and incorrect phone number formatting. |

### Related Components

| Component | Usage |
| --- | --- |
| **Phone number field** | Phone number fields are used to input phone numbers. |
| [Text field](https://zeroheight.com/626199550/p/980e7b) | Text fields allow short single-line and free-form content. |
| [Text area](https://zeroheight.com/626199550/p/438e9d-text-area) | Text areas allow multi-line text content. |
| [Date field](https://zeroheight.com/626199550/p/33c9e4-date-picker) | Date fields are only used to input dates. |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, phone number fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

| Web / iOS | Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=062c3826-1e24-4656-9795-effbe4b74aa9&&collection=contentId-3491856865&height=105&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ffcf4eb9-1c92-4da4-b903-8747f4399ff8&&collection=contentId-3491856865&height=105&occurrenceKey=null&width=298&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

Phone Number fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

#### Country code selection

It is autofilled based on geolocation or defaults to the brand's default country. It can't be deselected, always stays filled, and automatically updates the phone number field when changed.

| Desktop active (Dropdown) | Mobile / iOS active (BottomSheet) |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2cbd6a65-c717-4baf-93bd-0ca5f4f40142&&collection=contentId-3491856865&height=357&occurrenceKey=null&width=305&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3373f716-4b6f-4ebb-85d4-a6aa4166fc33&&collection=contentId-3491856865&height=524&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The rows in the dropdown list have the states default, hover and pressed. They can be selected or unselected.

| Unselected | Selected |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=054bcd76-da8f-4f32-9828-474c2bd2b517&&collection=contentId-3491856865&height=175&occurrenceKey=null&width=262&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=964909e2-d6b6-4866-8821-4b0b5fc14cb4&&collection=contentId-3491856865&height=175&occurrenceKey=null&width=262&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Errors

Phone number field saves entered phone numbers even when the country code changes. It has filled and empty states, with potential errors.

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b7cd53c5-7bba-43c0-9e28-3fe050a5f3ef&&collection=contentId-3491856865&height=91&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4c19954c-ff3e-42bd-b4f7-abc1f0706705&&collection=contentId-3491856865&height=91&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty (image unavailable) | Empty (image unavailable) |
| Filled (image unavailable) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4ce6fd0a-b6eb-4016-bf35-9cae427032ea&&collection=contentId-3491856865&height=91&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c746c15b-31b8-415c-902a-e296c6d8f5b3&&collection=contentId-3491856865&height=91&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f1a59bee-9f21-4e9f-8e37-bca6bdd10d4e&&collection=contentId-3491856865&height=91&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

The phone number field allows users to change the country code and enter a number when focused. The country code dropdown and the phone number text field have different active and hover states. They don't have a pressed state. Instead, they change to the active state when a user presses on the text field.

| Default | Hover field | Hover dropdown | Active | Disabled |
| --- | --- | --- | --- | --- |
| Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2a79e87e-16f6-46f1-a9f7-f99d7b52faa9&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=05f0f67f-35ae-4f3d-9ad0-4071f21fc3fb&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c3502114-0d15-4b47-bc82-17e4827a6aaa&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ecba8a6f-a0b4-4576-ada4-8d403abd481f&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Empty ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d5abca96-fba3-40e7-9716-29b1d516f252&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |
| Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=49ec0e34-0598-4917-b9f7-6f0d4c912271&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5126a579-340e-40e9-aa80-e16dcb097fdb&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d5783d4c-bc49-47b2-a198-44fd0141e1df&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=816c86e3-2978-40c9-94ba-95bce5ca8c53&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | Filled ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1f17e8b0-22d5-49ef-a81f-4d037e22e2e2&&collection=contentId-3491856865&height=69&occurrenceKey=null&width=255&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

The width can be set to 100% for a full-width layout, or a fixed size can be defined for specific use cases. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4b679bce-85d8-4fbf-b554-37ab1e61b1d0&&collection=contentId-3491856865&height=364&occurrenceKey=null&width=342&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the full width of the container for input fields. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2552dd9c-58e3-40c7-9241-e1a386de5c95&&collection=contentId-3491856865&height=280&occurrenceKey=null&width=342&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid using 50% width for input fields when they are grouped with other fields. |

### Breakpoints & Platform Adaptations

The style of the country code selector depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web: XXS - XS (0 - 599 px)** | Dropdown ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2cbd6a65-c717-4baf-93bd-0ca5f4f40142&&collection=contentId-3491856865&height=357&occurrenceKey=null&width=305&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |
| **Web: SM - XXXL (> 599 px)** | Bottom Sheet ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3373f716-4b6f-4ebb-85d4-a6aa4166fc33&&collection=contentId-3491856865&height=524&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Overflow Content

**Overflow in a text input:** if user input exceeds the single text input line, the content scrolls horizontally within the field container as the cursor is moved.

**Overflow in Dropdown:** the country code in the dropdown will be truncated if it exceeds the available space.

---

## Content & UX Writing

Placeholder text provides hints or examples, but disappears when the user starts entering data. It should not contain crucial information and is mandatory in text input fields by default.

* **Helper text:** if the second input field doesn't have a specific label, the helper text provides information to help users fill it correctly, usually explaining the correct data format. It is mandatory and replaces a tooltip. The helper text is always visible.
* **Placeholder:** the best way to display the phone number is to format it by country rather than language.

    * **Default:** if you can't implement separate spacing for the main countries, just stick with no spacing to avoid frustrating the user. Example: **+33 XXXXXXXXX**
    * **International:** we use the [E.123 standard](https://en.wikipedia.org/wiki/E.123) for international phone numbers. Example: **+22 XXX XXX XXXX**
    * **🇬🇧 UK:** use spaces in phone numbers. Examples: **07986 123 456**, **0300 123 4567** (for companies)
    * **🇫🇷 France:** use spaces between sets of 2 numbers. Example: **06 24 55 32 14**
    * **🇩🇪 Germany:** when designing in German, we use the DIN 5008 international format, represented as **+49 AAAA BBBBBB**
    * **🇧🇪 Belgium:** Belgian telephone numbers consist of three parts: first '0', secondly the "zone prefix" (A) which is 1 or 2 digits long for landlines and 3 digits long for mobile phones, and thirdly the "subscriber's number" (B). Landlines: **0AA BB BB BB** or **0A BBB BB BB**. Mobile phones: **04AA BB BB BB**
    
* **Number Display:** for more information please refer to the [number guidelines](https://zeroheight.com/626199550/v/latest/p/60fe5b-numbers).

---

## Accessibility (a11y)

Labels or instructions are provided for user input as needed. A label for a form control clarifies its purpose, and while it can be visually hidden, it must still be included in the code for various presentations and interactions.

* **Labels for code:**

    * Dropdown: Country code
    * Text field: Phone number input
