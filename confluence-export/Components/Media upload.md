<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450231/Media+upload | Last modified: Aug 26, 2026 -->

# Media upload

Media upload components allow users to upload, view, and manage media files such as images, videos and documents.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=182514261722&id=c0985ace-3da0-4b4d-aebf-258bcc1ed095&&collection=contentId-2831450231&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | To Do 🚧 |

* [Media upload on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7271)
* [Media upload on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-mediaupload--docs)

---

## Usage

Media upload components allow users to upload files by either dragging and dropping them or by clicking the drop zone.

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=e3d9bf075e52&id=986d8cb7-b60f-4c23-a3a8-1b099969e0da&&collection=contentId-2831450231&height=980&occurrenceKey=null&width=781&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Use the media upload to allow users to upload images, videos, or documents. |

### Related Components

Not documented

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, media uploads contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=bd2bad439e4d&id=5fe3a920-9f10-4d9e-9542-aa4a9958d96c&&collection=contentId-2831450231&height=329&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### Illustration

The empty drop zone contain a illustration placeholder. We recommend adding a pictogram.

**Figma tip**

To choose the correct illustration go the common page in the illustration library. For example: [Common Picto Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-249)

There you find illustrations for most use cases such as informative purposes, error messages, and more. If you can't find the illustration you're looking for please request it on #gemini_symbols.

[More information on the symbol library process](https://kugawana.slack.com/archives/C03HLJU6E3U/p1723193835245029)

#### File counter

The media upload includes an optional counter. In most cases, we recommend using the counter to give the user a clear idea of how many files they can upload.

| With counter | Without counter |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1570a0f0445c&id=81ceea70-fa9f-4f54-b8a7-4fcfc44c10c2&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=884cd62fb9e7&id=dd400c47-3676-4085-9cb9-057d7214c28c&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Filename

The image/file preview includes an optional filename. In most cases, we recommend displaying the filename to give the user more clarity about what files they can upload. Since the file preview (non-image) only displays a generic illustration, the filename will still be displayed below the icon even if the filename is hidden.

The default filename includes the file extension, e.g. bathroom.jpg. The filename (caption) can be changed using the action menu.

| With filename | Without filename |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8c902ced9795&id=13b44833-b99f-4c46-aa0a-05e1495c127b&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7fbce423cc8f&id=3eb1f998-989d-4a63-a133-8cfcda552979&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| With filename | Without filename |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=229783fe446e&id=3c75cb3f-0ead-4f65-b895-694f4af44ed0&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=acd93c015756&id=d7ca728b-201f-4bc7-951e-b2907f9e1c77&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Cover photo tag

The image/file preview includes an optional cover tag. This tag can be used to mark the cover image. The cover image can be changed in the action menu or by dragging and dropping an image to the first position. The tag can be applied to any type of file.

| With cover image tag | Without cover image tag |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=c65b8ab121b1&id=8cbecd3f-1aeb-48df-956e-940707de513a&&collection=contentId-2831450231&height=318&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=4a211a9fab7e&id=3603d724-551f-40ca-a977-992877698da9&&collection=contentId-2831450231&height=318&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Empty drop zone

Empty drop zones have the states default, hover, active and disabled. And they can be in an error state. When in error state, they contain an error message. Depending on whether it's the first upload or additional files are being uploaded, the icon and text inside the drop zone will change.

**Neutral — First upload**

| Default | Hover | Active (Web only) | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=843858325745&id=172bd48e-89fc-4d50-b221-b4abee58c832&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0c1f34b9f84d&id=35863456-1d25-456e-9f84-0426e1a87e24&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=9918153ecd78&id=0c93da84-75a7-4f7c-832a-1e05869c34f9&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f841ce983e82&id=ffa810c4-79a9-492a-bdc7-30dec8df842e&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Neutral — Additional files uploaded**

| Default | Hover | Active (Web only) | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3753085ee39b&id=49548a2d-c498-4b14-91af-223254ee4146&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b5d7904f44a3&id=69e8e46d-e181-4a4d-83c6-f2947ddb76d8&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=fed052c03c98&id=f2e5c37d-40ec-4b73-8111-455efbafa8fa&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=a99dfefff950&id=d64956ae-211c-4b2e-9e8c-4d339b5c1af0&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Error — First upload**

| Default | Hover | Active (Web only) | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0321b9ce822f&id=26ba26de-9538-43d4-83b2-5b4f8e6326cc&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=29360be2567e&id=e0ebfe43-9500-4078-975d-1b6cd836b6af&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=67d32b64a59b&id=fdaa17c2-dd2a-406a-b201-f3f2c90136c2&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=afc83bfd191b&id=fe88249a-e25a-4f15-a431-bb2dffdb953f&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Error — Additional files uploaded**

| Default | Hover | Active (Web only) | Disabled |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3f227d2d1104&id=8acca464-3953-49d2-b5fc-15f3bcdfc436&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=590eb4a41722&id=caa55899-aacf-4714-aa4e-552ce3d5c09e&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3ff28fedb920&id=4ad0409e-00e5-4349-85f4-605991a11f26&&collection=contentId-2831450231&height=365&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=bff5af678a4b&id=0bdd328c-d329-4b7f-b047-2dfc1c139212&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Filled with image

When the user uploads an image, a preview of that image is displayed. The image preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover, pressed and disabled. And they can be in an error state. When in error state, they contain an error message.

The drag & drop indicator text (Drag images to rearrange order) is only displayed on web desktop.

| Default | Hover | Pressed | Disabled | Error |
| --- | --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=17e8441c9130&id=c08e2023-1025-418e-8163-0c50b96fb048&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b728e4dde41a&id=336e760f-472e-41f9-913b-f7b704fb5bf0&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7c920856f957&id=d5bc7fa1-5a88-4e3d-a996-8bf79d64dd6c&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=50ea18d3360f&id=f2483db2-cec5-43a4-95cb-c4dbeb0d6479&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=f8807f631615&id=84f3e3f1-1451-47fe-aa8a-77d546f194de&&collection=contentId-2831450231&height=318&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

**Object fit**

Consumers can choose the preview behavior of uploaded images.

| Cover (default) | Contain |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=3856ad3b2ded&id=022f983d-2a0d-4ae7-a915-1378387e3edc&&collection=contentId-2831450231&height=267&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=04e655045aba&id=57682c81-55ae-45bb-bd92-552b56bbbbc7&&collection=contentId-2831450231&height=269&occurrenceKey=null&width=402&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

Cover: makes the image fill the container entirely, cropping parts if necessary to maintain its aspect ratio. Contain: makes the whole image fit inside the container, keeping its aspect ratio but possibly leaving empty space.

#### Filled with file

When the user uploads any other file (non-image), a generic file icon is displayed. The file preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover and pressed. And they can be in an error state. When in error state, they contain an error message.

The drag & drop indicator text (Drag images to rearrange order) is only displayed on web desktop.

| Default | Hover | Pressed | Error |
| --- | --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=dce1030eb57a&id=4d485fad-5789-458f-997a-a70fc06868f2&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=1af61c8a3e97&id=664774d5-07c0-4cb7-b68b-01958f177fa7&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=137ee07121e8&id=7aeac62a-f4ab-4016-94b3-3c9496620be2&&collection=contentId-2831450231&height=336&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=b6482fd76264&id=84f3e3f1-1451-47fe-aa8a-77d546f194de&&collection=contentId-2831450231&height=318&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

The disabled state is not currently available. If needed, please request it in [#gemini_support](https://kugawana.slack.com/archives/C048JM75SAC).

#### Loading

The loading state indicates to users that files are being uploaded and will appear shortly.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=d0f302c349de&id=3935de9f-0b9f-4c51-9c40-e9611f2135eb&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
#### File upload

Users can upload files by dragging and dropping or by clicking on the drop zone. The allowed file type, file size, and number of files must be defined by the consumer. If an unsupported file is uploaded, an error is displayed.

**First upload**

| Uploading | Loading | File preview |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=2c7da41133cf&id=05169897-3c26-4297-906a-68d0dbe33ac4&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7d2a8f14f448&id=573788aa-883b-4a52-aa11-1007e2c424df&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=7951183378d3&id=58443655-a2dd-4448-ba0a-20d4ea9274d7&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

User uploads files by dragging and dropping or by clicking on the drop zone. Files are uploading. Files were successfully uploaded.

**Additional files**

| Uploading | Loading | File preview |
| --- | --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=95e345f5a1dd&id=d7c32b30-73cd-4b38-8683-4f2ae4ab3438&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=d205d3868169&id=fc859da0-5d37-44f3-8ad0-f889e100db26&&collection=contentId-2831450231&height=663&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=963a397ea0b3&id=565283ee-4e99-4e99-880a-1549d33509a4&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

User adds additional files. Additional files are uploading. Additional files were successfully uploaded.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=a2797aa3155d&id=978dab4c-dead-4666-b4e5-7d926c657887&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
An error is displayed if an unsupported file is uploaded.

### Touch Target & Layout

* **Action menu:** The user can access the following options from the action menu: **Choose as cover** (set the file as a cover; any file type can be set as a cover), **Move forward** (moves the file one step forward; files can also be dragged and dropped to any position), **Move backwards** (moves the file one step backward), **Edit caption** (opens a modal to change the file name/caption), **Edit image** (opens an external image editor), **Remove** (deletes the file).
* **Width Adaptability:** The media upload cards adjust to the width of their container, filling the available space based on the size of the container. The width can be set to 100% (full-width) or 50% of the container. The cards have a fixed aspect ratio of 3:2.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=69f504bb3095&id=565283ee-4e99-4e99-880a-1549d33509a4&&collection=contentId-2831450231&height=661&occurrenceKey=null&width=394&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
### Breakpoints & Platform Adaptations

The text and style of the empty drop zone depends on the breakpoint. On the desktop, the dashed border and text indicates that drag and drop is possible. On phones and tablets, this is much less common, so the design is adjusted to reflect the different behavior. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web: XXS to MD (0 - 1023 px)** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=8f4ada0654dd&id=3c2fd9c8-1b92-4ce2-8eaa-b713d337169c&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Tap. Android and iOS: used on all breakpoints. |
| **Web: LG to XXXL (> 1024 px)** | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=45fbd3ad90b3&id=172bd48e-89fc-4d50-b221-b4abee58c832&&collection=contentId-2831450231&height=343&occurrenceKey=null&width=400&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Drag and drop. Android and iOS: not used. |

---

## Content & UX Writing

* **Labels:** Media uploads should always have a label, to help the user understand what files they are supposed to upload. Keep the label short and concise (1-3 words) and in noun form. Start with a capital letter and use no punctuation (including colons).
* **Helper text (optional):** Add helper text if the user needs assistance with uploading files, such as explaining the allowed file type, size, or number of files. It can also be used to explain the drag and drop feature of the file preview cards. Use sentence-style capitalization and punctuation.
* **Error messages:** See the UX Writing guidelines to learn about [error messages](https://zeroheight.com/626199550/p/4051b4-error-messages).

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
