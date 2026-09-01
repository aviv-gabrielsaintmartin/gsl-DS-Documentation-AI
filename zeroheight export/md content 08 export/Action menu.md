# Action menu · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Action menu

Ready

Action menus display context-specific actions in a dropdown list.

[

Guidelines

](/626199550/p/16f691-action-menu/b/500e66)

[

Web demo

](/626199550/p/16f691-action-menu/b/47f7db)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** To Do

![](/uploads/8HY5luhWgM6hGin5UWj1Ng.png)

-   [
    
    Action menu on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7287 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7287")
-   [
    
    Action menu on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-actionmenu--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-actionmenu--docs")

  

## Usage

Action menus display a list of context-specific actions in a dropdown list. They are used when additional options are available to the user, but space is limited.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/164a91776514f7752359f3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6afab0b52445eaf8452c81614481e6110dbacc51a370a57ae7e3ad56d29ecfdc)

Do

Use action menus to display a list of actions.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/23dce4c449aa845c7541a4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1016b583d1b5757d0aee95c730a0405bb988873f2ab86bf58c9beb978ba70f0b)

Do

Use action menus to filter pages.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/0b6b3acfda61bedea7e871?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=66e41202250e37e2f24c4c6ab33f68d357b5d1d0ff6c3ca99e6d1a9a6031bce2)

Don’t

Don't use action menus as selection elements inside a form. Use dropdowns instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2d593fb5f58d8a70aabc7b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5036682eaec186091aaac3540c25aa1e0bf69ef023ef8a5bde74f709552b8634)

Don’t

Don't use a backdrop behind the action menu. If you want to block the content, use a modal bottom sheet instead.

  

The action menu does not support submenus or subsections.

  

### Related components

**Component**

**Usage**

Action menu

Action menus display a list of context-specific actions. Although they are primarily used on desktop, they can also be used in apps if they contain only a few actions.

[Modal bottom sheet menu](https://zeroheight.com/626199550/p/28f40b-modal-bottom-sheet-menu)

Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps.

[Dropdowns](https://zeroheight.com/626199550/p/98cf75-dropdown)

Dropdowns are used in forms to allow users to select an option from a list.

  

---

  

### Platform

We use platform-specific action menus that differ between Web/Android and iOS. The difference is the position of the icons and that we use a native dropdown list on iOS. On iOS a destructive action is available, on Web/Android it's not.

![Web/Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/73f7397ca430391aff3f61?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=356ac2d190fe2d11f0c7639dc1b879a156d93ef390849a9ed5227c988c4c1e1e)

Web/Android

Add notes

![iOS](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5aa7f9d6806373d0451668?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c7c6f4849359eb11a84d95974af08ee64f9b59e9ef377c408a6981fbb4c43660)

iOS

Add notes

  

---

  

## Variants

### Modifiers

#### Trigger

The action menu can be opened with the following button types: tertiary icon button, floating icon button and text button.

If you use a different trigger, please share your use case with us so we can improve our guidelines and documentation.

  

![Tertiary icon button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/379824ccc59d5601a42c17?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=574b5a0682263ef8560aadf1ae151c9a44fc070538dbc8ded3624e8baf91d082)

Tertiary icon button

Add notes

![Floating icon button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3d4d5d66a994365fce3eba?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81b694091f763a164dc8615951238ae37c591ba79308536ef7ec4e62de6c871b)

Floating icon button

Add notes

![Text button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/390a974ccbfa04152f7c5a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8cbdf5db56884db5f449c2966047be59673e4c09c623d0407ef9ac1fcd7fda9a)

Text button

Add notes

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/164a91776514f7752359f3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6afab0b52445eaf8452c81614481e6110dbacc51a370a57ae7e3ad56d29ecfdc)

Do

Use icon buttons when space is limited or the action is commonly recognized, such as the three-dot menu icon.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2894f3b42df950b52b9571?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4ca55b5c66040aad28f703eb0c7e9daff10db08766b6f4a7734ce1a52dcfffe2)

Do

Use a floating icon button when the action menu is on top of a image or map.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/23dce4c449aa845c7541a4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1016b583d1b5757d0aee95c730a0405bb988873f2ab86bf58c9beb978ba70f0b)

Do

Use a text button when the action needs to be explicitly clear, especially for less common or more complex tasks. Use it to filter pages.

  

---

  

#### Icons

Icons can be added to the dropdown list. They act as visual cues to provide clarity to the user. On Web/Android the default icons are on the left and the external link icon on the right. On iOS all icons are on the right.

![Web/Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/73f7397ca430391aff3f61?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=356ac2d190fe2d11f0c7639dc1b879a156d93ef390849a9ed5227c988c4c1e1e)

Web/Android

Add notes

![iOS](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5aa7f9d6806373d0451668?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c7c6f4849359eb11a84d95974af08ee64f9b59e9ef377c408a6981fbb4c43660)

iOS

Add notes

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/a358e3b3a7a6932c17ac33?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7f90b72784f2a54adf08d8faeba660787e45cd57c27041336b3401169d4afe2d)

Do

If some items don't have an icon, remove all icons.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/de2e48b0c8ad74804e0fa2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=156aa76c2a8a41d3bea074f4697b4b60e3d2bc30faa4c1a9deecf406502c78ec)

Don’t

Don't mix menu items with and without icons, as it reduces readability.

  

---

  

#### Menu items

Menu items can be actions or links. If the menu item is a link, the external link icon is displayed.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/07a051aae471872b063173?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a1ee6eb71039d31bc943928e745f4e72b35a0fb87b207e36a60d67a15b544f9)

Do

Links are marked with the external link icon.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/979cab2094c3fbd1a7ba16?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=217e709e00fdb5ba98984bd4b28d3c905c4176cce24812ec1790a1ba79dc6db3)

Don’t

Don't hide the link icon, as it can be misleading to the user.

  

---

  

## Behaviors

### States

The items in the the dropdown list have the states default, hovered, and pressed. They can be selected or unselected.

![Unselected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/07be620b5d1f237df0959a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4b5fb2ddc36c03b86d83c428da509d14d4478508b8b2edf6d501c30c601ee57f)

Unselected

Add notes

![Selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f45b1aaa0d0f93d190cee9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d8441036ac97bc26fd48ce0f3c39668909bad33fe196527fdd8e90dec743f681)

Selected

Add notes

  

---

  

### Interaction

The action menu list opens when the user clicks or taps on the button. When it's focused, it can also be opened by pressing the return key or the space bar.

It closes when the user clicks on the button again, selects an option from the list, clicks outside the action menu or presses the esc key.

It's not possible to have two or more action menus open at the same time on the same page.

![Opening and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9684ac3ca6e686ae66780d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aa4aed3af5d3e262515bfeee9f25b40b76cd995ef0512d0efc383bd7e5633ad1)

Opening and closing

Add notes

Clicking on the button

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/79aa94f3f94eb4b495be0e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ff012d079657f3084b1741911f1ce920f99dd56f923080385159ca5fe46cf3b7)

Selecting and closing

Add notes

Clicking an option

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e18906c9ffd8df0a1fdfa0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9cbc6dbfbec3fa506fe73c2bb9bb13b5ad5c371ec60f36758e73afc4209368bb)

Closing

Add notes

Clicking outside the action menu or pressing esc

  

---

  

### Position

The dropdown menu can appear at the bottom, top, left, or right of the opening trigger. The opening trigger can be aligned to the left, center, or right.

On iOS, it's not possible to position the menu manually. It uses the default native behavior.

  

To avoid complexity, not all positions are available in Figma. Feel free to detach the component.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/76ae49d87bc164ba554ed2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ae9c523dd00329be073bf89cd942ca17bf1b4412767d385526c75dab3380bfc9)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/50170e325e41e5270db241?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=762eceea1329a5ecd494e029c0bc5de5c1d40b4a24e5177b1b5c15ade4ce5c48)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5e72202673062cbc5be8c0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ac82e74b1c54e20e12a9b3c313cd4ea888c3442246bd056c31b13f71914722f)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e30451e626f2198d42167e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8d88c64e9e537f16c039354ba89a90beda88b638626821ad5d5cb17df1ca7cbc)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c14a5e45e73ecacd3c5b2a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b62807e0bfbc46dde29492141c09397a8bc022a1d33bc83fe8029d21fd74f98b)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/850426d1376c844db45c87?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b5b8537a400de16292a06b48d5b34a5a37400a0743e5ff36185ed6b4c3feffbc)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5030f7d68d67591cfe9a09?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3ff836ffcb7ae7053ee9ef81a8737a68e9988e40dcf91299e220dface9766286)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a939e27546dbee003ed04a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=027ddbfd79a599a5a18ac8c74030c3c060a784b0fa20cb6f67e03f1d8216ddb0)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/61da83be2f5bda59bf1141?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c83dd9a2974e294f2e93fc32803bf2f8fc6834772b511097c7d9f7fd1c7bf714)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a767fcb796b0fa3e95396b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=50601a8597a87552503e0ee36e3b2fef89b3fd2066dcb9c4670e8056078754ba)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8f52644956bde2c858102e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5261a21bf41944ddbbed1ed567c7da4b36e62fc24e0891785dd4ad69d7fe5f62)

Add notes

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0161bcb5109925987d76a7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f7091435d10f16d2a447029ca38d8f81c95f5544eb7fab7a52e70399e16a865d)

Add notes

  

---

  

### Breakpoints and width

On the Web, for XXS and XS breakpoints (from 0 to 600px) a [modal bottom sheet](https://zeroheight.com/626199550/p/5942fd-modal-bottom-sheet) is used.

For the breakpoints above SM, the dropdown list is used. By default the width is 320px. It can also be set to hug the content.

On Android and iOS both components can be used regardless of the screen size.

To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Modal bottom sheet menu](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ce2db68f84b1749f3e7955?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6c42e6925a96fcc636d59e90033726ef09a48197a14444e5a70ad2d97163e29e)

Modal bottom sheet menu

Add notes

Web: XXS to XS (0 - 599 px)

Android and iOS: used on all breakpoints

![Action menu](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1f6b21644d93cc8f79fb71?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cec6b60ed002676424ec8b2ff63978efcc76bca5ffb0efdb1849493b3f398831)

Action menu

Add notes

Web: SM to XXXL (> 599 px)

Android and iOS: used on all breakpoints

  

---

  

### Scrolling

Scrolling is technically possible, but we don't recommend using it. We recommend using fewer options or to use a [modal bottom sheet menu](https://zeroheight.com/626199550/p/28f40b-modal-bottom-sheet-menu) in apps.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/031d6bda873e6aa252a8fa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28faf3cfc178a361ae8122f47ed816574bc38ec18d42b8d7119f6246a1497615)

Do

Use fewer options to prevent scrolling.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/1082768d0dc8b0b3518318?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130111Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1ac58e58d0cd17e5839a1cf7f42b614932cb619e1d1dafbb68a4c5aa64170ed9)

Don’t

Avoid using to many menu items to prevent usability issues. For longer lists consider using a modal bottom sheet menu on apps.

  

---

  

## Content

#### Menu items

The actions in the list should be clear and inciting. Our users should be able to anticipate what will happen when they click on an action.

Menu items should lead with an action verb that encourages action, in the infinitive tense.

Use sentence case without punctuation.

Try to keep it under 2 lines.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).