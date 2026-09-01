<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832400439/Toggle | Last modified: Aug 21, 2026 -->

# Toggle

Toggles are used to switch between on and off states.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=16e29328-9e7a-4b4e-ad95-8d558344c257&&collection=contentId-2832400439&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Toggle on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7286&t=cY0FVB8lofjw9Zwd-11) · [Toggle on Storybook](https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-toggle--docs)

---

## Usage

The toggle component is a component that allows users to switch between two states: on and off. It is commonly used when a user needs to enable or disable a feature or option.

### Platform

On the web, we use custom toggles. On Android and iOS, we use native toggles.

| Web | Android | iOS |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=94fc8489-988b-4c64-bf4e-188d278bd337&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f3cd269a-1d22-48e4-97b1-966d95e77dbf&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3fb2180b-acd6-4f83-a31f-b366796846cd&&collection=contentId-2832400439&height=97&occurrenceKey=null&width=668&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7262e047-d321-41bc-a110-6de577e59aa7&&collection=contentId-2832400439&height=658&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use toggles for binary on/off choices, where the selection is applied immediately. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f79030cf-e81f-49e3-9845-072b26335100&&collection=contentId-2832400439&height=288&occurrenceKey=null&width=672&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Avoid using toggle inside forms. Toggles should take effect immediately, without having to submit a form. Use checkboxes instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b3b9a519-fbc3-4856-854c-0fd6a4ef4ab4&&collection=contentId-2832400439&height=504&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** When you want to use toggles in a list, consider using the toggle group component. |

### Related Components

| Component | Usage |
| --- | --- |
| **Toggle** | Toggles are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving. |
| [**Checkbox**](https://zeroheight.com/626199550/p/3044f1-checkbox) | Checkboxes allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. |
| [**Radio button**](https://zeroheight.com/626199550/p/55bfd7-radio-button-group) | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. |

---

## Variants & Modifiers

### Toggle position

Toggle can be positioned on the left or on the right depending on the use case.

| Left | Right |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=94fc8489-988b-4c64-bf4e-188d278bd337&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20e0bf7b-cee3-491b-9c2c-ace64131f16a&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Modifiers

Toggles have the same elements as all form components:

* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the toggle label

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

| Optional | Required | Tooltip |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e3c905be-2de3-41e7-9791-408a37b6a2a7&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | _Image not available in source export_ | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d2d95a52-35d2-42e5-a53d-f771fe0c8ce5&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Neutral

Toggles have the states default, hover, pressed, and disabled. They can be selected or unselected. Unlike [checkboxes](https://zeroheight.com/626199550/p/3044f1-checkbox) or [radio buttons](https://zeroheight.com/626199550/p/55bfd7-radio-button-group), they don't have a red border indicating an error state, but they have an error message.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20e0bf7b-cee3-491b-9c2c-ace64131f16a&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bb9820b6-53c3-4800-89e6-ae6bedb66664&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20e70add-a5bb-42de-aca9-e0aedc22fdfd&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=151a7837-a1b7-467a-a33c-1159c223232f&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d5e793c4-c934-4068-ae2b-fff6baa22551&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c333be31-3f67-4430-ad35-67426fdf1ac8&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3f1f4ed5-f5e6-4650-be17-aa813187f171&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9a253716-0906-4198-93e1-55592ee730c4&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Error

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5b69a43e-758d-4c10-bd6e-c72424fc8959&&collection=contentId-2832400439&height=136&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Loading

This state is typically triggered when the action initiated upon click involves an API call or server query. This provides the user with a visual indication that their action is being processed.

During this waiting period, a loader will be shown in place of the toggle. If the loading process fails, a snackbar can be utilized to display the error message.

To avoid a flashing effect, the loader will be displayed for a minimum of 600 milliseconds.

| iOS | Web & Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=db947370-99b1-4fd3-a347-6d52c488d9a0&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=79142d0e-53cb-467e-b886-8142a7aa14ea&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

**Interaction:** Not only the toggle itself is clickable, but also the entire row. The row height is 48px.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e7c20c3b-ffd2-488e-8843-eda256fb2eaf&&collection=contentId-2832400439&height=96&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Width:** The width of the toggle component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

**Toggle lists** — Lists that use toggles should start with an uppercase letter.

**Toggle labels** — Always use clear and concise labels for toggles. Labels appear to the right or left of the toggle.

**Overflow content** — We recommend that toggle labels be less than 3 words. Don't use an ellipsis to cut off the text of a toggle label. If necessary, use 2 lines.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
