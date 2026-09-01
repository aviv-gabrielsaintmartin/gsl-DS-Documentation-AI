<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832203875/Progress+bar | Last modified: Aug 21, 2026 -->

# Progress bar

A progress bar shows a task's progress.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f56ac6b0-7ec8-4762-9d1e-14a2111f917f&&collection=contentId-2832203875&height=267&occurrenceKey=null&width=980&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

* [Progress bar on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=8346-132327)
* [Progress bar on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-progressbar--docs)

---

## Usage

We only provide the progress bar itself. Other elements, such as labels, can be added, removed or customized to suit your needs, depending on the context. Please share your use cases with us to help improve the guidelines.

| Stepper | Bar |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=01deebb0-0a00-4632-bdad-7097f3aae149&&collection=contentId-2832203875&height=496&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) It serve as a simple stepper, augmented with additional labels to enhance clarity and understanding. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=845d2cae-f304-4259-b43d-50d459c47cff&&collection=contentId-2832203875&height=496&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) The progress bar can be a simple graph and a valuable visual representation of task completion. |

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

### Styles

| Default | Inverted (on dark background) | Neutral | Success |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9103a3be-5166-4b72-ac47-5a4b80fc5c3d&&collection=contentId-2832203875&height=144&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=37d405bd-f14d-4c37-9560-530460194963&&collection=contentId-2832203875&height=144&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=63d76ba1-75d6-47cd-b897-8fa026044737&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=466&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=25ef1b0e-eeed-4d53-9b80-5472dd655107&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=466&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Size

| 4px | 8px (default) | 16px |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=95a7f115-4d70-4a3d-a70f-bfd24f54e73e&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bd03bccc-ebe8-490a-8d93-5fae7748b16f&&collection=contentId-2832203875&height=80&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2fb9bbb7-e68f-4d06-ad76-68680ff8e220&&collection=contentId-2832203875&height=96&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**4px:** Only recommended when the progress bar has a small hierarchy in the interface.

### Width

The width can be adapted to the context.

| Fixed | Full width |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e39f2619-b253-4f2c-9547-35a8711968b9&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=00a1b25a-844d-4aab-985f-d5f64d8f1120&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Labels

The progress bar alone does not provide sufficient information to be accessible. It should be accompanied by a numerical progress label (e.g. 75% or 1/5). Both the positioning and size can be customized to suit your needs, depending on the context.

| Left | Right |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=80fced52-11b5-4dbf-82fd-8a171aff5b35&&collection=contentId-2832203875&height=176&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=688f19d2-104e-45b0-a9a1-40f7c90e3f17&&collection=contentId-2832203875&height=176&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

| Default | In progress | Done | Success |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3b8e165e-c2b5-4520-888c-57d09a2db9be&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f6477588-1ec9-4cff-8743-7620691c62cf&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5b514ef4-d34a-4a97-b08f-e10b5575c09c&&collection=contentId-2832203875&height=72&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2752736b-ff05-43d2-b963-81f9fa9dd4b9&&collection=contentId-2832203875&height=112&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Success:** This state is not mandatory. It's recommend to use it when the bar is used as a chart and not a stepper.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
