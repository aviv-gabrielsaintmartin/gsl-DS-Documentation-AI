# Wizard · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

PATTERNS

# Wizard

Ready

Wizards guide users through step-by-step processes to achieve their goal.

[

Guidelines

](/626199550/p/723d8b-wizard/b/512499)

[

Web demo

](/626199550/p/723d8b-wizard/b/24726f)

  

**Web:** Ready ✅ │ **iOS:** To Do │ **Android:** To Do

![](/uploads/efksRaEmpDyRYGCdmwhn_w.png)

-   [
    
    Wizard on Figma
    
    
    
    
    
    ](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7269 "https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7269")
-   [
    
    Wizard on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-wizard--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-wizard--docs")

  

## Usage

Wizards guide users through a multi-step processes by breaking it down into smaller, more manageable tasks. Each step is presented sequentially, with visual indicators showing which steps are completed, active, or pending. This helps users navigate complex processes with ease and provides a clear sense of progress.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/5d7a28f10e12822e484449?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T133412Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6d3ff4952d29a7236ba3a6e1a9fe3d0808a25e57893ac7ab6ac4ae0e57dbbb18)

Do

Use the wizard to guide users through a linear, step-by-step process.

  

---

  

## Variants

### List type

The wizard list is available as an unordered or numbered list.

---

  

### Modifiers

#### Description

The description is optional.

---

##   
Behaviors

### Types and states

The wizard has the step types to do, done, error and disabled. Each type of step has the states default, hover and pressed.

  

#### To do

Uncompleted steps are marked with a black circle.

  

#### Done

Validated steps are marked with a check mark in a green circle. This includes mandatory steps that have been completed or non-mandatory steps that don't need to be completed.

  

#### Error

Input errors are marked with an exclamation mark in a red circle.

  

#### Disabled

Steps that are not yet clickable because other steps must be completed first are grayed out.

  

**Figma tip**

If the vertical lines between steps have the wrong color, select the layer **Top line** or **Bottom line** and change the variant too **Done**, **To do** or **Disabled**. If it's the first or last step select **Start or End**.

  

---

  

### Interaction

Each row is clickable, but the icon is not.

  

---

  

### Placement

On desktop the wizard can be used on its own or can be placed on any background. For example, it can be used in a sidebar.

On mobile devices, the wizard must be placed inside a modal bottom sheet.

  

The top bar can be used as an entry point to open the modal bottom sheet.

  

---

  

### Scrolling

If the wizard is longer than the container, it becomes scrollable.

---

  

### Width

The width of the wizard is determined by its content. If the container is smaller than the title and description, the text flows to the next line. Texts have a maximum length of two lines. If the text is longer, it is truncated.

  

---

  

## Content

#### Step titles

-   Titles should be descriptive and help users understand what is expected of them.
    
-   Keep titles short and concise. Use 1-3 words.
    
-   Start with a capital letter.
    
-   Use consistent terminology between the wizard and your page titles to avoid confusion.
    

  

#### Step descriptions

-   Use short, clear language to describe the user's progress.
    
-   If needed, provide a simple summary of completed steps.
    
      
    

#### Progress indication

Where appropriate, use numbers to clearly indicate progress through the steps.

  

### Overflow content

Title and description are limited to two lines. If the text is longer, it will be truncated.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).