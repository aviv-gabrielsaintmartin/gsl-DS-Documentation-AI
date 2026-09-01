# Tables · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

# Tables

Tables are used to organize and display all information from a data set. Display, organize, and sort data for users to analyze and take action on.

**Web:** In progress │ **iOS:** To do │ **Android:** To do

![](/uploads/0rDon-JZve3x_5TApwfbyA.png)

-   [
    
    Tables in Figma
    
    
    
    
    
    ](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?m=auto&node-id=7816-62373&t=NvnSmro4NrlL31fg-1 "https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?m=auto&node-id=7816-62373&t=NvnSmro4NrlL31fg-1")

## Usage

Table component is essential for displaying large volumes of structured information in an organized, grid-like format, making it ideal for use cases where users need to compare, sort, and analyze data efficiently. It is best suited for scenarios involving datasets with multiple attributes, where clarity and accessibility are paramount. Utilize this component when you need to present data in a way that empowers users to derive insights quickly and make informed decisions based on comprehensive, easy-to-navigate information.

  

---

  

## Anatomy

There are a few types of Tables, but the primary elements that constitute the Listing card component are as follows:

![](/uploads/x_TXX02RB_7Va9U24CIHcg.svg)

**Sub-component**

**Enable/Disable capability**

**Padding**

Header row

Yes

Left, Right: **12px, 16px, 20px**

Header cell

Yes

Left, Right: **12px, 16px, 20px**

Sorting button

Yes

N/A

Additional info button

Yes

N/A

Table row

N/A

Top, Down, Left, Right: **12px, 16px, 20px**

Table cell

Yes

Left, Right: **12px, 16px, 20px**

Footer

Yes

Left, Right: **0px, 16px,**

Footer Legend

Yes

N/A

Pagination

Yes

N/A

  

---

  

## Variants

Table variants are either Device or Feature driven so it adapts to different use cases:

-   **Device**: Desktop, Phone/Tablet
    
-   **Selectable rows**: Functionality to enable rows than can be selected individually or in a bulk from the Header
    
-   **Expandable rows**: Functionality to enable rows that can be expanded thanks to a button so it displays a bigger panel with more contextual data
    
-   **Horizontal scroll**: Functionality to enable data sets within columns to overflow the Table container and scrolling horizontally
    
-   **Full width\* (Phone/Tablet only)**: This functionality is reserved only for Phone and Tablets devices as in order to maximize the screen real estate the Table component gets "unboxed" to it can be expanded to the full width of the screen
    

## Device

![There is a Desktop and a Phone/Tablet version of the Table](/uploads/LCyx8QoOEJo84AhKjvceFw.svg)

There is a Desktop and a Phone/Tablet version of the Table

Tables for mobile devices have two ways of presenting the data within the rows

![](/uploads/_YsTHgKXfLGgIAn8KlxOBA.svg)

Horizontally distributed

![](/uploads/YAX7hq_q0zPg8HA11Blw_g.svg)

Stacked

But also can be aligned to the full-width of the device, making the most out of the available space

![](/uploads/Ko7MrVP0vUzFplLvk0dYWw.svg)

Horizontally distributed full-width

![](/uploads/iL9WsgLnWGLglDKXGB4akw.svg)

Stacked full-width

### Selectable rows

To facilitate the selection of rows you can implement the selectable rows variant

![](/uploads/4HKNkmiTi3gb44DcynCmVw.svg)

### Expandable row

You might need rows that can expand in order to show and hide contextual data, for this purpose you can use the Expandable row variant, which is **NOT available for mobile Tables** as the interaction of these type of rows might be difficult to interact with in smaller devices

![](/uploads/8WFVpkT8Y_IQQpCJ-0Nxcg.svg)

### Horizontal scroll

For very complex data sets that need a large number of columns to display it, there's this variant that allows the content of the rows overflow the container, in this variant a shadow on the edges appear to depict the overflowing content

![](/uploads/nGDgvL10dPWjIHJO1KY8vg.svg)

### Sample Table component

---

  

## Heders

The table headers come with two features: **Sorting and Info**

  

Sorting feature helps users to order the data on the Table based on that column values from highest value to lowest or from lowest to highest.

When clicking the sorting button it first displays and changes to highest to lowest value, clicking again changes from lowest to highest and clicking a third time it goes back to the default sorting

This functionality and the icon the button that enables it can be disabled and hidden

![](/uploads/QgXzBbW0TZkeMMzC42P78w.svg)

Sorting and info features enabled

![](/uploads/RH1YSbCH6xggYF_fzhAV8Q.svg)

Sorting icon changes depending on the sorting direction

Info icon gives contextual information about the data that can be seen in that column. Just like any other info icon across the product, when on hover or tap on mobile, it displays a tooltip with additional information.

This functionality and the icon the button that enables it can be disabled and hidden

![](/uploads/-PWgOzQj0I6MjaLVoiM8Ww.svg)

Activating the info icon, displays a tooltip

![](/uploads/Um3pirW3epFwOHWrOyUEog.svg)

Both features can be disabled

---

  

## States

As an interactive element, Tables also have different states which affects the different rows individually

### Loading

![When the Table data is loading it will display a skeleton](/uploads/zBCgT8-TwjjRublJ_4cqlA.svg)

When the Table data is loading it will display a skeleton

When a Table component takes some time to load its content you can display a skeleton depicting what type of content the user will encounter, keeping the coulumn amount and row amount. If the Headers can be displayed in advanced then there's no need for a skeleton on the header of the Table

  

### Hover and Selected

Table rows can be selected independently and in a bulk. Therefore the Table rows have different states to depict that interactivity.

On Default state Table rows use the `color-surface-default-default` color token

![Hover state](/uploads/_qIdgm-bbuFsMswGvTO1wg.svg)

Hover state

Hover state rows use the `color-surface-default-hover` color token

![Selected state](/uploads/ZEHr3nSLFHRS61EKGGCW6g.svg)

Selected state

Selected state rows use the `color-surface-default-pressed`color token

  

---

  

## Padding options

The set of spacing available for this component is limited as we've documented in the [Anatomy of the component](https://zeroheight.com/626199550/p/851561-tables/t/485e6cc329).

You can combine a set of **12, 16 and 20px spacing units**. Just make sure the spacing is balanced and consistent throughout the table

### Example

![12px gap between cells in the Header](/uploads/_eAbmr7WRmMrO-ogUco5GA.png)

12px gap between cells in the Header

![12px gap between fixed cells and the rest](/uploads/MjDQBLJbpu0aOhJxEgSGHQ.png)

12px gap between fixed cells and the rest

![12px gap between cells and 16px padding top and bottom of the row](/uploads/w22S4PTrN3brsXl7LLTxcg.png)

12px gap between cells and 16px padding top and bottom of the row

![Other padding  can be used within the cell content. E.g.: 8px](/uploads/thHqALE35ga2w6LlJV1oTQ.png)

Other padding can be used within the cell content. E.g.: 8px

  

---

  

## Guidelines

### Headers

![](/uploads/bFGoywFVfrZHBZwHwcf3-Q.svg)

Do

Keep the Header at the top of the Table

![](/uploads/nkLvZ_mljPASg1oisdPVeg.svg)

Don’t

Don't place the Header in between rows

![](/uploads/46DJ-PfFn9jeJ1W2BJkfJA.svg)

Caution

Alternatively you can have a Table without Header. Use it carefully as Tables without header are reserved for simple tables where each column data point can be understood by the user without context

### Row types

![](/uploads/JUZB0o0rpovcH3tRVx-QVQ.svg)

Do

When adding the functionality The funtionality of selecting rows in a table it is implemented to all rows by defaults

![](/uploads/PQl3n-tPGrD6cSr1NxESfQ.svg)

Don’t

When adding the functionality of selecting rows, the Header of the tabel should have a Checkbox to facilitate the function of selecting and unselecting all rows Don't randomize the functionality of selecting rows in a table, without context users won't be able to understand why some rows can be selected why others don't

![](/uploads/jeFGkJ8iH5Eu_ep8kG1GJQ.svg)

Do

When adding expandable rows, try to have the same functionality to all rows

![](/uploads/QNqurQigj-HxhivAPpFVoQ.svg)

Caution

Without context, user might not know why some rows can't be expanded. Only mix the functionality when you know

![](/uploads/-QbNkckaNr8U8Qq8W0L8Cw.svg)

Do

When the content of the Table can't be fitted inside theTable container you can enable the "horizontal scroll" A shadow will appear to help the user that there's more content underneath

### Phone / Tablet devices

![](/uploads/z6WxrwdMcw81a5uXENrLiA.svg)

Do

Tables can have the same appearance as on Desktop devices, having a boxed Table as one of our Phone/Tablet views

![](/uploads/sNoWD8iXsHahxbzAx6pd-A.svg)

Do

But also, to make the most out of the space on the screen, mobile device Tables can be align to the full-width of the screen

![](/uploads/DL4tHZM-ssxZjIoJ1zv1sA.svg)

Do

As normally the content of the tables won't fit in the smaller devices, bedsides scrolling horizontally to display more data, optionally you can stack the content of a whole row vertically

![](/uploads/su0Rj0qwmtdABVm2k6SQ3w.svg)

Do

And also expand the Table to the full-width for better readability

![](/uploads/uE7cn0yV1LhypVQoQtd8KA.svg)

Don’t

You can't combine the stacked row view with the horizontal scroll

![](/uploads/t1P5ejGTOdXxzhhNR5f4Qg.svg)

Do

When using the full-width Table for mobile devices make sure that in case you have the footer you must have the padded version

  

---

  

## Best practices

Besides general Table guidelines you must also follow our own Gemini content guidelines for [numbers](https://zeroheight.com/626199550/p/60fe5b), [dates](https://zeroheight.com/626199550/p/06ce3b-date-and-time) and [capitalization](https://zeroheight.com/626199550/p/437aef-capitalization).

### Left-align text columns

Everything that’s made up of letters should be left-aligned

### Match heading alignment to column

Column headers should always align according to their column content. Not following this rule creates off putting whitespaces and brings in unnecessary visual noise

### Avoid using center alignment

Using the right alignment for the right type of content is key for enhancing the user’s readability, mental calculations and comparisons between rows. Center alignment prevents quick scanning and noticing irregularities and ultimately makes the eye jump around unnecessarily.

### Avoid duplication

When possible, avoid repeating the title in every cell of a given column. For example, you can omit repeating the word “lead” in every cell like “Qualified Lead” or “Nurturing Lead”. Placing the word “Lead” in the heading and just using qualifiers in the rows will help reduce visual noise.

### Right-align numeric columns when standalone

**When numbers the only value within a column**. Unlike text, numerical values are much easier to compare and contrast when they’re right-aligned. The goal here is to align numbers according to the position of the decimal. If you’ve properly formatted your data so that numbers all show the same amount of decimal digits, aligning them to the right of the cell is the most logical way to display them.

### Vertical alignment

Use **vertical center-align** for when the row height varies only slightly (up to 3 lines). Centering the text vertically within row height spreads out the white space within the table and thus eases visual scan.

If row height varies more than 3 or 4 lines, using **top-alignment** makes most sense in terms of legibility and ensuring everything is visible.