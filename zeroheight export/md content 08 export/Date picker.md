# Date picker · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

PATTERNS

# Date picker

Ready

Date pickers are used to select a date using text input or a calendar view.

[

Guidelines

](/626199550/p/33c9e4-date-picker/b/25dcae)

[

Web demo

](/626199550/p/33c9e4-date-picker/b/02748e)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** To Do

![](/uploads/FKfcnOkggnHBX0X7-atNMA.png)

-   [
    
    Date picker on Figma
    
    
    
    
    
    ](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7270 "https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7270")
-   [
    
    Date picker on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-datepicker--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-datepicker--docs")

  

## Usage

Date pickers allow users to select a date from a calendar or manually enter a date in the input field. They can enter dates from the recent past, present, or future, with each date including the day, month, and year (dd/mm/yyyy).

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2df569a9fbe45f7d5d6cef?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131603Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=73d3020a80b45d848d6c50f93c72f86caebd638d0349dbc98a42ba7abb64ab46)

Do

Use the date picker to allow users to select a specific day in the past, present or future.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/57265643348707e8a6597e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131603Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e27e39534bc202a9a1c3812d8ba6184d1cd22053b62dfd12cfc53583812ec8cb)

Don’t

Don't use the date picker when users need to select a specific year. Instead, provide a text field where they can enter the year directly.

The date picker doesn't currently support range selection.

  

### Related components

**Component**

**Usage**

Date picker

Date pickers are used to select or enter specific dates in the past, present or future.

[Text field](https://zeroheight.com/626199550/p/980e7b-text-field)

Text fields allow short single-line and free-form content. They can be used to enter years.

---

  

### Platform

We use platform-specific date pickers that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders in the date field and the appearance of the calendar view.

  

#### Web

On the web, the label is always at the top of the date field. The placeholder is visible until a date is selected. On the web, we use a custom calendar.

![Date field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0b6371231f00c4a31b1523?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e32db9eeeb31ec6b362c72c6d57015133bcefa729f45137710fcd2f5fecb4e9e)

Date field

Add notes

![Date picker](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/41e99931d035072536c296?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20274de084197ea5f2f6a579002d39b53fe75c0f091520064f553cff04467815)

Date picker

Add notes

#### iOS

As on the web, the label is always at the top of the field on iOS. The placeholder is visible until a date is selected. On iOS we use the native calendar. On iOS, it's currently only possible to select the date using the calendar. It's not possible to type it directly into the field.

![Date field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0b6371231f00c4a31b1523?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e32db9eeeb31ec6b362c72c6d57015133bcefa729f45137710fcd2f5fecb4e9e)

Date field

Add notes

![Date picker](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/997d23aab38ab10b66f1d9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=be976db4531c513ce0850c4f1cd3226edc0da11ad0decae27cca96774d61ffc5)

Date picker

Add notes

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. Instead of a placeholder, the date format is displayed with the helper text. On Android we use the native calendar.

![Date field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c370c0935f348501b14f0d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ebd25b43e522cb2bce3ca08658e43dbbf909765732f33caa515cde8cca3304d9)

Date field

Add notes

![Date picker](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2ed53a399b7c6db55f9f05?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93e1c047740e60e5fa082aafaf17da2387afe8d54205b2bea03ffc403791e99a)

Date picker

Add notes

---

  

## Variants

### Modifiers

#### Header

Like all form components, date pickers contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3916d6ebb9fe3a3c2622d9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4c2216f1cbaa77d144896820825d669ffc69d0361530cda4ded99fa9a0635668)

Add notes

---

  

## Behaviors

### States

**Date field**

Like text fields, date fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, they change to the active state when a user presses on the date field.

The icon button in the field has the states default, hover, pressed and disabled.

  

**Neutral**

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2f8553b55fa2b9ff1e7e1e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6c485428a7a1333c4796b0a1a4384c1fd00f34edebd34793561ad0a5837488c4)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fa0efc3330e0e7bc65325b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=30cc68bfc15ae6aacd1808781aa5637a45e4a6a77d7a0894dedbb54c80527d82)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e0b953017ba760895f35a7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cccf90016de9b32e91f3411b25df869741a8b8707e33b060469db13251c1e000)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/65c7e4677e9d361686e6c7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ac03fb75c8d8262e0966f23de6b6b82d55ab70b208cc4fc0d8b38504c3080fe)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7d114f04de1d4e5b4e1edb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ab5a51e01b61b933b7392a4b02e8f18cb582a6d8ba583360d10d3ad943556875)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/80d71c8f10dd7b5c5b6641?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8c2468c4bb4442e9021686308b2f5257d4f87941c67de2545c6536c14e21ad3)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7e7d5d7b349759c23fc72c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1b71494854440d286b37ca5f0d0ec362d385007e7bc955565c92c711d01ecae1)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/17bd845737801a9343c028?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=84c0919ffed717f7f4617c471cd00cf2be25942aa174de5fda7bedbb5dbf6c6e)

Disabled filled

Add notes

  

**Error**

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/65523a7512bc7390071d53?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9e4bdaedf23e869873dc657f51875f478cd4426fb9b951c4ca4683077ba50218)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/754847e0256357e0074999?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47273b9ed498e08045be80ce6102a674ff41c3b744b231fb9d4256627a7ad79b)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/05c317e0086c7bacde6e72?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=618c571ba686dd02c8d9ead465b0f1766fc99ff1ab41579a5314bf347fc09fdc)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/707076edc3d03adfc8c58a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22ce31d49df3a5d8da1acca54fe05f8e28c3d3e59e6c37bc091c4af168635eaa)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a49a3c5ff0fbb65ad6760f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=23840b313de5077592c18ceae41643b26b89bdf59198e7c3bb281b2bc0bc22cb)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7ec98bb20bf04ee666fd3e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=326d029ad77be12a7ebd54d5d38608ed36003984f4f1adbda1be145fd0ed888c)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7739c2f524b4c9ebc54ba0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b5d0c3f2c578110cb602f29fb3bf8e4cf866b510d81d44addae66df23aefaa46)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f59c7ea81a21f8974157d1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=38004fb23349377535d5cabe09f00492cb74dedd45ebdb23e0c0dda17923b737)

Disabled filled

Add notes

  

**Date picker**

The buttons in the date picker have the states default, hover, pressed and disabled. They can be selected or unselected.

  

**Day**

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/104e9d17339dcba67cbcee?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a57fd503ede22ee44e5e4107421cb549af6ccfb8af6206742f1c648166853401)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1b100120c17b17daf7b584?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8bf9154e84d31a882a390f6f4eeb71e791141c7aa6096a7c7e6fecbedd0f38d1)

Hover

Add notes

![Pressed](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6891ed71dfbb0a355ca82e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1806932031ea0ab92865776b6b3b56421c0ae2cdccfa81bd802f8b6e6e0e2523)

Pressed

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f700330535590a6ad9c8f0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=815fe03662b46ce5426b31c790cd7d07429eaeda058f23be4f935d8c210ea36d)

Disabled

Add notes

![Default selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f757ca2611e44665b4b661?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=df4ee9c0982c2933d138cb50115f5c660c5502a11f0099fa94b5eace964f79f8)

Default selected

Add notes

![Hover selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3011650a1037a828d2b27a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6062897ea244d085e20d7dd1df6bb8c81cd0bd62d0a1588ce0a7572fb17e21c7)

Hover selected

Add notes

![Pressed selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/96c227666f990d071285a1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9bc0f499084fad4bafc3bc08df1300dcabf34127263a71e9993665d111761806)

Pressed selected

Add notes

![Disabled selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cb51e5470d2ee6a4a51353?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e6aa246bf19d3972e2d2b1746aff2b4cdbec239201bb1eb8c483ef82c2431147)

Disabled selected

Add notes

  

**Month/Year**

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/697b5a9d5738d1a1a94d99?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fcf25c7ae1ffc5efe72b9e0be79fbc15c877e94b34a7717622f24bd148b507aa)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a2096d12f0f4821c6e4db6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=860a055fbeb770f97dce237e1d7a77067420962f6ad31d5f29a47cf4054df3c6)

Hover

Add notes

![Pressed](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2bc26fcaf12b1aa1639b6a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=58e9b53729d46cedb460c5b1e9e041a61bae46f9ac38d2c8401ccbf5105aefa1)

Pressed

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cf5674f586f62ae349c5d6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8acfc1bfeac652b749199db46c0df617cc4ae584d23858aadb05c942a845a494)

Disabled

Add notes

![Default selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/680c40889990b2b7524cc0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fc38697710d8792626ed32d8e69b9ce602f8831ee21404609b20429b4f8aa5ab)

Default selected

Add notes

![Hover selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4edda695874eec1141794c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d7a70443355a96f1b893fae6b8ae481ffcec45b9e59890d192ff0ed5ccde3bc9)

Hover selected

Add notes

![Pressed selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/94a16eb986e42496d39772?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e465beaaf4162e7ba4a1cbe6f9b88911ed6deb55324904006f907edcfbde307a)

Pressed selected

Add notes

![Disabled selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2ec2cbc86ebe750a60a891?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d6567c0bee21de26eda26463cca31adc8645a62080d1178a998977e33fbaf110)

Disabled selected

Add notes

  

**Current day**

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e0161856af54c89e741f2f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=51f1d1661e393357267173b9aaefa8edaefa71504202ace357b24188b902496a)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e5ab617227c0611d3f7019?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=167a97dd7994c5b953d6dc64a0eb8cde1b59297b674d75f40a0840afb7b72bd5)

Hover

Add notes

![Pressed](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/583da771712d0f480f3f41?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=31b8fcc2549cbb726613ffa730d1203a87a981f1a46029c69ba2050e99911bc8)

Pressed

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b1f8463fe4828b6f430065?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5e6755b3bb989737a9fd676b7284d4fb4a68cf8246e81864065ac98f216387b8)

Disabled

Add notes

![Default selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/326889608a9fde0edeb53e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6012b91ab2c6363ac5db4946a55886bc77d97a457bf12f443610077e3b0f1e4e)

Default selected

Add notes

![Hover selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a294290e6a1dbc56085c24?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a69720bb42aee8d7d6ecb3aa5e94ca6d7a25c677c59249fef9b0d1e0f847ed2f)

Hover selected

Add notes

![Pressed selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ba4e2e38e0434c7faeb9c1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8974eb67eee0b8ba957d15d439a43c047b6bac90c543f25165c5120cbf0d8463)

Pressed selected

Add notes

![Disabled selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/31e16c3227775c7690130d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1981fd1df0a60569252d31361bda49ac583e4db7e0749e1d4021ab5adf824400)

Disabled selected

Add notes

  

---

### Date field interaction

#### Typing

The user can select a date by typing it into the date field. On the Web, we use a placeholder with progressive disclosure to help them understand the required format.

![Day](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c1946a57481ae00e7f9b56?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4cb96858f37cb3973cbed4bf4013da59001c9d1e84139d6983aa1968ca444d47)

Day

Add notes

![Month](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/522c6d2697032ae52e9c4a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=04f13e041463ca71d2a390289a631463383a4def8d479e0a2d955dc9eca8ea55)

Month

Add notes

![Year](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fb97b488cfb254b420af3e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d65478507ec251eab6726ca3f411d5f11b6418a92d76258109ae2df11807a45)

Year

Add notes

#### Clearing

Web only. Clearing on other platforms is done in the Date Picker.

The user can clear the date when the field is filled by clicking on the "clear" icon on the right. This button is optional.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4e8dd7051eecf627b72a90?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=89b49249a929065137cb3150991ce2cc92cceb7258a775d31c9f3ec2f924d82d)

Add notes

---

  

### Calendar interaction

#### Opening and closing

**Modal view**

The calendar opens when the user clicks the Calendar button. It closes when the user clicks the button again, clicks the Okay or Cancel button, clicks outside the calendar, or presses the Esc key.

To select a date, the user must click a day and then press the Okay button.

![Opening and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4b430718c1ddd43927b018?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=db339ffad1302c5c6c5ba27e611f6609c9353d43647bf563f9fd4d383461a249)

Opening and closing

Add notes

Clicking on the calendar button

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3f04b522020e19557b6d6d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5824cb02ec5f82a4ec8a713287af365a1e8c016e1af9d6cb53730d908cc2083b)

Selecting and closing

Add notes

Clicking a date and the okay button to select a date. Or clicking on the cancel button to close the calendar.

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3cb52a3f3f8d54cbcfabaf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c2124ab04965d0619030e37834eed2dbcd0796a1082a6b6b9f7ea5868cfd0d69)

Closing

Add notes

Clicking outside the calendar or pressing esc

  

**Dropdown view**

The calendar opens when the user clicks on the calendar button. It closes when the user clicks on the button again, selects a day, clicks outside the calendar or presses the esc key.

To select a date, the user simply has to click on a day. The buttons are not needed in the dropdown view.

![Opening and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/326130bb616034ac3dbd7a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4b2ec6718ac4e340103f8259dbeea72c970ff0d7b3dff7c456f48e598ce52abb)

Opening and closing

Add notes

Clicking on the calendar button

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0a051c5bb4f6d1b1d0eee1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d5c1469d3c66d5ec7d2b8212b2038ab7b5e33d0926038cab4cc4f9015441f2ac)

Selecting and closing

Add notes

Clicking an option

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/930f79ec089673dd7b73aa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7cc57933d80a0ec1f66bae6d7514575144b82b685b6decaa5981e80e5addd6e2)

Closing

Add notes

Clicking outside the calendar or pressing the Esc key

---

  

#### Changing months and year

Users can change the month and year by pressing the corresponding button and selecting an option from the dropdown list. In addition, they can change the month using the chevron buttons.

In the dropdown view, the user must change the month and year before selecting a day because the calendar closes when the day is selected. In the modal view, this is not relevant because the calendar only closes when the user presses a button.

![Calendar](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/24a120504f0fdb2a12883c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=807e086c66d720f199e46f47c4c3e056b0bec9e680a65cede224020787af5a39)

Calendar

Add notes

![Month selection](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f83ceaa8888c58e6a6f0ac?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d6e369acaf2a6f9453d58a700817842ecf95a944c8f3eae27c2c567b32465)

Month selection

Add notes

![Year selection](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/00cc17d886b8654fd53a03?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f1201db3a51e10ca3c9d2dd40fb392f5223a4c7f3fcebc684bad5bd20e1cb817)

Year selection

Add notes

The month and year selection looks slightly different in the native iOS and Android picker. The native variants for this are currently not available in Figma.

On the web, we currently still use the native browser dropdowns for the month and year selection. This will be fixed and aligned with Figma in the future.

---

  

#### Clearing

The user can clear the date when the field is filled by clicking on the "clear" button in the datepicker. This button is optional.

![Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fe441943cd0f27090d2180?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d18ed9536a3e0c1c83e24ec5719ef2b587cb1d02bac5873787bfad53f09bc0e3)

Android

Add notes

![iOS](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/68c92743667a90941bc2fb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d8557690a38893b2b4eee96b42e15bd368cbe4591cb233495edd153a28ac765a)

iOS

Add notes

  

---

  

### Position and scrolling

**Modal view**

The modal calendar is centered vertically in the middle of the screen.

![Centered](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3ee42d07d88ceb05c14c67?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86512c69932989e152d51534864788aeecfdce66d2a4a4de5c2785e683110837)

Centered

Add notes

  

**Dropdown view**

By default, the calendar is positioned below the field. If there is not enough space below it, it is positioned on top of the field. If there are more options than space available, the calendar becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings.

![Below the field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f1a69c2096aaa0873348b0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=12eabed947cb73978163e6cc0e3effc0cd117bfeda3e56325ec549d8d688d50a)

Below the field

Add notes

![On top of the field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b3baedef4b896e78f84a26?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f0f1f562387763b80173e6576d7b1d8d9bcea2035df50c76754f2a889cce40d5)

On top of the field

Add notes

![Scrolling](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ba2ab9cff8c4c5a11f2ce3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7af63d96e1769ca970276567849760ff2d186acad1e20348dee95e8ce0af4260)

Scrolling

Add notes

---

  

### Breakpoints and width

#### Date field width

The width of the date fields can be set to 100% (full-width) or 50% of the container. It's also possible to set it to a fixed size.

According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f9bb53f523b1d783c6ef3d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d5f6f174ee433e5fd6b80def9be174899def73100760ed921a00d6a4bc1c9837)

Add notes

  

#### Calendar width and breakpoints

The appearance of the date picker changes depending on the platform and breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

In the modal view, which is used on mobile web and apps, the calendar is full-width (minus 16px margin).

In the dropdown view, which is used on desktop, the calendar has a fixed width that can't be changed. The width depends on the brand and language. For example, in the aviv brand, in English, it has a width of 330px.

![Modal](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3ee42d07d88ceb05c14c67?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86512c69932989e152d51534864788aeecfdce66d2a4a4de5c2785e683110837)

Modal

Add notes

App and mobile web (Breakpoint: XXS - XS (0 - 599 px))

![Dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/807ee32a14005536773746?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cf73f831d8ae420403ba9fc679df5d69893421507877899f4aac179dc8843c80)

Dropdown

Add notes

Web only (Breakpoint: SM - XXXL (> 599 px))

---

  

## Content

For English, French, German, Spanish and Dutch content, we use slashes and write the date as: dd/mm/yyyy

For more information please refer to the [Number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers)