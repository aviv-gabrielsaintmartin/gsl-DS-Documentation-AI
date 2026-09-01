<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2740060239/Accordion | Last modified: Aug 13, 2026 -->

# Accordion

Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of information in a compact space.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c69911a7-5ef9-4c2b-81b4-0ea5b769c160&&collection=contentId-2740060239&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Accordion on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?m=auto&node-id=11-136048&t=k234WjfNSw8D6uVC-1) · [Accordion on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-accordion--docs)

---

## Usage

Accordions are typically used when screen real estate is limited, and there's a need to manage the visibility of large amounts of content. They enhance the user experience by presenting information in a structured, efficient manner, allowing users to access details as needed without having to navigate away from the current context.

### When to use

* Use accordions to shorten pages by grouping related information together and reduce scrolling for non-crucial content, especially on mobile interfaces, enhances the user experience.

### When NOT to use

* Be aware that when you use an accordion, you are hiding content from users.
* Accordions should not be used to display essential information, as hiding content behind an accordion can reduce users' awareness of that information.

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=aedad21e-698a-4efc-8b18-7ad24a63f63e&&collection=contentId-2740060239&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use accordions to contain secondary or supporting content that is complementary. This reduces screen clutter and makes it easier to quickly scan through content. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c4c9a287-8291-4a6a-a11f-9ebb2a90f565&&collection=contentId-2740060239&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't put blocking crucial content inside an accordion where users can't move forward without digging into an accordion. Important messages should not be hidden inside an accordion. |

### Related Components

Not documented

---

## Variants & Modifiers

### Border

The accordion is available with or without a border. The bordered version has a white background whereas the unbordered version has a transparent background.

| With border | Without border |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c8615548-0b41-4a86-889d-b63d500f15c0&&collection=contentId-2740060239&height=280&occurrenceKey=null&width=1520&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Accordions with borders are used when the accordion needs to be visually prominent, especially on pages with colored or patterned backgrounds. The white background improves readability by providing a clear contrast to the surrounding content, making it easier for users to focus on the accordion's text. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=445627d5-f042-4406-b10a-61ca162b2caa&&collection=contentId-2740060239&height=282&occurrenceKey=null&width=1520&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Accordions without borders are used on pages with a solid, neutral background, where readability isn't an issue. |

### Modifiers

#### Icons

Icons are used to highlight and complement the text in the accordion's header.

| With icon | Without icon |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e99bb677-5fb1-49a1-9462-feb13f49e974&&collection=contentId-2740060239&height=280&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=71861ea0-44cb-4b25-b4a7-6a8fdb254d69&&collection=contentId-2740060239&height=280&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Title, body and description text

Title, body, and description text are optional elements that can be toggled on/off depending on the use case. The size of the title depends on the platform.

| Web | iOS/Android |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6a7b97ef-80ef-41d5-8694-f5f7a1fbd01d&&collection=contentId-2740060239&height=456&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) On Web to title sizes (22px and 16px) are available. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=49942329-dd20-4da9-b610-41b50165f1b4&&collection=contentId-2740060239&height=456&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) On iOS/Android only the smaller title size (16px) is available. |

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=2bb137fb-3129-4319-b3c9-8d6826ea2153&&collection=contentId-2740060239&height=994&occurrenceKey=null&width=718&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use only one title size and combine it with body or description text. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a681ae09-5d3e-4fe5-8a74-20e3b4bf3250&&collection=contentId-2740060239&height=994&occurrenceKey=null&width=718&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use both titles at the same time. |

#### Content

All types of content, such as text, images, and other components, can be placed inside the accordion.

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=14124976-2e9d-43ad-8116-7efa845247f7&&collection=contentId-2740060239&height=1258&occurrenceKey=null&width=718&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use text, images or other component inside the accordion. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=84fa3b92-c802-4a79-8cda-65f4790dc223&&collection=contentId-2740060239&height=1258&occurrenceKey=null&width=718&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't nest other accordions inside the accordion component. This makes it confusing and makes the content difficult to access. |

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Accordions have the states default, hovered, pressed, and disabled.
* **Interaction:** The accordion can be collapsed or expanded by clicking on the header of the accordion. The chevron icon at the end indicates the current state, pointing down when collapsed and up when expanded.

| Expanding | Collapsing |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=04167907-cc67-41e4-bac1-b01018e5c2b0&&collection=contentId-2740060239&height=568&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9624d652-a99b-42e1-98a9-830324204eb4&&collection=contentId-2740060239&height=568&occurrenceKey=null&width=1552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

* By default, accordions start in a collapsed state with all content panels closed. Starting in a collapsed state gives the user a high-level view of the information available.
* There may be a scenario where it is necessary to have a single panel open by default, while keeping the rest of the panels closed is helpful to surface content. This can allow users to notice information immediately and encourage them to explore the content of other panels.
* Accordions should never collapse due to interactions with other accordions. If there are a number of accordions in the same group, and a user expands the first accordion and then a second without collapsing the first, both accordions should remain expanded. Automatically collapsing accordions based on interactions with other accordions degrades usability and risks confusing the user about their location on the page.

| DO | DON'T | CAUTION |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f00f39f4-061c-406d-bacd-00161d63e8ba&&collection=contentId-2740060239&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** By default, all content panels are closed. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f2bbdd26-9134-4c40-a9fc-def2346f49b3&&collection=contentId-2740060239&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Avoid displaying all accordion panels expanded by default. This can increase the length of the page and make it difficult to find each panel. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=227dd045-6a78-41ab-badf-80224bd75272&&collection=contentId-2740060239&height=260&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** In a case where there is a set list view of accordion panels, the first panel is set to open by default. |

### Touch Target & Layout

* **Width Adaptability:** The accordion adjusts to the width of its container, filling the available space based on the size of the container.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Use sentence-style capitalization - capitalize only the first word.
* **Header Length:** An accordion header should give an idea of the content in the accordion panel. Keep headers short. By default, header content wraps to the next line at smaller widths, and multiple lines of text can be difficult to scan.

---

## Accessibility (a11y)

Not documented
