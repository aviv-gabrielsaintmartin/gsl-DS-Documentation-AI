<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3492446795/Listing+card | Last modified: Aug 26, 2026 -->

# Listing card

Listing cards are actionable cards that summarize the details of a property listed on any AVIV Group website. They are generally used as calls to action but can contain different actions within their content.

![](images/Wo3lI2EnblK39bpXMzUxDQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Non-gemini component | Ready ✅ | Ready ✅ |

* [Listing Card on Figma](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Experiences?m=auto&node-id=2115-63352&t=geH6znIMgzYmtyaC-1)
* [Listing Card on Storybook](https://card-mfe.awaited-seagull-dev.aws.aviv.eu/f1f2cc2f/index.html?path=/story/card-cardfull--responsive)

---

## Usage

Listing cards are summaries of properties used as calls to action. Depending on the environment the call to action can vary, from saving a property as a favorite to getting more details about the property or contacting the owner/agent.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/WD5aH8L-xYh7CvydW89Ekg.png) **DO:** You can hide certain elements of the Listing card if you don't need them for your design. | ![](images/wscwmtdfo7VVclCZP9c51A.png) **DON'T:** To favor the best information architecture, we don't recommend changing the order of elements of the Listing card. If you need more flexibility, consider using the Listing summary component. |
| ![](images/BbIfi64reI38iMQ2dPuDwQ.png) **DO:** Vertical aligned Listing cards should be listed vertically one after the other. | ![](images/tRPbBk7qwZCbxYBs0lt5Yw.png) **DON'T:** Don't align vertical Listing cards in a masonry way. |
| ![](images/foOf__hgUS6XBl0-vnd7KA.png) **DO:** Horizontal aligned Listing cards should be listed vertically one after the other. | ![](images/Cdmmxz__4aVyT9seE_dCXQ.png) **DON'T:** Don't align vertical Listing cards in a masonry way or inside carousels. |
| ![](images/1vXFB-FDZfvt-6sV6xrAyA.png) **DO:** Listing cards S (carousel) are only meant to be placed inside carousels. | ![](images/oeUvZDZqkebsjATP2DkyIQ.png) **DON'T:** Don't use Listing cards S (carousel) for regular listing lists aligned vertically. |

### Related Components

Not documented

**Research:** [Continuous Research from Team Waldo / Starlord](https://docs.google.com/presentation/d/1IZYgKJE0SP0P1PlVeiUS8mB09hgdTShDgFE9ZUL4130/edit#slide=id.g30b1c67e645_1_1)

---

## Variants & Modifiers

### Layout

* **Vertical layout** is reserved for mobile devices Listing Cards, both Web and App versions, except the S - carousel version.
* **Horizontal layout** is used on larger devices like tablets and desktop sizes. It can be used in combination with S - carousel.
* **Ribbon** is an add-on to bring more attention to the listing and use it as a promotion.

| Vertical | Horizontal | Overview |
| --- | --- | --- |
| ![](images/c607d663c8a89f12068cdd.png) | ![](images/24c4fe1474a2634169fe4a.png) | ![](images/f7116d71dbb23efca3571c.png) |

### S Carousel

#### S - carousel

The listing card size S only comes in vertical alignment, this is because it is only meant to be displayed inside carousels. These carousels can be added to your page as sponsored listings, suggested similar listings, etc.

The Image slider inside the Listing card is disabled so the user can't slide through the images, however, the slide counter is displayed with the numbers so the user can see the amount of images the listing contains.

![](images/a75527c43e6c3385adb519.png)

There are two ways of displaying these carousels:

#### Fixed width Listing Card S

This listing card has a fixed width of 280px so the overflowing cards can be cut out of the carousel. They all have a fixed margin of 24px in between cards and the carousel can slide these cards individually.

![](images/k_T-dcZSCqZzXfQxYXEYgA.png)
![](images/BL9d0DA1JRDe_XNtvUFzxQ.png)

*The fourth card in this carousel is clipped.*

#### Responsive width Listing Card S

This listing card has a minimum width of 280px but they grow horizontally to fit the carousel width in stacks of 3 to 5 cards. They all have a fixed margin of 24px in between cards and the carousel can slide these cards in groups of 3 to 5 cards.

![](images/Mp2ENhkHRwB9N3KEx3twJQ.png)
![](images/7cau-bKq8CkZwT34saX7QQ.png)

*Listing cards grow horizontally to fit the carousel's width.*

#### Carousel Card Height

In the context of carousel cards, where cards are placed side by side, variations in content length can result in inconsistent card heights. To maintain a uniform height for better readability and visual consistency, S Carousel cards can have a fixed height.

| DO | DON'T |
| --- | --- |
| ![](images/aPPjJ604aOQ7VkMHqlkmCg.png) **DO:** Carousel cards should have a fixed height to ensure better readability and visual consistency, as content length may vary between cards. | ![](images/7A--W609SEtkj_052iKjZw.png) **DON'T:** Avoid using relative heights for carousel cards, as this can result in inconsistent card heights, making them harder to read and disrupting the visual balance. Use a fixed height instead to ensure readability and uniformity. |

### Modifiers

![](images/ko4Giu4l_iCl80ZhWhzhwA.png)

| Sub-component | Enable/Disable capability | Quantity | Sizes | Other |
| --- | --- | --- | --- | --- |
| [Image slider](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/story/ui-content-imageslider--default) | N/A | N/A | S: 16:9 · M: 16:9 · L: 3:2 · XL: 16:9 + two 16:9 thumbnails half the height of main image · Map: 21:9 | Gradients on top and bottom are managed by the Image slider component. Size is linked to the size of the Card itself. |
| Top bar tags | Yes | 1, 2, 3 | N/A | — |
| Bottom bar tags | Yes | N/A | N/A | — |
| Price tag + Price €/m2, €/month | Yes: as a whole · Yes: Price €/m2, €/month · No: Price tag only | N/A | Price tag: Headline 24 (default), Headline 22. Price €/m2, €/month: Body 14 (default), Body 12 | — |
| Title | Yes | N/A | 16 (default), 14, Headline 24 | — |
| Feature list | Yes | 3, 4 | 12, 14 (default), 16 | Icons enabled/disabled: 12 size (16px icon), 14 size (16px icon), 16 size (20px icon) |
| Location | Yes | N/A | 12, 14 (default), 16 | — |
| Actions | Yes | 1, 2 | Button size 40 | — |
| Provider | Yes | N/A | M: Avatar size 48px · L: Avatar size 56px · XL: Avatar size 72px · Private owner: Avatar size 24px | They are linked to the size of the Card itself. The divider on top is deleted when no provider. |
| *SEO text block | Yes | N/A | Text size: 12px | **Only needed for Web version of the card** |
| *Partner link | Yes | N/A | Text size: 14px | **Only needed for SeLoger** |

---

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
