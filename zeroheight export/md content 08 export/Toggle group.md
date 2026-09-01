# Toggle group · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Toggle group

Ready

Toggle groups are used to organize related options, allowing users to switch between multiple settings, with each toggle independently controlling an on or off state.

[

Guidelines

](/626199550/p/51f970-toggle-group/b/67f040)

[

Web demo

](/626199550/p/51f970-toggle-group/b/5404a1)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** To Do

![](/uploads/jSIv4dliExAz9xxnc9HL0Q.png)

-   [
    
    Toggle group on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=11-60709&t=G4GRFXe9ksnNqcW5-11 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=11-60709&t=G4GRFXe9ksnNqcW5-11")
-   [
    
    Toggle group on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-togglegroup--docs "https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-togglegroup--docs")

  

## Usage

Toggle groups allow users to enable one or more options from a predefined set of choices. The preference should take effect immediately, without the need to submit or save the action. They are most often used for preferences and settings.

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/d2c96f848ec3af778748c1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133326Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9aa8d0f37397e006cc469632587dd8549ff73e2610be1b166c505ec1b73b916f)

Do

Use toggle groups in settings for binary choices, where the choice is applied immediately.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/ea2c658f02bc80106054a0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133326Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cddf07dad4a45c0237d9514be840194fe0fd81fa61632d3353566c9cb9e50fce)

Don’t

Don't use toggle groups when only one item can be selected. Use radio buttons instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/ee57fdcd9d9f3ef70d0fc5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133326Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67d21262493155a3bea7427a14ab4c56200fcb70acefa9a961fbf673d3e97155)

Caution

Avoid using toggle groups within forms. Toggles should take effect immediately, without submitting a form. Use checkboxes instead.

  

### Related components

**Component**

**Usage**

Toggle group

Toggle groups are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving.

[Checkbox group](https://zeroheight.com/626199550/p/41df87-checkbox-group)

Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect.

[Radio button group](https://zeroheight.com/626199550/p/55bfd7-radio-button-group)

Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect.

  

---

  

### Platform

As with standalone toggles, the group contains custom toggles on Web and native toggles on iOS and Android.

  

---

  

## Variants

### Modifiers

#### Toggle position

Like standalone toggles, toggle groups can also switch from a toggle left position to a toggle right position, depending on use case and layout.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/3d931fe720f0a3e4d0ba1d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133326Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a5a748ba32608be7d74e88b515dcff4203f52a65e0785d39fdf5b0cdf70c45a)

Do

All toggles in a toggle group should have the same position.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/309ba374f9c8c42f5ff723?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133326Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b21ee75d3ecc3a97d59d1b029e3a7dd4c68233ee2240359837e7b0e90599118d)

Don’t

Don't mix positions in the same toggle group.

---

  

#### Header

Like all form components, toggle groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

  

## Behavior

### States

Like the standalone toggle, groups have the states default, hover, pressed, and disabled. They can be selected or unselected, and they can be in an error state. When in error state, they contain an error message.

They also contain a loading state which is typically triggered when the action initiated upon click involves an API call or server query. To learn more about toggle loading go to the [toggle documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/4685c0-toggle/t/e5617ecdeb).

More information:

-   [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
    
-   [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)
    

  

---

  

### Interaction

Not only the toggle itself is clickable, but also the entire row. The row height is 48px.

---

  

### Width

The width of the toggle group component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

  

---

  

### Wrapping and alignment

Text that exceeds the available space is automatically wrapped to a new line. Toggle and content are centered.

---

  

## Content

#### **Toggle group**

Toggle group labels should:

-   Start with a capital letter
    
-   Not use commas or semicolons at the end of each line
    

####   

#### Toggle label

Always use clear and concise labels for toggles.

Labels appear to the right or left of toggles.

  

#### **Group labels (optional)**

In most cases, a group label precedes a set of toggle to provide further context or clarity.

A group label can either indicate the category of the grouping or describe the actions to be taken below it.

In some cases, a group of toggles may be within a larger group of components that already have a group label. In this case, no additional group label is required for the toggle component itself.

  

#### Helper text (optional)

Add an helper text below the label to provide additional context and help the user make a decision.

  

### Overflow content

We recommend that toggle labels are less than a few words words. Don't use an ellipsis to cut off the text of a toggle label. If necessary, use 2 lines.

Make sure that the text under the toggle wraps to the next line, and that the toggle and its label are aligned at the centre.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).