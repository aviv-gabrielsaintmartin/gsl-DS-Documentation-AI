# Cards over Maps · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

Maps

# Cards over Maps

This is a guideline on how to deal with cards with different information when they are placed on a Map, where to place them depending on its context

![](/uploads/DiQHySpPcTFy-jS53BcJ4A.png)

## Usage

Our users interact with our maps for a variety of purposes, but their primary goal is to access relevant contextual information. The placement of information cards on the map plays a crucial role in ensuring users can easily interpret and compare the data accurately.

**Contextual information can be displayed within a card positioned in various areas of the map. Use the following guidelines to determine the most appropriate placement for these cards:**

## Desktop devices

### Next to pin

The Card component containing contextual information can be positioned next to the pin that triggered the interaction. **This placement works only when the map is not cluttered with multiple pins or interactive elements. In crowded scenarios, placing cards near multiple items can make interactions and comparisons more challenging, often requiring additional clicks to navigate effectively**.

![](/uploads/4mVZ0yy9oW_QhP6E9_VOwg.png)

Do

Place the contextual information in a card next to the active pin when the Map is not cluttered with multiple pins or interactive elements

![](/uploads/FB54_jIeDaBXRx4ui9TD6w.png)

Don’t

Avoid placing the contextual information card next to the active pin when the map is cluttered with multiple pins. In such cases, this placement can make it harder for users to compare information and interact with other elements effectively.

If the map is cluttered with pins and interactive elements, we recommend placing the contextual information card at the [bottom of the map, aligned to the center](https://zeroheight.com/626199550/p/9960c2-cards-over-maps/t/f5c5332442). This ensures clarity and minimizes interference with other elements on the map.

### Bottom middle

This placement is **recommended for cases where the map is crowded with pins and other interactive elements**. Positioning the contextual information cards at the bottom, aligned to the center, **helps to declutter the main interaction area of the map** while establishing a consistent pattern where users can reliably find contextual data during their interactions.

Due to its placement **when Cards are displayed on mobile maps, the main CTAs** until the user interacts with the map to not display any Car

![](/uploads/3dyLGqUJEuTDDTdWIrPXfw.png)

Do

When the Map is crowded with interactive elemnts we recommend to place the contextual information cards at the bottom, aligned to the center

  

#### Carousel

Regardless of the number of pins or interactive elements on the map, we recommend **always placing carousels at the bottom of the map**. This placement ensures seamless interaction with the carousel elements, especially when only one item is displayed at a time.

**The Cards inside a Carousel have a fixed width of 328px**

The Carousel takes the full width of the Map unless the entire amount of cards of the carousel fit in the width of the map, in that case the cards are aligned to the middle

Due to its placement **when Cards are displayed on mobile maps, the main CTAs and the map controls fade out** until the user interacts with the map to not display any Card

![](/uploads/O9dIwLObiuKrgSNv5P_RHg.png)

Do

Place Carousels at the bottom aligned to the center for a better interaction these cards width is fixed 328px

![](/uploads/v4yWHG6ajEby05qi8JCEOw.png)

Do

If the amount of cards inside the carousel can fit inside the full width of the Map then these cards, like standalone cards, are aligned to the middle without the need of cropping them

![](/uploads/sfJvAgwywEHDsKQt20ninQ.png)

Don’t

Avoid placing a carousel with an undefined width next to a pin. This can cause the cards within the carousel to occupy excessive space, disrupting the map experience and making it harder to interact with other elements on the map.

![](/uploads/YOPyz1LwDOVSobCDrlBTzw.png)

Don’t

Interacting with a carousel that displays only one element at a time can be challenging, especially when other interactive map elements are positioned behind the carousel.

## Mobile devices

### Bottom middle

Both cards and carousels **should be placed at the bottom center of the map**. This placement ensures easy interaction with the rest of the map and its interactive elements, especially given the varying screen sizes across devices and the often limited screen real estate.

The **width of the card should always occupy 100% of the screen** on mobile devices, regardless of the screen size. The card is designed to adapt to any mobile screen width while ensuring sufficient space remains for users to interact with other elements on the screen.

Due to its placement and, **when Cards are displayed on mobile maps, the main CTAs and the map controls fade out** until the user interacts with the map to not display any Card.

![](/uploads/Ytx7Nqn_vDXL4yQM7prqHA.png)

Do

Mobile Cards are place at the bottom, aligned to the center and scales to full width independently of the size of the mobile device

![](/uploads/C-PoByTRraUlwH8_FkCPqg.png)

Do

When Cards are displayed on the screen the main CTAs and the Map controls fade out to avoid interactive elements to overlap

![](/uploads/Shw76eoHe6Ho78zZapE-5w.png)

Don’t

Don't place the Card next to the pin, this way the interaction with the rest of elements becomes very difficult to interact with the map in small screens

![](/uploads/LNXrQoUVuPPgeiLUXGFagg.png)

Don’t

Don't set a fixed width to stand alone Cards on mobile

#### Carousel

Carousels contain multiple cards with contextual information and just like a standalone Card, on mobile devices should be aligned to the bottom and take the 100% width of the map  
  
**The Cards inside a Carousel have a fixed width of 328px**

Due to its placement **when Cards are displayed on mobile maps, the main CTAs and the map controls fade out** until the user interacts with the map to not display any Card.

![](/uploads/1_YLVT6WfPlGqNfSexML4g.png)

Do

Cards inside the carousel have a 328px fixed width and the carousel takes the full width of the map

![](/uploads/h5kDEgkxVIPPyvxM3TZc5A.png)

Do

When Carousels are displayed on the screen the main CTAs and the Map controls fade out to avoid interactive elements to overlap

![](/uploads/WO3LKpJfo2fhnRiEO6Tjkw.png)

Don’t

Don't align Carousels next to the interactive pin