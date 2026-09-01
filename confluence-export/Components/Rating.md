<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831155311/Rating | Last modified: Aug 21, 2026 -->

# Rating

The rating is used to display the result of user ratings.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a3082dea341d&id=604735a7-a609-4cde-b760-6e975f29239e&&collection=contentId-2831155311&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Rating on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7313)
* [Rating on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-rating--docs)

---

## Usage

The rating is a non-interactive component used to display the results of user ratings and provide a quick overview of user satisfaction.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8344b37c754c&id=eda52e1b-ca85-4328-9eb0-878955eacd7e&&collection=contentId-2831155311&height=946&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the rating component to display results of user ratings. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=03c83443a50c&id=5e503d5b-a7b3-4977-aa44-f0f43277c8d8&&collection=contentId-2831155311&height=456&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Since it is not clickable, this component cannot be used to collect new ratings or feedback from users. This is done in an external tool called Opinion System. |

### Related Components

Not documented

---

## Variants & Modifiers

### Size

The rating is available in two different sizes. The choice of size depends on the layout and the desired prominence of the rating.

| L | S |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4266e00c03e8&id=7e75904e-f5df-467d-b3c2-95f875f4d985&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4761fe0ab5bd&id=81d69827-0552-4c6a-8663-8c5b5d12256e&&collection=contentId-2831155311&height=40&occurrenceKey=null&width=436&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

### Condensed display

The rating can be condensed to a single star or shown in full with all the stars. Which version you use depends on how much space is available in the layout.

| Full | Condensed |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=291b637d88f8&id=7e75904e-f5df-467d-b3c2-95f875f4d985&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=552&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c597919723a6&id=dba0bc4a-b7a2-44cc-b54d-e3a13eb1cd39&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=360&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=745c3c266141&id=8caccc5b-4018-4686-bfa3-d5e2d0246dd6&&collection=contentId-2831155311&height=600&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the condensed variant when space is limited. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b489a4334df4&id=57eac390-d033-4f16-9b53-1fef6bbd6fc0&&collection=contentId-2831155311&height=600&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the full version when enough space is available. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8c0420042064&id=91ba38ae-9f8e-46d5-bb6f-f0f8a568a28f&&collection=contentId-2831155311&height=600&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't hide the rating amount when using the condensed variant. |

### Modifiers

The following elements are optional and can be hidden: Number of ratings, user rating and maximum rating (e.g., "/5"). When hiding elements, make sure the context is still understandable.

| All elements | Hidden maximum amount of rating | Hidden rating | Hidden reviews | Hidden rating and reviews |
| --- | --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=417fa1dac215&id=a41912c5-7e24-4afe-b4fc-283af3746c99&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=584&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=d933ed37172a&id=6c237709-ea56-4da1-9a73-2bb6b7bbb90c&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=550&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=08718ac88a7d&id=488f1fdd-6035-4336-acbe-d4ff78fc1231&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=490&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7757da57bae0&id=b5b0b685-a474-45d7-b72e-0c76be63a4da&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=366&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=fa972bc7a7f2&id=56c6711f-57de-4dd9-b7ce-a7210f0e6e73&&collection=contentId-2831155311&height=48&occurrenceKey=null&width=272&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

This component has no interactive states. It is a static, display-only element with no hover, focus, pressed, loading, or disabled behavior.

### Touch Target & Layout

Not applicable. This component does not respond to touch or pointer interaction and has no minimum touch target requirement.

### Breakpoints & Platform Adaptations

Not applicable. This component does not adapt its layout or behavior across breakpoints or platforms.

---

## Content & UX Writing

### Scale

The stars are mathematically rounded.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a79949e4e8c7&id=7abf77db-5b73-43df-baf8-fb27dbfd6106&&collection=contentId-2831155311&height=688&occurrenceKey=null&width=382&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Rating results

The notation of the rating result depends on the language. For French, German, Spanish, and Dutch content, we write ratings using commas. In English, we write ratings with decimal points.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=cba6963ad488&id=f3e06923-b9b7-4665-8257-2ddb6572391b&&collection=contentId-2831155311&height=368&occurrenceKey=null&width=948&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Reviews

We use the following abbreviations for numbers.

**English:**

* **K** for thousands
* **M** for millions

**French:**

* **k** for "mille" (thousand)
* **M** for "million" (million)

**Dutch:**

* **K** for "duizend" (thousand)
* **M** for "miljoen" (million)

**German:**

* **Tsd.** for "Tausend" (thousand)
* **Mio.** for "Million" (million)

![](blob:https://media.staging.atl-paas.net/?type=file&localId=5747780c1a68&id=381a50c7-c690-40dd-b645-63feb771c2b2&&collection=contentId-2831155311&height=240&occurrenceKey=null&width=948&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
For more information on content guidelines, please refer to the [number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers).

---

## Accessibility (a11y)

Not documented
