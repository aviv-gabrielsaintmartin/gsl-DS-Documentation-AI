# Carousel · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Carousel

Ready

Carousels are used to display a collection of items that the users can slide through.

  

⚠️ Web only

[

Guidelines

](/626199550/p/19c888-carousel/b/9774ba)

[

Web demo

](/626199550/p/19c888-carousel/b/139d78)

  

**Web:** Ready ✅ │ **iOS:** N/A │ **Android:** N/A

![](/uploads/BDSCuGlvtGA_Fn4mMCV6GQ.png)

-   [
    
    Carousel on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7307 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7307")
-   [
    
    Carousel on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-carousel--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-carousel--docs")

  

## Usage

Carousels are versatile components that allow users to browse a collection of items (such as images, text, cards or media) by sliding or clicking horizontally through them. They are often used to display multiple pieces of content in a limited space, providing a dynamic and interactive way to explore information.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/96ac9480a060b3acc73619?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e5e590632702dedf36f2190c7fd2db9c8fcbf2e4328cbc6280d06134e1b05230)

Do

Use carousels when you want to highlight related content and encourage user exploration. They are useful if you have limited space but want to display multiple items.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/260c7d35fb4e8eac4d594a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ca62a7b72b797c4d8ea2c1e048331fcdc2aedfa773384c6a0da1032f49a92b43)

Don’t

Don't use carousels for key messages or calls to action, as they can be hidden if users don't engage with the carousel. Also, don't use them when users need to find information quickly. Carousels can slow down the experience by requiring multiple interactions to view all the content.

  

### Related components

**Component**

**Usage**

Carousel

Carousels are versatile components that allow users to slide horizontally through mixed content such as images, text, cards or media.

Image slider

Image sliders display a sequence of images that users can slide through horizontally.

  

---

  

### Platform

The carousel is only used on the web. On iOS and Android, scrollable horizontal item lists are used.

  

---

  

## Variants

### Arrow position

Arrows can be positioned inside or above the content. We recommend using the inside arrows for visually focused content and large images. Use the top arrows when you want to avoid covering content, or when the design has interactive elements that need to remain visible.

![Inside](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3819e3ad7de7238bcdbea6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e08fdf43e1814d9c3c3f7ba94fc403c9509954db7c8daed02b069e312b27c85c)

Inside

Add notes

![Above](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d88e1948579fcae86bce92?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d68b73a7b4e3f5167aeaf9ae2e15d96166b364276baa91034c7c2a1de5ec0465)

Above

Add notes

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/77599480811038a28b2605?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2c9507df2d30ca05902a2372225cc6b96564ca79cb9131f86fc2bd3e148b7b86)

Caution

Make sure the arrows don't cover relevant information or interactive elements. If they do, use arrows above the content.

  

For accessibility reasons arrows are **mandatory** on the web (desktop and mobile).

---

  

### Dots

Dots are optional progress indicators that show the current slide. They can be placed inside or outside the content. We recommend placing dots inside the content when space is limited or the design is more focused on visuals, and outside the content when you want to avoid content overlap and improve readability. If the dots are placed inside, change the style of the dots to "contrast".

![Inside](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/472840332b3660697be386?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=102a084ac5d0f46e528759552181021d61c6f3c4c1c69f7d7d6f1c1c75f08a8b)

Inside

Add notes

High contrast dots

![Outside](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/63006ff457bb9e6a81efcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8f2916067fb61a71a8d1cae3ac067937f612d7cac8efcba360f174bbfd454d7)

Outside

Add notes

Default dots

![No dots](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4494d4c77ac4741a9fdbbd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c084aee68c908669cd4787fa2ef08cd938a6f3c9eead2dfa8988acaa43df373b)

No dots

Add notes

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/110de88576ba5eda1842c4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1a52de613c30f09913d17229a2e0f50e626f17b30529c6eb01822e73b3ed5ce9)

Caution

Make sure that dots don't cover relevant information. Use outside dots if they don't.

  

---

  

### Clipped content

It's possible to show or clip the content that exceeds the carousel container.

![Clipped content](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d73e1b1455d2a8aeb77f37?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dd1f789db645f979080c32e45c9a403972e1c2d4ceef0cb175b30bcc79eef86d)

Clipped content

Add notes

![Visible content](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d66dd21b11d37d8d84f598?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=51b9c15af97d794e968d91338ff3f73e27b38b835e973ed544d96c4215bd014f)

Visible content

Add notes

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/92854f59a4badc75be03bc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a0f2573f77c13760e7683ec0c977ab3c1bdf39d1d35b39178c09170b192c73f1)

Do

Use the carousel with clipped content if you want to align the content with other content on the page.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/96ac9480a060b3acc73619?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130922Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e5e590632702dedf36f2190c7fd2db9c8fcbf2e4328cbc6280d06134e1b05230)

Do

Use the carousel without clipped content if you want the content to reach the edge.

  

---

  

### Modifiers

#### Title and description

Title and description are both optional. We recommend using the title as the primary identifier, and adding a description when additional clarity or explanation is needed. We don't recommend using the description alone.

![Title and description](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c3f5626838a0227be3ce19?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86b2fed95ec0c2aa84e8d3922b300d0877eee560bec946401412d6c8639fdad4)

Title and description

Add notes

![Only title](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1cc229657b298107e3a830?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=00b8d38f433370991ae8224aae0e81ee41be9274a48a70e9d24adf246e256ea9)

Only title

Add notes

![No title or description](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bf0b7740db60d3bec5adbb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6b32cd7290dc3354dc3770b10fa54b13c2c3314231d4265ae97746af627eeecc)

No title or description

Add notes

  

---

  

## Behavior

### Button states

The state of the buttons depends on the slide position. At the beginning and end of the carousel the button becomes disabled.

![Start](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a8692da34a35a3ef4ecbe3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a609ed80ee364c8d7bb77fa80a40cf70756476c84936e2b79d61fdd87f63c49)

Start

Add notes

![Middle](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b11428913a9c436ae23091?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29e49b9f4eff9e1051de9aac798d953aa2f7d9c2b4b88d72e99e6c327b924255)

Middle

Add notes

![End](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/60f1e5d367872433ed520e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b4268f3b52f68c5e6457f0fc95faa3bd95bc9a09a81dc18f36fb44bf332c56be)

End

Add notes

---

  

### Interaction

We recommend limiting carousels to 5-7 slides. This range helps to maintain user interest without overwhelming them, ensuring the most relevant content is seen and easy to navigate.

The carousel slides horizontally by pressing the chevron buttons or dragging the mouse on desktop and swiping on mobile. It's also possible to navigate using the arrow keys on the keyboard.

![Clicking button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f8206be13b00ee70388a5f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fa59dd3979dc832372daf091187fd2f587abae8f5ee51e4c9eed4146c2210bb5)

Clicking button

Add notes

![Dragging / swiping](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a1d90114055ec00af18f38?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=88933557aa53cf8f1c38a0d0e5a37f21604dcaa08672a78394a5f2a17e8ca916)

Dragging / swiping

Add notes

---

  

### Carousel items

Carousel items hold the content. The carousel can be set to automatically adjust the number of items displayed per slide based on the available screen width, or it can be configured to display a fixed number of items per slide.

In addition, the number of items displayed can change at different screen sizes (breakpoints), so that more items are displayed when more space is available.

  

**Figma tip**

To simulate different slide positions in figma, you can change the item alignment from left to center.

---

  

### Size

The width of the carousel is fixed and need to be defined by the designer/developer. The height is automatically determined by the content.

  

---

  

## Content

Carousels are visually complex, so any text should be brief and concise. Aim to present only essential information, making it easier for users to quickly grasp the content of each slide.

It's best to have only one CTA per slide, or if there are multiple items on a single slide, make sure each item has only one CTA. This helps to avoid overwhelming users with too much content.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).