# Toggle · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Toggle

Ready

Toggles are used to switch between on and off states.

[

Guidelines

](/626199550/p/4685c0-toggle/b/851f00)

[

Web demo

](/626199550/p/4685c0-toggle/b/514bbe)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/gvq4xxgMMGqLso7a0Yy7WA.png)

-   [
    
    Toggle on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7286&t=cY0FVB8lofjw9Zwd-11 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7286&t=cY0FVB8lofjw9Zwd-11")
-   [
    
    Toggle on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-toggle--docs "https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-toggle--docs")

  

## Usage

The toggle component is a component that allows users to switch between two states: on and off. It is commonly used when a user needs to enable or disable a feature or option.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/92e1082ee2270b02819095?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133306Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7dcf05e757477031b4b50f101d51fb2af7ef5942daa6bde5e95b7212675d44ac)

Do

Use toggles for binary on/off choices, where the selection is applied immediately.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c06701d4502d99c2f300b3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133306Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4487816f55d6bd3fc5712fd6399f1ea27dd0b2f47169f31807917f99f65efcc3)

Caution

Avoid using toggle inside forms. Toggles should take effect immediately, without having to submit a form. Use checkboxes instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/58e71b838bbd28d5ac26b4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133306Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a10f59533117ca11c24de8017b3459e44273f1d7c7051ce02e609b4dc0b5bd8)

Caution

When you want use toggles in a list, consider using the toggle group component.

  

### Related components

**Component**

**Usage**

Toggle

Toggles are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving.

[Checkbox](https://zeroheight.com/626199550/p/3044f1-checkbox)

Checkboxes allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect.

[Radio button](https://zeroheight.com/626199550/p/55bfd7-radio-button-group)

Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect.

  

---

  

### Platform

On the web, we use custom toggles. On Android and iOS, we use native toggles.

  

---

  

## Variants

### Toggle position

Toggle can be position on the left or on the right depending on the use case.

---

  

### Modifiers

Toggles have the same elements as all form components:

-   Required asterisk to the right of the label (visible by default)
    
-   Optional mention to the right of the label
    
-   Tooltip to the right of the toggle label
    

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

  

  

---

  

## Behavior

### States

Toggles have the states default, hover, pressed, and disabled. They can be selected or unselected. Unlike [checkboxes](https://zeroheight.com/626199550/p/3044f1-checkbox) or [radio buttons](https://zeroheight.com/626199550/p/55bfd7-radio-button-group), they don't have a red border indicating and error state, but they have an error message.

  

#### Neutral

  

#### Error

  

#### Loading

This state is typically triggered when the action initiated upon click involves an API call or server query. This provides the user with a visual indication that their action is being processed.

During this waiting period, a loader will be shown in place of the toggle. If the loading process fails, a snackbar can be utilized to display the error message.

To avoid a flashing effect, the loader will be displayed for a minimum of 600 milliseconds.

  

  

---

  

### Interaction

Not only the toggle itself is clickable, but also the entire row. The row height is 48px.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5cd74b4fd31c14661bf3f2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0a47f117ce22ad9a0eb16191ab8ff0412106919ec0d480441504ea0acd094eae)

Add notes

---

  

### Width

The width of the toggle component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

  

---

  

## Content

#### **Toggle lists**

Lists that use toggles should:

-   Start with an uppercase letter
    
      
    

#### **Toggle labels**

Always use clear and concise labels for toggles.

Labels appear to the right or left of the toggle.

  

### Overflow content

We recommend that toggle labels be less than 3 words. Don't use an ellipsis to cut off the text of a toggle label. If necessary, use 2 lines.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).