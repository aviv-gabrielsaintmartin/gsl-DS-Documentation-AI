<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830991442/Select+card+group | Last modified: Aug 21, 2026 -->

# Select card group

Select cards are used for single- or multi-selection inside forms.

![](images/jSIv4dliExAz9xxnc9HL0Q.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Not documented | Ready ✅ | Ready ✅ | Partially developed |

* [Select card group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7282)
* [Select card group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-selectcardgroup--docs)

---

## Usage

Select card groups are collections of cards organized together to allow users to choose between related options. They provide a visually engaging alternative to traditional radio buttons or checkboxes. They support single- and multi-select and include icons, illustrations and descriptions.

### Platform

Select cards contain custom checkboxes on Web/iOS and native checkboxes on Android.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/842d0178eda49810307333.png) **DO:** Use select cards to display more visual engaging choices, that are enhanced with icons, illustrations and descriptions. | ![](images/4669b8f4755e09945dbafa.png) **DON'T:** Don't use select cards when you need to display more than 6 options, or when there is limited space available. Use radio and checkbox groups instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **[Radio button group](https://zeroheight.com/626199550/p/55bfd7-radio-button-group)** | Not documented | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. | Not documented |
| **[Checkbox group](https://zeroheight.com/626199550/p/41df87-checkbox-group)** | Not documented | Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. | Not documented |
| **[Button cards](https://zeroheight.com/626199550/p/093ea0-button-card)** | Not documented | Button cards are navigational elements. | Not documented |

---

## Variants & Modifiers

### Group

Select cards are available as a group or individual select cards.

### Type

Select cards are available as single or multi-selection component. The multi-selection variant contains a checkbox, the single-selection one doesn't contain an indicator.

### Alignment

The content inside select cards can be in a vertical or horizontal alignment, depending on the use case and layout structure.

### Modifiers

#### Icons and illustration

Select cards contain optional icons and illustrations. The illustrations are available in the size 40 and 64px. If you use an illustration we recommend the usage of pictograms.

#### Title and description

The select cards contain a mandatory title and an optional description, that can be added to provide additional explanations.

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Select cards support default, hover, and pressed states, and can be selected or unselected.
* **Disabled State Guidance:** Select cards support a disabled state and an error state; not documented further.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* The title is mandatory, the description is optional. Both title and description can be multi-line.
* The **title** helps to structure the content. It's concise and has no punctuation.
* If you need to give additional guidance to the user, use the **description**.
* For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
