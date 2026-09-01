# Coach mark · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Coach mark

Ready

Coach marks are temporary overlay messages that provide contextual information about user interface elements. They can be used successively to create a guided interface tour.

**Web:** WIP │ **iOS:** To Do │ **Android:** WIP

![](/uploads/GwOjYxT8sMvbAII7lkLgcw.png)

-   [
    
    Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=13151-2940&t=BVNzgE29hXFwHbmp-11 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=13151-2940&t=BVNzgE29hXFwHbmp-11")

  

## Usage

Coach marks are temporary messages that provide contextual information to educate users about new or unfamiliar features.

It appears as small overlay containers on top of the content, with an arrow indicator.

Coach marks can be linked together in a sequence to create a tour.

![Single step](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/25643d6a8aadbe6492f147?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b5c06ebdb38e84efd92c5458bc796e7a21e2dba81b0cc89492b6ab710781fe9)

Single step

Add notes

![Multi step](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/21a6bee93866def418f9a9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2de9f6fe81478f2687cc15d9274f9f6829ffa9503f78621b5ca93cb51fce8e08)

Multi step

Add notes

  

Don’t

Limit the display of coach marks to one at a time to prevent distraction and cognitive overload for users

Don’t

Avoid navigating between pages; clicking the next button should not lead to a transition between different pages within a flow

Don’t

You can use a coach mark to emphasize a specific user interface element rather than the entire page. Prefer a Modal.

  

  

  

  

### Related components

**Component**

**Usage**

**Tooltip**

Temporary short overlay messages serve to clarify the purpose of user interface elements or provide additional context related to their functions.

  

---

  

## Variants

### Boolean

Only the title and the close icon are mandatory. All other elements can be hidden, offering a variety of layout.

![Full](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/61b400115880f9fdfd12c9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4ac63eabc78a5c129941b0cf24ce03cc0c9c375fe1413b15383bf7b81f0fe0af)

Full

Add notes

![Simple](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/63bca522fa2e1b59beec7b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8eb88baa0329fd6f7dd4072bd3ddd5a656ea6d746f4dfd8397c263ff45f87a0e)

Simple

Add notes

### Tag position

To ensure a perfect readability, the tag can be aligned with the title or placed on top when the title is on two lines. It's up to the consumer.

![Horizontally aligned](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4cf5e93d03522cb47ed843?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8016118a9220ba348a4b0f297d1bdb1d2175523d102a1bd4ba085aa36f457a6)

Horizontally aligned

Add notes

![On-top](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/eebab352701bc568a324bc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c2ad82b3d9d5c44e5d1557eaa044616cc13d86ae0aff156fd1be70ae96973fa9)

On-top

Add notes

  

  

---

  

  

## Behaviors

  

### Position

The coach mark appears near the triggering object.

The auto-placement feature identifies the best position from all available placement options, promoting effective use of space.

![Bottom Start](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/dce13f233b27b73ce00060?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=817603fb799f01aa8af546cdd8ccdbb2f9956bb10fbf842f8013c9b2e7e27f14)

Bottom Start

Add notes

![Bottom Middle](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/b925e8adbe96e67624e9d6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc7e6dd239fc45ca344ee0a6874b3d1445278b5592be50b1aceeae11af6129f6)

Bottom Middle

Add notes

![Bottom End](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/020b07fda8fb89b326f6ab?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a0968030feb0a302f02d894674e7b44e9ca7ab5c0c97137ab6b1c4b966f3e495)

Bottom End

Add notes

![Left End](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e7dc7f7120e809398f10b9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=59d20730aa5f455128218f8851aaebf4c530f375fbf9b35e241b4f9b6097cc1f)

Left End

Add notes

![Left Middle](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cd5bcc919b075677189fac?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=172f52561063b09ffb6dc178c0b4e01f415622a3a69408da0e19e8cda3a04750)

Left Middle

Add notes

![Left End](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/17961c3052982b2bda102e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2aff500f0389336197da9611afb117df7e95e9cb3a8ad5c3d3db97b9f6c7f61d)

Left End

Add notes

![Left Start](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9a40d56553395d22e7361a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a5f5237e204e5d4ebbb635a22bf5366787f423b9e3ed851bbde8883729f278f7)

Left Start

Add notes

![Left Middle](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1eee35fec76d61bd9e9043?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ee22023c0dc1b89cc0b8d46fbaceec3c8412c9203e7510b4460bb8f2066540c5)

Left Middle

Add notes

![Right End](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a9679a46e69010dff8053d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3beeff27f43df8915b82dbd5458a9e25ab2ee062e7913885cf756955dc002b19)

Right End

Add notes

![Right Middle](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a771c4e2fb18a82f4aa0fe?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0302950bb1184005a116ff36fa2e4b46b805b99191dcb0ea2dabb92e86a80eee)

Right Middle

Add notes

![Left Start](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5c6a75d8103d2efd2e7fcc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=44317314ae59e4a0edfa7ecc9b5ed084a26024e966d2ab9c2a71f2a4a1708dfa)

Left Start

Add notes

![Right Start](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/579c05da1e552681559aba?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c758941e2e7a9ecda88fb0f28160559b246120ca41c96cb42f6635dd1fbf54f)

Right Start

Add notes

  

---

  

### Size

Should be defined by the user between 296 and 400px

  

---

  

### Interaction

The coach mark appears automatically after the page loaded (decided by the consumer).

A coach mark is an advisory overlay, not a modal dialog. It provides optional information. Its interaction model should reflect its subordinate nature.

By allowing it to be dismissed easily, we reinforce that the coach mark is a temporary guide, not a mandatory step. This distinguishes it from critical alerts or dialogs that require an explicit user action before proceeding.

![Multi step](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/032d715feb3142d59e8056?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=203c00af8abd790e6a6599c6bc660c59b989426937f985da29e78243d9646f66)

Multi step

Add notes

![Single step](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/dbdb1e8369109afe25461c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f5c5171927fea1918a877e783739bcb19044c3468c504359bbb8671252c764dc)

Single step

Add notes

---

  

### Scroll

The coach-mark should be dismiss on scroll.

A user's scroll action is a clear signal that their focus is shifting. They are navigating to a different part of the page.

-   **Respecting Focus:** Keeping the coach mark visible would actively work against the user's intent, pulling their attention back to a part of the UI they have chosen to move away from.
    
-   **Reducing Intrusion:** The coach mark's job is to be a helpful, temporary guide. Once the user navigates away, its job is done. Dismissing it respects the "temporary" nature of the component.
    

  

---

  

### Animation

An animation is used when the coach mark appears and disappears.

During a tour, the coach the first coach mark fades out before the second one becomes visible.

The coach-mark don't move on screen.

  

---

  

## Content

**Keep body text succinct and informative**

Coach marks are quick overviews of functionality. Body text should be at least a few words, but no more than a few sentences. The title should be a few words, ideally on one line.

**Communicate the main benefit to the user**

For example, "Manage your issues" instead of "Issue types".

**Don't repeat content from the title**

Concise information is more effective, and placing the most important keywords at the beginning of each sentence enhances clarity.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

  

---

  

## Accessibility

-   When the Popover gets opened, the first focusable element within the Popover content is focused.
    
-   Focus is trapped and wrapped in the Popover content. (Source: [Progress Design system kit](https://www.telerik.com/design-system/docs/components/popover/accessibility/))
    
-   Upon closing the Popover through the keyboard or by interacting with an element within the Popover content, focus is returned back to the anchor element.
    

  

### Focus order

1.  Tag
    
2.  Title
    
3.  Subtitle
    
4.  Close (positioned here to allow an quick close)
    
5.  Steps
    
6.  Button 1
    
7.  Button 2
    

  

The picture is decorative and therefore ignored by the screen readers.