# Top bar · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

PATTERNS

# Top bar

Ready

Top bars display navigation elements, titles and actions such as buttons or icons at the top of the screen.

  

[

Guidelines

](/626199550/p/27f21d-top-bar/b/31990c)

[

Web demo

](/626199550/p/27f21d-top-bar/b/39af2b)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Partially available

![](/uploads/O-ifxQ8--9J3s4P5GVBDpQ.png)

-   [
    
    Top bar on Figma
    
    
    
    
    
    ](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7268 "https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7268")
-   [
    
    Top bar on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-topbar--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-topbar--docs")

  

## Usage

Top bars are navigational elements positioned at the top of the screen that provide page-specific context and actions. They typically include a title, icons, and buttons relevant to the current page, ensuring that users can quickly access key functions without losing context.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/5d21a6277d396ed9b267be?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c4f3ed8ff4bd5e374be9e46db2aaab05a11da2eeb5c9acb74fe2fdeebc076c1)

Do

Use the top bar to display page-specific titles, actions or navigation.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/7c918ad0eb52a2be640ebc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=db7d015cfef3ee8c9f5ad77100d7c4dd1490b363c7b867b75a5578330a072ecd)

Don’t

Don't use the top bar for global navigation. Use the navigation bar instead.

  

### Related components

**Component**

**Usage**

Top bar

The top bar provides contextual and screen-specific actions or secondary navigation within a specific page or screen.

Navigation bar

The navigation bar provides global navigation throughout the site and access to key destinations.

  

---

  

### Platform

We use platform-specific top bars that differ between Web, iOS, and Android. They differ in appearance and height, but offer the similar options and functionality. Only the badge, is currently not available in web.

  

---

####   

## Variants

### Size

Top bars are available in small and medium sizes. The small variant is best for compact layouts or secondary pages where vertical space is limited. The medium variant is ideal for primary pages or sections where emphasizing the title is important for clarity and hierarchy.

---

  

### Style

Top bars come in two styles: default and on picture. The default style works well on plain backgrounds, providing a clean and simple appearance. The on picture style is designed for use over images or visual elements, maintaining readability while blending seamlessly with the background.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/388ddfc5049ef525fb986c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133350Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22a85df220b77b608b92e150d9d9df65545465a2c7fbfcbf731efdf33b14ad36)

Do

Use the default variant on pages with a plain background.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/961d931a84078f6e123932?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2fbebd0b98416f0b84e80be07155fbc2e6f8823d602241e2a2df82e92860e992)

Do

Use the on picture variant on top of images.

  

---

  

### Modifiers

#### Icons and actions

The top bar contains optional icons and an optional button.

---

  

#### Title

The small title in the medium top bar is optional. We don't recommend hiding the title in the small top bar, except for the on-picture variant, to help users understand their current location.

---

  

#### Badge

A badge can be placed next to the title. They can be used to indicate notifications or updates. For example, for messages or alerts.

  

---

  

## Behaviors

### Scrolling

On the web, consumers can choose whether the top bar stays fixed at the top or scrolls with the content.

On iOS and Android, the top bar always stays on top.

  

---

  

### Width

The top bar is full-width, which means it stretches across the width of the screen.

  

---

  

## Content

#### Title

Use short and concise titles that give users an idea of what the page is about.

Use sentence case without punctuation.

  

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.

Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like “Done,” “Close,” “Cancel,” or “OK.”

Use sentence case without punctuation.

Try to keep it under 4 words and/or 30 characters maximum in English.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).