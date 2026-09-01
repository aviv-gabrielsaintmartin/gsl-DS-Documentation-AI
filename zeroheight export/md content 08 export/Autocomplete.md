# Autocomplete · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

COMPONENTS

# Autocomplete

Ready

Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more efficiently by providing relevant results.

[

Guidelines

](/626199550/p/094183-autocomplete/b/933944)

[

Web demo

](/626199550/p/094183-autocomplete/b/2323de)

  

**Web:** Ready ✅ │ **iOS:** To Do │ **Android:** Ready ✅

![](/uploads/qVZPr35vzW8m3tMKJ-mqyg.png)

-   [
    
    Autocomplete on Figma
    
    
    
    
    
    ](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7275 "https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7275")
-   [
    
    Autocomplete on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-autocomplete--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-autocomplete--docs")

  

## Usage

The autocomplete component is an advanced text input that simplifies the selection of one or more values from a long list of options.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/62ed5641632c2aa60f312c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130338Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bdacc1c5f9f629dde60181961a04f0bedebd6968e34ce81c9f36dd13ecf80244)

Do

Use autocomplete to help users find what they're looking for quickly when there's a large amount of data or options.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/85b2ced17869df1b966737?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130338Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7501ef01fe56ba91a9f2ec6e707b23de3fe51c017c13427058b2ced5275e6eb8)

Don’t

Don't use the autocomplete when there is a small, predefined list of choices. Use a dropdown instead.

  

### Related components

**Component**

**Usage**

Autocomplete

Autocompletes suggest options as users type, ideal for large or dynamic lists.

[Dropdown](https://zeroheight.com/626199550/p/98cf75-dropdown)

Dropdowns display a predefined list of options for users to choose from.

  

---

  

### Platform

We use platform-specific autocomplete components that differ between Web, iOS and Android. The main differences are the platform-specific text field and the modal bottom sheet.

  

#### Web

On the web, the autocomplete appears in a full-screen modal bottom sheet on phones and as a standalone dropdown on desktop.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/486554d10fef4951da216b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5a85d15e9c0fc8779e551b45c6bb11251f47f536225f065f86aeb51e9408156)

Phone

Add notes

![Desktop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d2ee331462c3eab7487938?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=397154aee63973b2485e503eb06e079b14518753ab3505845a3b8c8a14e0ebc7)

Desktop

Add notes

  

#### iOS

On iOS, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The iOS-specific text field and modal are used.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e1c43ae8d77c56479b99cb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=acd93b2a05e0ee4adec40a896b9063fbc89cfe2067256e2b621ce75a8783c614)

Phone

Add notes

![Tablet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6c9f15486c1c819c46bbc8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=96016f9fed7d75ecca49d9f258884c5279813b33f8d1280bb89c22b48e736992)

Tablet

Add notes

  

#### Android

On Android, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The Android-specific text field and modal are used.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/22c10d372af196b406f99e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b37f106e6a1b067c6f771135825221dae2e92557f50a32812e3a677597b627c4)

Phone

Add notes

![Tablet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/22f89a2c97334e617f13f5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d14f64369429e183ef0f50b2b86a9d868f874d57c9c4b70a414c5494dd8064a)

Tablet

Add notes

---

  

## Variants

### Modifiers

#### Dropdown list

The dropdown list consists of a mandatory label and an optional caption on the right. The number of displayed rows is defined by the consumer, with no fixed limit. The list rows are available in small and large heights.

![Small rows](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/60880df7075e58567f4065?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1600e2c4b7fc34f1e55e223b9bce53de975cba6a1397adf1ffd7a3b0418772de)

Small rows

Add notes

![Large rows](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/aa3d130c0d29c9cda062a0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2c035d6582fe19728e08402f91db25846263965c40cb55b1aed9169494cc099f)

Large rows

Add notes

The dropdown list includes an optional text button. The button is positioned at the end of the list.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/6c58b8546b280230f617d7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cb5791aefa6a358458e4d997de6790cfe28df41b7ddeb891ac65daa38be7f711)

Add notes

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/15b224e8e74e7a2ac8b7bb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130338Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2ceb6fc2aa15e04458ed37fa20530c2a48e85d3e690a905dda0ce118cd416526)

Do

Use the button for geolocation tracking.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/b4f5a9c2fe2ffc5f2be0f6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T130338Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=955a83c9152ec3c446843b61b7cfb65bced4d38db3ff3e033c3df2fb8d1e6e50)

Do

Use the button to help users when they can't find the result they expect.

  

The dropdown list also includes optional icons on the left and right.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5d2db2b6e1ae0349b83e74?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=35d582e727292e0a1d46b379e617016ffc2f57efb9579df9c982279b0f0e9add)

Add notes

  

#### Text field

The autocomplete contains a text field. See the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-97e03c-84052978-35) to learn more about the modifiers of this component.

  

#### Modal

On iOS/Android tablets, the autocomplete appears in a modal. See the [modal bottom sheet documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet) to learn more about this component's modifiers.

  

#### Top bar

The autocomplete on phones contains a top bar. See the [top bar documentation](https://zeroheight.com/626199550/p/27f21d-top-bar) to learn more about the modifiers of this component.

####   

---

  

## Behaviors

### States

#### Autocomplete

The autocomplete component has the following main states:

-   -   **Default empty**: The input field is inactive, meaning that the user hasn't yet interacted with the field.
        
    -   **Active empty**: The input field is active (focused) but still empty. This state indicates that it is ready for user input.
        
    -   **Filled**: The user has entered text, and a dropdown list of matching suggestions appears below the input field, allowing the user to choose from the available options.
        
    -   **No results**: No matching options were found. A message appears to inform the user, with additional text offering suggestions or alternative actions.
        

![Default empty (Phone)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/10d6e0d851cdd6cb7e0961?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=455e5024e2abe0f6cda0780d5bb58a4ccd43b7071d7c1d1644e3421395bcd0b8)

Default empty (Phone)

Add notes

![Active empty (Phone)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/833db8d9ea603f33875e9e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f24cc9bc7b538fca84da128c15837959f473ffa0d65052fdf27a511a998e7df1)

Active empty (Phone)

Add notes

![Filled (Phone)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/486554d10fef4951da216b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5a85d15e9c0fc8779e551b45c6bb11251f47f536225f065f86aeb51e9408156)

Filled (Phone)

Add notes

![No results (Phone)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fc15b121b4d9294cf05a99?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7922590aa5c14f2ac64a38e835551c749c01a61f54ebc6309c6c1c356346fa1b)

No results (Phone)

Add notes

![Default empty (Desktop)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/75d102677c9a78079afac3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22fa57921517b6e852ba83e0313d3acb2b8a33869c0f144fd5b8ca5310a2c352)

Default empty (Desktop)

Add notes

![Active empty (Desktop)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/63e23d902630b7913f1c62?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3ac6612c29e3e4bf9b9be3734cafea5b61fe72334fbb03ec08fa6757dc1b8bfb)

Active empty (Desktop)

Add notes

![Filled (Desktop)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d2ee331462c3eab7487938?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=397154aee63973b2485e503eb06e079b14518753ab3505845a3b8c8a14e0ebc7)

Filled (Desktop)

Add notes

![No results (Desktop)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fff9aea0eae6817b6a64ed?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1dc7f12a4bc7ae5329aea1b289f465a35bdf011af7baf27e336df84e2c96b6e4)

No results (Desktop)

Add notes

#### Text field

See the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-97e03c-84052978-35) to learn more about text field states and error.

  

#### Dropdown list

The rows in the the dropdown list have the states default, hover and pressed. They can be selected or unselected.

![Unselected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f6c0c35dd55ebe8fef2c8d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6796edc1290ffa2a20ecccdd5111f66f2a89b08b2b823f20bd2d2ba5951298dc)

Unselected

Add notes

![Selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/95fe1ae882fdd6fae827d5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=742198abe3e2d297377a848e38a9529b760bcb37c668652ee55c6b61970ba953)

Selected

Add notes

  

---

###   

### Loading

The loading state appears when suggestions are being fetched after the user enters a query.

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/06f494bdffd409131b5cf3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fe4b0fa7ff42dbddbd2e5149b05ddf3e9ab16ad54e79cc7a39ed0c6c41670511)

Phone

Add notes

![Dektop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c87fe818210eabf9c823a6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a3fb159f00516730e29829f216fcc5fd68b49c6af8459b693f33095745c1e44c)

Dektop

Add notes

---

  

### Interaction

#### Desktop

On desktop, the dropdown list opens when the user begins typing in the input field. It closes when the user selects an option from the list, clicks outside the dropdown, or presses the Esc key twice.

![Opening](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f9da2061d57e4f2c1a9d72?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c58d5fddc4cad329d8732c13665a229e66c8795be242d27bef31b8b26364ab82)

Opening

Add notes

Typing in the field

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0c3db4ea6c0363d8898dd2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7290b05e82a27757b9d22aed24fe19a699f085136f24e6e48796ad935661f13f)

Selecting and closing

Add notes

Clicking an option

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c608abb3a876e94c3f2c6a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e416de616cdfecb02235f03cd7148216bea302752def2532d9ded476962944e0)

Closing

Add notes

Clicking outside the dropdown or pressing the Esc key twice

  

#### Phone and tablets

On phones and tablets, autocomplete opens in a modal bottom sheet (full-screen on phones and modal on tablets) when the user presses the input field. In the modal, the user can filter the results by typing in the text field. When the user selects an option, the modal closes. The user can also close the modal by tapping the x-button.

![Opening](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/666f627b001a2c8c610fa4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=43559b49380a87ccaff02c639043b7dab3df0c8f932389788a901002578a7033)

Opening

Add notes

Tapping the field

![Selecting and closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0c53ba394cb68d3bff83d2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ccc9ba018552e9b215ff90e0e2764846ed752d17d58dcc683bfee8fbbb6907d1)

Selecting and closing

Add notes

Tapping an option

![Closing](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/31b26715f0c0c74edc41c3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47bdfbcd174e6f22c6f32845327b2136d820f30b5bba476b8ce834890ad1868a)

Closing

Add notes

Tapping the x-button

---

  

### Position and scrolling

By default, the dropdown list is positioned below the field. On desktop, it is placed above the field if there is not enough space below it. If the options exceed the available space, the dropdown list becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings.

To avoid complexity, not all positions are available in Figma. Feel free to detach the component.

  

![Phone](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1e049b2917d22b3b2b3120?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9625bf2563f82993d444151a5830215d45b03db06f737aad809419ea17b4921)

Phone

Add notes

![Desktop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5d96886ea6a78866969c03?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a911499dd5eb99de12fa89574088cf0330fc2d2ccc82e2014f1536f166f4caf9)

Desktop

Add notes

![Desktop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/43c4d88350bf7ac160d22b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b7488f0e0740af60d3854dd58035c973ede5754aa7d68b076361090e67414ac9)

Desktop

Add notes

  

---

  

### Breakpoints

The style of the autocomplete depends on the breakpoint on web and Android, and on the device on iOS. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Full page](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/486554d10fef4951da216b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5a85d15e9c0fc8779e551b45c6bb11251f47f536225f065f86aeb51e9408156)

Full page

Add notes

Web breakpoint: XXS - XS (0 - 599 px)

Android breakpoints: Medium - Expanded (> 599 dp)

iOS: iPhone

![Standalone dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/d2ee331462c3eab7487938?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=397154aee63973b2485e503eb06e079b14518753ab3505845a3b8c8a14e0ebc7)

Standalone dropdown

Add notes

Web: SM - XXXL (> 599 px)

Android: Compact (0 - 599 dp)

iOS: iPad

  

---

  

## Content

#### Text field

Refer to the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-980e7b-84054521-39) to learn about labels, helper and placeholder texts in the input field.

  

#### Dropdown list

The label in the dropdown should clearly identify the option. Use a value of your choice depending on the requirement (e.g. name of town, department, district, street...).

The caption should provide supporting details (e.g. department, town, district...).

Try to keep it under 2 lines.

  

#### No results

Refer to the [info state documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/84818f-info-state/t/page-7142d3-87401819-40) to learn more.

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).