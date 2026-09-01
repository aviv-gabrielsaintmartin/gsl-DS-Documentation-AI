<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450186/Segmented+control | Last modified: Aug 21, 2026 -->

# Segmented control

Segmented controls are used to select one option from a group of mutually exclusive choices. They are displayed as a horizontal row of buttons.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1800afa8-ce84-441b-85c6-35c8e6cb549d&&collection=contentId-2831450186&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | To Do 🚧 | To Do 🚧 | To Do 🚧 |

[Segmented control on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=15480-471)

---

## Usage

Segmented controls are used to choose between mutually exclusive options. They can be used to make selections within a form, to switch views or filter content. They are similar to [tabs](https://zeroheight.com/626199550/p/45521d-tabs).

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cee22758-fff5-4c39-adbb-a51853280ddf&&collection=contentId-2831450186&height=1280&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use segmented controls to allow users to choose between 2-5 options that are closely related and mutually exclusive. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=85387c1c-6188-431f-ba85-de63108cacd1&&collection=contentId-2831450186&height=1280&occurrenceKey=null&width=750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use segmented controls when there are more than 5-7 options. Use other selection components like dropdown or radio buttons instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Segmented control** | Segmented controls are horizontally arranged buttons that allow users to select one option from a group of mutually exclusive choices. They are often used to switch views or filter content within the same screen. There is always one option selected. |
| [**Tabs**](https://zeroheight.com/626199550/p/45521d-tabs) | Tabs are navigational components used to switch between distinct content areas or views, typically at the page or section level. There is always one option selected. |
| [**Button group**](https://zeroheight.com/626199550/p/83dfff-button-group) | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. It's possible to have nothing selected. |

---

## Variants & Modifiers

### Modifiers

#### Icons

Icons can be added as visual cues to provide clarity to the user. The icon is always to the left of the label.

| Icon only | Icon left | No icon |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e8846259-142f-4227-8bb4-14ce53bdf7e0&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=240&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a8e62366-2d7e-4d1f-a9e2-002d17edd5f6&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=416&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=74c91f13-2fd3-4f2c-afde-adec9c122edd&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=304&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7ad91f03-907f-4fe4-8ed5-88ffb59c3eb4&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=500&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Combine icons with text for clarity. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4ad17b67-9945-4413-a167-81b7a6681809&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=240&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid mixing different combinations. |

#### Badges

A badge can be placed next to the label.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=78cad86f-9f39-426f-b921-d789e0a3b6e4&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=512&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

### Interactive States & Loading

* The unselected buttons have the states default, hover, pressed and disabled. The selected buttons only have a default state.
* Segmented control components only support single-select. There is always one button selected per default.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=41c60708-f32b-4082-a03a-18e9952fb9bc&&collection=contentId-2831450186&height=640&occurrenceKey=null&width=760&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b97011b3-1aa8-4178-a863-e97e5d98791d&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=1040&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Touch Target & Layout

* **Width Adaptability:** The segmented control can either hug the content inside or fill a container.

| Hug content | Fill container |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7e4f3509-0046-48f7-9b90-1cf9d1bdc970&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=416&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d342dbb5-c4a2-4ef2-991d-ba9f7555ff51&&collection=contentId-2831450186&height=96&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start with a capital letter and do not use punctuation (nor colons).
* **Label Formula:** Noun form, of similar length across buttons.
* **Length Limits:** Keep button labels short and concise (1-3 words). Labels should be clear and descriptive.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
