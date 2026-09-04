Opacity multipliers (0–1) for fading elements and overlay washes. Code-only
primitive.

> **This page is evidence-based.** Consumption checked against
> `gsl-core-web-design-system`.

## Only three of the eleven are used

**No component token binds an opacity.** All use is direct in `.tsx`, and it
collapses to three values:

| Token | Value | Used by |
| --- | --- | --- |
| `opacity.none` | 0 | `Button`, `ImageSlider` — hiding an element while keeping its box |
| `opacity.50` | 0.5 | `CellContent` |
| `opacity.full` | 1 | `ImageSlider`, `Toggle` — restoring from a faded state |

**The eight remaining deciles — `10`, `20`, `30`, `40`, `60`, `70`, `80`, `90` —
have no consumer anywhere.**

That is a scale built for completeness rather than from need. Nothing is wrong
with it, but an agent should not read eleven evenly-spaced steps as eleven
sanctioned choices: the system uses opacity as an on/half/off switch, not as a
gradient.

**Prefer a colour token over an opacity.** Where the design system wants a
translucent *surface* it uses a colour with baked-in alpha
(`Surface/Transparent/*`, `Surface/Constant/Black/Transparent/*`), not an opacity
multiplier — because opacity fades an element *and all its children*, including
text, while an alpha colour fades only the fill. Reach for opacity only when the
whole element should fade together.

## Tokens (11)

| Token | Value | Used by |
| --- | --- | --- |
| `opacity.none` | 0 | `Button`, `ImageSlider` |
| `opacity.10` | 0.1 | **no consumer** |
| `opacity.20` | 0.2 | **no consumer** |
| `opacity.30` | 0.3 | **no consumer** |
| `opacity.40` | 0.4 | **no consumer** |
| `opacity.50` | 0.5 | `CellContent` |
| `opacity.60` | 0.6 | **no consumer** |
| `opacity.70` | 0.7 | **no consumer** |
| `opacity.80` | 0.8 | **no consumer** |
| `opacity.90` | 0.9 | **no consumer** |
| `opacity.full` | 1 | `ImageSlider`, `Toggle` |
