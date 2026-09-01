# Info state · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

PATTERNS

# Info state

Ready

Info states are placeholders used to inform users about success, error and empty states.

[

Guidelines

](/626199550/p/84818f-info-state/b/37e5e8)

[

Web demo

](/626199550/p/84818f-info-state/b/472e12)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/LN74ZjSUK8ybAYHhYiKc2Q.png)

-   [
    
    Info state on Figma
    
    
    
    
    
    ](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7261 "https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7261")
-   [
    
    Info state on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-infostate--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-infostate--docs")

  

## Usage

Info states are used to communicate system status, errors, or other relevant information to users. They typically include

-   Empty states: Shown when there is no content to display or resources are missing
    
-   Error states: Indicates problems such as network outages
    
-   Success states: Acknowledge successful actions, such as submitting a form
    
-   Loading states: Notifies users that data or content is being processed or loaded
    

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/46b091654d0343e2f7a1a8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=381828a70a8787e7cac9d3f63f1eefd6c0ded7438e1bd6db470323406b563915)

Do

Use the info state component for empty states, when there is no data to display.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/37e3f163af8ab6d6a73c34?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a64ebed558e3802313a0be75b2d5ffdd5b521bdf446325382a3cea84568024c4)

Do

Use info states to display errors such as network outages.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/2cb3baa27b299ffc1188db?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a66215cc5b707b099427f925eeb824b57678aed5584b6dce4a57cb22c8a334c)

Do

Use info states to confirm successful actions.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/abf50a1f4baa2140d9bf7d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9bfddf416e5a284c1c3cf7eaeb2d5eb72ffb219d265f5cc9cd96622b6b599edf)

Do

Use info states to inform users that content is loading.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/5458ffe59f844fedd88bcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7013f546cce76ba18b096560baed41409a62a15b118bec9f5bb2e74e2e1fb58b)

Don’t

Don't use info states for quick inline notifications. Use feedback messages instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c2399db2d1dbcf6ed76458?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4897dfa535740d72a819bac708871b037e4af9ef92e2c9ae8ca3e2d6d4b80004)

Don’t

Don't use info states for warnings or errors that should block the user flow. Use alerts instead.

  

### Related components

**Component**

**Priority**

**Usage**

**Example**

[Snackbar](https://zeroheight.com/626199550/p/54ff4c-snackbar)

Low

Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that don't require user confirmation.

Seeker saves listing to favorites

[Feedback message](https://zeroheight.com/626199550/p/8754bc-feedback-message)

Medium

Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. They inform users of system processes or provide additional information about a task. They can be used for critical alerts or as passive feedback.

Seeker receives warning that he has reached the limit of saved searches

Banner  
(not a gemini component)

Medium

Banners are used for important, persistent information. They remain until the user closes them or the problem that caused the banner is solved.

Seeker is shown static information about search results on map

[State message](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/ced82a7a5e)

Medium

State messages are used for inline feedback in forms to guide users, correct errors, or provide additional information.

User enters incorrect password

[Alert](https://zeroheight.com/626199550/p/7142d3-alert)

High

Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken.

Agent deletes listings

Info State

High

Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states.

User is not connected to the Internet

  

---

  

## Variants

### Modifiers

#### Illustration/Icon

Info states can be used with an icon, an illustration, or neither. You can't use them with an icon and an illustration at the same time.

If you use an illustration we recommend the usage of hero illustrations.

![With illustration](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b43245d8e5f5387fca434c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4fffdafe4609444690fa694df2bdf916db58bcbc6468b4eca01ac63d40e3e79)

With illustration

Add notes

![With icon](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f356c5e938b777c5f806d1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ac56bc8f5b5be6bed6aa370c834a0f45b26e0c36cca7a419225d9aa4999c2413)

With icon

Add notes

![No icon/illustration](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8b795bc895a534d7457f61?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=019e01390fee7a74ee25417248ad4a77b767f696df5bde7f33439cb4f431e6ea)

No icon/illustration

Add notes

  

**Figma tip**

To select the correct illustration, go to the common page in the illustration library. For example: [Common Hero Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-312)

There you will find illustrations for most use cases, such as informational purposes, error messages, and more. If you can't find the illustration you're looking for, please request it on #gemini\_symbols.

[Learn more about the symbol library process](https://kugawana.slack.com/archives/C03HLJU6E3U/p1723193835245029)

---

  

#### Title and description

Both title and description are mandatory.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8b795bc895a534d7457f61?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=019e01390fee7a74ee25417248ad4a77b767f696df5bde7f33439cb4f431e6ea)

Add notes

---

  

#### Buttons

Info states can be used with 1-2 buttons, or without any. If two buttons are used, we recommend combining the primary and tertiary buttons.

They should be used when they provide clear next steps or actions for users, such as retrying after an error, navigating to another page, or resolving an issue.

![With two buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8b795bc895a534d7457f61?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=019e01390fee7a74ee25417248ad4a77b767f696df5bde7f33439cb4f431e6ea)

With two buttons

Add notes

![With one button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7fa8063ff5002e92d5f496?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=42d7f18550a16daa544094d300c8c174e4f04c7c70e50edcd0177b0763683e45)

With one button

Add notes

![Without buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4928752a8f8996d4d040e9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29528264385f6dca006350dca8f06b1721d8fd6846c0a629c7ca5140676eeeaf)

Without buttons

Add notes

---

  

## Behavior

### Interaction

Info states appear in response to system events such as errors, loading processes, empty content, or successful actions.

They disappear when the user takes action, such as retrying or navigating away, or when the system resolves the problem on its own, such as completing a load process. In some cases, they disappear automatically after a short period of time, or they may require manual dismissal by clicking an action button.

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d46916d37174dd25627df7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=475a1621bf7d61f2c064fad6b44442752dc3e48174c333ae074522dee44112c0)

Closing

Add notes

Clicking an action

---

  

### Breakpoints and width

The width of the info state and it's buttons depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Width: 100%](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f3aef2585646e61490db09?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc97d2c4400029beba3b8251595d525e72f52dc37d5d050ecca294ba37e8db25)

Width: 100%

Add notes

Web: XXS - XS (0 - 599 px)

Android: Compact (0 - 599 dp)

iOS: device 0 - 523 px

![Reduced width](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b3efa8a391cf1632936a6c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=94a7e48cc4720584b42fdfb38efd3c674dc6ea9d6dbdc9cad02962c90a20ac3c)

Reduced width

Add notes

Web: SM - XXXL (> 599 px) --> width: 50%, max-width: 570px

Android: Medium - Expanded (> 599dp) --> max-width: 429 dp

iOS: device > 524 px --> max-width 524 px

  

---

  

## Content

#### Title

The mandatory title should be short and concise. It should contain a brief and clear statement or question.

  

#### Description

Descriptions are mandatory and are used to give additional context and details. Use clear and simple language and don't overwhelm the user with too much information. Tell the user what happened and what they need to do to proceed.

Don't blame the user. Stay positive and empathetic but don't say please and sorry. Don't use "Oops".

Keep the description to 1-2 sentences.

  

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.

Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like “Done,” “Close,” “Cancel,” or “OK.”

Use sentence case without punctuation.

Try to keep it under 4 words and/or 30 characters maximum in English.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro) and [Info state guidelines](https://zeroheight.com/626199550/v/latest/p/85a997-info-state).