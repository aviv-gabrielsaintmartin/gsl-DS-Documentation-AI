_Semantic colour tokens for all GSL products. This is the **only** source of colour for product UI — never take a raw colour value from anywhere else._

## Families

_Pick the family that matches what you're colouring, then open that page for its Overview (which token root), Semantic usage (which specific token), and Tokens (exact values) tables._

| Family | Use for | Page |
| --- | --- | --- |
| **Background** | The page/screen canvas — never for component fills | [Background](background.md) |
| **Surface** | Component fills — cards, buttons, inputs, sheets, and their interaction states. Start here for most product UI. | [Surface](surface.md) |
| **Border** | Strokes and outlines on components | [Border](border.md) |
| **Content** | Text and icon fills — bind all text colour to these, never hardcode | [Content](content.md) |
| **Symbols** | SVG/icon fills carrying brand identity, disabled-state icon fills, and illustration/avatar skin tones. **Design-authoring only — not used in web code**, see [usage audit § C2](color-usage-audit.md) | [Symbols](symbols.md) |
| **Scale** | Energy Performance Class (DPE) labels and CO2 emission data visualisation — domain-specific, not general UI | [Scale](scale.md) |
| **Native** | iOS/Android platform-specific colours (ripple effects, splash screen) — never for web | [Native](native.md) |

## How a colour reaches a component

Components do **not** pick semantic tokens directly. A component-token layer sits
in between and holds every actual colour decision:

```
brands/<BRAND>/figma/colors.{light,dark}.json      218 semantic tokens
        │                                           (same keys in all 6 brands × 2 modes)
        ▼
shared/components/*.json                            60 files · 631 colour bindings
        │   component.toggle.color.borderHover
        │       = {color.border.interactive.hover}
        ▼
libraries/ui/src/*.tsx                              53 components
            borderColor="unsafe_component.toggle.color.borderHover"
```

This means the family pages below describe the *palette*, while the real usage
rules live one layer down. Two companion pages cover that layer:

- [color-rules-ai.md](color-rules-ai.md) — the rules to apply when generating UI
- [color-usage-audit.md](color-usage-audit.md) — what is actually bound where,
  which tokens are unused, and the verdict on every deviation

## Brand theming

All six brands (SeLoger, SeLoger Neuf, Logic Immo, Logic Immo Neuf, Belles Demeures, Meilleurs Agents) share the same token structure — the identical **218-key set** is defined in every brand and both modes. Only a small minority carry brand-specific colours: **21 of 218 tokens vary in Light mode, 23 in Dark** (the two sets differ slightly). Everywhere else, the value shown on a family's page is correct for all six brands.

> **AVIV is not a live brand — ignore it.** An `AVIV` token set ships in
> `libraries/tokens/src/brands/`, structurally identical to the six above. It is
> not in use and must not be documented, generated for, or counted as a brand.
> The extraction script excludes it by default.

The brand-varying tokens are concentrated in a few families: primary CTA fills (`Surface/Brand`), a handful of accent/active states, and text/borders that sit on top of a primary fill (`On-Primary`). Values shown throughout this space are for **SeLoger**, Light and Dark, as the reference brand.

Where a token varies by brand, its own page flags it in the Notes column and provides the full brand breakdown in a collapsed _"Brand variance"_ section directly below its token table — Light and Dark values, one lookup, no need to leave the page. This page does not duplicate those values; go to the family page for the token you need.
