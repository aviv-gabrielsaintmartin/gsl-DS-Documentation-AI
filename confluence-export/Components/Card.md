<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831712331/Card | Last modified: Aug 17, 2026 -->

# Card

Cards are flexible containers used to visually group content.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=64e7d877-8ad9-4e4a-872c-d02a5be93de2&&collection=contentId-2831712331&height=750&occurrenceKey=null&width=2756&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Card on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7306)
* [Card on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-card--docs)

---

## Usage

Cards are used to group related content and actions into a visually distinct, cohesive container. They help structure information and provide an organized layout.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8d810c16-9a16-46d7-8c47-dc7101f882ce&&collection=contentId-2831712331&height=626&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use cards to encapsulate related content or actions that belong together. You can add text, actions, icons, illustrations and images within cards. Place elements in a way that creates a clear hierarchy and is easy to scan. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d130de5a-82d8-4ec4-9997-b59d19e9d5bc&&collection=contentId-2831712331&height=620&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Separate larger cards with a divider. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=69f5e94a-2044-45ca-b889-77337b1925bc&&collection=contentId-2831712331&height=626&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Create clickable cards by placing the cell content component inside the card. |

| DON'T |
| --- |
| **DON'T:** Don't use cards for selection. Use select cards instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Select card** | High | Use instead of Card when the container itself represents a selectable option | User needs to pick one or more options presented as cards |
| [**Cell content**](https://zeroheight.com/626199550/p/27116a-cell-content) | High | Place inside a Card to make the whole card clickable | Card acts as a clickable row or tile linking to another page |

---

## Variants & Modifiers

### Color

The card is available with 4 different background colors. Choose the color according to how much attention you want to draw to the card.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=639db333-ad91-4405-a2dd-990bd7133299&&collection=contentId-2831712331&height=992&occurrenceKey=null&width=812&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use different background colors to create visual hierarchy. |

### Radius

Cards are available with a radius of 4, 8 or 16px. Choose the radius according to the size of the card. The bigger the card, the bigger the radius should be.

### Padding

The card can be used with 8px padding or without padding. Choose the padding according to the content you want to put inside.

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f631b177-166f-4b82-bd21-bc8b90e1c0ab&&collection=contentId-2831712331&height=440&occurrenceKey=null&width=748&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the card with padding to separate content from the edge. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bbb6e550-ba34-450f-aa08-f0a9f6c1601c&&collection=contentId-2831712331&height=440&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When you wrap clickable cell contents inside cards, no padding is needed because the cell contents already contain padding. This makes the entire card clickable. |

### Slots

The content placeholder in the card is available with 1 to 5 slots. You can use the slots as a helper to structure the content inside.

---

## Behavior & Responsiveness

### Interaction

Cards themselves are not clickable. If you want to create clickable cards, place a [cell content](https://zeroheight.com/626199550/p/27116a-cell-content) inside the card.

### Interactive States & Loading

Not documented

### Touch Target & Layout

* **Width Adaptability:** The width and height of the card are determined by its contents, with the card adapting to the elements inside.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

For general content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/v/latest/p/324518-intro). If you are using cell content within a card, please see the [cell content guidelines](https://zeroheight.com/626199550/p/27116a-cell-content/t/page-27116a-84054092-25).

---

## Accessibility (a11y)

Not documented
