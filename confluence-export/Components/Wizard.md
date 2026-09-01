<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830991466/Wizard | Last modified: Aug 21, 2026 -->

# Wizard

Wizards guide users through step-by-step processes to achieve their goal.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

[Wizard on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7269) · [Wizard on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-wizard--docs)

---

## Usage

Wizards guide users through a multi-step processes by breaking it down into smaller, more manageable tasks. Each step is presented sequentially, with visual indicators showing which steps are completed, active, or pending. This helps users navigate complex processes with ease and provides a clear sense of progress.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f3c9efa5-5cfa-478e-ad9d-530173723d6f&&collection=contentId-2830991466&height=1528&occurrenceKey=null&width=2108&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f3c9efa5-5cfa-478e-ad9d-530173723d6f&&collection=contentId-2830991466&height=1528&occurrenceKey=null&width=2108&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the wizard to guide users through a linear, step-by-step process. |

### Related Components

Not documented

---

## Variants & Modifiers

### List type

The wizard list is available as an unordered or numbered list.

| Unordered list | Numbered list |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cecea0d2-0ded-4e9b-8070-bfa8e6b7771a&&collection=contentId-2830991466&height=1200&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e0b44ae0-dfaa-42a9-b528-c40ca1e09fd1&&collection=contentId-2830991466&height=1200&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Unordered list:** Used when the user needs the flexibility to jump between steps without following a strict sequence. This variant is suitable for tasks where the order of completion is not critical.

**Numbered list:** Used when processes must be completed in a specific order, where each step depends on the completion of the previous one. This variant is suitable for tasks where linear progress is crucial.

### Modifiers

#### Description

The description is optional.

| With description | Without description |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1953461e-40af-4948-a833-5c39fe5bcc71&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=432&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e75334e5-f00b-4a95-ba0e-86c8a8ada9a6&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=432&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

The wizard has the step types to do, done, error and disabled. Each type of step has the states default, hover and pressed.

#### To do

Uncompleted steps are marked with a black circle.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=85855809-cbdf-4736-bd78-6f1afd9116dd&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=14c92cd7-5f45-4dcd-9e86-22315dbf271b&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c6c5e246-1ee0-4599-8932-2752f795b796&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default active | Hover active | Pressed active |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0b3bae3c-eefa-4c97-90a6-dc797227ac13&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e4769fc0-194d-4409-a0a7-0bebb23b4031&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=09c493cd-57f2-4ca2-8209-4853865f2a79&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Done

Validated steps are marked with a check mark in a green circle. This includes mandatory steps that have been completed or non-mandatory steps that don't need to be completed.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=34b66ace-a729-476e-a3ed-20576e26f639&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2d36c58e-5eaf-4325-ae34-736bf37e4f46&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8f509521-6049-4cba-93f7-8e72197c877e&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default active | Hover active | Pressed active |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f2df39f4-3e16-4b02-b340-74e10bab66a2&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e20f9571-f2d3-4ca4-9fd0-849a5a8163e3&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7da0a654-eed6-44b1-ba0d-4db6f47a0ec0&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Error

Input errors are marked with an exclamation mark in a red circle.

| Default | Hover | Default active | Hover active | Pressed active |
| --- | --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cf7e2250-271f-4536-ac84-bf0586f8a44a&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=832ea61d-cffd-4e34-b5e1-e9f23d0ea71b&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=70d93481-64ad-4d83-9ac1-7c10e0f31541&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=924da4db-e6d4-465a-8a47-3356d3e9f308&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=fbbf8cae-08be-482f-8049-11e6fe701a4d&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Disabled

Steps that are not yet clickable because other steps must be completed first are grayed out.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0f9b9591-0f1e-457d-95ad-bdd37a8a37b6&&collection=contentId-2830991466&height=120&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Figma tip:** If the vertical lines between steps have the wrong color, select the layer Top line or Bottom line and change the variant to Done, To do or Disabled. If it's the first or last step select Start or End.

### Touch Target & Layout

* **Interaction:** Each row is clickable, but the icon is not.
* **Width:** The width of the wizard is determined by its content. If the container is smaller than the title and description, the text flows to the next line. Texts have a maximum length of two lines. If the text is longer, it is truncated.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=075795f6-eefd-47f0-9779-7975db6c8b3c&&collection=contentId-2830991466&height=720&occurrenceKey=null&width=656&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Breakpoints & Platform Adaptations

**Desktop:** On desktop the wizard can be used on its own or can be placed on any background. For example, it can be used in a sidebar.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c66547fa-7b7e-42aa-acfb-f10662b05635&&collection=contentId-2830991466&height=1400&occurrenceKey=null&width=2232&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
**Mobile:** On mobile devices, the wizard must be placed inside a modal bottom sheet.

| Phone | Tablet |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=eec3b582-595a-49a1-adcd-e725e7c4666b&&collection=contentId-2830991466&height=1448&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8ca8a463-872d-449b-b383-0fd2c7c78396&&collection=contentId-2830991466&height=2048&occurrenceKey=null&width=1536&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Entry point:** The top bar can be used as an entry point to open the modal bottom sheet.

| Web | iOS | Android |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=83506551-4a9f-41ca-8459-d0bd1500da05&&collection=contentId-2830991466&height=192&occurrenceKey=null&width=784&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f7e7a650-46fa-4483-b029-c1a7d6feca3a&&collection=contentId-2830991466&height=176&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=565125d1-7885-4536-b45b-f91c87b79204&&collection=contentId-2830991466&height=192&occurrenceKey=null&width=768&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Scrolling:** If the wizard is longer than the container, it becomes scrollable.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=451c86f8-0227-4ffc-935c-154f4b6afece&&collection=contentId-2830991466&height=816&occurrenceKey=null&width=752&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Content & UX Writing

* **Step titles:** Should be descriptive and help users understand what is expected of them. Keep titles short and concise, using 1-3 words. Start with a capital letter. Use consistent terminology between the wizard and your page titles to avoid confusion.
* **Step descriptions:** Use short, clear language to describe the user's progress. If needed, provide a simple summary of completed steps.
* **Progress indication:** Where appropriate, use numbers to clearly indicate progress through the steps.
* **Overflow content:** Title and description are limited to two lines. If the text is longer, it will be truncated.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
