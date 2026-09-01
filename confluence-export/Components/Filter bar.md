<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832695387/Filter+bar | Last modified: Aug 21, 2026 -->

# Filter bar

Filter bars are used to narrow down search results or displayed content based on selected criteria.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a40552ed0621&id=4b7c6178-e749-48bf-96c3-c55add521c39&&collection=contentId-2832695387&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | N/A | N/A | N/A |

Figma only (owned by SERP team).

* [Filter bar on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?m=auto&node-id=2240-119052&t=44YLeVrnPbcXxr0R-1)

---

## Usage

The filter bar allows users to set criteria to narrow down displayed content on a search results page or in a table. It consists of filter buttons that refine the results based on the user's selected criteria.

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

### Size

The filter bar is available with a height of 40 and 48px.

| 40px | 48px |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=cb07df19b5b2&id=f299e7b7-8487-4c20-9a4f-4f1ab25ba1cd&&collection=contentId-2832695387&height=36&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=407430c49c9c&id=ce7532ea-a28a-4cce-875d-9e431ec29f4b&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Filter button types

There are three types of filter buttons, each offering a different user interaction:

| Opens Modal | Opens dropdown | Boolean |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=ff9769fc44ff&id=ed65406c-10fe-4669-8b0d-3d956cc3ad43&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=96&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0f2c0316e24a&id=69aa3713-8203-4082-a1d2-371c4a9d8d77&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c5aba15ccf6d&id=f63e5dd2-00ec-454b-b4e9-909d4b0fd06e&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=67&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Opens Modal:** When the user clicks this filter button, a modal with multiple filtering options is displayed.

**Opens dropdown:** When the user clicks this filter button, a dropdown panel appears, allowing the user to select and apply filters.

**Boolean:** When the user clicks this filter button, the content is automatically filtered based on the criteria specified on the button.

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=606be7290aee&id=fc6f3ed3-796b-4ea8-9f24-84cdc964a9ac&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Try not to mix alternating boolean filter buttons with dropdown filter buttons, as this can cause confusion. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=51a40ca53d5e&id=72a6e2e1-62cc-4fbd-a15f-be08a6821f19&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Try not to mix alternating boolean filter buttons with open modal filter buttons, as this may cause confusion. |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=5e49bc97324b&id=5da68a6f-b033-49e2-8bde-22237430a4d9&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Place all of the dropdown filter buttons together. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=33f6170d8f38&id=fd641d2c-c86d-4188-8ae5-3731db3dc5fb&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Place all boolean filter buttons together, even if they exist next to another type of filter button. |

#### Filter number counter

Optionally an open modal filter button can display a counter with the number of filters applied.

* In the filter bar, in the filter button clicked on step 1, the badge is shown with the amount of filters selected.
* In the filter bar, in the "More" button, the badge is shown with the total amount of filters selected in all the filters.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=243b58bc46b7&id=f663f2b8-9496-42c1-82b6-ae1cd1352bdd&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=126&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Modifiers

#### Show/hide filters button (desktop only)

All the filters button can be shown or hidden.

| All filters visible | Hidden filters |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=879b7c26883e&id=1ff4bedd-0d92-49e6-b528-a1d50db1656f&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=d5e9ef9bf1ab&id=cc7758e6-1970-4ea9-bf04-6e9029ec02b6&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Show/hide primary button

Since the primary button is not a validation button, it is optional and can be hidden.

| With primary button | Without primary button |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=e3d560de8387&id=1ff4bedd-0d92-49e6-b528-a1d50db1656f&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8f31e83bf9c0&id=780833ce-7d6f-44d9-808f-3fad3a756a33&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

When the user clicks on a filter button, either a dropdown or a modal opens. The dropdown/modal closes when the user clicks outside or on a submit button.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=7dd9a09ff077&id=eb99c98a-87d2-40b7-a131-044a21ba5167&&collection=contentId-2832695387&height=131&occurrenceKey=null&width=305&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
In Figma, you can add any type of component inside the dropdown panel by swapping the .Slot instance inside the filter dropdown container.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=ba35f1855844&id=e2b10726-fa72-46a0-a361-8a3349e5c77d&&collection=contentId-2832695387&height=698&occurrenceKey=null&width=1242&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
The modal bottom sheet is a separate component that can be combined with the filter bar.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=22eda49a4593&id=df6ac2c0-c095-4646-a090-ff298560f847&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When using the dropdown panel, align it to the right or left edge of the filter button. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=6b1ae36920f4&id=9490b1ae-6432-46d4-8193-99932f2fb49e&&collection=contentId-2832695387&height=355&occurrenceKey=null&width=545&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** It's possible to combine the filter bar with a modal, but it should be checked how it affects usability. For a seamless flow, the dropdown panel is often the better choice. |

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

The appearance of the filter bar changes depending on the breakpoint. To learn more about our breakpoints, see our grids and breakpoints guidelines.

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Desktop** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=e6922aa9bc71&id=ce7532ea-a28a-4cce-875d-9e431ec29f4b&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=835&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XL - XXXL (> 1279 px) |
| **Tablet** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f8a2c582cc4b&id=e6307744-16fd-45ad-afdc-23426f141821&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=680&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: SM - LG (600 - 1279 px) |
| **Mobile 1** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=01b4b75dd111&id=613742ee-928c-4103-8999-803b9a1b7fa7&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) |
| **Mobile 2** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=991c14007ec7&id=8f9f532e-97f3-4770-a882-1c0f81140b53&&collection=contentId-2832695387&height=44&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Web: XXS - XS (0 - 599 px) |

We don't recommend stretching the filter bar over the entire width on desktop as this can cause usability issues.

---

## Content & UX Writing

Filter buttons should be clear and concise. Our users should be able to anticipate what will happen when they click the button. Use consistent terminology and structure across all filters. If one label reads "Price Range," another should not read "Select Area," but rather "Location."

* Use sentence case without punctuation.
* Try to keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
