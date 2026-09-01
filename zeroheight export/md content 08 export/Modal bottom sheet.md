# Modal bottom sheet · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Modal bottom sheet

Ready

Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen.

[

Guidelines

](/626199550/p/5942fd-modal-bottom-sheet/b/19a993)

[

Web demo

](/626199550/p/5942fd-modal-bottom-sheet/b/848cca)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/EqU4JRZ6DUy6dKER-TKYFg.png)

-   [
    
    Modal bottom sheet on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7293 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7293")
-   [
    
    Modal bottom sheet on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-modal--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-modal--docs")

  

## Usage

Modal bottom sheets are used to display contextual information that is related to the current screen or to offer actions that are relevant to the user's current context.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/34b7ecc6ba07e8c2f78297?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cde6f158e33e7e8fbdd3f7adde73d0789713452633101635368501b08992cf0c)

Do

Use modals when it's important to get the user's full attention.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/d51884675204ed59ebfe8d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28a448a5da33ad6745bdd8fe3c909923e9056be5eba7e8e7f1a4b82cd2205cb3)

Do

Use a modal bottom sheet to present additional content, actions or supplementary information related to the current context.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/e38e8f49fa34e5631a367c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=487a6f689ac3b8f21444697599dd218f2e8fc584f004debc5fa6e414b6d01b7e)

Don’t

Don’t use modal bottom sheets when the information or action isn’t urgent or can be completed inline without interrupting the user’s flow.They can be disruptive if overused. Use other components such as feedback messages, snackbars or info states.

  

Since the [alert](https://zeroheight.com/626199550/p/7142d3-alert) is not yet developed for the web, please use the modal bottom sheet instead.

  

### Related components

**Component**

**Usage**

Modal bottom sheet

Modal bottom sheets are used to display contextual information that is related to the current screen or to offer actions that are relevant to the user's current context.

[Alert](https://zeroheight.com/626199550/p/7142d3-alert)

Alerts are used for critical information that requires immediate attention or confirmation before proceeding. Since the alert has not yet been developed for the Web, modal bottom sheets should be used instead.

---

  

### Platforms

We use platform-specific modal bottom sheets that differ between Web, iOS and Android.

  

#### Web

On the Web, the component appears as a bottom sheet on phones and as a modal on desktop. The modal bottom sheet is not draggable on the Web.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d062ffe312cd74bc9b893f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70dc74a2f1fd96d5b262c4e0bded8254a4e0e97fcde01b208185548010aadf29)

Phone

Add notes

![Dektop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/41df3408fbf6071b6c7c59?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=887cdd1cced3c17b8638df8d3283e0f5b32c7422a234732ed18c567d2a688c10)

Dektop

Add notes

  

#### iOS

On iOS, we use native, draggable modal bottom sheets. As on the web, the component looks like a bottom sheet on phones and a modal on tablets. The tablet modals have a fixed height on iOS. If you have a small amount of content, please use the pop-up component instead.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e3d0f3ac3069d6327fcb36?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b36da7b6e203ab2e3b32bc22329631e9dafa7ec81ee7a7e2a3c291276b8b900b)

Phone

Add notes

![Tablet Portrait](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ed1fde2d97f6a3b4bf99a9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=818d61294cda7a0744f55a4241b72379277314427f6b67d40555af361bcad525)

Tablet Portrait

Add notes

![Tablet Landscape](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bf091153c3902a7f794d89?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a52289b0027260513d50d853f3465bf2e1a10c442759478be9bff91170080ce6)

Tablet Landscape

Add notes

  

#### Android

On Android we use native, draggable modal bottom sheets. The component appears as a bottom sheet on phones. On tablet you can choose between a bottom sheet (`ModalBottomSheet`) or a modal (`SheetSuite`).

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fc9f83fb7489f3094e780c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6750c586d06be9e525bb8882ee576c6a3c11f7b8f4da18a3c6e38fd253269a59)

Phone

Add notes

`ModalBottomSheet`

![Tablet Portrait](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0bf342eca7cd882ac037e3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b03516f923798a9ba8175dd25873f8028a0c4dbd5ee8f627422c2ef1b3382efe)

Tablet Portrait

Add notes

`ModalBottomSheet`

![Tablet Landscape](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/074371d52d47076b2bbd18?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9eacf5dc46b373734405cb261269f0a69523fadb8b24e4d4f879621a77d575e5)

Tablet Landscape

Add notes

`ModalBottomSheet`

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fc9f83fb7489f3094e780c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6750c586d06be9e525bb8882ee576c6a3c11f7b8f4da18a3c6e38fd253269a59)

Phone

Add notes

`SheetSuite`

![Modal Bottom Sheet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/aef50d8e4f281b86c6a74c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a33582b57d3e26307e4c1e9b4c9775df350076873f8047dbf0322c09c299c1a3)

Modal Bottom Sheet

Add notes

`SheetSuite`

![Modal Bottom Sheet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0c19b2da0c434d0565c40a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2defc24a83b38c8d7151de52ab79d89169734deef4dbcb1745a8c6290e2fd2bc)

Modal Bottom Sheet

Add notes

`SheetSuite`

  

---

  

## Variants

### Sizes

The modal bottom sheet is available in different heights.

![Default (hug content)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d062ffe312cd74bc9b893f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70dc74a2f1fd96d5b262c4e0bded8254a4e0e97fcde01b208185548010aadf29)

Default (hug content)

Add notes

The height adapts to the content. It grows until it reaches full-height.

![Full-Height](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ec430392ecf777096d581d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=793301f9d565a99817ba6a47f136d214fbc358694afc8c779cc75666875d9d57)

Full-Height

Add notes

The modal has a fixed height. If the content is shorter, there is white space underneath. If the content is longer, the modal is scrollable.

![Full-Screen](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b7614ea8769c174ea57664?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1f0631f299c279f8e305d7051f7a28eb03f76f4765c32386b3d41e1ed2c3e5ce)

Full-Screen

Add notes

The modal fills the entire screen. If the content is shorter, there is white space underneath. If the content is longer, the modal is scrollable.

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/7ca99b6cb52352ef7ecf74?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=42d2bcf5d29073cf0dc67d59e8b506847abbad3035b8adf7db23ae23b0b55423)

Do

Use the default size when the modal contains a small amount of content. Since the height adjusts to fit the content, it's ideal for compact information or simple actions that don't require scrolling.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/995c40378354c2d10cc72e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4786322de9e9b40f4ee454695dd85c92664d4576827e99993abbf9814d838ecc)

Do

Use the full-height size when the modal contains a large amount of content and may require scrolling. The fixed height ensures consistency within flows.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2269c122cf728b29f5e6b0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6aae4784e81dc15f4f14b12aba09ead00e5c2e706ca3f1f569b32ce77cad4169)

Do

Use full-screen size for extensive content or detailed data entry. Full-screen modals are ideal when users need to focus solely on the modal content without distractions. It's useful for displaying maps or full-width images.

  

---

  

### Modifiers

#### Padding

The modal bottom sheet can be used with or without padding.

![With padding](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/13e3027049de64b3eed723?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bb6202b7c45785164e1e0d39897783ebea4ac0e283e3c6a24033e30cd293a4c0)

With padding

Add notes

![Without padding](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/53778fedefec46d8f989a4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=50e188448bc723c0eb1a5abcda67deed4e091e737031f2109ba402556d915945)

Without padding

Add notes

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/f4c40a59272d3d2b916e5c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=50767b5ef07563a9dcc9804a984195c1e132846746f41517903d483e4c03d52c)

Do

Use the modal bottom sheet with padding for most use cases. The padding helps separate text, illustrations and components from the border.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/3508db5cb528925a2f8d88?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc77fd9c14bbe7a03e668502d0e678f5816f59f7e134a4e4a817fffe49084a3c)

Do

Use the modal bottom sheet without padding when you want to display maps or images in full width.

  

---

  

#### Header and footer

The modal bottom sheet contains an optional header and footer.

![Header and footer](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/da5e7f4d04e6cfa017a69c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f0c933424aa9a35ea345f498323476f3c79190b7404816ebda886e42a0bd05cd)

Header and footer

Add notes

![Only footer](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3a9588326f4a08eb319f0a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1217984516bdaf8d775dc642874b4330fa98ebfcfd1b696e0dad31e547293a06)

Only footer

Add notes

![Only header](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/55422e1247df5840a3a9a5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b47ae1f966eb232da07ec24fc353bc7f2e38028c0e2a6b4a6b7e77bc6cc711a8)

Only header

Add notes

  

**Header**

The header has a close button on the left, a title in the middle and either a secondary button or up to 2 icons on the left. All elements of the header are optional.

![Header with button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/784ae0b521fef55a13db5f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=754aead1034cd084daba0925bc7df4c93239f89dfd3d327f19ee103b490e09cd)

Header with button

Add notes

![Header with 1 - 2 icons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ff37120ef9bff095370337?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9f1234c9e07a759380a847a32b7bd8bf696b0a585cd8d4957b810f3097966aab)

Header with 1 - 2 icons

Add notes

ℹ️ If a close button is needed, it should be on the left. Please don't change the position in the top bar.

  

**Footer**

The footer (bottom bar) has 1 - 2 buttons. They can be aligned horizontally or vertically. We recommend vertical alignment only if there is not enough space to align them side by side.

![Footer with 1 button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6ef2c23100ccf98bbf1b3e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a35b867d3b33cf7092974d15e7b13deced5c7af0f9dadb43f461f8f485048030)

Footer with 1 button

Add notes

![Footer with 2 horizontal buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/00596a51c708c0fa221638?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=51b3469d0f2de66bd4b62c447e7eb8c29a85a3a84d2c7d999b848f1d4807f692)

Footer with 2 horizontal buttons

Add notes

![Footer with 2 vertical buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8b43da026a2055df5f532e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=32219c0f5e340d74d77f4a41f6f533fb2c3db092860e748e7ec01511279f76e9)

Footer with 2 vertical buttons

Add notes

  

---

  

## Behaviors

### Interaction

Modal bottom sheets appear in response to a user action, such as clicking a button, submitting a form, or completing a task. They can also appear automatically based on user behavior, such as reaching a certain scroll depth, spending time on a page, or attempting to exit.

They can be closed by clicking the close button, performing an action, or clicking outside the modal. On iOS and Android, they can also be closed by dragging them down.

![Clicking the x-button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ef67289bf551fb4167f01e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc3c088563b6066186c9ed372035081032f66e53504a455718b580989e07d632)

Clicking the x-button

Add notes

Web and app

![Clicking an action](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/96b68eaad5eebcb5e80c2e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c285ab459fe58fa02e9963aaa327cacbd60919ec24dd85dcf80120b5a2637fcf)

Clicking an action

Add notes

Web and app

![Clicking outside](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3f7ac9bb770523e808c63e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=00ae65e1326312c1932bb7c5c1180430d708b04c004a3b634dff6ffb1280f0c5)

Clicking outside

Add notes

Web and app (can be defined by consumer)

![Dragging modal](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1615b0b63fc14c33a7841c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=19e2d37d4423652fd9511b41ec713dd1e5a364c07ba134e66bd6cc7c2949eab7)

Dragging modal

Add notes

App only

  

**X-button vs. cancel button**

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c55b8535e8870a31ba2109?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b392f42a67caa3121829a774e43374fa09ab78f540b7f9d6790a31094e5f6c13)

Do

In most use cases, the close button is located in the upper left corner. The "X" is quick to locate and is best for quick exits.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2a4638419d0ead2105e341?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0379ee08023f7df37dddaa6a9f73aca213c848241996f9d4a2f090adf72ca1d6)

Do

When using modals as alerts that require users to take action or make a decision, include a "Cancel" button next to the primary action.

  

---

  

### Scrolling

When the content exceeds the available space, the modal becomes scrollable, allowing users to access all the information without having to resize or close the modal. Whether the scrollbar is visible or not depends on the user's system settings.

To better separate the content from the header, a divider line appears when the user scrolls the modal.

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c7451d05fd80fcfefa27bd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c32d5f709d4a9ebb30973b065a4b76d2d892ca92a0f6c30368ee08ca35ddd8c7)

Default

Add notes

![Scrolling](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fd2ebc408db494d4962d86?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b051d0921fbbd499182e0022fa4246034703c1104837888b2f05882e2c5d8d14)

Scrolling

Add notes

---

  

### Breakpoints and width

The style of the modal bottom sheet depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Bottom sheet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d062ffe312cd74bc9b893f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70dc74a2f1fd96d5b262c4e0bded8254a4e0e97fcde01b208185548010aadf29)

Bottom sheet

Add notes

Web: XXS - SM (0 - 767 px)

Android: Compact (0 - 599 dp)

iOS: iPhone

![Modal](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/41df3408fbf6071b6c7c59?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=887cdd1cced3c17b8638df8d3283e0f5b32c7422a234732ed18c567d2a688c10)

Modal

Add notes

Web: MD - XXXL (> 767 px)

Android Medium - Expanded (> 599 dp)

iOS: iPad

Breakpoints are different on iOS and Android. Check the [platform documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet/t/a053439e7a) to see the differences.

  

---

  

## Content

#### Title

The title should be short and concise. Titles are optional, but recommended to improve clarity and explain the purpose of the modal.

  

**Content**

Give users enough context within the modal itself to understand what they're being asked to do without having to refer to the main screen. Format the modal content with headings, bulleted lists, or short paragraphs to make it easy to read quickly. Include only essential information; remove anything irrelevant to the decision or action the user needs to take.

  

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.

Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like “Done,” “Close,” “Cancel,” or “OK.”

Use sentence case without punctuation.

Try to keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).