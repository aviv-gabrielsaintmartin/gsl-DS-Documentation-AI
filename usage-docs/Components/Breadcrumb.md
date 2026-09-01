<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832302192/Breadcrumb | Last modified: Aug 21, 2026 -->

# Breadcrumb

Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. They help users keep track of their location and allow them to navigate between pages.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ (owned by Header/Footer team) | Ready ✅ | N/A — web only | N/A — web only |

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20d0c4c4-9a4d-4349-a3b6-e705c1ec80ec&&collection=contentId-2832302192&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
* [Breadcrumb on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7262)

---

## Usage

Breadcrumbs are a navigational aid that displays the user's current location within a hierarchy and allows them to trace their path back to previous sections. They help improve navigation by providing a clear trail of links, making it easier to understand the structure and move between different levels of content.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=827145a3-d7ac-4516-948a-6cb5d74fa014&&collection=contentId-2832302192&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Platform

Breadcrumbs are only used on the web. On iOS/Android, other navigation concepts are used, such as using the navigation bar or simply a back button.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c7fd9ffc-1c75-437a-9808-d78d79c227cb&&collection=contentId-2832302192&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use breadcrumbs when content is organized hierarchically or has deep navigation layers, to help users understand their location and easily backtrack through the structure. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=64bb6248-e912-4697-8f7c-0ada58728407&&collection=contentId-2832302192&height=436&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use breadcrumbs when users are likely to have landed on the page from external sources, such as search engines, to provide context and improve SEO. |

| DON'T |
| --- |
| **DON'T:** Don't rely on breadcrumbs as your primary navigation. Use the navigation bar (header) instead. |

### Related Components

Not documented

---

## Variants & Modifiers

### Modifiers

#### Icons

Breadcrumb links are available with an icon to the left or right. External links should be marked with the external link icon.

| Icon left | Icon right | External link icon |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4b9b5386-89b1-48d7-abd9-9a80e1fc08fd&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=476c53b9-ae02-4b34-86e3-0e93047f10a9&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8eeee1bd-a7c4-4736-accc-5ed2c7dc9c0b&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

All links in the breadcrumbs have the states default, hover and pressed. We don't recommend disabling links, as this defeats their purpose of providing easy navigation through the site's structure.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f4aa0a92-21e1-4f80-8379-fdea34293bc7&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=4ab1d94b-f02b-446d-8e9e-6364a56c35cb&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=0804188f-34c3-4de1-acfc-92ce0ca34811&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=192&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

Every link in the breadcrumb is clickable, except the current page.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ec34a5e4-70d6-47c0-b311-a730f8804484&&collection=contentId-2832302192&height=33&occurrenceKey=null&width=245&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Touch Target & Layout

If the path is too long, it is possible to hide links and replace them with an ellipsis to save space and maintain clarity. This can be done in two ways: hide links in the middle of the path, allowing users to see the start and end points, or hide links at the beginning, giving priority to the most recent navigation steps.

| No hidden links | Hidden links in the middle | Hidden links in the beginning |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d5ca42df-65a8-4fd1-be43-199da1d9992d&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=557&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e721d6e5-cef5-4be6-8575-12b43520f503&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=528&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ada75036-30ee-43ed-90d7-900b2d405508&&collection=contentId-2832302192&height=22&occurrenceKey=null&width=531&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The default font size for the breadcrumbs is 16px. We recommend using the same size across the platform, but it can be adjusted if needed.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* Link texts should be clear and inciting. Our users should be able to anticipate where the links lead to.
* Use consistent language and terminology throughout the breadcrumbs to reinforce the structure of the site and help users become familiar with navigation patterns.
* Use short, concise phrases for each breadcrumb link to avoid overwhelming users. Aim for clarity and brevity to improve readability.
* For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
