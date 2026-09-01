# Media upload · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

PATTERNS

# Media upload

Ready

Media upload components allow users to upload, view, and manage media files such as images, videos and documents.

[

Guidelines

](/626199550/p/21722f-media-upload/b/42cb17)

[

Web demo

](/626199550/p/21722f-media-upload/b/96d98a)

  

**Web:** Ready ✅ │ **iOS:** Ready ✅ │ **Android:** To Do

![](/uploads/o_n_WvAV6f-6H3j2GuTtiw.png)

-   [
    
    Media upload on Figma
    
    
    
    
    
    ](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7271 "https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7271")
-   [
    
    Media upload on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-mediaupload--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-mediaupload--docs")

  

## Usage

Media upload components allow users to upload files by either dragging and dropping them or by clicking the drop zone.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/1b4a98eae8fe1f596d9242?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132446Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e1266b6d6aaf6a3a656e5f1d0d1cff5868705f300c7209ffaa3790d7a9937301)

Do

Use the media upload to allow users to upload images, videos, or documents.

  

---

  

## Variants

### Modifiers

#### Header

Like all form components, media uploads contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/187f823e2e62eecdda93ef?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0272d7604624ededdb50cfc57f428957de43d3a9ea07f85951ea2ea9fa6c4117)

Add notes

---

  

#### Illustration

The empty drop zone contain a illustration placeholder. We recommend adding a pictogram.

**Figma tip**

To choose the correct illustration go the common page in the illustration library. For example: [Common Picto Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-249)

There you find illustrations for most use cases such as informative purposes, error messages, and more. If you can't find the illustration you're looking for please request it on #gemini\_symbols.

[More information on the symbol library process](https://kugawana.slack.com/archives/C03HLJU6E3U/p1723193835245029)

---

  

#### File counter

The media upload includes an optional counter. In most cases, we recommend using the counter to give the user a clear idea of how many files they can upload.

![With counter](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/880c4038d25b8d9ba08a15?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f085035d475d74010d09e179ba3745c24d3da0753cc77b73b89b5a93b06d1ede)

With counter

Add notes

![Without counter](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2cb54be6c5aecae5a6d92c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18ba841b4b15f1c15f34bdee73072efad95ba193a229af5a7e8ea017115fbbab)

Without counter

Add notes

---

  

#### Filename

The image/file preview includes an optional filename. In most cases, we recommend displaying the filename to give the user more clarity about what files they can upload. Since the file preview (non-image) only displays a generic illustration, the filename will still be displayed below the icon even if the filename is hidden.

The default filename includes the file extension, e.g. bathroom.jpg. The filename (caption) can be changed using the action menu.

![With filename](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5b2d48c09686999ae48c10?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=017785e99c405d5c86317da87c219147a04595d8dfd81dea027235395ae77d20)

With filename

Add notes

![Without filename](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7111f10fc22b8c8d846288?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ba28d987ac3ff2c9f24d3dcdd745ae2b12bac9e046225bd186bedae7c769b998)

Without filename

Add notes

![With filename](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c5493817b8ebc63fba50e2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9c1d78e9d95d5087997b39fca38b8ddad07b46f025cf4405651848634eec3ef8)

With filename

Add notes

![Without filename](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/363b6d408549c144cdba6e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9149c36502e2cafeed758f214bc8928a01d82b80c24f2bb22fa015024d04e5e9)

Without filename

Add notes

---

  

#### Cover photo tag

The image/file preview includes an optional cover tag. This tag can be used to mark the cover image. The cover image can be changed in the action menu or by dragging and dropping an image to the first position. The tag can be applied to any type of file.

![With cover image tag](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8fef7bee11a1dab59bc687?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2517c97dfc3276ce30404513a695a85f5810fcb4935d00fb7af762c178edf82b)

With cover image tag

Add notes

![Without cover image tag](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0c2438e649ae2febe96063?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4f4a8665a700a1bf78b675fbfdf56d6373047a57652a9ae7ac170052306f5a6f)

Without cover image tag

Add notes

---

  

## Behaviors

### Types and states

#### Empty drop zone

Empty drop zones have the states default, hover, active and disabled. And they can be in an error state. When in error state, they contain an error message.

Depending on whether it's the first upload or additional files are being uploaded, the icon and text inside the drop zone will change.

  

**Neutral**

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a4b09ec62d0f10521bb698?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4062def50ff8faace3ebe528cd7332429eeab7fdd992291a3bc445d6c30e40b7)

Default empty

Add notes

First upload

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/776559d2e41699d96ab984?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7731a6759fdef25d79cd31f8194ebed50e91222ac0eb9c875a949a75b316bab9)

Hover empty

Add notes

First upload

![Active empty (Web only)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2af623c793e3170d8e7496?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eea6dd6350dabfb84c0de1d73920262fa3df4942c5f16072347c0f07b3a7f35f)

Active empty (Web only)

Add notes

First upload

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/400257164c5cac0bfba86a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9e4cccabd0e7c4e2183a24dc23a2e204470cd43f24a28b4a44e5175cf7c263cb)

Disabled empty

Add notes

First upload

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ce4c56b2108785da2ce40b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=99a64d482e0eaa5f9b4dbed30ed4479eeb497846ab1e5ce1c86efabe005c0c8e)

Default empty

Add notes

Additional files uploaded

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2d6a092f1c29cbf7ccefad?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e8ece3a802bb1c0d6a3f66d88376e08b05eb6daca24aad37141f5d294c8c4862)

Hover empty

Add notes

Additional files uploaded

![Active empty (Web only)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ddaa2e6691127c4d3b803f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=757ccc28ee27d4ef94b6a91098a3f39a436814546c5adc7e033287038b85c237)

Active empty (Web only)

Add notes

Additional files uploaded

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a4af2e21329813700d77c3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=51f65e51d8137cda66d86849dbc400c015b200123964bcf563b6847c5109efd8)

Disabled empty

Add notes

Additional files uploaded

  

**Error**

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/094ba96cd4e550bee56d82?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7b6c35481df1a22bb1afbc2bdb5312916386a7399ad0639cdeeeadc0b045b999)

Default empty

Add notes

First upload

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/171e138ab8c7c6bec30e31?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5563f5af1e1b874504bc52c34b425bfb286ae3fc76ac5f718758c82da4c53cab)

Hover empty

Add notes

First upload

![Active empty (Web only)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/029eca1d9c3c535e1e671b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a13f61da0ff7a65b525c5067620f94b2dd446f242f128ec341db4b6d57abffbd)

Active empty (Web only)

Add notes

First upload

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/28a80ef1d0ce10e3ed37f5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=33c17e1289a793e78fb49dbb718b0a624ac36eccdd73929865036a85460d8c62)

Disabled empty

Add notes

First upload

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/01ffc12ece62b3d86ef020?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7d58e0988b1c3c373b7d53b63e96e500b23075e163a1158e990f3e72aa90b328)

Default empty

Add notes

Additional files uploaded

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2aabcfbb942cc6e75b7290?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fecc9ba47696f2f278a5d89e53dcc0346a0643e4b8612f56d5cfc25b71b5abd7)

Hover empty

Add notes

Additional files uploaded

![Active empty (Web only)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/13d7ad6a36af06f54d1adf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2b987825cace01047b5fb222c2463f066a15637aed8d258f8b7030dd76468c70)

Active empty (Web only)

Add notes

Additional files uploaded

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/945298e13c73bd6a0b0c18?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=047ad3407bba10a121b249c7c873d81ad1fa18c428924bac38194e60c674d18f)

Disabled empty

Add notes

Additional files uploaded

  

#### Filled with image

When the user uploads an image, a preview of that image is displayed. The image preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover, pressed and disabled. And they can be in an error state. When in error state, they contain an error message.

The drag & drop indicator text (Drag images to rearrange order) is only displayed on web desktop.

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/128dd5be931f516c86532c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=53596f63e2d8a414d9ec1e7ddbc50019ba082646df716bbe9c9cb1911d05a8e1)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/319d4aa29266ab320a781f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28c31925bc59498a28b53806c0c4fea7481e8dd5d27dbc1c3478aa6e8432318b)

Hover filled

Add notes

![Pressed filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7ba6dc0434c2f4c21b372b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ccff269b58b2f256b5ac2a47b4c8e14bc668995805b759c560b52c3a84e1d56f)

Pressed filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/045626cf8769e8b21a4df4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ab01d02573a2a2ce30fa13bec029d447e48446046a88f6330997de32a8176977)

Disabled filled

Add notes

![Error filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/960bf8f50c98c4a926ee3c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ac60b89f098ddf2c9669651bb828c5c82726cc96cbf6fbb0a90eb0735272852)

Error filled

Add notes

**Object fit**

Consumers can choose the preview behavior of uploaded images.

![Cover (default)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/09be8f087c388905cc51aa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b64cef3cfcda78df8db53ccf4462ceb3f58bb7ee6c11dcee4276f712207081ff)

Cover (default)

Add notes

Makes the image fill the container entirely, cropping parts if necessary to maintain its aspect ratio.

![Contain](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a2010b622796b5d6bc54df?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c016e5810c9f413c925403510d46537908970881881e27f2660436c6b38f9cf1)

Contain

Add notes

Makes the whole image fit inside the container, keeping its aspect ratio but possibly leaving empty space

  

  

#### Filled with file

When the user uploads any other file (non-image), a generic file icon is displayed. The file preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover and pressed. And they can be in an error state. When in error state, they contain an error message.

The drag & drop indicator text (Drag images to rearrange order) is only displayed on web desktop.

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/af71a7fc363743bc2a6dfc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d1a205eb14612c85d4109d12671b7ed4b82cc4ae8ca09b4515e941fbbeb2cb5)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/49941ef241cca8f4ca1c5e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f5514f3e6fe7e9811d01980d08895394bd7bdf832204a3e5e9d56e6b01801f5b)

Hover filled

Add notes

![Pressed filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/478d4e164609813a769422?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=426efae65c2c08d13cc50d6445240e83f3467c3e37f4f4f41253833f35cc4367)

Pressed filled

Add notes

![Error filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/960bf8f50c98c4a926ee3c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ac60b89f098ddf2c9669651bb828c5c82726cc96cbf6fbb0a90eb0735272852)

Error filled

Add notes

The disabled state is not currently available. If needed, please request it in [#gemini\_support](https://kugawana.slack.com/archives/C048JM75SAC).

---

  

### Loading

The loading state indicates to users that files are being uploaded and will appear shortly.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a994c59668710803348146?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=32923a800f13d71b0c14a061ce8e935ac22eccf19d925c65e311af58cc2a7853)

Add notes

---

  

### File upload

Users can upload files by dragging and dropping or by clicking on the drop zone. The allowed file type, file size, and number of files must be defined by the consumer. If an unsupported file is uploaded, an error is displayed.

![Uploading](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/c72799846c597ec3fa1857?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ae9fe93359ce81f403d4901c40f758ed5f73e9953f3cf72e9baf69ec7f1648de)

Uploading

Add notes

User uploads files by dragging and dropping or by clicking on the drop zone

![Loading](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/af9d91d1bb783322180c76?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=31c984ce3531d2ed59cc9b72f740e318e8eae6d50dbb78059bcdd12112a5a1cb)

Loading

Add notes

Files are uploading

![File preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/03b0934511da3790d8a2e4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=160f9658646f59d60e76783a3007b3025e8127d30d5fd371583267442a8e47c2)

File preview

Add notes

Files were successfully uploaded

![Uploading](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0900e0cc46ef1d5db2e036?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1fdd44fb78a7f3fccc5d4b767ca680bae51c45c14a68c84b428d6f5183e776c7)

Uploading

Add notes

User adds additional files

![Loading](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cbe776a8abec1380157270?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=be46b69e6f66e2d7942602add3a347e71f41ea56e662942f5ceaae9e7dd05f4b)

Loading

Add notes

Additional files are uploading

![File preview](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/17f8f866d170a656b8cfee?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=12103b476dd583fd4f40c18af886147db0f822db69117188f979c409f6ee5703)

File preview

Add notes

Additional files were successfully uploaded

![Error](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/bfc849e7ab25f3684158ea?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=985da5254616c03a35e249844594acddd4b185eed8506d0f06aebfc501c7302d)

Error

Add notes

An error is displayed if an unsupported file is uploaded

---

  

### Action menu

The user can access the following options from the action menu:

-   **Choose as cover**  
    Set the file as a cover. Any file type can be set as a cover.
    
-   **Move forward**  
    Moves the file one step forward. Alternatively, files can be dragged and dropped to any position.
    
-   **Move backwards**
    
    Moves the file one step backward. Alternatively, files can be dragged and dropped to any position.
    
-   **Edit caption**
    
    Opens a modal where the user can change the file name (caption).
    
-   **Edit image**
    
    Opens an external image editor.
    
-   **Remove**
    
    Deletes the file.
    
      
    

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/17f8f866d170a656b8cfee?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=12103b476dd583fd4f40c18af886147db0f822db69117188f979c409f6ee5703)

Add notes

---

  

### Breakpoints

The text and style of the empty drop zone depends on the breakpoint. On the desktop, the dashed border and text indicates that drag and drop is possible. On phones and tablets, this is much less common, so the design is adjusted to reflect the different behavior.

To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Tap](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7eac4c848283063478caf2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bf552c7b79bf4ec3624a974f14a86d811fcc85241c0984c59fa3e0eb47e46de4)

Tap

Add notes

Web: XXS to MD (0 - 1023 px)

Android and iOS: used on all breakpoints

![Drag and drop](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a4b09ec62d0f10521bb698?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4062def50ff8faace3ebe528cd7332429eeab7fdd992291a3bc445d6c30e40b7)

Drag and drop

Add notes

Web: LG to XXXL (> 1024 px)

Android and iOS: not used

---

  

### Size

The media upload cards adjust to the width of its container, filling the available space based on the size of the container. The width can be set to 100% (full-width) or 50% of the container. The cards have a fixed aspect ratio of 3:2.

  

---

  

## Content

#### Labels

Media uploads should always have a label, to help the user understand what files they are supposed to upload.

-   Keep the label short and concise (1-3 words) and in noun form.
    
-   Start with a capital letter and use no punctuation (including colons).
    

  

#### Helper text (optional)

Add helper text if the user needs assistance with uploading files, such as explaining the allowed file type, size, or number of files. It can also be used to explain the drag and drop feature of the file preview cards.

Use sentence-style capitalization and punctuation.

  

#### Error messages

See the UX Writing guidelines to learn about [error messages](https://zeroheight.com/626199550/p/4051b4-error-messages).

  

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).