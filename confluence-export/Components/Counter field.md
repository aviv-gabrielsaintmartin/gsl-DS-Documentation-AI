<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830860391/Counter+field | Last modified: Aug 17, 2026 -->

# Counter field

Counter fields are used to enter or select numeric values.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b4122d9e-7ac5-4c74-9a7f-d5af3a800d28&&collection=contentId-2830860391&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Counter field on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7278)
* [Counter field on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-counterfield--docs)

---

## Usage

Counter fields allow users to enter a numeric value or incrementally adjust a value with +/- buttons.

### Platform

Unlike other form components, we use the same counter field on all platforms.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=06d716c0-e6c3-469b-9fbe-f3d43498ff3e&&collection=contentId-2830860391&height=248&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the counter field to allow users to enter or select numeric values. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d24d13bb-0db8-4d0f-aaf9-d0261453bc39&&collection=contentId-2830860391&height=248&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use the counter field to select the apartment floors. Instead, use the floor selection component. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2e80fff2-aa13-4283-acd8-5743d9be49db&&collection=contentId-2830860391&height=248&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use the counter field for larger numbers. Use text fields instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Counter field** | — | Allows only numeric values — doesn't support letters or words. | — |
| [**Floor selection**](https://zeroheight.com/626199550/p/244373-floor-selection) | High | Used to select floors; contains "GF" (ground floor) as a word. | User needs to pick an apartment floor, including ground floor |
| [**Text field**](https://zeroheight.com/626199550/p/980e7b-text-field) | High | Allows all kinds of free-form content; used for larger numbers such as prices, square meters, zip codes, or street numbers. | The number is large or formatted (price, zip code) rather than a small adjustable count |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, counter fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

## Behavior & Responsiveness

### Interaction

Numbers can be entered into the counter field using the keyboard — it is not possible to enter letters. Numbers can also be selected using the +/- buttons; consumers can decide how many steps the counter will increase/decrease per click (e.g. 0.5, 1, 5, 10 steps etc.). The counter field allows positive and negative integer and decimal numbers. The default, maximum and minimum values can be defined by the consumer.

### Interactive States & Loading

* **Default / Hover / Active / Disabled:** Counter fields have the states default, hover, active, and disabled. They don't have a pressed state — instead, they change to the active state when a user presses on the field. When in error state, they contain an error message.
* **Buttons:** The +/- buttons have the states default, hover, pressed and disabled.

### Touch Target & Layout

* **Width Adaptability:** The default size of the counter field is 144px. The width can also be set to 50% of the container if two counter fields are in the same row. Using the counter field at 100% (full-width) is not recommended. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start with a capital letter and use no punctuation (including colons).
* **Label Formula:** Noun form.
* **Length Limits:** 1-3 words for labels.

**Digit:** The counter field supports both positive and negative numbers. Decimal numbers are also supported.

**Labels:** Counter fields should always have a label, to help the user understand what information to enter.

**Helper text (optional):** Add a helper text if the user needs assistance completing a field. Use sentence-style capitalization and punctuation. Helper text is an optional feature and can be used instead of a tooltip. When used, helper text is always available when the input is focused and appears below the field — the exception is when an error or warning message replaces the helper text on Android.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
