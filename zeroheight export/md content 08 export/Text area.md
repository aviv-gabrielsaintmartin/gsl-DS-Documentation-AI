# Text area · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Text area

Ready

Text areas are used to enter and edit multi-line text content.

[

Guidelines

](/626199550/p/438e9d-text-area/b/812dee)

[

Web demo

](/626199550/p/438e9d-text-area/b/024f77)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/Wui_hPh43PH8foRvC0PW4w.png)

-   [
    
    Text area on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7285 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7285")
-   [
    
    Text area on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textarea--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textarea--docs")

  

## Usage

Text areas are used for entering and editing larger amounts of text compared to single-line [text fields](https://zeroheight.com/626199550/p/980e7b-text-field). They are commonly used in forms for purposes such as entering descriptions, comments, and messages.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/95d51eab3636afd009f992?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133232Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0531c87246c45916d6691ac3c4509b880d565eafc020d1d1325df57204a11e74)

Do

Use text areas for multi-line text content.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/ef5c447c139d4f6782a88c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133232Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dea7e7648a7b2d6b97e39569f5e508a5b8d217e196fead06c02610029ca8d543)

Don’t

Don't use text areas for single-line content. Use text fields instead.

  

### Related components

**Component**

**Usage**

Text area

Text areas allow multi-line text content.

[Text field](https://zeroheight.com/626199550/p/980e7b-text-field)

Text fields allow short single-line and free-form content.

[Phone number field](https://zeroheight.com/626199550/p/490309-phone-number-input)

Phone number fields are only used to input phone numbers.

[Date field](https://zeroheight.com/626199550/p/33c9e4-date-picker)

Date fields are only used to input dates.

  

---

  

### Platform

We use platform-specific text areas that differ between Web, iOS and Android. The main difference is the behavior of labels, placeholders and the resize handle.

  

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled. On Web, the field contains a resize handle; on iOS, it doesn't.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0a965e77a8aef88bb3d9e5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ee61477d545f417929bfff6503eb69d024d6715a6670a4f24d4f6d122620fb92)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7aa352821725425a35ffc4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=42bcb0598d1993f507aeb7b7170f6fd2b1c9f17f13385f3b7988839bacd48541)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/10adb3386ab2fcfdf11696?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b1d78c8514f0e88310584b22d64113b38ba83dddc35954997efb43fecffbf97)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9c76879a412a489eeda307?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7423535a5b71b503c5bd9f43a8ec522fef834a8492c115faad1dbbfd8a3c8050)

Active filled

Add notes

  

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3a68903f4e686c60ecee46?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4dcc9f795a29152b1775476fc0ee4877c0f0cf2ec25bf774b1ae1f4befba728b)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0fd6695160c85c20bd973b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3194284261ceadb91bd25417353ee03046513aa2b5dd230190875fd44da4701e)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d018d0db0fece167ac65af?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02b6b8b770c4358cca6b6873388e5a7338e4af7bd7365d453af89a3d45473b4d)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d8e332414727e5899c83ca?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=19d5b5abf57f76619a62dce90708d2b412358d06c87ba413b3943e10eb15da4d)

Active filled

Add notes

  

---

  

## Variants

### Modifiers

#### Header

Like all form components, text areas contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8e14d91c2989d39ef7594a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2866603b93168ab7478735bdf8705a7b34039d57ebb0d33aa6635173812c42f2)

Add notes

Text areas should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

---

  

#### State message

State messages can be used to provide additional information or feedback on the usage of the text area.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

![Error (Web, iOS, Android)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/07651285044e8db5f959c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b018d459f616a8b05fc7ae5c00ae2cedfe12f624196dec6f051ce702daf04951)

Error (Web, iOS, Android)

Add notes

![Information (iOS/Android)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6e56784df7196532fc8938?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b61595c83a6d0bd2d5ab7c57019d9469ed32746023ebec07965223945dba5b82)

Information (iOS/Android)

Add notes

![Success (iOS/Android)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d3ba20ea617adf645263d5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f2b1b7aaaf090662b4bd0534c4d89b85ec1a8c10a31e4801baf783d7dd49c51b)

Success (iOS/Android)

Add notes

![Warning (iOS/Android)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/369526b6105fa45d7be5e0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e46f178a86bbb81fccd50c4e8709fe36d5ed904441690628664df265591e4e11)

Warning (iOS/Android)

Add notes

  

More information:

-   [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
    
-   [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)
    

  

---

  

#### Icons and suffix

Unlike the text field, the text area does not contain any icons or suffixes.

  

---

  

#### Character counter

A character counter can be added to display the number of characters entered and the total number of characters allowed.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a054629da917411b9068dc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b8a69b74cc3bb02eabcc52383693c8c2dd08f9cb91dbd79e099098684ec329dc)

Add notes

Depending on the platform, there is different behavior when the character count is exceeded.

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4ccfcd4aee702ae8a68e30?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4091c6bdf439de5c2bac250c6a0546e6f4fd084cd508635ebb8b4dfc00a30b3d)

Web

Add notes

The counter goes into an error state.

![Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4d90d005499114fe0fdaa9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fc8db8a92bc518ffc9ea3cfa8e358f21d21d3e5d49efe17062e5279692e09fbd)

Android

Add notes

The entire field goes into an error state and an error message is displayed.

![iOS](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7d4c0c89adc99aa919d11d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4fc5ced06c52612a0f9b677a8c448cac2c0764db759cc3b1aec833dc68622f1c)

iOS

Add notes

It is not possible to type in more characters than are allowed by the character limit.

---

  

#### Resize handle

Only on Web the text area contains a resize handle. It allows the user to change the height of the field. It is not possible to change the width of the field with the handle. It's also not possible to make the field smaller than the min-height (96px).

On Android, the field automatically grows if the content is longer than the field.

On iOS, the field has a fixed height. The user cannot resize the field.

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/232bdbc835f0812a296a26?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=554cc175efc0a922ceb05c018346dad11fe9aff37e783ea11373c235a8223a3a)

Web

Add notes

![iOS](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/110683ffe2c33e96eb5457?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ebed1728a272abe14fe80691d39ff8626a50ff7ed942a9e6d3e904a8e5b1c8b6)

iOS

Add notes

![Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d9bf75c08a3491ae37f59c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aad575cfb6628365d3bd838ed0d3dd074e69a1cf2f10184d8a155569ba80d75b)

Android

Add notes

---

  

## Behaviors

### States

Text areas have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, it changes to the active state when a user presses on the text area.

  

#### Neutral

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0a965e77a8aef88bb3d9e5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ee61477d545f417929bfff6503eb69d024d6715a6670a4f24d4f6d122620fb92)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/570993d125301f45d20a4e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4d1a4d140d340c303deb0fdd7a4e5b56f4982fa92a40488df6927c046f99bb30)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/10adb3386ab2fcfdf11696?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b1d78c8514f0e88310584b22d64113b38ba83dddc35954997efb43fecffbf97)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1fe93966a4bfba26697db8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b80c924ec704419db37bc8c5adf191787ef159d88550a7a23e96e0437e46821)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7aa352821725425a35ffc4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=42bcb0598d1993f507aeb7b7170f6fd2b1c9f17f13385f3b7988839bacd48541)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ab3a5ac9820ab938da43d7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f92bb9231f33618bb16d3963ff64eea9dd0898de4031fa9af63384901f07a515)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9c76879a412a489eeda307?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7423535a5b71b503c5bd9f43a8ec522fef834a8492c115faad1dbbfd8a3c8050)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6c1090682b7917ff893a38?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6d50e5742114964bab87f5e8125058e4be0f3466f74fd1548afcd9688baeb9cd)

Disabled filled

Add notes

#### Error

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cf176ee34dacba35071dbd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c3bc91ea9afde65bc17b12b80259350035071bfdf8024097ef3aeb0ce0dd5ced)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7f723bc005979324025dc6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=36e49acd7d5f921c7b9760eb6594115dcc305cbd71c084390237c9a8f205076a)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/604e9334ee8787fb6e89b7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=13f22f0b439c910b3525f1d6d27323118b9db8aac4c363eee77fdaa217e83fb8)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4f5e83c9862cba5861ad73?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fdee8156af0e0e5f37ea329db3b184a894ff53bb85b5f3901f687fab3e3f49d3)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6486197d246ce8420e742c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc53043991f702597e21bf860d1a3391ff884549fac8a2f203c5b8712d781934)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8387fc1fbeaf222ba2cf0e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8eec5619fbd3b8c4f233ba8eacb1a03ae9dfee6f2f8922b370609ef6237423ff)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6b72832fe45d75f295d878?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8d93c71d5aaf75b412d54743ef4f129ebe1aec8a8aa4729fd787bb312ae8ef5e)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2fe47d7aa8e569c4fd9400?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0f1d657a1fdc88bec7e6b6fe355603b485da8cfb8f1e5a3f925f1411a0b207b8)

Disabled filled

Add notes

---

  

### Height and width

The text area can have a fixed width or can be set to 100% (full-width) of the container. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

The min-height of the text-area is 96px. On Web the user can make the field longer by pulling on the [resize handle](https://gemini.zeroheight.com/styleguide/s/92948/p/438e9d-text-area/t/3d6be5de7b). On Android, the field automatically grows if the content is longer than the field. And on iOS, the field has a fixed height, which the user cannot resize. When the field is smaller than the content inside, vertical scrolling is available.

![Default height](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0868f5900d9e01e9a76091?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e48b56bede1b64f38d9f8fa5c41002b16daca613500bf67eb83133df44ba9cb2)

Default height

Add notes

![Height increased by user](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/edae14e85c20e657d39dea?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fc60b3ea689aa74d9178705366c940b77874355d50c48f6fe123b335bd3c32d)

Height increased by user

Add notes

![Height smaller than content](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b744133ff7f53b70006d2f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=de75a221d0fb4a3970cfa86193ca7ef1eacb945e2c222fb8cd670b7b753e51bf)

Height smaller than content

Add notes

  

---

###   

## Content

### Main elements

#### Labels

Text areas should always have a label, to help the user understand what information to enter.

-   Keep the label short and concise (1-3 words) and in noun form.
    
-   Start with a capital letter and use no punctuation (including colons).
    

  

#### Helper text (optional)

Add an helper text if the user needs assistance completing a field.

Use sentence-style capitalization and punctuation.

Helper text is an optional feature and can be used instead of a tooltip.

When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text.

  

#### Placeholder text

Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.

  

### Overflow content

If a user's content exceeds the vertical space of the variable text area, the user can either expand the field container using the resize handle or scroll the content vertically within the set field container.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).