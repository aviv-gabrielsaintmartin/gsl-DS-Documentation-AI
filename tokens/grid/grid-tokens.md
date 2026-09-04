Column-grid setup per viewport tier — column count, outer margin, gutter, and the
column width they imply.

> **This page is evidence-based.** Consumption checked against
> `gsl-core-web-design-system`.

## Grid is not used by any component

**No component, and no component token, references a grid value.** A search of
`libraries/*/src` and all 60 component token files returns nothing.

That is expected rather than alarming: the column grid governs **page
composition**, which lives in the product codebases, not in the component
library. Components size intrinsically and fill whatever their container gives
them.

So this page describes a contract between **Figma and product teams**. An agent
generating a component should never reach for a grid value; an agent laying out a
*page* is working outside what this design system verifies.

**The earlier open question — whether a sanctioned grid layout system exists to
build against — is answered: it does not.** `Count`, `Margin` and `Gutter` are
defined values, not an implemented layout primitive. Using them today means
assembling a layout from raw numbers.

## Tokens

| Token | Importable | XS | SM | MD | LG | XL | XXL | XXXL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Grid/Count` | no | 4 | 8 | 8 | 8 | 12 | 12 | 12 |
| `Grid/Margin` | yes | 16 | 32 | 32 | 32 | 80 | 80 | 80 |
| `Grid/Gutter` | yes | 16 | 16 | 16 | 16 | 24 | 24 | 24 |
| `Grid/Width` | no | 70 | 53 | 74 | 106 | 71.33 | 92.67 | 124.67 |

`Count`, `Margin` and `Gutter` are defined in
`shared/figma/grids.json` and verified against it for all seven tiers.

### `Grid/Width` is derived, and now verified

`grids.json` has no `width` field — the doc's values were previously unverifiable
for that reason. They are in fact exact, and reproduce from the other three
tokens plus the breakpoint width:

```
column width = (viewport − 2 × margin − (count − 1) × gutter) ÷ count
```

| Tier | Viewport | Count | Margin | Gutter | Computed | Documented |
| --- | --- | --- | --- | --- | --- | --- |
| XS | 360 | 4 | 16 | 16 | 70.00 | 70 |
| SM | 600 | 8 | 32 | 16 | 53.00 | 53 |
| MD | 768 | 8 | 32 | 16 | 74.00 | 74 |
| LG | 1024 | 8 | 32 | 16 | 106.00 | 106 |
| XL | 1280 | 12 | 80 | 24 | 71.33 | 71.33 |
| XXL | 1536 | 12 | 80 | 24 | 92.67 | 92.67 |
| XXXL | 1920 | 12 | 80 | 24 | 124.67 | 124.67 |

All seven match. The fractional values at XL and above are the arithmetic, not an
approximation — do not round them into a `Sizing` token.

## Relationship to Spacing

`Grid/Margin` and `Grid/Gutter` must stay in step with the page-rhythm table in
[spacing-tokens.md](../spacing/spacing-tokens.md): the outer margin and card grid gap for a
tier are the same numbers expressed as `Spacing/*` tokens.

| Tier | `Grid/Margin` | `Spacing` equivalent | `Grid/Gutter` | `Spacing` equivalent |
| --- | --- | --- | --- | --- |
| XS | 16 | `Spacing/16` | 16 | `Spacing/16` |
| SM–LG | 32 | `Spacing/32` | 16 | `Spacing/16` |
| XL–XXXL | 80 | `Spacing/80` | 24 | `Spacing/24` |

These agree today. If one moves, move both.
