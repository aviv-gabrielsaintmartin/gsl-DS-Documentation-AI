# Pagination · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Pagination

Ready

Pagination divides content into smaller, numbered pages, making it easier for users to navigate through large amounts of content.

  

⚠️ Web only

[

Guidelines

](/626199550/p/75187e-pagination/b/24454e)

[

Web demo

](/626199550/p/75187e-pagination/b/702f04)

  

**Web:** Ready ✅ │ **iOS:** N/A │ **Android:** N/A

![](/uploads/OAOm0A4bXtYPsHaCWfBvmQ.png)

-   [
    
    Pagination on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7290 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7290")
-   [
    
    Pagination on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-pagination--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-pagination--docs")

  

## Usage

Pagination helps users navigate through large amounts of content by dividing it into multiple pages. It provides controls that allow users to move forward, backward or to a specific page. It reduces cognitive load by allowing users to focus on smaller, more manageable chunks of content at a time. Pagination also improves performance by reducing the amount of content that needs to be loaded at once.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/196ed2431b3a5bf3bd400b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132639Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=672c8607d35f66593dd2171f2169084e586888778c775abc3022cb3bd1b313bd)

Do

Use pagination to display large amounts of content, such as search results, reviews or lists.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/f50be3247cbc6d73042c46?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132639Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a1ad7d648b35351634d98e039ac64f301162688029ec74f077745274a030f926)

Don’t

Don't use pagination for linear, step-by-step processes. Use the wizard instead.

  

---

  

### Platform

The pagination component is only used on the web. On iOS/Android, we recommend using infinite scrolling.

  

---

  

## Behavior

### States

The digit buttons in the pagination have the states default, hover, pressed and disabled. They can be selected or deselected.

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2b1e851c8ff9fcd8949849?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cf9ba4e280d0f91305b4af70705c796eca9e9f71df1f1c176160af4197427053)

Default

Add notes

![Hover](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/884c2d7b74b2ae00df3157?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=317fdc5f69dd6e217d96483f8f98e619271092410fe6e1167e7678ac6a1b2341)

Hover

Add notes

![Pressed](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/abedd3ca94ed4fe9679eb6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=164f8b50c3ad1eec81d9c9e805124c2b04d739e9a423891865442e27a1b38ee9)

Pressed

Add notes

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e9d5ae953234621086a251?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a9cf33a06e0f9b38018fdf15a317f641dcd4347fa10c954162430a406d24af49)

Disabled

Add notes

![Default selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/52c846f6af2edd16b4e2a0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5f45044cbd2332fde04cb6a3ebee2c348b6dfe0059b369835b96ac31ac0e35ab)

Default selected

Add notes

![Hover selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a3e62458d367983ec6cfbb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a8a75b41a4b5b17fa9eb5747098d86c9d4445769c55c9b06da50b45de129c122)

Hover selected

Add notes

![Pressed selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/72f3b3c224ed30dbb7c39a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=df116f8ed9d408721116b0a27e2f410973e62f9d2fd28ec52425d03e0be6feab)

Pressed selected

Add notes

![Disabled selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b2b7ebeda362166669611d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e3dddeff31cc499fe479e784a9d9116c76fe9707f1b4fa9d9cad6ffe189f162f)

Disabled selected

Add notes

---

  

### Interaction

To navigate to another page, users can either select a page number or use the chevron buttons to go to the next or previous page. When the first/last page is selected, the back/forward chevron is hidden.

![Go to next page](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ee79217af711ef1d851412?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7cb2a4df2911bdd256d6ef160166e392b5b42e8953808bce9a3805d1c64c5e55)

Go to next page

Add notes

![Go to previous page](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/04799bcb0902db94babbd1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=30995e69e77e7fd73d4b3e9c7985343dea6d4ccbffadad6141b82f94a9849165)

Go to previous page

Add notes

![Go to a specific page](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/acfa9d8185da48ff1dc752?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=99628286783766d1e84db2ffaefbc41aa14c5dcb01b7e880379bcefc61bf8872)

Go to a specific page

Add notes

  

---

  

### Truncation

Pagination is truncated when a threshold number of pages (4 - 5) is reached. It truncates the pagination by displaying only the most important pages, such as the first, last and nearest pages, while using ellipses to indicate skipped pages. The truncation ellipse is not clickable.

![First page selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/22d4fa1c40218ad6e9cd21?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f054f1f9cac4ea7429c1c2a3d4054f8c7c1abf8903aa338f0ac62fd7db5702c1)

First page selected

Add notes

![Last page selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2f91db02d6c9a44a1d9f15?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aa196b174478e16c097880bb94a7b4e11d01f41c0410ba63414cd778c00e5ac6)

Last page selected

Add notes

![Middle page selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/340517b9c3dcad3f836881?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=56520233e4f596ff3460a102a0bddae05dffbebeed9767089b58af2804c28530)

Middle page selected

Add notes

---

  

### Position

Pagination is positioned at the bottom of the pageable content, allowing users to reach the end of the current page or section before deciding to navigate to the next. Pagination is centred in most cases, but can be left or right aligned depending on the layout.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/196ed2431b3a5bf3bd400b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=14918d1da873a586795fbb4154ffbd324a0a21f244c53ca8c07a591c3408d35a)

Add notes