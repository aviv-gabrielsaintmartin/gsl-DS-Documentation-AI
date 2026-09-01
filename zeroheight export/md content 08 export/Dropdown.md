# Dropdown · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Dropdown

Ready

Dropdowns are used to select one option from a list.

[

Guidelines

](/626199550/p/98cf75-dropdown/b/25287b)

[

Web demo

](/626199550/p/98cf75-dropdown/b/24fece)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/Yen_CT99Dth3O9m3lN3OKg.png)

-   [
    
    Dropdown on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7279 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7279")
-   [
    
    Dropdown on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-dropdown--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-dropdown--docs")

  

## Usage

Dropdowns allow users to select one option from a list. They are most commonly used in forms.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/113a79b2c75910b94bc5a8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131748Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3b0e40a9659fbaf1c5af90e678a304926eba4cf900525f7d97764c3351b45a02)

Do

Use dropdowns to allow users to select one option from a list.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/e6ca2777fc2a57505d75a9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131748Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=861bafd16a5e7eab6e8f96dea5b068de966d0a02f82a94088fd2a6fe6ab493b3)

Don’t

Don't use the dropdown to display a list of actions. Use the action menu instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/32399771efb3087ba0f72d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131748Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86bf96a1cadbf51b8f84ff3c2149f5580f2ac96f7f7655fc5c3c5ad5185d137f)

Caution

It's possible to use dropdowns to filter pages, but for consistency reasons we recommend using the action menu instead.

For now the dropdown only supports single-select. For multi-select, please use another component, e.g. the [checkbox group](https://zeroheight.com/626199550/p/41df87-checkbox-group).

  

### Related components

**Component**

**Usage**

Dropdowns

Dropdowns are used in forms to allow users to select an option from a list.

[Action menu](https://zeroheight.com/626199550/p/16f691-action-menu)

Action menus display a list of context-specific actions.

  

---

  

### Platform

We use platform-specific dropdowns that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders and the appearance of the dropdown list.

  

#### Web

On the web, the label is always on top of the field. The placeholder is visible until an option is selected.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d435a2d0e6541a20fd91c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c845452abc9128280c95b29853b9674b3a97f71d57e81135b045243c7ffcd53)

Default empty

Add notes

![Default selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b33c39765d5089e410b91a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=97c4b536d84e7704d0d44eaf7d585b5ae9314a4e6600ace09801792f4ff4f4bc)

Default selected

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e1e0cb8bda2ea5e084f5c7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bbf8a9fa2d31bdc3894d3da497efa6133164388be6a2905ce8dc2b7595496207)

Active empty

Add notes

![Active selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f1235e3051358fc6a2871f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=009b56d36f7fdf9db8fd56b90936ddc3b6e65cf8531db245d7c1a87ccfee882a)

Active selected

Add notes

  

#### iOS

As on the Web, on iOS the label is always on top of the field. The placeholder is visible until an option is selected. On iOS, we use the native dropdown list.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/daaf864e317482349a1185?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1664496c25274692e2b3aa2c95ff7b80b5918bbb91e513ea538bc4d0de482a9b)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/126db4768fddcb7007d924?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc7ad108a296192f5095d095376fb8d01e2cda3e96f28bc1963ff7f7ae19508d)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/870b5ad58093e85327681a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b36ae1ecc6d8459db8bb3ba552228fee416c3ab76febb35320a129d8038c4960)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d69a847991a6f923c40574?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6525d5d866cae255d02304579809b325d15732bd74fde56f98010f9e88d283bc)

Active filled

Add notes

  

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible when the field is active.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1787c087efe42e104f2a39?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1c3a03513d041b668a97a25f9f5aa7988a91faf613f2981c44191fd518342d63)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ed3b9aa92f006ba8675a4c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b7f65ea241ee4109e214ba6a1ad95ac0434e7af36c587c98b34a67b92dbdb9b8)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/51486029ec323dc96d5fac?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c7d2e33bde0796044e5a7ed638fbece550165e83120b3bfca2f985abe10b581b)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/05070550b31af81cbcc3f6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5c2283f5271ff271f90930d909f196a03a6d7bc2e18e565d61a309fe0d1fc36)

Active filled

Add notes

  

---

  

## Variants

### Modifiers

#### Header

Like all form components, text fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8c58195b44d6bb17d064e0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cfbddb8687eb8fa39175c160f9ddc848b24ceef5d11eae29fef1f06d334e2b24)

Add notes

---

  

#### Icons

Icons can be added to the field and the dropdown list. They act as visual cues to provide clarity to the user. All icons are non-clickable.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0dcbf16e32a7e500b12072?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7b3349afb784d12efeeb92c791e701d82f2d111fb76cf27becedd220fd11f81a)

Add notes

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/841f6373706d35d7e57c98?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131748Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=de1a786bdd389fb458b66645da7dac4aef4524a6ab4480d6957187e67f049c6c)

Do

If some items don't have an icon, remove all icons.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/29d26926ccce64898ffb2b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T131748Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47459a4a5116438df22c8c99d5e378499ab7b8e40f524a5f6cab57d86295b9d5)

Don’t

Don't mix list items with and without icons, as it reduces readability.

  

---

  

#### Suffix

The suffix can be added to provide additional context.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1b9eb99780fb7abcd4b334?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02594147c2a5860b5581e18c99f12fde98c1c194c1c23b8e01103ed41f9f6840)

Add notes

---

  

## Behaviors

### States

The field of the dropdown has the states default, hover, active, and disabled. It can be empty or filled, and it can be in an error state. When in an error state, the dropdown contains an error message.

The field doesn't have a pressed state. Instead, it changes to the active state when a user presses on the text field.

  

#### Neutral

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d435a2d0e6541a20fd91c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c845452abc9128280c95b29853b9674b3a97f71d57e81135b045243c7ffcd53)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cc4e3390755b17884d4fad?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bcf94416d443be209f7e364d5716ec3e476d26b2d4d9ffe321bf370eff58f225)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e1e0cb8bda2ea5e084f5c7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bbf8a9fa2d31bdc3894d3da497efa6133164388be6a2905ce8dc2b7595496207)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9d3b1e51226b1955231d31?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=421543cd7927b78bcdcb14acf516a75338e7090efaa128e5f9fd5ad9ae51828b)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b33c39765d5089e410b91a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=97c4b536d84e7704d0d44eaf7d585b5ae9314a4e6600ace09801792f4ff4f4bc)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ea1022389997601113646b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=91c44e5ed364196ddb9299a24c688950a69bc69b2dd91b2cec113415eb4f8e7e)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f1235e3051358fc6a2871f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=009b56d36f7fdf9db8fd56b90936ddc3b6e65cf8531db245d7c1a87ccfee882a)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/741f12f03d07ac30cad1dc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21e6a461b5833589bac76ddedff6d7d8d298aa233f75856fb1d8d7b8a554d497)

Disabled filled

Add notes

  

#### Error

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/935dcbc5a2ebbb44c2c477?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=36eaab5eb9bf1511e5d53a187c2e1fea5456c9018e0bb4caeee97f25c437ee9b)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3a92984649ed58b66dacb6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d0b4f4fe00d341654824b207188af4a93ba2b7133f51730d1750860eacdbb60d)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a555d18979b8beb730504d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b87cdce6d3c31e265b900f99f5b93073981ca2cd6cffeb60405a7d478938e1f1)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/215c1191a26c0b9b6e224f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7f73de44117d3e7bcfd6bbdee1ca2e5d0002a14302943b0869dd5e01ffc98103)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/acc49e4f462d8880badb77?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6123864b2d15e6faf8f99d92d59b0d23c201c03f9bc118c4bd4cb5fcef44488a)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b2e2e1e3329b1c09eb205a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=efd1b01f4195e92386b5ac9a6caa973dc3f7bf3a27d821a4a3d8d516602d2573)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8115b708422153c8a71f08?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc9841f1bfee523cb2f9eec98eb3643cd12684011090f811352bf8abd7b037d4)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/dd6b1018d23d47ba61f3f5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a1e6ef4d46bf199445c80434bf5a74dc204820a9f3d503f7e4a53664f3348ac)

Disabled filled

Add notes

  

#### Dropdown list

The rows in the the dropdown list have the states default, hover and pressed. They can be selected or unselected.

![Unselected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2ee3940a166dbf15ceef75?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6ca89a4f27b1a71a2b62afd7501d659421311826518a28edb05f458d6eb3a07d)

Unselected

Add notes

![Selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e58535fed5a2b4d0246492?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0f97e49b6d9e24f34d9ffc5ad6b6319028bcb372a62f09f8488f5525803ba3b0)

Selected

Add notes

  

---

  

### Loading

The loading state indicates to users that the data is loading and will appear shortly.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4eb7c444e21526f715cd77?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1f77bc87cb4e48931701d2c9117b8d1e17042307a04998028593e6e89445f94c)

Add notes

  

---

  

### Interaction

The dropdown list opens when the user clicks in the field. It closes when the user clicks on the button again, selects an option from the list, clicks outside the dropdown or presses the esc key.

![Opening and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e25d9051f808049e2b6f36?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=938bfc7b9a320b732d101ad81b257bb1b9972646348d63dd221537da82f4c79c)

Opening and closing

Add notes

Clicking on the field

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/974e8ed520f8011225ee40?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7a69a61e9257bb290549453bfac8c585421471620083e0bd613bd39e55299f69)

Selecting and closing

Add notes

Selecting an option

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bdc1a87b53f67f2e712c7d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=90f38708337393c249113a0eec57373015dac57664d4296d3d98108cf2c5ca60)

Closing

Add notes

Clicking outside the dropdown or pressing the Esc key

---

  

### Position and scrolling

By default, the dropdown list is positioned below the field. If there is not enough space below it, it is positioned on top of the field. When the options exceed the available space, the dropdown becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings.

To avoid complexity, not all positions are available in Figma. Feel free to detach the component.

  

![Below the field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d3ae98ed951a8c64a9447c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dfc2a7b0cba045fd5d60ab32ca5a9f10f26e50ece7f05fb9d27b247577b212b1)

Below the field

Add notes

![On top of the field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d364c547c6b49bca99f47a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7098bd31e2a2245fc057c60c49a21fe4a4ac73d2a2ee4bb18d2289841fe96f60)

On top of the field

Add notes

![Scrolling](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4ffc6574232d6ea446a1f1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3b307fc9671db12647dec2215b42795183f231302be17c5559979e0cc80ba0f8)

Scrolling

Add notes

---

  

### Width

The width can be set to 100% (full-width) or 50% of the container. For special use cases it is also possible to define a fixed size.

According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3baf20d8e358dc7fc9242e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=004c51e2db0d622da70662089670d751c7a03215aecf7a4e3ccedbddd97c2c2e)

Add notes

  

---

  

## Content

### Labels

Labels inform users what to expect in the list of dropdown options.

Keep the label short and concise by limiting it to 1 line of text.

  

### Placeholders

Placeholder text is displayed in the field by default when no selection is made from the dropdown. This is important if the dropdown does not have a label above it.

Use clear placeholder text for the dropdown trigger so that users understand the purpose.

  

### Helper text

Helper text should only be used when the user needs additional help to select the correct item from the dropdown menu.

Use sentence-style capitalization and write the text as a full sentence with punctuation.

  

### Items

We recommend presenting the options in a logical or alphabetical order.

Try to keep it under 2 lines.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).