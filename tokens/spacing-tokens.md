Spacing belongs to the `Primitive` architectural tier, not the `Brand` tier — it is the correct and only source for spacing (as it is for radius and border width). All spacing tokens are published.

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
| `Spacing/48` | Vertical section rhythm on Mobile/Tablet (XS–LG) between major content sections |
| `Spacing/64` | Vertical section rhythm on Desktop (XL–XXXL) between major page sections |
| `Spacing/80` | Hero section breathing room; outer horizontal viewport margin for XL+ tiers |
| `Spacing/128` | Extended hero banner offsets; editorial landing section buffers on desktop |
| `Spacing/256` | Display marketing transitions — used selectively for high-impact landing canvases |

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

*Outer margin and grid gutter values here must match the [Grid tokens](grid-tokens.md) `Margin`/`Gutter` columns for the same tier — this table exists to map those to their `Spacing/*` token equivalents.*

## Rules

- Never hardcode a pixel literal (`margin="15px"`, `gap="10px"`) — every spacing value must resolve to a `Spacing/*` token.
- Don't invert containment: a gap between inner elements shouldn't exceed the padding of the card containing them.
- Don't apply page-rhythm tokens (`Spacing/48`, `Spacing/64`, `Spacing/80`+) inside individual components or cards — those are for macro layout only.
- Don't override a pre-built design-system component's internal padding via CSS — use the component's default.

## Tokens (17)

| Token | Value (px) |
| --- | --- |
| `Spacing/None` | 0 |
| `Spacing/2` | 2 |
| `Spacing/4` | 4 |
| `Spacing/6` | 6 |
| `Spacing/8` | 8 |
| `Spacing/12` | 12 |
| `Spacing/16` | 16 |
| `Spacing/20` | 20 |
| `Spacing/24` | 24 |
| `Spacing/32` | 32 |
| `Spacing/40` | 40 |
| `Spacing/48` | 48 |
| `Spacing/56` | 56 |
| `Spacing/64` | 64 |
| `Spacing/80` | 80 |
| `Spacing/128` | 128 |
| `Spacing/256` | 256 |
