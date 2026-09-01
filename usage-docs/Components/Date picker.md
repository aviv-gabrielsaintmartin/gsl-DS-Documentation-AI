<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832367723/Date+picker | Last modified: Aug 21, 2026 -->

# Date picker

Date pickers are used to select a date using text input or a calendar view.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=0c86389b3d71&id=87ff6628-82f6-4926-8b79-8d136d4741cc&&collection=contentId-2832367723&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Web | iOS | Android |
| --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 |

* [Date picker on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7270)
* [Date picker on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-datepicker--docs)

---

## Usage

Date pickers allow users to select a date from a calendar or manually enter a date in the input field. They can enter dates from the recent past, present, or future, with each date including the day, month, and year (dd/mm/yyyy).

### Platform

We use platform-specific date pickers that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders in the date field and the appearance of the calendar view.

#### Web

On the web, the label is always at the top of the date field. The placeholder is visible until a date is selected. On the web, we use a custom calendar.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=bde6a773edd7&id=bfc5c250-b5be-443d-a285-9b61ecee2768&&collection=contentId-2832367723&height=352&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Date field**

_\[Missing image: 41e99931d035072536c296 — placed at bottom of page for manual placement\]_

#### iOS

As on the web, the label is always at the top of the field on iOS. The placeholder is visible until a date is selected. On iOS we use the native calendar. On iOS, it's currently only possible to select the date using the calendar. It's not possible to type it directly into the field.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=8ce9b0639baa&id=bfc5c250-b5be-443d-a285-9b61ecee2768&&collection=contentId-2832367723&height=352&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Date field**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=2cfe76bcae85&id=a5fe16b3-7e45-4cfa-9800-b4d34e1376d2&&collection=contentId-2832367723&height=818&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Date picker**

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. Instead of a placeholder, the date format is displayed with the helper text. On Android we use the native calendar.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=12a69ae6cf72&id=b14d1609-1819-4767-8a9a-7c2efb9cd286&&collection=contentId-2832367723&height=352&occurrenceKey=null&width=640&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Date field**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=d4f817bdb5da&id=ed8a6038-7239-4f0d-b64e-76fe362875da&&collection=contentId-2832367723&height=1048&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Date picker**

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=d4e89f23b214&id=cd7008bf-3faf-42f8-9d4e-ae90c7785a2f&&collection=contentId-2832367723&height=1120&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the date picker to allow users to select a specific day in the past, present or future. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5210a1967c10&id=5410f1d5-b567-4857-b682-c55da3c0326f&&collection=contentId-2832367723&height=1120&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use the date picker when users need to select a specific year. Instead, provide a text field where they can enter the year directly. |

| DON'T |
| --- |
| **DON'T:** The date picker doesn't currently support range selection. |

### Related Components

| Component | Usage |
| --- | --- |
| **Date picker** | Date pickers are used to select or enter specific dates in the past, present or future. |
| [**Text field**](https://zeroheight.com/626199550/p/980e7b-text-field) | Text fields allow short single-line and free-form content. They can be used to enter years. |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, date pickers contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=76e0586cbcbd&id=7d727b76-934d-4028-91d8-a07c9d964df1&&collection=contentId-2832367723&height=232&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

### Interactive States & Loading

#### Date field

Like text fields, date fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message. They don't have a pressed state. Instead, they change to the active state when a user presses on the date field. The icon button in the field has the states default, hover, pressed and disabled.

**Neutral — empty**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=02a72b1d700a&id=c22dfde0-939c-47ad-9e26-ce6b20905147&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f9e6b3b4fe26&id=8db7fb69-05ac-467d-9f74-d63ab4f0f6af&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a3acb8f54d14&id=0aed3d15-2853-4cbd-a0d5-0e482d6ba477&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1d2746fa7788&id=648f7e96-9111-4c9a-a8b3-698b1b138946&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Neutral — filled**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1d51e46a6bfd&id=c9f307af-85f1-442a-b1e7-919310e4b4a2&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5d7d86ac8956&id=81ec6641-f2c5-4126-a20f-defbcd37ee80&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=03ad7ecf29d1&id=69cfabb9-5790-49e4-b94b-e295f7aadc96&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=e57bb1c94093&id=737a7ca8-6b29-496e-bf25-79cfc35a7448&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Error — empty**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=88854cbe12a1&id=2289d0cb-66de-4b2b-a8b3-8f6e62a8a0cb&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9d3b149d5549&id=db54ba90-5cff-4078-9e06-c32bff3eb784&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0f442637b9a3&id=0ca90702-0ed3-4d4d-a22f-60306a7d9241&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0fef77930d16&id=53f4af25-fa24-40e0-ae26-010461576a36&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Error — filled**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=e4a8dda9bf28&id=99147f4f-b6cf-4c15-87f3-3c1a9fe440a6&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b61de3156b9b&id=5602bc85-9d3b-44ef-ba7c-48d0ca849bed&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9d4e89131c68&id=a4375072-3c63-42a9-8b05-2bd699a9a4f5&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=186e25c1c47c&id=232fccc7-fa04-44f6-85ff-6be65c28078a&&collection=contentId-2832367723&height=200&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Date picker

The buttons in the date picker have the states default, hover, pressed and disabled. They can be selected or unselected.

**Day — unselected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c81601f8f5f7&id=6dbea3e3-fe40-4079-baef-fc7da573b382&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0e637c14ec44&id=1b5f90e2-5b59-42cf-8c06-4398dc442608&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0d7b9af7edf3&id=8c94621e-a323-4653-81ce-617d8f45004a&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8b5118003924&id=102e66a2-e96b-4a77-85ac-350d40fc1bd2&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Day — selected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=93ff97bb54e4&id=367ac474-b7ed-4255-af80-7c6e6d6ba201&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5db0cc713b2d&id=4f31a28c-7d85-4349-a548-7aef01a182ab&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5f38c25259e0&id=d39c5c62-e32c-4034-9632-78d448da4e97&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1c3fe4975827&id=376eaee9-436c-4cef-88e9-9b5bb188c2f1&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Month/Year — unselected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9eb1fa71d51f&id=d65e8492-8cb2-48cf-bd5e-ae571737e3de&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=82ef96b2afe5&id=f6d848cf-0ad9-4c7f-8f13-b3ad973f59f7&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=973f8cb38437&id=24538da8-a15d-469d-aad4-988e2ef6c7db&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6903c5937489&id=2e81bf90-896e-445f-9ca9-c4f53301a46b&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Month/Year — selected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a6aa7c74701d&id=972fb5a1-d8de-4727-a81b-d969a346f500&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1f514ba0b184&id=eb69c6e3-3601-4ccd-9a99-74648b27a752&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6d512c481720&id=429341d7-b0a4-4a1a-802e-022a97085fba&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7268ec8b1711&id=cd58c828-cd63-4c73-8145-92b29fb9ef34&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=166&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Current day — unselected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=bca23c0581a5&id=a8c1b190-7447-474c-b618-ad42063776bd&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f0f2b3301076&id=2bd9f14b-d75f-4e11-b0f9-b5b073dbdd30&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=aa66684b453c&id=164020d9-a355-494c-9d88-bd79cc0beda2&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=73379943173d&id=50db735b-00fa-418a-bbcf-098f11b98540&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Current day — selected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=332883343da7&id=01bdc39e-9928-4c03-8d82-e4a958e26fa6&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | _\[Missing image: a294290e6a1dbc56085c24 — placed at bottom of page for manual placement\]_ | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a2f535821882&id=bd51eb0d-9979-4393-b339-b449f8a15e99&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=823cc741b0ca&id=c8b38922-e6b9-4188-b6a3-6338312df2cc&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Date field interaction

#### Typing

The user can select a date by typing it into the date field. On the Web, we use a placeholder with progressive disclosure to help them understand the required format.

| Day | Month | Year |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0cf4e4666fbb&id=72653641-9e3f-4b22-93c1-6ab25a242e42&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f73b3bd5935d&id=ffc54e2f-5e87-46e5-838c-f57d42573c20&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=140f483130cd&id=d87f59fb-1d56-4518-9ce2-9ad4e8f4be14&&collection=contentId-2832367723&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Clearing

Web only. Clearing on other platforms is done in the Date Picker. The user can clear the date when the field is filled by clicking on the "clear" icon on the right. This button is optional.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=b3bdcbd0d572&id=8a3039b1-bb23-49ac-9363-23f8ed2d7679&&collection=contentId-2832367723&height=172&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Calendar interaction

#### Opening and closing

**Modal view**

The calendar opens when the user clicks the Calendar button. It closes when the user clicks the button again, clicks the Okay or Cancel button, clicks outside the calendar, or presses the Esc key. To select a date, the user must click a day and then press the Okay button.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=85e076766820&id=7583723a-fd64-48d2-b2f9-89468b01d251&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Opening and closing — clicking on the calendar button**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=f409dbc1d389&id=1af52a75-baf4-42b1-bee8-84b1b43868d7&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Selecting and closing — clicking a date and the okay button to select a date, or clicking on the cancel button to close the calendar**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=df003ea7eb80&id=0eceb379-bdbd-4b7a-847e-c63c93535add&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Closing — clicking outside the calendar or pressing esc**

**Dropdown view**

The calendar opens when the user clicks on the calendar button. It closes when the user clicks on the button again, selects a day, clicks outside the calendar or presses the esc key. To select a date, the user simply has to click on a day. The buttons are not needed in the dropdown view.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=9dab95a39d9b&id=7c6675fb-3d71-40de-a68b-ec3df06ebe8d&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=1680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Opening and closing — clicking on the calendar button**

_\[Missing image: 0a051c5bb4f6d1b1d0eee1 — placed at bottom of page for manual placement\]_

![](blob:https://media.staging.atl-paas.net/?type=file&localId=9fb28fac636d&id=35e68d4b-b5aa-4d52-8063-dbcae7dea9bd&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=1680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Closing — clicking outside the calendar or pressing the Esc key**

#### Changing months and year

Users can change the month and year by pressing the corresponding button and selecting an option from the dropdown list. In addition, they can change the month using the chevron buttons. In the dropdown view, the user must change the month and year before selecting a day because the calendar closes when the day is selected. In the modal view, this is not relevant because the calendar only closes when the user presses a button.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=41592df955a7&id=00416032-9399-457f-99d0-b3d90e75ae63&&collection=contentId-2832367723&height=796&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Calendar**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=f99acfd1efe3&id=7b79cbfc-2a68-4cc7-ba2b-2b84801b7ef0&&collection=contentId-2832367723&height=796&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Month selection**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=8a1bf056673b&id=fc5cbcdb-9ff5-4c97-b014-074a9274cf59&&collection=contentId-2832367723&height=796&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Year selection**

The month and year selection looks slightly different in the native iOS and Android picker. The native variants for this are currently not available in Figma. On the web, we currently still use the native browser dropdowns for the month and year selection. This will be fixed and aligned with Figma in the future.

#### Clearing

The user can clear the date when the field is filled by clicking on the "clear" button in the datepicker. This button is optional.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=75be009594dc&id=b7b678d3-605e-4422-bc5c-e00b4fb425ee&&collection=contentId-2832367723&height=1052&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Android**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a97b4d4c8f58&id=0aebbd2c-02c9-422f-9ace-05579a9eb8f9&&collection=contentId-2832367723&height=818&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**iOS**

### Position and scrolling

**Modal view**

The modal calendar is centered vertically in the middle of the screen.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=6f11ffd01d69&id=f44ce22b-cdb0-464d-be82-4391425d84bd&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Centered**

**Dropdown view**

By default, the calendar is positioned below the field. If there is not enough space below it, it is positioned on top of the field. If there are more options than space available, the calendar becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=ad9a5fa31edf&id=c6303032-03e3-4109-a1f3-6ae1b818ade7&&collection=contentId-2832367723&height=936&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Below the field**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=9f45e6ab2d03&id=d62bb709-9ca1-4362-b83d-519c03544b6f&&collection=contentId-2832367723&height=838&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**On top of the field**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=97b34a2053d7&id=ed001d06-3c46-4521-a496-c98bd76fec2a&&collection=contentId-2832367723&height=820&occurrenceKey=null&width=688&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Scrolling**

### Breakpoints & Platform Adaptations

#### Date field width

The width of the date fields can be set to 100% (full-width) or 50% of the container. It's also possible to set it to a fixed size. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=b46d88593076&id=6349b2b7-5b4f-4c1d-972e-6d3991918dbf&&collection=contentId-2832367723&height=552&occurrenceKey=null&width=974&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Calendar width and breakpoints

The appearance of the date picker changes depending on the platform and breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). In the modal view, which is used on mobile web and apps, the calendar is full-width (minus 16px margin). In the dropdown view, which is used on desktop, the calendar has a fixed width that can't be changed. The width depends on the brand and language. For example, in the aviv brand, in English, it has a width of 330px.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=3f2ed0bc487c&id=f44ce22b-cdb0-464d-be82-4391425d84bd&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Modal — App and mobile web (Breakpoint: XXS - XS (0 - 599 px))**

![](blob:https://media.staging.atl-paas.net/?type=file&localId=164d84086edc&id=46f36976-7102-4da5-8797-339c06b1e3fa&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=1680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Dropdown — Web only (Breakpoint: SM - XXXL (> 599 px))**

### Touch Target & Layout

Not documented

---

## Content & UX Writing

For English, French, German, Spanish and Dutch content, we use slashes and write the date as: dd/mm/yyyy. For more information please refer to the [Number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers).

---

## Accessibility (a11y)

Not documented

---

**Images pending manual placement** — the following 3 uploaded images could not be matched to their source captions and need to be dragged into place by hand: (1) Web/iOS "Date picker" screenshot, (2) Current day "Hover selected" state, (3) Dropdown view "Selecting and closing" screenshot.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=93d85c9f4c5e&id=31d501c3-0afd-4f21-8069-d19619b62b22&&collection=contentId-2832367723&height=352&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=355569fd6fb8&id=2e2c6ffa-a852-4c9a-a7f2-38ab05452250&&collection=contentId-2832367723&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=035e944fe4ce&id=fe3ca00c-7c68-44e4-83c4-ebb845aceb29&&collection=contentId-2832367723&height=1280&occurrenceKey=null&width=1680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
