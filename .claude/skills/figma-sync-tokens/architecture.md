# Figma Variables Architecture

Cached copy of the Confluence page "Figma Variables Architecture" (space `ADS`, page `3417014414`), pulled 2026-08-26 when Confluence was dropped as this skill's runtime dependency. This is static background reading, not something the skill writes to — re-cache only if the token architecture itself changes.

## Source of truth

| | |
|---|---|
| Figma file | **GSL Foundations Library** |
| File key | `utQzIdpY7RaHMTmu068e5r` |
| Generated | 31 July 2026 |

Figma is authoritative for design-intent values. The code design system has its own dev-side adjustments, so a value here is the design intent, not a guarantee of what ships.

## Which collection each category comes from

**Colour never comes from `1 - Primitive`**, but spacing, radius and border width come from nowhere else.

| Category | Source |
|---|---|
| Colour | `3 - Brand` |
| Spacing, radius, border width | `1 - Primitive` |
| Breakpoints, grid | `4 - Breakpoint` |
| Typography | local **text styles** (not variables) |
| Shadows | local **effect styles** (not variables) |
| Opacity, Motion, Z-Index | code only — no Figma source |

## Collections and modes

| Collection | ID | Modes |
|---|---|---|
| `3 - Brand` | `VariableCollectionId:31221:180246` | 6 brands |
| `2 - Mode` | `VariableCollectionId:31221:179784` | Light, Dark |
| `1 - Primitive` | `VariableCollectionId:31221:179629` | single `Value` |
| `4 - Breakpoint` | `VariableCollectionId:31221:179812` | 7 viewport sizes |
| `5 - Platform` | `VariableCollectionId:31221:180385` | Web, iOS, Android |

| Mode | ID |
|---|---|
| Brand: SeLoger | `35121:0` |
| Brand: SeLoger Neuf | `53696:0` |
| Brand: Logic Immo | `36957:3` |
| Brand: Logic Immo Neuf | `53803:0` |
| Brand: Belles Demeures | `52556:0` |
| Brand: Meilleurs Agents | `36978:4` |
| Appearance: Light | `31221:39` |
| Appearance: Dark | `31221:40` |

`2 - Mode` and `5 - Platform` are authoring layers — never read tokens from them directly. `5 - Platform` lets a designer switch a component's platform variant and has no code equivalent.

## Scope rule

**Any variable whose name contains 🔒 is excluded** from all documentation. These are component-scoped authoring internals, not consumable tokens. In `3 - Brand` that removes 294 of 515 variables, leaving 221.

Also deliberately excluded:

- The **401** `Color/*` primitives in `1 - Primitive` — raw ramps, hidden from publishing. Semantic colour comes from `3 - Brand`.
- Variables flagged hidden-from-publishing, which consumers cannot import even when documented (`Grid/Count` and `Grid/Width` are the two that still appear, marked as such).

## How brand and light/dark resolve

A colour token carries **one value per brand** in `3 - Brand`, and each of those is usually an alias into `2 - Mode`, which in turn aliases a raw value in `1 - Primitive`. So a single resolved colour is a three-hop walk:

```
3 - Brand [brand mode] → 2 - Mode [Light|Dark] → 1 - Primitive [Value] → #RRGGBB
```

Two consequences worth knowing before extracting anything:

- Setting the brand mode and the appearance mode on a frame is enough — Figma walks the rest. No extra variable import is needed for dark mode.
- When reading values programmatically, `figma_get_variables` resolves against the **default** mode of `2 - Mode`, which is Light. Dark values require walking the chain yourself with the mode pinned, or every dark value silently comes back equal to its light value.
