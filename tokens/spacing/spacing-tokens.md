> **This page is evidence-based.** The **Used by** column lists the components
> that bind each token in `gsl-core-web-design-system`, generated from
> [spacing/spacing-usage-ledger.md](spacing-usage-ledger.md).
> Rules for generating UI: [spacing-rules-ai.md](spacing-rules-ai.md).
> Evidence: [spacing-usage-audit.md](spacing-usage-audit.md).
>
> **"No component" does not mean unused.** `Spacing/48`–`256` are page-rhythm
> tokens applied by product pages outside the component library — the fact that
> no component binds them is the rule working, not a gap. See below.

Spacing is brand-independent — the same 17 tokens resolve to the same values for
every brand and both modes. It is the correct and only source for spacing (as it
is for radius and border width). All spacing tokens are published.

*(The earlier wording called this the "`Primitive` architectural tier". That term
appears nowhere in the code repo — it is presumably Figma variable-collection
naming. The structural claim it made is true and is restated above without the
unverifiable label.)*

## Overview

*Which layer a spacing decision falls into — see Semantic usage below for the specific token.*

| Layer | Use for |
| --- | --- |
| Micro spacing | Inline micro-arrangements within atomic components and tight groupings |
| Container internals | Assembling custom cards, disclosure panels, sheets, or container blocks |
| Layout composition | Auto-layout gaps, flex gaps, and structural offsets between sibling components |
| Page rhythm & viewport margins | Major section separation, hero banners, and outer canvas margins |

## Semantic usage

| Token | When to use |
| --- | --- |
| `Spacing/2` | Hairline spacing, badge edge adjustments, sub-pixel alignment offsets |
| `Spacing/4` | Inline icon-to-text spacing (compact), tag vertical padding, list item counters |
| `Spacing/6` | Intermediate micro gaps, compact status badges, avatar group overlaps |
| `Spacing/8` | Standard icon-to-label gap, badge horizontal padding, checkbox/radio label gap |
| `Spacing/12` | Compact container padding — dropdown items, tooltips, compact mobile list cells |
| `Spacing/16` | Standard internal padding on Mobile (XS–SM); content flow gap between title and body; vertical gap between consecutive form fields; gap between inline filter chips |
| `Spacing/20` | Generous internal padding; spacing above a card's action footer row |
| `Spacing/24` | Standard internal container padding on Desktop (MD–XXXL); standard grid gutter; horizontal and vertical gap between cards in search results |
| `Spacing/32` | Separation between distinct card clusters; structural gap between sidebar and main rail |
| `Spacing/40` | Extended separation between independent form sections or preview panels |
| `Spacing/48` | Vertical section rhythm on Mobile/Tablet (XS–LG) between major content sections — **page-level only** |
| `Spacing/56` | *No documented use.* No component binds it and no page-rhythm table references it — the one token in the scale with no stated purpose |
| `Spacing/64` | Vertical section rhythm on Desktop (XL–XXXL) between major page sections — **page-level only** |
| `Spacing/80` | Hero section breathing room; outer horizontal viewport margin for XL+ tiers — **page-level only** |
| `Spacing/128` | Extended hero banner offsets; editorial landing section buffers on desktop — **page-level only** |
| `Spacing/256` | Display marketing transitions — used selectively for high-impact landing canvases — **page-level only** |

*`Spacing/None` has no dedicated usage note — it's the explicit zero-gap reset.*

## Applied patterns

*Multi-token combinations for common containers and layouts — not single-token lookups, so kept separate from Semantic usage above.*

### Container padding

| Container type | Mobile (XS–SM) | Desktop (MD–XXXL) |
| --- | --- | --- |
| Listing / product card | `Spacing/16` | `Spacing/24` |
| Dropdown / popover panel | `Spacing/12` | `Spacing/16` |
| Modal / dialog body | `Spacing/16` | `Spacing/24` to `Spacing/32` |
| Embedded filter box | `Spacing/16` | `Spacing/16` |

### Page rhythm by viewport tier

| Viewport tier | Outer margin | Section gap | Card grid gap | Form field gap |
| --- | --- | --- | --- | --- |
| XS / Mobile | `Spacing/16` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| SM / Tablet portrait | `Spacing/32` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| MD–LG / Tablet landscape | `Spacing/32` | `Spacing/48` | `Spacing/24` | `Spacing/16` |
| XL–XXXL / Desktop | `Spacing/80` | `Spacing/64` | `Spacing/24` | `Spacing/16` |

*Outer margin and grid gutter values here must match the [Grid tokens](../grid/grid-tokens.md) `Margin`/`Gutter` columns for the same tier — this table exists to map those to their `Spacing/*` token equivalents.*

## Rules

*The first and third rules below were checked mechanically against all 60
component token files — **both hold, with zero violations**. See
[spacing-usage-audit.md](spacing-usage-audit.md).*

- Never hardcode a pixel literal (`margin="15px"`, `gap="10px"`) — every spacing value must resolve to a `Spacing/*` token.
- Don't invert containment: a gap between inner elements shouldn't exceed the padding of the card containing them. **Verified: 0 violations across the 24 components that have both.**
- Don't apply page-rhythm tokens (`Spacing/48`, `56`, `64`, `80`, `128`, `256`) inside individual components or cards — those are for macro layout only. **Verified: 0 violations across 60 component files.**
- Don't override a pre-built design-system component's internal padding via CSS — use the component's default.

## Tokens (17)

| Token | px | Components | Used by |
| --- | --- | --- | --- |
| `Spacing/None` | 0 | 3 | `button`, `carousel`, `stateMessage` · direct: `Accordion`, `Autocomplete` |
| `Spacing/2` | 2 | 5 | `datePicker`, `feedbackMessage`, `tag`, `toggle` +1 · direct: `DateCalendar` |
| `Spacing/4` | 4 | 23 | `actionMenu`, `avatar`, `badge`, `button` +19 · direct: `Button`, `MediaUpload` |
| `Spacing/6` | 6 | 4 | `button`, `chip`, `datePicker`, `slider` · direct: `DateCalendar`, `ImageSlider` |
| `Spacing/8` | 8 | 36 | `accordion`, `actionMenu`, `button`, `buttonBar` +32 · direct: `Button`, `Carousel` |
| `Spacing/12` | 12 | 14 | `actionMenu`, `button`, `checkbox`, `chip` +10 · direct: `Checkbox`, `Dropdown` |
| `Spacing/16` | 16 | 27 | `accordion`, `actionMenu`, `button`, `buttonBar` +23 · direct: `Autocomplete`, `CoachMark` |
| `Spacing/20` | 20 | 1 | `slider` |
| `Spacing/24` | 24 | 4 | `infoState`, `modal`, `selectCardGroup`, `snackbar` |
| `Spacing/32` | 32 | 9 | `buttonBar`, `feedbackMessage`, `imageSlider`, `infoState` +5 · direct: `DateCalendar`, `MediaUpload` |
| `Spacing/40` | 40 | 0 | direct: `CoachMark`, `unsafe` |
| `Spacing/48` | 48 | 0 | **no component** |
| `Spacing/56` | 56 | 0 | **no component** |
| `Spacing/64` | 64 | 0 | **no component** |
| `Spacing/80` | 80 | 0 | **no component** |
| `Spacing/128` | 128 | 0 | **no component** |
| `Spacing/256` | 256 | 0 | **no component** |
