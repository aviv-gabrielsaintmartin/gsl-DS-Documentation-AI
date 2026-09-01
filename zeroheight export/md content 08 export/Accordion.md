# Accordion · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Accordion

Ready

Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of information in a compact space.

[

Guidelines

](/626199550/p/74e509-accordion/b/25c7a2)

[

Web demo

](/626199550/p/74e509-accordion/b/686b86)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/wkNTz-LmYzzZ9oU95EBrLQ.png)

-   [
    
    Accordion on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?m=auto&node-id=11-136048&t=k234WjfNSw8D6uVC-1 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?m=auto&node-id=11-136048&t=k234WjfNSw8D6uVC-1")
-   [
    
    Accordion on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-accordion--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-accordion--docs")

  

## Usage

Accordions are typically used when screen real estate is limited, and there's a need to manage the visibility of large amounts of content. They enhance the user experience by presenting information in a structured, efficient manner, allowing users to access details as needed without having to navigate away from the current context.

Use accordions to shorten pages by grouping related information together and reduce scrolling for **non-crucial content**, especially on mobile interfaces, enhances the user experience.

Be aware that when you use an accordion, you are hiding content from users. Accordions should not be used to display essential information, as hiding content behind an accordion can reduce users' awareness of that information.

![](/uploads/n-GQVeFzTx0wd-mXHwMxDg.svg)

Do

Use accordions to contain secondary or supporting content that is complementary. This reduces screen clutter and makes it easier to quickly scan through content.

![](/uploads/8d7vOTBrOZaKpN3uTKitug.svg)

Don’t

Don't put blocking crucial content inside an accordion where users can't move forward without digging into an accordion. Important messages should not be hidden inside an accordion.

  

---

  

## Variants

### Border

The accordion is available with or without a border. The bordered version has a white background whereas the unbordered version has a transparent background.

  

![With border](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a79c0e81967a73f855d4fd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9baa07b79182c17754da72d6464227df365dc35f51b3f3bbd7a691610fc97f07)

With border

Add notes

Accordions with borders are used when the accordion needs to be visually prominent, especially on pages with colored or patterned backgrounds. The white background improves readability by providing a clear contrast to the surrounding content, making it easier for users to focus on the accordion's text.

![Without border](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d2db3470279f73bb39b1d9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5b8f6554bdba986f3dc1fa0cc5b0be1402f906e4a9541307688142391458e56)

Without border

Add notes

Accordions without borders are used on pages with a solid, neutral background, where readability isn't an issue.

---

  

### Modifiers

#### Icons

Icons are used to highlight and complement the text in the accordion's header.

![With icon](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/958cdda489108ac8e0cd01?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cbba37e3a02010ba4d1a54c9f3b0315290ab14bae0c4dc3d0523b34b3445994b)

With icon

Add notes

![Without icon](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d12eb90c64775f510dcab9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e9ed6146fbcc17cc8b2cccb859ffd57352d8bcef9d5e064f594f3248de90c9a5)

Without icon

Add notes

  

---

  

#### Title, body and description text

Title, body, and description text are optional elements that can be toggled on/off depending on the use case.

The size of the title depends on the platform.

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b3a81368bf117a570bbfb4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aaddcc0005929b656fa0226778d1d2bedc1fb9172e3be307c6993d901353a612)

Web

Add notes

On Web to title sizes (22px and 16px) are available.

![iOS/Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e1d611d3177b72ea4eb10b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=60ca4b6409f3f53224b067c5c629ae35bd4f6394396511afb7a63724fbcfe311)

iOS/Android

Add notes

On iOS/Android only the smaller title size (16px) is available.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/76535cc8de9a7d6620445f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29dd9557f23d2f739626332d271c9b98bfaf95d1129b9e40fc38247989b29c36)

Do

Use only one title size and combine it with body or description text.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c457073a5f3c1be05fc77a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f2e761ddf3ba5adee70c36499edb03b0da9f768920515560b5e241b57458761d)

Don’t

Don't use both titles at the same time.

  

---

  

#### Content

All types of content, such as text, images, and other components, can be placed inside the accordion.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/6b5bf842dff679c8c780a1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3966eede9f9349f7b99c91772e94929089287bcd7e449fba8097c2fc5c567f45)

Do

Use text, images or other component inside the accordion.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/f76b408f5c1bfec6cc3ee1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f4687de2d1a8bf105e5c7e0468067559928341970f3ff206cc96248212ec01c7)

Don’t

Don't nest other accordions inside the accordion component. This makes it confusing and makes the content difficult to access.

  

---

  

## Behavior

### States

Accordions have the states default, hovered, pressed, and disabled.

![Expanding](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a32e2941459d269a19e651?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=536f8627002def5476ca6329b9c71ffab8204960ca575d5d989031e003205a5a)

Expanding

Add notes

![Collapsing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1f57e65d5430328ac9a99f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=92bc9505fd4538e65a5f71742cbe2b2f36d8fd7a72b4cdafd6d60eb9c87367af)

Collapsing

Add notes

---

  

### Interaction

The accordion can be collapsed or expanded by clicking on the header of the accordion. The chevron icon at the end indicates the current state, pointing down when collapsed and up when expanded.

![Expanding](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a32e2941459d269a19e651?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=536f8627002def5476ca6329b9c71ffab8204960ca575d5d989031e003205a5a)

Expanding

Add notes

![Collaping](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1f57e65d5430328ac9a99f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=92bc9505fd4538e65a5f71742cbe2b2f36d8fd7a72b4cdafd6d60eb9c87367af)

Collaping

Add notes

![Expanding](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a32e2941459d269a19e651?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=536f8627002def5476ca6329b9c71ffab8204960ca575d5d989031e003205a5a)

Expanding

Add notes

![Collapsing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1f57e65d5430328ac9a99f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=92bc9505fd4538e65a5f71742cbe2b2f36d8fd7a72b4cdafd6d60eb9c87367af)

Collapsing

Add notes

  

By default, accordions start in a collapsed state with all content panels closed. Starting in a collapsed state gives the user a high-level view of the information available.

There may be a scenario where it is necessary to have a single panel open by default, while keeping the rest of the panels closed is helpful to surface content. This can allow users to notice information immediately and encourage them to explore the content of other panels.

![](/uploads/dTi-tqG-98xYqRsWV98DqA.svg)

Do

By default, all content panels are closed.

![](/uploads/A9-qCazONUmuj_D4I4KHbA.svg)

Caution

In a case where there is a set list view of accordion panels, the first panel is set to open by default

![](/uploads/vSiHyk15Ay7dHlzXHv1RFA.svg)

Don’t

Avoid displaying all accordion panels expanded by default. This can increase the length of the page and make it difficult to find each panel.

  

#### Accordions should never collapse due to interactions with other accordions

If there are a number of accordions in the same group, and a user expands the first accordion and then a second without collapsing the first, both accordions should remain expanded. Automatically collapsing accordions based on interactions with other accordions degrades usability and risks confusing the user about their location on the page.

---

  

### Width

The accordion adjusts to the width of its container, filling the available space based on the size of the container.

  

---

  

## Content

An accordion header should give an idea of the content in the accordion panel. Keep headers short. By default, header content wraps to the next line at smaller widths, and multiple lines of text can be difficult to scan.

Use sentence-style capitalization - capitalize only the first word.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).