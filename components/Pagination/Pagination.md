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
| ![](images/196ed2431b3a5bf3bd400b.png) **DO:** Use pagination to display large amounts of content, such as search results, reviews or lists. | ![](images/f50be3247cbc6d73042c46.png) **DON'T:** Don't use pagination for linear, step-by-step processes. Use the wizard instead. |

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
| ![](images/2b1e851c8ff9fcd8949849.png) | ![](images/884c2d7b74b2ae00df3157.png) | ![](images/abedd3ca94ed4fe9679eb6.png) | ![](images/e9d5ae953234621086a251.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![](images/52c846f6af2edd16b4e2a0.png) | ![](images/a3e62458d367983ec6cfbb.png) | ![](images/72f3b3c224ed30dbb7c39a.png) | ![](images/b2b7ebeda362166669611d.png) |

**Interaction:** To navigate to another page, users can either select a page number or use the chevron buttons to go to the next or previous page. When the first/last page is selected, the back/forward chevron is hidden.

| Go to next page | Go to previous page | Go to a specific page |
| --- | --- | --- |
| ![](images/ee79217af711ef1d851412.png) | ![](images/04799bcb0902db94babbd1.png) | ![](images/acfa9d8185da48ff1dc752.png) |

### Touch Target & Layout

**Truncation:** Pagination is truncated when a threshold number of pages (4 - 5) is reached. It truncates the pagination by displaying only the most important pages, such as the first, last and nearest pages, while using ellipses to indicate skipped pages. The truncation ellipse is not clickable.

| First page selected | Last page selected | Middle page selected |
| --- | --- | --- |
| ![](images/22d4fa1c40218ad6e9cd21.png) | ![](images/2f91db02d6c9a44a1d9f15.png) | ![](images/340517b9c3dcad3f836881.png) |

**Position:** Pagination is positioned at the bottom of the pageable content, allowing users to reach the end of the current page or section before deciding to navigate to the next. Pagination is centred in most cases, but can be left or right aligned depending on the layout.

![](images/196ed2431b3a5bf3bd400b.png)

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
