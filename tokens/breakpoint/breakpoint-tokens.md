The eight viewport tiers the design system targets, and how components consume them.

> **This page is evidence-based.** Consumption checked against
> `gsl-core-web-design-system`. Rules:
> [spacing-rules-ai.md](../spacing/spacing-rules-ai.md) (layout) ·
> [grid-tokens.md](../grid/grid-tokens.md) (column grid).

## How components use a breakpoint

**Breakpoints are not referenced as tokens.** No component writes
`"breakpoint.md"`. Instead every `Box` style prop accepts a **responsive
object** keyed by tier name:

```tsx
<Box padding={{ base: 'spacing.16', md: 'spacing.24' }} />
```

`mapStylePropsToCSSObject` (`libraries/core/src/Box/styles/index.ts`) walks those
keys, resolves each tier to its pixel value, and emits one
`@media (min-width: …)` block per tier.

Two consequences worth knowing:

- **`base` emits no media query.** It resolves to `0`, so its value is applied
  directly as the default and the other tiers layer on top. Always give `base`
  first.
- **Tiers are min-width, so they cascade.** A value set at `md` also applies at
  `lg`, `xl`, `xxl` and `xxxl` unless overridden. Only specify the tiers where
  something changes.

There is also `useBreakpointValue` in `core` for the cases where a value must be
read in JavaScript rather than expressed in CSS.

**In use by:** `ActionMenu`, `Autocomplete`, `Carousel`, `DatePicker`,
`MediaUpload`, the chart components, and `useBreakpointValue`. All eight tiers
are exercised. Most components never need a responsive prop — they size
intrinsically and let their container do the work, which is why this list is
short.

## Viewport ranges

| Tier | Range | Media query |
| --- | --- | --- |
| **base** | 0 to 359 px | none — applied directly |
| **XS** | 360 to 599 px | `min-width: 360px` |
| **SM** | 600 to 767 px | `min-width: 600px` |
| **MD** | 768 to 1023 px | `min-width: 768px` |
| **LG** | 1024 to 1279 px | `min-width: 1024px` |
| **XL** | 1280 to 1535 px | `min-width: 1280px` |
| **XXL** | 1536 to 1919 px | `min-width: 1536px` |
| **XXXL** | 1920 px & more | `min-width: 1920px` |

`base` is code-only, with no design-tool equivalent — an intentional complement
below XS, not part of the seven-tier design system.

## Tokens

Code ships **one value per tier** — the min-width threshold above. Figma models
the same tiers as five variables per tier, of which only the width is importable:

| Figma variable | XS | SM | MD | LG | XL | XXL | XXXL | In code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Breakpoint/Width` | 360 | 600 | 768 | 1024 | 1280 | 1536 | 1920 | **yes** — the media-query threshold |
| `Breakpoint/Min width` | 360 | 600 | 768 | 1024 | 1280 | 1536 | 1920 | alias of Width |
| `Breakpoint/Max width` | 599 | 767 | 1023 | 1279 | 1535 | 1919 | 7680 | no — design spec only |
| `Breakpoint/Height` | 640 | 962 | 1024 | 768 | 720 | 864 | 1080 | no — design spec only |
| `Breakpoint/Min height` | 640 | 962 | 1024 | 768 | 720 | 864 | 1080 | alias of Height |

`Min width` and `Min height` are aliases, so their values always match `Width`
and `Height`. They exist for auto-layout constraints, not as separate data.

Code values verified against `shared/figma/breakpoints.json` and
`shared/breakpoints.json` (`base`).
