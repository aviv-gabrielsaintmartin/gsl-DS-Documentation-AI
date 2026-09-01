<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831024238/Tabs | Last modified: Aug 21, 2026 -->

# Tabs

Tabs are used to organize related content into different views and allow users to seamlessly switch between them.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1e0f8456-b95c-4e3a-aeb8-4b612fa970bd&&collection=contentId-2831024238&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Web | iOS | Android |
| --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ |

* [Tabs on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7291)
* [Tabs on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-tabs--docs)

---

## Usage

Tabs organize related content that is at the same level of hierarchy. By separating content into distinct views, tabs help reduce clutter and allow users to easily switch between tasks or categories without leaving the page.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=33ebc325-712c-49ae-b6f3-c281a3b49019&&collection=contentId-2831024238&height=409&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use tabs to group related content into different views. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=793c9361-027c-4439-8cf7-9f0387140ce1&&collection=contentId-2831024238&height=409&occurrenceKey=null&width=355&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use tabs for linear step-by-step processes. Use the wizard instead. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=232b889e-8c2f-4094-b7c5-146a853c9099&&collection=contentId-2831024238&height=409&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use tabs for primary navigation or to move between pages of different hierarchy levels. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d2a5d257-5ea0-4306-9dac-a3e253ea4275&&collection=contentId-2831024238&height=409&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't use tabs to move between top-level pages in an app. Use the navigation bar instead. |

### Related Components

| Component | Usage |
| --- | --- |
| **Tabs** | Tabs organize related content into distinct views and allow users to switch between them without leaving the page. |
| **Navigation bar (app)** | Navigation bars allow users to navigate between different pages within an app. They persist throughout the app to help users move between high-level destinations. |

---

## Variants & Modifiers

### Number of items

Tabs are available with 2 to 5 elements. We don't recommend using more than this to avoid overwhelming the user.

### Modifiers

#### Icons

Icons can be positioned on the left or on top of the tab.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9a946e95-1760-4e40-8f28-f39cbce98a75&&collection=contentId-2831024238&height=403&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** On smaller screens with limited space, place the icons at the top to avoid scrolling. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e879c180-35df-4711-af95-d4754a9e4d22&&collection=contentId-2831024238&height=403&occurrenceKey=null&width=711&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** On wider screens, position the icons on the left. |

#### Badge

A badge can be placed next to the tab label.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9c364751-7659-4ca5-ac5a-7b1cddf40fb5&&collection=contentId-2831024238&height=406&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use badges to indicate notifications or updates. For example, for messages or alerts. |

---

## Behavior & Responsiveness

### Interactive States & Loading

* **States:** Each tab has the states default, hover, pressed and disabled.
* **Default selection:** By default, the tab component always has one tab preselected, typically the first tab. Only one tab can be active at a time. If the user selects a new element, the previous tab is automatically deactivated.
* **Interaction:** In order to change the active tab, the user must click on an inactive tab.

### Touch Target & Layout

* **Size:** Tabs can be configured to either adapt to the content length (Hug content), or be evenly distributed to fill the available container space (Fill container). Use the "Hug Content" option for varying tab lengths, preserving a more compact layout. Choose "Fill container" if you want the tabs to span the entire width.
* **Alignment:** Tabs can be aligned in different ways within their container. Use center alignment to position tabs evenly in the middle, creating a balanced look. Use left alignment to align tabs to the beginning of the container, which is useful for interfaces where a left-anchored layout is preferred.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Android & iOS** | When a row of tabs doesn't fit on the screen, the tabs become scrollable. |
| **Web** | Arrows need to be added to allow the user to navigate through them. Alternatively, for small spaces, consumers can implement the Compact Tab variant instead of [Scrolling and arrows](https://zeroheight.com/626199550/p/45521d-tabs/t/page-45521d-84054612-14) — when there are too many tabs to fit horizontally across the viewport, the tabs component can be displayed as a Dropdown. The width of the Compact version is relative to the width of the active state. |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f2ef07fb-a300-41b4-a2f8-1c54632a29f9&&collection=contentId-2831024238&height=364&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the arrows on the mobile web to ensure accessibility. This is critical to ensure that users with motor impairments, or those who rely on assistive technology, can comfortably access content without having to scroll or directly interact with dynamic elements. |

---

## Content & UX Writing

* **Label length:** When labelling tabs, keep the text short and descriptive. Use 1-2 words that accurately convey what the user will find when they click on the tabs.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
