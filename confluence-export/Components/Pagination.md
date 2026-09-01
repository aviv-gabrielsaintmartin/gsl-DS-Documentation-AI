<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832597057/Pagination | Last modified: Aug 21, 2026 -->

# Pagination

Pagination divides content into smaller, numbered pages, making it easier for users to navigate through large amounts of content.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | N/A | N/A |

**⚠️ Web only**

* [Pagination on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7290)
* [Pagination on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-pagination--docs)

---

## Usage

Pagination helps users navigate through large amounts of content by dividing it into multiple pages. It provides controls that allow users to move forward, backward or to a specific page. It reduces cognitive load by allowing users to focus on smaller, more manageable chunks of content at a time. Pagination also improves performance by reducing the amount of content that needs to be loaded at once.

### Platform

The pagination component is only used on the web. On iOS/Android, we recommend using infinite scrolling.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e581d525-61ac-4093-9f90-c119e28f37b7&&collection=contentId-2832597057&height=932&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use pagination to display large amounts of content, such as search results, reviews or lists. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b69f1953-b7ed-4b41-8420-ac652affde88&&collection=contentId-2832597057&height=932&occurrenceKey=null&width=780&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use pagination for linear, step-by-step processes. Use the wizard instead. |

### Related Components

Not documented

---

## Variants & Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

The digit buttons in the pagination have the states default, hover, pressed and disabled. They can be selected or deselected.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=fe2afd4a-a0df-46b8-b3b1-cc80c56793ab&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=edf64a22-0c90-45fe-a148-61ceb0def9e6&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=99f926bf-7bbc-4580-ade5-ff167d3e67b9&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=cd3d232c-5c5e-4bcd-9b06-a41646a977d3&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=04a26aa9-d7ed-4ff2-844e-f39bf0d9f9e0&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bf482322-ca93-4f78-b16e-1a0b74aa8f79&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=04163030-09ac-4b6f-b4f8-cf929ad661ce&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ae497945-949d-4d02-8c3c-b97e4d65d094&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=80&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Interaction:** To navigate to another page, users can either select a page number or use the chevron buttons to go to the next or previous page. When the first/last page is selected, the back/forward chevron is hidden.

| Go to next page | Go to previous page | Go to a specific page |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a6023ce7-0d02-47c6-8009-8725c8d608a9&&collection=contentId-2832597057&height=108&occurrenceKey=null&width=520&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=07fd8c6b-85ac-4ee9-b4bb-c8ef578e11dc&&collection=contentId-2832597057&height=108&occurrenceKey=null&width=512&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=92606836-7179-490a-8ada-429806cf9ea2&&collection=contentId-2832597057&height=108&occurrenceKey=null&width=624&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Touch Target & Layout

**Truncation:** Pagination is truncated when a threshold number of pages (4 - 5) is reached. It truncates the pagination by displaying only the most important pages, such as the first, last and nearest pages, while using ellipses to indicate skipped pages. The truncation ellipse is not clickable.

| First page selected | Last page selected | Middle page selected |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=53d76e3e-eed2-4c91-9854-5d72aba1c989&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=512&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d69488b2-a2ee-494d-a9fe-ae508d7e8bcd&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=512&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=de6c7a30-3ef9-4d77-a441-cecffaaeabca&&collection=contentId-2832597057&height=80&occurrenceKey=null&width=784&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Position:** Pagination is positioned at the bottom of the pageable content, allowing users to reach the end of the current page or section before deciding to navigate to the next. Pagination is centred in most cases, but can be left or right aligned depending on the layout.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e581d525-61ac-4093-9f90-c119e28f37b7&&collection=contentId-2832597057&height=932&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
