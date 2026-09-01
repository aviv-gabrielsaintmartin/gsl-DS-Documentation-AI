# Text field · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Text field

Ready

Text fields are used to enter and edit single-line text content.

[

Guidelines

](/626199550/p/980e7b-text-field/b/36736e)

[

Web demo

](/626199550/p/980e7b-text-field/b/33419c)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/QZHTpDq_y6-HIPdqRyoDDw.png)

-   [
    
    Text field on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7284 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7284")
-   [
    
    Text field on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textfield--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textfield--docs")

  

## Usage

Text fields allow users to input and edit short free-form content. They are commonly used in forms for purposes such as contact and property information, login, registration and search queries.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/5e6555cc253b965b20274f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ec2c4a69c6230769a0a8b7e3b9a8132f778cc4e4bf3ba4d0bff7bd1fb5679701)

Do

Use text fields for short single-line content such as name and address.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/532d40c146b56f14b4f452?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1f34c4238fde26f20eb71ec26633b18e7fcf4378edf05047b9ad598a3ee7c2a8)

Don’t

Don't use text fields for large amounts of content that exceed one line. Use the text areas instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/a46349c76e41f79c3709b6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=78aea86f46b14b2fd3ba60087a6e76da2260081b90112239656ca00072560ea8)

Don’t

Don't use text fields for phone numbers. Use the phone number field instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/b4ed32640a65f8edf46ae7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8cce1b7f9069afb219fefd7136a34b1a6a811c29aa7b3f9585e7eaa90b31849c)

Don’t

Don't use text fields for date selection. Use the date field instead.

  

### Related components

**Component**

**Usage**

Text field

Text fields allow short single-line and free-form content.

[Text area](https://zeroheight.com/626199550/p/438e9d-text-area)

Text areas allow multi-line text content.

[Phone number field](https://zeroheight.com/626199550/p/490309-phone-number-input)

Phone number fields are only used to input phone numbers.

[Date field](https://zeroheight.com/626199550/p/33c9e4-date-picker)

Date fields are only used to input dates.

  

---

  

### Platform

We use platform-specific text fields that differ between Web/iOS and Android. The main difference is the behavior of labels and placeholders.

  

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled.

  

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

  

---

  

## Variants

### Modifiers

#### Header

Like all form components, text fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

Text fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

---

  

#### State message

State messages can be used to provide additional information or feedback on the usage of the text field.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

More information:

-   [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
    
-   [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)
    

  

---

  

#### Icons

Icons can be added as visual cues to provide clarity to the user. Icons on the left are non-clickable. Icons on the right can be clickable (icon button) or non-clickable.

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/9ccbb65f3b8055de7c7b07?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67bc318b50efde117c32dc480a90fa635074013f6b202bba3239abb1d5dd948b)

Do

Use non-clickable icons to provide visual cues to the user.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/9c21161133b43f8fcd551b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7178c83cc6b9bba081d826ac2ef7d89219ae0a139c9935dfcf159cd488ad2df8)

Do

Use clickable icon buttons for actions related to the text field, such as deleting the contents of the box.

  

---

  

#### Suffix

The suffix can be added to provide additional context or constraints for the user input.

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/46d805924cd0030440a441?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133251Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6f4c150e47b548e77996207220ba610131fe0d4becf82e5b3cfceb214fbd59ac)

Do

Use the suffix for measurements, currency, or contextual information.

---

  

## Behaviors

### States

Text fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, they change to the active state when a user presses on the text field.

  

#### Neutral

  

#### Error

###   

---

  

### Width

The width can be set to 100% (full-width) or 50% of the container. For special use cases it is also possible to define a fixed size.

According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

---

  

## Content

### Main elements

#### Labels

Text fields should always have a label, to help the user understand what information to enter.

-   Keep the label short and concise (1-3 words) and in noun form.
    
-   Start with a capital letter and use no punctuation (including colons).
    

  

#### Helper text (optional)

Add an helper text if the user needs assistance completing a field, such as explaining the correct data format.

Use sentence-style capitalization and punctuation.

Helper text is an optional feature and can be used instead of a tooltip.

When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text in apps.

  

#### Placeholder text

Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.

  

**Placeholder text - numbers**

When designing a text field that will contains numbers (price, size, etc.) please make sure you use numbers or leave the text field empty. For example a text field for minimum price to maximum price should say 0 € , allowing the user to type in a number if they wish.

See the [Number Guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers) to learn more about the rules for designing with number-related text.

  

### Overflow content

If a user's content is too long for the single line of text input, the value content can scroll horizontally within the field container as the cursor moves from one end of the value to the other.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).