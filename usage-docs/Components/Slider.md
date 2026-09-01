<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450204/Slider | Last modified: Aug 21, 2026 -->

# Slider

A range slider can be used to select a single value or a range between minimum and maximum values.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bc3913cd-1df2-4427-bf43-3673145aa488&&collection=contentId-2831450204&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | WIP 🚧 | To-do 🚧 | To-do 🚧 |

* [Slider on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=10755-46456)

---

## Usage

The slider component allows users to select a value from a specified range by sliding a handle along a track. This is particularly useful for adjusting settings such as volume, brightness, or any other numerical value.

The range slider allows to select a range by sliding 2 handles along the track. This is useful to choose a price range, a distance or any range.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9aad6af6-fbab-4a0e-a7ef-5469d1ef0b80&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9f19a7e4-2db4-4044-9fbb-66dade1cd888&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

Not documented

### Related Components

Not documented

---

## Variants & Modifiers

### Modifiers

#### Display the selected value

The slider value should always be visible to the user. By default, it can be displayed on the top right of the component.

The value can be hidden if displayed in another place on the screen or if the selection value is visible in live such as when cropping an image.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9aad6af6-fbab-4a0e-a7ef-5469d1ef0b80&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9f19a7e4-2db4-4044-9fbb-66dade1cd888&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Display the min and max value

The minimum and maximum selectable value can be displayed on the left and right of the slider.

Those values are mandatory when selecting a numeric value but not for other use cases such as sound level selection slider.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5793f2aa-e6a9-4db7-aa9e-a34152b1d311&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5cee28cd-a4b5-4022-8f8a-2666040478bc&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Display the steps marks

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4a56d14d-265e-448a-a57a-8c632d821db0&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2ad11f23-3d7b-4ec1-a5ee-a23b0b39c5a6&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Display the steps values

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4045a68d-99cb-4816-902f-3c959b243a64&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bc2abcbb-8ba1-437f-8a88-16eda9de6db1&&collection=contentId-2831450204&height=158&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Display the text fields

When a numeric value is selectable, you can display the text field, allowing user to write directly the requested value.

This is strongly recommend when a precise value such as the monthly revenue.

When the text field is displayed, the selected value is hidden.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d25a58c7-57fd-4a99-b69c-25090b61537b&&collection=contentId-2831450204&height=262&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=08461c45-c058-4193-8a59-1bdd32aa78f5&&collection=contentId-2831450204&height=262&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Display the header

When used as a form element, you can display the form header, including the tooltip trigger, required and/or optional mentions and the helper text.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e942b85e-a6ff-49be-bde2-d74f34a1d411&&collection=contentId-2831450204&height=238&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a4f85218-bad5-4df0-8c7d-9fdd0c496930&&collection=contentId-2831450204&height=238&occurrenceKey=null&width=577&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** The slider itself has the states default and disabled. The handles have all the states: default, hover, pressed and disabled.
* **Disabled State Guidance:** The slider can be fully disabled, preventing interaction with both the track and the handles.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=442d6ea1-dc5b-4d2c-924f-d80af0a8d13c&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d6636762-95f9-4c91-b3cd-6a23ae8564de&&collection=contentId-2831450204&height=142&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6ddef17d-3233-4a1e-9b4a-ca0f68dd58df&&collection=contentId-2831450204&height=132&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6cc450b9-7608-4532-b31a-2e564013412d&&collection=contentId-2831450204&height=132&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Error:** the error can only occur when the text fields are displayed. The error occurs when the user writes a value that is outside the allowed range. On click on the slider track, the value is selected and the error disappears. The user should correct the error themselves.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=982e042a-c1cb-46ac-b500-58b8cea93b7e&&collection=contentId-2831450204&height=358&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9f62de7e-0239-4b84-ace9-d9cfa18884ef&&collection=contentId-2831450204&height=358&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Interaction:** value selection by touch/click — on click on the track, the closest handle will move where the click happens. Value selection by filling the text fields — when the text field is displayed, any change in the handle position will automatically update the value of the text field; conversely, updating the text field value will also adjust the handle position accordingly.

### Touch Target & Layout

* **Width Adaptability:** The slider adjusts to the width of its container, filling the available space based on the size of the container. The minimum recommended width is 288px (minimum mobile size minus the left and right margin).

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Labels:** Slider should always have a label, to help the user understand what information to enter.
* **Capitalization:** Start with a capital letter and use no punctuation (including colons) for labels; helper text uses sentence-style capitalization and punctuation.
* **Label Formula:** Keep the label in noun form.
* **Length Limits:** Keep the label short and concise (1-3 words).
* **Helper text (optional):** Add a helper text if the user needs assistance completing a field. Helper text is optional and can be used instead of a tooltip. When used, it is always available when the input is focused and appears below the field — exceptions are when an error or warning message replaces the helper text in apps.
* For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
