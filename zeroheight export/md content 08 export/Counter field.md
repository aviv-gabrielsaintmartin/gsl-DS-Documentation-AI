# Counter field · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Counter field

Ready

Counter fields are used to enter or select a numeric values.

[

Guidelines

](/626199550/p/273135-counter-field/b/6320bc)

[

Web demo

](/626199550/p/273135-counter-field/b/56bbef)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/theZ5Og8R2pC8tFQLmvTwA.png)

-   [
    
    Counter field on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7278 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7278")
-   [
    
    Counter field on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-counterfield--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-counterfield--docs")

  

## Usage

Counter fields allow users to enter a numeric value or incrementally adjust a value with +/- buttons.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/8713257107d87169caf404?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=10b981a4341f03c1775b79dc798aeb4532c4b1f4cc848104dc96da7ec64cb38f)

Do

Use the counter field to allow users to enter or select numeric values.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/b09c260c3e0f41c758b223?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=75ffc85f20e619de4f14e48c26c283ec6514e811a366f0bfcd612b53bceccdc8)

Don’t

Don't use the counter field to select the apartment floors. Instead, use the floor selection component.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/6dda486bc6f305bc73ff28?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131536Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aae83528ffe91e8a60ac4360c6f2ae655b6554abff64163222a40160813750bc)

Don’t

Don't use the counter field for larger numbers. Use text fields instead.

  

  

### Related components

**Component**

**Usage**

Counter field

The counter field allows only numeric values. The component doesn't support letters or words.

[Floor selection](https://zeroheight.com/626199550/p/244373-floor-selection)

The floor selection component is used to select floors. The component contains "GF" (ground floor) as a word.

[Text field](https://zeroheight.com/626199550/p/980e7b-text-field)

Text fields allow all kinds of free-form content. They should be used for larger numbers such as prices, square meters, zip codes, or street numbers.

  

---

  

### Platform

Unlike other form components, we use the same counter field on all platforms.

  

---

  

## Variants

### Modifiers

#### Header

Like all form components, counter fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/101c3385210efedec8d0ad?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=73164800fd03e30898dfbc42ff852692193f67051bcbbcd2e5c7af4932399931)

Add notes

  

---

  

## Behaviors

### States

Counter fields have the states default, hover, active, and disabled. They don't have a pressed state. Instead, they change to the active state when a user presses on the field. When in error state, they contain an error message.

  

#### Neutral

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f34feb69ba6b757d513690?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21ddce900798f5804ffd91eb45745472b771e2715402383c064440629b97779f)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/be7e44a2c4dcd6052fdba1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=76614632eeab2d9379b3e444f297866a6e03fcd8e91965b066bd620ad2dd1fe8)

Hover

Add notes

![Active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f97cc8859bda2913e18b6d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d1b2498ff2748f81a682ecb79b4e3cd51e95822bf2b59a37cb694a824a335e05)

Active

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d21d21fe3a39f686879d11?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=753c31ae48e279d6bf877da72b4221ff8f1123e7d7288d84483f3b7f6a05c450)

Disabled

Add notes

  

#### Error

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b99d16a03f43b28c4faca3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=15887faea548028659b242520e75ecb623fb07e842ae34d2a5c65eabd47d6f0e)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/53b4716d7620f54a00d4cb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f6c0be5687ce1718c472ee8184445160ad32c81fd8ae9f37b3512973b0238310)

Hover

Add notes

![Active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9b782bbcdf4e19252c1310?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18df107777a14cd9ab23c650a4a88ebaf955fbcc5a133e22db1f2be79ad72001)

Active

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1b2b02424c39b6aaf8fafd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e99ef64b416c3d1c8c1122d19d8c51b3930a30101553540a01cb3f31fec1ed29)

Disabled

Add notes

  

#### Buttons

The +/- buttons have the states default, hover, pressed and disabled.

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f34feb69ba6b757d513690?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21ddce900798f5804ffd91eb45745472b771e2715402383c064440629b97779f)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7cdd2be2493e666706d40b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=76bdc805681e797811e1bbe8e2eb694ee561695195c97a33ed125e0813556a86)

Hover

Add notes

![Pressed](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1792ecdb6b6d58e68a8108?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b90cde602e6b740436bac4711dc646f747cf4cb60caea7f390a0dc6e9832ec70)

Pressed

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ac4b478fcc6dfccda7f5d1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=92392f8d879ab2a4e041e2a2d936db363a280145e7be0d55e7486f03db4a4b50)

Disabled

Add notes

---

  

### Interaction

Numbers can be entered into the counter field using the keyboard. It is not possible to enter letters in the counter field component.

Numbers can also be selected using the +/- buttons. Consumers can decide how many steps the counter will increase/decrease when the buttons are clicked (e.g. 0.5, 1, 5, 10 steps etc.).

The counter field allows positive and negative integer and decimal numbers. The default, maximum and minimum values can be defined by the consumer.

![Entering with keyboard](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c85339720628a9ec98aeb7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fd44c0e66795760204edc4f57e31b706b33f2c1b614d092aa943a25ccd13ceb4)

Entering with keyboard

Add notes

![Selecting with buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/671bdce186f531e25a4854?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86b57d3bc53b562cf138b772efd1f74120fa2981ee21db3d19d93d40e230b2b0)

Selecting with buttons

Add notes

---

  

### Width

The default size of the counter field is 144px. The width can also be set to 50% of the container, if two counter fields are in the same row. We don't recommend using the counter field at 100% (full-width).

According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/86306b09f8a92458eb05e2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20e339325e704265b2a358c04a944580918243fee1a6021e29c020f89745d2af)

Add notes

---

  

## Content

#### Digit

The counter field supports both positive and negative numbers. Decimal numbers are also supported.

  

#### Labels

Counter fields should always have a label, to help the user understand what information to enter.

-   Keep the label short and concise (1-3 words) and in noun form.
    
-   Start with a capital letter and use no punctuation (including colons).
    

  

#### Helper text (optional)

Add an helper text if the user needs assistance completing a field.

Use sentence-style capitalization and punctuation.

Helper text is an optional feature and can be used instead of a tooltip.

When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text in Android.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).