Text styles for all GSL products. Sizes and line heights in px. Apply these as
styles rather than setting font properties by hand.

> **This page is evidence-based.** The **Used by** column lists the components
> that bind each style in `gsl-core-web-design-system`, generated from
> [typography/typography-usage-ledger.md](typography-usage-ledger.md).
> Rules for generating UI: [typography-rules-ai.md](typography-rules-ai.md).
> Real-screen evidence and reasoning:
> [typography-usage-audit.md](typography-usage-audit.md).
>
> **"No component" does not mean unused.** Product pages set type directly and
> live outside the component library — `headline/28/bold` is the detail-page
> price on a real screen yet no component binds it. Read the column as "is this
> style available to you by using a component", not as "is this style alive".

## Brand theming

**The font family is the only thing that varies by brand — and it varies in
every one of the 32 styles.**

| Brand | Font family |
| --- | --- |
| BD | `Gotham` |
| LI | `Open Sans` |
| LIN | `Open Sans` |
| MA | `Poppins` |
| SL | `Cera SL sys` |
| SLN | `Cera SL sys` |

Every other property — size, weight, line height, letter spacing, case,
decoration — is **identical across all six brands**. The scale is universal; only
the typeface changes.

Never hardcode a family name. Bind the style token and let the theme resolve it.

## Overview

*Which family to use — see Semantic usage below for how the specific size within a family gets chosen.*

| Family | Use for | In components |
| --- | --- | --- |
| Display | **No component uses it.** Not observed on any sampled product screen either. If you reach for Display, you are outside every precedent in the system. | 0 of 6 styles |
| Headline | Section and module headers, and price-style primary numbers. In practice **bold only** — every `regular` headline weight exists solely for `avatar`'s initials. | 4 of 10 styles |
| Body | The default text family — titles, key facts, captions, labels alike, sized by local emphasis rather than hierarchy depth. | 7 of 16 styles |

## Semantic usage

*Bold vs Regular within any size is an emphasis choice, not a hierarchy signal.*

Token choice is **not** a fixed page hierarchy ladder — no H1→H5 mapping holds up
against real screens. Size is chosen per block, from two things: how prominent an
element must look next to its immediate neighbours, and how much room its
container has. There is no formula; for a component with no precedent elsewhere
this is a judgement call. See
[typography-usage-audit.md](typography-usage-audit.md) for observed pairings on
real screens.

### Underlines

There are **two** mechanisms, and the second is the one that scales:

| | Token | Effect |
| --- | --- | --- |
| A full underlined style | `body/16/regular underlined` | pins size *and* underline — used by `link`'s standalone variant |
| A decoration longhand | `typography.css.textDecoration.underline` | adds underline only, inheriting size and weight — used by `link`'s default variant |

The longhand is why **seven of the eight `underlined` styles have no consumer**:
an inline link inherits its surrounding size and only needs the decoration. Reach
for the longhand unless you specifically need to pin the size too.

Never apply underline decoration outside a link.

## Tokens

### Display (6)

| Style | Size | Line height | Weight | Decoration | Used by |
| --- | --- | --- | --- | --- | --- |
| `display/57/bold` | 57 | 64 | Bold | — | **no component** |
| `display/57/regular` | 57 | 64 | Regular | — | **no component** |
| `display/45/bold` | 45 | 52 | Bold | — | **no component** |
| `display/45/regular` | 45 | 52 | Regular | — | `avatar` — *sizing ramp only* |
| `display/36/bold` | 36 | 44 | Bold | — | **no component** |
| `display/36/regular` | 36 | 44 | Regular | — | **no component** |

### Headline (10)

| Style | Size | Line height | Weight | Decoration | Used by |
| --- | --- | --- | --- | --- | --- |
| `headline/32/bold` | 32 | 40 | Bold | — | `progressCircle` |
| `headline/32/regular` | 32 | 40 | Regular | — | `avatar` — *sizing ramp only* |
| `headline/28/bold` | 28 | 36 | Bold | — | **no component** |
| `headline/28/regular` | 28 | 36 | Regular | — | `avatar` — *sizing ramp only* |
| `headline/24/bold` | 24 | 32 | Bold | — | `progressCircle` |
| `headline/24/regular` | 24 | 32 | Regular | — | `avatar` — *sizing ramp only* |
| `headline/22/bold` | 22 | 28 | Bold | — | `accordion`, `infoState`, `loadingState`, `mediaUpload` +2 |
| `headline/22/regular` | 22 | 28 | Regular | — | `avatar` — *sizing ramp only* |
| `headline/20/bold` | 20 | 26 | Bold | — | direct: `unsafe` |
| `headline/20/regular` | 20 | 26 | Regular | — | **no component** |

### Body (16)

| Style | Size | Line height | Weight | Decoration | Used by |
| --- | --- | --- | --- | --- | --- |
| `body/16/bold` | 16 | 24 | Bold | — | `accordion`, `button`, `cellContent`, `datePicker` +12 · direct: `CoachMark`, `DateCalendar` |
| `body/16/bold underlined` | 16 | 24 | Bold | underline | **no component** |
| `body/16/regular` | 16 | 24 | Regular | — | `accordion`, `actionMenu`, `avatar`, `cellContent` +18 · direct: `Carousel`, `ImageSlider` |
| `body/16/regular underlined` | 16 | 24 | Regular | underline | `link` |
| `body/14/bold` | 14 | 20 | Bold | — | `badge`, `field`, `mediaUpload`, `rating` +3 |
| `body/14/bold underlined` | 14 | 20 | Bold | underline | **no component** |
| `body/14/regular` | 14 | 20 | Regular | — | `accordion`, `buttonGroup`, `cellContent`, `checkbox` +15 · direct: `ButtonGroup`, `CoachMark` |
| `body/14/regular underlined` | 14 | 20 | Regular | underline | **no component** |
| `body/12/bold` | 12 | 16 | Bold | — | `badge`, `datePicker`, `mediaUpload` · direct: `DateCalendar`, `SelectableList` |
| `body/12/bold underlined` | 12 | 16 | Bold | underline | **no component** |
| `body/12/regular` | 12 | 16 | Regular | — | `avatar`, `mediaUpload`, `slider`, `tag` · direct: `unsafe` |
| `body/12/regular underlined` | 12 | 16 | Regular | underline | **no component** |
| `body/11/bold` | 11 | 16 | Bold | — | **no component** |
| `body/11/bold underlined` | 11 | 16 | Bold | underline | **no component** |
| `body/11/regular` | 11 | 16 | Regular | — | `avatar` — *sizing ramp only* |
| `body/11/regular underlined` | 11 | 16 | Regular | underline | **no component** |

### Shared (1)

*Not brand-specific — a CSS longhand that inherits every other property.*

| Token | Effect | Used by |
| --- | --- | --- |
| `typography.css.textDecoration.underline` | `text-decoration: underline`, everything else inherited | `link` |
