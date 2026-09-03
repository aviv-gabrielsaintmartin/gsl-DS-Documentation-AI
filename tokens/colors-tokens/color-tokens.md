_Semantic colour tokens for all GSL products. This is the **only** source of colour for product UI — never take a raw colour value from anywhere else._

## Families

_Pick the family that matches what you're colouring, then open that page for its Overview (which token root), Semantic usage (which specific token), and Tokens (exact values) tables._

| Family | Use for | Page |
| --- | --- | --- |
| **Background** | The page/screen canvas — never for component fills | [Background](background.md) |
| **Surface** | Component fills — cards, buttons, inputs, sheets, and their interaction states. Start here for most product UI. | [Surface](surface.md) |
| **Border** | Strokes and outlines on components | [Border](border.md) |
| **Content** | Text and icon fills — bind all text colour to these, never hardcode | [Content](content.md) |
| **Symbols** | SVG/icon fills carrying brand identity, disabled-state icon fills, and illustration/avatar skin tones | [Symbols](symbols.md) |
| **Scale** | Energy Performance Class (DPE) labels and CO2 emission data visualisation — domain-specific, not general UI | [Scale](scale.md) |
| **Native** | iOS/Android platform-specific colours (ripple effects, splash screen) — never for web | [Native](native.md) |

## Brand theming

All six brands (SeLoger, SeLoger Neuf, Logic Immo, Logic Immo Neuf, Belles Demeures, Meilleurs Agents) share the same token structure and, for most tokens, the same resolved value. Only a small minority of tokens carry brand-specific colours — **21 of 221 tokens vary in Light mode, 23 in Dark** (the two sets differ slightly). Everywhere else, the value shown on a family's page is correct for all six brands.

The brand-varying tokens are concentrated in a few families: primary CTA fills (`Surface/Brand`), a handful of accent/active states, and text/borders that sit on top of a primary fill (`On-Primary`). Values shown throughout this space are for **SeLoger**, Light and Dark, as the reference brand.

Where a token varies by brand, its own page flags it in the Notes column and provides the full six-brand breakdown in a collapsed _"Brand variance"_ section directly below its token table — Light and Dark values, all six brands, one lookup, no need to leave the page. This page does not duplicate those values; go to the family page for the token you need.
