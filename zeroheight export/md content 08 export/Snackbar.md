# Snackbar · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Snackbar

Ready

Snackbars are used to provide quick feedback after an action is taken.

[

Guidelines

](/626199550/p/54ff4c-snackbar/b/07ac21)

[

Web demo

](/626199550/p/54ff4c-snackbar/b/14fcc0)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/iVl8k509VdXqV-5U4qY40A.png)

-   [
    
    Snackbar on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7301 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7301")
-   [
    
    Snackbar on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-snackbar--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-snackbar--docs")

  

## Usage

Snackbars are short messages that appear at the bottom of the screen to inform users of the outcome of an action without interrupting their current activity. They should be used to provide quick, non-intrusive feedback that doesn't require user confirmation before proceeding. They don't block the user from continuing their task. An action may be encouraged, but not required.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/213088a349162eaace8538?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed42cd0d1e66d187a91bdf9c3d143296e30672e118615c84a75fbb9ab5507720)

Do

Use snackbars to provide non-critical feedback after an action has been taken. For example, saving, sending, or deleting items.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c76777eca69c81bf2e7594?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f31b7a4af3bce11c2d0d9272fde14d7d61a676d72762fc5ca49140fdacf88554)

Do

Use snackbars for non-intrusive feedback on actions that doesn't require user confirmation before proceeding.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/3b07fe65a77534c2c6b307?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d0c5134c78b62fe3e21d2c4181723aaa28205700304d696db22f3deba0264db7)

Don’t

Don’t use snackbars for static information that are not a result of a user action. Use feedback messages instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/0cfedcf709161b42e9a5e6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a0bbecc8fb8886daa89aecb56f3af6539bb84a101199d39b2f0b53d498fe480)

Don’t

Don't use snackbars for error messages that point to a specific part of the page. Use feedback messages instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/9bd902159cb0f74b2b0190?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ac00857df1984dcff07791e032be507ec0790955f1cb48e50e22867d7b4e7c8d)

Don’t

Don’t use snackbars for critical messages that require the users attention. Use feedback messages or alerts instead.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/3a48967e2e5358aac98ee5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133122Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4b2c640a7b57f46b101daa4320ed4b6fd87a1df10b6c2d1704c8f29baec5c7c7)

Don’t

Don’t use snackbars if you need to block the users flow. Use alerts instead.

  

  

### Related components

**Component**

**Priority**

**Usage**

**Example**

Snackbar

Low

Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that doesn't require user confirmation before proceeding. They don't block the user from continuing their task. An action may be encouraged, but not required.

Seeker saves listing to favorites

[Feedback messages](https://zeroheight.com/626199550/p/8754bc-feedback-message)

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

[Info State](https://zeroheight.com/626199550/p/84818f-info-state)

High

Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states.

User is not connected to the Internet

  

---

  

### Platform

The snackbar has a close button (x-icon) on the web. On iOS/Android, it doesn't have a close button, but disappears automatically after 4 seconds.

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/03be43f3c7d420bf180b69?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29eb98f4385abfe3635ad1b4b937bb3b62301e2bd1f59eb013202d4f705264c7)

Web

Add notes

![iOS/Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/42b31092ad824117ed962f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bd3f40c590bf43cc57a98c5a2231fcba860d15edb1e35ddf832ab75708e5699e)

iOS/Android

Add notes

---

  

## Variants

### Type

Snackbars come in the following types: info, success, warning, and error. These variations help users quickly understand the nature of the message, whether it's informational, confirms success, issues a warning, or highlights an error.

![Info](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2241cebfcc81c2207cc68a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c3939ebe93a823a4b34555ca60c8524ad847141dbd339473be2945ce9a3e580)

Info

Add notes

![Success](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/250c45a26e301cb4ec2a89?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8746ba987b26b00cc1f571962b812dd2017dca78d5b7d98091a2e8662033da91)

Success

Add notes

![Warning](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ea870caafd00078ddc6951?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18dbf06926009988c4382adbf837e8f4afc3d8b3b27f41c00a8c16724fd1c010)

Warning

Add notes

![Error](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/08aba68b6edd034ed5cbf1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=48b29e6cf3f7ac38a5956b03b23f022d20525571e226cb6138c22e40c26a36d5)

Error

Add notes

The icons associated with each snackbar type are standardized and should't be changed to ensure consistency and clarity across our products.

---

  

### Actions

Snackbars contain optional action buttons. Short actions appear on the same line as the snackbar message, longer actions appear below the snackbar message.

![Short action](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2f80b0f4a4ad4eb65c506c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2d538a4f9269569429db985088d9c9d87a46daa8634e9a92d3a8a265b169fa66)

Short action

Add notes

![Long action](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/3100635aec748f90bfb1f3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85442f99cb11dc58d22544075ba2e2fbb3496749a36b18cb567fabe886c046e1)

Long action

Add notes

![Without action](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5acc5141d24f837d311d07?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eb09613222373999710f878e3b99481324bd6bbe13a0a02ea5967914a97142a7)

Without action

Add notes

  

---

  

## Behavior

### Interaction

Snackbars appear in response to a user action, such as clicking a button, submitting a form, or completing a task.

**Web**

On the web, snackbars remain on the screen until the user clicks the close or action button to dismiss them.

For accessibility reasons we can't make snackbar disappear automatically on web. Learn more: [WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG21/Understanding/timing-adjustable.html)

**App**

On iOS and Android, snackbars can be either auto-dismissable or persistent. Auto-dismissable snackbars disappear automatically after 5 seconds (default value) or when the action button is clicked. Persistent snackbars remain until the user takes an action. We recommend using auto-dismissable snackbars only for noncritical messages.

  

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7766412da2823c9e461fd2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fdd86f6f31e2cacd5f80b50a2d06fef9463c2df17132c99778d3d7db5d0f318)

Web

Add notes

Clicking the close button

![Web](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/81a0b7861d23d27f403bd8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9a22e86958e26a79d5ebd7806f402b49f6206edc4a4ee81a40d455f5e5cd957c)

Web

Add notes

Clicking the close button

![iOS/Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e2e49ac8ca3ee0dc18fdf2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0fd414b3e74112e9dbe0c99a91446ad14ce78e874161d5e76b91bbe069833414)

iOS/Android

Add notes

Clicking on action button or waiting 5 seconds

---

  

### Breakpoints and position

Snackbars are positioned on the bottom of the screen. On web the spacing from the bottom depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

#### Single snackbars

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6f05ff7349b151bb4dd4ff?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b4aa5ee6d33820d52ec1b81397cb0fff3cf2caabd31c90ec650eecc1a8641e9b)

Phone

Add notes

Web: XXS - XS (0 - 599 px)

![Phone (above navigation bar)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6386158e30ce24a063d450?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7bd8522f138e198ced95b890cc33945146a2586ac452b59fe34d69a6df6ffa5e)

Phone (above navigation bar)

Add notes

Web: XXS - XS (0 - 599 px)

![Phone (above button bar)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/54ee2230c5dec18d64b4d7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=83faabe9764d2caac7ceec81efac6c2b647efaa03e65d6026c361b25fcf53111)

Phone (above button bar)

Add notes

Web: XXS - XS (0 - 599 px)

![Tablet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0be94ebbf19c3a1d8a4083?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fd10760c71b78d6d000770ea30139fc87d9248ae60c0bfe9a5cf64c224d7c336)

Tablet

Add notes

Web: SM - LG (600 - 1279 px)

![Desktop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ac65efba6047a6d0be6cb1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a291b376de487594f24219b1d4248b8c71f2c2470cd5cff8336a1851a82eabc4)

Desktop

Add notes

Web: XL - XXXL (> 1279 px)

  

  

#### Stacked snackbars (Web only)

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0e86ddf57945136173cccb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a9dbe6799c150a4103e6c4650fb55907ddfb18b0150eacd8da5c162ccfe4b9f1)

Phone

Add notes

Web: XXS - XS (0 - 599 px)

![Phone, above navigation bar](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/51295605ca455e68fa6a53?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f12000df8f52dae2f53f798a72182ae3006e5f3c053c4b13e548a72bba61f72f)

Phone, above navigation bar

Add notes

Web: XXS - XS (0 - 599 px)

![Phone (above button bar)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/93261c35a93d38b7dc1dd0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7bf22b2872cd0ef1a971b1a4913f726ebfa02402b896d1371e1c5fd2449a722f)

Phone (above button bar)

Add notes

Web: XXS - XS (0 - 599 px)

![Tablet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5eea5d6dba2c21e5f9e955?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=57c9968135b465c66d9e2d40d81bcb51d730cf2eb57ded6843f277cd6947e599)

Tablet

Add notes

Web: SM - LG (600 - 1279 px)

![Desktop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4512e45739c31b6236f410?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4e5eace86cb9f41b2b5e821b99b1edb7c90702710f9e69ecba22f8b1892b9f33)

Desktop

Add notes

Web: XL - XXXL (> 1279 px)

  

Snackbars can only be stacked on the web. On apps, only one snackbar is visible at a time. When a second snackbar appears, the previous one disappears.

---

  

## Content

Snackbar messages should be short and concise. Keep the message to 1-2 sentences.

Write in an active voice and clearly state what happened as a result of the user's action and avoid unnecessary details. Make sure the message is straightforward and easy to understand at a glance. For example: "Message sent."

If the snackbar includes an action button, use a concise, verb-based label for the button. For example: "Undo"

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).