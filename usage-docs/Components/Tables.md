<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3492184533/Tables | Last modified: Aug 25, 2026 -->

# Tables

Tables are used to organize and display all information from a data set. Display, organize, and sort data for users to analyze and take action on.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1221ee7f-2fd5-4e41-9649-aa7d54905ca7&&collection=contentId-3492184533&height=682&occurrenceKey=null&width=2505&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | In progress 🚧 | To do 🚧 | To do 🚧 |

[Tables in Figma](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?m=auto&node-id=7816-62373&t=NvnSmro4NrlL31fg-1)

---

## Usage

Table component is essential for displaying large volumes of structured information in an organized, grid-like format, making it ideal for use cases where users need to compare, sort, and analyze data efficiently. It is best suited for scenarios involving datasets with multiple attributes, where clarity and accessibility are paramount. Utilize this component when you need to present data in a way that empowers users to derive insights quickly and make informed decisions based on comprehensive, easy-to-navigate information.

### Anatomy

There are a few types of Tables, but the primary elements that constitute the Table component are as follows:

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5f4d5a14-f850-4971-81fa-1703395a8d67&&collection=contentId-3492184533&height=685&occurrenceKey=null&width=928&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| Sub-component | Enable/Disable capability | Padding |
| --- | --- | --- |
| Header row | Yes | Left, Right: 12px, 16px, 20px |
| Header cell | Yes | Left, Right: 12px, 16px, 20px |
| Sorting button | Yes | N/A |
| Additional info button | Yes | N/A |
| Table row | N/A | Top, Down, Left, Right: 12px, 16px, 20px |
| Table cell | Yes | Left, Right: 12px, 16px, 20px |
| Footer | Yes | Left, Right: 0px, 16px |
| Footer Legend | Yes | N/A |
| Pagination | Yes | N/A |

### Padding options

The set of spacing available for this component is limited as we've documented in the [Anatomy of the component](https://zeroheight.com/626199550/p/851561-tables/t/485e6cc329). You can combine a set of 12, 16 and 20px spacing units. Just make sure the spacing is balanced and consistent throughout the table.

#### Example

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=bda31e8b-64f9-4525-9a60-f65c00f7ef94&&collection=contentId-3492184533&height=87&occurrenceKey=null&width=729&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
12px gap between cells in the Header

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b59f8d63-ba5d-46b4-81a8-ebe0ff9958c4&&collection=contentId-3492184533&height=125&occurrenceKey=null&width=720&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
12px gap between fixed cells and the rest

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6c1be857-4497-4d72-a778-cf9896a9f0ca&&collection=contentId-3492184533&height=126&occurrenceKey=null&width=691&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
12px gap between cells and 16px padding top and bottom of the row

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e2899d57-ff3e-4167-b424-6462c12548bc&&collection=contentId-3492184533&height=110&occurrenceKey=null&width=161&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Other padding can be used within the cell content. E.g.: 8px

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

* **Left-align text columns:** Everything that's made up of letters should be left-aligned.
* **Match heading alignment to column:** Column headers should always align according to their column content. Not following this rule creates off putting whitespaces and brings in unnecessary visual noise.
* **Avoid using center alignment:** Using the right alignment for the right type of content is key for enhancing the user's readability, mental calculations and comparisons between rows. Center alignment prevents quick scanning and noticing irregularities and ultimately makes the eye jump around unnecessarily.
* **Avoid duplication:** When possible, avoid repeating the title in every cell of a given column. For example, you can omit repeating the word "lead" in every cell like "Qualified Lead" or "Nurturing Lead". Placing the word "Lead" in the heading and just using qualifiers in the rows will help reduce visual noise.
* **Right-align numeric columns when standalone:** When numbers are the only value within a column, unlike text, numerical values are much easier to compare and contrast when they're right-aligned. The goal is to align numbers according to the position of the decimal.
* **Vertical alignment:** Use vertical center-align for when the row height varies only slightly (up to 3 lines). If row height varies more than 3 or 4 lines, using top-alignment makes most sense in terms of legibility and ensuring everything is visible.

Follow our Gemini content guidelines for [numbers](https://zeroheight.com/626199550/p/60fe5b), [dates](https://zeroheight.com/626199550/p/06ce3b-date-and-time) and [capitalization](https://zeroheight.com/626199550/p/437aef-capitalization).

### Related Components

Not documented

---

## Variants & Modifiers

Table variants are either Device or Feature driven so it adapts to different use cases:

* **Device:** Desktop, Phone/Tablet
* **Selectable rows:** Functionality to enable rows that can be selected individually or in bulk from the Header
* **Expandable rows:** Functionality to enable rows that can be expanded thanks to a button so it displays a bigger panel with more contextual data
* **Horizontal scroll:** Functionality to enable data sets within columns to overflow the Table container and scroll horizontally
* **Full width (Phone/Tablet only):** Reserved for Phone and Tablet devices — to maximize screen real estate the Table component gets "unboxed" so it can be expanded to the full width of the screen

### Device

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f05a438f-eb61-4b24-ab66-a1c984f54034&&collection=contentId-3492184533&height=492&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
There is a Desktop and a Phone/Tablet version of the Table

Tables for mobile devices have two ways of presenting the data within the rows:

| Horizontally distributed | Stacked |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=20eefb93-4952-4980-89de-0fd10747fa1b&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e92d0168-63a9-4cd2-8a22-8fb55dd0ed59&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

But also can be aligned to the full-width of the device, making the most out of the available space:

| Horizontally distributed full-width | Stacked full-width |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9a801c26-e3bb-405c-863c-4bd07e8ccd87&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=85953a22-d104-4d08-b796-69108b68a666&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

#### Phone / Tablet Guidelines

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a81315f5-8aa6-4390-a752-c850eb1c0d4b&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Tables can have the same appearance as on Desktop devices, having a boxed Table as one of our Phone/Tablet views. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7e92d908-1c3f-40a5-a5c9-a2bd8883b2c4&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** To make the most out of the space on the screen, mobile device Tables can be aligned to the full-width of the screen. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=43dcdade-d926-4ad8-bdb3-d3f4f912581b&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** As normally the content of the tables won't fit in smaller devices, besides scrolling horizontally to display more data, optionally you can stack the content of a whole row vertically. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=235699a2-5b68-465f-b01f-3dbd2d00bc14&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Also expand the Table to the full-width for better readability. |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5f0fd842-c232-4581-86dc-f27488a73e71&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When using the full-width Table for mobile devices, make sure that in case you have the footer, you must have the padded version. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3030c22b-98f2-4083-a86a-917427f134d4&&collection=contentId-3492184533&height=780&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** You can't combine the stacked row view with the horizontal scroll. |

### Selectable rows

To facilitate the selection of rows you can implement the selectable rows variant.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ec229f3f-cd70-4c86-bcd3-ad88af4c55ef&&collection=contentId-3492184533&height=492&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=952f38ff-939a-4b4c-84d9-0bb7176df2ae&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When adding the functionality of selecting rows in a table, it is implemented to all rows by default. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=16855453-59a0-42c3-a266-b8249724af2e&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** The Header of the table should have a Checkbox to facilitate selecting/unselecting all rows — don't randomize the functionality of selecting rows in a table, without context users won't be able to understand why some rows can be selected and others don't. |

### Expandable row

You might need rows that can expand in order to show and hide contextual data. For this purpose you can use the Expandable row variant, which is NOT available for mobile Tables as the interaction of this type of row might be difficult to interact with on smaller devices.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=96f86ed4-ce46-4bd2-9901-34874dc8ed9b&&collection=contentId-3492184533&height=492&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f1e74a2a-9a5e-42a0-8431-bfc85288fa32&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When adding expandable rows, try to have the same functionality for all rows. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=d1c3a05b-0ec1-48ad-b520-3b3b44e5f7bc&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Without context, users might not know why some rows can't be expanded. Only mix the functionality when you know why. |

### Horizontal scroll

For very complex data sets that need a large number of columns to display, this variant allows the content of the rows to overflow the container — a shadow on the edges appears to depict the overflowing content.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=23b51877-f233-4f2d-ad8d-c7ada35b9414&&collection=contentId-3492184533&height=492&occurrenceKey=null&width=1200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dd3aec64-b3d4-4745-956a-4a372a597676&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** When the content of the Table can't be fitted inside the Table container, enable "horizontal scroll" — a shadow will appear to help the user notice there's more content underneath. |

### Modifiers

#### Sorting

Sorting helps users order the data on the Table based on that column's values, from highest to lowest or from lowest to highest. Clicking the sorting button first sorts highest to lowest, clicking again sorts lowest to highest, and clicking a third time returns to the default sorting. This functionality and the icon that enables it can be disabled and hidden.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b908874f-a73f-40bf-83a1-6dfa057f149f&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Sorting and info features enabled

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=30ec49cc-8258-4f33-9687-a1c6a82b541f&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Sorting icon changes depending on the sorting direction

#### Info

The info icon gives contextual information about the data visible in that column. Just like any other info icon across the product, on hover or tap (mobile) it displays a tooltip with additional information. This functionality and the icon that enables it can be disabled and hidden.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=53d787f6-d170-4ca0-aa6e-39f6384dc0ef&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Activating the info icon displays a tooltip

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=3fc6bf92-7c2b-4a3c-b6d0-c2a081efaff6&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Both features can be disabled

#### Header placement

| DO | DON'T |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=258489a3-fb56-4648-aad2-9c73e7ab0375&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** Keep the Header at the top of the Table. | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5e05da55-ee92-4127-9fa6-0bc7ee3716bb&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** Don't place the Header in between rows. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9b8f16de-8299-4845-aeb6-d0560997d7b4&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Alternatively you can have a Table without a Header. Use it carefully — Tables without a header are reserved for simple tables where each column's data point can be understood by the user without context. |

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Loading

When a Table component takes some time to load its content, you can display a skeleton depicting the type of content the user will encounter, keeping the column amount and row amount. If the Headers can be displayed in advance, there's no need for a skeleton on the header of the Table.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7653016b-963b-47db-9e76-04d724ccb8a0&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
When the Table data is loading it will display a skeleton

#### Hover and Selected

Table rows can be selected independently and in bulk, so Table rows have different states to depict that interactivity. On Default state, Table rows use the `color-surface-default-default` color token.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=91659e61-8c16-456e-b8cc-42feb996fedd&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Hover state rows use the `color-surface-default-hover` color token

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=df9015ff-36e5-406e-b745-c0be742372af&&collection=contentId-3492184533&height=390&occurrenceKey=null&width=600&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
Selected state rows use the `color-surface-default-pressed` color token

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
