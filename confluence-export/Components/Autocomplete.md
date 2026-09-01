<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831941697/Autocomplete | Last modified: Aug 13, 2026 -->

# Autocomplete

Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more efficiently by providing relevant results.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a0df8c7170d8&id=3185aabf-cefb-403e-a3d9-6add31cfc424&&collection=contentId-2831941697&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | Ready ✅ |

[Autocomplete on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7275) · [Autocomplete on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-autocomplete--docs)

---

## Usage

The autocomplete component is an advanced text input that simplifies the selection of one or more values from a long list of options.

### Platform

We use platform-specific autocomplete components that differ between Web, iOS and Android. The main differences are the platform-specific text field and the modal bottom sheet.

#### Web

On the web, the autocomplete appears in a full-screen modal bottom sheet on phones and as a standalone dropdown on desktop.

| Phone | Desktop |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=2f1dddb5637c&id=b07c220b-33e4-475a-bdbd-a895cfe36602&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=dad9d4e26b7e&id=9ea8c401-b50c-49a4-be7c-5addffacbfa6&&collection=contentId-2831941697&height=962&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### iOS

On iOS, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The iOS-specific text field and modal are used.

| Phone | Tablet |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6b7e86da421f&id=3f8d0e05-626a-4d85-9fcb-bc4ae5792932&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f1a8412ad2f7&id=5e483d74-52f5-4222-946b-d467c4b31e30&&collection=contentId-2831941697&height=2048&occurrenceKey=null&width=1536&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Android

On Android, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The Android-specific text field and modal are used.

| Phone | Tablet |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=ff75bad71a24&id=27fa2a24-3db7-47f3-ba97-1b2cb266050d&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a25cba909032&id=1f29e691-8887-4934-a374-88b2ea0c30bc&&collection=contentId-2831941697&height=2048&occurrenceKey=null&width=1536&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

* To help users find what they're looking for quickly when there's a large amount of data or options

### When NOT to use

* When there is a small, predefined list of choices — _Use Dropdown instead._

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a6980453010c&id=23396fe2-28bf-4c32-b0a4-6d9459390577&&collection=contentId-2831941697&height=880&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use autocomplete to help users find what they're looking for quickly when there's a large amount of data or options. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b0d5ca694270&id=6f769905-66b6-45a6-992f-4a8fe8c5deaf&&collection=contentId-2831941697&height=880&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Use the autocomplete when there is a small, predefined list of choices. Use a dropdown instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| [**Dropdown**](https://zeroheight.com/626199550/p/98cf75-dropdown) | High | Dropdowns display a predefined list of options for users to choose from. | When there's a small, predefined list of choices |

---

## Variants & Modifiers

### Modifiers

#### Dropdown list

The dropdown list consists of a mandatory label and an optional caption on the right. The number of displayed rows is defined by the consumer, with no fixed limit. The list rows are available in small and large heights.

| Small rows | Large rows |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=ba2443fdb425&id=8f4669ec-0486-4741-a600-444302ea3eb0&&collection=contentId-2831941697&height=486&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=330c3cb7395c&id=183955eb-b385-48cd-9480-6293ec7db168&&collection=contentId-2831941697&height=496&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The dropdown list includes an optional text button. The button is positioned at the end of the list.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=7764e3867063&id=12021ccd-7c0e-49c7-903c-ad7d56da9407&&collection=contentId-2831941697&height=592&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=38fb03bb52c2&id=92754309-2765-4db2-83d4-30ca59b34014&&collection=contentId-2831941697&height=1232&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the button for geolocation tracking. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1145f24c4482&id=ecc9c20e-fe5c-4d61-b1cb-d9c1a7e79711&&collection=contentId-2831941697&height=1232&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the button to help users when they can't find the result they expect. |

The dropdown list also includes optional icons on the left and right.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=4ae11619d214&id=6d984351-becd-48db-a47d-9ec462e0cca4&&collection=contentId-2831941697&height=496&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Text field

The autocomplete contains a text field. See the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-97e03c-84052978-35) to learn more about the modifiers of this component.

#### Modal

On iOS/Android tablets, the autocomplete appears in a modal. See the [modal bottom sheet documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet) to learn more about this component's modifiers.

#### Top bar

The autocomplete on phones contains a top bar. See the [top bar documentation](https://zeroheight.com/626199550/p/27f21d-top-bar) to learn more about the modifiers of this component.

---

## Behavior & Responsiveness

### Interactive States & Loading

The autocomplete component has the following main states:

* **Default empty:** The input field is inactive, meaning the user hasn't yet interacted with the field.
* **Active empty:** The input field is active (focused) but still empty, ready for user input.
* **Filled:** The user has entered text, and a dropdown list of matching suggestions appears below the input field.
* **No results:** No matching options were found. A message informs the user, with additional text offering suggestions or alternative actions.

| State | Phone | Desktop |
| --- | --- | --- |
| Default empty | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=543291d55ce9&id=5d241586-4b26-44b6-9e86-38fd8b3a090b&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9f394e0bed0f&id=5a8ed8a1-f049-4699-a4f7-33f0f54ed4fc&&collection=contentId-2831941697&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |
| Active empty | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=60e3ef7e14b6&id=5cd19b64-6074-4a18-addc-a4695f141c2a&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f2864fc219b7&id=a8aedc71-dc37-4882-841d-2b343ee50e91&&collection=contentId-2831941697&height=152&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |
| Filled | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=26e9be3fc484&id=b07c220b-33e4-475a-bdbd-a895cfe36602&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3d4ee4847544&id=9ea8c401-b50c-49a4-be7c-5addffacbfa6&&collection=contentId-2831941697&height=962&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |
| No results | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=83750b6fa810&id=a7488f92-4955-483f-9930-c50721bb0566&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9bb3049419b7&id=38486d6d-5a7a-45f0-87c7-8af36023c0b8&&collection=contentId-2831941697&height=402&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Interaction — Desktop:** the dropdown list opens when the user begins typing in the input field. It closes when the user selects an option from the list, clicks outside the dropdown, or presses the Esc key twice.

| Opening | Selecting and closing | Closing |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=42cedfd5321d&id=53756fe9-f4c9-409a-b75e-3f2dfb31fd13&&collection=contentId-2831941697&height=178&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Typing in the field | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7d27955094f7&id=f0d37cdb-4736-4c16-92e4-50fb9c1cb5b1&&collection=contentId-2831941697&height=530&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Clicking an option | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=320e58d411e6&id=c936d767-aa48-4777-8896-686a2adc32a1&&collection=contentId-2831941697&height=530&occurrenceKey=null&width=696&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Clicking outside the dropdown or pressing the Esc key twice |

**Interaction — Phone and tablets:** autocomplete opens in a modal bottom sheet (full-screen on phones and modal on tablets) when the user presses the input field. In the modal, the user can filter results by typing in the text field. When the user selects an option, the modal closes. The user can also close the modal by tapping the x-button.

| Opening | Selecting and closing | Closing |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=99de6f1e31ee&id=171b8c86-cdb3-4cfe-9a07-5d19962010c4&&collection=contentId-2831941697&height=178&occurrenceKey=null&width=560&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Tapping the field | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c0169a3f2366&id=89cb35cf-a7f2-4f6a-bbb8-864ee7ceb49d&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Tapping an option | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=01ea71c5e2f8&id=17356e85-5ffb-4790-b1a9-d76ae284f72c&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Tapping the x-button |

The rows in the dropdown list have the states default, hover and pressed. They can be selected or unselected.

| Unselected | Selected |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8217addb8575&id=cc621009-ff73-4dbc-82b2-afd81e734b93&&collection=contentId-2831941697&height=384&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=dd436423b6ec&id=10109887-cb60-420b-b28f-b1d01a9e2b5f&&collection=contentId-2831941697&height=384&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The loading state appears when suggestions are being fetched after the user enters a query.

| Phone | Desktop |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=09450a530776&id=f4789630-9a29-43a1-8822-7150fbb634f2&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3777f368ea1f&id=de5b0288-103c-46b4-b9cb-37812943278b&&collection=contentId-2831941697&height=274&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

By default, the dropdown list is positioned below the field. On desktop, it is placed above the field if there is not enough space below it. If the options exceed the available space, the dropdown list becomes scrollable — whether the scrollbar is visible depends on the user's system settings. To avoid complexity, not all positions are available in Figma; feel free to detach the component.

| Phone | Desktop |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=bb31bf9af51c&id=c9b0f996-6565-4e41-9d72-926c39dcc011&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=97728db8824c&id=b0efb6d7-8f37-4f57-a868-9f51d82f4709&&collection=contentId-2831941697&height=866&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a302db3c9fbb&id=78c07ba9-0c51-4a91-bf65-a576ad697f72&&collection=contentId-2831941697&height=862&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Breakpoints & Platform Adaptations

The style of the autocomplete depends on the breakpoint on web and Android, and on the device on iOS. See our [grids and breakpoints guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| Web: XXS – XS (0–599px)  
Android: Medium – Expanded (>599dp)  
iOS: iPhone | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3baa9e0d5d4d&id=b07c220b-33e4-475a-bdbd-a895cfe36602&&collection=contentId-2831941697&height=1152&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Full page — full-screen modal bottom sheet |
| Web: SM – XXXL (>599px)  
Android: Compact (0–599dp)  
iOS: iPad | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b8e6aa85184a&id=9ea8c401-b50c-49a4-be7c-5addffacbfa6&&collection=contentId-2831941697&height=962&occurrenceKey=null&width=576&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Standalone dropdown |

---

## Content & UX Writing

* **Text field:** Refer to the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-980e7b-84054521-39) to learn about labels, helper and placeholder texts in the input field.
* **Dropdown list:** The label should clearly identify the option — use a value of your choice depending on the requirement (e.g. name of town, department, district, street...). The caption should provide supporting details (e.g. department, town, district...). Try to keep it under 2 lines.
* **No results:** Refer to the [info state documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/84818f-info-state/t/page-7142d3-87401819-40) to learn more.

---

## Accessibility (a11y)

Not documented
