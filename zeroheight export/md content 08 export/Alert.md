# Alert · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Alert

Ready

Alerts are modals that provide users with critical information they need immediately.

**Web:** To Do │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/Eu5gCszyADmog0cdnC6abQ.png)

-   [
    
    Alert on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7297 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7297")

  

## Usage

Alerts are used to communicate urgent or critical information that requires immediate user attention or action. They should be used sparingly to avoid overwhelming users, and to ensure that only the most important messages are conveyed through alerts. They disable all other page functionality when they appear and remain on the screen until acknowledged, dismissed, or a required action is taken.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/0e1a64e9c08bd22f050cab?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d790543a7d6decd13b2a59968bd4ce71b9e9b457bb15e1fb0de11cd66a83ab4b)

Do

Use alerts to ask the user for confirmation before completing a destructive action such as deleting a listing.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/21f1f2579710c768f39c25?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=adab7a5eb811e24a541e25a2d12df81545a51f11e3257de8511ea5d52b87aa3e)

Do

Use alerts to convey critical information that requires immediate user attention or action.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/0ae86cc71c767c17cb9cdd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=34bd12b0d0bb2586518a060a8567a3d899c342307c710d3c9d5aa4cf8a4155a3)

Don’t

Don't use alerts for non-critical information or routine notifications. Use less intrusive components, such as snackbars or feedback messages, that don't interrupt the user flow.

Alerts are disruptive and block the user flow. Therefore they should be used sparingly.

  

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

Alert

High

Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken.

Agent deletes listings

[Info State](https://zeroheight.com/626199550/p/84818f-info-state)

High

Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states.

User is not connected to the Internet

  

---

  

### Platform

The design of the alert depends on whether the alert is specific to the app or website (custom design) or is a system-level notification (native design).

The alert is not yet developed for the web. In the meantime, please use the [modal bottom sheet](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-modal--docs) instead.

  

#### All platforms (custom)

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/0e1a64e9c08bd22f050cab?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d790543a7d6decd13b2a59968bd4ce71b9e9b457bb15e1fb0de11cd66a83ab4b)

Do

Use custom alerts for messages generated by the app or website to ensure a consistent look and feel across all platforms.

  

#### iOS and Android (native)

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/26715ff98ede61c4ff741a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=25a1b93f0acc5dc82266129989a6f4719b75d9543c8ce0c6fd1f28b62c71c486)

Do

Use native iOS alerts for system-level notifications. For example, to request permission to send notifications to the user or for location tracking.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/4fc131a60a5d870553b0fa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130317Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9f73eefbe076021b6bebeb3a913f0b6770397ca88f8d1b6c6ffcad1dce181e13)

Do

Use native Android alerts for system-level notifications. For example, to request permission to send notifications to the user or for location tracking.

We don't provide all native system components in Gemini. If you need one, please refer to the official Figma platform libraries:

-   [Material design 3 Kit](https://www.figma.com/community/file/1035203688168086460/material-3-design-kit)
    
-   [Apple Design Resources – iOS 18 and iPadOS 18](https://www.figma.com/community/file/1385659531316001292/ios-18-and-ipados-18)
    

  

---

  

## Variants

### Modifiers

#### Icon/Illustration

Alerts can be used with an icon, a spot illustration, or neither. You can't use them with an icon and and an illustration at the same time.

![Icon](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7ec3ca3762867cfd90ecb2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=16f4a834b67be1ef640f8233afd82661add7241494153ba740c203a654b42e69)

Icon

Add notes

![Illustration](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/205a035c36cb9cdd09e92c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3082764e947c32f7f42a90f9954743b9a56bfa3f384145f8af40dba99da2e558)

Illustration

Add notes

![No icon/illustration](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8ba18075fd31d0d96c5a6a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a3a8b5d51534142704ef96b468daad1b30418186f2578057564c975f263fe804)

No icon/illustration

Add notes

**Figma tip**

To choose the correct illustration go the common page in the illustration library. For example: [Common Spot Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-250)

There you find illustrations for most use cases such as informative purposes, error messages, and more. If you can't find the illustration you're looking for please request it on #gemini\_symbols.

[More information on the symbol library process](https://kugawana.slack.com/archives/C03HLJU6E3U/p1723193835245029)

  

---

  

#### Title and description

Titles are optional, but recommended for clarity. Descriptions are optional and are used when additional context or detail is needed.

![With title and description](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/895118f33b665ee22f17cf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7ce95e5131f3969b8fe07fa7d7bff6ab23adc74fceb54a41686fce2c038290f4)

With title and description

Add notes

![Without description](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e125884e93d8c9c74bfdd8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=66446568bc4be36e61efd209a84d727f245d1341a887de7a9565c729e40d4b44)

Without description

Add notes

![Without title](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/24f4dd8f5329db0c9c638a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=95ddde2ddc3190f275cdd0a8d3f7f0c964d0023738e413d8600147dc022ee57a)

Without title

Add notes

---

  

#### Buttons

Alerts can be used with one to three buttons. If two buttons are used, we recommend combining the primary and tertiary buttons.

![1 button](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bbfa2f2b82173b40645296?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e028c62146f8d4348ddb116c6d7a25b7041c400a3b629187069874069df42019)

1 button

Add notes

![2 buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/205a035c36cb9cdd09e92c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3082764e947c32f7f42a90f9954743b9a56bfa3f384145f8af40dba99da2e558)

2 buttons

Add notes

![3 buttons](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b159c6dae8607e21c6b766?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a8dcd9c37f670d1bd62a426d66044778b6af1a27e8375de58e39c7465d02c478)

3 buttons

Add notes

  

---

  

## Behavior

### Interaction

Alerts either appear in response to user actions, such as submitting a form or deleting a listing, or they appear automatically to notify users of important information or errors.

Alerts can be closed by clicking on an action or by clicking outside the alert. On iOS, you can choose whether or not to close the alert when you click outside of it.

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b319b3dedd740632177e89?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=41d2be89c5065cbe8310ef89b9931c36c703b6c1a8ba8274537f09046cc4f3e0)

Closing

Add notes

Clicking an action

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/017c57ec0bac26fcdc7435?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ba69375a0ad6bed9bf7939990e4ebc46fcf3e30c2cb0c5669d5d6c41b990948)

Closing

Add notes

Clicking outside the alert

---

  

### Breakpoints and width

The width of the alert depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Full width (minus 16px margin left and right)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/aa74232f5ee0fce8a4743c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9bb6df64355849ed2fab00688442305a83f419290a82169ba4d57683f60780a7)

Full width (minus 16px margin left and right)

Add notes

Web: XXS - XS (0 - 599 px)

Android: Compact (0 - 599 dp)

iOS: device 0 - 399 px

![Fixed width: 400px](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1dcfe92c117fcf10a25f00?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4f0916ae690cf9d191a65b9fb71b0c7d471fba85b28122eae18c4a686f85fed)

Fixed width: 400px

Add notes

Web: SM - XXXL (> 599 px)

Android: Medium - Expanded (> 599 dp)

iOS: device > 400 px

  

**Figma tip**

Use the breakpoint variables to automatically set the correct width.  
  
[Learn more about using variables](https://zeroheight.com/626199550/p/37f3bf-breakpoints--grids)

  

---

  

## Content

#### Title

The title should be short and concise. It should contain a brief and clear statement or question. Titles are optional, but recommended to improve clarity.

  

#### Description

Descriptions are optional and are used when additional context or detail is needed. Use clear and simple language and don't overwhelm the user with too much information. Tell the user what happened and what they need to do to proceed.

Don't blame the user. Stay positive and empathetic but don't say please and sorry. Don't use "Oops".

Keep the description to 1-2 sentences.

  

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.

Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like “Done,” “Close,” “Cancel,” or “OK.”

Use sentence case without punctuation.

Try to keep it under 4 words and/or 30 characters maximum in English.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro) and [Alert guidelines](https://zeroheight.com/626199550/v/latest/p/719bc9-alerts).