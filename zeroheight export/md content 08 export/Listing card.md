# Listing card · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

EXPERIENCES

# Listing card

Ready

Listing cards are actionable cards that summarize the details of a property listed on any AVIV Group website. They are generally used as calls to action but can contain different actions within their content.

**Web:** Non-gemini component │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/Wo3lI2EnblK39bpXMzUxDQ.png)

-   [
    
    Listing Card on Figma
    
    
    
    
    
    ](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Experiences?m=auto&node-id=2115-63352&t=geH6znIMgzYmtyaC-1 "https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Experiences?m=auto&node-id=2115-63352&t=geH6znIMgzYmtyaC-1")
-   [
    
    Listing Card on Storybook
    
    
    
    
    
    ](https://card-mfe.awaited-seagull-dev.aws.aviv.eu/f1f2cc2f/index.html?path=/story/card-cardfull--responsive "https://card-mfe.awaited-seagull-dev.aws.aviv.eu/f1f2cc2f/index.html?path=/story/card-cardfull--responsive")

  

## Usage

Listing cards are summaries of properties used as calls to action. Depending on the environment the call to action can vary, from saving a property as a favorite to getting more details about the property or contacting the owner/agent

  

---

  

## Anatomy

There are various types of listing cards, but the primary elements that constitute the Listing card component are as follows:

![](/uploads/ko4Giu4l_iCl80ZhWhzhwA.png)

**Sub-component**

**Enable/Disable capability**

**Quantity**

**Sizes**

**Other**

[Image slider](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/story/ui-content-imageslider--default)

Image slider:

-   N/A
    

Top bar tags:

-   Yes
    

Bottom bar tags:

Yes

  

Image slider:

-   N/A
    

Top bar tags:

-   1, 2, 3
    

Bottom bar tags:

-   N/A
    

-   S: 16:9
    
-   M: 16:9
    
-   L: 3:2
    
-   XL: 16:9 + two 16:9 thumbnails half the height of main Image
    
-   Map: 21:9
    

Gradients on top and bottom are managed by the Image slider component.

  

Size is linked to the size of the Card itself

Price tag + Price €/m2, €/month

-   Yes: as a whole
    
-   Yes: Price €/m2, €/month
    
-   No: Price tag only
    

N/A

Price tag:

-   Headline 24 (default)
    
-   Headline 22  
      
    

Price €/m2, €/month

-   Body 14 (default)
    
-   Body 12
    

  

  

Title

Yes

N/A

16 (default), 14, Headline 24

  

Feature list

Yes

3, 4

12, 14 (default), 16

Icons enabled/disabled

-   12 Size (16px icon)
    
-   14 Size (16px icon)
    
-   16 Size (20px icon)
    

Location

Yes

N/A

12, 14 (default), 16

  

Actions

Yes

1,2

Button size 40

  

Provider

Yes

N/A

-   M: Avatar size 48px
    
-   L: Avatar size 56px
    
-   XL: Avatar size 72px
    
-   Private owner: Avatar size 24px
    

They are linked to the size of the Card itself

  

The divider on top is deleted when no provider

  

\*SEO text block

  

Yes

N/A

Text size: 12px

**Only needed for Web version of the card**

\*Partner link

Yes

N/A

Text size: 14px

**Only needed for SeLoger**

  

---

  

## Variants

The listing cards component is heavily used in different sizes, layouts, states, and with various add-ons.

-   **Vertical layout** is reserved for mobile devices Listing Cards, both Web and App versions, except the S - carousel version
    
-   **Horizontal layout** is used on larger devices like tablets and desktop sizes. It can be **used in combination with S - carousel**
    
-   **Ribbon** is an add-on to bring more attention to the listing and use it as a promotion
    

![Listing Card vertical](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c607d663c8a89f12068cdd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=accfe679edefd15a699102868405b9275775c406c42d87f32f84cbbebd373829)

Listing Card vertical

Add notes

![Listing Card horizontal](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/24c4fe1474a2634169fe4a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=95dd41264e61f06cb18c287000865b28e48d576a44ac442a2206448041b8af4b)

Listing Card horizontal

Add notes

![Listing Card overview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f7116d71dbb23efca3571c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a9d29edefa3dd56cf4812008930d84631c237d39fe5bb8a178c8069614a87a77)

Listing Card overview

Add notes

---

  

## Listing cards S carousel

  

![Listing Card S (carousel)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a75527c43e6c3385adb519?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46366ea6d976a0dee04b8df92ae6d5a5485da3aa7ce47bc190ec3efcbae8e953)

Listing Card S (carousel)

Add notes

**The listing card size S only comes in vertical alignment**, this is because it is **only meant to be displayed inside carousels**. These carousels can be added to your page as sponsored listings, suggested similar listings, etc.

**The Image slider inside the Listing card is disabled** so the user can't slide through the images, however, the slide counter is displayed with the numbers so the user can see the amount of images the listing contains

There are two ways of displaying these carousels:

  

### Fixed width Listing Card S

![](/uploads/k_T-dcZSCqZzXfQxYXEYgA.png)

**This listing card has a fixed width of 280px** so the overflowing cards can be cut out of the carousel. They all have a **fixed margin of 24px** in between cards and the carousel can slide these cards individually

![The fourth card in this carousel is clipped](/uploads/BL9d0DA1JRDe_XNtvUFzxQ.png)

The fourth card in this carousel is clipped

  

### Responsive width Listing Card S

![](/uploads/Mp2ENhkHRwB9N3KEx3twJQ.png)

**This listing card has a minimum width of 280px** but they grow horizontally to **fit the carousel width in stacks of 3 to 5 cards**. They all have a **fixed margin of 24px** in between cards and the carousel **can slide these cards in groups of 3 to 5 cards.**

![Listing cards grow horizontally to fit the carousel's width](/uploads/7cau-bKq8CkZwT34saX7QQ.png)

Listing cards grow horizontally to fit the carousel's width

#### **Carousel Card Height**

In the context of carousel cards, where cards are placed side by side, variations in content length can result in inconsistent card heights. To maintain a uniform height for better readability and visual consistency, **S Carousel cards** can have a fixed height.

![](/uploads/aPPjJ604aOQ7VkMHqlkmCg.png)

Do

Carousel cards should have a fixed height to ensure better readability and visual consistency, as content length may vary between cards

![](/uploads/7A--W609SEtkj_052iKjZw.png)

Don’t

Avoid using relative heights for carousel cards, as this can result in inconsistent card heights, making them harder to read and disrupting the visual balance. Use a fixed height instead to ensure readability and uniformity

  

---

  

## Guidelines

![](/uploads/WD5aH8L-xYh7CvydW89Ekg.png)

Do

You can hide certain elements of the Listing card if you don't need them for your design

![](/uploads/wscwmtdfo7VVclCZP9c51A.png)

Don’t

To favor the best information architecture, we don't recommend to change the order of elements of the Listing card. If you need to have more flexibility, please consider using the Lsiting summary component

![](/uploads/BbIfi64reI38iMQ2dPuDwQ.png)

Do

Vertical aligned Listing cards should be listed vertically one after the other

![](/uploads/tRPbBk7qwZCbxYBs0lt5Yw.png)

Don’t

Don't align vertical Listing cards in a masonry way

![](/uploads/foOf__hgUS6XBl0-vnd7KA.png)

Do

Horizontal aligned Listing cards should be listed vertically one after the other

![](/uploads/Cdmmxz__4aVyT9seE_dCXQ.png)

Don’t

Don't align vertical Listing cards in a masonry way or inside carousels

![](/uploads/1vXFB-FDZfvt-6sV6xrAyA.png)

Do

Listing cards S (carousel) are only meant to be placed inside carousels

![](/uploads/oeUvZDZqkebsjATP2DkyIQ.png)

Don’t

Don't use Listing cards S (carousel) for regular listing lists aligned vertically

---

  

## Research

[Continuous Research from Team Waldo / Starlord](https://docs.google.com/presentation/d/1IZYgKJE0SP0P1PlVeiUS8mB09hgdTShDgFE9ZUL4130/edit#slide=id.g30b1c67e645_1_1)